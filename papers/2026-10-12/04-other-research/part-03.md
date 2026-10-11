# 📦 其他研究 | 2026年10月12日

> 本类共 **329** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-329](./part-07.md)

---

### 101. [3DTexMOR: 3D Gaussian Multi-Object Removal via Texture-Space Inpainting](https://arxiv.org/abs/2610.11198)

**<font color=#1a73e8>作者：</font>** Kunxin Guang, Yonghao Zhao, Jian Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D object removal aims to remove target objects from reconstructed scenes and complete the geometry and appearance of occluded regions. Existing NeRF- and 3DGS-based methods typically inpaint 2D images to guide 3D completion. However, complex multi-object layouts limit the surrounding context visible in each view, making 2D inpainting prone to artifacts. Inconsistent completions across views also introduce conflicting supervision and blurry reconstructions. We propose 3D Gaussian Multi-Object Removal via Texture-Space Inpainting (3DTexMOR). Our key idea is to perform inpainting in a unified texture space shared by all views. By combining complementary observations, this space provides richer context for recovering missing regions and promotes cross-view appearance consistency. We aggregate multi-view observations into texture maps, inpaint the missing regions, and reproject the completed maps into camera views to supervise Gaussian scene completion. To avoid the influence of view-dependent highlights and reflections, we decompose appearance and aggregate view-independent intrinsic attributes instead of RGB colors. We further introduce geometrically regularized Gaussian completion to constrain the geometry of the completed regions. Extensive experiments demonstrate visually plausible completions and state-of-the-art multi-object removal performance, improving PSNR by 5.8 dB and reducing LPIPS by at least 22% compared with existing methods.

---


### 102. [Dissecting Representation Structure in Vision Transformers: A Rigorous Architectural Study](https://arxiv.org/abs/2610.11205)

**<font color=#1a73e8>作者：</font>** Kim-Cuc Nguyen, Ngai-Man Cheung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation structure is crucial for understanding Vision Transformer (ViT) architectures and their generalization behavior. However, prior studies neither isolate nor analyze module-level features nor investigate how their interactions contribute to performance estimation. In this work, we conduct the first rigorous analysis of feature information across diverse architectural scales, empirically uncover the relationship between ViT representation and generalization behavior, and leverage these insights to guide efficient ViT design. Our contributions are fivefold: Across diverse architectural scales, 1) We identify feature collapse at initialization, which leads to redundancy, and propose a reduction scheme to mitigate this issue. 2) We quantify feature information using entropy and the minimum eigenvalue, demonstrating that these metrics serve as reliable indicators for generalization prediction. 3) We show that feature in the token space provides a more faithful representation than those in embedding space. 4) We discover an unexpected finding: features produced by linear submodules within ViT layers are critical for the prediction of generalization performance. 5) Our proposed proxy improves the correlation ranking by 18-48% over prior baselines and can effectively identify ViT architectures that achieve higher accuracy at lower or comparable computational cost.

---


### 103. [Do Flatter Minima Drive Better Generalization? An Algorithmic Separation in Grokking](https://arxiv.org/abs/2610.11206)

**<font color=#1a73e8>作者：</font>** Mohnish Harwani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flat loss landscapes have long been linked to better generalization in neural networks. However, its role as a causal mechanism for generalization is less established. Grokking provides an unique testbed to understand this distinction: models are prone to fit observed data using non-generalizing structure and remain in that regime for prolonged periods, transitioning to generalization only under particular training conditions. In this work, we study whether flat loss landscapes can act as a driving mechanism in this transition. While recent work has argued for flatness as a necessary geometric condition for this transition, we find that biasing training toward flatter solutions using sharpness-aware minimization (SAM) is insufficient to reliably induce this transition, despite producing flatter solutions. However, when SAM is paired with mechanisms that drive generalization such as weight decay, an interesting property emerges: SAM can accelerate the transition to generalizing solutions by up to 4x at the epoch-level. We theoretically untangle this relationship between SAM and weight decay using a minimal interpolating two-layer ReLU model with both memorizing and generalizing solutions. We show that even in this simple setup, flatness alone cannot distinguish a memorizing solution from a generalizing one, while weight decay favors generalizing solutions. However, under a local stability analysis, there exists a window where a memorizing interpolant is locally stable under gradient descent but unstable under SAM in the low-norm regime, which can explain SAM's ability to accelerate this transition. Overall, our results provide a more interpretable account of the role of flatness in driving generalization, especially in settings where models are vulnerable to minimizing loss through learning non-generalizing structure.

---


### 104. [AliO: Output Alignment Matters in Long-Term Time Series Forecasing](https://arxiv.org/abs/2610.11213)

**<font color=#1a73e8>作者：</font>** Kwangryeol Park, Jaeho Kim, Seulki Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term Time Series Forecasting (LTSF) tasks, which leverage the current data sequence as input to predict the future sequence, have become increasingly crucial in real-world applications such as weather forecasting and planning of electricity consumption. However, state-of-the-art LTSF models often fail to achieve prediction output alignment for the same timestamps across lagged input sequences. Instead, these models exhibit low output alignment, resulting in fluctuation in prediction outputs for the same timestamps, undermining the model's reliability. To address this, we propose AliO (Align Outputs), a novel approach designed to improve the output alignment of LTSF models by reducing the discrepancies between prediction outputs for the same timestamps in both the time and frequency domains. To measure output alignment, we introduce a new metric, TAM (Time Alignment Metric), which quantifies the alignment between prediction outputs, whereas existing metrics such as MSE only capture the distance between prediction outputs and ground truths. Experimental results show that AliO effectively improves the output alignment, i.e., up to 58.2% in TAM, while maintaining or enhancing the forecasting performance (up to 27.5%). This improved output alignment increases the reliability of the LTSF models, making them more applicable in real-world scenarios.

---


### 105. [GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images](https://arxiv.org/abs/2610.11215)

**<font color=#1a73e8>作者：</font>** Qirui Wu, Stan Birchfield, Hesam Rabeti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing complete, scene-aligned 3D objects from casual images requires integrating sparse, uncertain observations and inferring surfaces hidden by occlusions. We present GATOR, a generative and agentic framework that recovers textured object assets and their scene-relative pose from one or more images. Our local modality mixer couples patch-aligned RGB, target-mask, and pointmap features before cross-view reasoning, preserving scene context while distinguishing the target from its surroundings. Text-guided semantic conditioning complements these spatial cues with category names and object captions through stage-specific adapters for structure, geometry, and appearance generation. The generated asset initializes a multimodal agent, providing instance-specific geometry and pose for targeted structural and texture refinement through an observation-guided edit-render-review loop. Across synthetic objects, cluttered tabletops, and indoor scenes, GATOR achieves strong geometric and appearance fidelity while recovering scene-relative pose from sparse observations. Time-budget comparisons and scene-level simulation further demonstrate the reconstruction efficiency and simulation readiness. Project page: this https URL

---


### 106. [The Lattice of Transition Laws](https://arxiv.org/abs/2610.11216)

**<font color=#1a73e8>作者：</font>** T. Y. Tsui, Jiatao Gu, Lingjie Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and autoregression (AR) have long been seen as different categories of generative models, with diffusion specialising in continuous fields and AR specialising in discrete tokens. Recent work seeks to combine the advantages of the two models, and each hybrid fixes its decoding schedule by design. In this paper, we ask whether the performance of decoding schedules of one model can be predicted before decoding at a fixed number of steps. We describe diffusion, AR, and models in between as paths on one corruption lattice, and define the cost of a schedule as the dependence its parallel steps discard. The cost shows that the fewest steps of a zero-cost schedule are set by the geometry of the data, in the same way for tokens and for continuous fields. In particular, for data that are Markov on a graph and dependent along its paths, the fewest steps equal the graph's treedepth, which is logarithmic in the length of a sequence and linear in the side length of a grid. With fewer steps than the treedepth, every schedule pays a positive cost, whose ranking we predict before decoding with a kernel of pairwise dependence estimated from pretrained weights. Across text generation, image generation, and video generation, we verify most of the predictions about the rankings of different schedules under different metrics and benchmarks. This work therefore provides a design principle for decoding for future AR models, diffusion models, and anything in between. Our code is available at this https URL.

---


### 107. [BRACE: Differential Privacy for Dense Associative Memory with LSR Energy](https://arxiv.org/abs/2610.11218)

