import { Box, Button, ButtonGroup, Card, CardBody, CardFooter, Divider, Flex, Heading, Image, Stack, Text } from "@chakra-ui/react";
import { DishType } from "../utils/types";

const Dishes = ({ dishes }) => {
    
    console.log(dishes);
    
    return (
      <>
        { dishes.map((dish: DishType)=>(
            <Card key={dish.id} maxW='2xl'>
            <CardBody>
              <Image
                src={dish.img}
                alt='Green double couch with wooden legs'
                borderRadius='lg'
              />
              <Stack mt='6' spacing='3'>
                <Heading size='md'>{ dish.label }</Heading>
                <Text>
                  { dish.description }
                </Text>
                <Text color='blue.600' fontSize='2xl'>
                  ${dish.price}
                </Text>
              </Stack>
            </CardBody>
            <Divider />
            <CardFooter>
              <ButtonGroup spacing='2'>
                <Button variant='solid' colorScheme='blue'>
                  Details
                </Button>
                <Button variant='ghost' colorScheme='blue'>
                  Add to My Order
                </Button>
              </ButtonGroup>
            </CardFooter>
          </Card>
        ))}
    </>
)}

export default Dishes