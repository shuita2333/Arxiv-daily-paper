# 📦 其他研究 | 2026年07月10日

> 本类共 **207** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-207](./part-05.md)

---

### 51. [Head, Gaze, or Finger? Comparing Object Selection Techniques in Augmented Reality for People with Low Vision](https://arxiv.org/abs/2607.06778)

**<font color=#1a73e8>作者：</font>** Ruijia Chen, Tianyi Zhang, Sanbrita Mondal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmented reality (AR) can enhance visual perception for people with low vision (PLV) by overlaying multimodal information. Selection-based augmentation further allows users to flexibly choose and augment relevant information while reducing distraction and visual clutter. However, little is known about the ability and preferences of PLV in performing object selection techniques in AR, considering their potential visual and gaze control challenges. To understand what selection techniques are suitable for PLV to support selection-based AR augmentations, we conducted a mixed-methods study with 20 PLV and 18 sighted controls who performed target selection tasks using three input techniques -- head, gaze, and finger pointing with dwell-based confirmation -- in two real-world scenarios (sitting vs. on the go). We found that for PLV, gaze-based selection enabled the fastest initial pointing when sitting and comparable overall selection time to head-based selection in both scenarios; however, due to reduced gaze stability, head-based selection remained the most stable and the least mentally demanding. Uniquely, participants with central vision loss preferred finger-based selection, reporting a greater sense of control. Our results provide empirical insights into accessible AR interaction techniques and selection-based vision enhancements for PLV.

---


### 52. [URS-Stereo: Uncertainty-Guided Residual Search for Real-Time Stereo Matching](https://arxiv.org/abs/2607.06779)

**<font color=#1a73e8>作者：</font>** Pouya Sohrabipour, Chaitanya kumar reddy Pallerla, Dongyi Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time stereo matching is crucial for robotics, autonomous systems, and embedded vision applications, where both computational efficiency and disparity accuracy are required. Recent coarse-to-fine stereo matching methods improve efficiency by progressively refining disparity estimates using local cost volumes at higher resolutions. However, these methods rely heavily on the accuracy of propagated disparity estimates from previous stages. When the propagated disparity is inaccurate, the ground-truth correspondence may fall outside the predefined local search range, leading to unrecoverable matching failures during subsequent refinement. In this paper, we propose URS-Stereo, a real-time coarse-to-fine stereo matching framework that addresses this limitation through uncertainty-guided search adaptation. Specifically, we introduce an Uncertainty-Guided Residual Search Module (UGRSM), which predicts the reliability of propagated disparities together with residual search offsets to adaptively relocate the centers of local cost volumes before disparity refinement. By dynamically adjusting the search region according to the confidence of the propagated disparity, the proposed method significantly improves the robustness of local correspondence estimation while preserving the computational efficiency of coarse-to-fine stereo matching. Extensive experiments on SceneFlow, KITTI 2012, KITTI 2015, Middlebury, and ETH3D demonstrate that URS-Stereo consistently improves disparity estimation while maintaining real-time inference speed, validating the effectiveness of the proposed uncertainty-guided search strategy

---


### 53. [On Explicit Super-Expressive Approximation for Neural Networks](https://arxiv.org/abs/2607.06781)

**<font color=#1a73e8>作者：</font>** Feng-Lei Fan, Ze-Yu Li, Chen-Yu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we investigate the fixed-architecture neural network approximation with explicit parameter bounds and elementary activations. While prior work demonstrated super-expressive approximation using fixed-size networks, they lack quantitative and non-asymptotic characterizations of parameter magnitude with respect to the approximation error. We resolve this issue by introducing the Chinese Remainder Theorem as a constructive encoding mechanism. For Lipschitz continuous functions on $[0,1]^D$, we construct a width-$\max\{D,4\}$, depth-$5$ network with explicit parameter-error trade-offs. For Hölder-smooth functions in $C^{r,\gamma}_A\left([0,1]^D\right)$, our fixed network of width $\max\{2D,\ D+5N+1\}$ and depth $r + 9$ achieves the parameter magnitude $\mathcal{P}$ bounded by $\log_2 \mathcal{P}=\mathcal{O}\bigl(\varepsilon^{-2D/(r+\gamma)}\log(1/\varepsilon)\bigr)$. This is the dual result compared to those in the parameter-bounded and architecture-unbounded paradigm.

---


### 54. [Enhancing deep learning models for time series classification via knowledge distillation](https://arxiv.org/abs/2607.06796)

**<font color=#1a73e8>作者：</font>** Javidan Abdullayev, Maxime Devanne, Jonathan Weber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has achieved remarkable success in various domains including time series analysis, computer vision and natural language processing. However, high computational and memory demands of state-of-the-art architectures pose challenges for deployment in resource-limited environments. Knowledge Distillation (KD) addresses this by transferring knowledge from a large teacher model to a smaller, more efficient student model while maintaining competitive performance. In this work, we investigate the effectiveness of KD for Time Series Classification (TSC) across three architectures: the classical Fully Convolutional Network (FCN), the convolutional Inception model and the transformer-based ConvTran model. We evaluate our approach on UCR Archive, the largest benchmark repository of time series datasets, by modifying architectural components such as convolutional filters, Inception modules and attention heads across the three architectures. Our results consistently show that KD most effectively benefits student models of intermediate complexity across all three architectures, with the distilled FCN student reducing parameters by a factor of 38, the distilled Inception student achieving nearly the same performance as the teacher with 42% fewer parameters and the distilled ConvTran student with 2 attention heads showing the most significant improvement through distillation. To encourage further research and reproducibility, we provide our implementation at this https URL.

---


### 55. [ECO/CPO-DAG: A Contradiction-Based Accountability Layer for Adversarial Supply Chains](https://arxiv.org/abs/2607.06804)

**<font color=#1a73e8>作者：</font>** Sebastian Cochinescu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present ECO/CPO-DAG, a domain-specific accountability protocol for adversarial supply chains that formalizes contradiction detection as a supplemental validation layer rather than a consensus or truth-establishing mechanism. Participants publish signed Event Claim Objects (ECOs) into a causally ordered, append-only directed acyclic graph (DAG) whose edges encode happened-before relations. When two claims about the same subject violate a domain constraint, any observer can compile a Contradiction Proof Object (CPO), a self-verifying object binding the two signed claims and the violated rule, which, on public verification, triggers economic slashing of a determinately blamed party. We map constraints to GS1 EPCIS 2.0 event semantics (spatial uniqueness, temporal monotonicity, quantity conservation, quality monotonicity, regulatory validity), so detection targets inconsistencies that are meaningful in practice. Selective disclosure via commitment schemes and, optionally, zero-knowledge contradiction proofs lets parties withhold claim contents until a challenge forces the minimal opening. We give an analytical treatment: an independent-observer detection model $1-(1-p_{\min})^h$, a deterrence condition $S>g(1-p)/(kp)$ under $k$-party collusion, and a storage estimate of order 1 GB per participant per year under stated assumptions. The protocol's boundary is explicit: it detects provable contradictions, not consistent lies; a party that never contradicts itself is invisible to it, so the layer complements, and does not replace, source verification and oracle aggregation. A single-machine reference implementation corroborates the detection model, with the predicted coverage band overlapping the measured 95% confidence interval at every observer count, and records zero false accusations; the fully zero-knowledge CPO, multi-party propagation, and adaptive-adversary evasion remain analytical.

---


### 56. [When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems](https://arxiv.org/abs/2607.06807)

**<font color=#1a73e8>作者：</font>** Haowen Xu, Xue Tan, Lei Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While enabling effective collaboration on complex tasks, LLM-based Multi-Agent Systems (MAS) face critical security challenges due to vulnerabilities at the agent and interaction levels. Most existing MAS security defenses are built upon two core assumptions: semantically-explicit malicious attacks and explicit graph-based modeling of the MAS topology and agent-level interactions. In practice, real-world attacks are becoming more semantically stealthy, while MAS execution is typically asynchronous without the temporal alignment assumed by graph-based propagation models. To address these limitations, we propose AcMAS, an activation-based framework for malicious-behavior detection in MAS. By analyzing internal reasoning states in the activation space of local agents, AcMAS detects even stealthy attacks in a synchronization-robust fashion, without relying on explicit interaction graphs. Moreover, our activation analysis provides critical signals to guide AcMAS in restoring the functionality of compromised agents, rather than the disruptive agent isolation commonly used by the state-of-the-art methods. Comprehensive evaluation demonstrates that AcMAS significantly outperforms graph-based baselines against stealthy attacks, by +0.22 F1 in synchronous settings (0.94 vs. 0.72) and by +0.55 F1 in asynchronous settings (0.93 vs. 0.38), with generalization across diverse open-source LLM backbones, attack intensity, and MAS scale.