**<font color=#1a73e8>作者：</font>** Chang Qu, Zhaoyang Shi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dense associative memory (DAM) provides an energy-based framework for memory retrieval with close connections to attention mechanisms in modern artificial intelligence. Despite growing interest in differential privacy for AI, the privacy of DAM retrieval dynamics remains relatively unexplored. In this paper, we develop a differential privacy framework for log-sum-ReLU (LSR) dense associative memory, whose finite-support retrieval dynamics pose distinctive challenges for privacy-preserving computation. We propose the Boundary-Responsive Adaptive Correction Evolution (BRACE) algorithm, a differentially private retrieval mechanism for LSR-DAM that adaptively corrects boundary-sensitive perturbations to control their cumulative effect over the retrieval trajectory. In theory, we prove that our method is minimax optimal by deriving dimension-independent terminal and full-trajectory retrieval error rates, with optimal dependence on the inverse temperature and, in the growing-horizon regime, the retrieval horizon. We further establish central limit theorems that enable uncertainty quantification for private retrieval by characterizing its asymptotic distribution and the additional variability introduced by privacy. Numerical experiments compare our proposed method with baseline differential privacy approaches and evaluate its retrieval accuracy. Together, our results provide a theoretical foundation for optimal privacy-preserving retrieval and uncertainty quantification in energy-based associative memory systems.

---


### 108. [SteerCast: Retrieval-Based Latent Steering for Decoder-Only Time Series Forecasting](https://arxiv.org/abs/2610.11229)

**<font color=#1a73e8>作者：</font>** Van Dai Do, Huu Hiep Nguyen, Minh Hoang Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting aims to predict future values from historical observations and auxiliary features. We propose \textbf{SteerCast}, a retrieval-based latent steering method that improves decoder-only forecaster at inference time, without updating its parameters. SteerCast constructs a database from the training set by storing a representation of each history window together with a \emph{steering vector} computed in the forecaster's latent space, defined as the difference between representations induced by the ground-truth continuation and by the model's own prediction. At test time, SteerCast retrieves nearest neighbors for a query history, aggregates their steering vectors, and injects the resulting signal into the forecaster's hidden states at every step of autoregressive generation, guiding predictions toward trajectories consistent with similar training cases. Experiments across diverse multivariate benchmarks and multiple horizons show that SteerCast consistently improves forecasting accuracy over the fine-tuned backbone and retrieval-based baselines, while requiring no additional training beyond the original fine-tuning and using only the training set as a retrieval corpus.

---


### 109. [Low-Cost Sensor Calibration for Indoor Air Quality Monitoring: A Dataset, Evaluation Scenarios, and a Lightweight Model](https://arxiv.org/abs/2610.11236)

**<font color=#1a73e8>作者：</font>** Jinyong Yun, Seokho Ahn, Hyungjin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-cost sensors enable scalable indoor air quality monitoring but require calibration because of nonlinear distortions, noise, and temporal drift. The conventional strict pairwise calibration setting requires a co-located reference sensor at each deployment location and does not account for spatial and temporal heterogeneity. To address these limitations, we introduce a six-month dataset comprising multivariate indoor air-quality measurements from low-cost and reference sensors with contextual metadata collected at five locations. Using this dataset, we define four evaluation scenarios. The reference-efficient and location-transfer scenarios evaluate spatial generalization, whereas the long-term drift and event-conditioned scenarios assess robustness to gradual and abrupt distribution shifts. Based on these scenarios, we derive design requirements and propose a lightweight temporal model that combines input-window compression with residual temporal and feature fusion. Experiments show strong calibration performance across all four scenarios with low edge-inference cost.

---


### 110. [Breaking the Group Size Barrier: Parameter-Efficient Group Dance Generation with Chain-of-Dancers](https://arxiv.org/abs/2610.11237)

**<font color=#1a73e8>作者：</font>** Jing Xu, Cunjian Chen, Qiuhong Ke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Group dance generation aims to synthesize coordinated multi-dancer choreography from music, with broad applications in animation and interactive content creation. This task requires modeling dense inter-person dependencies to ensure spatial coordination, while naturally preserving individual dancer identities. Existing approaches model all dancers jointly with end-to-end transformers, which tie the architecture to a fixed group size and entangle per-dancer identities across frames. We propose ChainDance, a scalable framework that reformulates group dance generation as a Chain-of-Dancers: a sequential decomposition over per-dancer conditional distributions, allowing a single model to scale across variable group sizes without retraining and naturally preserving per-dancer identity. Built on a frozen single-dancer diffusion backbone, ChainDance introduces two lightweight modules: a Role-Aware Text Encoder (RATE) for per-dancer semantic conditioning, and a Group-Aware Motion Encoder (GAME) that aggregates previously generated dancers via a distance-weighted graph convolutional network, and incorporates a training-free noise optimization procedure at inference time to enforce global spatial coherence. Experiments on AIOZ-GDance demonstrate that ChainDance achieves state-of-the-art motion quality and group coordination while structurally preserving per-dancer identity, with $3$-$4\times$ fewer parameters and requiring $3$-$6\times$ less training time compared to prior approaches.

---


### 111. [Attributing HOW, Not Just WHICH: Counterfactual Response Trajectories for Diffusion Models](https://arxiv.org/abs/2610.11238)

**<font color=#1a73e8>作者：</font>** Haoqian Zhang, Ziyuan Yang, Zerui Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved remarkable success in image generation, yet tracing their outputs to individual training examples remains challenging. Existing attribution methods often compress factor-specific effects into scalar responses, making distinct internal changes indistinguishable. This is particularly limiting for diffusion models, where semantic factors emerge through evolving representation dynamics during denoising. We therefore reformulate diffusion data attribution as attributing factor-induced internal response trajectories. In this paper, we propose a novel Concept Attribution method through Dynamic Trajectories(CADT). We argue that attribution should therefore ask not only \emph{which} examples matter, but also \emph{how} their influence unfolds during generation. Specifically, we construct matched counterfactual pairs at identical noisy states to isolate factor-specific representation displacements, and model their directional and magnitude evolution across denoising as dynamic attribution signatures. For each training example and generated query, CADT extracts stage-wise feature vectors and integrates them along the denoising process to form a trajectory descriptor. Applying the same construction across the training set yields a bank of factor-specific trajectory descriptors. The covariance statistics of this bank are then used to construct . CADT uses this covariance-aware positive-semidefinite kernel to calibrate the query and training representations, and compares the calibrated query trajectory with each training trajectory to produce the final training-sample attribution scores. Experiments on multiple public datasets show consistent improvements over existing diffusion attribution baselines across hierarchical, compositional, and style attribution.

---


### 112. [TAP3D: Thermal-Assisted 3D Human Point Clouds](https://arxiv.org/abs/2610.11241)

**<font color=#1a73e8>作者：</font>** Xie Zhang, Chengxiao Li, Xuan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human body point clouds are a versatile representation for AI-enabled human sensing. However, existing methods using LiDAR, radar, and depth cameras suffer from inherent drawbacks in high cost, sparse reconstruction, and privacy concerns, etc. In this paper, we exploit low-cost thermal arrays and present TAP3D, the first system to reconstruct 3D human point clouds from body heat signatures, offering significant advantages in cost, density, human sensitivity, and privacy. To overcome major challenges in depth estimation, thermal interference, and multi-person separation, we propose a novel physics-informed design, which integrates a forward thermal physics model with two distinct modules: multi-primitive estimation for self-supervised joint recovery of depth and other thermal properties, and geometric perspective fusion for suppressing interference and disentangling multiple people. We implement TAP3D using a single commodity thermal array sensor and build a large-scale dataset (160K samples, 8 environments, 11 users) for evaluation. TAP3D achieves remarkable accuracy for dense point cloud generation, enabling downstream tasks like fall detection (91.46%), indoor tracking (21.86 cm MAE), and human mesh recovery (4.87 cm error). By transforming body heat into point clouds for the first time, TAP3D pioneers a new paradigm for privacy-first, fully passive human sensing for many applications. TAP3D is open-sourced at this https URL.

---


### 113. [Neuro-Memory Fuzzy Inference System for Mimicking Human-like Car Following Behavior](https://arxiv.org/abs/2610.11252)

**<font color=#1a73e8>作者：</font>** Nazmul Haque, Md Asif Raihan. Md. Hadiuzzaman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study presents the Neuro-Memory Fuzzy Inference System (NeMeFIS), a hierarchical machine learning architecture that asymmetrically models acceleration and deceleration in car following behavior by integrating five human memory types procedural, working, episodic, semantic, and declarative. By linking external variables to memory functions via metaheuristics and validating them through factor and p-value analyses, NeMeFIS uncovers latent cognitive influences across Arterial, Collector, and Rural Highway corridors for different types of vehicles. Results from 54 different trained models emphasize cognitive thresholds shaped by driver perception limits and cognitive load. The trained NeMeFIS models outperform traditional statistical and conventional machine learning models in replicating realistic driving behavior, including comparisons with Linear Regression, ANFIS, and LSTM architectures. Fuzzy rule analysis reveals that declarative memory demands the highest rule, especially during deceleration, indicating complex braking decisions. Procedural memory drives acceleration, while semantic and declarative memory guide deceleration. Risk perception also emerges as a key factor, particularly on urban roads. Validated on both heterogeneous and homogeneous datasets, NeMeFIS offers a robust framework for modeling driver cognition. The findings support psychotherapeutic applications and the development of adaptive, human-like decision systems in Connected and Autonomous Vehicles (CAVs) to enhance traffic safety.

