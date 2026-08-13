@ECHO OFF
REM ============================================
REM  ReadDocs - One-click deploy script
REM  Build docs and open local preview
REM ============================================
pushd %~dp0

echo [1/3] Building docs...
call make.bat html
if errorlevel 1 (
    echo Build FAILED! Check errors above.
    pause
    exit /b 1
)

echo.
echo [2/3] Build SUCCESS! Output: build\html\
echo.

echo [3/3] Opening local preview...

REM Detect python command (fallback to Anaconda path)
set "PY=python"
where python >nul 2>nul
if errorlevel 1 set "PY=D:/DLSoftware/Anaconda3/1/python.exe"

REM Check if port 8000 is already serving
netstat -ano | findstr ":8000" | findstr "LISTENING" >nul 2>nul
if errorlevel 1 (
    echo Starting local HTTP server on port 8000 - no-cache mode...
    start "ReadDocs Preview" /min cmd /k "%PY% server.py"
    ping -n 3 127.0.0.1 >nul
) else (
    echo Port 8000 is already serving - reusing it.
)

echo Opening browser...
start "" http://localhost:8000/

echo.
echo Preview URL: http://localhost:8000/
echo To stop the server, close the "ReadDocs Preview" window.
echo.

popd
