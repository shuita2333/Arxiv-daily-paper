# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-534](./part-11.md)

---

### 401. [Variance-Aware Non-Stationary Bandits:All-Budget Regret Bounds and Adaptation Costs](https://arxiv.org/abs/2610.26116)

**<font color=#1a73e8>作者：</font>** Xiaojin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low reward variance reduces estimation cost, but does not eliminate monitoring of arms that may improve while unobserved. We refine the variance--variation tradeoff and characterize how both costs depend on supplied variance and variation budgets in bounded, non-stationary multi-armed bandits. Let $A$ be the number of arms, $T$ the horizon, $B$ a bound on consecutive mean variation excluding the initial vector, and $Q$ a bound on the sum of the largest per-round reward variances. For every admissible pair $Q,B$, the minimax expected dynamic regret is, within a single logarithmic factor, \[
\min\{T,\;A+\sqrt{AQ}+(AQBT)^{1/3}
+\sqrt{AT}\min\{B,\sqrt B\}\}. \] The deterministic boundary $Q=0$ is characterized without logarithms. For small positive budgets, a safe calibration phase identifies a common interval containing all future means of surviving arms. Clipping observations to a wider interval reduces the cost of restarting a prior hybrid static-regret algorithm; an original-mean analytical reference controls its residuals without charging the variation of clipped means. Balancing clipping bias and monitoring closes the small-budget noisy regime. Fixed oblivious constructions give the matching lower bound. We also quantify adaptation costs: on a disclosed deterministic one-improvement family, a stationary-regret budget has a matching worst-case change-regret frontier, including a finite improvement pulse. This implies an $\Omega((T/A)^{1/4})$ loss when one policy competes with all supplied-budget deterministic oracle rates. The budget-free low-noise scheduling problem remains separate.

---


### 402. [Optimal Multi-Kernel Combination for Online Multi-Label Classification](https://arxiv.org/abs/2610.26123)

**<font color=#1a73e8>作者：</font>** Tingting Zhai, Wei Liu, Renjian Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-label classification is particularly challenging in streaming scenarios, where data arrives sequentially. Online kernel methods offer a promising solution. However, prevailing methods rely on a single preselected kernel, making them prone to suboptimal choices since the global data distribution is unknown in advance in online settings. Although the recent method, Online Kernel Selection for Online Multi-label Classification (OKS-OMC), enables data-driven kernel selection, it fails to fully harness the complementary information from multiple kernels and encounters the curse of kernelization. To address these limitations, this paper introduces a novel online multi-kernel combination method for large-scale multi-label classification. First, an efficient and robust online single-kernel multi-label method is designed. Second, learning an optimal convex combination of multiple multi-label kernel classifiers is formalized as a structural risk minimization problem. An improved alternating optimization procedure is developed, in which the combination coefficients are updated by directly minimizing the objective function, while each kernel classifier is updated by minimizing a surrogate upper bound. This procedure decouples the learning of kernel classifiers from combination coefficients, allowing independent classifier updates via our single-kernel method and accelerating convergence to high-quality solutions. Our multi-kernel method is proven to asymptotically converge to the optimal fixed convex combination of the best fixed single-kernel models chosen in hindsight. Ablation studies confirm that our method's components outperform their counterparts in OKS-OMC. Comprehensive evaluations across 11 datasets and seven metrics demonstrate our method's overall superiority over existing online multi-label methods.

---


### 403. [Dynamical Batching: How Class-Cycling Training Shapes the Internal Structure of Neural Networks](https://arxiv.org/abs/2610.26156)

**<font color=#1a73e8>作者：</font>** Nicolás Ratier-Werbin, Samuel Lozano, Miguel Ruiz-García  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether cyclically varying the class composition of training batches can modify both the performance and the internal organization of neural networks. Motivated by nonequilibrium systems, in which cycling between related sub-goals can make switching between their solutions increasingly efficient, we introduce Dynamical Batching (DB), a sampling protocol that periodically emphasizes each class while leaving the loss and the optimizer unchanged, and compare it with Uniform Batching (UB), in which every mini-batch has equal class proportions. In the regime where standard training fails, DB changes the outcome: on a three-arm spiral, a capacity-limited MLP that plateaus far below perfect accuracy under UB fits the training data under DB. Tracking individual weights, we find that under DB the change between class-specialized states is carried by a smaller set of weights than under UB, and that this set is markedly more persistent from cycle to cycle, on every synthetic dataset we test and in a wider network that fits the data under both protocols. This organization is a signature of the protocol rather than a predictor of its benefit: it appears equally where DB leaves accuracy unchanged. On CIFAR-10, the same protocol modestly improves the test accuracy of a channel-narrowed ResNet-10, a standard residual architecture, and of a second capacity-limited convolutional network. These results show that how class emphasis is distributed in time can shape both the solution a network reaches and the internal structure of the network.

---


### 404. [VISAGENT: An Agent-Based End-to-End Voice Interaction System](https://arxiv.org/abs/2610.26168)

**<font color=#1a73e8>作者：</font>** Xiang Wang, Zhaoxiang Liu, Xiang Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice-based public services have evolved from manual switchboards to intelligent platforms to meet modern user needs. However, current systems remain constrained by rigid menu-driven interaction, fragmented vertical services, and limited extensibility. To address these issues, we present VISAGENT, an agent-based end-to-end voice interaction system for large-scale public services that integrates end-to-end speech interaction, hierarchical agent routing, a scalable voice-agent marketplace, and user memory support. The system replaces menu-driven workflows with natural speech and dynamically dispatches user requests to either a general conversational model or specialized domain agents via a two-level routing paradigm that achieves sub-second intent-to-agent selection over hundreds of agents. User memory informs preference-aware agent selection and supplies relevant preferences and context to selected agents, supporting personalized task execution and reducing the need for users to repeat previously provided information. A voice-agent registration mechanism converts task agents into conversational entities, enabling dynamic onboarding and ecosystem-level extensibility. We validate VISAGENT through a real-world deployment in China's 114 hotline across multiple service domains. Experimental results demonstrate low-latency full-duplex interaction, robust routing scalability, and competitive speech naturalness. More broadly, this work advocates a shift from isolated voice assistants toward agent-centric conversational infrastructures, providing a general blueprint for building extensible voice-agent systems in public services and beyond.

---


### 405. [Conditional information Retrieval for Longitudinal Survey Harmonisation](https://arxiv.org/abs/2610.26173)

**<font color=#1a73e8>作者：</font>** Wing Yan Li, Zeqiang Wang, Michelle Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying conceptually equivalent questions across different surveys is a challenging information retrieval task where surface-level textual similarity is insufficient. Two questions may be lexically similar yet assess entirely different sociological sub-concepts, or lexically different yet conceptually equivalent. We introduce a conditional information retrieval framework that addresses this by decomposing the task into two steps: concept extraction, which identifies the underlying sociological concept of a survey question using a fine-tuned generative model, and concept-aware retrieval, which augments question representations with the extracted concept as an explicit conditioning signal for finer-grained alignment. To reflect the realistic data scarcity conditions of specialised social science annotation, we use CLOSER as a case study. Our framework consistently outperforms baselines by 2-3 points in both MAP and Recall. We further analyse fine-tuning strategies including SFT, DPO, and dynamic DPO, finding that SFT delivers the most stable gains while dynamic DPO interacts differently with instruction-tuned versus distilled reasoning backbones. Finally, we demonstrate that a model fine-tuned on a general social science thesaurus (ELSST) transfers robustly to task-specific survey data, offering a practical solution under data scarcity.

---


### 406. [PhantomTac: Hijacking Robotic Tactile Systems with Deploy-and-forget Tags](https://arxiv.org/abs/2610.26174)

**<font color=#1a73e8>作者：</font>** Binbin Zhang, Yifeng Zhang, Xiaomeng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tactile perception is crucial for precise robotic manipulation, providing an important foundation for dexterous, closed-loop force control. Among various tactile sensing techniques, magnetic tactile sensors stand out thanks to their fine-grained, three-dimensional force perception capability and strong robustness against visual occlusion. In this study, we discover a physical loophole called PhantomTac in magnetic tactile sensors. The attacker can alter the magnetic field, thus spoofing the force interpreted by magnetic tactile sensors. The attacker can stealthily deploy such an attack by simply attaching a thin (the thickness is around 0.5 mm), battery-free magnetic tag to the surface of an object. Hence, the attack tag can be easily concealed by a barcode sticker. Such an attack scheme is "deploy-and-forget" -- the attacker can deploy the tag and leave. When a robotic hand is picking up an object, it may severely damage the object. Specifically, spoofing the normal force can crush the object, whereas spoofing the shear force can lead to a loose grip, thus dropping the object. Compared with directly sabotaging the robotic hand, PhantomTac is much more concealed as the attacker does not need access to the device. We performed extensive reverse-engineering efforts to characterize the sensing mechanism of commercial-off-the-shelf tactile sensors and proposed a practical tag design. End-to-end evaluations conducted on real robots and robotic arms demonstrate that our attack can bypass existing anti-interference mechanisms and effectively hijack their closed-loop control processes, achieving an attack success rate exceeding 95% when the grasping-position offset is bounded within 8 mm. Finally, based on the limitations of existing anti-magnetic interference mechanisms, we propose a multimodal-consistency defense mechanism to mitigate such physical-layer security threats.

