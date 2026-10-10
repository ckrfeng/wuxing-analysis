"""Restore a retained source snapshot into repository work/ using verified bytes.

Snapshots exclude dependency, cache, compilation, and temporary-render files.
Archived source is data: this tool never executes it.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = ROOT / 'provenance' / 'snapshots'


def safe_relative(value):
    p = PurePosixPath(value)
    if p.is_absolute() or not p.parts or '..' in p.parts or '\\' in value:
        raise ValueError(f'Unsafe manifest path: {value!r}')
    return Path(*p.parts)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshot', nargs='?', help='ID from --list')
    parser.add_argument('--list', action='store_true', help='List retained snapshots')
    parser.add_argument('--verify-only', action='store_true', help='Verify stored content without restoring')
    parser.add_argument('--output', help='Destination inside repository work/; default work/restored/ID')
    args = parser.parse_args()
    index = json.loads((SNAPSHOTS / 'index.json').read_text())
    if args.list:
        for item in index:
            print(f"{item['id']}\t{item['file_count']} files\t{item['status']}")
        return
    if not args.snapshot:
        parser.error('Supply a snapshot ID or --list')
    entry = next((x for x in index if x['id'] == args.snapshot), None)
    if entry is None:
        parser.error('Unknown snapshot ID; use --list')
    manifest = json.loads((SNAPSHOTS / safe_relative(entry['manifest'])).read_text())
    work = (ROOT / 'work').resolve()
    output = Path(args.output).expanduser().resolve() if args.output else work / 'restored' / args.snapshot
    if output == work or work not in output.parents:
        parser.error('Restore destination must be a subdirectory of repository work/')
    records = []
    relative_paths = set()
    for row in manifest['files']:
        rel = safe_relative(row['original_relative_path'])
        if str(rel) in relative_paths:
            raise ValueError(f'Duplicate logical path: {rel}')
        relative_paths.add(str(rel))
        stored = ROOT / safe_relative(row['retained_destination'])
        if stored.is_symlink() or ROOT not in stored.resolve().parents:
            raise ValueError(f'Stored content escaped repository: {stored}')
        data = stored.read_bytes()
        if digest(data) != row['sha256']:
            raise ValueError(f'Stored hash mismatch: {stored}')
        target = output / rel
        if work not in target.resolve().parents or target.is_symlink():
            raise ValueError(f'Restore target escaped work/: {target}')
        if not args.verify_only and target.exists() and (not target.is_file() or digest(target.read_bytes()) != row['sha256']):
            raise FileExistsError(f'Existing file differs; choose an empty work/ destination: {target}')
        records.append((target, data, row['sha256']))
    if args.verify_only:
        print(f"Verified {len(records)} files for {args.snapshot}; no files written.")
        return
    for target, data, expected in records:
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            with target.open('xb') as fp:
                fp.write(data)
        if digest(target.read_bytes()) != expected:
            raise ValueError(f'Restored hash mismatch: {target}')
    print(f'Restored {len(records)} files into {output}')


if __name__ == '__main__':
    main()
