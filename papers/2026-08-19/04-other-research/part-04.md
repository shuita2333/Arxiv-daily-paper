# 📦 其他研究 | 2026年08月19日

> 本类共 **435** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

---

### 151. [External Sinkhole Attack Detection in Large-Scale WSNs Using Metaheuristic Feature Selection](https://arxiv.org/abs/2608.15274)

**<font color=#1a73e8>作者：</font>** Seungwoo Han, Sawako Kitagata, Ingon Chanpornpakdi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sinkhole attacks in large-scale wireless sensor networks (WSNs) pose a serious threat to network functionality. This paper presents a metaheuristic feature selection for sinkhole attack detection using the bee swarm optimization (BSO) algorithm. In an external sinkhole attack simulation with 2000 nodes deployed over a 3000 $\times$ 3000 m$^2$ field, the proposed method achieves a detection accuracy of 0.997 while reducing the 16-feature set to eight features.

---


### 152. [Balancing Privacy and Compliance in DeFi: A Zero-Knowledge-Based Auditable Cross-Chain Framework](https://arxiv.org/abs/2608.15276)

**<font color=#1a73e8>作者：</font>** Huiheng Li, Kainuo Feng, Jiahao Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rise of decentralized finance (DeFi), cross-chain transactions, transfers of assets across different blockchain networks, face a fundamental conflict between user privacy and regulatory compliance. Unlike single-chain systems, cross-chain environments must balance privacy and auditability across heterogeneous architectures. Existing solutions, from transparent ledgers to anonymous cryptocurrencies, fail to reconcile these two requirements, hindering regulatory adoption. This research proposes an auditable cross-chain framework that integrates three building blocks. First, zero-knowledge proofs (ZKPs) verify transaction compliance (e.g., amount non-negativity, signature validity) without revealing transaction details. Second, a light-client mechanism enables trust-minimized cross-chain verification without relying on third-party relayers. Third, a threshold view-key mechanism based on distributed key generation (DKG) ensures that audit access is granted only to authorized entities under legal triggers such as the FATF Travel Rule and MiCA Regulation. For cross-border investigations, the framework adheres to national laws and the EU Directive on Mutual Legal Assistance. This work systematically combines ZKPs, threshold cryptography, and light-client verification into an auditable, privacy-preserving cross-chain protocol. It contributes to Regulatory Technology (RegTech) and provides a viable path toward compliant, interoperable decentralized finance.

---


### 153. [Memory-Bounded Continuation of Greedy Sampling for Continual Anomaly Detection](https://arxiv.org/abs/2608.15277)

**<font color=#1a73e8>作者：</font>** Yoon Gyo Jung, Jaewoo Park, Kuan-Chuan Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Greedy sampling produces a compact yet representative summary of normal data, which is essential for reliable anomaly detection that relies on measuring distance from normality. For continual anomaly detection where tasks arrive sequentially, extending greedy sampling is straightforward with unbounded memory through coreset accumulation. However, practical deployment requires fixed memory where the coreset size remains constant regardless of task count. We observe that continued greedy sampling, which iteratively applies greedy selection over previously greedy-sampled sets, effectively preserves representativeness under strict memory limits. Despite discarding data at each step to satisfy the memory constraint, coreset quality degrades gracefully rather than catastrophically, enabling reliable anomaly detection across the tasks. We provide theoretical justification by showing that resulting greedy-continued coreset approximates the oracle coreset within a bounded gap. We instantiate this principle in ContCore, which constructs a greedy-continued coreset through greedy expansion on new task features followed by greedy consolidation to enforce the memory budget. Unlike neural methods susceptible to catastrophic forgetting or naive coreset accumulation requiring unbounded memory, ContCore maintains fixed memory with theoretical guarantees. Empirically, ContCore achieves state-of-the-art performance across 11 task schedules on MVTecAD and VisA, and extends effectively to online continual AD settings where prior methods degrade significantly. Code: this https URL

---


### 154. [Geometry-Aware Spatio-Temporal Context Modeling for 4D Occupancy Forecasting](https://arxiv.org/abs/2608.15279)

**<font color=#1a73e8>作者：</font>** Sitao Chen, Zhuangwei Zhuang, Hui Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D occupancy forecasting models the spatio-temporal evolution of 3D scenes and is crucial for autonomous driving, especially for corner-case simulation. Existing methods often rely on discrete tokenization followed by autoregressive prediction, yet struggle with geometric distortion in static structures and inconsistent temporal coherence over the forecasting horizon. In this work, we propose a Geometry-Aware Spatio-Temporal context modeling method (GAST) for 4D occupancy forecasting, built upon progressive explicit-implicit generation and dual-path spatio-temporal modeling. Specifically, the generation module produces per-frame occupancy with high geometric fidelity and semantic plausibility through pose-driven warping, motion-aware feature modulation, and attention-based feature refinement. Subsequently, the spatio-temporal module enhances spatial consistency through global context aggregation while capturing scene evolution through temporal dynamics extraction. This unified design enables joint optimization of historical reconstruction and future forecasting in an end-to-end manner. Extensive experiments on Occ3D-nuScenes demonstrate the superiority of our method, outperforming the state-of-the-art by 7.67% in mIoU and 6.44% in IoU with a 2.84x speedup, while maintaining strong performance in long-term forecasting.

---


### 155. [$D^{2}R^{2}$: Discrete Diffusion with Regulation Reinforcement for Single-Cell Perturbation Prediction](https://arxiv.org/abs/2608.15288)

**<font color=#1a73e8>作者：</font>** Ninghan Fan, Qi Liu, Xunuo Zhu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting single-cell transcriptomic responses to genetic perturbations is central to functional genomics and virtual-cell modeling. Existing approaches, however, typically predict an entire expression profile as a whole, leaving the order in which individual gene responses are generated unmodeled. To address this problem, we introduce \textbf{$D^{2}R^{2}$} (\textbf{D}iscrete \textbf{D}iffusion with \textbf{R}egulation \textbf{R}einforcement), which reformulates perturbation prediction as regulation-guided gene-wise progressive generation. A Masked Discrete Diffusion Model represents expression as ordinal tokens and reconstructs a fully masked profile step by step, allowing generated gene responses to condition those that remain masked. A Regulatory Policy Module initializes the generation policy from a gene regulatory network inferred from control cells and adapts it to the perturbation and current partially generated state. Then, group-relative policy optimization refines only the ordering policy using final perturbation-effect agreement as reward. Across Norman19 and VCC-H1, $D^{2}R^{2}$ achieves the best performance on all five metrics on Norman19 and remains competitive on H1. Controlled ablations holding the generator and generation budget fixed show that biological-prior ordering improves over random ordering and is more reliable than uncertainty-based heuristics, whereas reversing the biological-prior ordering degrades every metric. Biological analyses further show that the refined policy prioritizes regulatory genes early while promoting perturbation-specific transcription factors and responsive genes. These results establish gene generation order as an effective, controllable, and biologically interpretable dimension of single-cell perturbation prediction.

---


### 156. [ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning](https://arxiv.org/abs/2608.15291)

**<font color=#1a73e8>作者：</font>** Ziyue Yang, Chaolin Xu, Yijing Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Demand forecasting increasingly requires combining two complementary sources of information: historical sales reveal recurring numerical dynamics, while future promotions, holidays, price changes, and platform interventions provide forward-looking knowledge. Existing text-enhanced forecasting methods often encode such context into generic representations and fuse it uniformly with time-series features, without explicitly distinguishing which semantic effects are forecast-relevant or how they should modify future dynamics.
We introduce ReasonCast, a structured semantic intervention framework that translates event knowledge into forecast-specific operations. An agent examines the event context, the no-text forecast, and its uncertainty to determine whether textual reasoning is needed. Rather than injecting free-form text, ReasonCast represents event knowledge through structured fields describing event relevance, demand direction, temporal shape, amplitude, and peak intensity. These fields interact selectively with temporal components of a time-series foundation model. An additive path corrects local trends and temporal shapes, while a multiplicative path captures event-driven level shifts.
ReasonCast introduces a forecast-grounded post-training curriculum. Schema SFT establishes semantic fields; semantic-field RL calibrates direction, shape, amplitude, and peak judgments; and forecast-utility RL evaluates semantic interventions through a frozen forecaster, aligning reasoning outputs with marginal forecast improvement. ReasonCast lowers WMAPE by 3.29, 1.25, and 0.47 percentage points on holiday-sensitive categories, mega-sale-sensitive categories, and M5 event windows, respectively. On stable-sales periods, indiscriminate semantic intervention increases WMAPE by 1.68 percentage points, whereas suppressing unnecessary intervention preserves the numerical backbone.

