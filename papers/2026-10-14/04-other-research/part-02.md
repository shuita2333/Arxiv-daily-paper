# 📦 其他研究 | 2026年10月14日

> 本类共 **244** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-244](./part-05.md)

---

### 51. [Structure-Aware Matching for Robust UAV Thermal-to-Satellite Geo-Localization](https://arxiv.org/abs/2610.12835)

**<font color=#1a73e8>作者：</font>** Chun Liu, Yuxin Wang, Zhenxiang Huo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV thermal-to-satellite geo-localization localizes UAVs by matching real-time thermal images against georeferenced satellite images, enabling autonomous navigation in GNSS-denied and low-visibility conditions. However, substantial cross-modal disparities in color, brightness and viewpoint hinder conventional appearance-based methods from establishing reliable correspondences. While existing approaches predominantly address global modality shifts, they overlook the invariant scene structures inherently shared between thermal and satellite views. To bridge this gap, we propose SAMF, a Structure-Aware Matching Framework that explicitly exploits stable cross-modal structural cues to improve UAV thermal geolocalization. Specifically, the Directional Structure Enhancement Module (DSEM) strengthens robust structural representations by capturing directional and low-frequency spatial patterns, and the Modality-Aware Affine Remapping Module (MARM) subsequently applies affine correction to these enhanced features, further promoting cross-modal alignment. Additionally, we introduce the Thermal-UAV-Paired benchmark derived from the Thermal-UAV dataset. Extensive experiments on both the Boson-nighttime and Thermal-UAV-Paired datasets show that SAMF achieves state-of-the-art performance. Ablation studies further validate the effectiveness and synergistic complementarity of DSEM and MARM. The code and dataset are released at: this https URL.

---


### 52. [Fear Is Not Always Fear: Variation in Emotion Label Equivalence Across Datasets](https://arxiv.org/abs/2610.12841)

**<font color=#1a73e8>作者：</font>** Emily Öhman, Anna Koufakou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion classifiers are routinely applied beyond their training data, on the assumption that same-named labels such as fear or surprise mean the same thing across resources. We test this assumption for five labels shared by GoEmotions, XED, and BRIGHTER, comparing models on identical inputs and under cross-corpus transfer. On the same texts, one fear classifier flags 71% as fearful and another 8%, yet the two largely agree on how the texts rank. Across 30 resource-label comparisons, training-label prevalence explains about half of this kind of scale mismatch, and a fitted intercept removes most of it. What recalibration cannot repair is larger: transferred models lose 55% of native discrimination in aggregate, agreement in ranking between classifiers is only weakly related to that loss, and for surprise the resources disagree about which texts express the emotion. The choice of training resource can therefore change conclusions: on two external tweet collections, BRIGHTER- and XED-trained classifiers give opposite answers about which shows more surprise, even after rank normalization, with intervals excluding zero in both directions. A shared emotion label name does not establish an interchangeable measurement target.

---


### 53. [APEX: Asynchronous Prefix Denoising for Extreme Compression](https://arxiv.org/abs/2610.12843)

**<font color=#1a73e8>作者：</font>** David Dinkevich, Nisan Chiprut, Yoav HaCohen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fewer latent tokens promise cheaper diffusion. Yet aggressive latent compression creates a reconstruction-generation dilemma: adding channels improves reconstruction but makes generation harder. We introduce APEX, short for Asynchronous Prefix denoising for EXtreme compression, which pairs a hierarchical latent space with asynchronous denoising over channel groups. Our autoencoder orders channel prefixes from structure to detail, while one shared denoiser generates them at staggered local times without adding tokens. On ImageNet-512, APEX outperforms existing methods at every evaluated channel count under 64x and 128x compression. At matched training and guided sampling compute, it also outperforms a 256-token model at every evaluated budget, with larger gains at lower compute. Code is available at this https URL.

---


### 54. [Towards Defining, Measuring, and Leveraging Creativity in AI Applications](https://arxiv.org/abs/2610.12845)

**<font color=#1a73e8>作者：</font>** Jingyi Yang, Alexander Tuzhilin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite extensive research, computational creativity still lacks a conceptually grounded, practically relevant, and empirically applicable formal definition across contexts such as art, scientific research, and games. Existing approaches to creativity often focus on proposing informal conceptual definitions without providing formal computational concepts. Alternatively, they propose formal definitions without carefully examining their underlying assumptions or providing validation of these definitions by testing their performance in specific application settings. To address these problems, this paper proposes several formal postulates of creativity grounded in prior psychological work on creativity, especially as related to Boden's three core criteria of creativity: newness, value, and surprise. Furthermore, we propose a conceptual mathematical definition of creativity that aligns with these postulates. We also validate our proposed creativity formula in two applications: determining the creativity of particular chess moves, and assessing the creativity of paintings by some artists, such as Picasso, Renoir, and other painters. Experimental results demonstrate that our formula of creativity successfully captures creative patterns across both the chess and the art domains. This suggests that creativity can be effectively characterized through a unified mathematical structure based on three fundamental criteria, namely newness, value, and surprise, whose specific measurements are adapted to the particular domains.

---


### 55. [When Generative Models Act as Simulators](https://arxiv.org/abs/2610.12847)

**<font color=#1a73e8>作者：</font>** Sevan Brodjian, Michael Hobley, Pietro Perona  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A simulator summarizes an environment in a state that users can read and change. Generative models learn representations of the world without explicit specification, but offer no built-in way to edit that world's state. We investigate the conditions under which a generative model can act as a simulator through $\textit{editability}$: whether changing a model's latent representation produces the next-step outputs we get by editing a simulator's state. Plainly stated, our goal is to find a mapping between a generative model's latent state and the simulator state, where the model is trained on observations alone and the mapping is learned afterward. We test two kinds of mappings, both learned from observations paired with simulator states. In one, we train probes to decode the simulator state from the model, then steer along them. In the other, we learn the mapping directly with an inverse map, which can succeed even where steering fails. We study both in two contrasting environments: the discrete board game Othello, and Rayworld, our own continuous world of moving discs seen through partial renderings, closer to physical scenes and video. We find that which mapping succeeds depends strongly on the environment, even though the state is decodable in every variant. In Othello, editability falls smoothly as the game is simplified, and even small rule changes have large consequences. In Rayworld, probes fail to steer along the simulator's continuous state, yet an inverse map sets the model from that state anyway. A model can therefore be driven by a simulator it may have never learned.

---


### 56. [Reinforcement Learning via Fixed-point Flow Matching](https://arxiv.org/abs/2610.12848)

**<font color=#1a73e8>作者：</font>** Denis Blessing, Onur Celik, Gerhard Neumann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In maximum entropy and behavior-constrained reinforcement learning (RL), the optimal policy is given by a Boltzmann distribution. Generating samples from this distribution can be challenging, as it is often complex and multimodal. While flow policies trained with flow matching provide a powerful framework for representing such distributions, they traditionally rely on access to training data, which is generally unavailable in online RL. To address this limitation, we propose fixed-point flow matching (FFM), a data-free procedure for training and fine-tuning flow policies in RL. FFM leverages the target flow identity to formulate the actor update as a fixed-point iteration, utilizing a flow-matching-style regression objective where the critic's action gradients serve as regression targets. We show that the optimal policy is a fixed point of this iteration. Through extensive experiments, we demonstrate that FFM effectively fine-tunes pretrained flow policies in the offline-to-online setting and enables efficient and accurate training of flow policies from scratch in online RL. These results establish fixed-point flow matching as a principled approach for learning expressive flow-based policies without requiring training data.

---


### 57. [Unreliable Narrator Framing as a Cost-effective Mechanism for Satire Explanation of Australian and American Satirical News](https://arxiv.org/abs/2610.12863)

**<font color=#1a73e8>作者：</font>** Kanay Gupta, David Y. Liu, Aditya Joshi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Satirical news is a unique form of misinformation: it is intended to be humorous by the original publication source but can be misinterpreted. Explanation of satirical news articles is challenging because recent and local context needs to be incorporated. This is a pilot study that explores explanation generation for satirical news articles from Australia and compares them alongside those from USA. The paper demonstrates that framing explanations on unreliable narrator theory on open-weights models can be a feasible, cost-effective alternative to frontier models. We find that models identify the satirical tropes more accurately on the American source than the Australian one. This work results in a novel dataset and an evaluation benchmark for satirical explanation.

---


### 58. [Time Delay System for Sequence Modeling](https://arxiv.org/abs/2610.12864)

