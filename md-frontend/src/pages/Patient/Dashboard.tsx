import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import Chart from "./Chart";
import Deposits from "./Deposits";
import Orders from "./Orders";
import BigHomeButton from "./BigHomeButton";
import { MedicalInformation } from "@mui/icons-material";
import { randomUUID } from "crypto";

const elements = [
  {
    label: "Medical History",
    icon: <MedicalInformation />,
    path: "medHistory",
  },
  {
    label: "Allergies & reactions",
    icon: <MedicalInformation />,
    path: "medHistory",
  },
  {
    label: "Immunisations",
    icon: <MedicalInformation />,
    path: "medHistory",
  },
  {
    label: "COVID-19 Vaccinations & Tests",
    icon: <MedicalInformation />,
    path: "medHistory",
  },
  {
    label: "Scans",
    icon: <MedicalInformation />,
    path: "medHistory",
  },
  {
    label: "Test Results",
    icon: <MedicalInformation />,
    path: "medHistory",
  },
  {
    label: "Documents",
    icon: <MedicalInformation />,
    path: "medHistory",
  },
  {
    label: "Hospital Visits",
    icon: <MedicalInformation />,
    path: "medHistory",
  },
  {
    label: "Advance Care Planning",
    icon: <MedicalInformation />,
    path: "medHistory",
  },
  {
    label: "Organ Donation",
    icon: <MedicalInformation />,
    path: "medHistory",
  },
];

export default function Dashboard({ user }) {
  return (
    <Box sx={{ display: "flex" }}>
      <Box
        component="main"
        sx={{
          backgroundColor: (theme) =>
            theme.palette.mode === "light"
              ? theme.palette.grey[100]
              : theme.palette.grey[900],
          flexGrow: 1,
          height: "100vh",
          overflow: "auto",
        }}
      >
        <Toolbar />
        <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
          <Grid container spacing={3}>
            <Grid item xs={12}>
              <Paper
                sx={{
                  p: 2,
                  display: "flex",
                  flexDirection: "column",
                  backgroundColor: "red",
                }}
              >
                <Grid container spacing={1}>
                  {elements.map((element, index) => {
                    const key = index + "btn-elx-r-";
                    return (
                      <Grid item xs={12} md={4} lg={3} key={key}>
                        <BigHomeButton
                          label={element.label}
                          icon={element.icon}
                          path={element.path}
                        />
                      </Grid>
                    );
                  })}
                </Grid>
              </Paper>
            </Grid>
          </Grid>
        </Container>
      </Box>
    </Box>
  );
}