---


### 114. [Provable Subexponential Algorithms for NIST Third-Round Lattice Families](https://arxiv.org/abs/2610.11254)

**<font color=#1a73e8>作者：</font>** Yiming Gao, Xuyuan Han, Honggang Hu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We give provable classical subexponential algorithms for secret recovery in growing parameter families associated with NIST third-round lattice candidates. For the Kyber/ML-KEM, FrodoKEM, SABER, NTRU LPRime, and Dilithium/ML-DSA families studied here, polynomial moduli and polylogarithmic coefficient scales yield recovery of the short secret component in expected time and space $2^{(1/2+o(1))n/\ln\ln n}$.
For noisy or rounded linear relations, we exploit an exact gap in the squared Euclidean norm of a comparison vector defined by each coordinate guess. One Gaussian list suffices to identify every secret coordinate by binary search, without enumerating the others. We establish the required sampling guarantees through new geometric bounds for structured public operators over prime and power of two moduli. The construction builds on the Wagner-style Gaussian sampling framework of Ducas, Engelberts, and Loyer (CRYPTO 2025) and the low-error decision-LWE algorithm of Han, Gao, and Hu (2026).
For quotient relations of NTRU type, we develop an affine slice search: fixing coordinates restricts candidate pairs to slices of the public lattice, and their estimated Gaussian masses guide the choice of each next coordinate. In the stated modulus window, Falcon's key generation quality condition supplies the required mass bound. The algorithm then recovers an equivalent signing key with high probability in time and space $2^{O(n/\ln\ln n)}$. The same search recovers the short key core for cyclic NTRU-HPS/HRSS.
Together, these results give subexponential algorithms for problem families associated with all seven NIST third-round lattice candidates. Despite the subexponential complexity, our results do not establish a reduction in the concrete security of the currently specified parameter sets.

---


### 115. [Magic Pen: Automatic Pen Mode Switching for Document Annotation](https://arxiv.org/abs/2610.11255)

**<font color=#1a73e8>作者：</font>** Kevin Desousa, Adam Bradley, Nathalie Henry Riche 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traditional digital pen interfaces use menu buttons to change the pen mode, which results in time and cognitive load spent on round-trip interactions and mode errors from tapping small mode selection buttons. This work presents the Magic Pen, a technique which uses machine learning to automatically switch between digital pen modes without requiring explicit mode changes. Magic Pen is driven by an LSTM model trained on pen data collected from 27 participants across two studies and uses transfer learning to iteratively tune the model towards how a specific user annotates. Error mitigation techniques using a flick gesture or on-screen tap are incorporated to correct mode errors or remove a stroke quickly. We evaluated Magic Pen in a comparative study with 18 participants, followed by iterative improvements and a deployment study with 8 participants. Magic Pen was preferred compared to a conventional menu-based approach, and transfer learning allowed for greater model predictability and stability.

---


### 116. [Residual spectral instabilities in representation learning](https://arxiv.org/abs/2610.11257)

**<font color=#1a73e8>作者：</font>** Zhen Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned representations can lose latent degrees of freedom successively, suggesting a cascade of transitions whose underlying stability principle remains unclear. Here we formulate dimension-wise posterior collapse in variational autoencoder (VAE) as a fluctuation theory around partially collapsed states. Interpreting the negative evidence lower bound as an effective free energy, its quadratic expansion defines a Gaussian theory whose Hessian acts as a mass matrix for latent fluctuations. We show that the collapsed directions form an invariant fluctuation sector and derive its exact mass spectrum in terms of a conditional residual operator. A local reactivation direction lowers the free energy when the decoder variance falls below the residual spectral upper edge, with equality marking marginality. The criterion recovers principal component thresholds in the linear Gaussian VAE limit. Viewed in reverse along continuously connected branches, the reactivation boundary provides a local criterion for successive collapse. Numerical continuation experiments show successive loss of latent dimensions near these spectral marginalities. These results support a spectral cascade interpretation governed by residual information left unexplained by the surviving representation.

---


### 117. [LR-V2X: Loss-Resilient Collaborative Perception under Low-Bandwidth Communication](https://arxiv.org/abs/2610.11264)

**<font color=#1a73e8>作者：</font>** Kang Yang, Tianci Bu, Peng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given the inherent unpredictability of packet loss in vehicular wireless communications, V2X collaborative perception can yield practical benefits only if agents can achieve reliable collaboration under lossy and low-bandwidth communication conditions. Existing dense BEV feature fusion methods depend on redundant BEV feature exchange, which is infeasible in low-bandwidth scenarios, while compact-communication methods aggressively compress messages but can hardly recover the missing feature content after packet loss. In this paper, we present LR-V2X, a loss-resilient, latent-space reconstruction framework that converts corrupted received latents (even under severe 90% packet loss) into a spatial prior and then reconstructs the missing BEV information from this informative prior and using ego context as condition. Notably, the model can be trained under complete communication conditions and can be directly applied to lossy conditions at test time, eliminating the need for training under numerous lossy conditions. Experiments on DAIR-V2X and V2XREAL show that LR-V2X delivers the strongest robustness under severe packet loss and preserves reliable collaboration as communication quality degrades. And it reduces communication overhead by $64\times$ compared to dense BEV feature fusion baselines. Code will be released at this https URL.

---


### 118. [TaReD: Tool-Aware Recursive Decomposition for Long-Horizon Tasks](https://arxiv.org/abs/2610.11268)

**<font color=#1a73e8>作者：</font>** Wei-Xiang Mao, Zhi-Kai Chen, De-Chuan Zhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents combine reasoning with tools to interact with external systems and complete real-world tasks. Early agents typically interleave reasoning and actions along a single execution chain. On complex tasks, this chain becomes unreliable because growing histories obscure intermediate dependencies and allow early planning errors to propagate. Recursively decomposing a complex task into smaller subtasks offers a natural solution, yet effective decomposition must account for the system's capabilities so that each subtask can be executed by the available tools. In realistic systems, however, tool libraries can be too large to expose in full. Injecting every tool description consumes substantial context while making relevant tools harder to retrieve and useful task boundaries harder to identify. We propose tool-aware recursive decomposition, which organizes tools by functional relationships into a hierarchy of capabilities. During execution, the agent discovers tools on demand and uses the hierarchy to recursively decompose a complex task into a subtask tree whose levels are aligned with the capabilities required at each stage. Experiments on complex real-world tasks show that the proposed method improves end-to-end task success rate by up to 40 percentage points over the compared baselines. The implementation of TaReD is available on GitHub: this https URL.

---


### 119. [Phonological Interference in Multilingual Speech Models](https://arxiv.org/abs/2610.11275)

**<font color=#1a73e8>作者：</font>** Moran Yanuka, Raja Giryes, Moris Alper  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Phoneme-level models transcribe or generate speech as a sequence of phonemes, the smallest sound units that distinguish words. These models enable fine-grained pronunciation control and understanding, yet often fail on input that does not match any single training language, such as speech alternating between two languages, known as code-switching, or low-resource languages absent from training. We identify a systematic failure mode behind this, phonological interference: models assume the input is in a single language and impose its phonology, overriding local phoneme-level decisions that conflict with the assumed language. We measure interference by how often a model retains phonemes that one language has but the other lacks. On code-switched input, two phone recognizers (speech-to-phoneme models) and a phoneme-conditioned text-to-speech model lose 32% to 79% of these phonemes, but lose far fewer of the phonemes both languages share. On unseen languages, we find that phone recognizers impose the phonology of the training language they assign to the speech, and the more confident the assignment, the more they lose phonemes the unseen language has but the assigned language lacks. We probe the models' language estimate from their internal activations, and trace interference to a low dimensional subspace. On monolingual speech, steering this subspace toward another language makes the model lose the phonemes that only the original language uses and produce phonemes that only the target language has. We introduce windowed language estimation (WLE), an inference time repair that replaces the model's language estimate in this subspace with one computed from a short window around each position. On code-switched input, WLE removes 34% to 69% of the interference in all three models, and in the recognizers it leaves monolingual performance essentially unchanged.