---


### 157. [SOS! : A Streamlined Object-Conditional Transformer for Model-free Segmentation](https://arxiv.org/abs/2608.15295)

**<font color=#1a73e8>作者：</font>** Jiaqi Hu, Junwen Huang, Hongli Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation segmentation models excel at generating high-quality, class-agnostic masks, but they struggle to associate these proposals with specific target objects. This semantic gap severely hinders their deployment in downstream applications like robotic manipulation, which demand precise unseen objects segmentation. Existing approaches attempt to resolve this by relying on exhaustive 3D object model priors, inherently introducing prohibitive computational overhead and complex, multi-stage pipelines. To address these limitations, we propose SOS (Streamlined Object-conditional Transformer for model-free Segmentation). SOS completely eliminates the reliance on 3D models, requiring only a single reference image per target object. Central to our framework is a novel Object-Conditional Transformer that learns identity-anchored queries, unifying mask generation and target identification into a single feed-forward pass. This streamlined design drastically improves both structural and computational efficiency. Extensive evaluations across multiple benchmarks demonstrate that SOS establishes a new state-of-the-art for model-free unseen objects segmentation, delivering accurate and high-efficiency performance. The project page and code are available at this https URL.

---


### 158. [FMReward: Aligning and Evaluating Audio-Driven 3D Facial Animation with Human Preferences](https://arxiv.org/abs/2608.15296)

**<font color=#1a73e8>作者：</font>** Sijing Wu, Yunhao Li, Zhilin Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-driven 3D facial animation is essential for advancing immersion and interactivity in virtual experiences. Although recent advances have shown promising capabilities, the training and evaluation of existing methods typically rely on ground-truth-based errors, which fall short of aligning with human preferences. To address this, we present a comprehensive framework that learns an automatic perceptual model from human preference data and leverages it to improve and evaluate the perceptual quality of audio-driven 3D facial animation. To begin with, we construct FMPair (Facial Motion Pairwise preference), the first human preference dataset for audio-driven 3D facial animation, which is built through a systematic annotation pipeline and comprises 65,574 annotated 3D facial motion pairs from 8,834 distinct in-the-wild audio clips. Based on the pairwise comparison dataset, we propose a Facial Motion Reward model, termed FMReward, which takes audio and 3D facial motion as inputs and predicts a perceptual quality score aligned with human preferences. Building upon FMReward, we further introduce Facial Motion reward Feedback Learning (FMFL), a direct fine-tuning algorithm that leverages a pretrained reward model to optimize diffusion-based audio-driven 3D facial animation models for better alignment with human preferences. Extensive experiments demonstrate the superiority of FMReward over other metrics in aligning with human preferences and the effectiveness of FMFL in improving the perceptual quality of audio-driven 3D facial animation.

---


### 159. [TinyDETR-Pose: Towards End-to-End Real-Time Single-Stage 6DoF Object Pose Estimation with Lightweight Transformers](https://arxiv.org/abs/2608.15297)

**<font color=#1a73e8>作者：</font>** Paul Julius Kühn, Duc Anh Nguyen, Saptarshi Neil Sinha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time 6DoF object pose estimation on resource-constrained hardware remains challenging, as accurate correspondence-based and refinement pipelines typically rely on non-differentiable PnP/RANSAC stages or costly iterative refinement, while recent foundation-model-based approaches incur inference costs that are prohibitive for edge deployment. We present TinyDETR-Pose, a lightweight, end-to-end, single-stage framework that jointly detects objects and regresses their full 6D pose in a single forward pass. Built on the efficient LW-DETR architecture, TinyDETR-Pose formulates detection and pose estimation as a set-prediction problem and attaches dedicated MLP heads for rotation, monocular depth, and projected object center regression to each decoder query, eliminating the need for PnP, NMS (non-maximum suppression), or iterative pose refinement. Object symmetries are handled through a ADD-S loss applied uniformly to all objects, without the need for object-specific loss schedules or separate geodesic/ADD supervision. In addition, predictions are assigned to ground truth using a symmetry-safe Hungarian matcher based on class and 2D spatial cues, yielding stable assignment under symmetry and depth ambiguity. On YCB-V, TinyDETR-Pose achieves a comparable ADD-S AUC of 85.9, while requiring up to 72.7% fewer parameters than other DETR-based single-stage pose-estimation approaches. Due to its compact design, TinyDETR-Pose runs in real time and achieves an inference latency of only ~4.5 ms per frame on an NVIDIA Jetson Nano using TensorRT, demonstrating that accurate end-to-end transformer-based 6D pose estimation can be made practical for edge deployment.

---


### 160. [Image Denoising via the Adaptive Rank-Cluster Filter](https://arxiv.org/abs/2608.15298)

**<font color=#1a73e8>作者：</font>** Dmitry Pozdnyakov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A spatial-local image-denoising filter is proposed, and its performance metrics are evaluated in comparison with baseline filtering algorithms, including the median, adaptive median, Gaussian, bilateral, Wiener, anisotropic diffusion, and non-local means. The developed filter is based on aligning the intensity value of the central pixel in a 3x3 window with the statistical majority intensity of one of the two clusters formed by optimal Otsu's partitioning of a pixel set sorted by intensity and trimmed to seven elements. This is followed by a fuzzy fusion of the calculated value with the median intensity of the pixels within the window. The proposed filter demonstrates the highest robustness to variations in image noise levels, particularly when processing mixed noise consisting of salt-and-pepper impulse noise and additive Gaussian noise in various proportions

---


### 161. [Resize, Remix, Regen: Frankensteining IoT Design Methods](https://arxiv.org/abs/2608.15301)

**<font color=#1a73e8>作者：</font>** Albrecht Kurze  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> There are numerous IoT design methods. Previous research shows that all of them have their strengths, but also their limitations. None of them is a universal, all-purpose method. However, experts often view these methods as more versatile than their creators intended. Therefore, analyzing existing methods and tools, as well as rearranging and combining their approaches and components - just as Frankenstein did with his creature - offers the possibility of new creations that may be better than any single method previously. We present the idea and concept of "Frankensteining", which is based on the repeated application of IoT design methods in various contexts. We present a practical Frankensteining creation that was used in a workshop, our own methods, and a serial Frankensteining approach that was tested in an educational context. We conclude with a discussion on Frankensteining and invite other experts and practitioners to share their perspectives and experiences.

---


### 162. [Vibes on Demand: Adding Vibrotactile Encoding to Line Charts Shows Experiential Benefits Without Performance Costs](https://arxiv.org/abs/2608.15307)

**<font color=#1a73e8>作者：</font>** Anchit Mishra, Oliver Schneider, Matthew Brehmer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Details on demand is a common design pattern in visualization design, especially useful when interacting with visually-saturated or small displays. Beyond visualization, another common approach for saturated displays is to incorporate other modalities, such as haptic feedback. While haptic rendering in visualization has primarily targeted accessibility needs, with haptics as a substitute for visual feedback, studies using haptics outside of a visualization context have shown value in experiential factors, such as increased confidence in ambiguous contexts and higher engagement. We explore vibrotactile feedback as a reinforcing information channel for communicating trends in details-on-demand tooltips on touchscreens. We identify preferred parameter configurations for our haptic encoding, informed by a study where participants identified parameter configurations that they perceived to most accurately reflect the dynamics of line charts appearing in tooltips. In a second study, we evaluated participant performance in a pairwise comparison task, finding that incorporating vibrotactile encoding improves involvement without affecting accuracy. We discuss the implications of these findings for future visualization design, and propose directions for applications and future studies.

---


### 163. [Physiological World Models for Human State Transitions](https://arxiv.org/abs/2608.15309)

**<font color=#1a73e8>作者：</font>** Chongyang Zhang, Rendong Wang, Hao Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous multimodal sensing now allows human physiology to be observed throughout daily life rather than only during occasional clinical visits. However, most health artificial intelligence systems are designed to recognize current states, estimate risks or analyse individual biomarkers. They do not directly model how physiological states change in response to real-world events, behaviours, contexts and interventions. Here we propose the Physiological World Model (PWM), an event-conditioned framework for learning these changes at the level of the whole person. We introduce the HumanState Transition Token, a structured, quality-scored unit that connects the physiological state before an event with the event or action, relevant context and intervention information, the physiological trajectory after the event, observed outcomes and data quality. We describe four capability levels, from state representation to bounded intervention planning, together with four data acquisition and validation protocols. We also propose six benchmark tasks covering HumanState representation, forecasting across multiple timescales, individualized response prediction, simulation of alternative interventions, bounded planning and reliability under distribution shift. Together, this framework provides a practical path towards personalized health management, behavioural intervention design and clinician-supervised decision support, while clearly separating prediction from causal inference and making uncertainty, safety, governance and limits of use explicit.

