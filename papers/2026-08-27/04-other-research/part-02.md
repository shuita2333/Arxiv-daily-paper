# 📦 其他研究 | 2026年08月27日

> 本类共 **194** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-194](./part-04.md)

---

### 51. [GlanceWAM: Sparse Test-Time Imagination for World-Action Models](https://arxiv.org/abs/2608.23927)

**<font color=#1a73e8>作者：</font>** Linhan Wang, Zijian An, Mingyuan Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generative models provide rich physical priors for robot learning, yet existing world-action models (WAMs) face a fundamental trade-off: synchronous video generation at control rate is latency-prohibitive, while abandoning test-time visual imagination sacrifices task success. We show that visual imagination achieves both real-time inference and superior success rates when generated asynchronously off the critical path and consumed directly in latent space. We introduce GlanceWAM, which decouples imagination from control within a single video DiT: an asynchronous proposer glances ahead on a slow clock to imagine a single lookahead frame seconds into the future in the background, while an action head decodes action chunks at control rate (48 ms) purely in latent space without blocking. Enabled by a non-interfering attention mask that isolates video representations and staleness-robust horizon training that accommodates asynchronous lookahead aging, GlanceWAM breaks the speed-success dilemma. Trained purely on demonstrations, it attains 72.2% on the 24-task RoboCasa kitchen benchmark (surpassing synchronous Cosmos Policy at 67.1% and imagination-free co-training at 64.4%) and 99.0% on LIBERO, executing at 48 ms per chunk on an NVIDIA A100 GPU (24x faster than synchronous baselines). Code is available at this https URL.

---


### 52. [SceneReGen: Generative Reconstruction of 3D Scenes from a Single Image](https://arxiv.org/abs/2608.23930)

**<font color=#1a73e8>作者：</font>** Zefan Tian, Yuteng Ye, Yiheng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image 3D scene reconstruction must complete partially observed objects and place them coherently in a shared observation-aligned scene frame. Object-level generative priors offer strong completion ability, but their centered, scale-normalized outputs are typically expressed in an object frame, creating a fundamental representation gap between object generation and scene reconstruction. We introduce SceneReGen, a generative reconstruction framework that reinterprets scene reconstruction as the generation and assembly of complete object assets in a shared observation-aligned scene frame. SceneReGen addresses the generation-reconstruction gap through selective pose factorization: each object's observed orientation is encoded directly in the generated mesh, while translation and scale are estimated from instance-level and global scene evidence. Given a scene image and instance masks, a geometry encoder extracts dense cues; learnable shape queries condition a pretrained DiT-based 3D generator to produce complete meshes in their observed orientations, while position queries fuse object and scene features to assemble them in the shared frame. On the 3D-FUTURE evaluation subset, SceneReGen achieves the best scene-level CD, scene-level F-Score, and 3D bounding-box IoU among the evaluated methods, ties the best object-level CD, and ranks second in object-level F-Score. Qualitative outputs in autonomous-driving and embodied-AI scenes further illustrate the potential of asset-centric reconstruction beyond indoor furniture.

---


### 53. [Evolutionary Recurrent Decision Model in Developing Adaptive and Maladaptive Behaviors](https://arxiv.org/abs/2608.23932)

**<font color=#1a73e8>作者：</font>** Andrew Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study introduces the evolutionarily recurrent decision model (ERDM), a computational reinforcement learning framework designed to examine how evolutionary mismatch, bounded rationality, and satisficing contribute to adaptive and maladaptive behavior. ERDM simulates agents across evolutionary recurrent environments, including threat, prey/goal-pursuits, and alliances. Agents learn through competing rewards abstracted from survival metrics. A validity study under varying adverse childhood experiences demonstrates that distinct adaptive and maladaptive strategies, such as learned helplessness, avoidance, healthy relationships, and aggression, emerge naturally without being hardwired. These results align with empirical literature, showcasing ecological validity. The results suggest that many psychopathology-relevant aspects may be interpreted as bounded cognitive systems operating under modern-ancestral environmental mismatch, positioning ERDM as a key computational cognitive tool that can be extended to other studies.

---


### 54. [SoK: ARCUS: On the Efficiency and Efficacy of Hardware Fuzzing](https://arxiv.org/abs/2608.23933)

**<font color=#1a73e8>作者：</font>** Alenkruth Krishnan Murali, Raghul Saravanan, Sai Manoj P D 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This work presents a comprehensive analysis of contemporary hardware fuzzing techniques applied across three major abstraction layers: Instruction Set Architecture (ISA), microarchitecture, and Register-Transfer Level (RTL). Our study examines key factors including input stimulus quality, mutation strategies, feedback mechanisms, target platforms, reference models, and achieved coverage. We find challenges, goals, and design trade-offs vary significantly across abstraction layers. We further identify several unmet needs in current hardware fuzzing practices, such as intelligent input generation, reliable and scalable golden reference models, expressive feedback channels, and cross-layer integration. Building on these insights, we outline future research directions, including hybrid fuzzing frameworks, AI-assisted test generation, scalable reference models, standardized evaluation metrics and benchmarks, and human-in-the-loop automation for guided exploration and analysis. Together, they aim to unlock efficient, reliable, and comprehensive hardware verification solutions.

---


### 55. [MnemoDyn: Learning Resting State Dynamics from 40K FMRI sequences](https://arxiv.org/abs/2608.23936)

**<font color=#1a73e8>作者：</font>** Sourav Pal, Viet Luong, Hoseok Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a dynamical-systems based model for resting-state functional magnetic resonance imaging (rs-fMRI), trained on a dataset of roughly 40K rs-fMRI sequences covering a wide variety of public and available-by-permission datasets. While most existing proposals use transformer backbones, we utilize multi-resolution temporal modeling of the dynamics across parcellated brain regions. We show that MnemoDyn is compute efficient and generalizes very well across diverse populations and scanning protocols. When benchmarked against current state-of-the-art transformer-based approaches, MnemoDyn consistently delivers superior reconstruction quality. Overall, we find that with such large-scale pre-training on (non-proprietary) rs-fMRI datasets, we get a highly performant model for various downstream tasks. Our results also provide evidence of the efficacy of the model on small sample size studies which has implications for neuroimaging studies at large where resting state fMRI is a commonly acquired imaging modality.

---


### 56. [CoDrift: Compositional Drifting for Offline Reinforcement Learning](https://arxiv.org/abs/2608.23939)

**<font color=#1a73e8>作者：</font>** Xiewei Ni, Ruofeng Mei, Xiangyu Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning is intrinsically multi-objective: a policy must remain compatible with the behavioral support of a fixed dataset while preferentially selecting high-value actions. We recast these objectives in a common form by viewing each as an action-space motion field that specifies how generated actions should move. This perspective enables heterogeneous learning objectives to be combined directly through field composition. Inspired by drifting models, we propose CoDrift, a compositional framework for one-step generative policy learning. CoDrift combines three objective-level fields into a unified policy field. The conditional field preserves state-dependent behavioral structure, while the marginal field pools actions across states to provide a more stable generative signal in the single-positive-sample regime of continuous-control offline RL. The value field moves generated actions toward higher-value regions. The composed field is absorbed into a stochastic generator that produces an action with a single forward pass at deployment. We evaluate CoDrift on 73 tasks from OGBench and D4RL in both offline and offline-to-online settings. CoDrift compares favorably with state-of-the-art methods and achieves the best average rank in both settings.

---


### 57. [Luce: Relightable Gaussians for 3D Asset Generation](https://arxiv.org/abs/2608.23943)

**<font color=#1a73e8>作者：</font>** Mayank Singh, Michele Stoppa, Alvise Memo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity image-to-3D generation requires a 3D representation that captures both geometry and appearance. To support relighting and integration into standard rendering pipelines, the representation should include physically based rendering (PBR) modalities such as albedo, metallic-roughness, and surface normals. We propose Luce, a 3D representation that unifies geometry and PBR materials within a voxelized multimodal Gaussian cloud, using dedicated Gaussian primitives for each modality. A variational autoencoder compresses this representation into a unified material-aware latent space. A rectified-flow transformer generates this latent from a single image, conditioned on multi-layer features from a pretrained image encoder that preserve both semantic context and fine spatial detail. The latent then decodes into relightable PBR Gaussians and an optional textured mesh with a tangent-space normal map. On Toys4K, Luce achieves state-of-the-art single-image-to-3D generation, improving FID by 28% over the strongest baseline. We further introduce a benchmark of AI-generated images, on which Luce improves the CLIP image-alignment score over the best baseline (0.8519 vs. 0.8299). Luce generates relightable, geometrically accurate, and materially faithful assets that preserve fine details such as text, logos, and inscriptions.

---