---


### 120. [Soft Voting for Policy-Aware Private Data Synthesis](https://arxiv.org/abs/2610.11285)

**<font color=#1a73e8>作者：</font>** Yingge Hu, Gautham Ramesh Babu, Mostafa Milani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blowfish privacy relaxes differential privacy (DP) by protecting only the attribute-value substitutions a data owner specifies as edges of a policy graph. A sparser policy can reduce the noise required by a mechanism, but only when the released statistic changes less across protected substitutions than across arbitrary DP neighbors. We study this question for evolutionary, nearest-neighbor DP synthesizers such as Private Evolution (PE) and its tabular instantiation Tab-PE, which score private records against a candidate population and release a noisy vote histogram. Their hard vote is constant inside each candidate's decision region and jumps at its boundary. Its policy-specific sensitivity therefore equals the full worst-case value whenever at least one protected substitution crosses a boundary, regardless of how short that substitution is. Because every round we examined contained such a substitution, the policy graph gave no reduction in noise. We propose BF-Soft, a temperature-smoothed soft vote whose response changes gradually with distance. Its sensitivity has a tight closed-form bound in the policy graph's reach and the temperature, independent of the number of candidates, and the bound can be computed once before synthesis. It also predicts from the policy alone when policy-aware smoothing cannot substantially reduce noise: protecting a flat categorical or binary attribute drives the reach to its maximum. On real and synthetic datasets under narrow numeric policies, BF-Soft reduces error relative to hard voting at strong privacy budgets, while the advantage reverses at weaker budgets. A public-data pilot predicts when soft voting is beneficial without spending private budget.

---


### 121. [Memorization and Malign Generalization in Conditional Diffusion Models with Random Features](https://arxiv.org/abs/2610.11288)

**<font color=#1a73e8>作者：</font>** Gwangho Kim, Sungyoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional diffusion models generate diverse, novel, and high-quality samples under prescribed conditions. However, theoretical understanding of their memorization and generalization remains limited, while recent works have characterized these behaviors primarily in unconditional settings. In this work, we analyze a random-feature conditional score model in the high-dimensional proportional limit, deriving asymptotic expressions for training and test losses. By decomposing the test loss, we show that in the overparameterized regime, increasing model width improves prediction of the condition-dependent mean while reducing within-condition prediction variance, a phenomenon we term "malign generalization." Furthermore, analyzing the training loss reveals that more informative conditions lead to memorization of training samples at smaller widths. These theoretical findings are supported by experiments with U-Net architectures on realistic data.

---


### 122. [ProxyEraseAgent: Blind Watermark Removal in the Wild](https://arxiv.org/abs/2610.11290)

**<font color=#1a73e8>作者：</font>** Jun Yao, Chao Wang, Yupeng Qiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Invisible image watermark removal has received growing attention. Despite substantial progress, existing attacks face a tension between practicality and specificity. Attacks exploiting detector outputs, decoder responses, or paired images can be tailored to the watermark decision boundary, but require information rarely available in realistic scenarios. Conversely, attacks based on compression, geometric distortion, or reconstruction are easily deployed from a single watermarked image, but remain largely open-loop: they apply generic transformations without knowing if the image is moving toward watermark failure. Thus, the key challenge in single-image blind watermark removal is not merely how to transform the image, but how to obtain a useful removal direction without accessing the hidden decoder.
To bridge this gap, we propose ProxyEraseAgent, an agent-driven framework recovering attack specificity through proxy decoder responses. Publicly available watermarking schemes provide a natural knowledge base of candidate decoders, where some are informative for a given unknown image. Our insight is that a decoder producing a strong calibrated response to the query image likely shares a nearby decoding boundary with the hidden target mechanism. ProxyEraseAgent ranks these decoders by calibrated response strength and uses the top ones as proxy boundary estimators. Their responses then guide a progressive search over heterogeneous removal operations (e.g., geometric distortion, JPEG compression, image reconstruction, and gradient perturbation) under perceptual-quality constraints. Experiments across 11 watermarking systems show ProxyEraseAgent achieves a 94.8% attack success rate, demonstrating the effectiveness of response-guided proxy retrieval and feedback-driven sequential planning for blind watermark removal.

---


### 123. [ORDO: Operation-level Round-aware Dynamic Ordering for MIP Presolve](https://arxiv.org/abs/2610.11294)

**<font color=#1a73e8>作者：</font>** Zehuan Chen, Chunhe Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Presolve strongly affects mixed-integer programming (MIP) performance, yet learning-based methods only optimize parameter configurations and cannot express the non-commutative temporal dependencies among actions, whose default order is nearly unique on most domains, yet functionally necessary: artificially shuffling the order of the same sequence inflates the tail of the solve-time distribution by up to several-fold. We recast presolve planning as autoregressive sequence generation over a unified atomic action space, moving the decision object to action sequences; we call this framework ORDO---Operation-level Round-aware Dynamic Ordering for MIP Presolve. Its payoff is cross-domain generalization: on multiple unseen domains it attains end-to-end zero-shot speedup---to our knowledge the first for presolve action sequences---varying by domain and not explained by corpus richness, the strongest domain reaching the largest speedup once racing is added. Deployment uses sequence racing, in which candidate sequences run concurrently and the winner is kept, enabled by an execution-and-observation facility, added by modifying the SCIP source, that injects sequences along the native path and records which actions actually execute and in which round.

---


### 124. [Spatial-Frequency-Aware Implicit Neural Representation of Multidimensional Signals via MLP-KAN Fusion](https://arxiv.org/abs/2610.11296)

**<font color=#1a73e8>作者：</font>** Wen Yan, Ligen Shi, Jun Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit Neural Representations (INRs) have emerged as a compelling paradigm for modeling multidimensional signals by mapping continuous coordinates to signal values. However, Multi-Layer Perceptrons (MLP)-based INRs inherently suffer from spectral bias, which favors low-frequency components and suppresses the reconstruction of essential high-frequency details. While existing techniques, such as Fourier feature mappings, mitigate this issue, they often rely on sensitive manual tuning and are prone to spectral artifacts. In this paper, we propose a spatial-frequency-aware INR framework that combines an MLP branch with a Kolmogorov-Arnold network (KAN) branch for complementary frequency-oriented modeling. The MLP branch provides a low-frequency-oriented representation of smooth structures, whereas the KAN branch complements localized variations and fine details. To coordinate the two branches, we integrate the discrete wavelet transform (DWT) and inverse discrete wavelet transform (IDWT) into the output fusion stage. The outputs of the two branches are decomposed into wavelet coefficients, and the corresponding coefficients are additively fused before inverse wavelet reconstruction. A wavelet-domain band-separation regularization further penalizes high-frequency responses in the MLP branch and low-frequency responses in the KAN branch, thereby encouraging complementary frequency-oriented behavior. Experiments on 1D signals, 2D images, 3D volumes and signed distance functions, videos, and 4D light-fields demonstrate the applicability of the proposed representation across the evaluated signal modalities. Results demonstrate improved reconstruction fidelity across the evaluated signal modalities.

---


### 125. [iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity](https://arxiv.org/abs/2610.11302)

**<font color=#1a73e8>作者：</font>** Chengfeng Han, Baole Ai, Xianlu Bian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free sparse attention offers a practical acceleration solution to Diffusion Transformers (DiTs) via reducing computations without fine-tuning. It typically involves estimating the importance of query-key regions and deriving sparse masks to compute only the important candidates, which inevitably introduces approximation errors that may degrade generation quality. To better balance the efficiency-quality trade-off, we propose iCATS, integrating improved importance estimation and sparse mask construction with an efficient hardware execution strategy. Specifically, for importance estimation, unlike previous works that perform independent clustering over query and key tokens based on feature similarity to estimate attention scores, iCATS demonstrates that clustering based on query-key dot-product interactions is more accurate and further reformulates this objective as a simple quadratic form for low-cost computation. For sparse mask construction, instead of using a fixed top-p rule, we observe that tolerance to sparse approximation errors varies across denoising timesteps and therefore introduce an SNR-guided sparsity schedule to adjust sparsity dynamically, leading to higher accuracy. Finally, for hardware execution, we devise a tail-merging strategy to reduce padding overhead caused by irregular cluster sizes, improving GPU kernel utilization. Extensive experiments show that iCATS achieves $2.03\times$ acceleration with 31.017 dB PSNR on HunyuanVideo-T2V-13B and $1.55\times$ acceleration with 29.301 dB PSNR on Wan2.1-T2V-14B, delivering a state-of-the-art efficiency-quality trade-off.