**<font color=#1a73e8>作者：</font>** Youshan Zhang, Jialu Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing sequence models share a critical limitation: they lack an explicit, interpretable mechanism for content-aware temporal recall. LSTMs compress everything into a single hidden state, thereby losing information about specific past events. Transformers attend to all tokens indiscriminately at quadratic cost, while state-space models like Mamba compress history into a fixed-dimensional state without explicit content-addressable memory. To address this gap, we introduce a novel framework grounded in nonlinear time-delay systems, in which the effective delay is dynamically estimated based on the semantic similarity between current and historical inputs. Our approach features three key innovations: (i) a differentiable semantic lag estimator that computes content-aware soft attention weights over history, producing a weighted historical context and similarity score; (ii) a diagonal state space with closed-form cumulative sum solution, achieving O(1) per-step complexity with no sequential loops; and (iii) an interpretable fuzzy semantic modulation mechanism that learns context-dependent rules for balancing instantaneous processing versus historical recall, where rule centers correspond to prototypical semantic contexts. Experimental results on text classification and generation outperform state-of-the-art methods.

---


### 59. [Selective Spatio-Temporal Fruit Inspector (S$^2$FI): A Mamba-based Framework for Rotational Fruit Quality Assessment](https://arxiv.org/abs/2610.12868)

**<font color=#1a73e8>作者：</font>** Hao Tian, Jie Hu, Guoqi Shan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The global fruit and vegetable industry confronts severe post-harvest sorting challenges for small and medium-scale growers. Large intelligent sorting systems are too costly, while manual sorting suffers from low efficiency, inconsistent standards, and high labor demand. To bridge this gap between expensive equipment and inefficient manual work, this study develops a low-cost, high-efficiency, lightweight fruit sorting system driven by deep learning, suitable for small and medium growers. We propose the Selective Spatio-Temporal Fruit Inspector (S$^2$FI) architecture, which combines a 3D convolutional encoder with a Mamba-based this http URL efficiently extracts spatiotemporal features, adaptively weighs informative frames during fruit rotation, and models long-range dependencies with linear complexity, reducing motion blur and occlusion. The hardware uses a dual-conveyor and curved rail design, supporting household power, fast deployment, and lightweight embedded deployment to improve affordability. We also built a conveyor-based fruit quality video dataset with 6,460 samples. Experiments on the held-out test set show that our method achieves the best trade-off among accuracy, efficiency, and practicality, outperforming the compared baselines on the test set, achieving an excellent balance of accuracy, speed, and practicality for real-world sorting.

---


### 60. [ROSETTA: Rotation Subspace Estimation for Training-free Transmodal Alignment](https://arxiv.org/abs/2610.12871)

**<font color=#1a73e8>作者：</font>** Alex Junho Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a query must be matched against a database built with a different sensor or processed by a different encoder, the independently trained encoders impose distinct coordinate systems on the feature space. No canonical reference frame exists to which all encoders can be aligned, and no single training procedure has fully closed this gap. We show that the relative transformation between any two such systems is a spatially preserving rotation in whitened feature space, whose angular velocity exhibits white-noise characteristics: large in norm, temporally uncorrelated, and unpredictable from the features themselves. However, the cross-covariance between encoder outputs has low effective rank, constraining only a small fraction of the rotation parameters, therefore local alignment is tractable. ROSETTA is a training-free calibration layer that estimates the local rotation via an expectation-maximization procedure, requiring no coobservation at query time. We validate ROSETTA on three public driving datasets spanning LiDAR, camera, thermal, and event modalities in cross-modal, cross-device, cross-representation, and cross-backbone settings, with milliseconds overhead per query.

---


### 61. [Beyond the Monolithic Interface: A Research Agenda for Plural Conversational AI](https://arxiv.org/abs/2610.12878)

**<font color=#1a73e8>作者：</font>** Avijit Ghosh, Afifah Kashif, Isabelle Kohout 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The current paradigm of artificial intelligence (AI) design elevates conversational chatbot interfaces, making them the default mode through which hundreds of millions of people interact with AI systems globally. This narrative review identifies three related harms produced by the single-voice chatbot interface, drawing on insights from literature in cognitive science, political studies, AI alignment, game design and human computer interaction. Firstly, cognitive offloading of user thinking, secondly, ideological narrowing of user beliefs, and thirdly, epistemic compression of cultural and value diversity. We then propose multi-persona interfaces, in which multiple personas are presented to the user simultaneously, as a cost-effective intervention that addresses all three harms at once. We ground this intervention in traditions the AI literature has largely overlooked, drawing on techniques from game design and participatory simulation, including the magic circle, role differentiation, and persona embodiment. We propose a taxonomy for the future design of multi-persona interfaces, and call for a research agenda that closes the gap between technical pluralistic alignment methods and empirical studies of human-AI interactions with pluralistic interfaces.

---


### 62. [CoGameReg: Cooperative-Game-Based Collaborative Semi-Supervised Regression for Seismic Reservoir Property Prediction](https://arxiv.org/abs/2610.12884)

**<font color=#1a73e8>作者：</font>** Zhiyu Guo, Jiwei Jia, Lei Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of reservoir properties from seismic data remains challenging when well-log labels are sparse but three-dimensional seismic observations are abundant. We present CoGameReg, a cooperative-game-based semi-supervised regression framework that uses contribution-weighted predictions of heterogeneous regressors to construct shared pseudo-labels. This design makes each regressor's influence explicit in the learning targets generated for unlabeled seismic samples under sparse well control. The Tri-Game Shapley mechanism combines a rank-MSE performance game with a pairwise consistency game to estimate nonnegative regressor weights from labeled training data. These weights remain fixed during collaborative training and are reused for final prediction fusion. Candidate pseudo-labels are screened using a common local k-nearest-neighbor error-reduction criterion before retraining. We evaluate CoGameReg on 10 public regression datasets, a synthetic three-dimensional P-wave velocity prediction task, and a field water-saturation application. The benchmark advantage is most pronounced at the 2.5% labeled-data ratio and decreases as supervision increases. CoGameReg obtains the best blind-well metrics in the synthetic experiment. In the field application, predictions clipped to 0-100% yield a pooled coefficient of determination of 0.5942, a root mean square error of 5.7441 percentage points, and a Pearson correlation of 0.8265 across three blind wells. CoGameReg has the highest Pearson correlation among the four field methods. The results support the use of CoGameReg to integrate sparse well labels with dense seismic attributes, with performance varying across metrics and well locations.

---


### 63. [Win-Win Fusion: Multi-Modal Image Fusion with Visual-Semantic Collaboration](https://arxiv.org/abs/2610.12887)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Xuhui Zuo, Jiayi Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing multi-modal image fusion (MMIF) methods generally face an optimization gap between the visual and semantic domains, limiting the enhancement of perception capabilities. To overcome this long-standing barrier, this work proposes W2F, a new visual-semantic mutual reinforcing paradigm for MMIF. First, we reinforce the foundation for visual-semantic collaboration by amplifying feature complementarity through two targeted designs. Specifically, the segmentation-guided fusion loss introduces object-aware structural guidance into visual fusion, while the embedded information restoration prior strengthens the ability of visual fusion to provide reliable perceptual evidence for the semantic branch under degraded conditions. Then, we introduce a strong multi-modal information interaction mechanism composed of interactive gated mixed attention (IGM-Att) and progressive coupling attention (PC-Att). These modules ensure comprehensive scene representation from both local and global perspectives, providing informational support for visual-semantic collaboration. Finally, we construct a collaborative mechanism to couple visual fusion and semantic fusion. It employs a feature search module to extract complementary key features from both tasks, enriching the representational potential of visual and semantic information. Meanwhile, a gradient correction strategy ensures collaboration from the optimization perspective, enhancing performance for both visual and semantic fusion through consistency learning. Extensive experiments demonstrate that W2F surpasses state-of-the-art methods in both visual appeal and decision accuracy. The code is publicly available at this https URL.

---


### 64. [The AI Side of the Human-AI Companion Relationship: Contributions to Users' Mental Models](https://arxiv.org/abs/2610.12891)

**<font color=#1a73e8>作者：</font>** Richard A. Fabes, Carol Lynn Martin, Gautam Dasarathy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> For many users, the relationship they have with an AI companion (AIC) feels genuinely mutual. The AIC appears to be attentive, empathic, and responsive, and the exchange can feel like two parties reacting to each other in real time. As a result, the user's mental model of relational adaptation correctly represents the AIC's responsiveness and change, but the mechanisms producing this may not be what the user thinks they are. In this paper, we illustrate how an AIC's apparent mutual engagement is generated without a persisting relational subject on the other side and without a self that persists between prompts. Despite this, we show that both the human and the AIC are changed by the interaction, but these changes occur at different levels. The change in the person is constitutive (i.e., intrinsic), but the change in the AIC is configurative (i.e., external and editable), and it is this difference in level that explains how the AIC contributes to a sense of mutuality. Importantly, we highlight how the mental models users develop regarding AIC mutuality may misrepresent its mechanisms and ontological significance. Specifically, we discuss how the ways in which AICs respond to a user contribute to the user's inaccurate inference that the AIC's adaptation is constitutive rather than configurative and how this can lead users to assign unwarranted interpersonal significance to the mutuality of the relationship. The paper specifies the implications this has for users, researchers, and AIC designers.