---


### 407. [Learning Goal-Conditioned Subgoals through Frozen Hierarchical World Models](https://arxiv.org/abs/2610.26179)

**<font color=#1a73e8>作者：</font>** Xiang Kaibo, Liu Qingfeng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hierarchical world models plan over long horizons by passing predicted states from a coarse model to a lower-level controller. Choosing these states can be expensive: the upper-level planner repeatedly differentiates through candidate macro-action trajectories. We replace this search with a lightweight goal-conditioned network trained through the frozen high-level predictor. The network supplies a conditioning vector, while the predictor generates the next latent waypoint. Training uses hindsight goals and state-prediction losses on offline trajectories, without search-solution targets or macro-action labels. Inference retains an autoregressive high-level rollout, but requires no high-level candidate optimization. We evaluate this approach on the shared-latent HWM checkpoints distributed with H-JEPA, using three backbone seeds and three head initializations per backbone. With a common evaluation protocol, mean success is 70.4% on Cube, 48.7% on Push-T, 100.0% on FourRoom, and 71.1% on Visual AntMaze. The method improves over the corresponding HWM search baseline on three environments and has the same mean on Push-T. Dedicated measurements on an NVIDIA L40S give 1.28-4.39x end-to-end speedups for batched evaluation. Ablations identify state-adaptive conditioning as a consistent contributor, while predictor-mediated subgoals and unrestricted conditions have environment-dependent benefits.

---


### 408. [HP-PnP-Flow: Hybrid Time Scheduling and Projection for Plug-and-Play Image Restoration via Flow Matching](https://arxiv.org/abs/2610.26183)

**<font color=#1a73e8>作者：</font>** Yong Li, Xiaojie Wang, Xiaoyan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration is a fundamental inverse problem that seeks to recover high-quality images from degraded observations. Plug-and-Play (PnP) methods provide a flexible framework for integrating pretrained denoisers into iterative reconstruction, whereas flow matching offers an efficient generative modeling approach based on continuous-time ODE dynamics. Very recently, Martin et al.\ (ICLR, 2025) developed a PnP-Flow method, which integrates the PnP framework with flow matching through a time-dependent denoiser constructed from a pretrained flow matching this http URL incorporating a different time schedule and an additional pixel-space projection operator, this paper proposes a novel efficient PnP-Flow algorithm (HP-PnP-Flow) that enjoys rigorous convergence guarantees under mild assumptions, without imposing restrictive conditions on iterates required by the aforementioned work. Numerical experiments on CelebA and AFHQ-Cat demonstrate that the newly proposed HP-PnP-Flow algorithm significantly outperforms PnP-Flow on several restoration tasks such as denoising, deblurring, super-resolution, random inpainting, and box inpainting. Notably, our algorithm achieves comparable or better reconstruction quality with substantially fewer iterations, reducing the iteration count from $500$ to $100$ for deblurring and super-resolution on AFHQ-Cat.

---


### 409. [On Counting Graphs for Modal Logic with Counting](https://arxiv.org/abs/2610.26187)

**<font color=#1a73e8>作者：</font>** Avijeet Ghosh, François Schwarzentruber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the theoretical computational complexity of counting trees and graphs that are classified positively by a graph neural networks, or said equivalently that satisfy a given formula of modal logic with counting. We also study convergence.

---


### 410. [Wan-Alpha++: Animating a Single RGBA Asset into Controllable Transparent Video Effects](https://arxiv.org/abs/2610.26189)

**<font color=#1a73e8>作者：</font>** Haotian Dong, Xin Wang, Wenjing Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGBA video generation is essential for creating compositable visual assets in filmmaking, game development, and digital content production. However, generating high-quality RGB appearance alongside temporally coherent transparency remains a significant challenge. Existing text-to-RGBA video methods often entangle RGB and alpha distributions and offer limited control over the precise appearance of a target asset. In addition, incorporating image conditioning typically suffers from the emergence-disappearance effects, which fail existing first-frame or first-and-last-frame conditions due to their fully transparent boundary frames. To address these issues, we present Wan-Alpha++, a unified framework that brings controllable RGBA video generation to both text- and image-to-video diffusion backbones through a shared RGBA latent space, extending our conference version Wan-Alpha from the text-conditioned setting to image-conditioned generation with an interior reference frame. Our method first learns shiftable RGB-alpha distributions while preserving the pretrained RGB prior. Specifically, we introduce a transparency-aware bidirectional diffusion objective to produce distinguishable RGBA latent representations, and a transparency-guided mean sampler that shifts the noise distribution to improve transparency generation and enable spatial controllability. Building upon this RGBA generation prior, we introduce temporal phase reparameterization for image-conditioned effect generation. By cyclically transforming a zero-positive-zero alpha pattern into a positive-zero-positive pattern, it relocates visible content to both temporal boundaries, facilitating effective appearance conditioning with limited RGBA data.

---


### 411. [VEILED-SH: Vulnerability Expression through Indirect Language Evaluation Dataset (Self-Harm)](https://arxiv.org/abs/2610.26190)

**<font color=#1a73e8>作者：</font>** Leanne Tan, Keith Chua, Shaun Khoo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI systems may miss indirect, culturally situated distress or provide support mismatched to the application context. Existing benchmarks do not jointly address cultural variation, application context, and practitioner disagreement. We introduce VEILED-SH, a benchmark and construction methodology for evaluating single-turn responses to indirect expressions of suicide, self-harm, and distress. Its 10,003 prompts span counselor chat, forum posts, platform search, and triage, drawing on Singapore-grounded sources and public datasets. An expert-validated multi-label taxonomy distinguishes intent, communicative function, and response behavior. Six automated profiles, individually calibrated to three peer-support practitioners and three clinicians, retain separate reference policies for proxy-alignment scoring. Evaluating five systems on a coverage-enriched sample reveals variation in proxy alignment across profile-generated reference policies, even for the same system responses.

---


### 412. [TaQFormer: A Treatment-as-Query Transformer with Data-Fusion for Multidimensional Treatment Modeling in Coupon Allocation](https://arxiv.org/abs/2610.26199)

**<font color=#1a73e8>作者：</font>** Jiahong Li, Zeqin Yang, Yu Xiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study coupon allocation on an online marketplace offering multiple service categories. Issuing coupons requires choosing a vector of category-specific discounts, accounting for both their direct effects and cross-category demand shifts. We present TaQFormer, a treatment-as-query Transformer for this multidimensional treatment setting. Each treatment coordinate is represented as a query token, allowing cross-attention to estimate the response to the full treatment vector. To combine large but policy-biased observational logs with a smaller stream of randomized controlled trial data, we use a two-stage pipeline: observational pretraining learns general outcome patterns, followed by LoRA fine-tuning on RCT data with a request-specific fusion gate. We evaluate the resulting system through the checks required for production, including offline uplift metrics, treatment-parallel serving, latency monitoring, and a 14-day online A/B test. At essentially the same subsidy cost rate, \model increases business value per user by 1.26\% over the production baseline and significantly outperforms both the production baseline and the RCT-only model, while meeting the latency budget. It was subsequently rolled out to all marketplace traffic and has operated at full scale for several months as of October 2026. The deployment illustrates how multidimensional treatment modeling and observational pretraining, combined with adaptation using RCT data, can support effective joint discount decisions in production.

---


### 413. [Focused Omni-Modal GUI Agents](https://arxiv.org/abs/2610.26203)

**<font color=#1a73e8>作者：</font>** Fuyao Zhang, Wenwen He, Jiaming Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) agents increasingly act over streaming omni-modal observations spanning screenshots, audio, video, interaction history, and device states. However, exposing this complete context uniformly at every step ignores that relevance is transient and sparse: the signal determining one action can become clutter at the next. Because executed actions feed back into the context, these errors compound into Sequential Distraction, driving the agent into irreversible trajectory drift. We formulate the underlying requirement as Focused Perception: a representation that is step-adaptive, action-sufficient, and non-intrusive. We realize this in FocusGUI, a lightweight adapter that dynamically prioritizes multimodal channels against a step-specific decision reference. Instead of uniformly processing all inputs, it compresses the most relevant evidence into a compact latent and subtly injects it into the frozen decoder's embeddings, guiding the model's attention without altering its native parameter space. FocusGUI trains from action supervision alone, requiring neither modality-relevance labels nor backbone fine-tuning. Across four omni-modal backbones, it raises overall Type Match by +33.2 and Exact Match by 3.0 times over the frozen backbone on average, and Type Match by +30.1 over the strongest existing enhancement method.

