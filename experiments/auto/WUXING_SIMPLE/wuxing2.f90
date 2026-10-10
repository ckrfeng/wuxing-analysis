!------------------------------------------------------------------
! Wu-Xing simple homeostasis model (logistic, no Wu terms)
! Parameters:
!   PAR(1) = a   self-production rate
!   PAR(2) = k   self-limitation (logistic)
!   PAR(3) = c   Sheng nourishment strength
!   PAR(4) = g   Ke over-acting strength
!   PAR(5) = h   Ke direct restraint strength
! Bifurcation parameter: PAR(1) = a (or swap to any other)
!------------------------------------------------------------------

SUBROUTINE FUNC(NDIM, U, ICP, PAR, IJAC, F, DFDU, DFDP)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: NDIM, ICP(*), IJAC
  DOUBLE PRECISION, INTENT(IN)  :: U(NDIM), PAR(*)
  DOUBLE PRECISION, INTENT(OUT) :: F(NDIM), DFDU(NDIM,NDIM), DFDP(NDIM,*)

  DOUBLE PRECISION :: x1, x2, x3, x4, x5
  DOUBLE PRECISION :: a, k, c, g, h

  x1 = U(1); x2 = U(2); x3 = U(3); x4 = U(4); x5 = U(5)

  a = PAR(1)
  k = PAR(2)
  c = PAR(3)
  g = PAR(4)
  h = PAR(5)

  F(1) = a*x1 - k*x1**2 + c*x5/(1.0D0+x1) - g*x1/(1.0D0+x3) - h*x1*x4
  F(2) = a*x2 - k*x2**2 + c*x1/(1.0D0+x2) - g*x2/(1.0D0+x4) - h*x2*x5
  F(3) = a*x3 - k*x3**2 + c*x2/(1.0D0+x3) - g*x3/(1.0D0+x5) - h*x3*x1
  F(4) = a*x4 - k*x4**2 + c*x3/(1.0D0+x4) - g*x4/(1.0D0+x1) - h*x4*x2
  F(5) = a*x5 - k*x5**2 + c*x4/(1.0D0+x5) - g*x5/(1.0D0+x2) - h*x5*x3

  IF (IJAC .EQ. 0) RETURN

END SUBROUTINE FUNC

!------------------------------------------------------------------
SUBROUTINE STPNT(NDIM, U, PAR, T)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: NDIM
  DOUBLE PRECISION, INTENT(INOUT) :: U(NDIM), PAR(*)
  DOUBLE PRECISION, INTENT(IN) :: T

  PAR(1) = 2.0D0    ! a  <-- main bifurcation parameter
  PAR(2) = 0.5D0    ! k
  PAR(3) = 1.0D0    ! c
  PAR(4) = 0.5D0    ! g
  PAR(5) = 0.3D0    ! h

  ! REPLACE these with output from find_eq2.py
U(1) = 2.67028644D0
U(2) = 2.67028644D0
U(3) = 2.67028644D0
U(4) = 2.67028644D0
U(5) = 2.67028644D0

END SUBROUTINE STPNT
!------------------------------------------------------------------
SUBROUTINE BCND(NDIM, PAR, ICP, NBC, U0, U1, FB, IJAC, DBC)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: NDIM, ICP(*), NBC, IJAC
  DOUBLE PRECISION, INTENT(IN) :: PAR(*), U0(NDIM), U1(NDIM)
  DOUBLE PRECISION, INTENT(OUT) :: FB(NBC), DBC(NBC,*)
END SUBROUTINE BCND

SUBROUTINE ICND(NDIM, PAR, ICP, NINT, U, UOLD, UDOT, UPOLD, FI, IJAC, DINT)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: NDIM, ICP(*), NINT, IJAC
  DOUBLE PRECISION, INTENT(IN) :: PAR(*), U(NDIM), UOLD(NDIM), UDOT(NDIM), UPOLD(NDIM)
  DOUBLE PRECISION, INTENT(OUT) :: FI(NINT), DINT(NINT,*)
END SUBROUTINE ICND

SUBROUTINE FOPT(NDIM, U, ICP, PAR, IJAC, FS, DFDU, DFDP)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: NDIM, ICP(*), IJAC
  DOUBLE PRECISION, INTENT(IN) :: U(NDIM), PAR(*)
  DOUBLE PRECISION, INTENT(OUT) :: FS, DFDU(NDIM), DFDP(*)
END SUBROUTINE FOPT

SUBROUTINE PVLS(NDIM, U, PAR)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: NDIM
  DOUBLE PRECISION, INTENT(IN) :: U(NDIM)
  DOUBLE PRECISION, INTENT(INOUT) :: PAR(*)
END SUBROUTINE PVLS