---


### 65. [Vulnerable Models in the AI Supply Chain: An Empirical Study of Adoption, Propagation, and Usage Patterns](https://arxiv.org/abs/2610.12893)

**<font color=#1a73e8>作者：</font>** Anh Nguyen, Triet Huynh Minh Le, M. Ali Babar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid integration of Artificial Intelligence (AI) models has established a complex supply chain, but many of these shared artifacts harbor severe vulnerabilities such as insecure serialization and architectural backdoors. While prior efforts have extensively scanned model registries to flag malicious artifacts, a critical gap remains in understanding how developers actually adopt and integrate these unsafe models into downstream software systems. We bridge this gap by conducting a large-scale empirical study on the usage and propagation of 16,977 known vulnerable models on HuggingFace flagged by InsightDB. We track their prevalence across GitHub repositories, software packages, fine-tuning chains, and deployed applications. Our analysis reveals that, despite being publicly flagged, these vulnerable models appear in over 21,000 code locations across more than 5,000 open-source repositories, with 3,757 distinct flagged models (22.1\%) actively referenced in at least one project. To understand how these models are integrated in code and identify recurring usage patterns, we categorize and analyze the recurring patterns surrounding them via a customized pipeline that combines Code Property Graphs extraction with a tailored Frequent Subgraph Mining approach. Across all patterns, we find no evidence of provenance verification or model sanitization logic, with developers frequently bypassing security parameters or delegating trust to permissive framework defaults. These findings underscore that scanning model files alone is insufficient, highlighting the urgent need for context-aware security analysis and stricter integration guardrails at the application layer of the AI supply chain.

---


### 66. [MeshBind: Point-to-Mesh Binding for Non-Rigid Scene Flow Automatic Annotation](https://arxiv.org/abs/2610.12895)

**<font color=#1a73e8>作者：</font>** Yinqi Chen, E Li, Shuaijun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene flow estimation is essential for many autonomous driving (AD) and robotic applications, but obtaining ground-truth scene flow for non-rigid objects such as pedestrians is highly difficult. We present MeshBind, an automatic annotation method that uses mesh models to generate per-point scene flow for non-rigid objects. The novelty of this work is threefold: 1) developing a multi-view module that reconstructs an articulated mesh model from six surround cameras and registers it to the LiDAR frame; 2) developing a local-frame binding technique that attaches each point to the mesh via a per-triangle tangent-normal frame, invariant under rigid motion yet adaptive to articulated deformation; 3) developing a three-layer flow registration pipeline that combines ego-vehicle motion compensation, box binding, and mesh binding to produce full-scene per-point flow. We implement MeshBind in SF-Studio, an interactive annotation tool that visualises flow and allows human mesh corrections with automatic recomputation. We also release SFB (SUScape-Flow Benchmark), a large-scale benchmark built on the public SUScape dataset, covering 41k frames with per-point non-rigid pedestrian annotations and a Rigid/Semi-Rigid/Non-Rigid evaluation protocol. Experiments show that fine-tuning on SFB reduces three-way endpoint error (EPE) by 2-3x, and brings non-rigid EPE to the same level as rigid EPE.

---


### 67. [AD-SRF: Attack-Defense Semantic Reinforcement for Multi-Modal Image Fusion](https://arxiv.org/abs/2610.12897)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Zhiqian Zheng, Linfeng Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing image fusion methods struggle to balance visual quality and semantic attributes due to the inherent conflict between their optimization objectives. To address this challenge, we propose an attack-defense semantic reinforcement framework for multi-modal image fusion, termed AD-SRF. By decoupling the optimization of these two aspects and then losslessly reintegrating them, this framework injects rich semantic attributes into the fused image without compromising its visual quality. First, we develop a transformer-based restorative visual fusion network as a strong visual baseline. Equipped with the cross-modal retrieval module and the information restoration-fusion collaborative loss, it produces highly visible fused images even under degraded conditions. Second, we introduce an attack-defense game mechanism to strengthen the semantic attributes of the fused images. The attacker learns perturbation patterns that impair downstream segmentation, whereas the defender restores missing semantics from the original inputs and reintegrates them into the fused image through an imperceptible semantic map. Through iterative adversarial interaction, this mechanism drives the defender to continually strengthen the fused image's semantic attributes, boosting downstream segmentation performance without compromising visual quality. Extensive experiments demonstrate that AD-SRF achieves a win-win performance in both visual quality and semantic attributes. The code is publicly available at this https URL.

---


### 68. [A Lightweight Velocity Correction Framework for Improving Instruction Following in Few-Step Text-to-Image Generation](https://arxiv.org/abs/2610.12899)

**<font color=#1a73e8>作者：</font>** Yating Gao, Zhenlong Zhu, Wen Zihao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step text-to-image generators produce high-quality images with few network forward passes, yet struggle with complex prompts involving multiple subjects, interactions, spatial relations, counting, and attribute binding. Can these errors be reduced without changing the generator's parameters or increasing its forward-pass count? We propose a lightweight correction framework for a frozen 6B-parameter generator. The generator predicts velocities that determine how its intermediate image representation is updated; a corrector with fewer than 20M parameters learns residual adjustments at selected sampling steps. Because earlier corrections change the states encountered at later steps, our On-Trajectory Flow-Bridge Supervision derives residual targets at the states actually reached during corrected generation. A single corrector is shared across selected steps and runs in parallel with the generator. Only the corrector is trained, requiring neither reward optimization nor re-distillation. To our knowledge, this is the first framework for lightweight velocity-residual adaptation of fully frozen few-step text-to-image generators that preserves their original sampling schedule and forward-pass count. On our target complex-scene distribution, the framework achieves a +17.60-percentage-point NetWin over frozen Z-Image-Turbo in pairwise instruction-following evaluation, with only 26.9 ms (0.84%) additional end-to-end latency per image and no increase in backbone evaluations.

---


### 69. [JMT-YOLO: Multi-task Domain Adaptation via Segmentation-Guided Consistency Learning](https://arxiv.org/abs/2610.12901)

**<font color=#1a73e8>作者：</font>** Zhenhua Yu, Jiahao Zhang, Wenchao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain adaptive object detection (DAOD) aims to reduce performance degradation due to distribution shifts between training (source) and testing (target) datasets. However, owing to insufficient modeling of fine-grained features and limited instance-level alignment, existing approaches become less effective under complex environmental conditions, such as extreme weather conditions and object occlusion. We overcome these challenges by proposing JMT-YOLO, a novel joint multi-task learning framework for DAOD. JMT-YOLO is based on the Mean Teacher architecture. It introduces an auxiliary semantic segmentation task and a masking mechanism to enhance the modeling of foreground-background semantic boundaries in the target domain. Specifically, fine-grained feature degradation is reduced by introducing a multiscale context-aware segmentation head equipped with a dense connection structure to effectively capture local and global contextual features. A mask-consistency loss is formulated by applying random masking operations to target images, thereby guiding the network to learn structural context and improving instance-level feature alignment. Extensive experiments on three benchmark domain adaptation tasks (Pascal VOC to Clipart1k, Cityscapes to Foggy Cityscapes, and KITTI to Cityscapes) demonstrate that JMT-YOLO achieves detection performances of 46.9%, 57.3%, and 61.0%, respectively. These results demonstrate superior performance over existing state-of-the-art and baseline methods, thereby validating the effectiveness and generalization of JMT-YOLO.

---


### 70. [Sample-Preserving Search-to-Decision Reduction for Noisy Linear Equations over Large Moduli](https://arxiv.org/abs/2610.12913)

**<font color=#1a73e8>作者：</font>** Andrej Bogdanov, Kel Zin Tan, Prashant Nalini Vasudevan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Noisy Linear Equations problem involves finding the solution to a random linear system over a finite field given noisy evaluations. This is a generalisation of various learning problems widely used in cryptography, including Learning with Errors (LWE), Learning with Rounding (LWR), and Learning Parity with Noise (LPN).
We present a new sample-preserving search-to-decision reduction for Noisy Linear Equations that has complexity $\mathrm{poly}(n,m,\log q, q/\sigma)$, where $n$ is the dimension of the secret, $m$ is the number of samples, $q$ is the modulus, and $\sigma$ is the magnitude of the noise (defined suitably for the kind of noise involved). In particular, this implies search-to-decision reductions for LWE and LWR that run in time $\mathrm{poly}(n)$ even if the modulus $q$ is exponentially large, as long as the noise-to-modulus ratio $\sigma/q$ is non-negligible. Our reduction works for prime moduli $q$. If $q$ is composite, it instead produces a list that contains a small multiple of the solution.
Prior to this work, known search-to-decision reductions for LWE and LWR either did not preserve the parameters of the problem (i.e., $m$, $n$, $\sigma$, and $q$), or had complexity that scaled polynomially with either $\sigma$ or the largest prime factor of $q$.

