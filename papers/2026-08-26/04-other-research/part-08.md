# 📦 其他研究 | 2026年08月26日

> 本类共 **361** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-361**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-361**

---

### 351. [Geometry-Driven Opti-Acoustic Co-Registration and View-Invariant Reflectivity Mapping for Side-Scan Sonar](https://arxiv.org/abs/2608.23479)

**<font color=#1a73e8>作者：</font>** Taqi Hamoda, Nuno Gracias  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Side-Scan Sonar (SSS) is a primary modality for large-scale underwater mapping, yet automated perception and cross-modal alignment are severely bottlenecked by acoustic complexities such as speckle noise, shadows, and extreme viewpoint dependencies. Traditional handcrafted descriptors and modern deep learning matchers fail to bridge the physical domain gap between optical and acoustic imagery without 3D geometric constraints. To overcome these limitations, we propose a novel geometry-driven framework for pixel-level opti-acoustic co-registration and view-invariant reflectivity mapping. Our method utilizes Structure-from-Motion (SfM) to reconstruct a dense 3D seafloor mesh, acting as a geometric anchor between the visual and acoustic domains. We introduce a First Bottom Return (FBR) extraction algorithm to dynamically correct non-linear altitude drift caused by uncalibrated SfM reconstruction. Furthermore, we apply an inverse Lambertian model and a dual-Gaussian weighting function to isolate the intrinsic seabed reflectivity, effectively neutralizing slant-range propagation loss and geometric view-dependence. By deterministically associating these isolated acoustic properties with optical pixels, our pipeline generates highly accurate, strictly co-registered multi-modal datasets. This automated, physics-guided approach eliminates the need for manual annotation and paves the way for advanced self-supervised learning in benthic habitat mapping.

---


### 352. [GeoWAM: Visual Geometry World Action Models for Autonomous Driving](https://arxiv.org/abs/2608.23486)

**<font color=#1a73e8>作者：</font>** Yiren Lu, Xin Ye, Jiaming Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving. Most existing WAMs learn scene dynamics in pixel space by combining a video-generation backbone for future-observation prediction with an action head for ego-trajectory prediction. Pixels, however, provide only an indirect representation of these dynamics: they entangle geometry and motion with appearance, texture, and illumination, forcing the model to infer three-dimensional transformations from two-dimensional observations. We argue that geometry, represented by point clouds, offers a more natural state space for driving because it explicitly captures spatial structure and the rigid and non-rigid transformations that govern scene evolution while directly aligning with the space in which driving actions are executed. Building on this insight, we introduce \textbf{GeoWAM}, a visual geometry world action model for autonomous driving. Rather than predicting future images, GeoWAM is pretrained to forecast future scene geometry, yielding representations that jointly encode spatial structure and temporal evolution. A geometry-conditioned action head then leverages these learned geometric dynamics to predict future ego trajectories. Extensive open-loop and closed-loop evaluations show that visual geometry world modeling yields substantially stronger driving policies than image-based alternatives, establishing future-geometry prediction as an effective pretraining objective for autonomous driving.

---


### 353. [SVD-Based Typicality Maps for Out-of-Distribution Detection in Vision Transformers](https://arxiv.org/abs/2608.23499)

**<font color=#1a73e8>作者：</font>** Aldo Sean Sartor, Leandro de Souza Rosa, Andriy Enttsel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a method for analyzing the internal representations of Vision Transformers (ViTs) exploiting the geometry of their learned parameters. Each affine layer's weight matrix is factored via Singular Value Decomposition (SVD), and activations are projected onto the leading right singular vectors to obtain compact, layer-intrinsic representations. A class-conditional density model is then fitted at each layer, producing per-class \emph{typicality scores} that are stacked across depth into \emph{typicality maps}: two-dimensional summaries of how class-specific evidence evolves through the network. From these maps, we derive two post-hoc scores for Out-Of-Distribution (OOD) detection: a \emph{Prototype Alignment Score} (PAS), measuring agreement with class reference prototype patterns, and a \emph{Multi-Layer Soft Voting} (MLSV) score, capturing cross-layer consensus without stored prototypes. On ViT-B/16 fine-tuned on CIFAR-100, the proposed scores achieve competitive detection performance without retraining or OOD exposure.

---


### 354. [EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards](https://arxiv.org/abs/2608.23525)

**<font color=#1a73e8>作者：</font>** Zhiqing Cui, Xinxiang Yin, Yihong Tang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Earth-system analysis reconstructs changing physical processes from observations that differ in source, scale, timing, and modality. Natural hazards make this work consequential because incomplete evidence can change estimates of severity, exposure, and mechanism. We introduce EarthVerse, a benchmark that evaluates scientific agents through package-scoped investigations. Its 405 reproducible tasks are grounded in 199 documented events and 19 hazard families. Agents inspect heterogeneous event packages, choose compatible evidence, execute transparent calculations, reconcile source differences, and preserve provenance in the final answer. We provide executable ground truth that decomposes each task into fine-grained answer units, together with task-specific rubrics that assess the supporting research process while allowing multiple valid paths. We evaluate 25 model and agent systems under a controlled tool-using protocol, then use controlled studies to locate failures in evidence access, tool selection, memory, reasoning, interaction, and scientific execution. Across systems, the best mean answer-unit accuracy is 84.65%, while the highest Strict@95 is only 34.81%. The gap shows that current agents often complete individual steps without maintaining a consistent chain across evidence, scales, units, calculations, and physical interpretation. EarthVerse provides a reproducible basis for measuring end-to-end scientific reliability in dynamic Earth systems.

