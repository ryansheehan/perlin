@echo off
pushd
cd %~dp0
call Scripts\activate.bat
popd
@echo on
%*
@echo off
pushd
cd %~dp0
call Scripts\deactivate.bat
popd