---


### 414. [Signature Knowledge Shielding: Protecting Antivirus Detection Knowledge through Robust Embedding Matching](https://arxiv.org/abs/2610.26207)

**<font color=#1a73e8>作者：</font>** Jieshuai Yang, Zhi Wang, Yan Jia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Antivirus (AV) signatures encode valuable detection knowledge accumulated through expert analysis, yet repeated black-box queries can expose this knowledge for unauthorized reuse and targeted evasion. We propose Signature Knowledge Shielding (SKS), a design paradigm that protects existing AV rules, termed Protected Signatures (PS), through auxiliary Shielding Signatures (SS). SKS uses AV-supervised importance ranking to discover candidate byte blocks, filters and selects them through negative-sample calibration, and combines SS matches with original AV verdicts through logical OR. SS matching introduces additional positive responses and verdict changes during probing, making detection feedback less directly attributable to PS and increasing the difficulty of localizing signature-related content, while preserving original positive verdicts. Within SKS, we integrate five individually tuned non-learning matching methods and further propose Robust Embedding Matching (REM), a lightweight learned matcher trained with random context and byte perturbations. REM provides stronger and more consistent protection against content modifications and scanning-alignment changes. We develop and open-source a ClamAV-based prototype and evaluate it against five probing methods. With an observed additional test false-positive rate below 0.1%, REM raises the mean query count of state-of-the-art probing to as much as 282.57 times the unprotected baseline, while introducing only 0.67% GPU scanning overhead. These results demonstrate that SKS can substantially increase signature-extraction costs with limited impact on detection utility and scanning efficiency.

---


### 415. [OceanTensorCube and ST-MMT: A Multimodal Data and Transformer System for Seven-Day Forecasting of Pyropia Bleaching](https://arxiv.org/abs/2610.26209)

**<font color=#1a73e8>作者：</font>** Gwangjin Kim, Cheolyoung Jang, Yosep Jo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bleaching of cultured Pyropia (laver) causes losses in Korean seaweed farming. We present a system that forecasts bleaching seven days ahead for farm clusters. OceanTensorCube aligns 32 channels from public marine, meteorological, ocean-model and satellite sources on a 30 m grid, and ST-MMT, a 9.2-million-parameter spatiotemporal transformer with hub-style multi-head cross-attention between variable groups, maps a 14-day input window to a seven-day-ahead bleaching probability. On the validation set, a six-seed ensemble detects every reported positive at a false-alarm rate of at most 3.5%, an upper bound because the report-based labels are positive-unlabeled. A same-date control on separately trained models indicates that the architecture discriminates between clusters when the calendar is held fixed. We also report the system's weaknesses: skill falls steeply as the quarterly nutrient survey ages (ROC-AUC 0.94 at 30 days, 0.53 at 129 days), and a single LSTM on cluster-average series outperforms a single ST-MMT, with only the ensemble leading at the operating point. We describe the labeling procedure, the evaluation protocol and the operational gate that withholds forecasts when inputs are stale. The forecasting service is operated at this https URL.

---


### 416. [ExMR: Extremity Motion Refinement for Monocular Human Motion Capture](https://arxiv.org/abs/2610.26213)

**<font color=#1a73e8>作者：</font>** Tom Wehrbein, Bodo Rosenhahn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detailed hand and foot articulation is important for animation and motion analysis, yet remains challenging to recover from monocular video. Recent expressive video methods infer hand articulation from shared whole-body representations. Our conference work suggests that this underexploits local evidence: the Foot Motion Refinement (FootMR) module refines ankle rotations from foot keypoints, improving reconstruction even when the initial estimator receives the same keypoints. We extend this principle to hands with the Hand Motion Refinement (HandMR) module. Because 2D finger keypoints are often missing or unreliable, HandMR combines image features of a pretrained hand reconstruction model with initial arm and hand rotations to refine elbows, wrists, and fingers. We integrate FootMR and HandMR into ExMR (Extremity Motion Refinement), a system for reconstructing 3D body, hand, and foot motion from monocular video. An initial temporal estimator predicts whole-body motion, after which both refiners revisit local evidence to predict residual joint rotations. Experiments on ARCTIC, MOYO, RICH, and MOOF show that ExMR outperforms state-of-the-art methods in hand and foot reconstruction, reducing hand per-vertex error and ankle joint angle error on MOYO by 19% and 18%, respectively, relative to the strongest competitor. Code will be made available for research purposes. Project page: this https URL

---


### 417. [Fairness or Fallacy? Mapping the Landscape of AI Bias in Disease Detection](https://arxiv.org/abs/2610.26215)

**<font color=#1a73e8>作者：</font>** Ghulam Mudassir, Hameed Ullah Khan, Ahmad Sami Al-Shamayleh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) has several transformative effects on healthcare, like to facilitate clinicians in disease detection and to manage patient care with enhanced precision. Due to the increasing complexity of medical data and the growing volume of diagnostic images, the substantial computational power needed to process such information creates both opportunities and challenges. To accomplish this objective, numerous methodologies have been proposed to integrate AI into disease detection systems. All these methodologies consider different aspects of clinical diagnosis, considering key parameters such as the type of AI model employed, the nature of input data, and the population demographics being analysed. In this paper, we review different state-of-the-art techniques which have been proposed for various areas of disease detection, specifically focusing on bias identification and mitigation. The proposed solutions are distinguished based on the type of input data they utilize, the architecture of model, and type of bias (algorithmic bias, demographic bias, model bias, and deployment bias). The time frame chosen to filter out relevant studies is between 2015 and 2026. Eventually, we review 23 related articles out of 64,389 analyzed from seven different digital libraries. The obtained results guide us to reach a conclusion with respect to state-of-the-art selected studies. Furthermore, these results reveal significant research gaps that can assist researchers in addressing AI-related bias in medical diagnosis. By prioritizing explainability, data diversity, and fairness in algorithmic design, as well as equitable access for affected patient populations, they can utilize available healthcare resources more effectively.

---


### 418. [RoAR-VAE: Improving Latent Diffusability through Robust Prediction](https://arxiv.org/abs/2610.26216)

**<font color=#1a73e8>作者：</font>** Yang Yue, Fangyun Wei, Yitong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An effective visual tokenizer must preserve image fidelity while producing latents that downstream diffusion models can learn efficiently. Prior work improves latent diffusability through semantic alignment or joint tokenizer--diffusion training. Revisiting REPA-E, a representative approach, we find that removing its diffusion objective and dedicated generative blocks while retaining semantic prediction from corrupted latents yields comparable downstream generation performance under a matched setting. This observation motivates a general principle of robust prediction: generation-relevant information should remain recoverable from corrupted latents. We instantiate this principle with two complementary objectives. RobustAlign predicts pretrained semantic features from corrupted latents to preserve high-level structure, while RobustRecon reconstructs the clean image to retain fine-grained spatial and appearance information. Together, they form Robust Alignment and Reconstruction VAE (RoAR-VAE). Our analysis suggests that robust prediction improves diffusability by making useful information more accessible in high-variance latent directions, which diffusion models tend to learn earlier. Empirically, RoAR-VAE improves average generation benchmark performance by 2.19 points over the strongest baseline tokenizer under the same training budget, while improving small-text reconstruction accuracy by 16.93 percentage points over FLUX.1-VAE. These results demonstrate that RoAR-VAE achieves a favorable balance between reconstruction fidelity and downstream generative learnability.

---


### 419. [SAR2Net: Learning Spatially Anchored Representations for Retrieval-Guided Cross-Stain Alignment](https://arxiv.org/abs/2610.26217)

**<font color=#1a73e8>作者：</font>** Tianle Shen, Fang Yan, Xiaofan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving spatial alignment between whole-slide images(WSIs) across stains is essential for integrating morphology and molecular information, yet it remains challenging due to extreme resolution, tissue fragmentation, and large nonlinear deformations. Conventional registration pipelines depend on global pre-alignment and spatial consistency, which often collapse under such distortions. We present SAR2Net, a framework that learns spatially anchored representations and reformulates cross-stain alignment as a region-level feature retrieval problem. Instead of estimating explicit transformations, SAR2Net learns pointwise representations encoding the relative spatial relationships to tissue landmarks. Given landmarks and arbitrary coordinates, it predicts spatially anchored features that serve as deformation-invariant descriptors of tissue topology. A twostage retrieval framework then establishes correspondences between slides, even when global alignment is infeasible. Experiments on biopsy-oriented HE-IHC datasets show that SAR2Net achieves robust region-level alignment under severe tissue distortions, outperforming previous methods. Code is available at this https URL.

---