---


### 164. [FedADB: Class Anchor-Driven Dual-Branch Federated Learning for Mitigating Forgetting](https://arxiv.org/abs/2608.15310)

**<font color=#1a73e8>作者：</font>** Zhenyan Liu, Hua Zhang, Haoran Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal data collected by heterogeneous devices are used for collaborative training, where federated learning (FL) serves as a key paradigm for effective distributed modeling with data privacy preservation. However, local training suffers from the forgetting of previously learned global knowledge under cross-client data heterogeneity, which leads to significant declines in both performance and convergence speed. Most previous studies rely on global alignment strategies to retain global knowledge, which hinder local optimization and lead to inadequate supervision of missing classes. Some studies introduce proxy datasets to supplement supervision for missing classes. However, it remains a challenge to balance class-wise global consistency and local optimization objectives without proxy datasets. In this work, we propose FedADB, a Class Anchor-Driven Dual-Branch FL framework. Specifically, the server generates class anchors optimized in a differentiable input space, which are shared across clients. These class anchors serve as global references that provide supervision for missing classes during local training. A dual-branch collaborative training mechanism is designed for clients. In this mechanism, the anchor-based global branch focuses on learning with global consistency, achieving global knowledge alignment by class-anchor balanced sampling. The local calibration branch focuses on learning discriminative local features, mitigating the degradation of local representations caused by excessive global alignment. Extensive experiments across multiple medical and natural datasets demonstrate that FedADB achieves significant improvements in both accuracy and convergence speed.

---


### 165. [Shape Operator PCA: Curvature-Aware Projections for Geometric Machine Learning](https://arxiv.org/abs/2608.15313)

**<font color=#1a73e8>作者：</font>** Alexandre L. M. Levada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose SHOPCA (Shape Operator-based Principal Component Analysis), a novel method for unsupervised metric learning and dimensionality reduction that incorporates differential geometric information into the covariance structure of classical PCA. SHOPCA regularizes the global covariance matrix using the mean shape operator, defined as the average of the absolute local shape operators estimated from the data manifold, steering principal components toward directions of both maximum variance and informative curvature. A single trace-normalized mixing coefficient $\alpha$ controls the regularization, recovering standard PCA at $\alpha = 0$ and a curvature-driven embedding as $\alpha \to \infty$. We further introduce a fully unsupervised criterion for selecting $\alpha$ based on the spectral eigengap of the regularized covariance matrix, maximizing the relative separation between the top-$d$ and remaining eigenvalues without using class labels. We evaluate SHOPCA on more than 50 real-world benchmark datasets, comparing it with PCA, ISOMAP, and UMAP using Adjusted Rand Index (ARI), Normalized Mutual Information (NMI), Fowlkes-Mallows index (FM), and V-measure. Results show that SHOPCA consistently improves clustering quality over PCA across a broad range of datasets and surpasses UMAP on small-sample settings, where iterative neighborhood-based manifold estimation can degrade. SHOPCA is computationally tractable, parameter-efficient, and applicable to domains requiring fully unsupervised, geometry-aware dimensionality reduction.

---


### 166. [Physics-informed VAE-EVT for Tail Aware Radio Map Prediction](https://arxiv.org/abs/2608.15314)

**<font color=#1a73e8>作者：</font>** Amanda Sheron Gamage, Niloofar Mehrnia, James Gross  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ultra-reliable low-latency communication (URLLC) requires precise identification of spatial regions where the signal-to-noise ratio (SNR) falls below an outage threshold. In this context, an outage refers to instances in which SNR falls below a specified threshold, which, for URLLC, can be as stringent as the 0.1% quantile of the SNR distribution. Traditional generative radio map models tend to focus on reconstructing average signal levels, often overlooking the low SNR that is crucial for accurate outage prediction. To address this limitation, we introduce a physics- and tail-informed VAE-EVT (variational autoencoder-extreme value theory) framework that distinctly models both the bulk and tail distribution of SNR. Our approach begins with a physics-informed preprocessing stage that extracts deterministic features, including line-of-sight, shadowing, and distance, from the scene geometry. A dual-latent encoder then captures the bulk SNR using a Gaussian mixture and the tail using a generalized Pareto distribution (GPD). By employing a modified variational objective, the model is trained to jointly supervise both regimes, ensuring focused attention on extreme fading events. Evaluated on the RadioMapSeer dataset, our method achieves an SNR RMSE of 4.83 dB in the outage region defined by the low threshold of 0.1% SNR quantile. This significantly outperforms the state-of-the-art GAN-based model, which records an SNR RMSE of 21.90 dB, with the performance gap widening as the outage threshold becomes more stringent.

---


### 167. [LightLoc++: Sensor-Robust Representation Learning for Efficient Outdoor LiDAR Localization](https://arxiv.org/abs/2608.15317)

**<font color=#1a73e8>作者：</font>** Wen Li, Shangshu Yu, Dunqiang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene coordinate regression (SCR) achieves strong performance in outdoor LiDAR localization, but it usually requires scene-specific training that can take days, limiting practical deployment. Recent works improve training efficiency by decoupling SCR into a scene-agnostic backbone and scene-specific prediction heads, where the backbone is pretrained on source datasets and frozen for new scenes, and only lightweight heads are optimized. However, we find that this paradigm heavily depends on the pretrained backbone. Existing decoupled methods can match conventional SCR methods fully optimized for each new scene when LiDAR configurations are similar to those used during backbone pretraining, but their accuracy drops noticeably on datasets collected with different LiDAR sensors. This suggests that efficient LiDAR localization requires representations that capture stable scene geometry across LiDAR configurations. Motivated by this observation, we propose LightLoc++, a sensor-robust and efficient outdoor LiDAR localization framework. To support sensor-robust representation learning, we introduce SULID, a synchronized urban multi-LiDAR dataset with representative 32-, 64-, and 128-beam rotating LiDARs, extensive cross-sensor overlap, and diverse urban scenes. Using SULID, we pretrain a sensor-robust backbone through cross-sensor consistency learning. LightLoc++ further preserves efficient new-scene learning by incorporating sample classification guidance and redundant sample downsampling, which reduce regression ambiguity and computational redundancy in large-scale outdoor scenes. Extensive experiments on multiple outdoor LiDAR localization benchmarks demonstrate that LightLoc++ achieves state-of-the-art localization performance with the lowest new-scene training cost among compared methods. Code and dataset will be made available at this https URL.

---


### 168. [Logical Embeddings for Argument Analysis](https://arxiv.org/abs/2608.15325)

**<font color=#1a73e8>作者：</font>** Leander Heldring, Santiago Torres  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a new framework for machine-learning-oriented argument analysis tasks. Our proposal involves replacing traditional contextualized word embeddings used in most NLP tasks with logical embeddings, an alternative encoding that directly exploits argumentation structures. In essence, logical embeddings encapsulate the logical semantics of an argument, allowing for a better representation of its meaning. Supporting these embeddings is a mathematical logic-based similarity measure that offers a transparent notion of proximity and is guaranteed to satisfy several desirable theoretical properties that current cosine similarity-based contextualized word embeddings cannot assure. This similarity measure induces a positive semi-definite kernel on the set of arguments, enabling us to uniquely define logical embeddings using the theory of Reproducing Kernel Hilbert Spaces (RKHS). Moreover, we prove that this encoding is optimal, in the sense that no logical information is lost in the process. As with other RKHS applications, logical embeddings can be used in numerous supervised and unsupervised tasks. We provide an implementation of the method and aim to test it against literature benchmarks. Additionally, we demonstrate that logical embeddings outperform most standard embedding methods on a classification task.

---


### 169. [The Benchmark Trap: Structures of Power and Injustice in AI Evaluations](https://arxiv.org/abs/2608.15326)

**<font color=#1a73e8>作者：</font>** Jason Branford, Angelie Kraft  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) benchmarks are not neutral tools of evaluation but socio-technical artefacts that shape competition, power, and research priorities within AI. Benchmarks standardise the assessment of systems and facilitate the creation of leaderboards that reward state-of-the-art performance with prestige, citations, trust, and institutional influence. As the costs of developing competitive AI systems rise, these rewards increasingly concentrate among powerful, industry-funded labs. This paper situates these concerns within Iris Marion Young's theories of oppression and structural injustice. It argues that current benchmarking practices may perpetuate systematic harms affecting various actors in AI research, aligning with four of Young's "faces of oppression". Benchmarking culture is further framed as a source of structural injustice, as these harms emerge from normalised, individually defensible practices and network effects, even without explicit wrongdoing. By reinforcing existing power structures and narrowing possible research trajectories, benchmarking may in fact prevent the field from advancing in epistemically robust and socially beneficial ways.