### 58. [STAIN-FL: Stealthy Targeted Attack Injection with Contextual Triggers in Federated Learning](https://arxiv.org/abs/2608.23952)

**<font color=#1a73e8>作者：</font>** Ashlinder Kaur, Purnima Murali Mohan, Zengxiang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated video anomaly detection trains model collaboratively without sharing raw surveillance footage, but limited server-side visibility lets compromised clients to inject backdoor via malicious updates. This paper introduces STAIN-FL, a stealthy targeted backdoor attack injection framework that uses naturally occurring surveillance conditions, including low-light scenes, indoor settings, and crowd density, as contextual triggers. STAIN-FL combines anomaly-to-benign label \textit{manipulation} with gradient masking over least-updated coordinates to preserve clean accuracy while inducing trigger-conditioned misclassification. We evaluate STAIN-FL on \texttt{UCF-Crime} using 1024-dimensional I3D features in a non-IID four-client multi-agency setting, comparing FedAvg and FedProx under sparse and continuous attacks. Results show that sparse attacks have low-detectability, operationally significant attacks rather than high-intensity attacks: they keep the mean clean-accuracy drop below $2\%$, yet still misclassify more than half of triggered anomalies at peak backdoor accuracy under FedAvg ($56.7\%$) and FedProx ($54.2\%$). Under FedAvg, the sparse backdoor remains above the $25\%$ backdoor-accuracy threshold for an average of $336$ post-attack rounds, highlighting the persistence risk of contextually triggered attacks in surveillance systems.

---


### 59. [Rules Before Oracles: Auditable, User-Configurable Argument Selection for Deliberative Polling](https://arxiv.org/abs/2608.23979)

**<font color=#1a73e8>作者：</font>** Muntaser Syed, Markus Zanker, Marius Silaghi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In a deliberative poll, once submissions outnumber what anyone will read, some mechanism chooses which arguments each voter sees, acquiring much of the decision; practice delegates it to opaque learned rankers, so a voter cannot recompute or contest the exposure that shaped their vote. We ask whether it can be a published rule over publicly recomputable evidence with parameters held by the voter, treating legibility as an admissibility condition on usable mechanisms, not an objective traded against accuracy. We formalise a poll over bipolar justification sets, judging a slate by reason coverage, the order it arrives in, and captured endorsement mass; we give seven checkable criteria for a civic recommender and a rule meeting them: a one-hop reversed endorsement flow parameterised by a relation-weight function. An agentic simulator records every slate at every vote, over about 17,000 seed-paired runs. Served slates fall 0.035 short of a label-reading ceiling upper-bounding every selection procedure, opaque ones included: any unconstrained ranker's advantage is bounded and small. On coverage alone, with non-degenerate authoring, the rule is indistinguishable from a random slate, a null due to an order-blind, charity-blind instrument; on the other two it leads at every prefix by a margin widening with adversarial pressure and dominates on mass by a factor of 3.3. Once a realistic fraction of submissions carries no reasons, the coverage margin returns and grows. Label-homogeneous flooding collapses completeness from 0.81 to 0.34 under a flat weight policy, only to 0.44 under author-count normalisation, making the weight function a security control worth 10% of completeness. The choice between ranking arms is a position on a coverage-versus-mass frontier, not a fact, the kind of choice only a legible rule can hand to the person it affects. It maps onto an open-source peer-to-peer platform.

---


### 60. [Source-Face Authenticity Detection for 3D Gaussian Heads Reconstructed from a Single Portrait: A Benchmark and Dedicated Detector](https://arxiv.org/abs/2608.23984)

**<font color=#1a73e8>作者：</font>** Yujie Gao, Zijian Yu, Yan Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in single-image 3D Gaussian head reconstruction have enabled highly realistic and freely renderable digital heads from a single portrait. However, reconstruction and rendering can weaken the forgery traces in the source portrait, making the resulting 3D face difficult to classify whether its underlying face is real or fake, and thereby posing risks to identity authentication and face privacy. To study this problem, we introduce the first large-scale benchmark for this task by collecting real portraits and fake portraits from multiple sources and evaluate representative existing detectors on this benchmark, revealing their lack of explicit mechanisms for retaining fine-grained information and maintaining feature consistency across rendered views. To directly address these two limitations, we propose a detector trained with a two-stage strategy. In Stage I, masked autoencoding encourages the visual backbone to retain the fine-grained appearance information required for local reconstruction, while multi-view contrastive learning enforces feature consistency across rendered views of the same head. Since CLS tokens at different depths exhibit complementary spatial attention patterns, Stage II freezes the adapted backbone and concatenates low-, middle-, and high-level CLS tokens for classification. Experiments show that our method achieves the highest accuracy and ranks first across all reported metrics among the evaluated detectors.

---


### 61. [Low-Latency Activation-Regularized Sparse Neural Operators with Distillation Assistance Towards Real-Time Edge-Deployable Virtual Sensing](https://arxiv.org/abs/2608.23987)

**<font color=#1a73e8>作者：</font>** William Howes, Farid Ahmed, Syed Bahauddin Alam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Virtual sensing enables digital twins and safety-critical systems to reconstruct and forecast spatial-temporal physics in real time. However, conventional computational and data-driven methods often face challenges in generalization, latency, and energy efficiency for edge deployment. Neural operators offer a promising alternative but remain reliant on power-intensive hardware. Spiking neurons and neuromorphic computing can improve efficiency, yet surrogate-gradient training and multi-step spiking introduce convergence and latency challenges. We propose the Sparse-Activation-ReLU (SAR) layer, a single-step alternative that promotes activation sparsity without surrogate-gradient training while remaining compatible with event-based computing. Within a trunk-based NOMAD architecture, SAR achieves over a fivefold improvement in the combined Latency-Error-Energy (LEE) metric compared with Variable Spiking Neuron (VSN) and Leaky Integrate-and-Fire (LIF) implementations. We further analyze spiking entropy and feature usage and introduce synthetic knowledge distillation, reducing the LEE score by more than twofold. Finally, we improve VSN through a ReLU-based spiking loss and graph-neighbor thresholding. On the Heat Exchanger dataset, these approaches reduce L2 error by more than twofold and nearly sevenfold, respectively, while reducing spiking and spatial aggregation. Overall, the work presented is a step towards energy-efficient virtual sensing by providing an alternative framework that can be positioned towards neuromorphic or other edge device integration that can be a gold standard to compare latency, energy, and error performance for future efficient designs that are sparsity or brain-inspired spiking based.

---


### 62. [Revenge of Monosemanticity: Specialized Neurons Improve Data Efficiency in MLPs](https://arxiv.org/abs/2608.24007)

**<font color=#1a73e8>作者：</font>** Amirhesam Abedsoltan, Enric Boix-Adsera, Fivos Kalogiannis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how neural networks learn and organize features is central to understanding their behavior. Much existing theory of feature learning has focused on the emergence of a global low-dimensional predictive geometry. We show that this picture is incomplete. In regression problems with clustered data, we demonstrate that multilayer perceptrons (MLPs) naturally develop monosemantic specialized neurons: individual neurons become strongly aligned with a specific predictive feature relevant to a particular region of the input space. Rather than learning a single global low-dimensional representation, MLPs learn a collection of local low-dimensional representations that can collectively span a high-dimensional space. This specialization provably gives MLPs a data-efficiency advantage over feature-learning methods based on a global low-dimensional representation.

---


### 63. [Absorbing Gradient Conflicts: Modeling Semantic Variance via Kent Distributions for Cross-Modal Hashing](https://arxiv.org/abs/2608.24010)

**<font color=#1a73e8>作者：</font>** Hengjie Zhu, Dayan Wu, Zihao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised proxy-based deep cross-modal hashing has become the dominant paradigm for large-scale retrieval. However, prevalent methods model class proxies as deterministic points in the embedding space. This rigid assumption causes severe gradient conflicts in multi-label scenarios, where gradient conflicts arising from label co-occurrence lead to severe gradient contention and optimization collapse. To resolve this, we propose Kent-based Distributional Proxy Hashing (KDPH), a novel framework that shifts proxy representation from static points to flexible anisotropic Kent distributions on the hypersphere. Unlike point proxies that must shift their positions to accommodate conflicting gradients, KDPH absorbs these conflicts by dynamically adjusting its directional variance. This allows the proxy to maintain a stable semantic mean direction while stretching to cover diverse label correlations. Furthermore, to ensure stable training of these geometric parameters, we derive a tailored loss function incorporating the Cayley transform to enforce strict orthogonality. To the best of our knowledge, KDPH is the first framework to successfully introduce the Kent distributions into cross-modal hashing. Experiments on three benchmark datasets demonstrate that KDPH mitigates proxy collapse and chaotic oscillation, significantly outperforms state-of-the-art methods. Code is available at this https URL.

