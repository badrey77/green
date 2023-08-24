import { ListItem } from "@chakra-ui/react";
import { getRandomItem } from "../utils/common";

const NutrItem = ({ inkey, value }) => (
    <ListItem key={inkey}>
      <span role="img" aria-label="dish">
        {getRandomItem([
          "🌭",
          "🍔",
          "🍟",
          "🍕",
          "🥪",
          "🥙",
          "🧆",
          "🌮",
          "🌯",
          "🥗",
          "🥘",
          "🍖",
          "🍝",
          "🍜",
          "🍲",
          "🍛"
        ])}
      </span>{" "}
      <strong>{ inkey }:{" "}</strong>
      { value }
    </ListItem>
  );

  export default NutrItem;