---


### 71. [Controlled-Minimax: Stabilizing Adversarial Optimization via Control Theory](https://arxiv.org/abs/2610.12915)

**<font color=#1a73e8>作者：</font>** Tianjiao Luo, Jianfei Chen, Jun Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Minimax optimization is fundamental to adversarial learning yet suffers from severe stability challenges, often manifesting as persistent limit cycles or divergence. This paper investigates these instabilities through the lens of continuous-time dynamical systems. By modeling training dynamics as a second-order Ordinary Differential Equation (ODE), we rigorously identify the root cause of non-convergence: the problematic eigenstructure of the loss function's Hessian near equilibrium points. To address this, we introduce Controlled-Minimax, a novel stabilization framework that reformulates the optimization trajectory as a controllable physical system. Unlike heuristic regularization techniques, our approach derives a specific feedback controller that provides theoretical guarantees of local exponential stability, regardless of the underlying Hessian spectrum. Consequently, our method stabilizes general minimax problems where traditional gradient descent-ascent methods fail. Extensive experiments on pathological benchmarks including the Dirac-GAN, 2D Gaussian mixtures, and Swiss Roll datasets, as well as high-resolution image synthesis with StyleGAN2-ada, demonstrate that Controlled-Minimax effectively suppresses oscillatory behavior while ensuring fast and robust convergence.

---


### 72. [DeFiRank: Federated Pairwise Ranking for Governance in Decentralized Financial Networks](https://arxiv.org/abs/2610.12916)

**<font color=#1a73e8>作者：</font>** Zahra Batool, Michael Duchesne, Kaiwen Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing governance approaches in decentralized financial networks rely on manual review processes conducted by human committees, which introduces subjective bias, creates a scalability bottleneck under high network volume, and fails to capture complex behavioural patterns and evolving network dynamics. To address these limitations, we propose \name, a federated learning-based pairwise ranking framework in which multiple institutions collaboratively train a ranking model without sharing their private transaction data. This collaborative learning enables the model to capture network-wide behavioural patterns that signify strong network participation and directly contribute to the network effect, including diversity of counterparties, usage of multiple applications, and frequency of transactions. The proposed system ranks providers based on the authenticity of their actions, promoting genuine contributors and demoting those exhibiting suspicious behaviour. We evaluate \name\ on a real-world blockchain transaction dataset. Results demonstrate that the federated approach achieves ranking performance modestly below the centralized baseline (NDCG@15: $\approx$0.87 vs.\ $\approx$0.92) while preserving data privacy and matching its ranking stability (Kendall $\tau$: $\approx$0.70 for both regimes), producing reliable governance decisions, including provider promotion and demotion (648 and 39 unique providers, respectively), without requiring centralized access to sensitive transaction data.

---


### 73. [AI-Mediation in Retail Markets: Revenue Effects and Assortment Optimization](https://arxiv.org/abs/2610.12917)

**<font color=#1a73e8>作者：</font>** Omar El Housni, Marouane Ibn Brahim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI shopping assistants increasingly influence which products consumers consider. We study retail assortment planning under AI mediation, where a retailer chooses a catalog, an AI intermediary forms a customer-facing shortlist, and the customer chooses from that shortlist according to a multinomial logit model. We consider both deterministic mediation, in which the AI follows a fixed segment-specific ranking, and stochastic mediation based on the Plackett-Luce model.
Empirically, we construct a dataset of product rankings from leading AI models, estimate Plackett-Luce ranking models, and evaluate their predictive performance on held-out assortments. Combining these estimates with synthetic customer preferences, we find that accounting for AI mediation can materially change optimal assortments and revenue. Across the tested capacity configurations, ignoring mediation yields mean revenue losses between 2.52% and 11.37% relative to the PL optimum. A much simpler deterministic plug-in, based only on the ordering of fitted AI utilities, performs substantially better, with mean losses of at most 0.53%.
Motivated by this performance, we study assortment optimization under deterministic mediation. We characterize its computational complexity and show that, for any fixed number of customer segments, the problem admits a fully polynomial-time approximation scheme.

---


### 74. [Teaching neural decoders with language](https://arxiv.org/abs/2610.12921)

**<font color=#1a73e8>作者：</font>** Xuan Wen, Yonghao Song, Yuhong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Brain-computer interfaces decode neural activity, yet class-label supervision (CLS) leaves relationships among classes implicit. We propose Language as Supervision (LaS), which aligns neural features with natural-language class descriptions through learned projections and predicts classes using candidate text prototypes. We evaluate seven encoder architectures with independently trained models for visual, motor, and speech decoding from scalp and intracranial recordings. LaS improves speech-decoding accuracy by up to 17.15~pp over matched CLS baselines. Its representations support candidate-set reuse and label-supervised subject and session adaptation, while LaS enables conditional unseen-frequency decoding in steady-state visual evoked potential (SSVEP) responses. Correct class-description correspondence supports this generalization, and dual-sided attribution visualization shows neural and textual contributions to the same class-matching score. These findings suggest that text descriptions can serve as general-purpose references for learning and interpretation in neural decoding.

---


### 75. [What Egocentric Video Embeddings Encode and How to Combine Them with Inertial Sensors for Human Activity Recognition](https://arxiv.org/abs/2610.12926)

**<font color=#1a73e8>作者：</font>** Kansuke Habano  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video and body-worn inertial sensors are increasingly recorded together, and the video is usually encoded by pretrained models. What these embeddings represent when the camera sits on the head, and how they should be combined with inertial sensing, has received little attention. Across VideoMAEv2, CLIP, DINOv2 and the egocentric VC-1, the leading principal directions of the embedding are dominated by where the camera looks. Measured head orientation explains them on Ego-Exo4D for egocentric (R^2 0.49-0.70) but not exocentric cameras, and the scene layout explains them on WEAR. The part that the limbs' inertial signals predict separates activities across people. In a set-level probe, the rest separates exercise sets within a participant but not activities across people. This is consistent with separate roles: the video finds the clips of the same set, and the inertial classifier labels them. On WEAR, with temporal order removed and one random limb per one-second clip, we propagate inertial predictions over a within-participant video graph whose leading components are removed. This raises subject-wise cross-validated macro-F1 from 0.648 to 0.852. In our comparisons, propagation helps only over the video graph, and fusing the modalities in one classifier, or adding inertial edges to the graph, performs worse.

---


### 76. [UniDeblur: Unified Motion Deblurring via Fourier Convolution Learning](https://arxiv.org/abs/2610.12941)

**<font color=#1a73e8>作者：</font>** Xintian Mao, Jiansheng Wang, Huaiyuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image deblurring is a fundamental task in computer vision, yet existing methods mainly specialize in isolated scenarios. Consequently, the deblurring performance of these models drops significantly across scenarios with different cameras and image contents. This motivates the development of a unified motion deblurring framework that can handle diverse blur patterns. To this end, we construct a multi-source dataset and develop a data pruning and quality control pipeline. Then, to restore blur images with various motion blur kernels across different scenarios, we propose a unified motion deblurring framework via Fourier Convolution Learning. Existing deblurring networks usually rely on pixel-level mappings and overlook the convolutional nature of blur. Thus, the network mostly fits the image content itself rather than learning the convolution process, making it difficult to handle multi-source blur images. Instead of relying on spatial mapping, we perform blur-adaptive global filter learning in Fourier space, which avoids the limited spatial support of kernel estimation. Extensive experiments demonstrate that our unified model effectively handles motion blurs across diverse sources and scenes, achieving competitive performance across both in-domain and OOD benchmarks. Code will be released at this http URL.

---


### 77. [AgentValve: Sybil-Resilient Payment Authorization for Permissionless AI Markets](https://arxiv.org/abs/2610.12948)