---


### 64. [Reflection with Action-Induced Visual Differences for Desktop GUI Agents](https://arxiv.org/abs/2608.24015)

**<font color=#1a73e8>作者：</font>** Yijie Ma, Chaoyue Niu, Fan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Planner-Operator-Reflector (POR) framework is widely used in GUI agents to maintain objective alignment in complex tasks through modular collaboration. However, desktop GUIs introduce a key challenge: large, dense interfaces often exhibit subtle or scattered state changes, placing most of the burden on the reflector, which must compare pre- and post-action screens, while the planner and operator reason over a single state. Existing reflectors collapse change detection and outcome verification into one step, leaving evidence implicit and yielding weakly grounded decisions. To address this limitation, we propose Evidence-First Reflection (EFR), a two-stage reflector that explicitly decouples action-induced visual differences extraction from outcome verification. EFR identifies the action location and candidate changed regions with Set-of-Marks annotations, describes and filters action-relevant changes, and makes the final judgment from the cleaned evidence. This evidence-reasoning decoupled design makes reflection better grounded in screen transitions, while reducing both visual search complexity and reasoning burden. Experiments on OSWorld-Verified and WindowsAgentArena demonstrate that EFR improves reflector accuracy by 7.11%, yielding average end-to-end task success gains of 5.94% and 4.95% on the two benchmarks, respectively.

---


### 65. [IterCAD: Iterative Program Repair for CAD Code Generation from Orthographic Views](https://arxiv.org/abs/2608.24020)

**<font color=#1a73e8>作者：</font>** Yuchuan Wu, Ke Niu, Haiyang Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating executable parametric CAD code from dimension-annotated orthographic drawings is a challenging task requiring geometric understanding, procedural reasoning, and precise numerical prediction. Existing vision-language approaches typically formulate this problem as one-shot generation, preventing the model from inspecting intermediate CAD results and correcting early mistakes, often leading to non-executable code or geometrically inconsistent outputs. In this paper, we propose IterCAD, an iterative framework that reformulates orthographic-view-to-CAD generation as a progressive program repair process. Instead of predicting the final CAD code in a single pass, IterCAD repeatedly analyzes the current CAD result, reasons about its discrepancy with the target views, and explicitly decides whether to REVISE the code or STOP the refinement process. To make iterative repair learnable, we further construct IterCAD-RS, a structured revise-or-stop supervision set containing both repairable intermediate CAD states and already-correct states, and develop a three-stage training strategy for initial generation, revision learning, and multi-turn RL optimization. By closing the loop between visual understanding, geometric verification, and code refinement, IterCAD progressively corrects structural and parametric errors. Experiments on CADExpert show that IterCAD consistently improves code executability and geometric fidelity over strong one-shot baselines.

---


### 66. [Low-Rank Velocity Fields as a Structural Prior for Unsupervised 4D Medical Image Interpolation](https://arxiv.org/abs/2608.24025)

**<font color=#1a73e8>作者：</font>** Haojin Li, Hengzhuo Wang, Chang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Endpoint-only unsupervised 4D medical image interpolation synthesizes intermediate volumes from sparsely sampled sequences with only the start and end volumes available for training; however, this weakly constrained setting often yields intermediates with unstable boundaries and non-physiological motion, limiting interpretability and downstream analysis. We propose low-rank velocity fields as a structural prior, constraining motion to a structured Tucker low-rank velocity field space that decomposes motion into globally shared spatial bases and a compact sample-specific core, thereby encouraging spatially correlated, anatomy-consistent deformation while suppressing voxel-wise high-frequency artifacts. To capture global coordination and local non-rigid details, we model motion in a coarse-to-fine multi-scale scheme and compose scale-wise deformations at inference to synthesize volumes at arbitrary times. We further provide a theoretical analysis showing that, under Tucker parameterization, low-rank parameters control the smoothness energy of the velocity field, explaining why low-rank modeling promotes smoother motion. Experiments on ACDC and 4D-Lung demonstrate state-of-the-art performance, remaining competitive with methods trained with intermediate-frame supervision, and producing intermediates with improved structural coherence and more stable anatomical contours.

---


### 67. [Phase-Aligned Finite-Fourier Periodic Deformation for 4D Medical Image Interpolation](https://arxiv.org/abs/2608.24027)

**<font color=#1a73e8>作者：</font>** Haojin Li, Hengzhuo Wang, Zhiheng Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D medical image interpolation aims to recover missing volumes from sparsely observed time points and is important for dynamic anatomical analysis in applications such as cardiac MRI and thoracic CT, where motion is often repetitive or near-periodic over clinically relevant intervals. A key challenge is that this structure is not always encoded directly in deformation representations for interpolation. In addition, physiological motion is often non-uniform, so equal temporal intervals do not necessarily correspond to equal amounts of anatomical change. To address these issues, we formulate interpolation as learning a continuous deformation process with a phase-structured prior. Given two endpoint volumes, we parameterize a phase-conditioned velocity field with a finite Fourier basis, which embeds near-periodic motion patterns directly into the deformation space and supports continuous querying at arbitrary target times. We further introduce a phase-aligned temporal reparameterization that maps normalized within-interval time to a latent motion phase according to deformation variation intensity, thereby better modeling non-uniform motion progression. Intermediate volumes are then synthesized by continuously warping both endpoints, followed by bidirectional fusion and lightweight residual refinement. Experiments on ACDC and 4D-Lung show that the proposed method achieves state-of-the-art performance over existing baselines while producing anatomically plausible and coherent intermediate volumes from sparse observations.

---


### 68. [XP-JEPA: Cross-Predictive Physics Grounding for Forecastable Latent Dynamics](https://arxiv.org/abs/2608.24044)

**<font color=#1a73e8>作者：</font>** Kehan Wen, Ziming Li, Siyuan Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models plan by predicting how candidate actions transform learned representations. In self-predictive models, however, the encoder and predictor are optimized jointly and can co-adapt to latent transitions that are easy to predict but only weakly constrained by the physical evolution of the scene. We introduce the cross-predictive JEPA (XP-JEPA), which grounds visual latent dynamics in privileged physical trajectories. XP-JEPA separately encodes visual observations and physical states, advances both through a shared action-conditioned predictor, and matches each prediction to both future representations. This objective encourages unified latent dynamics across the two modalities, grounded in the underlying physical transitions. The physical branch is discarded after training, leaving a visual-only model at deployment. On a multi-task suite spanning six evaluation subfamilies, XP-JEPA reduces rollout drift of a newly fitted predictor from $0.361$ to $0.104$ and increases mean control success from $53.6\%$ to $78.2\%$. Direct physical-state regression raises position decodability but leaves forecastability and control near the visual-only baseline. Cross-predictive physical grounding can therefore produce more forecastable latent dynamics for rollout-based control without privileged inputs at test time.

---


### 69. [Physics-Integrated Operator Learning via Gaussian Splatting Representations](https://arxiv.org/abs/2608.24049)

**<font color=#1a73e8>作者：</font>** Jihao Zhang, Junyi Guo, Jian-Xun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators provide efficient surrogates for spatiotemporal PDE systems, but purely data-driven formulations often accumulate substantial errors during long-horizon autoregressive prediction and may fail to exploit available governing-equation structure. Existing approaches incorporate physics primarily through residual-based training objectives or PDE-specific architectural constraints, which can introduce optimization difficulties or limit architectural generality. In this work, we introduce a representation-level approach to physics integration in which a feed-forward Gaussian splatting (FFGS) representation serves as a continuous interface between discretized solution fields and governing operators. The FFGS representation reconstructs the state as a continuous Gaussian field with closed-form spatial derivatives, allowing available physical PDE operators to be integrated directly within the learned evolution map without introducing a physics-residual loss. We evaluate the framework across two- and three-dimensional PDE systems, including advection, diffusion, nonlinear self-advection, and reaction dynamics. Over long-horizon autoregressive rollouts, the proposed framework reduces relative $\ell_2$ error by $1.5\times$--$2.2\times$ compared with the strongest purely data-driven baseline across the benchmark suite, while consistently improving spectral fidelity. The framework also remains effective when the governing equations are partially known, demonstrating robustness to incomplete physics. These results demonstrate that continuous field representations can provide a practical interface for incorporating known physical structure into generic neural-operator surrogates.

---


### 70. [ALPHABET: A Laplace-Pole History Aggregator with Banked Exponential Transport](https://arxiv.org/abs/2608.24051)

