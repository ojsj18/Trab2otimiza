all: montar quimica

quimica: 
	mv ./dist/quimica ./
teste:
	./quimica < ./exemplos/1.in
	./quimica < ./exemplos/2.in
	./quimica < ./exemplos/3.in
	./quimica < ./exemplos/4.in
	./quimica < ./exemplos/5.in
	./quimica < ./exemplos/1valor10-2.in
	./quimica < ./exemplos/2valor101-2-7.in
	./quimica < ./exemplos/3valor11-2-3-4-5.in
	./quimica < ./exemplos/4valor18-6-12-15.in
montar:
	python2.7 -m PyInstaller --onefile  quimica.py
clean:
	rm -r build/
	rm -r dist/
	rm quimica.spec
	rm quimica
