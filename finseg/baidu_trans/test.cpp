using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
namespace read_file
{
    class Program
    {
        public static int ReadInt32(Stream fs)
        {
            var temp = new byte[4];
            fs.Read(temp, 0, 4);
            int s = BitConverter.ToInt32(temp, 0);
            return s;
        }
        public static List<String> readWord(string path,List<String>list)
        {
            var fs = new FileStream(path, FileMode.Open, FileAccess.Read);
            fs.Seek(0, SeekOrigin.End);
            long endPosition = fs.Position;
            fs.Position = 0x350;
            do
            {
                int len = ReadInt32(fs);
                fs.Position += len * 2;
                var temp = new byte[len * 2];
                fs.Read(temp, 0, len * 2);
                String word = Encoding.Unicode.GetString(temp);
                list.Add(word);
            } while (fs.Position <endPosition-1);
            fs.Close();
            return list;
        }
        static void transform_txt(string path)
        {
            var files = Directory.GetFiles(path, "*.bdict");
            List<String> list = new List<string>();
            foreach (var file in files)
            {
                list = readWord(file, list);
                Console.WriteLine(file + "文件处理完毕！");
            }
            FileStream fs = new FileStream(path + "dict.txt", FileMode.Append);
            StreamWriter writer = new StreamWriter(fs, Encoding.UTF8);
            foreach (String word in list)
            {
                writer.Write(word + "\n");
            }
            writer.Close();
            fs.Close();
        }
        static void Main(string[] args)
        {
            string []paths = { "." };
            foreach (string path in paths)
                transform_txt(path);
        }
    }
}