**<font color=#1a73e8>作者：</font>** Daehwa Ko, JaeHyeon Kim, Oh Seong Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a sequence model remain competitive with only a few thousand parameters and an explicitly auditable prediction interface? We introduce ALPHABET, a compact linear-time model that compresses temporal history into stable complex pole modes: a direct bank synthesizes its modal states back into the feature trajectory, an independent cascaded bank analyzes the transformed trajectory without resynthesis, and an affine head reads only modal energies and lag moments from both banks. We characterize the temporal information this descriptor retains: for a stationary, fully observed feature process, each mode energy is a frequency-localized measurement of the second-order spectrum, the continuum of such measurements identifies the spectrum, and almost every mode separates any fixed finite set of spectrally distinct classes. On a Gaussian control with matched low-lag statistics, the learned descriptor approaches the Bayes oracle where raw autocovariances remain at chance. Across the fixed 82-task registry, ALPHABET attains mean rank 3.97 in the complete ten-family comparison. At the common-width D=64 runtime anchor, its 6,437 parameters deliver 5.02 times faster inference and 3.93 times faster complete training steps than the nine baselines on average.

---


### 71. [WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://arxiv.org/abs/2608.24053)

**<font color=#1a73e8>作者：</font>** Junjie Zhou, Ke Mei, Lei Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Universal multimodal embeddings are becoming a core component of modern AI systems, enabling heterogeneous content to be represented in a shared space for applications such as retrieval, recommendation, classification, and agentic systems. In this report, we present WeMM-Embedding, a family of universal multimodal embedding models supporting text, images, videos, visual documents, and arbitrarily interleaved multimodal inputs with flexible output dimensions. The family comprises 2B, 4B, and 9B variants and is trained in two stages: a large-scale multimodal alignment stage, followed by a refinement stage using curated data, fine-grained relevance supervision, and cross-scale knowledge transfer. Across extensive evaluations, WeMM-Embedding achieves leading performance on multiple public benchmarks. Notably, the 2B variant already surpasses the previously leading 8B open-source baseline on MMEB-v2, while the 9B variant further achieves a new state-of-the-art overall score of 80.6. WeMM-Embedding also demonstrates strong practical performance across WeChat applications, with substantial gains on a 26-task in-house benchmark and consistent improvements across 14 online A/B tests. It has been deployed at scale across recommendation and search applications, including WeChat Channels, Official Accounts, Moments, and e-commerce services. We have released the model weights and code to facilitate future research at this https URL.

---


### 72. [PhysicsBench: A Unified Leaderboard for Generative and Predictive Models in Engineering Design and Simulation](https://arxiv.org/abs/2608.24056)

**<font color=#1a73e8>作者：</font>** Sang Won Lee, Hyogu Jeong, Namwoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative and predictive artificial intelligence models are increasingly used to generate geometry and to predict physical fields and scalar quantities in engineering design and simulation. Yet these models are typically evaluated in isolation, on academic datasets at unconstrained scales, with inconsistent metrics and procedures. We present PhysicsBench, a unified benchmark and leaderboard that evaluates generative and predictive models under one standardized procedure. PhysicsBench spans seven generation and prediction tasks across 1D, 2D, and 3D domains and ranks 66 models on nine datasets, comprising industrial-scale CAD/CFD/FEA simulations and public references, expanded into 28 configurations. One procedure and ranking apply to both families, each ranked within its own tasks. Evaluation spans realistic, limited data scales from S to XL rather than the unlimited training sets common in academic benchmarks. A common metric suite captures geometric fidelity with distributional distances, physical-field and scalar accuracy, and engineering-specific field- and shape-validity. BenchRank debiases correlated metrics and ranks by PageRank over a head-to-head dominance graph, so every reported quality metric is also ranked, with computational cost in a separate efficiency view. Across tasks, an architecture's large-scale academic standing weakly predicts its small-data ranking. The top model changes with data scale in six of the seven tasks, and no model leads more than one task. PhysicsBench turns "state-of-the-art" from a self-reported claim into an openly published foundation for model selection.

---


### 73. [Negotiating Ontological Boundaries in User-Authored Personal Sensing Systems](https://arxiv.org/abs/2608.24058)

**<font color=#1a73e8>作者：</font>** Nava Haghighi, Danielle Olson, Halden Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designed artifacts are ontological, shaping, and at times limiting, what becomes possible or imaginable. One path toward mitigating such foreclosures is giving people power over how systems are designed and built. Despite decades of scholarship around systems that enable such authorship, these systems are often evaluated on whether or not they are usable, useful, or technically feasible, leaving questions of ontological boundary negotiation, unexamined. We design two open-ended probes that utilize a Wizard of Oz technique to enable the experience of training a personalized machine learning system on phenomena people define themselves. In a week-long exploratory study, participants use one of two probes in the course of their everyday lives. We identify four sites where ontological boundaries were negotiated; the boundaries of a phenomena, the subject as part of relations, what is signal and what is noise, and the objectivity of data. We offer starting points for supporting boundary negotiation through design and discuss open-ended probes as a method for ontological design.

---


### 74. [Mechanistic Circuit Identification for Controllable Data Generation](https://arxiv.org/abs/2608.24065)

**<font color=#1a73e8>作者：</font>** Nakyung Lee, Sangwoo Hong, Jungwoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While recent advances in data synthesis aim to curate high-quality datasets, most generation pipelines still rely on heuristic prompt-based control. This black-box paradigm provides limited insight into how individual samples interact with a model's underlying learning dynamics. To bridge this gap, we propose a circuit-grounded framework that connects training-dynamics-based data valuation with mechanistic interpretability (MI). Specifically, we conceptualize data quality along three complementary utility axes, learnability, challenge, and alignment. First, we uncover specialized model-internal circuits that causally govern these utility signals. Then, moving beyond heuristic prompting toward mechanistic control, we leverage these circuits as controllable interfaces, actively steering generation to produce utility-targeted data. Building on this capability, we introduce SAMS (Stage-Aware Mechanistic Scheduling), which schedules circuit-steered data according to the model's evolving optimization needs. Experiments on multiple-choice QA tasks demonstrate that our approach yields precisely controlled data with greater diversity than prompt-based baselines, consistently improving downstream performance and calibration. Ultimately, this work establishes a principled white-box paradigm for interpretable data generation, pioneering the use of MI not just as an analytical tool, but as a practical, controllable interface.

---


### 75. [A Feature-Major Codebook for Memory-Efficient Sparse-Binary Self-Organizing Maps: Scaling a MEDLINE Atlas to 1.05 Million Neurons on a Single Consumer GPU](https://arxiv.org/abs/2608.24067)

**<font color=#1a73e8>作者：</font>** Andrew James Amos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A self-organising map turns a large corpus into a browsable two-dimensional atlas, but building one at MEDLINE scale has been impractical: the best-matching-unit (BMU) search that dominates training is bound by the bandwidth needed to read the codebook every epoch. I show that this bottleneck is largely an artefact of codebook layout. Storing it feature-major with each feature's weights contiguous, W[v.M+i], recasts the search as a tiled sparse-dense product in which every loaded weight column is reused across a tile of samples. Varying only the layout, with implementation, precision and update rule held fixed, accelerates the BMU search by 4.5-8.5x. Because an exact-argmin BMU is invariant to how the codebook is stored, this gain costs nothing: held-out quantisation error agrees with a cuSPARSE baseline to within 0.5% at every map size. Against that baseline the advantage is a crossover rather than a constant: this http URL is faster at small maps, this http URL is 1.5x faster at 128x128 and 2.6x at 256x256, and at 512x512 it is the only one that runs at all on 24 GB. Paired with a radius-independent box-blur update and a convergence-based stopping rule, it trains a converged map over 29.9 million MEDLINE articles in about 72 s at 64x64 on one 24 GB GPU, and accommodates 262,144 neurons (512x512 edges) where every alternative algorithm I tested exceeds memory constraints. On a 141 GB H200 it reaches 1,048,576 neurons (1024x1024 edges) - to my knowledge the largest self-organising map yet reported. Held-out error follows a smooth power law with no elbow across three decades of map size, so the limit on resolution is compute rather than any breakpoint in the data. At matched work the design is ~82x faster than MedSOM, the CUDA implementation behind our earlier MEDLINE atlases and, at 128x128, 621x faster than the best available multicore-CPU library.

---


### 76. [Representation Learning in Diffusion and Flow-based Model: An Application Aspect](https://arxiv.org/abs/2608.24068)

**<font color=#1a73e8>作者：</font>** Yanchen Xu, Sida Huang, Zhenyu Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models and flow-based models have recently become the dominant paradigms in generative modeling, largely due to their ability to learn rich, multi-level visual representations through large-scale training. This creates a bidirectional relationship between generative models and representation learning: improving representation learning enhances generation quality, while the learned representations can be leveraged for broader understanding tasks. This survey systematically explores this interplay with a focus on applications. We propose a three-tier progressive framework that organizes existing works from three perspectives: using representation learning to improve generative capabilities, exploiting generative models to extract representations for perception tasks, and ultimately moving toward general-purpose unified applications. We systematically categorize representative methods across a wide range of downstream tasks, including image classification, dense visual prediction, instance-level perception, and annotation-scarce scenarios. By providing a unified taxonomy and identifying key challenges, this survey aims to clarify the underlying logic of current research and suggest promising directions for future exploration. We hope this work can serve as a valuable reference for researchers interested in harnessing the representation power of generative models for applications beyond generation.

