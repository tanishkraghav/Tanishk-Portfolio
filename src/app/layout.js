import './globals.css'
import { ThemeProvider } from '@/components/theme-provider'
import SmoothScroll from '@/components/smooth-scroll'

export const metadata = {
  title: 'Tanishk Raghav — Data Scientist',
  description: 'Data Scientist building delightful interfaces. Portfolio of Tanishk Raghav.',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="antialiased">
        <ThemeProvider attribute="class" defaultTheme="dark" enableSystem={false} disableTransitionOnChange>
          <SmoothScroll />
          {children}
        </ThemeProvider>
      </body>
    </html>
  )
}
