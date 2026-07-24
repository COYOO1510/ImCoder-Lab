@ECHO OFF
REM ============================================
REM  ReadDocs - One-click deploy script
REM  Build docs and prepare for GitHub Pages
REM ============================================
pushd %~dp0

echo [1/2] Building docs...
call make.bat html
if errorlevel 1 (
    echo Build FAILED! Check errors above.
    pause
    exit /b 1
)

echo.
echo [2/2] Build SUCCESS!
echo Output: build\html\
echo.
echo Upload build\html\ to your web server, or
echo push to GitHub to trigger auto-deployment.

popd