---


### 77. [AgentWorld: Personality-Aware Reliability Evaluation for Agentic Information Retrieval](https://arxiv.org/abs/2608.24076)

**<font color=#1a73e8>作者：</font>** Gunja Agarwal, Arup Kumar Das, Arun Menon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluation of agentic information retrieval remains limited to scripted interactions with uniform users, missing both natural personality diversity and adversarial brittleness. We present AgentWorld, a simulation framework combining (i)Big Five (OCEAN) personality-driven user populations with stateful tool-use environments; (ii)the pass$^k$ consistency metric with structured fault classification, partial-credit scoring, and dual-control handoff verification; (iii)score-thresholded training-data export in six fine-tuning formats; and (iv)an adversarial Risk Analyser that snapshots required-intermediate-state spines, branches Monte-Carlo rollouts under four task-aware perturbation types, and quantifies risk via $\Delta P / \Delta T$ scoring, Dempster--Shafer evidence fusion, and Shapley attack-category attribution. Three experiments demonstrate the framework: a conversational analytics agent across 10 OCEAN personas (240 evaluator judgments); a customer-support agent across 5 tasks $\times$ 4 persona variants; and adversarial stress-testing of 5 tasks revealing pre-existing trajectory brittleness ($V_{\min}=0.375$ without perturbation) and tool/infrastructure-layer attack dominance (Shapley: 46% system, 38% action). Personality variation surfaces failure modes uniform testing cannot expose---cross-domain leakage, contextual drift, a 0.27-point quality gap, and 50% vs. 100% pass-rate across personas on the same task---while the Risk Analyser quantifies trajectory-level brittleness that pass$^k$ alone cannot measure.

---


### 78. [Joint-Embedding Prediction of Masked Point Tubes for Self-Supervised Learning on 4D Point Cloud Videos](https://arxiv.org/abs/2608.24093)

**<font color=#1a73e8>作者：</font>** Jheng-Ling Lee, Shang-Tse Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised representation learning for 4D point cloud videos is challenging because annotations are costly and reconstruction-based pretraining can overemphasize low-level geometric details. We propose a JEPA-style framework that learns from unlabeled spatiotemporal point clouds through latent point-tube prediction. Instead of reconstructing raw coordinates, the model masks spatiotemporal regions and predicts their target representations from visible context representations in feature space. To stabilize latent prediction, we incorporate Sketched Isotropic Gaussian Regularization, which encourages non-collapsed embeddings without relying on explicit reconstruction targets. This formulation aims to capture both spatial structure and temporal dynamics while keeping the pretraining objective aligned with downstream semantic recognition. Experiments on action and gesture recognition benchmarks show that the learned representations improve downstream fine-tuning, limited-label learning, and cross-dataset transfer. These results suggest that JEPA-style latent prediction is a promising alternative to reconstruction-centered pretraining for 4D point cloud videos.

---


### 79. [The Sharp Tail of Uniform Stability](https://arxiv.org/abs/2608.24098)

**<font color=#1a73e8>作者：</font>** Pahan Dewasurendra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uniform stability controls how much one training example can change the loss at any test point. A new logarithmic-free upper bound shows that a $\gamma$-uniformly stable algorithm with loss in $[0,L]$ has generalization gap at most $O \left(\gamma\log(1/\delta) +L\sqrt{\frac{\log(1/\delta)}{n}}\right)$ with probability $1-\delta$. Whether an actual bounded-loss learning algorithm can realize the linear dependence on $\log(1/\delta)$ has remained open. The known construction realizes it only for auxiliary weakly dependent random variables whose pointwise range grows with $n$. The known learning lower bound holds only at constant probability. We close this gap. For every $n$, stability level $\gamma$, and loss bound $L$, we construct one deterministic $\gamma$-uniformly stable learning problem whose tail satisfies, simultaneously for $1\le p\le c n$, $\mathbb P \left( R(A_S)-R_S(A_S) \ge c'\min \left\{L,\gamma p+L\sqrt{p/n}\right\} \right)\ge e^{-p}.$ The construction is ordinary bounded absolute-loss regression with constant labels. Its key is a multiscale collection of rare Rademacher features. A coordinatewise ramp is stable in sup norm, while an odd symmetrized maximum converts a unique extreme feature into a gap of order $\gamma p$ without violating the loss bound. Geometrically spaced ramps put all confidence levels into the same problem. Together with the logarithmic-free upper bound, this determines the optimal high-probability and moment dependence of uniform stability up to universal constants.

---


### 80. [MatReplace: A Reference-Free, Conditioning-Aligned Benchmark for Material Replacement in Interior Scenes](https://arxiv.org/abs/2608.24107)

**<font color=#1a73e8>作者：</font>** Mingzhe Du, Thong Thanh Nguyen, Nguyen Tran Cong Duy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Material replacement is a common interior-design operation: changing the material of a selected surface while preserving its geometry, surroundings, and illumination. Despite its commercial relevance, no public benchmark isolates this task, and evaluating it is challenging. Reference-based metrics penalize valid outputs in this inherently one-to-many setting, favor the style of the reference generator, and cannot fairly compare editors that receive different forms of guidance. We introduce MatReplace, a reference-free benchmark that evaluates edits along four verifiable dimensions: local material correctness, global lighting harmony, outside preservation, and inside structure. It defines three tracks that vary one conditioning signal at a time: (A) instruction only, (B) instruction plus region mask, and (C) material reference image instead of instruction. Our results reveal a clear divide between naming and visually grounding materials. In Track A, leading closed-source editors achieve exemplar-level material rendering and surpass the exemplar anchor under our primary aggregate. In Track B, masks help only mask-compatible models with weak scene preservation, with task-paired, single-seed effects ranging from +0.137 to -0.090 across aligned model families. In Track C, reference-image conditioning degrades every family under both aggregates, by -0.031 to -0.508; in the worst cases, models repaint the reference image itself and perform worse than returning the input unchanged. Thus, named-material rendering is largely solved by the strongest closed editors on this distribution, but grounding materials from pixels remains an open challenge. Expert ratings validate our ranking (Kendall's tau = 0.68) and align with our aggregates more closely than GT-referenced or CLIP-based baselines.

---


### 81. [Scalable Question-Centric Text-to-Image Evaluation: Reliable Ranking, Fine-Grained Diagnosis, and Cost-Aware Routing](https://arxiv.org/abs/2608.24112)

**<font color=#1a73e8>作者：</font>** Shaoan Zhao, Fang Zhao, Xueqiang Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image (T2I) models often have similar total scores but different strengths, making practical selection difficult. Fine-grained benchmarks decompose prompts into questions, yet often return them to prompt scores and fixed categories, weakening attribution and ignoring complexity. Related requirements are also scored separately or as one total, obscuring basic versus compositional failure. We present QC-T2I-Bench, a question-centric framework that converts open prompts into attributed atomic questions and organizes their dependencies with Davidsonian Scene Graphs (DSGs). We use hierarchy-constrained question aggregation to exclude downstream questions after a prerequisite fails and to prevent simple and complex prompts from receiving the same total weight. We then use the DSG structure to measure joint success within prompts and compare repeated entities across prompts, separating basic realization failures from failures under additional requirements. We evaluate multiple open-source T2I models on English and Chinese prompts. The resulting question-level evidence supports reliable ranking and fine-grained diagnosis: joint completion falls from 80.7\% for components with two capabilities to 37.2\% for those with seven or more. Finally, we reuse the same records for training-free routing; our cost-aware router matches ERNIE's 89.51-point estimate with 21.3\% less GPU-s/MP.

---


### 82. [A mesh-free multiresolution deep energy method with phase-field modeling of brittle fracture](https://arxiv.org/abs/2608.24126)