---


### 355. [Correcting a learned physical invariant improves world-model rollouts](https://arxiv.org/abs/2608.23526)

**<font color=#1a73e8>作者：</font>** Richard Bao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models can predict video without learning dynamics that they reliably preserve. We test whether a frozen DreamerV3 trained only on pendulum video learns a scalar that its own latent transition treats as approximately conserved. A label-free search recovers the same energy-like invariant across independently trained conservative models, while the same procedure finds no comparable invariant in matched damped models. During autonomous rollouts, this quantity drifts. Projecting the latent state back toward its initial level set reduces rollout error in all three conservative models, whereas matched random constraints usually increase it. These results distinguish a dynamically meaningful invariant from a merely decodable correlate and reveal a concrete failure mode: a world model can learn a physical constraint from pixels yet violate that constraint when it imagines forward.

---


### 356. [Predicting Multiple Clinical Outcomes Related to Functional Recovery and Social Isolation Among Older Adults After Lower-Limb Fracture or Hip Replacement](https://arxiv.org/abs/2608.23531)

**<font color=#1a73e8>作者：</font>** Santosh Ray, Pratik K. Mishra, Ali Abedi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Older adults recovering after lower-limb fracture or hip replacement may experience complex recovery trajectories. Most of the time, these clinical aspects are studied in isolation, masking their joint impact on recovery. This study used the MAISON-LLF dataset, which contains multimodal sensor and clinical assessment data from 18 older adults recovering in the community after lower-limb fracture or hip replacement. Participants were monitored for up to eight weeks, corresponding to a maximum of 1,008 participant-days of sensor monitoring. Forty-six daily features were extracted from indoor motion, acceleration, step count, heart rate, out-of-home mobility, and sleep data. Five clinical outcomes were assessed every two weeks: the Social Isolation Scale, Oxford Hip Score, Oxford Knee Score, Timed Up and Go test, and 30-second Chair Stand test. We utilize an inherent relationship between multi-modal sensor data and different clinical scores and formulate it as a multi-output regression problem. We tested various machine learning and deep learning single- and multi-output regression algorithms to predict these scores simultaneously. The results showed that predicting clinical scores jointly was better than separately. The tabular DL multi-output regressor, NODE, gave a remarkable performance of MSE=3.96 and MAE=1.02 in comparison to other multi- and single-output regressors. The SHAP feature analysis further showed the importance of including multimodal sensors to provide a good estimate of patients' recovery trajectory. This work may support the simultaneous assessment of functional recovery and social engagement among community-dwelling older adults and ultimately help improve their care and quality of life.

---


### 357. [Adapter-Based Few-Shot Continual Learning for Malicious Packet Recognition](https://arxiv.org/abs/2608.23536)

**<font color=#1a73e8>作者：</font>** Kyle Stein, Guillermo Francia, III Eman El-Sheikh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The continual evolution of malware variants necessitates detection systems that can adapt to new threats without retraining from scratch. However, continually updating models on new data often leads to catastrophic forgetting, where previously learned knowledge is overwritten. While continual learning has been increasingly explored for malware detection, the specific setting of Few-Shot Class-Incremental Learning (FSCIL), where new malware classes must be learned from only a small number of labeled examples, remains comparatively underexplored. Therefore, this work investigates the FSCIL setting for malware classification. To address the stability-plasticity dilemma, we propose a hybrid framework that leverages a Self-Supervised Learning (SSL) backbone initialized through domain-specific pre-training on malware packets. Our method incorporates Low-Rank Adaptation (LoRA) to efficiently adapt the model during the base session while freezing the core backbone to preserve previously learned representations, alongside a prototype-based classification head for incremental sessions to establish robust decision boundaries from limited samples. Extensive experiments across several datasets demonstrate that our approach consistently outperforms prior malware FSCIL baselines and achieves state-of-the-art performance.

---


### 358. [How AI Assistance Affects Human Skill Development: A Study of Learning with Logic Puzzles](https://arxiv.org/abs/2608.23543)

**<font color=#1a73e8>作者：</font>** Shang Wu, Catarina G Belem, Shuyuan Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While AI assistance can improve human task performance in the short term, it may also undermine the development of skills in the longer term. We examine this tension in a controlled logic-puzzle experiment involving on-demand AI assistance, where participants complete tasks before, during, and after AI is available. By experimentally varying AI request costs, we find that lower-cost assistance induces more frequent AI use. We also find that participants who request AI assistance during the AI-access phase perform worse at the task after assistance is removed, and their subsequent unassisted performance is overestimated when predicted from earlier AI-assisted performance. We use a Bayesian latent ability model to separate initial ability, post-AI ability, and participant-specific skill change, while estimating how independent reasoning during the AI-access phase relates to skill development. The results show that greater independent problem-solving effort is associated with larger gains in latent ability, consistent with the interpretation that skill development is weaker when AI assistance substitutes for independent reasoning.