---


### 57. [Rail Track Extraction from Rasterized Classified Point Clouds Using a Full-Resolution, Fully Convolutional Recurrent Neural Network](https://arxiv.org/abs/2607.06829)

**<font color=#1a73e8>作者：</font>** Alexander Gribov, Jie Chang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rail track extraction is essential for effective railway asset management and maintenance, especially in automated inspection and mapping workflows. This paper introduces a novel method for extracting rail tracks from classified 3D point clouds using a fully convolutional recurrent neural network that preserves full spatial resolution and is trained exclusively on synthetically generated data. This approach enhances per-pixel quality and is particularly suited for rail track extraction. The proposed method begins by rasterizing points corresponding to railroad tracks, then applies the neural network to reduce noise and yield a cleaner track representation suitable for vectorization [1]. Subsequent morphological operations further refine the resultant data, enabling accurate track centerline extraction. Next, the extracted centerlines undergo smoothing to eliminate residual irregularities [2, 3]. Finally, the algorithm transfers 3D information from lidar points onto 2D polylines and applies additional vertical smoothing. A single centerline for both tracks is found using the Dynamic Time Warping (DTW) algorithm [4]. The final outcome consists of rail top centerlines and track centerlines derived for rail pairs, with minimal manual intervention. Experimental validation confirms the effectiveness of this method in yielding high-quality rail track extraction.

---


### 58. [Generative Diffusion Models of Stochastic Graph Signals](https://arxiv.org/abs/2607.06833)

**<font color=#1a73e8>作者：</font>** Yiğit Berkay Uslu, Samar Hadou, Sergio Rozada 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling stochastic signals supported on a graph underlies many graph machine learning tasks, including recommender systems, forecasting in financial markets, and wireless network optimization. In these settings, the target signals are realizations of unknown conditional distributions. However, prevailing approaches rely mostly on intricate, application-tailored designs that often regress to a conditional mean instead of sampling from the conditional law. This paper unifies such problems as conditional graph signal generative modeling and tackles them with a single denoising diffusion framework. We learn a reverse diffusion process, parametrized by graph neural networks (GNNs), that draws graph signals conditioned directly on the graph topology and on node-feature side information. The reverse process is realized by a novel architecture, the U-Graph Neural Network (U-GNN), which generalizes the image-convolutional U-Net to graph-structured signals. The U-GNN performs multi-resolution encoder--decoder processing in which pooling and unpooling reduce to a learned node selection, expressed by nested selection matrices, and a zero-padded lifting of coarse signals back to the full node set. The graph convolutions are carried out on the original graph, with a stride that sets their hop reach, so the U-GNN bypasses explicit graph coarsening at every resolution. We demonstrate our method on two generative tasks: stock price forecasting and optimal wireless resource allocation, with extensive numerical results in both domains.

---


### 59. [WildCity: A Real-World City-Scale Testbed for Rendering, Simulation, and Spatial Intelligence](https://arxiv.org/abs/2607.06838)

**<font color=#1a73e8>作者：</font>** Xiangyu Han, Mengyu Yang, Jiaqi Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans can navigate an unfamiliar city and gradually form a coherent spatial mental map spanning tens of square kilometers. Can AI build spatial representations at a comparable scale? Although recent foundation models have advanced scene reconstruction and embodied intelligence, scaling to entire cities remains an open challenge, primarily due to the lack of city-scale data. To bridge the gap, we introduce WildCity, a real-world multimodal dataset collected by autonomous fleets traversing complex urban environments. Our dataset includes 18 trajectories, each averaging 83.7 kilometers in length, and preserves the core challenges of in-the-wild perception, e.g., dynamic objects, lighting variations, and imperfect camera poses. We further establish an urban-tailored reconstruction baseline and convert the reconstructed environments into a closed-loop simulator. Beyond the dataset and baseline, we systematically analyze the key challenges on the path to simulation-ready urban digital twins: scalability, extrapolation, and uncertainty. Ultimately, WildCity aims to catalyze progress not only in city-scale rendering, but more broadly in the pursuit of AI that can perceive, remember, and reason across space at a scale comparable to human cognition. Project page: this https URL

---


### 60. [Retrieving and Refining Winning Noise Tickets for Diffusion-Based Motion Generation](https://arxiv.org/abs/2607.06843)

**<font color=#1a73e8>作者：</font>** Sakuya Ota, Qing Yu, Kent Fujiwara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based text-to-motion models synthesize realistic human motions but often exhibit semantic drift from the input text. Motion is inherently temporal, especially in compositional and long-duration sequences that require semantic consistency across multiple action segments and smooth kinematic transitions throughout the trajectory. We posit that the initial noise is central to this consistency: within the Gaussian noise space, certain instances, i.e. winning noise tickets, carry latent structure that biases denoising toward particular motion semantics, even under null prompts. We propose WInning Noise Retrieval and Optimization (WINRO), a training-free, model-agnostic framework that improves text-motion alignment by selecting and refining such tickets before diffusion sampling. WINRO maps random noises to motion features generated under null prompts, retrieves the best-aligned noise for a given text, and refines it via a KL-regularized objective that reduces the residual semantic gap while preserving the Gaussian prior. An optional LoRA-based adapter amortizes this refinement into a single forward pass. WINRO consistently improves text-motion fidelity across different base models, MDM and MotionLCM, on HumanML3D without retraining, improves temporal robustness on the MTT benchmark, and generalizes to applications such as motion stylization and spatial constraint satisfaction.

---


### 61. [A Gold-Standard Study of What Makes a Lightweight Game-Playing Agent Strong](https://arxiv.org/abs/2607.06854)

**<font color=#1a73e8>作者：</font>** Nima Kelidari, Mohammadsaeed Haghi, Mahdi Salmani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning agents for imperfect-information card games are only as strong as the opponents they train against, and they are hard to grade, since they beat a random opponent over 99 percent of the time and only tie copies of themselves. So we build a strong, fixed, rule-based expert for Gin Rummy and use it only as a yardstick, never for training. It beats every agent we trained 70 to 99 percent of the time. Across more than a hundred runs, we isolate what makes a lightweight agent stronger. Trust region updates, a well-aimed reward, a curriculum of tougher opponents, warm starting, and keeping the best checkpoint all help, and stacking them lifts a self-play champion from about 30 to 36 percent against the expert. Several ideas did not pay off. Short-term and longer-term reward shaping, learned state embeddings, imitation and DAgger, and a live large language model opponent were each unhelpful, too slow, or too heavy to train at scale. Comparing MLP, convolutional, set-based, attention, and recurrent encoders shows that extra capacity does little to break the ceiling, suggesting the limit is information rather than network size. We add standard baselines (neural fictitious self-play and information set Monte Carlo search) and confirm the approach carries over to Leduc Hold'em, where the optimum is computable. The result is a lightweight, game-agnostic recipe that trains competitive agents without training on the expert, for any game a small model can handle, reported with robust statistics and released as a reusable package.

---


### 62. [Gen4U: Unifying Video Generation and Understanding via Diffusion](https://arxiv.org/abs/2607.06856)

**<font color=#1a73e8>作者：</font>** Michael King, Aravindh Mahendran, Matthew Koichi Grimes 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prior work suggests that diffusion representations capture low-level geometry but struggle with high-level semantics. We demonstrate that state-of-the-art video diffusion models overcome this limitation. By systematically probing their intermediate activations using recent mutual-kNN alignment metrics, we reveal a highly structured latent space where visual representations evolve across both network depth and noise levels. We show that while moderate noise levels yield linearly separable global semantics, fine-grained details persist at lower noise levels but become spatially scattered, requiring attention mechanisms to decode. Building on these insights, we introduce Gen4U (Generation for Understanding), a framework that repurposes these generative representations with a single forward pass. Our experiments establish that frozen, large-scale video diffusion models function as highly competitive video encoders across a wide spectrum of tasks, spanning semantic and non-semantic objectives (video classification, depth estimation, camera pose estimation, image and video captioning). Bypassing fine-tuning, Gen4U unifies the generation and understanding paradigms, achieving strong perception performance while fully preserving the model's ability to generate high-quality video.

---


### 63. [Auditable Machine Unlearning for Privacy-Compliant Ransomware Detection Using Multi-Shard SISA and Deep Reinforcement Learning](https://arxiv.org/abs/2607.06860)

