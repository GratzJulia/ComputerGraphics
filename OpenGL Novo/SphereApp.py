from GLAPP import GLAPP
from OpenGL import GL
from array import array
import ctypes
import glm
import math
import random 

class SphereApp(GLAPP):

    def setup(self):
        # Window setup
        self.title("Dotted Sphere")
        self.size(600,600)

        # OpenGL Initialization
        GL.glClearColor(0.2, 0.2, 0.2, 0.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)

        # Pipeline (shaders)
        self.pipeline = self.loadPipeline("WhiteDotsPipeline")
        GL.glUseProgram(self.pipeline)
        self.a = 0
        self.sphereArrayBufferId = None

        # Texture
        GL.glActiveTexture(GL.GL_TEXTURE0)
        self.loadTexture("../texturas/mapa.png")
        GL.glUniform1i(GL.glGetUniformLocation(self.pipeline, "textureSlot"),0)


    def geraMVP(self):
        projection = glm.perspective(math.pi/4, self.width/self.height, 0.1, 100)
        camera = glm.lookAt(glm.vec3(0, 0, 5), glm.vec3(0), glm.vec3(0, 1, 0))
        model = glm.rotate(self.a, glm.vec3(0, 0, 1)) * glm.rotate(self.a, glm.vec3(0, 1, 0)) * glm.rotate(self.a, glm.vec3(1, 0, 0)) 
        return projection * camera * model

    def geraPto(self, position, textureCoord, i, j, n):
        theta = i*2*math.pi/n
        phi = j*math.pi/n-math.pi/2
        position.append(math.cos(theta)*math.cos(phi))
        position.append(math.sin(phi))
        position.append(math.sin(theta)*math.cos(phi))
        textureCoord.append(i/n)
        textureCoord.append(j/n)
        
    def drawSphere(self):
        n = 50

        if self.sphereArrayBufferId == None:
            position = array('f')
            textureCoord = array('f')
            for i in range(0,n):                
                for j in range(0,n):                  
                    self.geraPto(position, textureCoord, i, j, n)
                    self.geraPto(position, textureCoord, i, j+1, n)
                    self.geraPto(position, textureCoord, i+1, j+1, n)
                    self.geraPto(position, textureCoord, i, j, n)
                    self.geraPto(position, textureCoord, i+1, j+1, n)
                    self.geraPto(position, textureCoord, i+1, j, n)
                  
            self.sphereArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.sphereArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

            idTextureBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idTextureBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(textureCoord)*textureCoord.itemsize, ctypes.c_void_p(textureCoord.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(1,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))
        
        GL.glBindVertexArray(self.sphereArrayBufferId)
        mvp = self.geraMVP()
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.pipeline, "MVP"), 1, GL.GL_FALSE,glm.value_ptr(mvp))
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 6*n*n)
        self.a += 0.00003

    def draw(self):
        # clear screen and depth buffer
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        self.drawSphere()

SphereApp()