### 420. [Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening in Realtime Voice Agents](https://arxiv.org/abs/2610.26233)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhang, Kewei Fu, Yongqi Tong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-using voice agents often leave users waiting after speech ends, even when actionable information arrives earlier in the request. Speculative approaches begin work during speech, but chunk-bounded or interrupt-on-update generation can truncate a tool call before its arguments are complete. This couples computation time to speech updates, limiting useful work completed in advance. We introduce Heartbeat Thinking, which handles updated input through new Thinker invocations while allowing ongoing invocations and dispatched tools to finish. Periodic invocations read the latest partial transcript and a shared record of completed reasoning and tool results. These results help resolve missing arguments and initiate dependent calls, allowing preparation to progress across speech updates. Across SpeechFCEval, FDBench v3, and AudioCRAG, Heartbeat improves aggregate speculative tool coverage or retrieval reuse over a SHANKS-style windowed baseline, with benchmark-dependent effects on final task quality. On FDBench v3, it increases tool coverage by 16 percentage points and reduces mean final-response latency by 36.4\%. The results show that heartbeat thinking paradigm preserving ongoing computation during speech can turn listening time into reusable preparation for faster and more capable voice-agent responses.

---


### 421. [CoRS: Fast Neural Flexible Job-Shop Scheduling via Composite Interval State Reuse](https://arxiv.org/abs/2610.26239)

**<font color=#1a73e8>作者：</font>** Jiang Sutong, Zhao Peng, Wu Xuan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural solvers for the Flexible Job-Shop Scheduling Problem (FJSP) typically refresh graph representations and update feasibility after every operation--machine decision. However, only feasibility must remain exact at every step, whereas graph encoding is substantially more expensive and can potentially be refreshed less frequently. We present CoRS, which decouples them: an interval-level graph representation is reused across multiple sequential decisions, while a stepwise feasibility state is updated after every action. This two-timescale design amortizes graph encoding without parallelizing action generation or relaxing scheduling constraints. CoRS further develops a feasibility-preserving composite-interval decoding scheme with dynamic constraint tracking and boundary state synchronization, which reduces representation refresh frequency while maintaining continuous feasible schedule construction. Furthermore, to alleviate representation staleness caused by interval-level state reuse, CoRS introduces enhanced static features as a compensation mechanism. By providing more comprehensive structural information of the scheduling problem, these features improve the model's perception of overall problem characteristics. Extensive experiments on synthetic and multiple public FJSP benchmarks demonstrate that CoRS significantly reduces inference time while maintaining competitive solution quality, achieving favorable speed-quality trade-offs under tight wall-clock budgets and low-latency scenarios.

---


### 422. [Q-MALDetect: Quantum Image-Based Malware Detection and Adversarial Robustness Analysis](https://arxiv.org/abs/2610.26240)

**<font color=#1a73e8>作者：</font>** Walid El Maouaki, Mohammad Izen, Nouhaila Innan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantum machine-learning (QML) models are increasingly considered for security applications, yet their adversarial robustness in malware analysis remains insufficiently understood. This paper presents Q-MALDetect, a hybrid convolutional and variational-quantum detector for byte-image representations of x86-64 Executable and Linkable Format (ELF) binaries, and evaluates it under feature-space and a range of Grad-CAM-guided, executable-aware evasion attacks. The model achieves 97.2% training accuracy, but its robustness deteriorates as attack strength increases, with the strongest evaluated feature-space attack reaching a 78.7% attack success rate (ASR). Among executable-aware attacks, Grad-CAM-guided no-operation (NOP) insertion produces the highest conditional ASR of 32.9%. Dynamic adversarial training is the most effective evaluated defense, reducing feature-space ASR to as low as 5.0%, executable-aware ASR to 7.7%, and the sequential-attack ASR to 34.0%. In contrast, convolutional-autoencoder preprocessing increases executable-aware ASR to 39.7%, coinciding with a rise in Grad-CAM attribution mass within the mutable .text region from 35.2% to 45.7%. Ablation results reveal no monotonic relationship between qubit count and robustness, while the encoding interface modifies the learned attack surface without neutralizing the strongest attack. These findings demonstrate that the effectiveness of attacks and defenses depends strongly on the perturbation constraints and evaluation conditions. Reliable deployment of QML malware detectors therefore requires assessment against both feature-space and executable-aware attacks rather than reliance on clean accuracy or generic denoising alone.

---


### 423. [Machina Pauliana: A neuro-symbolic approach to the actio pauliana in Dutch insolvency law](https://arxiv.org/abs/2610.26241)

**<font color=#1a73e8>作者：</font>** Daan Boven, Gregor Behnke, David Graus  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Applying a legal provision frequently requires both structured rule-based reasoning and sensitivity to open-textured terms developed in case law. The actio pauliana of Article 42 of the Dutch Bankruptcy Act (Faillissementswet, Fw), which allows an insolvency practitioner to avoid transactions that prejudice creditors, requires both. We present a neuro-symbolic model of Article 42 Fw. Its symbolic core is written in Catala in a literate style that keeps statute and formalisation aligned and was developed through pair programming, with open-textured terms represented as boolean inputs where neural components couple to the symbolic solver. A neural routine structures a case's natural-language facts into boolean and date inputs. Neural subroutines resolve the open-textured terms through case-based reasoning over Dutch civil judgments, retrieved through a pipeline that filters on the requirement being resolved and expands along the procedural chain of a case. Segmenting and labelling those judgments attains high precision and recall against a manually annotated gold standard of 100 judgments. On ten hand-annotated cases the neuro-symbolic model handles most criteria reasonably but struggles with the knowledge requirement. Retrieval depth shows no clear quantitative effect, although retrieved judgments provide explicit grounding in prior case law.

---


### 424. [RECAP: Reciprocal Sparse Attention and Hierarchical Caching for Efficient Video Diffusion](https://arxiv.org/abs/2610.26244)

**<font color=#1a73e8>作者：</font>** Tiange Xu, Kai Liu, Linghe Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers generate high-quality videos but remain computationally expensive. Sparse attention and temporal caching reduce computation within and across denoising steps, respectively, offering a natural composition. However, predictions produced with sparse attention become sources for temporal reuse, coupling their errors along the sampling trajectory. We observe that improving the accuracy of these sources recovers fidelity without changing the reuse schedule, and that sparsification errors remain directionally aligned across nearby steps, suggesting that correction information can be shared rather than recomputed. These observations motivate RECAP, a training-free method that couples sparse attention with hierarchical caching through reciprocal correction, adaptively coordinated by online error feedback. Cached dense refinement corrects omitted interactions in current sparse estimates, while fresh sparse statistics track input changes and regulate the aging correction. The resulting predictions then renew the sources for whole-step prediction reuse, allowing prediction history to advance between dense refreshes. We evaluate RECAP on multiple video diffusion models against sparse-attention methods, caching methods, and their direct compositions. On HunyuanVideo at 720p 5-second generation, RECAP achieves a 3.05x speedup and outperforms all tested direct compositions in both fidelity and inference speed.

---


### 425. [SEAM: Spectral Embedding Alignment and Merging for Low-Resource TTS](https://arxiv.org/abs/2610.26252)

**<font color=#1a73e8>作者：</font>** Walaa Othman, Baher Mohammad, Stamatios Lefkimmiatis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expanding the vocabulary of conditional text-to-speech (TTS) models typically requires extensive fine-tuning with paired audio, creating a major bottleneck for low-resource and cross-lingual adaptation. To address this, we introduce SEAM, a zero-audio initialization method that constructs embeddings for unseen tokens from known subtokens. Unlike standard pooling strategies that ignore sequential structure, SEAM applies a spectral filter to preserve temporal phonetic order and uses closed-form ridge regression to align the new embeddings with the pretrained conditioning manifold. Across three languages and two TTS architectures, SEAM approaches or matches baseline performance using up to four times less training data, reducing sample complexity by 75\% compared to random initialization and mean pooling. Our approach provides a lightweight, reproducible, and theoretically grounded solution for vocabulary expansion in low-resource speech synthesis.

---


### 426. [LOCU: Lowdin-Orthogonalized Constraint Updates for Multi-Constraint Policy Optimization](https://arxiv.org/abs/2610.26256)

**<font color=#1a73e8>作者：</font>** Joonyoung Lim, Younghwan Yoo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate multi-constraint policy optimization in constrained Markov decision processes (CMDPs), where interactions among constraint gradients often yield ill-conditioned update directions, causing numerically fragile steps and unintended cancellation or redundant overlap in constraint corrections. To address this, we propose LOCU, which mitigates numerical instability arising from constraint interactions by applying symmetric Lowdin orthogonalization to the natural gradients of the reward and constraints under the Fisher-Rao metric. Combined with Fisher-geometric screening and near-collinear compression, LOCU yields a compact reduced space in which the trust region becomes a Euclidean ball and constraints are handled symmetrically through a low-dimensional active-set solve. For infeasible iterates, LOCU constructs a Pareto-descent direction which preserves the local feasibility of satisfied constraints within the same reduced formulation. Experiments show that LOCU remains stable under high constraint coupling, narrow feasible regions, and infeasible starts, and generalizes across different cost critic architectures.

