@echo off
set KMP_DUPLICATE_LIB_OK=TRUE
for /f "usebackq tokens=1,2 delims==" %%i in (".env") do (
    set "%%i=%%j"
)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