**<font color=#1a73e8>作者：</font>** Han Zhang, Mehrisadat Makki Alamdari, Babak Shahbodagh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Phase-field modeling of brittle fracture removes the need to track cracks explicitly by recasting their evolution as the minimization of an energy functional. In return it requires a discretization dense enough to resolve a localization band whose width is set by a regularization length and whose path is not known in advance. We propose a mesh-free discretization in which a single neural network represents the displacement and phase fields and is trained by minimizing the incremental energy directly. The coordinates enter the network through a multiresolution feature encoding built from $C^1$ quadratic B-spline grids, so the finest scale the representation can express is set by choice rather than reached through slow training, and the energy is estimated by stratified Monte Carlo integration on points redrawn at every optimizer iteration. This pairing proves critical, since the crack fails to advance both when the integration points are held fixed and when the encoding is too coarse to represent the band, while each ingredient tolerates a wide range of settings once the other is in place. Because the representation is globally $C^1$, the second- and the fourth-order fracture energy densities run on the identical discretization. Across six problems, from single-edge-notched tension and shear to a thick-walled ring on a single spline patch, the computed load-displacement curves follow staggered finite element references at matched regularization length, with peak loads within about 1% on the single-edge-notched tests and within 8% where the crack pattern changes topology. On a public benchmark dataset of random multi-crack configurations the method classifies the active or dormant state of 90% of the seeded cracks in twenty zero-shot runs, where the deep Ritz baseline of the dataset authors fails.

---


### 83. [Syn2RealTrack: Bridging the Gap Between Synthetic and Real-World Datasets for Online Multi-View Multi-Target Tracking](https://arxiv.org/abs/2608.24130)

**<font color=#1a73e8>作者：</font>** Duong Nguyen-Ngoc Tran, Ngoc Doan-Minh Huynh, Cu Quoc Le 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-camera 3D perception systems for warehouse scenes are trained largely on synthetic data and evaluated on physically captured environments. The resulting synthetic-to-real gap, which corrupts ground-plane localization and cross-camera identity association, is usually treated as one deficiency for a single domain-adaptation module to absorb; we argue instead that it enters the pipeline at three separable points: the camera calibration, the object shape prior, and the assumption that the object census is known, each admitting a different local remedy. Our online pipeline, Syn2RealTrack, follows this decomposition: lens distortion is recovered from images alone under a calibration that provides none, detections are fused across views by a visibility-weighted part-based descriptor that abstains on occluded parts rather than guessing, person height is measured in closed form from calibration instead of copied from a synthetic prior, and a closed-world cardinality prior is paired with a causal filter that removes the phantom boxes the prior manufactures. The system therefore adapts by reallocating trust between geometry and appearance without retraining a feature extractor. On the AI City Challenge 2026 Track~1 evaluation server it reaches a 3D Higher Order Tracking Accuracy (HOTA) of 52.0118%. The code will be released at this https URL

---


### 84. [From Gradient-Boosted Trees to Deep Recommenders: Practical Lessons from Migrating a Production Customer Support Recommender](https://arxiv.org/abs/2608.24132)

**<font color=#1a73e8>作者：</font>** Sonia Sharma, Jeyendran Balakrishnan, Shreya Rajpal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Product catalogs in fast-moving service businesses are shifting from static, independently priced SKUs toward dynamically bundled, discount-coupled offerings--a shift that strains the tree-based classifiers traditionally preferred for sparse and highly imbalanced data. These classifiers assume a fixed, slowly changing label space and struggle to incorporate multimodal signals such as tabular data and transcripts. We present the migration of a live, production conversational recommendation system from a gradient-boosted multiclass model to a pairwise-binary deep recommender. Because this system is critical to ecosystem growth initiatives and downstream features like dynamic pitching--surfacing the most relevant pitch text to a support agent in real time during a live customer conversation--maintaining live recommendation quality was a non-negotiable constraint. We detail the techniques that made this migration successful--reformulating recommendation as pairwise binary prediction to learn jointly from user and item features, and enhancing learned representations via negative sampling and noise injection. To efficiently incorporate long, live conversation context, we apply attention pooling over transcript chunks and benchmark it against TF-IDF and sentence-embedding baselines. Finally, we explore multiple architectures (including two-tower models, DeepFM, and their variants) and loss functions such as contrastive loss. Evaluating against a CatBoost baseline across all conversational stages, we demonstrate that our approach achieves parity at conversation beginning and outperforms at later conversational stages.

---


### 85. [Robust Data-Collection Policy Learning for Low-Variance Online Policy Evaluation](https://arxiv.org/abs/2608.24146)

**<font color=#1a73e8>作者：</font>** Claire Chen, Shuze Daniel Liu, Licheng Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning policy evaluation, classic on-policy methods often suffer from high variance when estimating policy performance. To mitigate this issue, behavior policy search has been proposed to learn data-collecting policies tailored to reduce online evaluation variance. However, these approaches do not account for uncertainties in the transition functions. In practice, simulator transitions often differ from the real world due to modeling errors or approximation limitations. As a result, behavior policies trained in simulation may still yield high variance when deployed in real environments, leading to costly reliance on real-world evaluation samples. In this work, we propose a double-loop gradient-based algorithm for learning behavior policies that are both efficient and robust to transition uncertainty. Theoretically, we derive novel transition-variance gradient expressions and establish global convergence guarantees for the algorithm. Numerically, we demonstrate that our method is less sensitive to transition perturbations than existing approaches, providing supportive evidence for its practical utility.

---


### 86. [Rethinking Pre-Training and Augmentation for Zero-Shot Cross-City Object Detection](https://arxiv.org/abs/2608.24154)

**<font color=#1a73e8>作者：</font>** Long Hoang Pham, Quoc Pham-Nam Ho, Huy-Hung Nguyen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world deployment of traffic surveillance systems is bottlenecked by geographic domain shift, in which models trained in one city underperform when applied to an unseen target city. Conventional domain adaptation relies on hyperparameter-sensitive architectures or direct profiling of target data. Both are fundamentally precluded in privacy-conscious ecosystems that require completely blind training and evaluation loops. In this setting, we explore the effects of pre-training and augmentation in addressing the domain shift problem. Specifically, we propose a new modular training pipeline for object detection structured around two core orthogonal pillars: (1) a multi-dataset pre-training strategy featuring a class-agnostic objectness distillation to decouple structural vehicle geometry from semantic taxonomies, and (2) a domain-resilient augmentation stream featuring a novel Grayworld transformation that forces global attention heads to strip volatile chromatic shortcuts in favor of robust shape priors. When evaluated with the real-time transformer-based detector RF-DETR, our framework bridges cross-city distribution gaps while using limited GPU memory (16GB). Our optimized variants, RF-DETR-HR and RF-DETR-Grayworld, deliver a substantial empirical gain of +24.29 over the baseline, achieving 1st place (47.53 mAP) on the AI City Challenge Track 6 leaderboard. Code and data are available at: \href{this https URL}{SKKUAutoLab/aic26\_cross\_city}.

---


### 87. [Balancing Evidence and Interpretation: Historical Grounding Ratio as a Design Parameter for AI-Generated Urban Storytelling](https://arxiv.org/abs/2608.24157)

**<font color=#1a73e8>作者：</font>** Fuyang Zhang, Maurice Benayoun  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Location-aware generative systems can now select historical archives and real-time contextual information based on a user's surroundings to automatically generate narratives for urban heritage walks. Yet when multiple sources jointly inform generation, existing systems provide neither a clear representation of how much content from each source actually appears in the output nor an operational means of measuring it. We introduce the Historical Grounding Ratio (HGR), defined as the proportion of claim-bearing information units in a generated narrative that are supported by historical archives. HGR turns the realized share of historical evidence in a narrative into a directly measurable design parameter. In GeoDrama, a mobile narrative system, we created three conditions that used a common retrieval procedure and comparable evidence-bundle sizes while varying the allocation of information from different sources during generation. We evaluated how changes in HGR affected narrative experience through a within-subject walking study with 18 participants. Increasing HGR significantly strengthened the perceived relevance between narrative content and the specific location. However, historical understanding, integration with the visible scene, appropriateness of the amount of information, and intention to explore further did not increase monotonically with HGR; all four measures were highest in the intermediate, balanced condition. These findings show that designing location-aware generative interfaces involves not only retrieving relevant material but also determining how information from different sources composes the final output. HGR offers an operational measure for comparing information-allocation strategies and their experiential consequences.

---


### 88. [OmniJudge or OmniBias? Diagnosing Multimodal Judges through Balanced, Decoupled Lenses](https://arxiv.org/abs/2608.24160)