---


### 126. [Collaboratively Guided Adversarial Robust Distillation with Teacher-Favorable Examples](https://arxiv.org/abs/2610.11306)

**<font color=#1a73e8>作者：</font>** Zhi Li, Haowei Liu, Hongchen Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial distillation transfers robustness from high-capacity teachers to compact students. Existing adversarial distillation methods mainly use teacher predictions on clean or adversarial examples to supervise student learning. However, teacher-favorable supervision within the perturbation neighborhood remains underexplored in adversarial distillation. We therefore propose Collaboratively Guided Adversarial Robust Distillation (CGARD), which jointly optimizes distinct student-adversarial and teacher-collaborative examples within the same perturbation neighborhood. The teacher-collaborative example is constrained to incur no greater cross-entropy loss under the teacher than the clean input. CGARD combines collaborative teacher guidance with adversarial teacher supervision to improve robust knowledge transfer. Experiments on CIFAR-10 and CIFAR-100, including white-box evaluation and additional black-box transfer evaluation, demonstrate consistent robustness improvements over strong adversarial distillation baselines.

---


### 127. [NP-Hardness of Minimizing Neurons in Two-Hidden-Layer ReLU Neural Networks](https://arxiv.org/abs/2610.11313)

**<font color=#1a73e8>作者：</font>** Sangrock Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fundamental question in neural network architecture optimization is whether the minimum hidden-neuron count required to approximate a target function within a prescribed tolerance can be computed efficiently. This paper resolves this question for two-hidden-layer ReLU networks under an $L^p(\mathbb{R}^d,\mathbb{R}^m)$ approximation constraint. For every fixed $d \ge 1$, $m \ge 1$, and $1 \le p < \infty$, we prove that computing the optimum exactly is NP-hard. The result holds even when the target is represented by a rational ReLU network whose realization is nonzero, componentwise nonnegative, compactly supported, globally Lipschitz, and continuous piecewise affine. The polynomial-time reduction from 3-SAT produces an architecture gap in which unsatisfiable formulas yield an optimum of zero, whereas satisfiable formulas yield an optimum of at least $d+2$. The proof constructs compactly supported polyhedral frustum functions realized by two-hidden-layer ReLU networks and establishes the $L^p$-density of finite linear combinations of box-frustum functions. The results offer theoretical justification for employing heuristic approximation methods in the design of ReLU neural networks, illustrating that attaining a minimal configuration within polynomial time is computationally unachievable.

---


### 128. [MetaEncoder: Exploring the Limit of Bi-Encoders for Multimodal System One Decision Making with Natural Language Interface](https://arxiv.org/abs/2610.11316)

**<font color=#1a73e8>作者：</font>** Jianpeng Cheng, Guangyu Sun, Aashu Singh 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> System One models output constrained decisions and probability distributions rather than free-form text generation. While prevailing paradigms rely on structured schema objects to encode state, intent, and candidate choices, we revisit a fully natural language-based System One interface. In this framework, both the user request and each candidate option are expressed in natural language, supported by multimodal (image and video) auxiliary inputs. We introduce MetaEncoder, which fine-tunes a pre-trained Muse-Glimmer 30B decoder into an instruction-following decision-making encoder. To scale effectively across both small closed-set (< 256) and massive open-set (millions) candidate spaces, MetaEncoder employs a bi-encoder architecture trained via unidirectional contrastive learning for request-candidate alignment. We conduct extensive evaluations across 11 benchmark suites and 190 tasks spanning multimodal decision-making, understanding (closed-set) and retrieval (open-set), highlighting where MetaEncoder beats SOTA multimodal encoders, as well as its current limits on reasoning-intensive tasks.

---


### 129. [Finsler Flow Matching: Dynamics-Aware Geodesic Interpolation for Single-Snapshot Trajectory Inference](https://arxiv.org/abs/2610.11318)

**<font color=#1a73e8>作者：</font>** Niklas Canova, Jonas Simon Fleck  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Single-cell snapshot data can resolve a continuum of cellular states but do not uniquely determine the dynamics governing transitions between them. However, additional dynamical information can often be encoded in a cell-cell Markov transition kernel. Existing generative approaches for single cell trajectory inference either infer transport only from population marginals, impose a symmetric geometry on the state space, or incorporate directionality through a single velocity vector at each observed state. We introduce Finsler Flow Matching (FFM), a framework for learning continuous stochastic dynamics from discrete Markov transition graphs. We use the first and second local moments to construct a Finsler structure motivated by the Freidlin--Wentzell action, where the second moment determines anisotropic accessibility and the first moment introduces a preferred direction of motion. We learn neural approximations of the resulting directed geodesics, use their Finsler cost to construct source-target couplings, and define geometry-aware stochastic conditional paths that can be distilled into a continuous generative process through simulation-free score and flow matching. Across synthetic and single-cell trajectory inference benchmarks, FFM improves recovery of withheld intermediate populations, particularly when the transition dynamics are strongly directional or anisotropic. Our results provide a principled route from discrete transition probabilities to continuous generative dynamics while retaining both directional and diffusive structure.

---


### 130. [It's Always 10:10: Reference Images Break a Bias That Prompts Only Dent](https://arxiv.org/abs/2610.11320)

**<font color=#1a73e8>作者：</font>** Luca Cazzaniga  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models appear to reproduce the habits of the photographs they learned from. Analog clocks are an extreme case: in advertising, watches almost always show 10:10, and generated clocks return to 10:10 even when another time is requested. We measure this bias and test three ways of overcoming it on 52 models available on the Magnific platform, with a replication on Higgsfield. Every image shows three identical clocks that must show 2:35, 6:50 and 11:20. The description of the object is fixed and only the request about the time changes: no time (A), the time in digits (B), the hand positions described by construction relative to the dial numerals (C), or the same description plus a drawn reference dial (D). Two AI readers read all 1,799 images blind from coded copies, with a third reader and the author settling disagreements (dial-level agreement 96.0% and 97.3%). With no time requested, 67% of the images have all three clocks at 10:10. On the 20 current models, all three clocks are correct in 34% of the images with digits, 30% with the hands described in words and 75% with the reference dial (D-B: +37 points, 95% CI +28 to +45); we found no evidence that describing the hands in words beats the digits (C-B: -4 points, CI -10 to +1). The replication on the 12 models shared by both platforms gives the same picture (B 54%, C 50%, D 81%). Writing the time reduces the bias but leaves two thirds of the images of the 20 current models with at least one wrong clock; adding a drawn reference raises full accuracy to three quarters and almost eliminates images entirely at 10:10. We release all images, prompts, raw readings and a script that recomputes every result.

---


### 131. [TokenBank: Financial Infrastructure for AI Services](https://arxiv.org/abs/2610.11333)

**<font color=#1a73e8>作者：</font>** Cary Chang, Jialin Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI services incur inference costs during execution, while revenue may arrive later. Changing API prices, limited upfront capital, and service failures can limit operators' ability to sustain or expand their services. Beyond reducing per-request costs, operators need to plan future spending, fund execution before revenue arrives, and obtain compensation for specified losses. This requires clear agreements across services with different pricing and execution conditions. These agreements must distinguish rights to consume services from rights to receive payments, define obligations under uncertain costs and income, and specify which failures qualify for compensation and how much can be paid. We present TokenBank, a financial infrastructure that represents these commitments through structured contracts. It supports service-consumption rights, agreements that settle API-price differences in cash (forwards), financing through limited rights to future service revenue, and protection claims for specified service failures. Contracts specify participants, covered services, validity, ownership, fulfillment conditions, and settlement rules. Evaluation combines replay of 899,441 API requests, real model-driven agent execution, and contract API tests. In a zero-discount rising-price resampling scenario, forwards reduce mean expenditure by USD 304.88 but increase its standard deviation from USD 1,152.45 to USD 1,190.82. A controlled replication with five portfolios per capital condition finds mean contribution differences between financing and self-funding of +1.0635, -0.1406, and -0.2962 experimental USD under low, baseline, and ample capital, respectively. The evaluation distinguishes contract correctness from economic effectiveness under declared economic and failure assumptions; supplier invoices and commercial revenue are unavailable.

---


### 132. [Point-Focused Attention Meets Context-Scan State Space: Robust Biological Visual Perception for Point Cloud Representation](https://arxiv.org/abs/2610.11342)