---


### 427. [REFLEX: RNA Ensemble Generation via Flexibility-Calibrated Stochastic Bridge](https://arxiv.org/abs/2610.26261)

**<font color=#1a73e8>作者：</font>** Wanli Ma, Tianmeng Hu, Ke Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> RNA molecules often function through multiple experimentally observed conformational states. A central challenge is to capture ensemble diversity without sacrificing structural fidelity: samples may collapse toward averaged representative structures or drift into unsupported conformational regions. We introduce REFLEX (RNA Ensemble generation calibrated by FLEXibility), a sequence-conditioned generator for RNA backbone-frame ensembles based on a heteroscedastic stochastic bridge on SE(3). During training, experimental B-factors calibrate residue-wise bridge widths, exposing each observed conformer through local perturbation neighborhoods with residue-specific scales while keeping constrained regions sharper. A learned flexibility condition guides the bridge-field network to recover target conformer-specific frames from these calibrated noisy states. At inference, REFLEX uses only the input sequence, requiring no MSA-subsampling heuristics. On a multi-conformer RNA benchmark, REFLEX achieves the best precision-recall trade-off for ensemble coverage across evaluation thresholds, while recovery-stress ablations indicate gains in target-frame recovery under stronger perturbations.

---


### 428. [TIM: Temporal Decoupling with Iterative Mutual-Refinement Model for Longitudinal Radiology Report Generation](https://arxiv.org/abs/2610.26271)

**<font color=#1a73e8>作者：</font>** Yiheng Dong, Yi Lin, Shilong Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic radiology report generation (RRG) aims to translate medical images into diagnostic text, reducing radiologists' workload and standardizing clinical documentation. Nonetheless, existing approaches mainly focus on single-timepoint analysis and fail to capture temporal disease evolution across longitudinal examinations. While recent longitudinal RRG (LRRG) approaches incorporate historical data, they often combine images from different time points within a single representation space, leading to blurred semantics and inconsistent temporal reasoning. In this work, we propose a Temporal Decoupling with Iterative Mutual-Refinement Model (TIM), a two-stage framework that explicitly decouples spatial pathology from temporal progression and iteratively refines reports through mutual feedback. Stage I performs temporal-decoupled representation learning, separating temporal evolution patterns from disease-specific features and generating radiology reports for both prior and current studies. Stage II introduces a mutual report refinement mechanism that identifies diagnostic inconsistencies within prior reports and iteratively rectifies both prior and current reports through error-sensitive feedback. Experiments on the Longitudinal-MIMIC dataset demonstrate that TIM surpasses existing single-image and longitudinal baselines, achieving new state-of-the-art performance across both language and clinical metrics. Code is available at this https URL.

---


### 429. [Bringing physics-based controller policies to virtual reality](https://arxiv.org/abs/2610.26278)

**<font color=#1a73e8>作者：</font>** Joan Llobera, Pierre Nagorny, Balint Hodossy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Nowadays, it is easy to set up any element of a VR experience so users can interact with it physically, except for interactive VR characters. Can we extend this to animated VR characters?
In this work, we studied whether physics-based character animation (PBCA) controllers can produce high-quality movement in VR-compatible environments (Unity3D, WebXR). We evaluated the quality of the results, as well as the losses at each stage of the processing pipeline: data ingest, training and inference. For data ingest, we computed accuracy metrics related to the retargeting method used. For training, we computed accuracy metrics related to different training policies and different training environments. We developed new JAX implementations of state-of-the-art PBCA controllers (DeepMimic, AMP and ADD) which can be trained in MuJoCo-MJX in minutes, 50 times faster than in a traditional CPU-based training environment. The benefit of these particular implementations is that the resulting control policies can be readily transferred to Unity3D and support cross-platform compilation, including Android, something critical for use in VR production. For inference, we tested these controller policies in Unity3D and WebXR. Our results suggest that DeepMimic and ADD trained in MuJoCo-MJX generate controller policies with better animation fidelity than other methods.
To simplify the comparison between controller policies, and different reference animations, we implemented an animation fidelity index (afi). Its results are analogous to other more common metrics, but afi is more intuitive to interpret and thus simplifies the comparison of training methods across the successive stages of the processing pipeline.

---


### 430. [Trust Your Targets: Is Target Propagation Block-Diagonal Gauss-Newton?](https://arxiv.org/abs/2610.26283)

**<font color=#1a73e8>作者：</font>** Giuseppe Castiglione, Christopher Buckley, Ivor Simpson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Target propagation (TP) is a backpropagation alternative in which local targets carry the global learning signal. Prior works claim that TP performs Gauss-Newton (GN) optimisation on these targets, but the correspondence has only been established under unrealistic assumptions where hitting them exactly is trivial. Practical variants instead descend on a least-squares problem via a single gradient step. In this paper, we rederive TP from a trust region under an implicit, previously unexamined norm, and introduce CGTP (Conjugate Gradient Target Propagation), which uses conjugate gradients to solve the layer-local subproblems in parallel. A single adaptive parameter jointly controls this trust region and a matching bound on the weight update; KFAC emerges exactly as the special case where the per-sample Jacobians are replaced by their batch mean, giving its factored damping a variational grounding. On MNIST and Fashion-MNIST MLPs, CGTP matches the accuracy of ADAM and KFAC while needing orders of magnitude fewer outer iterations than ADAM (about 10x fewer backward-pass-equivalents overall), while remaining stable across depth.

---


### 431. [Learning SOCP Solver Dynamics with Graph Neural Networks](https://arxiv.org/abs/2610.26285)

**<font color=#1a73e8>作者：</font>** Adam Ghalem, Lou Salaün, Davide Rinaldi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Second-order cone programs (SOCPs) are a fundamental class of convex optimization problems widely applied across engineering domains. Classical interior-point methods are robust and accurate, but their iterative nature can be costly in real-time or repeated-solve settings. This has motivated learning-based solvers that approximate optimizer solutions with neural networks. Recent work has increasingly studied graph neural networks (GNNs) for linear, quadratic, and second-order cone optimization, leveraging their ability to model sparse relational structure among variables, constraints, and objective functions. Most existing GNN-based solvers compress the optimization process into a single forward pass, predicting the optimizer directly without using the intermediate trajectory produced by classical solvers. We introduce SOCPNet, a recursive GNN framework that uses solver trajectories to learn an iterative SOCP solution procedure. A shared GNN model is applied repeatedly, refining the current iterate at each step and enabling inference for a variable number of iterations. Rather than predicting the solution in a single pass, SOCPNet learns from intermediate iterates to progressively refine its estimates using a trajectory-regularized training procedure. We evaluate SOCPNet on multiple datasets spanning standard SOCP problem classes and show that it consistently reduces the final solution error relative to a SOCP-GNN baseline. Finally, we demonstrate how trained SOCPNet models can be used in a hybrid optimization pipeline by warm-starting a classical interior-point solver, reducing solver iterations without loss of accuracy.

---


### 432. [Toward Online Robust Zero-Sum Markov Games with Function Approximation](https://arxiv.org/abs/2610.26286)

**<font color=#1a73e8>作者：</font>** Chenhao Zhou, Jiyu Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online robust zero-sum Markov games pose a coupled operator-learning and game-solving problem: from nominal interaction data, the learner must recover a worst-case minimax Bellman operator while maintaining strategic coverage and controlling stage-game approximation error. Existing robust reinforcement-learning theory does not yet provide such an operator-learning perspective beyond specialized multi-agent settings. We develop an optimistic dual robust Bellman framework that combines dual robust Bellman fitting, optimistic minimax planning, backward-validated confidence sets, and exploiter-mix data collection. Our analysis is organized around the robust Bellman residuals induced by the candidate value class and yields a regret reduction that separates exploration complexity, robust operator-estimation error, stage-game solution error, and misspecification. Under explicit interpretable assumptions, we obtain conditional theorem interfaces for general and projected function approximation, together with closed results in several structured regimes, including tabular, epochwise cross-fit linear, self-normalized pure-online linear / finite-rank kernel, and projected RKHS truncation. Small-scale numerical experiments illustrate robustness calibration, strategic coverage, and the return-gap trade-off predicted by the framework.

---


### 433. [CAST: Cast-Admissible Generative Design and Shape Optimization with Paired Depth Images](https://arxiv.org/abs/2610.26309)