---


### 359. [Robustness of Anomaly Detection Models for Industrial Control Systems under Training-Time Data Contamination](https://arxiv.org/abs/2608.23547)

**<font color=#1a73e8>作者：</font>** Mustafa Umut Ozbek, Taiwo Ojo, Pooria Madani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine-learning-based anomaly detection is increasingly used in industrial control systems (ICS), yet most studies assume that detector training data is trustworthy. In practice, training data may be corrupted through compromised logs, labeling errors, manipulated historian records, or unsafe retraining processes. This paper evaluates the robustness of offline ICS anomaly-detection pipelines on the Secure Water Treatment (SWaT) benchmark under training-time contamination. We assess 11 heterogeneous anomaly detectors under three contamination strategies: random injection, similarity-targeted injection, and feature-noise injection. The first two insert attack samples into the nominal training pool, while the third adds bounded Gaussian noise to selected normal training samples. These attacks are contamination-based rather than gradient-driven poisoning methods. Contamination budgets from 1% to 10% are evaluated using clean validation and test sets under a unified offline protocol. The results show that robustness is strongly model-dependent and cannot be predicted from clean-data performance alone. Injection-based contamination causes the greatest degradation, particularly for local-density and distance-based detectors, whereas feature-noise contamination has a comparatively limited effect. PCA, SVM, HBOS, and IForest remain relatively stable, while the tuned neural detectors demonstrate intermediate robustness. Overall, the findings highlight the importance of training-data integrity in ML-enabled ICS monitoring, subject to the evaluated dataset, models, and threat assumptions.

---


### 360. [FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors](https://arxiv.org/abs/2608.23549)

**<font color=#1a73e8>作者：</font>** Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rendering views using 3D scene representations such as Gaussian Splatting (3DGS), Neural Radiance Fields (NeRF), meshes, or even point clouds produces artifacts when input views are sparse or target views lie far from the input. Recent work mitigates these artifacts using diffusion-based generative priors, but is specialized to individual representations and require custom architectures or extensive retraining. We present FixAnything, a single model for fixing a wide range of rendering artifacts. It does so by repurposing a pretrained video generative model, leveraging its implicit multi-view priors with only minimal modification and lightweight finetuning. Our key insight is that even noisily-rendered sequences preserve camera motion and coarse scene structure, allowing cleanup to be formulated as video-to-video translation. To control what scene structure should be preserved, we introduce a binary mask denoting the clean pixels, enabling the model to anchor its output to high-quality inputs (e.g. training views) while refining the rest. To encourage FixAnything to produce 3D-consistent renderings that support downstream reconstruction, we use camera pose accuracy (recovered via structure-from-motion) as a reward signal for direct preference optimization (DPO). Across four distinct 3D representations, FixAnything consistently improves rendering quality with lightweight finetuning, demonstrating that a single generalist video prior can replace multiple specialist refinement pipelines. The simplicity of the framework enables immediate adoption of stronger future video models without architectural redesign.

---


### 361. [Provably adaptive sampling with uniform and remasking discrete diffusion models](https://arxiv.org/abs/2608.23554)

**<font color=#1a73e8>作者：</font>** Daniil Dmitriev, Zhihan Huang, Yuting Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models offer a promising alternative to autoregressive generation by enabling parallel updates, but their sampling efficiency can depend strongly on the choice of the forward process and the sampler. For the uniform forward process, existing lower bounds for the standard $\tau$-leaping sampler scale linearly with the ambient dimension $d$, raising the question of whether this dependence is intrinsic to the forward process. We answer this question in the negative. We consider a first-order sampler based on the leave-one-out denoiser for uniform and remasking processes whose coordinate updates can be performed in parallel. In both cases, the sampler can correct denoising mistakes during the sampling process, which becomes necessary when many coordinates are updated together. Our main result establishes an adaptive sampling guarantee: up to logarithmic factors, $N = O(\mathrm{DTC}(X_0) / \varepsilon)$ discretization steps suffice to achieve sampling error $O(\varepsilon_{\mathrm{score}}+\varepsilon)$, where $\varepsilon_{\mathrm{score}}$ is the error in score estimation. Thus, the sampling complexity is governed by the intrinsic dependence structure of the target distribution, as measured by its dual total correlation $\mathrm{DTC}(X_0)$, rather than directly by the ambient dimension $d$. Our analysis proceeds through a Bayes-optimal auxiliary sampler that separates discretization error from score-estimation error. We also derive an exact information-theoretic representation of the discretization error in terms of the mutual information between different coordinates of the forward process at different times. This representation applies to general forward processes and, in the uniform and remasking cases, can be controlled by $\mathrm{DTC}(X_0)$. Numerical experiments on structured synthetic distributions illustrate the predicted dimension-adaptive behavior.

---


> [!TIP]
> 当前位于：**351-361**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-361**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