**<font color=#1a73e8>作者：</font>** Jannatul Ferdous, Rafiqul Islam, Md Zahidul Islam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware poses an escalating cybersecurity threat as attackers continuously modify behavioral patterns to evade static defenses. Although existing machine learning-based detectors often achieve strong predictive performance, they generally assume fixed training data and do not support the selective removal of previously learned samples. This limitation conflicts with privacy regulations such as the GDPR and CCPA, which require the removal of sensitive user data upon request. To address this challenge, we propose an auditable ransomware detection and unlearning framework that integrates deep reinforcement learning with multi-shard SISA retraining. In the proposed system, a Double Deep Q-Network (DDQN) learns a reward-guided detection policy from behavioral features under asymmetric security costs, while multi-shard SISA enables privacy-compliant selective sample removal through shard-level retraining. The framework was evaluated using four criteria: utility preservation, oracle-based forgetting validation, membership inference auditing, and computational efficiency. On a balanced Windows 11 behavioral dataset comprising 2,000 samples and 103 features, the baseline DDQN detector achieved an F1 score of 0.9925 and an AUC of 0.9983. The experimental results show that single-shard unlearning maintains minimal utility degradation and low oracle disagreement, whereas moderate shard counts (M = 5-10) provide the best efficiency-performance trade-off, reducing retraining time to 5-30 s compared with 80-330 s for full retraining. In addition, the membership inference scores remain close to 0.5 across most configurations, indicating limited privacy leakage after unlearning. These findings demonstrate that a privacy-compliant ransomware detection framework can jointly achieve high detection performance, auditable deletion verification, and efficient sample removal.

---


### 64. [Geometric Collapse: When Vision Models Fail to Verify Physical Causality](https://arxiv.org/abs/2607.06871)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Jinhu Qi, Weiqiang Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in large-scale self-supervised learning has improved dense geometric prediction, but it remains unclear whether such scaling yields inference-time physical plausibility checks. We propose Scrambled Edges, a controlled counterfactual that injects salient edge-like cues while violating surface continuity, illumination coherence, and occlusion ordering. With energy-matched and structure-matched controls, we isolate the effect of unsupported edge evidence from high-frequency energy and edge sparsity. Across CNN/ViT/SSL depth predictors on NYU Depth v2 and KITTI, Scrambled Edges induce up to 3.2x larger deviation from clean predictions than energy-matched noise; additional diffusion and flow-matching depth estimators show attenuated but still significant collapse. The resulting Geometric Collapse propagates globally: even with oracle knowledge of the corrupted region, output-level repair recovers only 47%, with substantial error outside the mask. These findings provide controlled behavioral evidence that current dense predictors lack reliable mechanisms to quarantine physically unsupported edge cues, motivating explicit plausibility scoring and selective cue integration.

---


### 65. [Ensemble Deep Learning Approaches for AI-Altered Video Detection](https://arxiv.org/abs/2607.06872)

**<font color=#1a73e8>作者：</font>** Laiba Khan, Hung-Mao Wu, Wei Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The increasing accessibility of artificial intelligence has led to a rapid rise in AI-generated videos, making it more difficult to distinguish between real and manipulated content. Many existing detection methods rely on a single model and often struggle to generalize across different types of deepfakes. In this work, we developed a multimodal deepfake detection system that combines both audio and visual analysis using an ensemble of models. The system includes AASIST for audio-based detection, and EfficientNet, XceptionNet, and MesoNet for analyzing visual features in video frames. The pipeline takes a video as input, separates the audio, and extracts face frames using MTCNN. Each model produces a score indicating the likelihood of the input being fake. These scores are then combined using ensemble strategies, including mean averaging and stacking. Mean fusion provides a simple and stable baseline, while stacking uses a trained meta-model to learn how to combine predictions more effectively. Results show that while individual models perform well on the datasets they were trained on, their performance drops when tested on more diverse datasets. The ensemble approach helps improve overall robustness by combining predictions from multiple models, leading to more consistent performance across different types of deepfakes. This suggests that using both audio and visual information together is a more reliable approach for deepfake detection. Our results highlight generalization to unseen manipulations as the central open challenge, with average accuracy around 70%.

---


### 66. [Video2Reaction: Mapping Video to Audience Reaction Distribution in the Wild](https://arxiv.org/abs/2607.06875)

**<font color=#1a73e8>作者：</font>** Trang Nguyen, Sidong Zhang, Shiv Shankar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding and forecasting audience reactions to video content are crucial for improving content creation, recommendation systems, and media analysis. To enable audience reaction prediction and other content engagement applications, we introduce $\textbf{Video2Reaction}$, a multimodal dataset that maps short movie segments to a distribution of $\textit{induced emotions}$ of viewers in the wild, as expressed through social media. $\textbf{Video2Reaction}$ spans more than 10,000 videos and serves as a reliable benchmark as well as a training resource for audience reaction prediction. To enable cost-effective continuous annotations as reactions may change over time, we develop a two-stage multi-agent pipeline using only open-source LLMs, achieving 86% correctness under blind human verification despite the inherently noisy and subjective nature of the task. We establish the first benchmark for video-to-reaction-distribution prediction in the wild and show that pretrained foundation video models fail in zero-shot settings, while finetuning transforms them into state-of-the-art predictors capable of modeling both full reaction distributions and dominant responses from video alone. However, the task remains challenging: even the strongest methods achieve only 77% Top-3 F1 in dominant reaction prediction (LLaVA-Next), highlighting a substantial gap in modeling collective audience reaction. \modification{Dataset and code are available at our project page: this https URL

---


### 67. [Best-Arm Identification with Generative Proxy](https://arxiv.org/abs/2607.06879)

**<font color=#1a73e8>作者：</font>** Tianyi Ma, Hanzhang Qin, Ruihao Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Best-arm identification is a canonical model for data-driven decision-making, but in many applications each reward observation is costly. Motivated by the growing availability of cheap predictions from machine learning and large language models, we study fixed-confidence best-arm identification in which each costly reward pull is paired with a cheap but correlated proxy score. The marginal mean of the proxy can be estimated offline and is treated as known, whereas its correlation $\rho$ with the reward, which governs how much the proxy helps, is unknown and must be learned online in pair with real rewards. We show that a control-variate adjustment turns this model into a heteroscedastic identification problem whose oracle sample complexity improves by residual variance $1-\rho^2$. The central difficulty is that the correlation must be learned from the same costly samples that identification consumes online, and that a plug-in estimate of the residual variance is anti-conservative and can compromise correctness. We propose PROBE (PRoxy OLS for Best-arm Exploration), a phase-elimination algorithm that directly maintains an upper certificate on the residual variance with an ordinary least squares fit, whose exact chi-square law keeps the certificate valid regardless of the unknown correlation. We prove that PROBE is $\delta$-PAC and attains the known-correlation oracle sample complexity up to a constant multiplicative factor and a constant additive calibration cost. The guarantee extends to the $(\epsilon,\delta)$-PAC setting under minimal changes to the algorithm. Numerical experiments on synthetic instances and on an auto-loan pricing replay with large language model and tabular proxies confirm that the sample savings of PROBE scale with the strength of the reward-proxy correlation, exactly as the theory predicts.

---


### 68. [SA-DRL: Security-Aware Deep Reinforcement Learning for Ransomware Detection with Asymmetric Reward Design](https://arxiv.org/abs/2607.06880)

**<font color=#1a73e8>作者：</font>** Jannatul Ferdous, Rafiqul Islam, Md Zahidul Islam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware detection is a security-critical task in which false negatives and false positives have unequal operational consequences. Conventional machine learning detectors often use symmetric objectives that penalize missed ransomware detections and benign false alarms equally, although a false negative can cause irreversible encryption, operational disruption, and high recovery cost, whereas a false positive is usually reversible. This study proposes a Security-Aware Deep Reinforcement Learning (SA-DRL) framework that embeds false-negative and false-positive cost asymmetry into the reinforcement learning reward signal to prioritize missed-detection reduction. The framework also introduces a Security-Optimal Model Selection (SOMS) criterion and an adaptive episode-level sample-ordering mechanism. Four deep reinforcement learning agents, DQN, DDQN, PPO, and A2C, were evaluated using a symmetric baseline reward (R1) and a security-aware asymmetric reward (R2). Experiments used four discount factors, five-fold cross-validation, and three random seeds, resulting in 480 training runs on a balanced ransomware detection dataset. The SOMS criterion selects models by prioritizing false-negative rate, followed by F1-score and training time. Results show that asymmetric reward shaping improves security-oriented detection performance. The SOMS-selected configuration, DDQN with R2 and gamma = 0.1, achieved a false-negative rate of 0.0080, an F1-score of 0.9915, and an AUC of 0.998, reducing missed detections by 67.6% compared with the best supervised baseline. Across all configurations, R2 reduced the mean false-negative rate by 43% relative to R1. These findings show that reward-function design is important for security-sensitive ransomware detection.

---


### 69. [Converge to Surprise: Evolutionary Self-supervised Image Clustering](https://arxiv.org/abs/2607.06887)