**<font color=#1a73e8>作者：</font>** Jianting Zhang, Zhongtang Luo, Aniket Kate  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly select and pay service providers without human review. In emerging permissionless markets, however, adversaries can create inexpensive identities and fabricate feedback to inflate provider reputation, making reputation-based payment authorization vulnerable to Sybil attacks and exposing clients to unbounded financial loss.
This paper presents AgentValve, a protocol for Sybil-resilient payment authorization in permissionless AI markets. AgentValve builds on a trust network that represents reputation as finite capacity in a directed graph and authorizes payments through trust paths with sufficient available capacity. A smart contract atomically reserves the capacity supporting each admitted payment, bounding honest agents' payment exposure by the capacity they extend into the adversarial region, and thus creating identities or interactions entirely within that region cannot increase this bound. To limit capacity depletion by malicious senders, AgentValve combines payment-backed capacity creation with bounded route length, preventing attackers from depleting honest capacity without incurring corresponding payment costs. AgentValve further decouples off-chain route discovery from on-chain verification and introduces a witness-commit mechanism that reduces route verification to linear work while requiring only constant persistent state per admitted payment.
We implement a AgentValve prototype and evaluate it using six months of Ethereum data and synthetic workloads. Experimental results show that under attacks with up to 10,000 synthetic Sybil identities and with chosen attackers, the payment exposure and capacity depletion remain bounded. Regarding practicality, the witness-commit mechanism lowers admission cost by up to 40.8% compared with baselines, and admitting common payments costs approximately \$0.04-\$0.21.

---


### 78. [WaveMark: Robust Wavelet-Domain Image Watermarking for Diffusion Models](https://arxiv.org/abs/2610.12952)

**<font color=#1a73e8>作者：</font>** Jie Cao, Qi Li, Chaklam Cheong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Image watermarking enables provenance tracing for photorealistic images generated by diffusion models. However, state-of-the-art (SOTA) removal attacks can suppress embedded signals with little perceptual degradation. This vulnerability limits the effectiveness of watermarks for intellectual property protection and misuse attribution. We propose WaveMark, a novel wavelet-domain watermarking method that embeds messages in a diffusion model's initial noise. To support robust recovery from perturbed carriers, WaveMark distributes keyed replicas of message bits across spatial positions, wavelet orientations, and scales. Each carrier groups coefficients from four latent channels and encodes a randomized bit through magnitude projection, providing an explicit decoding margin. We evaluate WaveMark with SD2.1 on SDP and MS-COCO Captions under 14 attacks. WaveMark achieves 100.0% bit accuracy (BA) without attacks, while maintaining image quality comparable to the evaluated baselines. Under SOTA MarkNull and MarkNull-A, it retains over 88% BA, outperforming all baselines.

---


### 79. [DataCupid: Stable Matching Repair for Training Data Acquisition with Delayed Feedback](https://arxiv.org/abs/2610.12960)

**<font color=#1a73e8>作者：</font>** He Sun, Junyuan Mao, Wenhao Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matching repair after utility changes can reuse valid observations, but new evaluations must respect matching capacity and may return out of order. We study announced invalidations with bounded, possibly reward-dependent reporting delays and pending evaluations that do not occupy future matching capacity. Residualload repair (RLR) combines sound outcome certificates with batched matching schedules for unequal sample deficits. Its complete dyadic quota schedule admits a sharp issue-round bound with coefficient cb < 1.607 relative to the terminal residual endpoint load, together with separate delay and evidence-lifetime bounds. RLR-P monitors complete issue-order prefixes without changing the sampling plan before acceptance. With a deterministic pure oracle, a single-repair coupling from the same drained initial state guarantees no increase in certification time, issued observations, or time to a reusable checkpoint. We also derive an information-load lower bound. On fixed priority-star markets with unknown Bernoulli gaps, PrioritySearch attains the history-adjusted first-order constant for expected certification time as {\delta} {\sim} 0, under hypothesis-independent linear history scaling and sublogarithmic reporting delays. Paired simulations and measured-feedback replay quantify the trade-offs: in the replay, RLR-P has lower mean capped update-certification time than a monitored width-based baseline, at higher oracle CPU cost.

---


### 80. [Diffusion Precipitation Generation with Medium-range Weather Forecasting](https://arxiv.org/abs/2610.12976)

**<font color=#1a73e8>作者：</font>** Guowen Li, Yang Liu, Mengxuan Chen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate daily precipitation forecasts are important for weather-sensitive decisions. Although recent Weather Foundation Models (WFMs) have achieved significant progress, they are trained on reanalysis data, which exhibit regional and intensity-dependent biases. Since retraining WFMs on observation-based targets is costly, we study Dynamics-Precipitation Decoupling, a plug-and-play framework that uses a separately trained generator to map non-precipitation forecasts from a frozen weather model to observation-aligned daily precipitation. Its key challenges are to capture heterogeneous rainfall distributions and align daily accumulations with atmospheric signals that evolve across space and time. To address them, we train a diffusion generator conditional on atmospheric states and satellite-gauge estimates of precipitation. A multi-scale recurrent encoder summarizes atmospheric evolution, while cross-attention aligns atmospheric and precipitation features during denoising. Extensive evaluation of various backbones, including Pangu-Weather, GraphCast, and HRES, on global and regional forecasting shows improved daily precipitation accuracy and event detection, with better representation of localized accumulation patterns. Global ensemble evaluation shows lower Brier scores than ENS and training-from-scratch GenCast at all reported lead times, with lower CRPS in most comparisons. Remarkably, a heavy-rainfall case study using 2,288 stations in China further supports improved daily accumulation patterns and event detection against ground observations.

---


### 81. [Beyond Semantic IDs: Finite-Beam Reachability and Continuous-Query Generation in Generative Recommendation](https://arxiv.org/abs/2610.12977)

**<font color=#1a73e8>作者：</font>** Yu Sun, Renkai Xiang, Zuodong Xiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative recommendation (GR) of social media platforms commonly retrieves items by autoregressively decoding discrete Semantic IDs (SIDs) with finite-width beam search. This work examines how this output interface constrains whether held-out targets enter finite returned lists, while distinguishing catalog-wide scoreability from empirical top-K support. We introduce two continuous-query paradigms: CQG-Single generates one retrieval query in a single pass, and CQG-AR autoregressively generates continuous residual updates, retaining step-wise decoding while removing the SID item-token vocabulary, code lookup, and discrete beam expansion. These designs thereby eliminate the SID-specific reachability constraint induced by finite-beam decoding and avoid the technical challenge of aligning a discrete SID vocabulary with the pretrained backbone's vector space. Both methods make every encoded item directly scoreable through dense or approximate-nearest-neighbor retrieval. Under a unified protocol with valid-prefix constrained decoding, CQG-Single exceeds the TIGER-style baseline in all seven runs while using 55.3% as many trainable parameters. CQG-AR remains comparable on ML-1M and is numerically stronger on Beauty and Sports datasets. A controlled depth ablation further shows that additional continuous refinement does not monotonically improve shallow accuracy. These findings motivate decoupling output representation, autoregressive modeling, and retrieval budget when evaluating generative recommendation systems.

---


### 82. [Learning Representations to Guide Pixel Diffusion Transformers](https://arxiv.org/abs/2610.12978)

**<font color=#1a73e8>作者：</font>** Zihao Pan, Mengting Chen, Cheng Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual representations are largely developed for understanding, yet what makes them useful for generation remains unclear. We study this question in pixel diffusion transformers and uncover two key insights. First, better representation quality does not necessarily translate into greater generative utility, as externally aligned semantics can be progressively lost during pixel synthesis. Second, architectural separation with specialized pixel decoders mainly redistributes semantic and spatial modeling, without necessarily yielding representations better suited to generation. These insights suggest that a useful generative representation must be both properly formed and actively exploited. Motivated by these insights, we introduce Representation Guidance (RG), which directly forms and exploits internal representations while retaining a plain Transformer architecture. A low-dimensional bottleneck forces generation-relevant information into a compact representation, which is then explicitly used to guide decoder generation by modifying the flow-matching target according to its induced prediction offset. RG learns clearer semantic and spatial structure while scaling efficiently in both parameters and computation. On ImageNet 256x256, RG-L/16 with only 459M parameters outperforms substantially larger pixel diffusion transformers, while RG-XL/16 achieves an FID of 1.55. RG further reaches an FID of 1.74 at 512x512 and extends to text-to-image generation, achieving 0.89 on GenEval and 87.1 on DPG-Bench.

---


### 83. [Gaussian-Width Bounds for Offline-to-Online Linear Bandits](https://arxiv.org/abs/2610.12990)

**<font color=#1a73e8>作者：</font>** Kushagra Chandak, Volodymyr Tkachuk, Xiaoqi Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how offline data can help online learning in stochastic linear bandits. We focus on partially covered offline data, where only $k$ of the $d$ feature directions are poorly covered. Existing analyses of algorithms based on phased elimination and optimism give regret bounds of order $\widetilde O(\sqrt{dkT})$ in this regime. We show that this dependence arises from loose control of the reward prediction error, and obtain tighter bounds using concentration of Lipschitz functions of Gaussian vectors. Based on this analysis, we develop a phased elimination algorithm with regret $\widetilde O(k\sqrt T)$. For the unit Euclidean ball, we prove a matching regret lower bound under partial coverage, as well as matching upper and lower bounds under uniform offline coverage. We also study pure exploration with offline data, providing algorithms and matching upper and lower bounds on simple regret for fixed-design algorithms and also for adaptive algorithms under partial and uniform coverage of offline data.