---


### 170. [A concentration result for multilayer feedforward neural networks](https://arxiv.org/abs/2608.15335)

**<font color=#1a73e8>作者：</font>** Vera Koponen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We consider for an arbitrary fixed $\rho$ and for each positive integer $n$ a multilayer feedforward artificial neural network with $\rho$ layers, $n$ neurons in the first layer (the input layer) and only one neuron, the output neuron, in the last layer. Very roughly formulated, the main result is that if the distribution of weights of connections from a layer to the next are, for all large $n$, approximated well by a fixed continuous (but otherwise arbitrary) curve which does not depend on $n$, and if the values of the $n$ input neurons are independently and identically distributed with a continuous probability density function, then there is a number $\psi$ such that for all $\varepsilon > 0$ the probability that the value of the output neuron is in $[\psi - \varepsilon, \psi + \varepsilon]$ tends to 1 as $n$ tends to infinity.

---


### 171. [SAGE-OR: Semi-supervised Adaptive Scene Graph Generation for Operating Rooms](https://arxiv.org/abs/2608.15336)

**<font color=#1a73e8>作者：</font>** Brandon Leblanc, Charalambos Poullis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current surgical scene graph generation methods depend on dense multi-modal supervision and specialized hardware (synchronized RGB-D sensors, calibration rigs), making dataset construction expensive and restricting all existing benchmarks to simulated environments. We propose SAGE-OR, a feature-centric framework that replaces the traditional detect-then-reason paradigm with a decoupled representation-reasoning paradigm in which localization is derived from frozen foundation models, encoded implicitly in pre-computed features, and used without any localization supervision, while a lightweight graph transformer performs relational reasoning over cached features. We employ a semi-supervised formulation with general-purpose segmentation prompts to eliminate localization supervision while enabling unsupervised context augmentation through additional prompt-driven entities, such as hands, which are absent from annotations. General-purpose prompts are used to induce near-perfect recall, while precision is delegated to downstream attention-based reasoning, enabling simple adaptation to new entities via prompt-level modification. This design enables a lightweight 15M-parameter graph transformer that trains in 1.4 hours and runs relational inference at $\sim$1ms per frame with peak memory under 2GB, suitable for edge hardware used in the operating room; feature extraction runs offline as a separate caching stage (4.27s per frame). On the 4D-OR benchmark, the core model achieves 76% F1, matching the fully supervised 4D-OR baseline while eliminating all localization annotations, and unsupervised hand augmentation raises this to 86%, within 4 points of state-of-the-art (SOTA) methods requiring dense multi-modal supervision, providing a practical pathway for adaptation to new surgical settings without annotation other than relationship and class labels.

---


### 172. [TEA: Text Encoder Alignment for Robust Concept Erasure in Text-to-Image Models](https://arxiv.org/abs/2608.15341)

**<font color=#1a73e8>作者：</font>** Alireza Dehghanpour Farashah, Zhuan Shi, Negar Rostamzadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models can be misused to generate harmful content through adversarial or paraphrased prompts that bypass built-in safety mechanisms. Existing concept erasure methods often suffer from limited robustness against adversarial prompts, degradation of benign generation quality, or reliance on inference-time interventions that introduce persistent computational overhead. To address these limitations, we formulate concept erasure as a domain alignment problem in the text representation space. We propose a lightweight Text Encoder Alignment framework (TEA) that fine-tunes only the text encoder while keeping the generative backbone fully frozen. Given concept--anchor prompt pairs, our method trains a discriminator to distinguish token-level representations of concept-containing prompts from those of safe anchor prompts, while updating the text encoder to make these representations indistinguishable. TEA introduces zero inference-time overhead and requires only a small number of fine-tuning steps, making it highly efficient to deploy at scale. Despite this efficiency, TEA achieves state-of-the-art erasure robustness against black-box and white-box adversarial attacks on Stable Diffusion v1.4, while preserving generation quality on benign prompts. Furthermore, TEA is model-agnostic and achieves the lowest attack success rate on Stable Diffusion v3.5, extending concept erasure to a Rectified Flow Transformer architecture with T5 conditioning where prior methods remain largely unexplored. Code is available at \href{this https URL}{this https URL}

---


### 173. [Feed-Forward Hierarchical Gaussian Diffusion for Extreme CT Reconstruction](https://arxiv.org/abs/2608.15343)

**<font color=#1a73e8>作者：</font>** Yuezhe Yang, Li Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing three-dimensional computed tomography (CT) from severely constrained projections is highly ill-posed. Sparse angular sampling, restricted angular coverage, and low photon counts can occur individually or jointly, obscuring global anatomy and local tissue detail. Many learned CT reconstruction methods are tailored to a single dominant degradation. Existing diffusion and Gaussian approaches commonly recover global structure and local detail within a shared representation. We propose HiGDiff, a feed-forward hierarchical Gaussian diffusion framework that decomposes reconstruction both spatially and from structure to detail. Physics-conditioned anatomical anchors and a foreground capacity field allocate learnable Gaussian primitives to informative regions. A structure diffusion stage first recovers global attenuation geometry, and its learned representation conditions a detail diffusion stage for residual boundaries and tissue transitions. The resulting Gaussian banks are rendered as attenuation fields and further refined by a gradient-isolated residual module. Experiments on three distinct CT benchmark datasets demonstrate state-of-the-art reconstruction performance across isolated, paired, and joint degradation settings, including improvements of 5.81 dB in macro-average peak signal-to-noise ratio (PSNR) and 0.113 in structural similarity index measure (SSIM) on the Low Dose CT Image and Projection Data (LDCT-PD) collection. Code and experimental configurations are openly available at this https URL.

---


### 174. [ENAF: A Multi-Exit Network with an Adaptive Patch Fusion for Large Image Super Resolution](https://arxiv.org/abs/2608.15349)

**<font color=#1a73e8>作者：</font>** Duong M. Nguyen, Tuan Nghia Nguyen, Xuan Truong Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To accelerate single image super-resolution (SISR) networks on large images (2K-8K), many recent approaches decompose an image into small patches and dynamically determine an execution path according to its difficulty (referred to as a dynamic network). To quantify the hardness of a patch, they mainly rely on a handcrafted assessment score, e.g., edge, which weakly associates a patch's texture with the computational complexity of a SISR model. To address the problem, we introduce ENAF - a dynamic network for SISR with an adaptive patch fusion. Built on top of a backbone, ENAF incorporates multiple early exits (EEs) to tackle the over-parameterized SISR model. More importantly, ENAF plugs a tiny network that estimates PSNR to associate data texture with a computation cost at an EE. Based on the scores, ENAF effectively assigns image patches to an exit, enhancing the quality-complexity trade-off. Extensive experiments on common datasets with popular SISR backbones demonstrate the effectiveness of ENAF in various settings. The source code is provided in this https URL

---


### 175. [A Multi-Annotator Study of Segmentation Noise and Uncertainty in Turbid Underwater Images](https://arxiv.org/abs/2608.15363)

**<font color=#1a73e8>作者：</font>** Galadrielle Humblot-Renaux, Vasiliki Ismiroglou, Malte Pedersen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Label uncertainty and annotator disagreement are common challenges in the field of computer vision, yet their study has largely been confined to the medical domain or to generic image-recognition datasets. Underwater datasets are particularly susceptible to these issues due to the need for domain expertise, degraded visibility conditions, and the inherent difficulty of establishing reliable ground truth in inaccessible environments. Despite these challenges, annotation uncertainty in underwater imagery remains largely unexplored. In this work, we present the first systematic multi-annotator study of segmentation in real underwater scenes, with over 100 participants, and across varying, controlled levels of turbidity. We show that underwater datasets face many of the same annotation challenges as other vision tasks, while turbidity introduces additional systematic errors. We further investigate the main factors driving label noise and explore ways to improve annotation quality in turbid underwater environments, including privileged information, individual effort and annotator ensembles. All (meta-) data collected in this study will be available on the project page: this https URL

---


### 176. [Does 1/2-Tsallis-INF Also Work Well for Best-Arm Identification?](https://arxiv.org/abs/2608.15365)