**<font color=#1a73e8>作者：</font>** Guangzheng Hu, Ziyue Jiang, Weixu Qiao 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal understanding models that can jointly judge text-to-image (T2I), text-to-video (T2V) and text-to-speech (TTS) generation are increasingly used as "OmniJudges" for evaluation and automatic annotation. How reliably they understand what they score remains unclear, since existing benchmarks and training data tend to overemphasize positive examples and to conflate distinct failure modes, so a judge may score well without recognizing failures while its capability gaps stay hidden. Motivated by this, we introduce D3-Omni, a balanced and decoupled benchmark for diagnosing fine-grained multimodal understanding, covering 53 orthogonal binary dimensions (17/22/14) and 10,671 samples (3,526/1,998/5,147) across the three tasks. Rather than re-generating outputs, which may leak information across dimensions, we fix verified fully positive seeds and derive negatives through controlled prompt rewriting and atomic, dimension-isolating perturbations. The resulting D3 design is Dual-balanced, which helps alleviate negative-sample scarcity and per-dimension label imbalance; Decoupled, so that each error is attributable to a single capability; and Dynamic, steering construction toward under-represented regions of the label distribution as generative models this http URL suite reaches near 1:1 per-dimension parity and a uniform distribution over all total-score levels. Under this balanced view, even strong OmniJudges tend to struggle on modality-related dimensions, to confirm satisfied requirements far more reliably than they detect violated ones, and to treat nominally distinct attributes as largely a single decision, suggesting that aggregate accuracy may hide systematic blind spots that a balanced and decoupled lens can help expose and, in turn, address.

---


### 89. [From Relaxed Indexability to Exact Indexability: A $t$-Step Approach for Partially Observable Restless Bandits](https://arxiv.org/abs/2608.24167)

**<font color=#1a73e8>作者：</font>** Qizhen Jia, Keqin Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Whittle index policies offer a scalable method for restless multi-armed bandits, but under partial observability even determining the indifference subsidy at a single belief requires solving an infinite-horizon belief-state problem with no closed-form value function. Liu [10] addresses this difficulty by linearizing the unknown decision boundary, leading to a linear system and a closed-form approximate Whittle index. However, the resulting threshold uses only a one-step active--passive comparison and does not account for longer-horizon continuation values.
We extend this framework to a \emph{$t$-step lookahead threshold policy}. For each subsidy $m$, the threshold is defined by the active-minus-passive advantage under $t$-step finite-horizon value iteration. At $t=1$, the threshold is $m$-independent and recovers the linear threshold of Liu [10]; for $t>1$, it becomes subsidy-dependent through the induced first-crossing structure and tracks the exact decision boundary more closely. The proposed algorithm does not require indexability as an input and includes an indexability verification. Under the original Whittle indexability, we prove that the $t$-step approximate Whittle index converges geometrically to the exact Whittle index, \[ |\widehat W_t(\omega)-W(\omega)|=O(\beta^t). \] Numerically, all 2,715 tested three-state instances are verified as indexable according to the proposed criterion. The P95 index error decreases from $2.18\times10^{-2}$ at $t=1$ to $8.93\times10^{-4}$ at $t=8$. In an exact-comparable instance with $\beta=0.9999$, $t=2$ already recovers the exact Whittle-index ordering. Moderate-depth threshold policies also outperform the one-step baseline and remain close to the optimal dynamic-programming benchmark, while runtime grows mildly with $t$.

---


### 90. [Task-Adaptive Rubrics for GUI Reward Modeling](https://arxiv.org/abs/2608.24174)

**<font color=#1a73e8>作者：</font>** Tao Xiong, Xavier Hu, Wenkai Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent studies on GUI agents have increasingly focused on outcome reward modeling, which assigns outcome rewards by judging whether an executed trajectory satisfies the success criteria implied by the user instruction. Existing GUI reward verifiers, however, often under-specify how these criteria should be constructed for each task instance. Whether using generic rubric structures or implicit model reasoning, their judging criteria are not sufficiently task-adaptive: they can transfer checks across tasks, overlook concrete constraints in the current instruction, or become overly strict by enforcing unstated requirements. To address this limitation, we propose AdaptRubric, a Coarse-to-Fine Rubrics Framework that constructs task-adaptive judging criteria through a category-level coarse stage and an instance-level fine stage. AdaptRubric performs category-level coarse rubric retrieval by routing the instruction to a GUI task family and retrieving reusable task-family criteria, then conducts instance-level fine rubric generation to surface compact cues for concrete values, scopes, and constraints in the current instruction. Across offline reward evaluation and online reinforcement learning optimization, AdaptRubric consistently outperforms prior reward agents, improving F1 by 3.6 points over the baseline average under a matched image budget and yielding a 4.23-point task-success gain.

---


### 91. [Amortized Set Prediction for Inverse IFS Reconstruction from Density Maps](https://arxiv.org/abs/2608.24175)

**<font color=#1a73e8>作者：</font>** Yutaka Yamaguti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iterated Function Systems (IFS) generate self-similar fractals from a few contractive affine maps. The forward map from parameters to images is computationally inexpensive and well understood, whereas the inverse problem of estimating maps from an image is difficult and is typically handled by per-image optimization. We replace this loop with a single forward pass of a learned estimator that predicts the affine-map set directly from a visit-frequency density map, thereby amortizing the inverse problem. The design follows two constraints. First, density maps do not uniquely identify IFS parameters, so evaluation is based on reconstruction rather than parameter recovery; unordered map sets are handled by Hungarian matching, and ground-truth parameters provide a stable training surrogate. Second, the fully known forward model lets us generate exact synthetic training pairs and also supports image-only test-time refinement. On in-distribution tests, amortized initialization plus a few refinement steps lies on a better quality--speed frontier than equal-budget random-initialized per-image optimization, and a 30-step refinement (about $0.56$ s per sample) remains better than a doubled-budget baseline. Extending optimization to 1000 steps shows that the benefit is not only speed: amortized initialization reaches high-quality reconstructions more frequently than random starts. On real images (MNIST and Fashion-MNIST), it improves density metrics on average over a published per-image optimizer while being roughly 12 to 2600 times faster.

---


### 92. [PRQ-KMeans: Projection Residual Quantization for Semantic ID Tokenization](https://arxiv.org/abs/2608.24207)

**<font color=#1a73e8>作者：</font>** Yunxiao Luo, Siyuan Wang, Ben Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semantic identifiers (SIDs) represent entities as hierarchical token sequences for generative retrieval and recommendation. Residual-quantization tokenizers construct these sequences by selecting a codeword at each level and passing a residual to the next. We view this process as progressive commonality removal: each token captures a component shared within its group, while later tokens should model the remaining differences. This view reveals three limitations: a corpus-wide shared component can consume first-level capacity, hard assignment ignores graded similarities to nearby codewords, and full-codeword subtraction can leave variation along the selected-codeword direction in the next residual. We therefore develop our solution in the post-hoc setting, where residual construction is not constrained by input reconstruction. Specifically, we propose PRQ-KMeans, which removes the global-mean component, refines centroids with Top-k similarity-weighted updates, and replaces full-codeword subtraction with a projection residual that removes each representation's selected-centroid component. Experiments on a large-scale industrial search dataset and four public recommendation benchmarks show that PRQ-KMeans achieves the strongest overall performance among the evaluated tokenizers, including gains of up to 7.4% in HitRate and 11.8% in MRR on the industrial dataset.

---


### 93. [A Data-dependent Early Stopping Rule using Rademacher Complexity with L1-norm](https://arxiv.org/abs/2608.24210)

**<font color=#1a73e8>作者：</font>** Duy Hoang, Bastien Berret, Olivier Bruneau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training neural networks requires balancing the trade-off between fitting the training data and achieving robust performance on unseen inputs. This ability, commonly referred to as generalizability, is determined by the gap between the empirical risk on the training set (``empirical loss'') and the expected risk over the data distribution (``generalization error''). Existing approaches typically estimate the generalization error numerically, requiring gradient descent training and an ``early stopping'' strategy. In this work, we introduce an analytic framework that estimates the optimal time of early stopping without the need for training. Several works in the literature also give such analytical estimations, but they are generally based on random matrix theory and often make assumptions on the distribution of the data or the eigenvalue distribution of the covariance matrix. In contrast, our work is based on Rademacher complexity (RC) without needing such probabilistic assumptions. For both theoretical and numerical reasons, it is more relevant to express RC with the L1- norm rather than with the L2-norm. We focus on the case of linear models and the problem of linear regression. Thanks to the ``linear probing'' method, our results can, however, be successfully applied to nonlinear neural networks, as illustrated in the classification MNIST example.

---


### 94. [Beauty is in the ELBO of the Beholder: A Variational Account of Processing Fluency in Face Perception](https://arxiv.org/abs/2608.24219)

**<font color=#1a73e8>作者：</font>** Francisco M. López, Jochen Triesch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial attractiveness has been linked to statistical regularities such as symmetry and averageness, suggesting that beauty may depend on the ease with which a face is perceived. We empirically test this hypothesis by training variational autoencoders on four face datasets without attractiveness supervision and evaluating their representations on the 597 faces from the Chicago Face Database. Across models, human attractiveness ratings closely aligns with the direction defined by the VAE evidence lower bound (ELBO) in rate-distortion space. Independently learned latent spaces contain an attractiveness direction that transfers strongly across random initializations and training data. We also find that attractive faces are more prototypical in both shape and latent space. Our results connect classic accounts of aesthetics with learned generative models and provide empirical support for a variational interpretation of the processing fluency theory of aesthetic pleasure.

