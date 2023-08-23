import { Flex, HStack, Image, List, ListItem, Text, UnorderedList } from "@chakra-ui/react";

const ResultsList = (data) => {

    const elements = JSON.parse(data.elements);
    
    return (
        <List>
            {elements.map(elem=>(
                <ListItem key={JSON.stringify(elem.food.foodId)}>
                    <HStack spacing={3}>
                    <Image 
                    width={'100px'} 
                    height={'100px'} 
                    src={elem.food.image} 
                    alt={elem.food.label} />
                    <Text>{elem.food.label}</Text>
                    <UnorderedList>
                        <ListItem><Text>`Cals: ${JSON.stringify(elem.food.nutrients.ENERC_KCAL)}`</Text></ListItem>
                        <ListItem><Text>`Prots: ${JSON.stringify(elem.food.nutrients.PROCNT)}`</Text></ListItem>
                        <ListItem><Text>`Fibs: ${JSON.stringify(elem.food.nutrients.FIBTG)}`</Text></ListItem>
                    </UnorderedList>
                    </HStack>
                </ListItem>
            ))}
        </List>
    )
    
}

export default ResultsList;