**<font color=#1a73e8>作者：</font>** Kanglin Qu, Pan Gao, Qun Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synergistically capturing intricate local structures and global contextual dependencies has become a critical challenge in point cloud representation learning. To address this, we introduce PointLearner, a point cloud representation learning network that closely aligns with biological vision which employs an active, foveation-inspired processing strategy, thus enabling local geometric modeling and long-range dependency interactions simultaneously. Specifically, we first design a point-focused attention, which simulates foveal vision at the visual focus through a competitive normalized attention mechanism between local neighbors and spatially downsampled features. The spatially downsampled features are extracted by a pooling method based on learnable inducing points, which can flexibly adapt to the non-uniform distribution of point clouds as the number of inducing points is controlled and they interact directly with point clouds. Second, we propose a context-scan state space that mimics eye's saccade inference, which infers the overall semantic structure and spatial content in the scene through a scan path guided by the Hilbert curve for the bidirectional S6. With this focus-then-context biomimetic design, PointLearner demonstrates remarkable robustness and achieves state-of-the-art performance across multiple point cloud tasks.

---


### 133. [EvoSim: Learning to Model, Modeling to Learn](https://arxiv.org/abs/2610.11344)

**<font color=#1a73e8>作者：</font>** Yun-Wei Song, Jinkai Tao, Jun-Dong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physics-based models connect scientific explanation with quantitative prediction. Constructing them requires selecting physical processes, defining states and governing equations, specifying couplings, and identifying parameters from experiments. Existing AI systems remain limited in making these model structure decisions autonomously. We introduce EvoSim, a self-evolving AI scientist for physical modeling. It uses experimental discrepancies to drive mechanism and equation revisions and held-out experimental data to test physical plausibility. Exploration traces make updates to knowledge, skills, and multi-agent orchestration. This co-evolution improves physics-based models and EvoSim's ability to select mechanisms, diagnose failures, and coordinate research. We evaluate EvoSim on two industrial battery modeling tasks. It predicts lithium-metal-plating onset from 25 to 45 degrees Celsius and 2 C to 6 C with a mean absolute error of 1.79% in state of charge. Dynamic voltage prediction under vehicle driving conditions achieves a root mean square error of 7.62 mV, surpassing the reported accuracy of models developed by human experts. Self-evolution reduces model and physics errors by approximately 36% relative to baseline, demonstrating improved scientific modeling capability. EvoSim turns experimental observations into validated models and cumulative research expertise.

---


### 134. [EgoPhys: Estimating Peak Contact Force and Mechanical Work from Egocentric Manipulation Video](https://arxiv.org/abs/2610.11347)

**<font color=#1a73e8>作者：</font>** Zhuo Dong, Jianhua Yang, Haohao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physically grounded manipulation of articulated objects requires understanding both the maximum forces encountered during contact and the work performed as their parts move. Peak contact force and mechanical work quantify these complementary aspects, but estimating them from egocentric video is challenging because physical interaction cues are local and indirect. Moreover, peak force is associated with brief contact events, whereas mechanical work depends on force-motion coupling throughout the contact duration. To address these challenges, we propose EgoPhys, an RGB-only framework comprising Contact-Aware Spatial Aggregation (CASA) and Target-Specific Multi-Expert Temporal Routing (TMTR). CASA integrates appearance and geometry features to emphasize interaction-relevant cues, while TMTR models semantic, event, and motion cues with specialized temporal experts and routes them separately for force and work prediction. On the test split from Hoi! dataset, EgoPhys substantially improves predictions of peak force and mechanical work, achieving MAEs of \(5.205 \pm 0.584\) $N$ and $0.894 \pm 0.081$ $J$, respectively.

---


### 135. [Sample-Efficient Generative Conformal Prediction](https://arxiv.org/abs/2610.11349)

**<font color=#1a73e8>作者：</font>** Minxing Zheng, Shixiang Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative conformal prediction builds uncertainty sets from samples of a conditional generator, which are efficient only when the samples represent the response distribution well. This can require many samples, each of which can be costly, as in large diffusion models and scientific simulators, so the sampling budget must be used efficiently. Existing methods draw the same number of samples at every input, wasting samples where the response distribution is simple and undersampling where it is complex, which inflates sets and leaves those inputs under-covered. We propose CASA (Conformal Adaptive Sample Allocation), which characterizes the marginal value of an additional sample and allocates samples across inputs to minimize the expected set size subject to marginal coverage and an average sampling budget. Theoretical analysis shows that adaptive allocation yields smaller sets than a fixed count at the same budget: a missed mode forces a radius that spans the gap between modes, and even oracle radius cannot compensate for it. On synthetic and real tasks, CASA produces substantially smaller sets at the same budget, often improves conditional coverage, and complements existing radius-adaptive methods.

---


### 136. [Adaptive Adversarial Augmentation for Controllable Face Synthesis](https://arxiv.org/abs/2610.11356)

**<font color=#1a73e8>作者：</font>** Saransh Suri, Shivang Agarwal, Mayank Vatsa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic data provides a scalable alternative to real-world datasets for training face recognition models, particularly under challenging conditions such as low resolution, occlusion, and masks. Yet, most approaches lack diversity and fail to generalize effectively. We propose Ensemble Feedback Controllable Synthesis (EFCS), a guided framework that generates diverse and challenging samples while preserving visual realism. EFCS expands distributional variability, often reflected in higher FID and KID scores compared to single-feedback and random synthesis, while maintaining high precision. Recognition models trained on EFCS data consistently outperform baselines across multiple benchmarks, showing improved generalization to real-world scenarios. Furthermore, we introduce an analytically motivated formulation linking perturbation-induced difficulty, sample utility, and performance degradation, offering principled insights into balancing synthetic data complexity for optimal training. Together, these contributions establish EFCS as an effective and analytically grounded approach for bridging the gap between synthetic and real datasets.

---


### 137. [Bernoulli Flow Models: Self-Consistent Generative Modeling for Binary Data](https://arxiv.org/abs/2610.11362)

**<font color=#1a73e8>作者：</font>** Hao Mo, Liying Yang, Shumin Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Binary diffusion models typically require a large number of function evaluations (NFEs) to generate high-quality samples, making practical inference computationally expensive. Reducing NFEs while preserving sample quality without distillation or additional training remains a significant challenge. Existing binary diffusion models define a discrete one-step forward path and then derive the reverse posterior. In low-NFE settings requiring cross-step sampling, they approximate the true multi-step likelihood with a single-step likelihood transition, which severely degrades sample quality. To address this fundamental limitation and decouple the generative dynamics from fixed discrete time steps, we propose Bernoulli Flow Models (BFM). Rather than relying on sequential one-step Markov diffusion chains, BFM defines a unified continuous global Bernoulli probability flow path between data distributions and pure noise, from which we derive analytical closed-form posterior transitions over arbitrary time intervals. Consequently, reducing the inference NFE is no longer an approximation based on skipping discrete steps; it only requires re-evaluating the analytical posterior over a new time grid. This eliminates the structural training-inference mismatch inherent to discrete chains and yields self-consistent low-NFE sampling. Experiments show that BFM is highly robust to aggressive NFE reduction. On LSUN Churches 256x256, a BFM trained with 256 steps achieves an FID of 9.22 using only 16 sampling steps, whereas the state-of-the-art discrete baseline degrades to 204.10. BFM also remains competitive with continuous and discrete generative baselines under standard full-step inference. These results establish BFM as a theoretically rigorous, self-consistent, and practically effective framework for fast binary data generation.

---


### 138. [FlyMark: Training-Free Invisible Watermarking of 3D Gaussian Splatting via a Fruit Fly Connectome](https://arxiv.org/abs/2610.11364)

**<font color=#1a73e8>作者：</font>** Ziyuan Luo, Haoliang Li, Renjie Wan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A trained 3D Gaussian Splatting (3DGS) scene ships as a portable parameter array that can be copied, pruned, requantized, or repackaged outside its training pipeline, so ownership evidence is most useful when it lives in the released parameters and remains checkable long after the embedding tooling is gone. Existing 3DGS watermarks typically tie embedding or extraction to scene optimization, a learned decoder, or rendered views, so the evidence survives only as long as a second trained artifact does. FlyMark instead writes a keyed message into the parameters a 3DGS file already stores. Its carrier directions are derived from the photoreceptors of a published connectome, a citable versioned artifact that fixes the geometry exhaustively and leaves nothing to tune per scene. A virtual observer reads cone-wise apparent luminance along a scene-normalized orbit from stored centers, colors, and opacities; a keyed dithered quantization-index-modulation code replicates each message bit across these observations; and one sparse bounded least-squares solve realizes the targets through achromatic shifts of existing degree-zero colors under a hard per-channel linear-RGB bound. All geometry and higher-order appearance parameters are preserved bit-identically, and extraction needs only cone queries, rounding, and majority voting. Under a model-domain threat model on synthetic and real scenes, FlyMark attains high clean bit accuracy and visual fidelity while cleanly separating matched from wrong keys.