---


### 84. [Benchmarking Embedding Geometries and Clustering Algorithms for Unsupervised Patent Claim Classification](https://arxiv.org/abs/2610.12997)

**<font color=#1a73e8>作者：</font>** Sujith Subramanian, P N Bhargav Teja, Susen Sarkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prior-art retrieval systems are structurally organized around classification codes, making cross-code discovery difficult. This paper asks if an unsupervised representation trained on patent text can recover relevant connections that code-restricted search cannot, and if hyperbolic space helps. We trained a hyperbolic and a matched Euclidean Variational Autoencoder (VAE) on 45,000 US patents (96 runs, 6 seeds). The hyperbolic model retrieves genuinely cross-category prior art 52% more often than the Euclidean model (18.76% vs. 12.34% of top-10 results, 3,000 queries). This represents a practical gain for the motivating search problem. The hyperbolic model agrees less with official classification (NMI 0.2392 vs. 0.3206), which we explain geometrically: the two measures capture different goals, and only one aligns with prior-art search needs. In a study of 10 technology domains (50,000 more patents), we find that a domain's classification breadth--the number of distinct CPC subgroups spanned--predicts approach performance (Pearson r=-0.642, p=0.045, N=10), and that patents per subgroup is an even stronger predictor (r=0.715, p=0.020). This provides a checkable signal for practitioners to determine where the method is most valuable. We report all findings with statistical transparency and release a complete, 91-test automated implementation.

---


### 85. [Scaling Empowered Agents](https://arxiv.org/abs/2610.13002)

**<font color=#1a73e8>作者：</font>** Catherine Ji, Vivek Myers, Joshua Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Empowerment measures the capacity of an agent to actively control its environment. In this work, we explain the connection between skill learning and empowerment. While skill learning is not empowerment, we introduce a simple scalable recipe for empowerment maximization: empowerment corresponds to the number of executable skills from a state, so maximizing empowerment corresponds to reaching states that are good starting points for many skills. Our recipe applies to arbitrary underlying skill learning methods. Whereas most prior work on empowerment looks at tabular settings, this recipe enables us to study empowerment at a scale where we can realize theoretically-predicted but empirically-elusive properties of empowerment (e.g., gathering resources, environment modification, survival). Experiments show that empowerment maximization unlocks interesting emergent properties, such as building a house in Crafter. Website and code at \href{this https URL}{this https url}.

---


### 86. [Learning Features, Not Layouts: Feature-Axis Attention as a Transfer Prior for Medical Imaging](https://arxiv.org/abs/2610.13012)

**<font color=#1a73e8>作者：</font>** Aon Safdar, Mohamed Saadeldin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural-image-pretrained foundation models are increasingly adapted to medical imaging, yet transfer remains unreliable under domain shift, modality heterogeneity, and label scarcity. We trace part of this fragility to an overlooked design choice. Standard vision transformers place all global modeling on self-attention over spatial tokens, an object-layout prior well suited to natural scenes but not to medical images, where the discriminative signal lies in feature correlations and texture that recur across scanners while layout does not. We ask whether the axis of global attention, spatial versus feature, is itself a lever for transferable medical representations. Existing channel-aware hybrids confound this question, adding channel attention to a spatially-mixed backbone and leaving the axes coupled and the feature axis unmeasurable in isolation. We design FAD-ViT, a backbone that strictly decouples the two axes, making feature-axis attention the primary global operator and the attention axis a controlled variable. Evaluating comprehensively across 23 classification, segmentation, and low-data tasks under matched tokenization, capacity, and protocol, we find that shifting global attention from the spatial to the feature axis leaves from-scratch performance essentially unchanged, yet markedly strengthens transfer. Identical ImageNet pretraining yields up to roughly three times the transfer gain, with consistent improvements on every held-out segmentation task at up to a quarter the parameter count and far lower compute than standard and channel-attention baselines. The advantage is largest where texture rather than geometry is discriminative, tracking greater reuse of pretrained features. The axis of global attention is thus a design lever for medical transfer, and making it channel-primary is a simple, cheap, and principled choice.

---


### 87. [Evidential Multimodal Transformers with Dempster-Shafer Fusion for Emotion Recognition](https://arxiv.org/abs/2610.13013)

**<font color=#1a73e8>作者：</font>** Muhammad Usama, Yeoreum Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Softmax-based multimodal emotion recognition methods often assign high confidence even when sensor data are corrupted or contradictory, for example when facial expressions suggest positive valence while vocal prosody indicates negative arousal. We present an Evidential Multimodal Transformer with Dempster-Shafer Fusion (EMT-DS) that addresses this problem through formal uncertainty quantification. EMT-DS models predictions as Subjective Opinions (Dirichlet distributions), separating epistemic uncertainty (lack of evidence) from aleatoric uncertainty (sensor noise). Modality-specific transformer encoders produce belief mass distributions that are fused with Dempster's Rule of Combination, which normalizes the joint belief mass by a conflict coefficient 1/(1-c), so that contradictory evidence is explicitly quantified as conflict and the fused prediction becomes diffuse rather than being forced into an unjustified consensus. Under subject-independent and speaker-independent evaluation on four benchmarks, EMT-DS achieves 84.3% accuracy on IEMOCAP versus 81.7% for the best baseline (p < 0.01), 82.4% on DEAP under leave-one-subject-out evaluation versus 78.1%, and 96.8% on the highly imbalanced KEMDy20, and it improves accuracy on CMU-MOSEI by 2.4 points over the strongest evidential baseline. In controlled ablation, it reduces Expected Calibration Error from 0.153 (softmax transformer) to 0.042. It maintains 71.2% accuracy under severe Gaussian noise on audio features (sigma = 1.0), where attention baselines drop to 45.3%, and degrades gracefully when entire modalities are absent. The fusion step has O(MK^2) complexity, compared with O(M^2 d^2) for cross-modal attention. The learned conflict metric also flags likely errors: reviewing 20% of samples captures 80% of misclassifications, which supports selective prediction in clinical and safety-critical systems.

---


### 88. [Unified Generative Video Compression with Autoregressive and Bidirectional Video Diffusion](https://arxiv.org/abs/2610.13023)

**<font color=#1a73e8>作者：</font>** Tianyu Zhang, Shuai Huo, Dengchao Jin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models can reconstruct visually compelling content from severely compressed representations at ultra-low bitrates, but they impose a rigid deployment trade-off. Bidirectional (BI) models achieve high quality through dense full-sequence attention, yet require the entire sequence before reconstruction and incur substantial latency. Autoregressive (AR) models enable low-delay streaming, but their restricted temporal context reduces compression efficiency. This tension is particularly relevant when a video stream must be decoded in real time yet is also stored for later, quality-oriented playback, making AR and BI models natural choices for the live and replay stages, respectively. To support both stages, we present UniGVC, a Unified Generative Video Codec that supports two decoding modes from a single bitstream. UniGVC-BI employs a BI-DiT with dense attention for quality-oriented random-access decoding, whereas UniGVC-AR uses windowed AR-DiT for low-delay streaming. Both paths share a hierarchical latent codec that recurrently produces the same conditions with ultra-low bitrates, allowing UniGVC-BI to serve as a conditional teacher for single-step distillation of UniGVC-AR. A tiny conditional video decoder further reduces streaming latency while preserving most of the reconstruction quality. On standard 1080p benchmarks, UniGVC-BI achieves the best overall rate-distortion-perception trade-off among the evaluated methods and produces temporally stable video at rates as low as 0.0005 bits per pixel. Meanwhile, UniGVC-AR remains competitive while decoding 1080p video at 36.85 FPS, over $250\times$ faster than UniGVC-BI. Code and models will be released later.

---


### 89. [What Visual Representations Do World Action Models Need?](https://arxiv.org/abs/2610.13024)