**<font color=#1a73e8>作者：</font>** Jingxin Zhan, Yuze Han, Zhihua Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regret minimization (RM) and best-arm identification (BAI) are two fundamental objectives in multi-armed bandits. Among regret-minimizing algorithms, $1/2$-Tsallis-INF is a canonical best-of-both-worlds FTRL algorithm: it achieves logarithmic pseudo-regret in stochastic bandits while retaining minimax-optimal regret in adversarial bandits, without knowing the environment in advance. This raises a natural question: can the same algorithm, without additional exploration, also identify the best arm reliably? We study this question in stochastic bandits by analyzing the failure probability $\operatorname{Err}_t$, defined as the probability that the empirical best arm determined by the cumulative importance-weighted loss estimates of 1/2-Tsallis-INF differs from the true optimal arm. The main difficulty is that, at the logarithmic-regret scale, suboptimal arms are sampled with probability heuristically of order $1/t$. Consequently, importance weighting causes the cumulative estimator to fluctuate on the same linear scale as its mean separation. To overcome this obstacle, guided by a diffusion toy model, we construct a Lyapunov function for the gap process between the estimated cumulative loss of the optimal arm and that of the best competing arm. This leads to polynomial upper bounds on $\operatorname{Err}_t$: for learning rate $\eta_t=\alpha/\sqrt t$, $\operatorname{Err}_t$ decays at rate $t^{-2+\alpha^2\mu_{i_*}/4+\rho}$ for any $\rho>0$, where $\mu_{i_*}$ denotes the mean loss of the true optimal arm. We also establish a lower bound $\Omega(t^{-2-\varepsilon})$ for any $\varepsilon>0$, showing that the exponent $2$ is essentially tight.

---


### 177. [UC-PSRO: Utility-Conditioned Policy-Space Response Oracles with a Communication-Dropout Curriculum for Game-Theoretic Course-of-Action Generation in Adversarial Swarms](https://arxiv.org/abs/2608.15372)

**<font color=#1a73e8>作者：</font>** Phillip Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study generating game-theoretically optimized Courses of Action (COAs) for a Blue UAS swarm against an adaptive Red adversary in a communication-degraded environment, motivated by (but not derived from) a public U.S. Air Force SBIR solicitation. We propose UC-PSRO (Utility-Conditioned Policy-Space Response Oracles with a Communication-Dropout Curriculum), combining three mechanisms: (i) PSRO self-play, so Blue and Red policies train as approximate best responses to each other rather than one side against a fixed scripted opponent; (ii) FiLM conditioning of the Blue policy on a Commander's-Intent weight vector, sampled from a Dirichlet distribution during training, so one trained policy is re-steerable at execution time without retraining; and (iii) a curriculum annealing communication-graph edge dropout during training, so the swarm learns decentralized, peer-to-peer fallback instead of depending on full connectivity. We evaluate on a synthetic, unclassified stand-in for the solicitation's maritime scenario, with 5 seeds at N=25 Blue agents and a scalability sweep to N=200. We find a genuine trade-off, not a uniform win: the communication-dropout curriculum alone gives the strongest, most robust mission-completion rates of any learned method, improving counter-intuitively as denial increases (35% to 62% success as dropout rises from 0 to 0.75); adding utility-conditioning and PSRO self-play substantially slows convergence within a fixed budget, and we find no reliable exploitability advantage for self-play over a fixed-opponent policy, both statistically indistinguishable from a small, near-zero gap. We report this honestly as a convergence cost not yet offset by a demonstrated robustness benefit, rather than overstating one method as dominant, and provide a fully vectorized, open environment training at N=200 agents in single-digit milliseconds per step on a single consumer GPU.

---


### 178. [Beyond Field Accuracy: Two-Axis Diagnosis of Inverse-PINN Parameter Error](https://arxiv.org/abs/2608.15373)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Qian Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse physics-informed neural networks (PINNs) can reconstruct a field accurately while returning an incorrect physical parameter. We introduce a two-axis post-training diagnosis that separates finite-sample resolution under a specified observation-and-estimation protocol from the signed parameter preference encoded by the final learned field and residual metric. The first axis repeatedly fits noisy observations with a matched forward estimator. At known synthetic truth, the second freezes the field and residual view and computes a local score displacement toward a nearby residual-profile minimum. Endpoint consistency then tests whether joint training delivers that preference under the same final view. Across three synthetic one-dimensional, scalar-parameter PDEs, matched-forward mean absolute relative error ranges from 2.34 percent to 17.46 percent. The displacement tracks frozen-profile minima across locked seeds, architectures, and fresh-noise retraining (r from .945 to .982), and it tracks delivered signed log-error in 240 fresh-noise RBA runs (r = .994; 237/240 correct directions). A coupled two-parameter Darcy check validates the full matrix calculation. The axes are complementary diagnostic coordinates, not additive error components or a deployable oracle-free estimator. Together, they route follow-up work toward observations, residual evidence, or endpoint delivery.

---


### 179. [Look Before You Lift: Visual and Quantitative Diagnostics for Topological Deep Learning](https://arxiv.org/abs/2608.15388)

**<font color=#1a73e8>作者：</font>** Mathilde Papillon, Guillermo Bernárdez, Álvaro Ballón Barreiro 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topological deep learning (TDL) methods rely on lifting raw data into higher-order discrete domains such as simplicial complexes, cell complexes, and hypergraphs. In practice, this lifting step is often treated as a black box: practitioners select a lifting and then tune architectures, with limited visibility into whether the induced higher-order connectivity is meaningful for the downstream task. To address this missing diagnostic layer, we propose a visualization technique called TopoExplorer that leverages the strictly augmented Hasse graph form of topological datasets for exploratory data analysis. For the first time, practitioners can easily visualize the incidence- and adjacency-based neighborhoods that define the lifted dataset, as well as read off key graph metrics that describe its structural and feature landscape. Via an extensive set of experiments across many datasets and liftings, we show that several of these metrics correlate with downstream model performance, suggesting they can help inform TDL preprocessing design. Our perspective reframes the TDL workflow from lift-train to lift-look-design-train, enabling more principled, interpretable, and efficient model development. TopoExplorer is hosted at this https URL, and its source code is available at this http URL.

---


### 180. [JoLT: Joint Latent Trajectories for Context-Guided High-Resolution Tiled Generation](https://arxiv.org/abs/2608.15395)

**<font color=#1a73e8>作者：</font>** Mathis Koroglu, Guillaume Jeanneret, Hugo Caselles-Dupré 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although text-to-image generative models produce impressive results, they struggle to generate densely detailed, high-resolution (HR) images. Current literature addresses this issue with a low-to-high-resolution approach. First, a low-resolution (LR) image is generated. Then, an upsampled version is generated using the LR image as an additional cue. In this paper, we present Joint Latent Trajectories (JoLT). To generate an image, JoLT uses two streams that jointly denoise LR and HR latent images at each sampling step. The LR latent controls the overall layout, while the HR latent controls the details. We interconnect both branches to jointly integrate their information. We extensively validate our method, demonstrating its advantages over competing baselines. The resulting images are not only richly detailed but also visually pleasing, opening new avenues for artistic creation.

---


### 181. [Towards a theory of inference-time alignment with unknown rewards](https://arxiv.org/abs/2608.15402)

**<font color=#1a73e8>作者：</font>** Steve Hanneke, Hongao Wang, Mingyue Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative model alignment has received broad interest, and significant progress has been made in supervised fine-tuning and inference-time computation. Yet, alignment has remained poorly understood from a statistical learning perspective. We formulate inference-time alignment as a weak-to-strong learning problem, where a reference policy (weak learner) is assumed to be fairly good and the goal is to produce a strong learner that predicts a good response at test time with arbitrarily high probability. Our problem is formulated as learning from scratch --- everything is learned from data rather than assuming access to a good reward estimate, and thus differs from the existing inference-time alignment theory. Our model shares similarity to the recent work of arXiv:2510.15464, where for each prompt, there could be multiple good responses. Our definition of the alignment learnability follows the PAC learning principle. We introduce a novel combinatorial dimension of the reward class which we call the alignment dimension, and show that it completely characterizes the alignment learnability --- a reward class is alignment learnable if and only if its alignment dimension is finite. The core of our learning procedure works by invoking the ordinary one-inclusion graph algorithm to run a tournament over all pairs of label sets satisfying that neither is a subset of the other. We believe our results might shed light on establishing a complete theoretical understanding towards alignment.

---


### 182. [FAST-DeepONet: Factor-Augmented Branch Representations for High-Dimensional PDE Inputs in the Small-Sample Regime](https://arxiv.org/abs/2608.15408)