---


### 139. [CRISP: Fixing Flying Pixels in Latent LiDAR Generation via Diffusion Decoding](https://arxiv.org/abs/2610.11376)

**<font color=#1a73e8>作者：</font>** Andrea Ceron, Michael Schmidt, Alvaro Marcos-Ramiro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent LiDAR pipelines suffer from flying pixels: convolutional VAEs blur sharp radial depth discontinuities, yielding edge depths that back-project to points floating between surfaces. We identify this as a major, directly correctable decoder bottleneck and introduce CRISP: a pixel-space diffusion decoder with a backbone-agnostic latent adapter, DiT-based denoiser, and support mask predictor. CRISP replaces video-VAE and LiDAR-native decoders alike while keeping the encoder and latent generator fixed. Across KITTI-360, SemanticKITTI, and nuScenes, replacing only the decoder reduces FSVD/FPVD by 50.5% on average across frozen backbones; for generic video VAEs, the reductions reach 71%/74%. On the LiDAR-native LiDM backbone, FRID drops by 71%, with the largest gains at depth discontinuities. In a pretrained LiDM world model, the same zero-shot replacement improves FSVD by 15.5%, narrowing the sim-to-real gap.

---


### 140. [FastJEV: Understanding Redundancy for Compact JEV Inference](https://arxiv.org/abs/2610.11379)

**<font color=#1a73e8>作者：</font>** Jie Ma, Jie Gao, Yihang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> JEV models make multimodal decisions by directly scoring candidates. Although the common context is encoded once, candidate evaluation can still repeat matching token histories, duplicate inference states, and execute the full backbone. In this paper, we study these sources of redundancy and present FastJEV for compact candidate evaluation. We jointly organize history reuse and state storage, since sharing computation requires preserving states for later branches. We first introduce shared context anchoring to reuse recurrent initial states and omit unused final recurrent caches. We extend this reuse through candidate prefix sharing, retaining the intermediate states needed by subsequent branches. To further reduce the depth of these paths, we apply decision guided pruning based on relative score changes measured on a small unlabeled set. Our method retains full context encoding and all candidates without additional training. We evaluate FastJEV across three OmniJev model sizes on five public benchmarks and reconstructed LIBERO-10 offline questions. At the selected pruning budgets, the complete method reduces candidate depth by 43.75% to 45.83%, while retaining 93.66% to 97.52% of the original task scores on average across the six evaluation sets. Through controlled experiments, we show how candidate overlap and branching structure affect the execution cost of history reuse. In our implementation, candidate prefix sharing can reduce repeated computation while increasing latency. These findings motivate designing sharing granularity and execution schedules together for efficient JEV inference.

---


### 141. [Equal Path Cost, Unequal Output Effects: Understanding Perturbation Propagation in Diffusion Models](https://arxiv.org/abs/2610.11380)

**<font color=#1a73e8>作者：</font>** Wei Guo, Yaowen Zhang, Xingtong Ge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved remarkable success in generative modeling, with their sampling procedures routinely modified to control generation and improve efficiency. These modifications introduce perturbations along the sampling trajectory, raising a central question: how do such perturbations affect generated output? To address this question, we develop a theoretical framework to investigate perturbation propagation, combining dynamical analysis of the sampling process with an information-theoretic characterization of output responses. Within this framework, we quantify perturbation strength using the Kullback--Leibler (KL) divergence between perturbed and reference trajectory distributions, termed as path cost, which is shown to bound, but do not determine, changes in the output distribution. Building on this analysis, we derive a response identity that connects the propagation and accumulation of local perturbations with the information captured by a selected feature mean, explaining why changes in the output distribution can remain undetected by its first-order response. We test our theoretical analysis through controlled interventions at equal path cost in pretrained diffusion models, revealing distinct patterns of output sensitivity across sampling stages and spatial frequencies. To assess whether our framework can diagnose perturbations arising from practical approximations, we apply it to cache-based acceleration and show that our propagation analysis reliably identifies sampling intervals where caching causes larger image errors.

---


### 142. [EvoKnow: Continual Knowledge Evolution for AI-Generated Image Detection](https://arxiv.org/abs/2610.11381)

**<font color=#1a73e8>作者：</font>** Zhiheng Peng, Wenwei Jin, Yangshi Ge 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated image detectors are commonly trained on fixed generator domains and become difficult to maintain as new generative models emerge. Continual adaptation is challenging because replaying historical generated images is costly, whereas updating shared parameters with limited current-domain data can overwrite prior forensic knowledge. We propose EvoKnow, a replay-free framework that formulates continual AI-generated image detection as forensic knowledge evolution. EvoKnow preserves a shared forensic basis learned from base domains, incrementally adds isolated residual experts for complementary generator-relevant evidence, and retrieves expertise through an Analytical Incremental Router (AIR) updated in closed form from current-stage generated images and accumulated sufficient statistics. Experiments demonstrate effective cross-generator generalization, few-shot expansion, and long-horizon continual adaptation. With ten generated images per arriving generator, EvoKnow achieves 96.70% average accuracy on non-base GenImage generators and 94.48% accuracy on Chameleon without target-benchmark adaptation. Under a strict replay-free continual learning protocol, EvoKnow achieves state-of-the-art continual learning performance, attaining 96.32% mean stage-wise accuracy and 4.32% average forgetting.

---


### 143. [Fact over Fiction: Detection of Pathological Hallucinations in Sinhala-to-English Neural Machine Translation](https://arxiv.org/abs/2610.11389)

**<font color=#1a73e8>作者：</font>** Navam Obeysekara, Nevidu Jayatilleke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural Machine Translation (NMT) models, while capable of producing highly fluent outputs, remain vulnerable to hallucinations, which are translations that are natural yet semantically unrelated to the source. This vulnerability is acute in low-resource settings like Sinhala-to-English, where weak cross-lingual alignment leads to hallucinations. This paper introduces a framework for reference-free hallucination detection in this language pair. We present a 45,000-sample synthetic dataset generated through a probabilistic chain of five linguistically motivated corruption strategies, with a semantic rescue mechanism that uses character-level similarity to distinguish hallucinations from morphological variants. We fine-tune mDeBERTa-v3 for token-level sequence labelling, reaching a token-level F1 of 0.841 +/- 0.001 over three seeds on a source-disjoint test set, and study a three-signal ensemble integrating neural risk scores, sequence log-probabilities, and cross-lingual semantic embeddings (LaBSE). A source-ablation control shows that the detector relies on the Sinhala source rather than on surface artefacts of the corruption process: shuffling or removing the source reduces sentence-level AUROC from 0.970 to chance. We benchmark eight NMT systems spanning five model families and find that detector firings vary by an order of magnitude across architectures.

---


### 144. [TypedBench: A Benchmark for Calibration, Framing Sensitivity, and Cost in System One Decision Models](https://arxiv.org/abs/2610.11392)

**<font color=#1a73e8>作者：</font>** Rahul Sharma, Andrew B. Ducan, Gaétan Marceau Caron 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> System One models output calibrated probabilities over typed answers such as categorical choices, ordinal levels, or binary outcomes, via a non-generative interface. Software can act on these probabilities through thresholds, cost-weighted choices, and escalation rules. Consequently, if these probabilities are miscalibrated or wording-sensitive, the software ma take unintended actions leaving human operators with no textual rationale to inspect. Current evaluations largely report accuracy and calibration on public classification datasets without a clear reference. We present TypedBench, a benchmark for typed decision models like Jev built from seven policy-labelled generators and nine evaluation suites. We report accuracy as median and range across paraphrases, and calibration error relative to the finite-sample noise floor of a matched, perfectly calibrated predictor. We assess probability quality through selective prediction, ordinal proper scoring rules, and realised cost under asymmetric cost matrices. We evaluate a hosted model, an open encoder, and a family of open decoders spanning 0.8B-9B parameters on identical items. The hosted model follows the stated policy but is wording-sensitive and systematically underconfident; under asymmetric costs, using its probabilities can be worse than taking its top answer. Decoders route exactly and are slow as options or questions are added. The decoder is least accurate on policy questions and degrades with more options. Overall, typed decision models must be evaluated jointly on policy adherence, wording robustness, probability quality, and induced decision outcomes.

---


### 145. [CoPoE: Multimodal Fusion via Decomposable Disease-Coordinate Product-of-Experts for Missing-Modality Alzheimer's Diagnosis](https://arxiv.org/abs/2610.11394)