**<font color=#1a73e8>作者：</font>** Kai Liu, Jiangran Lyu, Tingyu Deng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) inherit powerful priors from pretrained video generation models, but their variational autoencoder (VAE) representations are optimized for visual reconstruction rather than manipulation. External visual representations can improve manipulation, but existing methods couple representation choices with different integration mechanisms, obscuring their individual effects. We systematically compare visual representations, five integration mechanisms, and feature combinations under controlled settings. Our study yields three main findings. First, strong general-purpose visual representations provide broader robustness gains and can match or outperform representations pretrained for specific visual capabilities. Second, channel-wise joint prediction achieves the highest average success rate; further analyses suggest that future-feature prediction and the action expert's effective use of added visual information contribute to its gains. Third, additional sources should be selected for the task-relevant information they contribute beyond existing representations, as the same source can help one combination but harm another. However, even the best evaluated composition provides a smaller additional gain than the initial improvement from adding a strong general-purpose representation to the VAE-only baseline. We instantiate the resulting Representation Recipe as R$^2$-WAM. It achieves state-of-the-art performance on RoboCasa GR1 Tabletop with an 84.7% success rate and reaches 92.8% on RoboTwin 2.0, improving over the VAE-only baselines by 5.9 and 2.2 percentage points, respectively. Taken together, these findings suggest that future work should prioritize stronger general-purpose visual representations and more effective mechanisms for integrating them into WAMs, with feature composition serving as a supplementary route to improvement.

---


### 90. [Post-Quantum Session Establishment for Matter over Thread: Message Size, Transport, and Protocol Options](https://arxiv.org/abs/2610.13026)

**<font color=#1a73e8>作者：</font>** Daniel Commey  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Matter's first post-quantum change protects device attestation with ML-DSA, but its operational handshake, CASE, still derives session keys from P-256 ECDH, so recorded traffic can be decrypted once a quantum computer exists. We quantify the cost of moving CASE to ML-KEM and post-quantum signatures over Thread, where frames carry at most 127 bytes and a Matter message at most 1178 bytes. A byte-exact model of the CASE messages shows that a drop-in ML-KEM-768/ML-DSA-44 handshake grows from 1.6 kB to 22.8 kB and that no fully post-quantum configuration built from FIPS 203/204/205 algorithms fits the message limit. A Monte Carlo model of multi-hop Thread, calibrated to OpenThread and Matter source constants, shows that sending these messages as fragmented IPv6 datagrams causes spurious retransmissions whenever a message and its reply outlast Matter's retransmission timer. At three to four hops the drop-in handshake then takes 1.8 to 2.6 times longer than with a selective-repeat block transfer, with or without interference, and up to 33% of handshakes with sleepy devices fail; raising the timers does not remove the effect. Caching certificate chains and authenticating the device with a pre-distributed ML-KEM key reduce the handshake to 6.1 kB and 44 ms of device computation. As a first step, hybrid P-256+ML-KEM-512 key exchange with a cached device chain protects session keys against harvest-now, decrypt-later attacks while every message still fits the current limit.

---


### 91. [Low-Rank Kolmogorov-Arnold Generator Flows for Interpretable Operator Learning](https://arxiv.org/abs/2610.13028)

**<font color=#1a73e8>作者：</font>** Minjong Cheon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators that learn physical laws from data should generalize beyond their training distribution and expose the learned law in closed form. The Kolmogorov-Arnold neural operator achieves both for position-dependent dynamics by learning a dense pseudo-differential symbol over all positions and frequencies, at a cost that grows with the square of the resolution and with closed forms that must be read out by hand. This dense symbol is unnecessary: a finite-order variable-coefficient differential operator has a symbol whose separation rank is bounded by the number of its coefficient functions, independently of the resolution, and the symbols that this network learns on its own benchmarks have rank two. We introduce the Kolmogorov-Arnold flow (KAFlow), which learns the generator of a physical operator as a low-rank symbol built from univariate Kolmogorov-Arnold functions, fixes the gauge of these functions so that every term has a unique place, integrates the dynamics with exact exponential integrators, and distills its closed form automatically. On the synthetic benchmarks of the Kolmogorov-Arnold neural operator, KAFlow lowers the out-of-distribution loss by 3.4 to 11 times and recovers every coefficient to within 10^-4 without symbolic templates, reaching the precision floor of the data. On long-horizon quantum dynamics, it lowers the state infidelity by up to 6 orders of magnitude, and by 30 times when trained only on position and momentum measurements. KAFlow also learns a variable-order fractional operator 15 times more accurately than existing operator networks and discovers nonlocal, fractional and non-polynomial dispersion relations on which sparse regression fails.

---


### 92. [Target-Constrained Pooling for Trajectory Extrapolation](https://arxiv.org/abs/2610.13034)

**<font color=#1a73e8>作者：</font>** Ning Wang, Claire Cardie, Sainyam Galhotra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory extrapolation from a partial target trajectory is underdetermined, but completed related trajectories provide information about the unresolved continuation. We propose target-constrained pooling (TCP), which separates the finite-horizon endpoint from continuation shape and estimates that endpoint from two complementary source signals. Uniform pooling captures final response levels, while matched-increment pooling captures the remaining change after aligning source and target states. TCP selects representative sources, projects both endpoint estimates onto a target-consistent region, converts them into corrections of the free forecast, and controls their influence through strength calibration and degradation-aware weighting. Across 25,245 targets from five domains and both forecasting directions, TCP reduces mean RMSE by 35.8% to 42.1% for all ten target-only forecasters and improves all 100 forecaster, dataset, and direction comparisons. The two endpoint signals consistently outperform either alone, while representative selection remains within 0.64% to 1.02% of the full donor pool using 12.7x fewer donor inputs and 138.8x fewer matching distance computations.

---


### 93. [Towards Easier-to-Tune Training Algorithms: New Results from AlgoPerf](https://arxiv.org/abs/2610.13036)

**<font color=#1a73e8>作者：</font>** Priya Kasimbeg, Ahmed Khaled, Aahlad Chandrabhatta 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating deep learning optimizer is challenging because confounding factors such as hyperparameter tuning and optimizer-model co-design often obscure true algorithmic performance. We present results of the updated AlgoPerf V1 benchmark, in which we evaluate a new set of training algorithms on wall-clock time-to-target across nine workloads on fixed hardware. This report focuses on the results of the benchmark's self-tuning ruleset, which requires submissions to use a single configuration across all workloads. Out of the 13 submissions in PyTorch and JAX, Schedule-Free AdamW ranked first. In addition to the wall-clock scores, we also analyze the trade-offs between step efficiency and wall-clock execution, revealing that matrix-preconditioned and two-loop methods achieve good sample efficiency but require more aggressive computational optimizations to be competitive in runtime. Finally, our hyperparameter saliency and retention analyses show that the learning rate and momentum are highly sensitive across domains and algorithms, highlighting the need for methods that are more robust against hyperparameter tuning and can generalize well to new tasks.

---


### 94. [Provably Subexponential Algorithms for Bounded-Error LWE with Few Samples](https://arxiv.org/abs/2610.13043)

**<font color=#1a73e8>作者：</font>** Haoxing Lin, Prashant Nalini Vasudevan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We show that a variant of the Wagner/BKW-style algorithm for LWE of Kirchner and Fouque [KF15] solves decision and search LWE with secrets of size $n$ over prime moduli $q=n^{\kappa+o(1)}$, for any fixed $\kappa>0$, with errors bounded by $\exp((\ln n)^{o(1)})$, in time $2^{O(n/\ln\ln n)}$ given $n+O(n/\ln\ln n)$ original samples. Further, if each coordinate of the secret is also bounded by $\exp((\ln n)^{o(1)})$, the same time bound holds with errors bounded by $n^{o(1)}$ and only $O(n/\ln\ln q)$ samples.
Earlier, it was known that Kirchner and Fouque's algorithm could solve LWE with these parameters in subexponential time with a much larger number of samples $m = \Omega(n\log{n})$ [HKM18]. Ducas et al. [DEL25] showed that an adaptation of this algorithm could solve the corresponding dual, the $\mathrm{SIS}^{\infty}$ problem, with a suitable norm bound $q/\operatorname{polylog}(n)$ and $m=n+\omega(n/\ln\ln n)$ variables in subexponential time. Whereas their analysis involves interpreting the algorithm in terms of chains of lattices, our approach is quite elementary and is based on bounding the lower moments of a Fourier statistic.

---


### 95. [NOFACE3D: NOise-scheduled Focused Anchoring and Controlled Enhancement for 3D Generation](https://arxiv.org/abs/2610.13050)