**<font color=#1a73e8>作者：</font>** Jiyong Kwon, Bongseok Kim, Guang Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep operator networks can become statistically unstable when partial differential equation inputs are observed at thousands of strongly correlated sensors but only a small number of operator samples is available. We introduce FAST-DeepONet, a branch representation combining a fixed spectral path with a regularized projection of the orthogonal residual, in which the directional penalty acts on the effective residual map after each of its rows is normalized. On Navier--Stokes flow a plain DeepONet degrades from $0.0394$ to $0.1556$ mean relative $L_2$ error as the branch grows from $129$ to $8193$ coordinates, while FAST-DeepONet stays near $0.04$, so the sensor grid can be refined without a statistical penalty. Across independent test sets for Navier--Stokes flow, Darcy flow, and signed terminal wavefield prediction it lowers mean relative $L_2$ error by $4.7\%$ to $37.0\%$ with three to seven times fewer trainable parameters. A spectral-only branch sharing the same basis separates the two paths: the fixed spectral path carries the improvement on Navier--Stokes and Darcy, while terminal wave prediction requires the residual path together with its directional penalty. FAST-DeepONet targets coordinate-query architectures and trains on solution values alone.

---


### 183. [A survey of AI-generated voices and their detection](https://arxiv.org/abs/2608.15411)

**<font color=#1a73e8>作者：</font>** Chengzhe Sun, Tianle Yang, Siwei Lyu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The ability of artificial intelligence (AI) models to generate highly realistic human voices has advanced rapidly. These technologies power accessibility tools, virtual assistants and creative applications, but they also enable harmful uses, including impersonation, fraud and disinformation. Recent incidents of voice cloning scams targeting businesses and political leaders underscore the urgent need for robust safeguards. Unlike image and video deepfakes, the detection of synthetic voices poses unique challenges due to the complexity of phonetics, prosody and auditory perception. This survey offers a comprehensive overview of AI voice generation and detection methods, encompassing both the technical foundations and the latest state-of-the-art advances. This study also identifies key open challenges, benchmark resources and future directions to make this survey useful for future researchers.

---


### 184. [ArtLang: Structured Language-to-Kinematics Grounding for Articulated 3D Actuation](https://arxiv.org/abs/2608.15419)

**<font color=#1a73e8>作者：</font>** Sylvia Yuan, Dan Wang, Ravi Ramamoorthi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Articulated-object reconstructions recover explicit geometry and kinematics, but their parts often remain semantically anonymous and must be controlled through part indices and numerical joint parameters. We present ArtLang, a framework for open-vocabulary language control of persistent reconstructed articulated assets. ArtLang represents an asset as a semantic-kinematic articulation graph and augments its surface with language features and graph-constrained motion. Open-vocabulary proposals are bound to reconstructed parts while allowing uncertain parts to remain unnamed. A typed parser converts a command into a directive graph containing referring expressions, actions, magnitudes, reference frames, and relations. We then solve a global graph-to-graph grounding problem that jointly reasons about semantic, spatial, relational, and kinematic compatibility, with support for null assignments and abstention under ambiguity. Accepted directives are converted into continuous joint targets within the observed motion range and executed through forward kinematics. Experiments on synthetic reconstructions, mesh-based assets, and real captures demonstrate reliable language grounding and continuous articulated control across repeated parts, spatial references, relational commands, and ambiguous instructions.

---


### 185. [HistReNeRF: Historic Image Relocalisation within Contemporary Neural Radiance Field Reconstructions](https://arxiv.org/abs/2608.15420)

**<font color=#1a73e8>作者：</font>** Benjamin T. Hughes, Stuart James  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Relocalising archival photographs within a contemporary scene model is challenging because historic and modern views can differ in photographic appearance, visible objects, and spatial layout. Therefore, we present HistReNeRF, a framework that estimates the 6-DoF pose of a historic photograph by matching adapted DINOv2 patch features to candidate rays sampled from a contemporary Neural Radiance Field (NeRF) reconstruction. The continuous representation of a NeRF provides a queryable scene interface from which candidate rays can be sampled and matched, enabling domain adaptation between historic photography and contemporary images directly in the feature representation used for localisation. We evaluate embedding-space-based domain adaptation against pixel-space methods on a new cross-temporal dataset comprising 10,545 contemporary street-level images and 230 archival photographs from three European landmarks. Embedding-space adaptation reduces translation and rotation errors by an average of 11% and 16%, respectively, across the three scenes. These results show that neural scene relocalisation provides a natural interface for feature-space adaptation, reducing cross-temporal appearance shift without modifying the query image. Code and dataset at this https URL.

---


### 186. [SAGA: Structure-Attended Generative Action Embedding Model that encodes Multi-Surface User Action Sequences](https://arxiv.org/abs/2608.15429)

**<font color=#1a73e8>作者：</font>** Tsz Fung Pang, Po Jen Chen, Nimish Ronghe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior embedding models for sequential recommendation typically operate within a homogeneous action space, limiting their ability to capture cross-surface behavioral signals spanning distinct behavioral domains. We present SAGA, a generative action embedding model that encodes multi-surface user interaction sequences across a Financial Service organization's ecosystems, from checkout, peer-to-peer (P2P) transactions, in-app engagement, email to account actions, into a unified user representation for downstream recommendation tasks. Central to SAGA is a per-field tokenization schema that decomposes each action event into multiple field-level tokens (e.g. product, interaction, surface), enabling field-level attention and per-field training objectives that fused single-token approaches cannot support. Through an offline ablation study on loss formulation, tokenization granularity and training data scope, we isolate the contribution of each design choice. A downstream model integrated with SAGA-generated user embeddings delivers the strongest overall click and conversion lift across diverse downstream touchpoints, compared to all ablated and alternative architectures.

---


### 187. [Everything Is a VisionBlock: Conversational Authoring over Git-Versioned Content for Spatial Computing](https://arxiv.org/abs/2608.15442)

**<font color=#1a73e8>作者：</font>** Zhaoming Yin  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Spatial applications compile their content into shipped binaries, so every change costs a build-and-redeploy cycle. We present the VisionBlock system, which splits an application into an engine -- a generic binary with a fixed set of capabilities (render panels, volumes, and immersive scenes; fetch data; run gestures) -- and themes: complete applications expressed as trees of VisionBlocks, units of declarative content the engine renders. Themes are data: creating, changing, or publishing one never touches the binary. Authoring is a chat -- each turn produces a VisionBlock's next version -- and versioning is plain git. The model is five-dimensional: dimensions 1-3 are space (panel, volume, room); dimension 4 is time (git history -- revert to roll back, branch to try variants); dimension 5 is the principal (the per-user domain: the same path resolves differently per person). The engine renders one point, (x, y, z, version, principal). One consequence follows per non-spatial axis: iteration collapses to chat turns and reverts; ownership and permission are properties of content; and together they make applications items -- grantable, forkable, sellable subtrees, an economy of apps inside one binary. A blockchain explorer, a document reader, an immersive showroom all run on the same engine; none requires a deploy to change. This paper presents the design; a production implementation is underway, and a subsequent version will report implementation and evaluation.

---


### 188. [Semantic Space of Parts of Speech](https://arxiv.org/abs/2608.15443)

**<font color=#1a73e8>作者：</font>** Jiří Milička, Ivan Kraus, Arnold Stanovský 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parts of speech categorization is understood in the European linguistic tradition as crisp categorization, which is also reflected in corpus linguistics, where each disambiguated token is assigned exactly one POS. However, the assigned categories are largely determined by arbitrary decisions distilled into annotation manuals. Since some words stand between parts of speech in their semantics or typical syntax, and some parts of speech are closer to each other than others, POS categorization seems inherently fuzzy. We analyze this fuzziness using word2vec embeddings, training a neural network to reduce their high dimensionality to three dimensions relevant for determining parts of speech. This creates a three-dimensional space onto which we map several thousand words, revealing which are prototypical and which lie on the boundaries, and visualizing relationships between parts of speech. The study uses Universal Dependencies POS tags for French, Czech, Finnish, Russian, and English.

---


### 189. [Detecting Money Laundering in Rwandan Mobile Money: A Machine Learning Framework](https://arxiv.org/abs/2608.15447)