**<font color=#1a73e8>作者：</font>** Canlin Zhang, Xiuwen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most self-supervised image clustering models, actually almost all deep learning approaches, are based on gradient descent: In order to calculate the loss, every optimization step requires a clearly defined target, whether a contrastive split, a masked patch or entity, an EMA-teacher output, a pseudo-label, or a differentiable information-theoretic functional. We propose a self-supervised framework that drops this requirement for image clustering. Without any prior knowledge, we have to assume that each pixel is i.i.d. according to the Principle of Maximum Entropy. Taking this as our null hypothesis H0, we define a "surprise score" that measures how unlikely the model's output representation would be under H0. Maximizing the surprise score forces the deep learning model to reject H0 - equivalently, to discover non-random feature from data. Also, here is our fundamental assumption: a surprise score cannot, in general, be reduced to a per-step loss. Hence, we propose the "converge-to-surprise" scheme to optimize our model: an evolution-strategy (ES) outer loop, which directly maximizes the surprise score without needing its gradient, paired with a periodic gradient-descent inner loop, which uses the surprising clusters already discovered by ES as surrogate targets. On standard image benchmarks, our framework achieves new state-of-the-art results in non-parametric self-supervised image clustering - the strictest deep-clustering setting, in which the number of ground-truth classes is not given to the model.

---


### 70. [ReMoDEx: A Local-to-Global Relevance-Based Model Decision Explainability Framework for large-Scale Image Datasets](https://arxiv.org/abs/2607.06889)

**<font color=#1a73e8>作者：</font>** Abhay Kumar Pathak, Mrityunjay Chaubey, Manjari Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning image classifiers achieve strong predictive performance yet remain opaque in how decisions are formed. A model may predict correctly while relying on irrelevant cues, shortcut associations, peripheral structures, or device level artifacts instead of task relevant regions. On large scale datasets this opacity is especially problematic, since inspecting heatmaps one sample at a time cannot scale to thousands of predictions. We propose Relevance Based Model Decision Explainability (ReMoDEx), a framework for systematic, dataset scale assessment of model decision behaviour in image classification. ReMoDEx defines a stepwise pipeline: model inference, target class selection, relevance map generation, heatmap standardisation, similarity based grouping of patterns, cluster level interpretation, and spatial relevance assessment. Local methods GradCAM++, Integrated Gradients, Occlusion Sensitivity, and Layerwise Relevance Propagation are each combined independently with a single global module that summarises an entire set of relevance maps into a few decision strategy clusters, replacing sample by sample inspection with an automatic, scalable summary. To demonstrate ReMoDEx, we applied it to a VGG16 based classifier distinguishing COVID-19, Normal, Lung Opacity, and Viral Pneumonia. The classifier showed stable performance (86.27% test accuracy, 0.9624 test AUC). However, each explainer combined with the global module consistently produced two recurring strategies: central thoracic region decisions and border/corner sensitive decisions, indicating possible shortcut learning that conventional metrics could not reveal. Masked image validation confirmed that model confidence and predicted class changed when central or peripheral regions were occluded. ReMoDEx thus provides a scalable relevance based decision assessment framework and an essential complement to accuracy based evaluation.

---


### 71. [New Cross-Sensory Approach to Designing Restorative Virtual Environments](https://arxiv.org/abs/2607.06901)

**<font color=#1a73e8>作者：</font>** Rachel Masters, Francisco Ortega  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual reality (VR) nature immersion is an increasingly popular field of research due to its potential to help people who do not have access to real nature. There are many questions surrounding how virtual forests can be designed to effectively reduce stress and restore attention. Many of these questions relate solely to visual aspects, but more recent literature has started exploring multisensory experiences. In these experiences, senses are treated as additive; however, certain results from the current literature may indicate that there are more complex, cross-sensory interactions occurring. For example, adding sound to visuals can increase stress reduction potential, but certain natural sounds can feel threatening if they are out of place within the virtual nature scene. Overall, cross-sensory interactions in VR nature environments (VNEs) are underexplored and challenge our current understanding of multisensory VNEs, and future explorations of these interactions are essential for designing optimal VNEs for stress reduction.

---


### 72. [Seeing What Matters: Lesion-Aware High-Resolution Patch Discovery and Fusion for Chest X-ray Report Generation](https://arxiv.org/abs/2607.06909)

**<font color=#1a73e8>作者：</font>** Yingshu Li, Yunyi Liu, Zhenghao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid advances in chest X-ray (CXR) foundation models, most radiology report generation (RRG) systems still rely on heavily downsampled inputs (e.g., 256x256) due to the fixed visual token budgets of pretrained vision encoders, suppressing subtle yet clinically important cues present in native-resolution images. However, enabling high-resolution (high-res) perception remains challenging: naive tiling causes prohibitive token inflation, while global compression suppresses subtle lesions and degrades diagnostic fidelity. Inspired by radiologists' workflow, localizing suspicious regions before detailed high-res assessment. We propose Lesion-Aware High-Resolution Patch Discovery and Fusion for Chest X-ray Reporting (LePaX), the first RRG framework that enables efficient high-res CXR perception (up to 1920x1920) without increasing the vision-token count. LePaX formulates high-res perception as a constrained spatial resolution allocation problem under a fixed token budget and introduces two key components: Learnable Spatial Resolution Allocation (LSRA), which learns a spatial utility map that adaptively allocates limited high-res capacity to diagnostically relevant regions, enabling targeted extraction of high-res patches from native CXRs; and Global-Regional Fusion (GRF), which performs token-preserving region-to-global refinement by projecting high-resolution regional evidence back onto the global feature grid through spatially aligned resolution write-back, avoiding token inflation. Experiments on multiple CXR benchmarks demonstrate that LePaX consistently improves both clinical and linguistic metrics while enabling native-resolution CXR perception with over 10x fewer visual tokens than naive high-res tiling.

---


### 73. [Smart Scissor: Coupling Spatial Redundancy Reduction and CNN Compression for Embedded Hardware](https://arxiv.org/abs/2607.06915)

**<font color=#1a73e8>作者：</font>** Hao Kong, Di Liu, Shuo Huai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling down the resolution of input images can greatly reduce the computational overhead of convolutional neural networks (CNNs), which is promising for edge AI. However, as an image usually contains much spatial redundancy, e.g., background pixels, directly shrinking the whole image will lose important features of the foreground object and lead to severe accuracy degradation. In this paper, we propose a dynamic image cropping framework to reduce the spatial redundancy by accurately cropping the foreground object from images. To achieve the instance-aware fine cropping, we introduce a lightweight foreground predictor to efficiently localize and crop the foreground of an image. The finely cropped images can be correctly recognized even at a small resolution. Meanwhile, computational redundancy also exists in CNN architectures. To pursue higher execution efficiency on resource-constrained embedded devices, we also propose a compound shrinking strategy to coordinately compress the three dimensions (depth, width, resolution) of CNNs. Eventually, we seamlessly combine the proposed dynamic image cropping and compound shrinking into a unified compression framework, Smart Scissor, which is expected to significantly reduce the computational overhead of CNNs while still maintaining high accuracy. Experiments on ImageNet-1K demonstrate that our method reduces the computational cost of ResNet50 by 41.5% while improving the top-1 accuracy by 0.3%. Moreover, compared to HRank, the state-of-the-art CNN compression framework, our method achieves 4.1% higher top-1 accuracy at the same computational cost. The codes and data are available at this https URL

---


### 74. [Compass: Prostate Cancer Detection Needs Multi-View Context](https://arxiv.org/abs/2607.06919)

**<font color=#1a73e8>作者：</font>** Paul F.R. Wilson, Mohamed Harmanani, Zhuoxin Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) analysis of micro-ultrasound ($\mu$US) has shown promise for prostate cancer (PCa) detection. However, most existing AI methods focus on the analysis of single $\mu$US images in isolation. By contrast, expert $\mu$US readers typically assess a full recorded video study, which provides three-dimensional context, to improve PCa detection compared to single-frame analysis. Inspired by this clinical workflow, we propose Compass, a novel AI methodology which models a $\mu$US study as a stream of 2D images. Compass jointly integrates rotational sweep videos of the prostate with $\mu$US frames acquired at the moment of biopsy, and performs evidence aggregation across the study using a transformer conditioned on the probe's rotational angle. Finally, a decoder head predicts frame-level and study-level risk scores for the patient. The model is trained and evaluated using a multi-center clinical trial dataset of $\mu$US studies, including continuous rotational scans of the prostate and videos captured during biopsy acquisition. We compare the proposed method to baseline AI methods from the literature and to risk scores provided by clinical experts. Our framework shows strong performance, highlighting the value of multi-view context for $\mu$US PCa detection, and providing a potentially powerful tool to complement human expertise in $\mu$US-based PCa diagnosis. Our code is available at: this https URL.