---


### 95. [Event-Based Motion Estimation via Oriented Distance Fields](https://arxiv.org/abs/2608.24223)

**<font color=#1a73e8>作者：</font>** Lei Sun, Yuqin Ma, Weilun Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based motion estimation is central to tasks that demand high temporal resolution and robustness to fast motion. Existing methods typically rely on iterative optimization or repeated hypothesis comparison, offsetting the sensor's low-latency advantage. We propose Oriented Distance Field Motion Estimation (ODF Motion Estimation), which replaces this optimization with a single averaging step over a precomputed field of event distance vectors, combined with an adaptive event-count selection strategy and a parameter-free trail filter. On public and self-collected datasets, ODF motion estimation reaches sub-pixel accuracy at the lowest latency among compared methods. We validate its generality on two downstream applications rather than treating them as separate contributions. First, the estimated trajectory is converted into a blur kernel and paired with a compact iterative-unfolding network, trained on simulated motion-estimation noise, for real-time non-blind image deblurring, attaining competitive or superior PSNR/SSIM with under 1M parameters. Second, the same precomputed field is repurposed for directional event filtering in a low-power asynchronous pupil and glint tracker, sustaining stable tracking for tens of seconds while lowering a near-eye module's power draw.

---


### 96. [Matched Excess-Outranker Regularization for Candidate-Set Interference in Continual Knowledge Graph Embedding](https://arxiv.org/abs/2608.24273)

**<font color=#1a73e8>作者：</font>** Hao Ren, Junbin Gao, Jiaojiao Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual knowledge graph embedding updates entity and relation representations as a graph grows. Existing methods primarily address catastrophic forgetting, but entity admission also changes the candidate universe of every compatible query. A historical answer can therefore lose rank even when its score and its ordering among old entities are preserved. We formalize this effect as candidate-set interference and introduce Matched Excess-Outranker Regularization (MEOR), a host-level objective that compares smooth answer-relative newcomer pressure with score-blind, structurally matched old references. Its one-sided penalty acts only when newcomer competition exceeds the matched reference, preserving the host learner's signal for legitimate new entities. Across eight paired runs on ENTITY-ComplEx, MEOR improves historical current-universe mean reciprocal rank (MRR) by 0.0057 over replay and reduces candidate-set interference by 0.0055, with one-sided 95% lower bounds of 0.0052 and 0.0051, respectively. It satisfies the preservation criteria for old-universe ranking and newcomer acquisition and improves historical current-universe MRR over persistent calibration, matched maximum regularizer (MMR), and unmatched old regularizer (UOR). Direct ablations support each component of its reference construction and aggregation. Adding MEOR also improves historical ranking in all ten reported FBInc-S and FBInc-L host and backbone settings, with every paired 95% confidence interval excluding zero. These results establish candidate admission as a distinct source of continual rank loss and show that it can be controlled without replacing the underlying embedding architecture or continual learner.

---


### 97. [Eating for a Sustainable Planet: Personalized Sustainable Diet Recommendation via Constraint-Aware Decision-Making Modeling](https://arxiv.org/abs/2608.24274)

**<font color=#1a73e8>作者：</font>** Ying Jin, Weiqing Min, Mingyu Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A sustainable diet represents a multi-dimensional synergy among four essential pillars: nutrition adequacy, economic affordability, cultural acceptability, and environmental respect. Despite the prevalence of population-level sustainability modeling, practical implementation relies on effective individual-level adoption. This transition is often hindered by inter-individual heterogeneity, posing a formidable challenge in aligning sustainable diet requirements with individual preferences. To address this issue, we propose a personalized sustainable diet recommendation model based on a constraint-aware decision-making mechanism, where sustainability is incorporated through learnable constraints rather than modeled as user preferences. To systematically evaluate the proposed approach, we construct a sustainable diet dataset named SusDiet with about 150k recipes, characterized by broad coverage of sustainability indicators. Experimental results on this dataset show that our method promotes more sustainable choices without compromising individual preference. This work establishes a framework for aligning individual dietary choices with planetary health, offering quantitative evidence to guide future sustainable diet interventions and policy-making for sustainable development.

---


### 98. [Example-based Robust Abnormality Detection with Minimal Annotations using Exemplar Med-DETR](https://arxiv.org/abs/2608.24281)

**<font color=#1a73e8>作者：</font>** Sheethal Bhat, Bogdan Georgescu, Awais Mansoor 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reducing annotation requirements remains a key challenge in developing robust medical object detectors. To address this, Vision-Language (VL) object detection methods leverage grounding text information to enable powerful zero-shot and few-shot object detectors in the natural image domain [1, 2, 3, 4]. However, transferring these methods to the medical domain is challenging due to the absence of comparable quality and quantity of the grounding data. Regardless, significant contextual and non-imaging information exists in medical images that remains underutilized. Few-shot learning (FSL) techniques partially address this limitation but struggle to general ize to unseen medical findings and require extensive retraining when new findings are introduced [5, 6]. To overcome these challenges, we extend our prior EM-DETR framework [7] and introduce a scalable FS detection approach designed for efficient abnormality detection in Chest X-Ray (CXR) images under minimal supervision. The proposed architecture incorporates exemplar-based feature generation and domain-aware contrastive optimization, enabling effective adaptation to novel disease findings without exhaustive retraining. Our method achieves near state-of-the-art (SOTA) detection performance using less than 10% of the annotated data, demonstrating its potential for practical, annotation-efficient clinical deployment across both proprietary and public CXR datasets.

---


### 99. [CARE: Camera-Residual Reserves for First Sightings in Adaptive LiDAR Sensing](https://arxiv.org/abs/2608.24282)

**<font color=#1a73e8>作者：</font>** Jiachen Gong, Yun Li, Ehsan Javanmardi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adaptive LiDAR scanning concentrates a limited sensing budget on regions of interest predicted from past object tracks, lowering data volume in autonomous driving while maintaining detection accuracy. However, existing scanning policies face three challenges. First, history-driven approaches depend on past tracks, so unseen objects are detected late or missed. Second, random or uniform sampling outside the predicted regions has no awareness of where new objects appear. Third, camera-guided alternatives spend budget on all camera detections, resampling objects already covered, costing recall in crowded scenes and range when budgets are scarce. This paper introduces the CAmera-REsidual reserve (CARE), a training-free allocation rule that reserves part of a fixed ray budget for the directions of current camera detections that the track forecasts cannot explain; the rest follows the base history policy, and unused reserve returns to a random floor. The paper makes three contributions. First, a leakage-free ray-budget evaluation on nuScenes (150 scenes, 4,148 events) measuring the first-sighting loss of history-driven scanning, with a strict-causal variant using the preceding keyframe. Second, CARE raises first-sighting recall by 5.2, 5.2, and 4.3 points at 10%, 20%, and 35% budgets over the history policy, with paired intervals excluding zero; the camera cue drives this gain, and the first-sighting versus overall trade-off is a budget-dependent Pareto choice. Third, a safety-bounded forgetting module that releases budget from receding or static tracks beyond a speed-dependent guard distance; at tight budgets, forgetting without the guard significantly harms near-field recall, so the guard is what keeps it safe. The pipeline runs end to end on a real vehicle and, in closed-loop simulation, detects an occluded pedestrian earlier and brakes more reliably than history-driven scanning.

---


### 100. [Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation](https://arxiv.org/abs/2608.24293)

**<font color=#1a73e8>作者：</font>** Yeonkyeong Lee, Hyunsung Go, Jongmin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models have emerged as a dominant framework for high-fidelity image and video synthesis, operating in compact latent spaces with variational autoencoders (VAEs) to enhance computational efficiency without compromising visual quality. However, conventional VAEs are suboptimal for video data as they employ fixed compression ratios that cannot adapt to the varying complexity of spatio-temporal content. We present KATok (Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation), a transformer-based VAE that incorporates an adaptive token selector which is jointly learned with latent tokens. By evaluating each token's content-richness as keep-or-drop probability, the token selector effectively discards uninformative tokens, naturally allowing data-dependent compression. Applying adaptive tokenization to diffusion models may cause spatial misalignment, as token dropping can disturb the original spatio-temporal structure. To alleviate this issue, we propose two position-prediction strategies: cascaded and joint generation, to ensure spatial consistency. We empirically show that our model achieves strong reconstruction and generation quality at a state-of-the-art compression ratio. Further analysis on video data reveals that this improvement is primarily achieved by reducing spatio-temporal redundancy and removing uninformative tokens, as supported by both quantitative and qualitative results.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-194](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