**<font color=#1a73e8>作者：</font>** Emmanuel Nahimana, Yaé Ulrich Gaba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile money has widened financial access across Sub-Saharan Africa and enlarged the surface for money-laundering and terrorism-financing (ML/TF) activity in ecosystems dominated by high-volume, low-value transactions. Rwanda is a case in point: several million active mobile-money users, telecom-led wallets on the MTN and Airtel networks, and a Financial Intelligence Centre (FIC) supervising transaction streams whose scale exceeds static rule-based monitoring. This paper develops and evaluates a transaction-monitoring framework aligned to the Rwandan AML/CFT regime under (i) extreme class imbalance (~0.1% prevalence), (ii) scarce and delayed labels, and (iii) bounded investigator capacity. Using SAML-D, a synthetic dataset of 9,504,852 transactions with 17 laundering typologies, we engineer account-centric behavioural features (rolling velocity, net-flow directionality, counterparty diversity, burstiness) and benchmark supervised classifiers (Logistic Regression, Random Forest, LightGBM), unsupervised anomaly detectors (Isolation Forest, Local Outlier Factor), a dense autoencoder, and a late-fusion meta-learner. Evaluation is operational: PR-AUC, recall at a calibrated ~90%-precision point, recall at top-K%, and alerts per 10,000. On the chronologically held-out test period, LightGBM attains PR-AUC = 0.0469, capturing 64 laundering cases at precision ~0.89 with 0.51 alerts per 10,000; the fusion stacker reaches PR-AUC = 0.0477 at precision ~0.91 and 0.46 alerts per 10,000, recovering 59 true positives. We map score bands to Rwanda-relevant analyst workflows and STR/SAR escalation, and outline a staged path from synthetic prototyping to real-data validation with the National Bank of Rwanda and FIC. The contribution is operational: a governance-aware pipeline and evaluation protocol calibrated to the constraints of an African mobile-money regulator, not a new algorithm.

---


### 190. [Spatially-Grounded Flow Matching: Structured Source Distributions for Image Generation](https://arxiv.org/abs/2608.15452)

**<font color=#1a73e8>作者：</font>** Arman Zarei, Mahdi M. Kalayeh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current flow matching models learn to transport the source i.i.d. Gaussian noise into the target distribution of natural images, yet this source distribution carries no notion of spatial structure. Images however are fundamentally local since nearby pixels are strongly correlated. By sampling the noise independently, we hypothesize that models are implicitly encouraged to exploit less noisy neighbors as context during training, partially bypassing the need to properly learn the true local structure of images. The source distribution, in other words, works against the inductive bias of the image domain. To ameliorate this design discrepancy, we propose StructFlow which encodes spatial locality directly into the source by having the pixels within a small region share a common noise component. This structured source produces transport paths that are geometrically aligned with image regions - enabling properties that generic flow matching struggles to provide: fine-grained local editing that naturally respects boundaries, robust structure preservation, and smooth semantic interpolation between images. We show that these benefits also extend to large pre-trained models, demonstrating that StructFlow can even be incorporated through a lightweight post-training phase. Comprehensive experiments on multiple datasets, in unconditional, class and text-conditioned regimes, using different diffusion transformer architectures confirm that StructFlow not only offers competitive image generation quality, but also significantly improves localized controllable re-synthesis.

---


### 191. [High-Dimensional Nonparametric Change-Point Detection via Low-Rank Degree-Three Density Projection](https://arxiv.org/abs/2608.15466)

**<font color=#1a73e8>作者：</font>** Guoqing Zhang, Zhaixin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributional changes can be invisible to means and covariances yet appear in skewness, asymmetric interactions, or other third-order structure. We develop a nonparametric change-point method that retains every degree-at-most-three coefficient of a density while avoiding direct density estimation. For observations in $[-1,1]^d$, we construct a symmetric order-three Legendre feature tensor $H_3(X)\in\Sym^3(\R^{d+1})$ such that $A(f)=\E_fH_3(X)$ is an exact isometric encoding of the degree-three density projection: $\|A(f)-A(g)\|_{\F}=\|P_3(f-g)\|_{L^2}$. Instead, fixed tensor contractions are degree-three polynomial chaoses with $\psi_{2/3}$ tails. The two terms have the characteristic order-three tensor scaling and match the powers in sharp concentration results for simple random tensors. For a coordinate-orthogonal specialization, the bound improves to $\sqrt{\log d}$ and enables a prefix-sum implementation in hundreds of dimensions. We derive the exact population tent shape and localization margin, introduce a seeded shortest-interval algorithm with a padded local recentering step, and prove exact recovery by induction: null recursive segments remain inactive, every undetected change retains a balanced isolating interval, and the shortest active seed contains exactly one change before recentering. A two-way cross-fitted scalar refinement attains $O_{\Pp}(\kappa^{-2})$ localization in the small-jump regime, matching a Le Cam lower bound on a pure cubic family whose degree-two projection jump is exactly zero. Reproducible experiments at $d\in\{20,50,100,200\}$ and a three-change $d=100$ sequence demonstrate the intended high-dimensional regime without materializing a $(d+1)^3$ tensor.

---


### 192. [Population Structure Analysis of an Inbred Population using Quantitative Shape Phenotyping from Stereo Retinal Photographs](https://arxiv.org/abs/2608.15471)

**<font color=#1a73e8>作者：</font>** Li Tang, Michael D Abramoff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The population structure of an inbred population of 781 people on Norfolk Island in the Pacific, 318 of which are descendants of the original Mutineers of the Bounty, is analyzed phenotypically using shape from stereo retinal fundus photographs. Three-dimensional optic nerve head (ONH) shape is reconstructed from stereo pairs by a multi-scale stereo matching algorithm. Using deep neural network, the shape of ONH, which is under genetic control, is decomposed into a set of hierarchical features through self-taught learning. Features captured at different levels are selected according to their discriminant power in identifying the two populations. The prediction accuracy is evaluated with stratified cross validation. Given the selected feature set, individuals are grouped into k hierarchical clusters and cluster membership fractions are determined for k=2,3,4,5,6,7. Population structure analysis on the basis of phenotypes through image analysis allows heritability and linkage analysis, including founder effects from English and Polynesian ancestors, potentially leading to new genetic risk factors for glaucoma and other ONH-related eye diseases.

---


### 193. [Optimal Lower Bounds for Networked Information Aggregation](https://arxiv.org/abs/2608.15472)

**<font color=#1a73e8>作者：</font>** Ambar Pal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The problem of networked information aggregation, studied in Kearns et al. (2026), involves a group of learners situated on the vertices of a directed acyclic graph $G$, each learning a linear predictor $\widehat Y$ for a fixed random variable $Y$ given access to a local feature, as well as the predictors learnt by its parents. Learning proceeds iteratively, with learners ordered according to a topological sort of $G$. The main quantity of interest is the error incurred by the current learner, constrained to this flow of information, with respect to the best linear predictor using all the features seen so far. When the studied error is the MSE, i.e., $\mathbb{E} (\widehat Y - Y)^2$, Kearns et al. (2026) show that the error is at most $O(1/\sqrt{D})$ along a path of length $D$. They also obtain a hard instance where the MSE is lower bounded by $\Omega(1/D)$, leaving the correct order open. In this work, we resolve this central open problem, and obtain a family of worst case problem instances with a MSE lower bound of $\Omega(1/\sqrt{D})$.
By exploiting invariances in the structure of the learnt predictors, our analysis generalizes to all convex loss functions $\ell(\widehat Y, Y)$ satisfying regularity conditions which include strong convexity in a ball around the origin, and that the ideal predictor minimizing the population loss is positively correlated with the label. We show that networked information aggregation on a gaussian instance in our worst case family incurs an $\ell$-error lower bounded by $\Omega(1/\sqrt{D})$ with respect to this ideal predictor. We demonstrate that a variety of common losses satisfy these regularity conditions. In particular, the logistic loss satisfies them, and hence our analysis also closes the gap between the upper and lower bounds in Bateni et al. (2026).

---


### 194. [Measuring Structured Predictability in Neural Training Dynamics: A Cross-Regime Study](https://arxiv.org/abs/2608.15483)

**<font color=#1a73e8>作者：</font>** Fanqi Wang, Weisheng Tang, Hairong Qi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep networks are trained through long update trajectories, yet their temporal organization remains less systematically characterized than architectures, losses, or optimizers. We study short-horizon predictability as a measure of temporal redundancy: where, when, and under which training conditions recent updates contain information about near-future parameter motion. We combine three complementary probe families, displacement-direction, subspace-residual, and predictor-based probes, with convention-aware, null-calibrated group-level readouts, and apply them to multi-pass vision training on CIFAR and public Pythia pretraining checkpoints. Across both regimes, vector-like tensors such as normalization parameters and biases (auxiliary parameters) exhibit simpler short-horizon dynamics than matrix-like feature-transforming weights (bulk parameters), whose predictable behavior concentrates in localized, time-varying pockets. Agreement within and across probe families, and with independent trajectory diagnostics, indicates that these measurements capture intrinsic trajectory structure, while probe differences distinguish complementary forms of temporal organization. Controlled CIFAR comparisons further show that architecture and training recipe systematically modulate the measured structure. A Pythia-70M case study further exposes a sequence of role-, depth-, and scale-dependent events, including bulk ESA falling below the random sign-agreement level and the emergence and redistribution of predictable qkv pockets across layers. These results position short-horizon predictability as a retrospective, parameter-resolved diagnostic of training dynamics.