**<font color=#1a73e8>作者：</font>** Chihun An, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Alzheimer's disease (AD) diagnosis benefits from integrating heterogeneous clinical, imaging, genomic, and biomarker evidence, but clinical cohorts frequently suffer from irregular modality missingness. Existing fusion methods often synthesize absent inputs, risking the introduction of artificial surrogates, or pool available signals into uninterpretable latent spaces. We present CoPoE (Disease-Coordinate Product-of-Experts), a disease-coordinate framework that maps multimodal evidence into a structured latent space partitioned into four distinct biological and clinical axes: genetic Risk, molecular Pathology, Neurodegeneration, and clinical Stage (R/P/N/S). Each observed modality parameterizes a diagonal Gaussian expert over the full RPNS vector, and a masked Product-of-Experts architecture fuses only the available modalities. Consequently, absent modalities add no factor to the fusion path, allowing the network to preserve a robust, decomposable posterior for any non-empty modality subset without synthetic imputation in the RPNS path. Through extensive missing-modality experiments on the ADNI dataset, CoPoE achieves the best all-modality performance and the highest mean AUROC across all 15 observed-subset evaluations among standardized missing-modality fusion baselines under a shared non-PET ADNI embedding benchmark, while substantially improving raw-probability ECE, Brier score, and NLL. Furthermore, PET-supervised probing shows evidence enrichment within the pathology (P) block under full modalities, with tau-related signal retained even when direct fluid biospecimen inputs are withheld. Our code is available at this https URL.

---


### 146. [MORDOR:Mitigating Overheads of Read Disturbance Preventive Operations via Elastic Refresh Scheduling](https://arxiv.org/abs/2610.11398)

**<font color=#1a73e8>作者：</font>** Maria Makeenkova, Ataberk Olgun, F. Nisa Bostancı 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern DRAM chips are susceptible to read disturbance phenomena such as RowHammer, where repeatedly accessing (hammering) a row of DRAM cells (i.e., a DRAM row) induces bitflips in other physically nearby (victim) DRAM rows. A common practice to avoid such bitflips is to preventively refresh victim rows that might otherwise experience bitflips. Unfortunately, preventive refreshes cause long latencies and need to be performed urgently before the aggressor row is activated again to ensure data integrity. This is done by prioritizing them over demand memory requests, thereby potentially imposing significant delays on those requests and causing performance and energy overheads. Our goal in this work is to alleviate these overheads by scheduling preventive refreshes off the critical path of demand memory requests. We propose MORDOR, a new preventive refresh scheduling policy that significantly reduces system performance degradation and energy consumption caused by preventive refresh operations. MORDOR is integrated into the memory controller and operates alongside memory-controller-based read disturbance mitigation techniques to intelligently delay preventive refresh operations, while maintaining their data integrity guarantees. MORDOR leverages the key observation that a preventive refresh operation targeting an aggressor row can be delayed to serve any other demand memory request, as long as that memory request does not access the aggressor row. By doing so, MORDOR executes latency-critical memory requests before long-latency preventive refresh operations, while mitigating read disturbance bitflips. We evaluate MORDOR by integrating it into six state-of-the-art read disturbance mitigation techniques. Our comprehensive evaluation shows that MORDOR significantly improves system performance and energy efficiency at low area cost.

---


### 147. [Learning from Hetero Density for Cryo-EM Protein Reconstruction](https://arxiv.org/abs/2610.11403)

**<font color=#1a73e8>作者：</font>** Xu Han, Chaozhuo Li, Xiaowei Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing protein structures from cryo-electron microscopy (cryo-EM) maps is essential for understanding macromolecular assemblies. Although learning-based methods have improved protein reconstruction, information from hetero components remains underused. Our analysis finds both false predictions and reference protein sites near hetero components; filtering nearby candidates can improve or impair chain construction. We introduce CryoCue, a framework that uses hetero information to guide protein reconstruction. An anchor-supervised detector learns hetero representations across five component classes. Multiscale hetero features guide backbone localization, while predicted hetero candidates condition structure refinement through their class, confidence, and frame-relative geometry. Experiments show that CryoCue improves backbone localization near hetero components and achieves more accurate protein structure reconstruction.

---


### 148. [MC-TRCM: Observation-Aware Recursive Fusion for Incomplete Mobile and Wearable Mental-Health Feature Views](https://arxiv.org/abs/2610.11408)

**<font color=#1a73e8>作者：</font>** Wentao Wang, Lifeng Han, Zining Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Public mobile and wearable mental-health datasets often provide summarized feature tables rather than synchronized raw sensor streams. In these releases, each anchor corresponds to a survey or label time and may combine phone or wearable summaries, prior symptom scores, demographics, clinical variables, and source-availability indicators. We propose the Modality-Conditioned Temporal Recursive Context Model (MC-TRCM), which preserves each feature source as a separate token and incorporates missingness as part of the input context. Observed sources are encoded with values and missingness summaries, absent sources use learned absence tokens, dataset and task embeddings condition fusion, and a recursive prediction head refines each output over validation-selected steps. We evaluated MC-TRCM on six predefined endpoints from DepreST-CAT and Prediction of Severity Change-Depression (PSYCHE-D) using participant-level splits and validation-only model selection. MC-TRCM achieved the lowest mean absolute error on DepreST-CAT Patient Health Questionnaire-9 (PHQ-9) and Generalized Anxiety Disorder-7 (GAD-7) severity, improving over the best tabular reference by 0.181 and 0.217 scale points. Classification endpoints showed task-dependent behavior: MC-TRCM matched the best rounded GAD-7 category balanced accuracy, was numerically highest by 0.002 balanced-accuracy points on PSYCHE-D multiclass prediction, and remained close to the strongest references on PHQ-9 category and PSYCHE-D binary prediction. Ablations support Feature-wise Linear Modulation, absence tokens, missingness projections, and recursive refinement, while calibration and feature-source controls characterize endpoint behavior. Our code is available at this https URL.

---


### 149. [Fresco++: Frequency-Guided and Canonical-Consistent Optimization for Fine-Grained Head Avatar Modeling](https://arxiv.org/abs/2610.11412)

**<font color=#1a73e8>作者：</font>** Shikun Zhang, Yong Li, Yiqun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Fresco++, a unified optimization framework for fine-grained and view-consistent head avatar reconstruction. Head avatar optimization is typically driven by per-view image supervision, which can lead to premature fitting of unstable high-frequency details and inconsistent local appearance across viewpoints. Fresco++ addresses these challenges by regulating both the progression of visual detail and the formation of cross-view supervision during optimization. For frequency-aware optimization, a progressive curriculum first stabilizes low-frequency structures and then introduces high-frequency constraints to recover fine facial and hair details without amplifying spurious responses at early stages. For cross-view optimization, we introduce Canonical Group Consensus, which associates local observations through shared canonical surface regions and establishes correspondence across different viewpoints. Geometric and visibility-aware screening removes unreliable observations, while the remaining multi-view evidence is aggregated in feature space to form a consensus target for supervising the current rendering. This design enforces local consistency without relying on a specific image-space parameterization and avoids additional rendering of the auxiliary view. Together, the frequency curriculum and canonical consensus provide stable optimization from coarse structures to fine details while maintaining coherent appearance across viewpoints. Extensive experiments on NeRSemble demonstrate improved reconstruction quality and cross-view consistency, while evaluations across diverse avatar representations further confirm the generality and transferability of Fresco++.

---


### 150. [Missing Modality-Aware Calibration for Trustworthy Brain Tumor Segmentation](https://arxiv.org/abs/2610.11419)

**<font color=#1a73e8>作者：</font>** Sol Lee, Hyunji Kim, Sungrae Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal brain tumor segmentation typically leverages multiple MRI modalities, yet incomplete modality acquisition is common in clinical practice due to protocol heterogeneity and scan failures. Although recent methods maintain segmentation accuracy under missing modality conditions, they frequently overlook prediction reliability, leading to miscalibrated confidence estimates that hinder clinical adoption. Existing calibration techniques are largely modality-agnostic or assume that prediction difficulty decreases monotonically as additional modalities become available. However, in brain tumor segmentation, prediction difficulty depends primarily on which modalities are absent rather than how many, leading to combination-specific and spatially heterogeneous calibration errors. To address this, we propose Missing Modality-Aware Local Temperature Scaling (MMA-LTS), a post-hoc voxel-wise confidence calibration method. It estimates a spatially adaptive temperature field conditioned on a modality-availability learnable token and a voxel-wise difficulty score. Experiments on BraTS 2020 and FeTS 2024 show that MMA-LTS improves calibration while preserving the segmentation accuracy of state-of-the-art models across diverse missing-modality scenarios, thereby enhancing trustworthiness toward clinical deployment.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-329](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
