import type { Metadata } from "next";
import { Source_Serif_4, IBM_Plex_Mono } from "next/font/google";
import "./globals.css";

const serif = Source_Serif_4({
  subsets: ["latin"],
  variable: "--font-serif",
  style: ["normal", "italic"],
});

const mono = IBM_Plex_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
  weight: ["400", "500", "600"],
});

export const metadata: Metadata = {
  title: "The Long Count — how fast San Francisco counts ballots",
  description:
    "Every results release from every San Francisco election since 2002. " +
    "The count never got slower — election night just stopped being when the counting happens.",
  openGraph: {
    title: "The Long Count",
    description:
      "San Francisco hasn’t gotten slower at counting ballots. Election night just stopped being when the counting happens.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={`${serif.variable} ${mono.variable}`}>
      <body className="antialiased">{children}</body>
    </html>
  );
}
