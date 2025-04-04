using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Thread_2._1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int x = 20; //координаты цетра шарика 1
        int y = 20;
        int vx = 10; //компоненты скорости шарика 1
        int vy = 15;
        
        int x2 = 40;//координаты цетра шарика 1
        int y2 = 60;
        int vx2 = 20; //компоненты скорости шарика 1;
        int vy2 = 10;
        
        int r = 10; // радиус шарика

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode =
                System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            Graphics p = this.CreateGraphics();
            p.Clear(Color.White); 
            p.DrawEllipse(new Pen(Color.Red, 2 * r), x, y, 2 * r, 2 * r);
            p.DrawEllipse(new Pen(Color.Blue, 2 * r), x2, y2, 2 * r, 2 * r);

        }

        private void timer1_Tick_1(object sender, EventArgs e)
        {

            void run1() //движение шарика 1
            {
                x += vx;
                if (x - 2*r < 0 || x + 2*r > this.ClientSize.Width-20) // шарик 1 стукнулся о вертикальную границу
                {
                    vx = -vx;
                }

                y += vy;
                if (y - 2*r < 0 || y + 2*r > this.ClientSize.Height-20) // шарик 1 стукнулся о горизонтальную границу
                {
                    vy = -vy;
                }

                int vx_1, vy_1, vx_2, vy_2; //промежуточные переменные
                vx_1 = vx;
                vy_1 = vy;
                vx_2 = vx2;
                vy_2 = vy2;

                if ((Math.Abs(x2 - x) <= 2 * r) && (Math.Abs(y2 - y) <= 2 * r)) // столкновение 1 и 2
                {
                    vx = vx_2;
                    vy = vy_2;
                    vx2 = vx_1;
                    vy2 = vy_1;
                }
                Thread.Sleep(50);
            }

            void run2() //движение шарика 2
            {
                x2 += vx2;
                if (x2 - 2*r < 0 || x2 + 2*r > this.ClientSize.Width - 20) // шарик 2 стукнулся о вертикальную границу
                {
                    vx2 = -vx2;
                }

                y2 += vy2;
                if (y2 - 2*r < 0 || y2 + 2*r > this.ClientSize.Height-20) // шарик 2 стукнулся о горизонтальную границу
                {
                    vy2 = -vy2;
                }

                int vx_1, vy_1, vx_2, vy_2; //промежуточные переменные
                vx_1 = vx;
                vy_1 = vy;
                vx_2 = vx2;
                vy_2 = vy2;

                if ((Math.Abs(x2 - x) <= 2 * r) && (Math.Abs(y2 - y) <= 2 * r)) // столкновение шариков
                {
                    vx = vx_2;
                    vy = vy_2;
                    vx2 = vx_1;
                    vy2 = vy_1;
                }
                Thread.Sleep(50);
            }

            Parallel.Invoke(run1, run2); //параллельно считаем движение шариков
            
            this.Refresh();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Start();
        } 
    }
}