---


### 195. [A Network-driven Framework for Public Event Forecasting via Dynamic Interaction Network Evolution](https://arxiv.org/abs/2608.15488)

**<font color=#1a73e8>作者：</font>** Jie Wei, Yue Liu, Xiaochuan Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective public event forecasting is essential for intelligent service systems, enabling proactive risk management, adaptive resource allocation, and timely decision-making. In many real-world scenarios, the evolution of public events is driven by dynamic interactions among participants. Motivated by this observation, this paper proposes auto-ibDLM, a network-driven deep learning framework that represents events as dynamic interaction networks and predicts public event evolution through participant growth forecasting. The proposed framework adopts a hybrid representation learning strategy that first represents network evolution using network science-informed structural metrics and subsequently transforms the resulting structural feature vectors into compact and robust latent representations through an auto-learning layer. A GRU-based temporal forecasting module is then employed to capture temporal dependencies and predict future participant growth. Extensive experiments on 13 real-world public event datasets and two publicly available dynamic network datasets demonstrate that auto-ibDLM consistently outperforms representative state-of-the-art methods in both forecasting accuracy and generalization capability, achieving over 97% accuracy in public event forecasting. Comprehensive experimental analyses further validate the effectiveness of the proposed hybrid representation learning strategy and demonstrate its representation-level interpretability. These results indicate that auto-ibDLM provides an effective and practical solution for intelligent public event forecasting.

---


### 196. [QSMP: finding representative time series subsequences through Quick Shift+Matrix Profile](https://arxiv.org/abs/2608.15492)

**<font color=#1a73e8>作者：</font>** Carlos H. Mendoza-Cardenas, Rogers F. Silva, Austin J. Brockmeier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finding representative waveforms in long time series has scientific and practical value in many domains, as it enables summarization and visualization of large time series datasets, and downstream tasks like classification and forecasting. We present here QSMP, a method to find representative waveforms in long time series through a density-guided clustering of time series subsequences. Our method makes a novel connection between Quick Shift, a mode-seeking algorithm, and the Matrix Profile, a time series similarity-search data structure, to adapt Quick Shift to the clustering of subsequences in long time series, with a space complexity that is superior to the state-of-the-art method. Our experiments on synthetic and real datasets show that QSMP can be a valuable tool to summarize and visualize long time series by finding representative waveforms.

---


### 197. [Who Leads Now? Token-Level Modality Arbitration for Chart-to-Code Generation](https://arxiv.org/abs/2608.15510)

**<font color=#1a73e8>作者：</font>** Qinghao Fu, Yarong Wang, Shunlei Ning 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chart-to-code generation requires a model to read the fine-grained visual details of a chart and write executable code that reproduces it. Existing chart-to-code methods either train visual and coding abilities separately, or fine-tune on chart-to-code data with the two abilities entangled. Neither strategy accounts for the distinct nature of the two abilities or the interference that arises when they are optimized together. We propose MoCA (Mixture of Cross-modal Arbitration), which separates the two abilities rather than blending them. MoCA is built on Cross-modal Arbitration Block (CAB), which maintains a visual branch and a code branch as two distinct pathways, and a lightweight arbiter that arbitrates their relative contributions at every layer and generated token. We train MoCA in two stages: a supervised warm-up on self-distilled reasoning trajectories that decomposes visual understanding into explicit steps, followed by reinforcement learning with rewards on both the reasoning process and the final code. Analysis shows that the arbiter learns structured rather than arbitrary allocations, with expert contributions varying systematically across tokens, layers, and instances. Across three benchmarks, MoCA delivers competitive performance against general-domain and chart-specialized models. Ablation results show that the gains cannot be attributed to a larger model size alone, but instead arise from the joint contributions of complementary visual and code branch initialization and input-conditioned arbitration through CAB.

---


### 198. [A Lifecycle-Oriented Detection and Defense Framework for Price Manipulation Attacks in DeFi](https://arxiv.org/abs/2608.15518)

**<font color=#1a73e8>作者：</font>** Xingyu Xiong, Chang Liu, Xiaoqi Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Aiming at frequent oracle price manipulation attacks in Decentralized Finance (DeFi), this paper investigates attack patterns, vulnerability types, risk assessment, automated detection, and defense strategies. Based on Oracle lifecycle theory, a three-layer attack tree covering the physical, protocol, and application layers is constructed to analyze the attack chain and identify the data election stage as a key intrusion point. Four major contract-level vulnerabilities are summarized: insufficient validation of price data flow, oracle call risks, uncontrolled cross-contract calls, and defects in AMM price reading logic. Fuzzy-AHP and Value-at-Risk (VaR) models are combined to quantify risk factors and construct a risk matrix covering technology, market, governance, and contract risks. An automated detection tool based on an extended Slither framework is developed using taint tracking and pattern matching. Finally, a multi-layer defense strategy is proposed, integrating trusted execution environments at the data source layer, TWAP smoothing and adaptive circuit breakers at the smart contract layer, and optimized kernel network configurations at the operating system layer. Experiments show that the proposed approach reduces attack-induced price deviation from 55.56% to below 5%. The detection tool achieves 94.38% accuracy and 92.31% recall, outperforming existing open-source tools.

---


### 199. [Guaranteed Adaptive Modality Acquisition: When the Policy Chooses Its Own Calibration Group](https://arxiv.org/abs/2608.15520)

**<font color=#1a73e8>作者：</font>** Melika Baghi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A multimodal system may begin inference holding only some of its inputs and may acquire the rest at a cost. With adaptive acquisition, the policy determines which inputs are ultimately observed, so we state the guarantee conditional on that terminal input pattern. Conditional calibration normally assumes the grouping map is fixed independently of the calibration sample, which policy-induced grouping does not satisfy. We characterize when pattern-conditional guarantees remain valid and give two finite-sample constructions: threshold-free routing with calibration applied at the terminal pattern, and simultaneous certification of complete policy-pattern pairs, which lets calibration data select the deployed policy. A counterexample shows that a guarantee proved for a calibration-independent grouping map need not transfer once the policy makes the terminal group calibration-dependent. We call the resulting method RouteCert. On a clinical electrocardiogram task with a staged, cost-ordered lead protocol, the certified policy answers 71.2% of held-out patients at an observed 7.4% disagreement with the cardiologist's diagnosis at 48.8% of the prespecified ordinal cost of acquiring every stage, and all three acquisition stages carry their own certificate. On masked multimodal benchmarks, certifying pointwise at each terminal pattern holds observed worst-pattern selective risk, measured against the full-information reference decision rather than the true label, at 0.034 where a pooled design reaches 0.145 against a 0.10 cap, at a comparable answered fraction (0.350 vs 0.342); under the budget-matched simultaneous comparison the answered fraction falls to 0.305.

---


### 200. [Efficient Audio-Visual Generation via Synchrony-Aware Cross-Modal Sparse Attention](https://arxiv.org/abs/2608.15522)

**<font color=#1a73e8>作者：</font>** Shengchuan Gao, Teng Hu, Bohao Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent audio-visual generation models can synthesize synchronized video and sound in a unified diffusion process, but their inference cost remains high because long video token sequences require repeated attention computation across denoising steps.A variety of acceleration techniques have been developed for video generation models, including low-bit quantization, attention sparsification, and feature this http URL, since these methods are originally designed for video generation, directly applying them to audio-visual models overlooks the interactions between the audio and video branches and may therefore disrupt audio-video this http URL present a synchronization-aware acceleration framework for efficient audio-visual this http URL key observation is that bidirectional audio-video cross-attention reveals structured interactions between the two branches, with high responses often concentrated on a few sound-related visual and temporal this http URL by this interaction pattern, we introduce a protected sparse attention strategy that preserves high-fidelity computation for synchronization-critical tokens while sparsifying redundant attention this http URL explicitly accounting for cross-modal dependence during acceleration, our method improves inference efficiency while keeping video quality, audio quality, and audio-video synchronization.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
