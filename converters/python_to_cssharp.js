class PythonToCSharpConverter {
    convert(pythonCode) {
        const csharpCode = [];
        const lines = pythonCode.split('\n');
        
        for (let line of lines) {
            line = line.trim(); 


            if (line.startsWith('print(') && line.endsWith(')')) {
                const toPrint = line.substring(6, line.length - 1); 
                csharpCode.push(`Console.WriteLine(${toPrint});`);
            }
           
            else if (line.includes('=')) {
                csharpCode.push(`${line};`); 
            }
        }

        return csharpCode.join('\n'); 
    }
}

module.exports = PythonToCSharpConverter;