---


### 75. [Latency-Constrained DNN Architecture Learning for Edge Systems using Zerorized Batch Normalization](https://arxiv.org/abs/2607.06922)

**<font color=#1a73e8>作者：</font>** Shuo Huai, Di Liu, Hao Kong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning applications have been widely adopted on edge devices, to mitigate the privacy and latency issues of accessing cloud servers. Deciding the number of neurons during the design of a deep neural network to maximize performance is not intuitive. Particularly, many application scenarios are real-time and have a strict latency constraint, while conventional neural network optimization methods do not directly change the temporal cost of model inference for latency-critical edge systems. In this work, we propose a latency-oriented neural network learning method to optimize models for high accuracy while fulfilling the latency constraint. For efficiency, we also introduce a universal hardware-customized latency predictor to optimize this procedure to learn a model that satisfies the latency constraint by only a one-shot training process. The experiment results reveal that, compared to state-of-the-art methods, our approach can well-fit the 'hard' latency constraint and achieve high accuracy. Under the same training settings as the original model and satisfying a 34 ms latency constraint on the ImageNet-100 dataset, we reduce GoogLeNet's latency from 40.32 ms to 34 ms with a 0.14% accuracy reduction on the NVIDIA Jetson Nano. When coupled with quantization, our method can be further improved to only 0.04% drop for GoogLeNet. On the NVIDIA Jetson TX2, we compress VGG-19 from 119.98 ms to 34 ms and even improve its accuracy by 0.5%, and we scale GoogLeNet up from 20.27 ms to 34 ms and achieve higher accuracy by 0.78%. We also open source this framework at this https URL

---


### 76. [Bi-PT: Bidirectional Cross-Attention Point Transformers for Four-Chamber Heart Reconstruction from Sparse Cardiac MRI Data](https://arxiv.org/abs/2607.06923)

**<font color=#1a73e8>作者：</font>** Chenchuhui Hu, Shaoming Pan, Leon Axel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Bi-PT, a pipeline for reconstructing 3D four-chamber human heart meshes from clinical sparsely sampled cardiac magnetic resonance imaging (CMR) data. This work addresses the error-prone generation of 3D cardiac shape from a sparse point cloud (SPC) extracted from 2D long-axis and short-axis views used in routine clinical CMR protocols. Bi-PT enables accurate inference of the four-chamber heart mesh from the SPC by learning robust point features via bidirectional point cross-attention between an atlas and the SPC, together with per-point semantic labels that improve correspondence estimation. We formulate the deformation field as a Neural Ordinary Differential Equation (NODE) parameterized by a per-point affine transformation and translation to deform the atlas toward the target heart shape. By learning such a NODE, we can guarantee the deformation field to be a locally affine diffeomorphic deformation. We also integrate a semantic label loss into the Chamfer distance to encourage label-consistent correspondences and add a smoothness regularization to stabilize and improve the learning of the deformation field. Extensive experiments demonstrate that Bi-PT achieves accurate and robust performance compared to baselines.

---


### 77. [Intrinsic-Noise Consolidation: A Doob-Barrier-Conditioned Diffusion Turns Analog Device Noise into a Continual-Learning Resource](https://arxiv.org/abs/2607.06924)

**<font color=#1a73e8>作者：</font>** Gunner Levi Howe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On analog neuromorphic hardware, intrinsic device noise is normally an accuracy tax. We ask whether it can instead consolidate memories. We cast per-synapse consolidation as a Doob h-transform: condition each weight's stochastic dynamics on never crossing a memory-critical barrier around its consolidated value. The conditioned diffusion gains an extra drift sigma^2 d/dw log h, a restoring force amplified by the noise variance itself that diverges at the barrier. We are explicit about novelty: the anchored drift -s(w-mu) our rule also contains is not ours (the limit of OUA, MESU, and EWC), and we surrender it. We claim only the conjunction of (a) the Doob barrier-conditioning as a synaptic rule, to our knowledge unclaimed (every h-transform use we found is generative modeling, none synaptic), and (b) a falsifiable prediction: increasing intrinsic noise non-monotonically improves sequential-task retention, an inverted-U that anchored-drift methods cannot produce. We pre-registered this as a go/no-go gate; it passes. On single-head Split-MNIST (8 seeds) the rule lifts retention 10.9 points at an interior optimum (paired Wilcoxon p=0.004), while matched OU/EWC/MESU anchors are monotone. Ablating the conditioning removes the effect; the optimum tracks the barrier; the inverted-U survives a second task stream and the realization where noise enters the forward pass. We then measure the intrinsic noise on real BrainScaleS-2 silicon (additive, trial-to-trial independent, tunable via on-chip averaging) and run the rule on the chip with its noise in the training loop: barrier-conditioning retains a prior task 15.6 points better than the matched control at matched average accuracy, a stability-plasticity shift, not a net-accuracy win (single seed; retention measured, energy modelled). Intrinsic analog noise thus becomes a consolidation dividend a digital accelerator must spend energy to generate.

---


### 78. [Imputation Meets Clustering: Exploiting Latent Subgroup Structure for Missing Data Recovery](https://arxiv.org/abs/2607.06930)

**<font color=#1a73e8>作者：</font>** Chuyao Zhang, E Li, Taochen Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Missing data is prevalent in practical applications, making effective imputation an essential preprocessing step for downstream analysis. Real-world datasets often exhibit complex latent structures composed of multiple subgroups with distinct distributions. However, existing methods often overlook such population heterogeneity. Without explicit structural guidance, these methods tend to produce generic estimates that blur subgroup boundaries and lack instance-level fidelity. While incorporating subgroup information offers a remedy, it faces a circular dependency: reliable subgroup identification requires complete data, while data completion is the imputation objective itself. To resolve this, we propose CAGI (Cluster-Aware Generative Imputation), a framework that reformulates clustering and imputation as a mutually reinforcing co-optimization process. CAGI employs a ``Partition-Guide-Restore'' strategy where dynamic cluster assignments act as local priors to condition a Generative Adversarial Network. An iterative feedback loop is established to progressively refine both cluster structures and imputed values toward faithful subgroup distributions. To ensure distributional stability, CAGI further employs a multi-level optimization objective combining instance-level reconstruction with distribution-level regularization. Extensive experiments on 14 benchmark datasets with 15 representative baselines demonstrate the superiority of CAGI. The source code is available at: this https URL

---


### 79. [Self-Supervised Pretraining Improves Cross-Site and Cross-Scale Robustness of Point Cloud Leaf-Wood Segmentation](https://arxiv.org/abs/2607.06948)

**<font color=#1a73e8>作者：</font>** Heeju Mun, Tackang Yang, Yunsoo Nam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The accuracy of existing leaf-wood segmentation methods for tree point clouds varies across forest types and sites. Self-supervised learning (SSL) on point clouds has improved the generalization of deep learning models for forestry point cloud tasks, including biomass regression and individual tree segmentation, but its applicability to leaf-wood segmentation remains untested. In this study, we pretrained Point-M2AE, a widely used SSL architecture for point clouds, on ShapeNet-55 augmented with 2,400 individual tree point clouds. For fine-tuning and inference, we used recursive voxel subdivision to handle the wide variation in point density across inputs, allowing the same model to operate at both individual-tree and plot scales without architecture change. Compared to the model without pretraining, the pretrained model improved wood IoU from 60.5% to 70.0% for needleleaf and from 69.7% to 76.3% for broadleaf trees. On a benchmark spanning four countries across three climatic zones, the pretrained model achieved the smallest cross-site variation and highest overall performance among compared methods (LeWos, CWLS, and PointTransformer). Plot-level segmentation maintained accuracy comparable to individual-tree performance, with mIoU of 84.7% for broadleaf and 77.7% for needleleaf plots, showing that the model generalizes across scales without additional finetuning. As a downstream test in tropical forests, where dense canopies make segmentation challenging, we applied our model and a quantitative structure model to estimate wood volume for 28 trees from Guyana, Indonesia, and Peru to assess whether the segmentation improvements from SSL pretraining translate into improved downstream performance. The resulting volume estimates achieved the lowest error among all methods tested (MAE = 2.40 m$^3$), less than half that of algorithmic baselines (LeWos: 5.94 m$^3$; CWLS: 5.27 m$^3$).

---


### 80. [SpiS-GAN: Spiral-Modulated Handwriting Synthesis with Star Operation](https://arxiv.org/abs/2607.06949)

