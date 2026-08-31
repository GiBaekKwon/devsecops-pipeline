# DevSecOps Security Pipeline

## 프로젝트 목적
실제 보안 취약점을 탐지하고 차단하는 실무형 CI/CD 보안 파이프라인 구축.
단순 스캔 리포트 생성이 아니라 심각도 기준 미달 시 배포 자체를 막는 정책 게이트를 목표로 합니다.

## 아키텍처
```text
Code Push → GitHub Actions
 ├─ SAST (Semgrep)
 ├─ SCA (Trivy fs scan)
 ├─ Secret Scan (Gitleaks)
 ├─ Docker Build
 ├─ Container Scan (Trivy image scan)
 └─ 정책 게이트 (Critical/High 발견 시 배포 차단)
     ↓ (통과 시)
 NCP Container Registry → NCP 배포
```

## 기술 스택
- CI/CD: GitHub Actions
- SAST: Semgrep
- SCA / Container Scan: Trivy
- Secret Scan: Gitleaks
- Container: Docker
- Cloud: Naver Cloud Platform (NCR)

## 진행 현황
- [x] 테스트용 취약점 Flask 앱 작성
- [x] Dockerfile 작성 및 로컬 빌드 확인
- [x] Trivy 로컬 스캔 (Critical 2 / High 40 발견 — 스크린샷 참고)
- [ ] GitHub Actions 자동화
- [ ] NCP Container Registry 연동
- [ ] 정책 게이트 (자동 차단) 구현

## 스캔 결과 (Before)
의도적으로 오래된 베이스 이미지(`python:3.9-slim-buster`, EOL)를 사용해
Trivy가 실제로 다수의 취약점을 탐지하는지 검증했습니다.

### 1. 전체 요약 결과
![Trivy 요약](docs/trivy-scan-1.png)

### 2. OS 패키지 상세 취약점
![OS 스캔](docs/trivy-scan-2.png)

### 3. Python 패키지 상세 취약점
![Python 스캔](docs/trivy-scan-3.png)
