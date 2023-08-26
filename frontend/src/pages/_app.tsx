import { ChakraProvider } from '@chakra-ui/react'

import theme from '../theme'
import { AppProps } from 'next/app'
import MainBanner from '../components/MainBanner'
import { CTA } from '../components/CTA'

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider theme={theme}>
      <MainBanner />
      <Component {...pageProps} />
      <CTA />
    </ChakraProvider>
  )
}

export default MyApp