**<font color=#1a73e8>作者：</font>** Nguyen Duy Hieu, Dang Hoai Nam, Pham Hoang Giap 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training robust handwriting recognition (HTR) systems requires massive amounts of annotated data, which is often difficult to acquire. While synthetic handwriting generation offers a practical solution to expand training sets, existing models struggle with several core issues. First, previous approaches, even MLP-based models fail to effectively trace cursive handwriting due to fixed-grid spatial receptive field. Second, their CNN-relied discriminators usually lose structural details through aggressive downsampling, making broken connections difficult to detect. Third, existing architectures are either limited to linear feature interactions or too expensive for high-resolution synthesis. Finally, existing approaches lack explicit edge constraints, often resulting in blurred stroke boundaries. To address these challenges, this study proposes a Spiral-Modulated Handwriting Synthesis framework based on Generative Adversarial Networks (SpiS-GAN). Our generator employs Star-Spiral Blocks combining proposed Modulated Elliptical SpiralFC with the star operation to capture spatial relationships and efficiently follow complex handwriting stroke trajectories, while a Spiral-Modulated discriminator is introduced for multi-domain flaws detection. Additionally, we introduce a Sobel-Regularized Edge Reconstruction Loss that provides edge guidance, ensuring every character remains clear and legible. Evaluations on the English and Vietnamese datasets demonstrate that SpiS-GAN significantly outperforms current state-of-the-art models. The generated images are highly authentic, accurately preserve the original writer's style across languages, and successfully lower error rates when training downstream HTR systems.

---


### 81. [HPR-SAM: Hierarchical Probabilistic Representation Learning for Prompt-free SAM-based Medical Image Segmentation](https://arxiv.org/abs/2607.06972)

**<font color=#1a73e8>作者：</font>** Yingzhen Hu, Yiheng Zhong, Keying Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt-free adaptation of the Segment Anything Model (SAM) has emerged as a promising paradigm for automatic medical image segmentation. Existing methods mainly focus on prompt generation, while overlooking that prompt quality is fundamentally constrained by the expressiveness of anatomical representations. However, deterministic prototypes or semantic tokens are insufficient to jointly capture global anatomical priors, intra-structure diversity, and local structural reliability. To address this limitation, we propose the Hierarchical Probabilistic Representation (HPR) framework, which learns complementary anatomical representations through Distributional Anatomical Representation (DAR), Multi-component Anatomical Representation (MAR), and Local Reliability Representation (LRR), and integrates their predictions via Hierarchical Prediction Fusion (HPF) while remaining compatible with the original SAM decoder. Experiments on the Synapse, LA, and PROMISE12 datasets demonstrate that HPR-SAM achieves state-of-the-art performance on Synapse and the best performance under few-shot settings on LA and PROMISE12, validating the effectiveness of the proposed hierarchical probabilistic representation learning framework for prompt-free medical image segmentation. Code is available at this https URL.

---


### 82. [Hybrid Least Squares/Gradient Descent Methods for MIONets](https://arxiv.org/abs/2607.06976)

**<font color=#1a73e8>作者：</font>** Jun Choi, Chang-Ock Lee, Minam Moon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose an efficient hybrid least squares/gradient descent (LSGD) method for MIONets to accelerate training. This method generalizes the LSGD method for DeepONets. Since MIONet is the sum of the entrywise product of multiple branch networks and a trunk network, it can be viewed as a multilinear function with respect to the last layer parameters of each branch network. These sets of parameters can be optimized using the alternating least squares method, where we solve the LS system for a single branch network in turn. To handle the large-sized system matrix, we introduce Kronecker and Khatri-Rao products and tensor permutation matrices to factor the large matrix into small ones. Our method is compatible with a general type of $L^2$ loss with regularization terms for the last layer parameters of each branch, where linear operators can be applied to the MIONet output in each loss term.

---


### 83. [Robust Federated Learning Under Real-World Client Churn](https://arxiv.org/abs/2607.06979)

**<font color=#1a73e8>作者：</font>** Dhruv Garg, Neha Lakhani, Debopam Sanyal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables training shared models on private, on-device data, but production deployments remain constrained to slow, multi-day refresh cycles due to the complexity of coordinating massive client populations. For applications such as feed ranking, ad targeting, and personalized recommendation, model freshness: the ability to rapidly adapt to new user-local data is critical for maximizing objectives like click-through rate. This lag leaves models stale and unresponsive to volatile data distributions driven by viral trends and shifting user intent. Bridging this gap requires addressing three challenges overlooked by existing FL systems: transient client availability, dynamic data heterogeneity, and delays between model predictions and observable outcomes. We present FeLiX, an FL orchestration framework that minimizes wall-clock time-to-target accuracy on live interaction streams. FeLiX introduces three primitives: (i) streaming-aware availability tiers that leverage lightweight telemetry to identify ready clients at scale; (ii) fresh-utility selection, a dual-tier mechanism that prioritizes statistically valuable updates from devices able to meet tight refresh deadlines; and (iii) informativeness-aware, delay-robust aggregation that incorporates late, high-value updates containing ground-truth outcomes without biasing the global model toward stale distributions. Unlike prior systems that rely on unrealistic oracular knowledge of client availability, FeLiX achieves near-oracular performance in real-world settings. Across CIFAR-10, Google Speech, and realistic low-availability traces, FeLiX reduces wall-clock time-to-target accuracy by up to 2.37X while reducing communication bandwidth by 1.30X compared to state-of-the-art synchronous and asynchronous FL baselines.

---


### 84. [EdgeCompress: Coupling Multidimensional Model Compression and Dynamic Inference for EdgeAI](https://arxiv.org/abs/2607.06982)

**<font color=#1a73e8>作者：</font>** Hao Kong, Di Liu, Shuo Huai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks (CNNs) have demonstrated encouraging results in image classification tasks. However, the prohibitive computational cost of CNNs hinders the deployment of CNNs onto resource-constrained embedded devices. To address this issue, we propose EdgeCompress, a comprehensive compression framework to reduce the computational overhead of CNNs. In EdgeCompress, we first introduce dynamic image cropping (DIC), where we design a lightweight foreground predictor to accurately crop the most informative foreground object of input images for inference, which avoids redundant computation on background regions. Subsequently, we present compound shrinking (CS) to collaboratively compress the three dimensions (depth, width, and resolution) of CNNs according to their contribution to accuracy and model computation. DIC and CS together constitute a multidimensional CNN compression framework, which is able to comprehensively reduce the computational redundancy in both input images and neural network architectures, thereby improving the inference efficiency of CNNs. Further, we present a dynamic inference framework to efficiently process input images with different recognition difficulties, where we cascade multiple models with different complexities from our compression framework and dynamically adopt different models for different input images, which further compresses the computational redundancy and improves the inference efficiency of CNNs, facilitating the deployment of advanced CNNs onto embedded hardware. Experiments on ImageNet-1K demonstrate that EdgeCompress reduces the computation of ResNet-50 by 48.8% while improving the top-1 accuracy by 0.8%. Meanwhile, we improve the accuracy by 4.1% with similar computation compared to HRank, the state-of-the-art compression framework. The source code and models are available at this https URL

---


### 85. [Physics-guided spatiotemporal neural models for fuel density prediction](https://arxiv.org/abs/2607.06999)

**<font color=#1a73e8>作者：</font>** Tolga Caglar, Jaynil Jaiswal, Saqib Azim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a physics-guided machine learning (PGML) framework for fuel density prediction, integrating physics constraints and domain knowledge into deep learning models to enhance model accuracy and stability. We explore three deep learning architectures -- ConvLSTM, Adaptive Fourier Neural Operator (AFNONet), and Video Vision Transformer (ViViT) -- to model the spatiotemporal evolution of fuel density. Our approach incorporates differentiable physics-informed terms in the loss function, including a mass-conserving fuel transport term and a rate-of-spread estimation. Experimental results, averaged across multiple independent trials, demonstrate that the proposed PGML framework outperforms purely data-driven baselines without physics constraints in both accuracy and stability. This framework enables computationally efficient, physically plausible fire forecasting to support adaptive prescribed burn management.

---


### 86. [Gimitest: A Comprehensive Tool for Testing Reinforcement Learning Policies](https://arxiv.org/abs/2607.07029)

**<font color=#1a73e8>作者：</font>** Dennis Gross, Quentin Mazouni, Helge Spieker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) policies can be unsafe and vulnerable to attacks. Ensuring their reliability is often a pain point as existing automated testing methods target only selected environments, testing scenarios, and RL algorithms. To address this, we propose a comprehensive framework for testing single- and multi-agent RL policies under varying conditions. Our implementation of this framework, Gimitest, is an open-source tool that supports various gym frameworks and allows for modifications of their integrated components. This article describes the framework and details Gimitest's functionality and architecture. It showcases its effectiveness in testing multiple RL policies in environments such as the official Farama Gymnasium and PettingZoo.

---


### 87. [Gauge-Invariant Learnable Spectral Positional Encodings for Directed Graphs via Hermitian Block Krylov Subspaces](https://arxiv.org/abs/2607.07032)