**<font color=#1a73e8>作者：</font>** Jihoon Kim, Yongmin Kwon, Namwoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep generative design can produce complex geometries, but unconstrained representations may create undercuts that prevent release from a two-part mold. We present CAST, which reformulates three-dimensional shape generation under a selected mold-opening constraint as a two-dimensional image generation problem using paired top and bottom depth images. Each valid depth pair defines one material interval along a selected mold-opening direction, so reconstructions exclude undercuts in that direction by construction. Diffusion models generate candidate shapes in this representation, and a finite element analysis (FEA) guided optimizer refines the same two boundaries. We evaluate diffusion-based generation with limited training data comprising 211 SimJEB bracket designs. On SimJEB brackets, FEA-guided refinement with a volume penalty reduced compliance in 193 of 200 generated candidates. The median reduction across all candidates was 36.8 percent in the optimization FEA model. Reconstruction of existing brackets revealed a mass--stiffness trade-off: filling occluded regions increased material volume and reduced displacement under the evaluated loads. Paired depth images thus connect generative exploration and structural refinement in a shared design space that preserves the selected pull-direction restriction.

---


### 434. [Selective Transfer through Sequence Distillation: From Benchmark Knowledge to Backdoor Behaviour](https://arxiv.org/abs/2610.26311)

**<font color=#1a73e8>作者：</font>** Jonibek Mansurov, Sholpan Bolatzhanova, Filbert Aurelian Tjiaranta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation is widely used to transfer capabilities from teacher models to student models, but recent work shows that it can also transfer unintended teacher properties. We study whether different hidden teacher properties survive the same distillation channels. Specifically, we compare two properties: benchmark-associated knowledge and refusal backdoors, and show that distillation treats them very differently. Teachers fine-tuned on benchmark data successfully pass that knowledge to students through all four distillation channels we test, including when students are trained only on teacher-generated number sequences containing no natural language or domain content whatsoever. Refusal backdoors tell the opposite story: backdoored teachers achieve near-perfect triggered refusal, yet sequence-distilled students inherit essentially none of this behaviour. Logit-based distillation transfers it substantially, reaching up to 85.5\% triggered refusal in students that saw zero backdoor examples. Distillation is therefore selective, and the selection criterion is not what data the student sees, but what structure the teacher's property has. The code is available at this https URL.

---


### 435. [CARNet: End-to-End Coupled Association-Recognition Network for Fine-Grained Multi-Drone Collaborative Detection](https://arxiv.org/abs/2610.26312)

**<font color=#1a73e8>作者：</font>** Zhao Zhang, Ruigang Fu, Yu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-drone collaborative detection aims to enhance target recognition by leveraging complementary observations from overlapping aerial viewpoints. Existing approaches typically follow a two-stage pipeline that first establishes cross-view correspondences and then performs fusion-based recognition. However, this decomposition suffers from inconsistent optimization objectives, redundant pairwise modeling, and irreversible error propagation, where incorrect associations inevitably undermine subsequent recognition performance. To overcome these limitations, we propose the Coupled Association-Recognition Network (CARNet), a unified framework that jointly optimizes cross-view target association and recognition fusion through a shared target-pair representation. To improve association reliability in densely populated scenes with visually similar targets, CARNet explicitly incorporates spatial cues into pairwise relation modeling. Moreover, we introduce two complementary causal-inspired intervention strategies: the first enhances cross-view association by emphasizing appearance-confusing pairs, while the second bolsters the robustness of fusion-based recognition by learning stable multi-view representations under incomplete visual evidence. In addition, we present MDMT-CD, a fine-grained extension of the MDMT dataset that enriches the original vehicle annotations with detailed category labels, providing the first benchmark specifically designed for multi-drone collaborative vehicle detection. Extensive experiments demonstrate that CARNet consistently outperforms existing state-of-the-art methods. The MDMT-CD dataset and source code will be available at this https URL.

---


### 436. [MCDA: Multi-View Graph Contrastive Learning with Dynamic Topology Augmentation for Functional MRI Analysis](https://arxiv.org/abs/2610.26322)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Xiaoyun Liu, Shuo Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Resting-state fMRI (rs-fMRI) is a vital non-invasive tool for diagnosing brain disorders and uncovering pathological mechanisms. However, existing graph contrastive learning (GCL) methods often underexploit augmentation histories across training epochs and the relationships among different augmented views. In this paper, we introduce a topology-guided Multi-view graph Contrastive learning framework with Dynamic graph topology Augmentation (MCDA) for fMRI analysis. Unlike traditional GCL that uses fixed noise or edge-dropping, MCDA employs a Dynamic Augmentation Update (DAU) module that iteratively refines the augmented topology. Specifically, we incorporate self-aware and cross-sample augmentation strategies to simultaneously capture individual-specific functional signatures and inter-subject heterogeneity. We then design a topology-guided multi-view graph contrastive learning scheme that explores interrelationships not only between the original network and its augmented views, but also across different augmented views to maximize structural information preservation. We characterize the score-level optimization directions and establish a lower bound for the contrastive objective. The framework combines classification and contrastive losses for brain disorder diagnosis and examines discriminative functional connectivity patterns as potential biomarkers. Experiments on two public rs-fMRI datasets comprising 1,236 subjects demonstrate that MCDA outperforms the state-of-the-art methods. The code has been made publicly available at: \url{this https URL}.

---


### 437. [TriScore: Post-Hoc Out-of-Distribution Detection with Energy, Boundary Probes, and Transform Consistency](https://arxiv.org/abs/2610.26323)

**<font color=#1a73e8>作者：</font>** Ege Gursoy, Nicolas Mansard  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-hoc out-of-distribution detection usually relies on a single signal extracted from a frozen classifier, such as confidence, energy, features, or gradients. This dependence becomes fragile under classifier-level adversarial shift, where the shift can preserve the detector's chosen cue while changing the model's decision behavior. We investigate whether this failure mode can be mitigated by combining complementary detection criteria instead of selecting a single score. We introduce TriScore, a post-hoc OOD detector that combines three ID-calibrated signals from the same frozen backbone: an energy prior, a boundary-fragility score, and a transform-consistency score. These signals are standardized on ID validation data and fused by an input-dependent ID-residual gate, requiring no OOD labels, auxiliary model, training, or stored feature bank. Across four ImageNet-scale backbones, TriScore achieves the best mean AUROC among 15 post-hoc baselines under a non-adaptive adversarial-shift protocol, while remaining competitive on standard OOD benchmarks. Ablations show that the gains come from combining complementary cues rather than optimizing a single detector signal. These results support multi-criterion post-hoc detection as a practical route toward more robust OOD detection under classifier-level shift. The source code is publicly available at this http URL.

---


### 438. [The Control Layer Behind Rule-Following Agents Trading Across Market Conditions](https://arxiv.org/abs/2610.26324)

**<font color=#1a73e8>作者：</font>** Saad Naja, Nasser Odtallah, Jake Van-Praag 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trading discipline often fails people. Our study tested whether four AI trading agents followed their strategies and risk rules. Offering traders the evidence and an agent evaluation toolkit to separate luck from following the rules, before giving agents meaningful autonomy or capital. Our study analysed 2,627 closed positions from 12 February to 27 August 2026 across the same asset universe and execution conditions. Most positions were simulated against live prices with a 0.09% round-trip fee; 18% involved real Hyperliquid orders. Each position declared a strategy, stop and target, with a limit of five open positions per agent. The fleet finished net positive after fees. Rule adherence was high across all four agents, including the unprofitable one. Profitability tracked how often agents won relative to their break-even win rates. Institutional-style controls ran by default and contained losses through a 29% market drawdown and recovery, with documented exceptions. The discipline held for all four agents. Agents kept 97.5% of gross loss within declared stops, and typical losses closed at declared levels. Declared risk remained stable after losses and broadly stable across calm and volatile months. Twenty-three of 24 runs respected the position limit; logs identify the exception's size and duration. The same live data produced different results across assigned strategies. The trade-log tests can be rerun from the published trade snapshot; regime tests also require the published Bitcoin prices and regime labels. Section 3.5 specifies the stop-breach tolerance. These trade-level results are not account-level returns or proof of a lasting edge. Our study provides an evaluation toolkit to help traders distinguish rule-following from luck before committing capital. For anyone considering allocating capital to agents to trade, discipline should be the entry test, not the only test.

---


### 439. [Fortress: Fork Resistant Transparency logs Relying on Social graph Structure](https://arxiv.org/abs/2610.26327)

