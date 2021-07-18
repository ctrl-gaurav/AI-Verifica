import '../App.css';
import shuchit from './image/shuchit.png';

function Team() {
  return (
    <div>
        <h1 class="title">
            Our Team
        </h1>
        <div class="team_container">
          <div class="team_card">
              <img src={shuchit} class="team_image"/> 
              {/* You-Only-Look-Once-Hacks\face_detection\src\components\image\shuchit.png */}
              <p>
                  Gaurav
              </p>
          </div>

          <div class="team_card">
              <img src={shuchit} class="team_image"/> 
              {/* You-Only-Look-Once-Hacks\face_detection\src\components\image\shuchit.png */}
              <p>
                  Shuchit Pant
              </p>
          </div>

          <div class="team_card">
              <img src={shuchit} class="team_image"/> 
              {/* You-Only-Look-Once-Hacks\face_detection\src\components\image\shuchit.png */}
              <p>
                  Roma Sinha
              </p>
          </div>


        </div>

        <div class="team_container">
          <div class="team_card">
              <img src={shuchit} class="team_image"/> 
              {/* You-Only-Look-Once-Hacks\face_detection\src\components\image\shuchit.png */}
              <p>
                  Yashwin
              </p>
          </div>

          <div class="team_card">
              <img src={shuchit} class="team_image"/> 
              {/* You-Only-Look-Once-Hacks\face_detection\src\components\image\shuchit.png */}
              <p>
                  Aninditaa
              </p>
          </div>

        </div>
        
    </div>
  );
}

export default Team;