**<font color=#1a73e8>作者：</font>** Jiaqing Xie, Yuxin Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectral positional encodings (PEs) for \emph{directed} graphs face two obstacles: magnetic Laplacians require an $O(n^3)$ Hermitian eigendecomposition per potential, and their complex eigenvectors are defined only up to unitary gauge, which prior work handles with basis-invariant architectures. We propose learnable spectral PEs of the form $h_\theta(A_q)\,R$, where $A_q$ is a normalized magnetic operator, $h_\theta$ a learnable scalar spectral response, and $R$ a block of random probes. Because the PE is a \emph{matrix function} of the operator, it is gauge-invariant by construction. We compute it in a Hermitian block Krylov subspace from sparse matrix--vector products only, prove that $k = O(\log(1/\varepsilon))$ block steps suffice uniformly over heat--resolvent response families, and give a covering-number argument for why low-dimensional structured families generalize where free per-eigenvalue weights overfit. On a directed SBM whose symmetrization is uninformative by construction, direction-blind PEs stay at chance while magnetic Krylov PEs converge to the exact-eigendecomposition oracle as the depth grows. The same probes yield gauge-invariant pairwise features with $1/\sqrt{s}$ Monte-Carlo error, and the undirected $q{=}0$ case improves heterophilous benchmarks over no-PE and polynomial baselines.

---


### 88. [Intrinsic Green's Learning: Supervised Learning on Manifolds via Inverse PDE](https://arxiv.org/abs/2607.07034)

**<font color=#1a73e8>作者：</font>** Alexandre Quemy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Intrinsic Green's Learning (IGL), a framework that models a target function on a manifold as the solution to a linear PDE whose source term is learned from data. Rather than approximating the target directly, IGL learns a source and integrates it against a Green's kernel. An encoder discovers a low-dimensional coordinate chart on the manifold where both the source and the kernel decompose as low-rank tensors, collapsing a high-dimensional integral into independent one-dimensional integrals with cost linear in the intrinsic dimension. A two-stage algorithm separates coordinate discovery from source fitting, a near-convex linear solve, preventing the dimensional collapse of joint training. Learnable gates on each coordinate automatically discover the intrinsic dimension of the manifold. We validate IGL on synthetic manifolds and on MNIST, where it simultaneously achieves near-optimal classification and automatic recovery of the intrinsic dimension.

---


### 89. [On the Principles of Deep Feedforward ReLU Networks](https://arxiv.org/abs/2607.07035)

**<font color=#1a73e8>作者：</font>** Changcun Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The architecture of deep feedforward neural networks is ubiquitous in deep learning, either as a whole system or as a subnetwork of other architectures, and thus its mechanism is a key ingredient of the black box of neural networks. On the basis of the simplest two-layer ReLU network, this paper systematically studies the mechanism of deep feedforward ReLU networks with multiple hidden layers and successfully explains the training solution obtained by the back-propagation algorithm. The concept of a path, especially in terms of the relationships between paths, plays a central role in uncovering the mystery of the black box. It is shown that a unit of a deep ReLU network can form a piecewise linear manifold to divide the input space, instead of a hyperplane of the two-layer case. How to efficiently use the hidden-layer units to produce both linear functions and partitions of the input space is also a central problem. The principles of a two-layer ReLU network can be generalized to the deeper case to a large extent, such as multiple strict partial orders and continuity restriction. The combination of the basic and simple principles proposed can yield complicated instantiations including the training solutions, and in this sense the black box of deep feedforward ReLU networks is revealed.

---


### 90. [TRACE-Seg3D: Counterfactual Context Auditing For Robust 3D Glioma Segmentation Under Institutional Shift](https://arxiv.org/abs/2607.07038)

**<font color=#1a73e8>作者：</font>** Nguyen Linh Dan Le, Nguyen Pham Hoang Le, Tran Dang Khoi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation models can achieve strong benchmark performance while remaining sensitive to scanner, protocol, and institutional variation. These context shifts alter image appearance without changing the underlying lesion, allowing models to exploit nuisance cues that Dice and HD95 fail to expose. We present TRACE-Seg3D, a counterfactual context auditing framework for robust 3D medical image segmentation. TRACE-Seg3D preserves lesion-relevant evidence and systematically varies imaging context to quantify prediction stability under controlled context shifts. The framework pairs each segmentation with audit evidence for context sensitivity and anatomical plausibility, enabling case-level reliability assessment beyond overlap-based evaluation. Experiments on BraTS and UTSW glioma segmentation benchmarks demonstrate competitive in-distribution and cross-domain performance. TRACE-Seg3D also exposes context-sensitive failure modes missed by conventional metrics. These results establish counterfactual context auditing as a practical route toward transparent and reliable 3D medical image segmentation under distribution shift. Our code is available at this https URL.

---


### 91. [Measuring Intelligence Beyond Human Scale](https://arxiv.org/abs/2607.07040)

**<font color=#1a73e8>作者：</font>** Jerry Han, Rafael Moschopoulos, Ella Colby 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How can we measure intelligence beyond human capability?
Human-authored benchmarks saturate, and above human capability, examiners may not know which tasks are both hard and verifiable. We argue that this difficulty is inherent to absolute-scale evaluation and propose a new paradigm based on relative measurement in which models generate public challenges that separate other systems. Aggregating these outcomes yields an adversarial psychometric rating system that can scale with the systems being measured. We describe practical protocols that reduce incentives for private-information attacks, support judge-free adjudication, and naturally scale with agent capabilities. We instantiate the framework across verifiable and open-ended, non-verifiable domains, illustrating how model-generated evaluation can continue to measure systems beyond the human frontier.

---


### 92. [An Automated Framework for Generating Stealthy Cell-Embedded Hardware Trojans](https://arxiv.org/abs/2607.07049)

**<font color=#1a73e8>作者：</font>** Raghul Saravanan, Sudipta Paria, Sai Manoj P D 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware Trojans (HTs) pose significant threats across the Integrated Circuit (IC) design lifecycle because they can be inserted by untrusted entities at different stages under the zero-trust model. When triggered under rare conditions, HTs can compromise the functionality, reliability, or security of the fabricated chip. HT assessment is typically performed by modeling realistic Trojan insertion scenarios in RTL implementation or gate-level netlists. While this model is useful for evaluating detection methods, it does not capture attacks where malicious behavior is hidden inside standard-cell implementations from a compromised library supplied by an untrusted vendor. This paper presents a novel framework for automatically generating cell-embedded hardware Trojans using compromised standard-cell implementations. Our proposed framework analyzes a mapped design, identifies candidate cell instances with rare input conditions, and applies payload templates that corrupt the selected cell output only when the trigger condition is satisfied. Experiments on open-source combinational and sequential benchmark designs show that our proposed framework can generate valid and stealthy Trojan instances across different cell types and design sizes. The results highlight a critical gap in current Trojan detection assumptions and show the need for cell-aware validation of standard-cell implementations in zero-trust IC design flows.

---


### 93. [Making Implicit Preservation Intent Explicit in Conversational Image Editing](https://arxiv.org/abs/2607.07051)

**<font color=#1a73e8>作者：</font>** Soomin Han, Jihyung Ahn, Bumsoo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conversational image editing requires preserving not only visible content, but also content that temporarily disappears across turns. When newly added or modified content occludes a previously visible region, that region should reappear if it was never semantically changed. However, existing systems often fail to recover such occluded-but-unchanged content, producing inconsistent or hallucinated results. We introduce OCCUR-Bench, a diagnostic benchmark for temporal preservation in conversational image editing. OCCUR-Bench provides diverse occlusion-and-revelation scenarios with historical restoration references, enabling evaluation of faithful restoration rather than plausible regeneration. We also propose ReSpec, a training-free framework that makes implicit preservation explicit by pairing restoration-aware instructions with historical visual references. Given an editing history, ReSpec identifies what should persist, selects the historical image state that provides missing visual evidence, and conditions an in-context editor on the resulting instruction and reference image. Experiments show that ReSpec improves restoration fidelity and temporal consistency on OCCUR-Bench, highlighting the need to ground preservation in editing history rather than only the current image.

---


### 94. [Complexity-Budgeted, Interaction-Aware Interpretable Model for Tabular Data](https://arxiv.org/abs/2607.07060)