**<font color=#1a73e8>作者：</font>** James Rose, Jingwen Liang, Wenchao Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image-to-3D models generate complete, high-quality assets from a single image, with global shape and appearance that are already convincing; what remains is the fine scale, where small, thin, elongated, or detail-rich regions are reconstructed softly and under-resolved. This gap can arise in generators with fixed-resolution spatial grids: the same spatial sampling density is used for a large, smooth, low-curvature surface and for a thin, high-curvature structure that carries most of the perceived detail. To this end, we introduce NOFACE3D, a training-free framework that refines these detail-critical regions while preserving the rest of the asset. Given a generated mesh, its input image, and a refinement box, NOFACE3D extracts the selected submesh, scales it up to fill the generator's input volume, and re-encodes it into the full-resolution latent grid. Conditioned on the image crop, it refines the region through flow-based sampling with a spatially varying noise schedule that anchors boundary latents. The refined region is then integrated back into the original asset, preserving the surrounding geometry and appearance. We implement NOFACE3D on TRELLIS.2 and its sparse voxel representation; all of it operates purely at inference time on the frozen pretrained generator. We evaluate NOFACE3D on PAniC-3D, TexVerse and BigDetail, a new benchmark of 339 assets with annotated detail-critical regions. On all three, it generates sharper geometry and finer texture detail than the baselines. Project page: this https URL

---


### 96. [Space Over Statistic, Retraining Over Ranking: Auditing Training Labels Under Label-Only Backdoors](https://arxiv.org/abs/2610.13051)

**<font color=#1a73e8>作者：</font>** Arnab Dey, Mohammad Mahfuzul Islam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Some backdoor attacks never touch an image. FLIP only changes labels: on CIFAR-10, flipping 3% of them makes a ResNet-32 send 99.7% of triggered source-class images to the attacker's class. The usual defenses look for the poison inside a model trained on those same labels. So when they struggle, is the problem the test they run, or the space they run it in?
We answer with a controlled swap: we keep the test, the labels and the metric fixed, change only the feature space, and judge each defense by retraining the victim on what it keeps. The space decides. On dog$\to$cat the same nearest-neighbor check scores AUROC 0.546 on the poisoned model's features, 0.967 on frozen DINOv2 features that never saw a label, and 0.995 on the same network trained on clean labels, an oracle control rather than a defense. We reproduce SPECTRE, the defense FLIP's authors recommend, to 90.94 / 0.97 against its published 91.47 / 1.7, then price it: on truck$\to$deer it deletes 20% of every class, while a prototype audit on the frozen features deletes 6% for higher clean accuracy and lower attack success. On three harder pairs that audit leaves about a quarter of the attack standing. A count read off encoder geometry and clean labels, before any attack is run, separates the pair where the audit removes the attack from those where it only partly does, though on a single zero-count pair.
Three results warn against the easy story. A better detection score does not mean a safer model: on two of four pairs Confident Learning scores the higher AUROC, and on dog$\to$cat leaves 2.6 times the attack success. The prototype family, our best static performer, is the first an adaptive attacker slips past. And past a point, catching more poisons stops reducing attack success. Check labels in a space that never learned them, and judge a defense by the retrained model, not by its detection score.

---


### 97. [UniMergeTrack: Hierarchical Model Merging for General RGB-X Visual Object Tracking](https://arxiv.org/abs/2610.13053)

**<font color=#1a73e8>作者：</font>** Shiao Wang, Xiao Wang, Yuhe Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-X tracking leverages complementary modalities, such as thermal infrared, event, or depth, to improve robustness under challenging conditions. Existing general-purpose RGB-X trackers typically follow two paradigms: independent task-specific training and joint training across modality combinations. However, the former suffers from knowledge isolation and model redundancy, while the latter introduces optimization interference across heterogeneous tasks. In this work, we present UniMergeTrack, a new model merging paradigm that preserves task-specific optimization while enabling effective cross-task knowledge integration. UniMergeTrack first trains modality-specific trackers independently and then performs hierarchical model merging. Specifically, transferable backbones are merged across RGB-X tasks via high-pass-filtered merging, and complemented by lightweight task-specific experts that preserve modality-specific cues. Tracking heads are merged within each task using optimal transport-guided channel alignment to mitigate hidden channel mismatch. A subsequent distribution alignment fine-tuning stage further improves compatibility between the unified backbone and task-specific heads. Extensive experiments on the LasHeR, RGBT234, VisEvent, VOT-RGBD22, COESOT, and CDTB benchmarks demonstrate that UniMergeTrack achieves state-of-the-art or competitive performance across RGB-Thermal, RGB-Event, and RGB-Depth tracking tasks, while exhibiting strong generalization to unseen datasets. The source code will be released upon acceptance. The source code of this paper will be released on this https URL.

---


### 98. [A4-MR: Abnormality-aware Anatomical Alignment for MR](https://arxiv.org/abs/2610.13056)

**<font color=#1a73e8>作者：</font>** Noel D'souza, Zhijian Yang, Nishank Singla 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in large-scale foundation models have enabled strong generalization across a wide range of clinical and research tasks in magnetic resonance imaging (MRI). However, existing vision-language MRI models remain limited in anatomy-specific localization and pathology-aware representation, particularly in real-world settings. We introduce A4-MR, a 3D vision-language foundation model trained on approximately 50,000 MRI studies comprising 491,000 series, roughly half of which are paired with radiology reports. A4-MR is designed to: (1) learn anatomy localization through large-scale pretraining with noisy labels; (2) align image and text representations at the anatomical level; and (3) learn distinct representations of healthy and abnormal anatomy. Across a diverse set of downstream tasks, A4-MR outperforms existing foundation models, including a +1.7 AUROC improvement over MedSigLIP for abnormality detection. Using a frozen encoder, A4-MR also surpasses an end-to-end task-specific MedNeXt model for knee segmentation by +1.4 Dice and performs comparably to the best task-specific model for abdominal organ segmentation on AMOS, within 0.4 Dice. Finally, without anatomical prompts, A4-MR localizes 3D anatomy comparably to MedSAM2 provided with ground-truth bounding boxes. Together, these results demonstrate that anatomy-level multimodal alignment and abnormality-aware representation learning can enable a single MRI foundation model to support localization, segmentation, and pathology-related tasks.

---


### 99. [CoBe: A Benchmark For Conversational Counterfactual Text Editing](https://arxiv.org/abs/2610.13057)

**<font color=#1a73e8>作者：</font>** Arvind Raghavan, Inwoo Hwang, Shreyas Havaldar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Counterfactual text editing is the ability to revise a given text in light of a hypothetical change while preserving facts not causally affected by that change. When asked what would have happened if a doctor had not recommended surgery, the model output should retain the patient's medical history and modify only the consequences of the decision. This requires causal understanding: a model must determine, without being explicitly instructed to, what events are affected by the hypothetical change and what should remain fixed. This skill is central to human reasoning, especially in safety-critical domains like healthcare or law. By contrast, the task of associational text generation merely generates text statistically associated with the altered condition. In the medical example, an associational response might make the patient's symptoms less severe because milder cases correlate with no surgery. Such responses produce a plausible scenario, but not the counterfactual version of the given one. Prior counterfactual-text datasets do not clearly separate these modes of reasoning. We introduce the Counterfactual Benchmark (CoBe), a testbed for models' zero-shot ability to counterfactually edit a given textual scenario when prompted to do so in a conversationally natural way. CoBe contains 2000 questions spanning healthcare, science and engineering, business, and everyday scenarios. We test a suite of frontier and smaller models, with frontier systems achieving an average score of $58.05\%$. Our findings indicate that models frequently default to associational generation rather than preserving the causal structure of the original scenario. Moreover, performance does not scale consistently with either model size or output token length, suggesting that the failure may reflect model training objectives rather than insufficient model capacity.

---


### 100. [Evolving Creatives with Clicks: CTR-Driven Advertising image Editing via Attribute Disentanglement and Preference Alignment](https://arxiv.org/abs/2610.13066)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Haohan Wang, Zheng Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The optimization objective for e-commerce advertising creatives has shifted from aesthetic quality to online business metrics like click-through rate (CTR). Recent methods generate appealing ad images from product images by constructing CTR-based reward signals and refining prompt generation via Reinforcement Learning. Such paradigms equally penalize all attributes within an underperforming image, even though some are actually beneficial to clicks. In this work, we propose Evolving Creatives with Clicks (ECC), which reformulates creative optimization as fine-grained editing rather than generation from scratch. ECC selectively refines attributes that hurt CTR while preserving those that contribute positively. Specifically, faced with a rich attribute space across massive images, ECC first identifies 28 attributes significantly correlated with CTR via ANOVA and Random Forest regression. Based on attribute contrasts between images with disparate CTRs, we instruction-tune a prompt model to generate editing suggestions, then refine it with real click preferences since reference-derived suggestions are not uniformly beneficial. Furthermore, we introduce Consistent Preference Optimization (CPO) as ECC's preference optimization strategy, which enforces consistency across semantically equivalent shuffled suggestions to mitigate DPO overfitting and improve preference generalization. Extensive experiments demonstrate that ECC significantly improves the CTR of ad images, outperforming state-of-the-art models by a substantial margin. The complete data pipeline, including attribute extraction and analysis, the resulting dataset, and source code will be released upon acceptance.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-244](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
