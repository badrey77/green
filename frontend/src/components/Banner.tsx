import { Flex, Heading } from '@chakra-ui/react'
import Bg from '../resources/ts/images/background.jpg';

export const Banner = ({ title }: { title: string }) => (
  <Flex
    justifyContent="center"
    alignItems="normal"
    height="20vh"
    bgGradient="linear(to-l, heroGradientStart, heroGradientEnd)"
    bgClip="text"
    backgroundColor={"green.800"}
    backgroundImage={Bg.src}
    border={"5px double gray"}
    position={"relative"}
    margin={"0 auto"}
  >
    <Heading fontSize="7vw">{title}</Heading>
  </Flex>
)

Banner.defaultProps = {
  title: 'Resultats',
}