**<font color=#1a73e8>作者：</font>** Anastasiia Kucherenko, Melissa Chase, Esha Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Transparency systems -- such as Key Transparency (KT), Certificate Transparency, and binary transparency -- require that all honest participants see the same view of an untrusted server's directory, or, failing that, that the misbehaviour is publicly detected. Every existing design closes this gap with an external trust anchor: a publicly available bulletin board (BB), a blockchain, or an out-of-band (OOB) gossip network among auditors.
We observe that transparency systems already have a built-in resource that has so far been overlooked: the social graph induced by the users themselves. We ask whether it can replace the bulletin board or the external gossip channel entirely, and answer in the affirmative (if occasional out-of-band interactions are allowed).
We formalise a new primitive, Social-Graph based Forking-Resilient Transparency (sg-FORT), which captures the security guarantees of a BB-free transparency system and we construct Fortress Fork Resistant Transparency logs Relying on Social graph Structure, to our knowledge the first such protocol. In every epoch either all users output the same post, or at least one honest user produces a publicly verifiable Proof of Misbehaviour. Our guarantees hold against an arbitrary malicious server, including a snapshot adversary that may compromise a user and learn its secret state, as long as the server does not compromise close users. In honest executions, OOB interactions occur only when a user resets their secrets, so the total OOB cost approaches the natural lower bound of one call per reset -- dramatically below the full-gossip alternative. We prove security under standard cryptographic assumptions on signatures and dictionary commitment. Under simplifying assumptions (synchronous epochs, always-online users), we view this as a first feasibility result that opens up the design space of social-graph-based transparency systems.

---


### 440. [CIS-Transolver: A Cross-Layer Incremental-State Neural Operator for Fine-Scale Automotive Aerodynamic Flow Prediction](https://arxiv.org/abs/2610.26337)

**<font color=#1a73e8>作者：</font>** Jianglong Liu, Zhicheng Zhu, Jia Hao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators offer an efficient data-driven approach to rapid prediction of complex automotive aerodynamic flows. However, spectral bias and other factors limit accurate reconstruction of fine-scale flow variations near complex geometries. Existing studies improve the representation and fitting of fine-scale information mainly through information extraction and training objectives. Further study is needed to determine how extracted local details can be used continually in subsequent operator computations and contribute effectively to the overall flow-field representation. We propose CIS-Transolver, a cross-layer incremental-state neural operator that extends fine-scale modeling from local information extraction to its use across layers. The method extracts fine-scale information through local multiscale analysis and encodes it as geometric moment states that are propagated and updated across layers. By combining information from previous layers with feedback to the value representations in Physics-Attention, the method allows local details to contribute continually to subsequent modeling of global physical correlations. We systematically evaluate CIS-Transolver on three public automotive aerodynamics benchmarks, ShapeNet-Car, AhmedML, and DrivAerNet++, covering surface pressure fields and volumetric pressure and velocity fields. CIS-Transolver achieves the lowest mean relative L2 error among the evaluated methods for all five prediction metrics across the three benchmarks. The relative error reductions average 8.72% across the five metrics compared with the best baseline for each metric, reaching 16.38% for ShapeNet-Car pressure prediction and 15.60% for AhmedML velocity prediction. These results provide a new approach to fine-scale flow prediction for complex geometries.

---


### 441. [SplatXR: A Toolkit for Multi-Layered Extended Reality via On-Headset 3D Gaussian Splatting](https://arxiv.org/abs/2610.26338)

**<font color=#1a73e8>作者：</font>** Cyrus Vachha, Mohamed Kari, Parastoo Abtahi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in Gaussian splatting, 3D foundation models, and video-passthrough mixed reality offer unprecedented fidelity for capturing and blending physical and virtual worlds. However, established XR methods rely on polygon-based pipelines that treat physical and digital environments as separate domains, making seamless integration across recent novel representations difficult. Because splats lack explicit surface geometry, they impede standard graphics techniques necessary for cross-reality interactions, such as shadow or collision handling. Furthermore, while 3D foundation models can reconstruct physical objects on-the-fly into digital splats, current XR systems fall short of leveraging this capability for user experiences that transition seamlessly between physicality and virtuality. To address this, we organize XR as a multi-layered reality of interacting primitives, letting pixels and objects move across physical and digital boundaries. We contribute SplatXR, a Unity toolkit that operationalizes this structure as building blocks for interactive, immersive apps leveraging 3D Gaussian splatting: a standalone renderer, splat-to-mesh reconstruction, splat physics, splat blending, and offloaded splat object reconstruction via on-headset capture. SplatXR unites vision and graphics techniques to make splat-based XR development broadly available, and we validate it through demonstrative applications and a small developer study.

---


### 442. [A Generic On-Board AI Processing Chain for Earth Observation: From Application Development to Embedded Deployment and Mission-Level Orchestration](https://arxiv.org/abs/2610.26340)

**<font color=#1a73e8>作者：</font>** Michel-Fran{\c c}ois Foulon, Liz Ramos Medina, Thomas Goudemant 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Earth observation satellites acquire more data than they can downlink. Extracting information on board with artificial intelligence (AI) turns the satellite into a data-reduction stage that downlinks compact products, such as masks or detections, instead of full scenes; deploying it in a mission, however, involves the whole processing chain and not only the neural network. We present a generic on-board AI processing chain along three axes, with wildfire segmentation as the worked example among ship detection and cloud segmentation. (i) The AI model is tuned (spectral-band selection, input normalization), quantized to 8-bit integers (int8) and ported to an AMD Versal VCK190, with its excellent segmentation performance preserved on the board. (ii) A modular tiler-inference-mosaicer workflow, reused unchanged across applications, brings the tile-level model to scene level, turning a full acquisition into a scene-level mask or detection list. (iii) Each step is packaged as a unikernel and orchestrated on board by ORCHIDE, a cloud-native orchestrator. The chain is characterized end to end, from the standalone execution on the target to its execution under orchestration with parallel workflows on a representative test bench. Beyond AI inference on individual tiles, this approach aims at increasing the maturity of on-board AI deployment by addressing a complete processing chain, from the acquired scene to the mission-level execution.

---


### 443. [CARRS: A Constraint-Aware, Real-Time Routing System for Emergency Vehicles in Urban Environments](https://arxiv.org/abs/2610.26346)

**<font color=#1a73e8>作者：</font>** Vincent Sello, Timothy Adeliyi, Ridewaan Hanslo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emergency vehicles such as police vehicles, fire engines, and ambulances require a stable and efficient route optimization to reach life-critical events in the shortest times possible. However, the dynamic nature of urban traffic makes this ideal scenario much more challenging, causing critical life-threatening delays. Traditional civilian navigation systems cannot account for real-time traffic changes alongside vehicle-specific constraints, creating inadequate routing scenarios. This research presents the Constraint-Aware Real-Time Routing System (CARRS), a unified software architecture tailored for emergency coordination. The CARRS architecture is engineered to fuse together classical pathfinding algorithms such as A*, Dijkstra, and Bidirectional A*, with Constraint Satisfaction Problem methodologies. The Design Science Research Methodology is the research framework, and prototyping is the iterative process. The artifact was empirically evaluated using OpenStreetMap data for major metropolitan road networks, combined with simulated dynamic traffic scenarios. Performance metrics focused on route optimality, constraint adherence, rerouting responsiveness, and the potential for future system scalability. Findings revealed the system's capability to generate optimal routes for operationally relevant subgraphs in under 35 seconds, with incremental rerouting responsiveness below 20 seconds. Furthermore, the system achieved more than 90% adherence to vehicle-specific constraints, making the CARRS architecture viable for real-time dynamic routing requirements. This study delivers a routing platform that bridges artificial intelligence-driven optimization with software engineering operational compliance, presenting a practical transformative step toward adaptive emergency vehicle coordination in dynamic urban environments.

---


### 444. [Logit Averaging During Training Sets a New State of the Art for Non-Invasive Speech BCI](https://arxiv.org/abs/2610.26347)

**<font color=#1a73e8>作者：</font>** Miran Özdogan, Gereon Elvers, Michael Bronstein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-invasive brain-computer interfaces are in practice limited by signal-to-noise ratio, and recent state-of-the-art methods address this limitation by aggregating over repeated trials of the same stimulus. Yet multi-trial aggregation has been treated inconsistently across the literature: some work averages brain signals at the model's input, other work averages predictions at the model's output, and neither treats aggregation as an architectural choice in its own right. We provide the first systematic comparison of aggregation strategies for non-invasive neural decoding, evaluating six paradigms (including logit averaging during training and three attention-based variants we introduce) across three datasets, four tasks, and two group sizes. We find that aggregation choice matters substantially: training-time logit averaging, the simplest method we propose, outperforms all others in 6 of 7 settings. On the phoneme classification setting of the 2025 PNPL competition, it sets a new state of the art, significantly outperforming the competition winner by 17.4 absolute percentage points in balanced accuracy. We further draw a theoretical connection between logit averaging and joint ensemble training, which has been shown to underperform independent ensembling in the deep learning literature; our results call into question recent explanations of why joint ensemble training fails. Together, these findings establish multi-trial aggregation as a key design choice for non-invasive neural decoding and identify training-time logit averaging as a simple, effective default.

---


### 445. [HGASurv: Hierarchical Granularity-Aware Integration for Multimodal Survival Prediction](https://arxiv.org/abs/2610.26357)