**<font color=#1a73e8>作者：</font>** Srikumar Krishnamoorthy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inherently interpretable classifiers for tabular data typically rely on sparse features, rules, or patterns that users can inspect directly. The marginal feature-screening step common to these methods can discard variables whose predictive value emerges only through joint configurations with other variables. We present Interaction Aware Interpretable Machine Learning (IAIML), a framework that addresses this limitation through three coordinated mechanisms: adaptive per-feature discretization, finite-grid pairwise interaction scoring, and a partitioned explanation budget. Detected interactions are routed through one of two strategies: relaxing the screening filter so that interaction-supported variables enter the pattern search, or constructing explicit pair terms for a sparse downstream classifier. On a 40-dataset panel comprising 24 real-world tabular benchmarks and 16 synthetic interaction stress tests, evaluated under nested cross-validation, IAIML achieves mean AUC within 1.4 points of tuned gradient-boosted ensembles while requiring roughly 14--28 times fewer fitted explanation components. On datasets with strong pairwise interaction structure and low marginal signal, IAIML outperforms all baselines. Among compact interpretable methods, IAIML is comparable to RuleFit in AUC and component count and is less expensive to tune. EBM obtains a small but significant AUC advantage across the full panel, with a substantially larger lookup-table footprint. Performance degrades on datasets requiring higher-order interactions beyond the pairwise scope. Component-isolated ablations confirm that adaptive discretization and interaction-aware admission each contribute incrementally. These results support IAIML as a compact, interaction-aware framework appropriate for settings where bounded explanation size and controlled treatment of feature interactions are design requirements.

---


### 95. [Deanonymizing Monero Transactions in Tor Network](https://arxiv.org/abs/2607.07062)

**<font color=#1a73e8>作者：</font>** Ruisheng Shi, Shihan Zhang, Yulian Ge 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Monero is a privacy-focused cryptocurrency that deploys the Dandelion++ protocol and incorporates anonymity networks (such as Tor and I2P) to prevent malicious attackers from linking transactions with their source IPs. In this paper, we demonstrate that Monero's integration of the Tor network introduces a fundamental vulnerability: a Monero Tor node's originated transactions are exclusively forwarded to two outgoing Tor hidden service nodes (proxy nodes) prior to clearnet propagation, enabling an adversary to capture originated transactions by occupying the target node's outgoing connections. Based on this observation, we propose \textit{ProxyMark}, a three-stage deanonymization framework for the Monero Tor network, comprising node role identification, originated transaction identification, and node location deanonymization. Through experiments on the live Tor network, Monero mainnet, and testnet, we empirically demonstrate the effectiveness of \textit{ProxyMark} in successfully deanonymizing transactions originating from Monero nodes over Tor.

---


### 96. [Multiplication Beyond Groups: Stratified Fourier Mechanisms in Transformer Circuits](https://arxiv.org/abs/2607.07066)

**<font color=#1a73e8>作者：</font>** Zitong Andrew Chen, Junaid Hasan, Akhil Srinivasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have demonstrated a remarkable ability to learn algorithmic reasoning, yet mechanistic analyses have mostly focused on globally invertible operations such as cyclic addition and group composition. In this work, we investigate how small transformers learn modular integer multiplication over composite moduli, a fundamentally non-invertible operation due to the presence of zero-divisors. We propose the monoid extension: a localized generalization of Group Composition via Representation (GCR) that suggests the learned computation does not rely on a single global representation space. Instead, the model partitions the input space into local hierarchical algebraic regions, where group-like structure survives and Fourier mechanisms can be applied. In transformers trained on square-free modular multiplication, we find that embeddings organize around these regions, attention exhibits class-sensitive routing and low-rank write directions, and local character features explain a large fraction of the model's output logits. Our results suggest that representation-theoretic mechanisms previously identified for group operations can extend beyond groups to more general structures.

---


### 97. [An Hybrid Quantum-Classical Diffusion Model for Image Generation](https://arxiv.org/abs/2607.07072)

**<font color=#1a73e8>作者：</font>** Qipeng Qian, Keli Deng, Yuntao Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum diffusion models provide a physics-consistent route to generative learning by formulating noising and denoising directly on quantum states. However, applying such models to classical high-dimensional data is constrained by the qubit cost of state encoding and the computational burden of simulating large density operators. We propose a scalable hybrid generative pipeline that combines a classical autoencoder for dimensionality reduction with a mixed-state quantum denoising diffusion probabilistic model (MSQuDDPM) operating in the learned latent space. The autoencoder compresses data into compact latent codes that can be embedded into a small-qubit Hilbert space, after which the quantum diffusion model learns a generative distribution over latent density operators and decodes samples back to the original domain. Algorithmically, we simplify the reverse dynamics by predicting an estimate of the clean state $\rho_0$ at timestep $t$ and computing the one-step reverse update via an analytic backward propagation rule, rather than learning an explicit predictor for $\rho_{t-1}$. We demonstrate the proposed approach on MNIST image generation and discuss how mixed-state quantum diffusion can serve as a practical backbone for hybrid quantum--classical generative modeling under realistic qubit budgets.

---


### 98. [ShapeTalk: Combining Natural Language and Sketch for Time-Series Pattern Querying](https://arxiv.org/abs/2607.07073)

**<font color=#1a73e8>作者：</font>** Guoruizhe Sun, Yueqiao Chen, Emily Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Searching for time-series segments that match user-defined patterns is important in domains such as finance, climate science, and healthcare. However, existing visual query tools often struggle to support vague, composite, or fuzzy pattern descriptions, often requiring users to express their intent through precise sketches or rigid structured filters. We present ShapeTalk, a coordinated natural-language and sketch-based querying system for univariate time-series pattern search. Rather than treating text and sketch as a fused input stream, ShapeTalk uses them as complementary representations of analytic intent: natural language supports semantic and compositional pattern descriptions, while sketching supports direct geometric refinement. The two modalities are linked through a shared visual context, editable feature representations, and synchronized result views, enabling users to move between text and sketch during iterative query formulation. At its core is an LLM-based semantic parsing pipeline that translates free-form natural-language queries into interpretable and editable shape-feature constraints. We evaluate ShapeTalk through two usage scenarios, a user study with failure-case analysis, and an assessment of the LLM-based semantic parsing pipeline. The results show that ShapeTalk supports effective time-series pattern search, with natural language serving as an accessible entry point and sketching providing a complementary mechanism for refinement and recovery when textual specifications are insufficient.

---


### 99. [Cyber Dynamics I: Finite Macrostates for Behavioral Anomaly Detection in Network Telemetry](https://arxiv.org/abs/2607.07075)

**<font color=#1a73e8>作者：</font>** Abdul Rahman, Eranga Bandara, Sachin Shetty  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Entropy-based methods have long been used for network anomaly detection, but most existing approaches treat entropy as a scalar statistic on narrow observables rather than as part of a broader behavioral state-space for cyber systems. We propose a finite-dimensional macrostate framework for network telemetry, instantiated over the Canonical Security Telemetry Substrate (CSTS), so that coarse-graining is performed over persistent entities, typed relations, and temporal state rather than isolated event records. The resulting macrostate captures activity, distributional disorder, structural organization, temporal volatility, persistence, and deviation from benign baselines. Rather than scoring only unusual states, we model window-to-window macrostate transitions and define regime structure, stability, and anomalous change. This supports discrimination between benign workload drift and adversarial reorganization. We evaluate the framework on benchmark network telemetry datasets and compare it against Shannon-, Rényi-, and Tsallis-style entropy baselines, as well as standard anomaly detectors. The proposed representation improves anomaly discrimination and supports more interpretable behavioral analysis of cyber telemetry.

---


### 100. [Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis](https://arxiv.org/abs/2607.07077)

**<font color=#1a73e8>作者：</font>** Yapeng Li, Bo Jiang, Ziyan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Functional brain networks exhibit a hierarchical organization across ROI, community, and whole-brain levels, supporting local processing, inter-community coordination, and global integration. Recent studies have demonstrated that brain community-aware modeling is beneficial for both diagnosis and biomarker identification of brain networks. However, existing brain graph modeling methods often struggle to model ROI-community interactions, thereby failing to fully exploit the hierarchy across ROI, community, and whole-brain network levels. To address this issue, inspired by deep hyperbolic learning in modeling hierarchical structures, we propose a novel framework, termed Hyperbolic Learning on Brain Graphs (HLBG), for brain network analysis. The core idea of HLBG is to exploit the inherent hierarchical geometry of hyperbolic space to model the hierarchical relationships among ROIs, functional communities, and the whole-brain network, thereby learning hierarchy-aware and highly discriminative representations for brain network data. Specifically, HLBG first projects representations from ROIs, communities, and the whole-brain network into Lorentzian hyperbolic space. Then, the multi-level hierarchy is imposed via two geometric entailment constraints. In addition, we introduce a new Graph-aware Mamba (GaMamba) model, which incorporates topology-derived structural prompts into Mamba to capture long-range dependencies while preserving graph topological information. Experiments on ABIDE-I and REST-MDD demonstrate that HLBG outperforms state-of-the-art methods and identifies disorder-relevant functional biomarkers.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-207](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
