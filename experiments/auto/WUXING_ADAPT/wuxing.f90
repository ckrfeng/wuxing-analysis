!------------------------------------------------------------------
! Wu-Xing five organ model for AUTO-07p
! State variables: x(1)..x(5) = Wood, Fire, Earth, Metal, Water
! Parameters (PAR array, must match c.wuxing ordering):
!   1:  a    (uniform self-production, symmetric case)
!   2:  u    (uniform upregulation strength)
!   3:  c    (uniform Sheng strength)
!   4:  g    (uniform Ke over-acting strength)
!   5:  h    (uniform Ke restraint strength)
!   6:  th0  (uniform baseline set point theta_i^0)
!   7:  alp  (uniform alpha_i, mother's set point influence)
!   8:  bet  (uniform beta_i, controller's set point influence)
!   9:  n_h  (Hill exponent, the main bifurcation parameter)
!   10: w    (Wu rebellion strength, 0 = homeostasis only)
!   11: eps  (Wu weakness threshold)
!   12: uu   (uniform u_m = u, second Hill exponent = n_h)
!------------------------------------------------------------------

SUBROUTINE FUNC(NDIM, U, ICP, PAR, IJAC, F, DFDU, DFDP)
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: NDIM, ICP(*), IJAC
  DOUBLE PRECISION, INTENT(IN)  :: U(NDIM), PAR(*)
  DOUBLE PRECISION, INTENT(OUT) :: F(NDIM), DFDU(NDIM,NDIM), DFDP(NDIM,*)

  ! Local variables
  DOUBLE PRECISION :: x1, x2, x3, x4, x5
  DOUBLE PRECISION :: a, uu, cc, g, h, th0, alp, bet, nh, w, eps
  DOUBLE PRECISION :: th1, th2, th3, th4, th5
  DOUBLE PRECISION :: thn1, thn2, thn3, thn4, thn5
  DOUBLE PRECISION :: xn1, xn2, xn3, xn4, xn5
  DOUBLE PRECISION :: hill_prod1, hill_up1
  DOUBLE PRECISION :: hill_prod2, hill_up2
  DOUBLE PRECISION :: hill_prod3, hill_up3
  DOUBLE PRECISION :: hill_prod4, hill_up4
  DOUBLE PRECISION :: hill_prod5, hill_up5

  ! Unpack state
  x1 = U(1); x2 = U(2); x3 = U(3); x4 = U(4); x5 = U(5)

  ! Unpack parameters
  a   = PAR(1)
  uu  = PAR(2)
  cc  = PAR(3)
  g   = PAR(4)
  h   = PAR(5)
  th0 = PAR(6)
  alp = PAR(7)
  bet = PAR(8)
  nh  = PAR(9)
  w   = PAR(10)
  eps = PAR(11)

  ! Adaptive set points: theta_i = th0 + alp*x_mother - bet*x_controller
  ! Sheng mothers:     sig(1)=5, sig(2)=1, sig(3)=2, sig(4)=3, sig(5)=4
  ! Ke controllers:    rho(1)=4, rho(2)=5, rho(3)=1, rho(4)=2, rho(5)=3
  th1 = th0 + alp*x5 - bet*x4
  th2 = th0 + alp*x1 - bet*x5
  th3 = th0 + alp*x2 - bet*x1
  th4 = th0 + alp*x3 - bet*x2
  th5 = th0 + alp*x4 - bet*x3

  ! Clamp set points to avoid negative theta (safety)
  th1 = MAX(th1, 1.0D-6)
  th2 = MAX(th2, 1.0D-6)
  th3 = MAX(th3, 1.0D-6)
  th4 = MAX(th4, 1.0D-6)
  th5 = MAX(th5, 1.0D-6)

  ! theta^n and x^n for Hill functions
  thn1 = th1**nh;  xn1 = x1**nh
  thn2 = th2**nh;  xn2 = x2**nh
  thn3 = th3**nh;  xn3 = x3**nh
  thn4 = th4**nh;  xn4 = x4**nh
  thn5 = th5**nh;  xn5 = x5**nh

  ! Hill production terms (n_i = m_i = nh, symmetric)
  hill_prod1 = a*x1*thn1 / (thn1 + xn1)
  hill_prod2 = a*x2*thn2 / (thn2 + xn2)
  hill_prod3 = a*x3*thn3 / (thn3 + xn3)
  hill_prod4 = a*x4*thn4 / (thn4 + xn4)
  hill_prod5 = a*x5*thn5 / (thn5 + xn5)

  ! Deficiency upregulation terms
  hill_up1 = uu*thn1 / (thn1 + xn1)
  hill_up2 = uu*thn2 / (thn2 + xn2)
  hill_up3 = uu*thn3 / (thn3 + xn3)
  hill_up4 = uu*thn4 / (thn4 + xn4)
  hill_up5 = uu*thn5 / (thn5 + xn5)

  ! Right-hand sides
  ! Ke targets:    kap(1)=3, kap(2)=4, kap(3)=5, kap(4)=1, kap(5)=2
  ! Wu term on x_i: -w * x_kap(i) / (1 + x_i/eps)

  F(1) = hill_prod1 + hill_up1 &
       + cc*x5/(1.0D0+x1) &
       - g*x1/(1.0D0+x3) &
       - h*x1*x4 &
       - w*x3/(1.0D0 + x1/eps)

  F(2) = hill_prod2 + hill_up2 &
       + cc*x1/(1.0D0+x2) &
       - g*x2/(1.0D0+x4) &
       - h*x2*x5 &
       - w*x4/(1.0D0 + x2/eps)

  F(3) = hill_prod3 + hill_up3 &
       + cc*x2/(1.0D0+x3) &
       - g*x3/(1.0D0+x5) &
       - h*x3*x1 &
       - w*x5/(1.0D0 + x3/eps)

  F(4) = hill_prod4 + hill_up4 &
       + cc*x3/(1.0D0+x4) &
       - g*x4/(1.0D0+x1) &
       - h*x4*x2 &
       - w*x1/(1.0D0 + x4/eps)

  F(5) = hill_prod5 + hill_up5 &
       + cc*x4/(1.0D0+x5) &
       - g*x5/(1.0D0+x2) &
       - h*x5*x3 &
       - w*x2/(1.0D0 + x5/eps)

  ! Jacobian: set IJAC=0 in constants file to let AUTO use finite differences
  ! (recommended for first pass; set IJAC=1 and fill DFDU analytically later)
  IF (IJAC .EQ. 0) RETURN

END SUBROUTINE FUNC

!------------------------------------------------------------------
SUBROUTINE STPNT(NDIM, U, PAR, T)
! Starting point: symmetric equilibrium guess
  IMPLICIT NONE
  INTEGER, INTENT(IN) :: NDIM
  DOUBLE PRECISION, INTENT(INOUT) :: U(NDIM), PAR(*)
  DOUBLE PRECISION, INTENT(IN) :: T

  ! Parameter values at starting point
  PAR(1)  = 2.0D0   ! a
  PAR(2)  = 0.5D0   ! u
  PAR(3)  = 1.0D0   ! c
  PAR(4)  = 0.5D0   ! g
  PAR(5)  = 0.3D0   ! h
  PAR(6)  = 1.0D0   ! th0
  PAR(7)  = 0.1D0   ! alpha
  PAR(8)  = 0.1D0   ! beta
  PAR(9)  = 2.0D0   ! n_h  <-- main bifurcation parameter
  PAR(10) = 0.0D0   ! w (Wu off to start)
  PAR(11) = 0.5D0   ! eps

  ! Initial guess: symmetric equilibrium, all organs equal
  U(1) = 2.02267667D0
  U(2) = 2.02267667D0
  U(3) = 2.02267667D0
  U(4) = 2.02267667D0
  U(5) = 2.02267667D0

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
