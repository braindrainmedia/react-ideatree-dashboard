import { Box, Typography, useTheme } from "@mui/material";
import { tokens } from "../theme";
import ProgressCircle from "./ProgressCircle";
import Divider from '@mui/material/Divider';
import CachedIcon from '@mui/icons-material/Cached';
import DownloadIcon from '@mui/icons-material/Download';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import IosShareIcon from '@mui/icons-material/IosShare';
import AssistantIcon from '@mui/icons-material/Assistant';

const DocBox = ({ title, subtitle, icon, progress, increase }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <Box width="100%" m="30px 30px" >
      <Box display="flex" justifyContent="space-between">
        
      
        <Box>
          {icon}
        
          <CachedIcon sx={{ color: colors.grey[400], fontSize: "26px", mr:1, mt:1, ml: "460px", opacity:".5" }}/>
          <DownloadIcon sx={{ color: colors.grey[400], fontSize: "26px", mr:1, mt:1, opacity:".5" }}/>
          <IosShareIcon sx={{ color: colors.grey[400], fontSize: "26px", mr:1, mt:1, opacity:".5" }}/>
          <AddCircleIcon sx={{ color: colors.grey[400], fontSize: "26px", mr:2, mt:1, opacity:".5" }}/>
        
          
          
          <Typography
            variant="h2"
            fontWeight="bold"
            sx={{ color: colors.grey[100] }}
          >
            Slogans:
          </Typography>
          
        </Box>
        
      </Box>
       
      <Box display="flex" justifyContent="space-between" mt="2px" >
      
        <Typography variant="h5" sx={{ color: colors.blueAccent[500] }}>
          GPT_Prompt_Slogans.py
        </Typography>
        
        
      </Box>
      
      <Divider light sx={{ mt: '10px' }}/>
      <Box display="flex" justifyContent="space-between" mt="10px">
        <Typography variant="h6" sx={{ color: colors.grey[200] }}>
        Attention remains a crucial area of investigation within education, psychology, neuroscience, cognitive neuroscience, and neuropsychology. Areas of active investigation involve determining the source of the sensory cues and signals that generate attention, the effects of these sensory cues and signals on the tuning properties of sensory neurons, and the relationship between attention and other behavioral and cognitive processes, which may include working memory and psychological vigilance. A relatively new body of research, which expands upon earlier research within psychopathology, is investigating the diagnostic symptoms associated with traumatic brain injury and its effects on attention. Attention also varies across cultures.  Attention remains a crucial area of investigation within education, psychology, neuroscience, cognitive neuroscience, and neuropsychology. Areas of active investigation involve determining the source of the sensory cues and signals that generate attention, the effects of these sensory cues and signals on the tuning properties of sensory neurons, and the relationship between attention and other behavioral and cognitive processes, which may include working memory and psychological vigilance. A relatively new body of research, which expands upon earlier research within psychopathology, is investigating the diagnostic symptoms associated with traumatic brain injury and its effects on attention. Attention also varies across cultures.Attention remains a crucial area of investigation within education, psychology, neuroscience, cognitive neuroscience, and neuropsychology. Areas of active investigation involve determining the source of the sensory cues and signals that generate attention, the effects of these sensory cues and signals on the tuning properties of sensory neurons, and the relationship between attention and other behavioral and cognitive processes, which may include working memory and psychological vigilance. A relatively new body of research, which expands upon earlier research within psychopathology, is investigating the diagnostic symptoms associated with traumatic brain injury and its effects on attention. Attention also varies across cultures.
        </Typography>
        
      </Box>
    </Box>
  );
};

export default DocBox;