**<font color=#1a73e8>作者：</font>** Peike Yu, Wuchao Liu, Jihong Guan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: Multimodal survival prediction jointly analyzes histopathological whole-slide images (WSIs), genomic profiles, and clinical variables to stratify patients by risk. However, existing approaches often inadequately account for granularity differences across modalities, particularly in spatial organization and feature dimensionality. To address these challenges, we propose HGASurv, which introduces a hierarchical WSI encoding module and a clinical-guided graph propagation module for granularity-aware multimodal integration. Methods: The hierarchical WSI encoding module maps WSI patch features onto a spatial grid using their original coordinates and applies parallel convolutions to construct representations at patch, local-neighborhood, and regional scales. Genomic signature embeddings then query these scale-specific WSI representations through cross-modal co-attention, producing signature-conditioned morphological features. The clinical-guided graph propagation module uses clinical variables to define patient-similarity edges and propagates fused image-genomic node embeddings with graph attention, integrating clinical information through topology rather than feature concatenation. Results: Across three TCGA cohorts, HGASurv achieved the strongest overall C-index performance, with ablation studies supporting the complementary contributions of the hierarchical WSI encoding and clinical-guided graph propagation modules. Conclusion and Significance: By introducing hierarchical WSI encoding and clinical-guided graph propagation, HGASurv unifies multi-scale pathology representation with topology-based clinical integration in a hierarchical granularity-aware framework. This design shows that matching representation and integration mechanisms to modality-specific granularity improves multimodal survival prediction.

---


### 446. [Remote Expert Evaluation of Tabletop Avatar Gaze Control in Asymmetric Multi-Scale MR--VR Collaboration](https://arxiv.org/abs/2610.26360)

**<font color=#1a73e8>作者：</font>** Carlos Mosquera, Neven Elsayed, Ernst Kruijff 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper proposes an integrated setup for a multi-scale asymmetric collaboration scenario in the context of a remote-expert use case, focusing on the expert side. In this system, the remote expert (with an exocentric view in Mixed Reality (MR)) uses a Tangible User Interface (TUI) to precisely position and rotate their avatar within a scaled tabletop World-in-Miniature (WIM). Inside the WIM, the expert's avatar and the operator share the same scale and egocentric view, while the expert retains a global tabletop overview of the plant to support collaboration.
Interviews with industry experts during the participatory design phase revealed the need for an egocentric view inside the plant on the remote-expert side to enable full collaboration. We designed and studied three interaction-visualisation combinations to integrate and control the expert avatar's gaze: VR (fully immersive with direct head control), Head (floating screen with direct head control), and Touch (on-avatar screen with touchpad control).
We evaluated these methods with 29 participants across two fault-detection tasks: Same Machine, where both collaborators inspect the same machine, and Twin Machine, where they inspect identical machines in separate locations. The VR condition, which combines immersion, direct head control, and a full-scale view, yielded the strongest overall performance and user experience, while the tabletop avatar setup was well received for collaboration. Our findings inform the design of gaze-control techniques for asymmetric MR-VR collaboration and reveal challenges and opportunities for future work.

---


### 447. [From Tasks to Turns: Measuring Human Labor Contributions in Human-Agent Joint Production](https://arxiv.org/abs/2610.26365)

**<font color=#1a73e8>作者：</font>** Likai Wang, Dezhao Su, Jing Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In agent workflows, a brief human instruction can alter subsequent search, reasoning, and tool execution, yet final task outcomes rarely reveal the contribution of an individual instruction to human-agent joint production. We propose a Human Turn-level framework for measuring human contributions, using task quality and token usage to characterize the collaborative production outcomes associated with each human instruction. We compare continuations from adjacent checkpoints under matched models, budgets, and termination conditions, and assess stability through repeated measurements. Across four archived and simulated interaction settings, we conduct 29,124 comparisons between predicted and observed directions of quality and computational change at both Human Turn and session levels. On HumanBench, we obtain 506 valid comparisons across 85 real-user scenarios. Results show that quality and computational changes associated with human guidance depend on task conditions. Expert-style and ordinary-style guidance differ in information provision, correction, and repetition. Even when task quality after continuation is identical, remaining computational demands can differ substantially across checkpoints. Our framework advances the measurement of human labor contributions from tasks and sessions to individual turns, providing a repeatable, fine-grained foundation for studying human contributions and their allocation in human-agent joint production.

---


### 448. [CTLite: Lightweight Irregular Multivariate Time Series Forecasting with Reusable Continuous-Time Summaries](https://arxiv.org/abs/2610.26379)

**<font color=#1a73e8>作者：</font>** Shusen Ma, Xudong Zuo, Yangchun Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregular multivariate time series forecasting (IMTSF) requires capturing temporal dynamics and cross-variable dependencies from sparse, asynchronous observations. Existing methods often rely on learned temporal encoders, coupling historical representation construction with model optimisation and repeatedly processing the same observations. We propose CTLite, a lightweight forecasting framework that decouples historical summarisation from learned prediction. Specifically, a parameter-free continuous-time moment encoder summarises local levels and trends at multiple temporal scales while suppressing poorly supported slope estimates. A compact readout combines damped local extrapolation with a low-rank cross-variable correction that accounts for observation freshness, target availability, and forecast horizon. Since the historical summaries are independent of trainable parameters and forecast queries, they can be reused across optimisation steps and repeated predictions for an unchanged history without altering predictions or parameter gradients. Experiments on four real-world benchmarks show that CTLite achieves the best or second-best mean MSE and MAE among the evaluated methods with only 88-2,537 trainable parameters. Under matched GPU workloads at batch size 32, CTLite reduces inference latency by 18.6-87.3% compared with the latest models, including the cost of historical encoding. Reusing summaries further reduces total runtime by approximately 52% over 16 forecast calls on the same history compared with recomputing the encoder for every call, including the initial encoding cost. The code is at: this https URL.

---


### 449. [From Legacy to Contemporary: Scalable Color Modernization for Long Videos](https://arxiv.org/abs/2610.26391)

**<font color=#1a73e8>作者：</font>** Dongyun Kim, Jiwoo Choi, Jaeseong Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bringing legacy video back to contemporary screens does not necessarily make it look contemporary. Earlier imaging pipelines often leave color casts, muted chroma, weak con- trast, and tonal imbalance, while correcting these character- istics still relies heavily on expert colorists and scales poorly to long, multi-shot videos. We formulate long video color modernization, a task that updates the chromatic and tonal appearance of legacy color footage while preserving scene content and coherence across frames and shots. We introduce a scalable, training-free framework that jointly modernizes grids of temporally adjacent keyframes using a pretrained text-guided image editing model, producing coherent con- temporary references without paired supervision. Compact shot-specific color transforms then propagate these adjust- ments throughout each shot, preserving spatial structure and temporal stability. We conduct a multidimensional evaluation on diverse legacy videos spanning five decades. We combine a human evaluation of perceived modernness with quantita- tive measures of content fidelity, temporal stability, percep- tual quality, and efficiency, and introduce Source-Weighted Inter-shot Grade Consistency (SW-IGC) to assess grade co- herence across shots. On our evaluation set, our frame- work achieves the highest perceived modernness while re- maining competitive across complementary measures, open- ing a path toward the systematic study of long video color modernization. Code is available at this https URL this http URL

---


### 450. [One Fact, Many Places: Redundant Evidence in Long Visual Documents Breaks Single-Gold Evaluation of Retrieval, Citation and Attribution](https://arxiv.org/abs/2610.26401)

**<font color=#1a73e8>作者：</font>** Xiaokang Yuan, Binhui Yao, Luwei Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document understanding is increasingly judged on where an answer comes from, scored against annotated gold locations as if each fact lived in one place. In long visual documents, a fact often lives in several places: a chart value is restated in the text, a key figure reappears in the summary. We ask how often such copies occur in standard benchmarks and what they do to evaluation. We annotate 420 questions from MMLongBench-Doc and MMDocRAG with the locations that independently establish each required fact, checked by two independent reviewers. Copies are common and often cross-modal: 19.5% of MMLongBench-Doc test questions have a strict copy outside the gold, and in 28% of MMDocRAG questions a non-gold candidate alone supplies a required fact. Single-gold scoring then fails in three predictable ways. A retriever that finds a copy is scored as a miss: page recall@1 of text and visual retrievers is underestimated by 13-24 points on questions with a cross-page copy. A model that cites a copy is scored as citing wrongly: crediting equivalent evidence reverses 11% of pairwise orderings among 65 competitive MMDocRAG systems. Masking the gold region leaves the fact available elsewhere: with a copy in the input, 41-56% of correct answers across four models survive it yet fail once every annotated instance is masked. Set-level masking with automatically found copies closes 78% of the gap to masking every annotated instance at matched granularity (three models); an unverified key-string rule lowers survival at least as far but masks three times the area. We release the annotations and redundancy-aware metrics.

---


> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-534](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
