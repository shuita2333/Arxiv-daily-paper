# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 301. [Target-Aware Interaction-Guided Reinforcement Learning for Black-Box Node Injection Attacks on Graph Neural Networks](https://arxiv.org/abs/2607.04091)

**<font color=#1a73e8>作者：</font>** Yi Lan, Ye Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have achieved remarkable performance in graph representation learning, yet their inherent vulnerability to adversarial attacks poses severe security risks. Especially, black-box node injection attacks have become a major threat to GNNs since they inject malicious nodes without altering the original graph topology. However, they typically decouple the generation of malicious node features and edge connections, thereby resulting in suboptimal attack efficacy under stringent budgets. To address this critical issue, this study proposes a novel Target-aware Interaction-guided Reinforcement learning for Black-box node injection Attacks on GNNs (TIRBA), which formulates the attack as a Markov Decision Process and jointly optimizes node feature generation and edge construction in a heterogeneous action space. Firstly, TIRBA designs a target-aware interaction encoder to fuse information of node features and edges. Further, it introduces a class-center guidance mechanism to utilize prior class distribution information, thereby guiding efficient exploration of the high-dimensional feature space. Finally, a topology difference-aware state value evaluation is adopted to explicitly capture local structural anomalies caused by injected nodes, thereby stabilizing the reinforcement learning training process. Experimental results demonstrate that the proposed TIRBA significantly outperforms state-of-the-art black-box node injection attack methods.

---


### 302. [Sparse4D-Radar: An Efficient and Robust Framework for Surround-View 3D Object Detection via 4D Radar-Camera Fusion](https://arxiv.org/abs/2607.04098)

**<font color=#1a73e8>作者：</font>** Fuyuan Ai, Yuchen Tan, Jiehui Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, 4D imaging radar has gained wide attention in autonomous driving for its robustness against harsh weather and ability to output target velocity. Nevertheless, mainstream 4D radar-camera fusion methods only support front-view perception, lacking mature solutions for surround-view sensing. Directly expanding these pipelines to full 360° coverage introduces excessive computation cost and limits real-world deployment. To tackle these limitations, this work proposes Sparse4D-Radar, an efficient robust surround-view multi-modal fusion framework. We first design a Deformable Fusion module to embed radar-camera features into sparse queries, constructing the lightweight base version Sparse4D-Radar-Base. Two dedicated modules are further introduced to boost localization accuracy and modality stability: Velocity-Consistency Sampling (VCS) refines features via radar velocity cues for motion awareness, and Adaptive Modality Gating (AMG) dynamically adjusts cross-modal fusion weights according to feature confidence. Combining all components, we build Sparse4D-Radar-Acc for high-precision detection demands. Comprehensive experiments on OmniHD-Scenes verify that our approach achieves state-of-the-art surround-view 3D detection performance. Compared with prior arts, our method obtains over 7% mAP and 10% ODS improvements under complex driving scenes while running at nearly 10 FPS, striking a favorable trade-off among detection accuracy, environmental robustness and inference efficiency. Our open-source code is available at this https URL.

---


### 303. [The Multipath Blind Spot: $K$-Agnostic Robust Calibration for Sparse-Anchor Metric Depth from Frozen Foundations](https://arxiv.org/abs/2607.04101)

**<font color=#1a73e8>作者：</font>** Sohag Roy, Rajesh Misra, Swami Shastravidyananda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth foundations predict domain-general relative depth but lack absolute scale; a handful of sparse metric anchors from a range sensor can calibrate them to metric depth, an attractive alternative to metric-supervised training. Existing sparse-anchor calibration methods, however, assume the anchors are clean, whereas real sensors produce outliers that are present with the wrong value -- time-of-flight multipath, mixed pixels -- not merely missing. We show that the established residual-on-CFA calibration recipe collapses under such outliers, and that the strongest publicly deployed method, VI-Depth, has a structural multipath blind spot: robust to missing anchors, it falls behind an unprotected baseline on three of four datasets when anchors are present but wrong. We propose Multipath-Robust Anchor Calibration (MRAC), a parameter-free, inference-time wrapper that gates anchors by foundation consistency -- a Theil--Sen fit and a median-absolute-deviation test against the foundation's own relative-depth ordering -- before a single call to the calibration head. MRAC adds no learned parameters, runs its selection in $\approx 50\,\mu$s on CPU, and serves anchor budgets $K \in [5,200]$ from one checkpoint. On a $320$-cell benchmark with a same-backbone, same-architecture control, MRAC strictly wins $84\%$ of same-backbone cells across all four outlier families and, against VI-Depth, wins all twelve corrupted multipath cells and all sixteen KITTI cells, reducing KITTI multipath AbsRel by $3.2\times$ ($0.489$ to $0.151$) at zero retraining.

---


### 304. [Semantic Integration and Lexical Expectation Shape N400 and P600 Dynamics During Naturalistic Reading](https://arxiv.org/abs/2607.04107)

**<font color=#1a73e8>作者：</font>** Kun Sun, Rong Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Word surprisal is a well-established computational predictor of human neural responses during language comprehension, but it remains less clear whether local semantic fit explains neural response variation beyond lexical expectation during naturalistic reading. Using the Dublin EEG-based Reading Experiment Corpus (DERCo), this study examined whether contextual semantic relevance predicts word-locked EEG activity in the N400 and P600 windows. Contextual semantic relevance was computed as an attention-aware measure of how strongly a target word is semantically connected to its recent discourse context, and it was compared with GPT-based word surprisal. Across 22 participants and 32 EEG channels, we tested both predictors using regression-based ERP analyses and generalized additive mixed models while controlling for lexical variables and repeated observations. Both predictors were reliably associated with EEG responses, but they showed partly different temporal and scalp-level patterns. Surprisal captured expectancy-related variation, whereas contextual semantic relevance showed robust effects across N400- and P600-window mean voltages, with particularly strong explanatory support in the P600 window. Model comparisons indicated that contextual semantic relevance contributed explanatory value beyond lexical controls and surprisal. These findings suggest that naturalistic reading depends on both lexical expectation and local semantic integration, and that contextual semantic relevance offers an interpretable computational link between discourse semantic fit and ERP dynamics.

---


### 305. [Asymptotic-Preserving A Posteriori Analysis of Diffusion and Flow-Matching Samplers](https://arxiv.org/abs/2607.04113)

**<font color=#1a73e8>作者：</font>** Shiheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-matching samplers integrate a learned probability-flow ODE from a large noise scale down to a small terminal floor $\sigma_{\min}$, at which the score is stiff and the flow develops a boundary layer. We treat $\sigma_{\min}$ as a singular-perturbation parameter and determine which fixed-step samplers are asymptotic-preserving (AP), that is, stable and uniformly accurate as $\sigma_{\min}\to0$, casting the criteria as an a posteriori audit: residual functionals with $\sigma_{\min}$-uniform coefficients, computable on a pretrained checkpoint without ground-truth scores or exact trajectories. On the terminal layer, Euler in the $\sigma$-clock, the deterministic DDIM update, is the unique layer-exact discretization up to affine reparameterization, with rectified flow its flow-matching counterpart; the $\lambda$-clock is stable only for steps $h\le h_\star=1+W(1/e)$, and the uniform-$\sigma^2$ heat clock stalls a $\sigma_{\min}$-independent distance from the data. On two solvable models (rank-deficient Gaussian, symmetric two-point mixture), deterministic samplers remain first-order uniformly accurate with no $\log(1/\sigma_{\min})$ factor, even across a symmetric posterior-switching interface whose distributional budget is a universal constant; the logarithm is charged entirely to the Itô term of stochastic samplers, whose path-KL scales as $\Lambda^2/N$ against the ODE's $O(\Lambda^2/N^2)$ budget, with $\Lambda=\log(\sigma_{\max}/\sigma_{\min})$. On the EDM CIFAR-10 checkpoint, spectra measured once predict held-out residual budgets across step count, schedule, and noise level against pre-specified gates with no per-configuration refitting, and calibrate the Itô coefficient at $M_1=1.00\pm0.01$. The clock decides stability; the noise, not the geometry, charges the logarithm.

---


### 306. [GlacierCastAI: Predicting Glacier Retreat from Multi-Modal Satellite Imagery and Climate Signals](https://arxiv.org/abs/2607.04117)

**<font color=#1a73e8>作者：</font>** Arunkumar Ramachandran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ERA5 seasonal climate variables contain predictive information about future glacier retreat beyond what satellite imagery alone provides, yet existing deep learning methods focus on mapping current boundaries rather than forecasting future ones. This paper presents GlacierCastAI, which reframes glacier boundary prediction as a multi-modal spatiotemporal forecasting problem, fusing multi-temporal Landsat imagery with ERA5 reanalysis climate variables and Copernicus DEM terrain features to forecast glacier boundaries across five glaciers spanning four climate regimes. The architecture couples a ResNet50 spatial encoder with a ConvLSTM temporal model and a cross-attention climate fusion module. Because forecasting is inherently more uncertain than mapping current boundaries, the reported IoU values (0.320-0.337) are not directly comparable to state-of-the-art mapping models. Comparisons are against traditional baselines and experimental conditions. Through a pre-registered ablation study, adding ERA5 climate signals improves image-only IoU from 0.326 to 0.337 (+3.4%), suggesting that atmospheric forcing carries predictive information beyond imagery alone. All deep learning models substantially outperform persistence and linear trend baselines (IoU 0.160 and 0.169 respectively), with improvements of 89-99% relative IoU. A lightweight climate-only MLP baseline (661K parameters) achieves an IoU of 0.320 (98% of image-only performance) using 85x fewer parameters, suggesting that ERA5 variables encode substantial predictive signal independently of satellite imagery. SHAP attribution analysis suggests that spring solar radiation (MAM) is the dominant climate driver, consistent with the known role of spring insolation in setting melt season trajectories.

---


### 307. [Parametric Memory Decoding for Zero-Shot Routing in LoRA-Based External Parametric Memory](https://arxiv.org/abs/2607.04118)

**<font color=#1a73e8>作者：</font>** Fengxian Ji, Zhuohan Xie, Jingpu Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rise of parametric memory, LoRA-based External Parametric Memory (EPM) has emerged as a modular solution, but existing routing methods often introduce additional training, deployment, and maintenance overhead. This raises a natural question: can a LoRA-based EPM bank be routed without maintaining an additional routing component? However, existing zero-shot LoRA routing methods still face two problems under the EPM setting: (1) their evaluations are scattered across different task settings rather than organized around EPM access, and (2) their routing signals lack a unified perspective to guide systematic improvement. To address these problems, we organize PMD-Bench, covering document-level, domain-level knowledge, and task-skill, and propose Parametric Memory Decoding (PMD), the first framework designed to systematically improve zero-shot LoRA routing by reframing it as decoding activations over external parametric memory. Based on PMD, we further instantiate PMDRouter, which scores each LoRA by its response magnitude from a single base-model prefill. Experiments on PMD-Bench show that PMDRouter achieves the strongest internal-signal performance across multiple zero-shot routing settings. These results demonstrate the feasibility of zero-shot LoRA routing and suggest that PMD can serve as a general framework for improving zero-shot routing methods. Sources: Github (this https URL)

---


### 308. [SOV-CAD: Stepwise Orthographic Views Guided CAD Modeling Sequence Reconstruction](https://arxiv.org/abs/2607.04119)

**<font color=#1a73e8>作者：</font>** Zhaopeng Feng, Chen Zhi, Xuhong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing Computer-Aided Design (CAD) modeling sequences from images is crucial for preserving design intent and supporting parametric editing. However, existing methods typically generate full CAD sequences holistically, overlooking the iterative, feedback-driven nature of human design workflows. We address this limitation by introducing the rich stepwise visual supervision: at each modeling step, the system observes the target's orthographic projections, the projections of the incrementally constructed model, and the active sketch, enabling informed action selection. To effectively leverage this on-the-fly feedback, we propose SOV-CAD, a framework that formulates CAD reconstruction as a sequential decision-making task and employs offline reinforcement learning with a Decision Transformer architecture. This design incorporates continuous visual feedback guided by geometric alignment rewards, resulting in a more accurate and human-like modeling process. Extensive experiments show that SOV-CAD surpasses state-of-the-art methods in CAD sequence reconstruction while exhibiting strong data efficiency. Code of SOV-CAD is available at: this https URL

---


### 309. [CertMix: Certified, Data-Efficient Metamaterial Design by Affine Mixing of Aligned Neural-Implicit Weight Spaces](https://arxiv.org/abs/2607.04123)

**<font color=#1a73e8>作者：</font>** Yifan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse design of mechanical metamaterials seeks a periodic unit cell whose homogenized elastic properties meet a prescribed target, but current learning-based methods are data-hungry, mostly interpolative, and provide no guarantee that the generated design satisfies the specification. We introduce CertMix, a data-efficient framework that represents each exemplar unit cell as a small periodic neural implicit field, specifically a SIREN signed-distance decoder overfit from a shared anchor, so that exemplar weight vectors become aligned and directly comparable. The key observation is that, in this aligned weight space, the homogenized elasticity tensor is approximately linear in the mixing coefficients. Targeted design therefore reduces to a small constrained affine-mixing problem solved with a differentiable periodic homogenizer in the loop. Negative coefficients enable extrapolation beyond the exemplar range, a linearity-mismatch trust region keeps blends valid, and split-conformal calibration converts the mismatch signal into a distribution-free certificate on achieved-property error. From as few as 50 exemplars, CertMix attains a scaled property error of $10^{-4}$, roughly two to three orders of magnitude below conditional generative baselines trained on 1000 cells. It remains accurate far outside the exemplar range, is $57\times$ faster than per-target topology optimization while avoiding checkerboards and enclosed voids, and extends to spatially graded fields, 3D triply periodic surfaces, and a certified running-shoe midsole application.

---


### 310. [FRFDet: Efficient UAV Small Object Detection with Symmetric Sampling and Scalable Fusion](https://arxiv.org/abs/2607.04125)

**<font color=#1a73e8>作者：</font>** Yunzhong Si, Huiying Xu, Xinzhong Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small object detection in Unmanned Aerial Vehicle (UAV) imagery remains challenging under adverse conditions, including complex weather, low illumination, and sensor noise. These challenges mainly stem from severe background clutter, fine-grained detail degradation, and suboptimal semantic-spatial feature fusion, which jointly hinder robust small-object representation. To this end, we propose FRFDet, a lightweight yet effective single-stage detector tailored for UAV-based small object detection. FRFDet proposes two plug-and-play modules: Inverse Bidirectional Sampling (IBS) and Scale-Feature Relationship Cross-Fusion (SFRCF). IBS preserves critical spatial details via channel expansion-compression and bidirectional pattern reconstruction, improving feature alignment. SFRCF explicitly models scale-dependent fusion behaviors, revealing that inter-group element-wise multiplication favors compact models, while inter-group additive fusion benefits larger architectures. Extensive experiments on VisDrone, UAVDT, HazyDet, and MS COCO demonstrate that FRFDet achieves state-of-the-art performance among lightweight detectors with low computational cost, compact parameters, and fast inference, making it well suited for resource-constrained UAV platforms.

---


### 311. [Real-Time LiDAR Gaussian Splatting SLAM](https://arxiv.org/abs/2607.04127)

**<font color=#1a73e8>作者：</font>** Seungjun Tak, Yewon Jeon, Jaeik Hwang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a real-time LiDAR-based framework for Gaussian Splatting SLAM that tightly couples fast G-ICP registration with spherical rasterization-based dense mapping for large-scale sequences. Leveraging LiDAR geometry rather than appearance, we reuse tracking-estimated local covariances to initialize Gaussians with range-aware scales and to derive surface normals for geometry-aware map optimization. We further introduce a covariance-derived geometry score that measures local complexity and drives pruning in planar regions and selective densification in structurally rich areas, while optimized Gaussians and LiDAR-specific confidence cues are fed back to improve tracking robustness. On the Newer College dataset, our method achieves an F-score of 86.78\% using purely online trajectories at real-time speed ($>$20 FPS), and additional experiments on other datasets confirm its stability and scalability.

---


### 312. [MDL Meets Latent Confounders: LNML-based Causal Discovery](https://arxiv.org/abs/2607.04133)

**<font color=#1a73e8>作者：</font>** Zhongyi Que, Shin Matsushima, Kenji Yamanishi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery with nonlinear mechanisms and latent confounders remains challenging. Existing methods often rely on either linear assumptions or causal sufficiency, limiting their applicability. We propose an MDL-based causal discovery framework that explicitly accounts for latent confounders while allowing flexible nonlinear mechanisms by minimizing the luckiness normalized maximum likelihood (LNML) code-length. The causal relationship between each variable pair is determined by selecting the shortest code-length of the causal model, and we introduce the notion of $\Delta$-pseudo-collinearity to identify dependencies induced by latent confounders. Based on these ideas, we develop a greedy algorithm, termed Pseudo-Collinearity Guided Causal Discovery (PCG-CD). Experiments on synthetic and real-world datasets demonstrate that the proposed method accurately recovers directed causal relationships and effectively detects latent confounders.

---


### 313. [Masked Generative-Contrastive Representation Learning for Cross-Dataset EEG-Based Emotion Recognition](https://arxiv.org/abs/2607.04139)

**<font color=#1a73e8>作者：</font>** Huqin Weng, Jiayang Huang, Yimin Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) shows strong potential for cross-dataset transfer by improving feature representation and generalization. However, its application to EEG-based emotion recognition remains largely unexplored. Existing SSL methods struggle to capture the intricate spatiotemporal dependencies of EEG signals under varying channel configurations, extract fine-grained representations resilient to noise, and derive global features that generalize well across subjects. To address these challenges, we propose Masked Generative-Contrastive Representation Learning (MGCRL), a novel SSL framework specifically designed for EEG-based emotion recognition. Built upon a region-aware spatiotemporal encoder, MGCRL integrates generative and contrastive learning to achieve both fine-grained and global discriminative representations for cross-dataset generalization. MGCRL introduces three key designs: 1) a spatiotemporal encoder that incorporates region-based graph convolution to capture localized spatial and functional relationships, enhancing region-specific feature learning and mitigating the impact of varying EEG channel configurations across datasets; 2) a generative learning mechanism based on the joint embedding predictive architecture (JEPA) that utilizes masked features to capture noise robustness fine-grained representations, improving the model's capability to characterize subtle emotional states; and 3) a contrastive learning strategy that leverages masked and original features to learn temporally stable and cross-subject-invariant representations across the same stimuli, boosting emotion discrimination and cross-subject generalization. Under these designs, MGCRL exhibits remarkable ability to learn universal representation. Extensive experiments involving pretraining on the large FACED dataset and fine-tuning on multiple SEED-series datasets demonstrate the effectiveness of MGCRL.

---


### 314. [Binary Iterative Method for Non-targeted Adversarial Attack](https://arxiv.org/abs/2607.04145)

**<font color=#1a73e8>作者：</font>** Naman Goyal, Milan Chaudhari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks guide and provide additional training and test data for both adversarial training and adversarial robustness validation, and expose the 'piecewise linearity' of deep learning based models. Since adversarial attacks and adversarial robustness are mathematically defined problems that can be optimised directly with end-to-end differentiable search, adversarial robustness is more widely applicable than other robustness metrics such as corruption and perturbation robustness, and new kinds of adversarial attacks are beneficial for robustness testing. Attacks are targeted or non-targeted depending on whether the image is modified to misclassify to a particular class or to any incorrect class; we focus on the non-targeted setting. Finding the optimal input data points and hyper-parameters for generating non-targeted adversarial attacks remains a challenge for current methods like the Fast Gradient Method, Basic Iterative Method and Virtual Adversarial Method. We propose a new method, the "Binary Iterative Method" (BinIM), which uses a divide-and-conquer paradigm to optimise parameters and hyper-parameters for the generation of non-targeted attacks. We compare our method to other gradient-based adversarial attacks evaluated over pre-trained networks (InceptionV3, InceptionV2, ResNet V2 152) on classification tasks. On 1000 randomly-sampled images from the standard ImageNet dataset, the Binary Iterative Method outperforms all other gradient-based methods, qualitatively making the classifier misclassify with confidence up to 0.995 while reducing the probability of the true label to 2.21e-09 (approximately 0).

---


### 315. [Perceiving Better Moments: Cover Frame Reselection and Enhancement for Live Photos with the Live2K Dataset](https://arxiv.org/abs/2607.04151)

**<font color=#1a73e8>作者：</font>** Junyu Lou, Kai Chen, Weiyi You 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern smartphones capture Live Photos, short video bursts surrounding a still image, offering a dynamic and engaging photographic experience. However, the cover photo and video components are generated by two distinct imaging pipelines: the photo stream undergoes full computational photography processing, while the video stream is constrained by real-time efficiency and heavy compression. This intrinsic separation produces a substantial quality gap in resolution, color fidelity, and dynamic range between the cover photo and video frames. When users reselect an alternative frame from the video to replace an imperfect cover, the chosen frame often suffers from severe degradation, making direct replacement visually unsatisfactory. Restoring such frames requires simultaneous enhancement of spatial detail and color appearance, a task considerably more challenging than ordinary super-resolution or color enhancement. To address this, we define the Live Photo Cover Frame Reselection and Enhancement (LPRE) task, which leverages the intrinsic cues available within each Live Photo: the high-quality cover image as a structural and color reference, the user-reselected low-quality frame as the reconstruction target and several adjacent video frames providing temporal cues. Building upon this formulation, we construct Live2K, a real-world dataset of 2,042 Live Photos, and develop a unified one-stage baseline that integrates multi-frame fusion, guided color enhancement and super-resolution, establishing the first benchmark for Live Photo enhancement research.

---


### 316. [Mask-based Predictive Representations for Reinforcement Learning](https://arxiv.org/abs/2607.04153)

**<font color=#1a73e8>作者：</font>** Kai Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-based deep reinforcement learning involves dealing with high-dimensional inputs of image information. It is crucial to abstract effective states from high-dimensional image inputs and limited samples for sample-efficient reinforcement learning. To address this challenge, inspired by fields such as natural language processing and computer vision, we propose a self-supervised task based on mask prediction as an auxiliary task for reinforcement learning. This non-reconstruction method uses the sequence information collected by the agent from the environment and the context information in the sequence to predict the masked information, thereby strengthening the agent's understanding of the task and learning effective representations. Combined with transformers, we find that the model reconstructs the masked input sequence in the latent space. By feeding the compressed representations learned by this method into reinforcement learning models, we observe an improvement in the sample efficiency of reinforcement learning. Moreover, the model outperforms state-of-the-art sample-efficient reinforcement learning methods on multiple continuous and discrete control benchmarks.

---


### 317. [Piercing Gilbreath's Conjecture: From Deep Number Theory Insights to Fintech and Cybersecurity](https://arxiv.org/abs/2607.04166)

**<font color=#1a73e8>作者：</font>** Vincent Granville  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> I propose a new methodology to attack the fascinating Gilbreath's conjecture about prime numbers, first posted in 1878 and unsolved to this day. The problem statement is rudimentary: kids can understand it. However, despite decades of research, almost no progress has been made. This paper changes the game by presenting a new approach based on sieving, a number of new results with proof, a precise path to the solution, and solid references. It also introduces the concept of reverse sieving, along with applications to testing randomness, pattern and fraud detection, cybersecurity, synthetic data, sequence categorization and normalization, or to detect and quantify a new type of chaos in time series including Brownian motions. Magic primes, forbidden prime number constellations, cellular automata, and reduction via classes of equivalent sequences, are some of the innovative and promising topics discussed in the paper.

---


### 318. [FedFFT: Taming Client Drift in Federated SAM via Spectral Perturbation Filtering](https://arxiv.org/abs/2607.04170)

**<font color=#1a73e8>作者：</font>** Liyang Yuan, Yibo Yang, Dandan Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables decentralized training without data sharing, but suffers from statistical heterogeneity across clients, leading to client drift, poor generalization, and sharp minima compared to centralized training. Sharpness-Aware Minimization (SAM) has emerged as a promising approach to improve generalization, yet its application in federated learning still suffers from divergence problems, since perturbations are computed locally and reflect client-specific loss geometries. To better understand this issue, we provide experimental evidence from a new perspective, the frequency domain, for SAM perturbations in federated settings, revealing that inter-client perturbation inconsistencies are predominantly concentrated in the low-frequency spectrum. Motivated by this insight, we propose Federated learning with Frequency-domain Filtering of SAM perturbations (FedFFT). It is a lightweight and plug-and-play method that filters out low-frequency components of SAM perturbations without requiring additional communication, thereby suppressing inconsistent components in client updates while preserving consistent learning signals. Extensive experiments across multiple benchmarks and diverse backbones demonstrate that FedFFT consistently outperforms SAM-based FL methods, particularly under severe non-IID distributions. These results highlight the effectiveness, scalability, and general applicability of our frequency-domain perspective for sharpness-aware federated optimization.

---


### 319. [A Clustering-Based Framework for Identifying Suspicious Trading Patterns in Capital Market](https://arxiv.org/abs/2607.04184)

**<font color=#1a73e8>作者：</font>** Asif Zaman, Romona Magdalene Sarkar, Sabiha Khair Ohi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Market manipulation is the dubious practice of manipulating stock prices in order to make a quick profit, which truly degrades confidence on trading platforms. We implemented an unsupervised fraud-detection toolkit that begins with K-Means++ clustering to address this issue. A dataset of roughly one million financial transactions from 2012 to 2024 is used. In order to identify fraudulent trades and categorize them using market practice heuristic thresholds, the study suggests a clustering-based pipeline. The method highlights 2.02% of trades as suspicious where 51.10% clearly indicate spoofing, 0.10% indicate pump and dump, 0.55% indicate insider trading, 1.43% indicate a fake breakout, and 46.83% are unclassified. Despite the lack of ground truth, the model's performance is confirmed by a Silhouette Score of 0.561.

---


### 320. [Physics-Informed Graph Learning with Uncertainty Awareness for Open-Set Domain Generalization in Fault Diagnosis](https://arxiv.org/abs/2607.04188)

**<font color=#1a73e8>作者：</font>** Jinfeng Zhu, Shiyu Long, Ye Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intelligent industrial maintenance critically relies on reliable fault diagnosis of rotating machinery. However, it faces formidable challenges from unknown fault types and domain shifts induced by varying operating conditions, which is formally formulated as the open-set domain generalization (OSDG) problem. Existing methods are mainly data-driven, thereby overlooking the cascaded propagation of uncertainty across feature extraction, topological learning, and decision-making this http URL tackle this challenge, we propose PGU-OD, a novel Physics-Informed Graph Learning framework with Uncertainty Awareness for Open-set Domain generalization. First, it designs a physics-informed spectral attention module to extract condition-robust fault features, thereby suppressing perceptual uncertainty caused by frequency shifts. Further, it constructs an uncertainty aware adaptive graph learning mechanism to dynamically adjust the edge weights of the sample graph guided by class-scale Gaussian distribution parameters, which mitigates the structural propagation of uncertainty. Finally, a Gaussian-distribution-based adaptive boundary loss function and a dual-criteria open-set inference strategy are developed to optimize decision boundaries and reliably reject unknown faults. Extensive experimental evaluations on two public and widely used rotating machinery fault datasets demonstrate that the proposed PGU-OD outperforms state-of-the-art baselines in both known fault classification and unknown fault rejection under domain shifts.

---


### 321. [SpecGradFilter: A Spectral Gradient Filtering Framework for Taming Federated Heterogeneity](https://arxiv.org/abs/2607.04189)

**<font color=#1a73e8>作者：</font>** Liyang Yuan, Yibo Yang, Dandan Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) is fundamentally challenged by statistical heterogeneity, where non-identically distributed (non-IID) data induces client drift that severely hampers global convergence. While existing approaches attempt to mitigate this drift through spatial-domain gradient correction or regularization, they overlook the intrinsic spectral structure of optimization signals. In this work, we revisit client drift from a novel frequency-domain perspective and uncover a critical Spectral Bias of Drift: inter-client gradient divergence is predominantly concentrated in low-frequency components which encode client-specific distributional shifts, while high-frequency components representing fine-grained features remain relatively consistent. Motivated by this, we propose SpecGradFilter, a unified Spectral Gradient Filtering Framework that tames heterogeneity by suppressing discordant low-frequency signals. Crucially, we demonstrate that SpecGradFilter is a generalizable principle, effective not only via precise FFT-based truncation but also through spatial approximations like Gaussian detrending. Extensive experiments on benchmarks such as CIFAR-10/100 and Tiny-ImageNet demonstrate that SpecGradFilter significantly performs better performance in highly Non-IID settings with negligible communication overhead, establishing a new paradigm for robust federated optimization.

---


### 322. [Exploring Convolutional Neural Processes for Weather Downscaling](https://arxiv.org/abs/2607.04190)

**<font color=#1a73e8>作者：</font>** Francisco Passos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global reanalysis products such as ERA5-Land provide spatially complete weather fields but at resolutions too coarse for local applications, particularly in mountainous regions where temperature can vary by several degrees over short distances. This project investigates Convolutional Conditional Neural Processes (ConvCNPs) for statistical downscaling of daily maximum temperature from the ~11km resolution ERA5-Land grid to ~1km resolution over Switzerland, building upon the architecture of Vaughan et al. (2022) and adapting it to the topographically complex Swiss domain with high-resolution elevation features from the swisstopo DHM25. The best model, trained on ten years of data (2014-2023) with five-fold temporal cross-validation, achieves a mean absolute error of 1.31 Celsius and a CRPS-based skill score of 0.524 relative to bilinear interpolation, reducing the expected prediction error by more than half. An ablation study reveals that the elevation MLP is the indispensable component - without it, the model diverges entirely - while explicit seasonal features and Topographic Position Index provide secondary benefits. Under sparse on-grid input the model degrades gracefully, maintaining positive skill down to approximately 10% of the input grid; however, zero-shot deployment on off-grid station observations does not achieve positive skill at any density tested. All configurations exhibit severely overconfident uncertainty estimates, a structural limitation of the Gaussian likelihood training objective. These results demonstrate that ConvCNPs are a viable and effective approach to climate downscaling in complex terrain, and identify uncertainty calibration and native support for non-gridded input as the key challenges for operational deployment.

---


### 323. [Ball Differential Privacy: How to Mitigate Data Reconstruction with Less Noise](https://arxiv.org/abs/2607.04209)

**<font color=#1a73e8>作者：</font>** Joseph Margaryan, Nirupam Gupta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vector embeddings of raw records, while not human-readable, do not preserve record privacy: an adversary can reconstruct training records from a released model even when that model is a simple convex classifier. Differential privacy (DP) is the principled defense, but its noise is calibrated to worst-case indistinguishability, hiding arbitrary single-record substitutions, including those far outside the set of plausible alternatives relevant to a reconstruction adversary. The result is noise far larger than what reconstruction robustness requires, degrading accuracy without a corresponding security benefit.
We propose Ball-DP: enforcing epsilon-delta indistinguishability over single-record substitutions restricted to a ball of radius r under a distance metric d in the embedding space. A deployment facing only local reconstruction threats can choose a small r, thereby reducing noise and recovering accuracy. The radius makes the scope of the privacy claim explicit against reconstruction attacks; standard DP is recovered when r covers the entire admissible record domain. We provide noise calibrations for regularized convex learning problems under Ball-DP, and derive corresponding reconstruction-robustness certificates, called Ball-ReRo, that upper-bound an attacker's reconstruction success. By deriving the optimal finite-prior MAP reconstruction attack, we empirically audit Ball-ReRo certificates on seven benchmark learning tasks. Our experiments show that calibrating noise to Ball-DP improves utility, considerably exceeding the dilution of reconstruction robustness in high-privacy regimes, i.e., when epsilon is small.

---


### 324. [Channel-Adaptive Robust Aggregation for Over-the-Air Federated Learning in Heterogeneous Networks](https://arxiv.org/abs/2607.04218)

**<font color=#1a73e8>作者：</font>** Zubaida Fatima, Zubair Shaban, Yusuf Jamal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing demand for privacy-preserving, data-intensive applications such as IoT, augmented reality, and autonomous systems positions Federated Learning (FL) as a key enabler in 6G networks. Over-the-Air FL (OTA-FL) leverages the superposition property of the wireless multiple access channel for efficient aggregation via simultaneous transmissions. Existing methods rely on fixed aggregation schedules and do not jointly address noise, fading, and client heterogeneity. We propose CHARGE-FL (CHannel-Adaptive Robust agGrEgation), a framework that adaptively schedules aggregation based on channel dynamics and application readiness. By combining a tailored optimization strategy with a dual-purpose precoding mechanism, CHARGE-FL mitigates channel distortion and bias from partial updates, achieving superior accuracy, stability, and convergence under realistic wireless conditions. Empirical results under realistic wireless conditions show that CHARGE-FL significantly improves accuracy, stability, and convergence over state-of-the-art OTA-FL methods, particularly in straggler-prone and noisy scenarios.

---


### 325. [Unsupervised Features Mining via Activation Geometry](https://arxiv.org/abs/2607.04222)

**<font color=#1a73e8>作者：</font>** Amit LeVi, Elad David, Max Fomin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interpretability methods aim to reveal the features represented inside large language models (LLMs). Many existing methods begin with labeled examples of a human-defined concept that may reflect human biases, and then identify how that concept is represented within the model, for example in its activation space or through other decomposition methods. We introduce \emph{Mining via Activation Geometry} (MAG), a simple unsupervised framework for extracting reasoning features from model activations by prepending the same natural-language instruction $Q$ to every input $p$, where $Q$ defines the reasoning feature of interest, such as ``Can this object be found in the desert?'' or ``Is this prompt malicious?'' We measure how the instruction changes the model's internal representation using $m(Q \mid p) - m(p)$ at a single readout point. We explore eight different MAGs. The extracted reasoning features predict the models' own world understanding and judgment, can be approximated into a single activation direction, we found that some features are more linearly represented and some less, this linear representation, which is vector steering, can change the LLMs' decisions through activation steering by injecting reasoning features. Finally, we use the same method to select the best training datasets for prompt-injection classifier probes: while similarity between ordinary activations is almost unrelated to downstream performance, RFD-based similarity achieves $94.7\%$ Top-1 and $100\%$ Top-2 accuracy.

---


### 326. [Hierarchical Multi-to-Single-Modal Knowledge Distillation for Disruption Prediction in EAST](https://arxiv.org/abs/2607.04241)

**<font color=#1a73e8>作者：</font>** Qiang Chen, Xiao Wang, Hao Si 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Plasma disruption is a critical threat to tokamak safety. Existing data-driven predictors mainly rely on time-series diagnostic signals, while visible images provide complementary spatial cues including plasma deformation, local brightening, and radiation-structure evolution. Although the image modality improves the model's discriminative capability, it also substantially increases the computational cost during inference. To address this issue, we propose a hierarchical multi-to-single-modal knowledge distillation framework for disruption prediction on a synchronized EAST multimodal dataset. During training, visible images and time-series signals are used to train a multimodal teacher, which learns disruption precursor representations through Transformer-based encoders and a prototype-guided spatiotemporal hypergraph module. During inference, only the time-series student is retained, with multimodal knowledge transferred through graph-structure-level, representation-level, and decision-level distillation. On the 640-discharge EAST dataset, the results demonstrate that the proposed framework can preserve the discriminative advantages of multimodal learning while substantially reducing inference cost, and providing an effective route for efficient disruption prediction in EAST. The source code of this paper will be released on this https URL.

---


### 327. [HeartVolMesh: Cardiac Volumetric Mesh Reconstruction via Covariance-Guided Graph Deformation](https://arxiv.org/abs/2607.04243)

**<font color=#1a73e8>作者：</font>** Fengming Lin, Arezoo Zakeri, Haoran Dou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate patient-specific tetrahedral cardiac meshes are essential for in-silico trials, yet common segmentation-then-modelling pipelines can blur thin-wall anatomy and offer limited cross-case correspondence. We propose HeartVolMesh, which lifts each template vertex to an anisotropic Gaussian kernel and uses a 3D CNN-GNN to predict per-vertex displacements and Cholesky-parameterized covariances from volumetric images. Training is guided by a covariance-aware negative log-likelihood loss with lightweight mesh regularization. For volumetric meshing, we warp a fixed tetrahedral template to the reconstructed surface via staged alignment, non-rigid registration, and deformation propagation, preserving connectivity and correspondence by construction, with resolution controlled by template density. Experiments show consistent gains over deformation-based baselines in surface mesh accuracy and volumetric mesh fidelity.

---


### 328. [Signal or Noise? Understanding Generative Models for Real-World Sensor Time Series](https://arxiv.org/abs/2607.04245)

**<font color=#1a73e8>作者：</font>** Zitao Shuai, Zongzhe Xu, Yuntian Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models have changed how machine learning represents complex data distributions, especially in language and vision, yet many real-world systems are observed instead as continuous, high-dimensional, and noisy sensor time series. Existing generative modeling of sensor data, however, remains fragmented across modalities, datasets, and task formulations, limiting a systematic understanding of when, how, and why generative models succeed or fail in real-world settings. To address this gap, we introduce SensorGen, a large-scale study of sensor-signal generation spanning 14 settings across 4 domains, 7 datasets, and 12 signal modalities. Leveraging SensorGen, we systematically evaluate generative models from five major families and uncover three key findings: (1) flow-matching models provide strong overall performance across most settings; (2) signal properties matter, with demographic covariates improving longitudinal generation and time-frequency modeling improving high-frequency signal generation; and (3) generated signals have practical utility beyond visual realism, with scaling improving generation quality and synthetic data improving downstream performance. Together, SensorGen establishes a broader understanding of design choices, evaluation protocols, and failure modes in real-world sensor data generation.

---


### 329. [AdaptiveSplat:Texture Aware Controllable 3D Gaussian Allocation for Feed-Forward Reconstruction](https://arxiv.org/abs/2607.04256)

**<font color=#1a73e8>作者：</font>** Badrinath Singhal, Srihari K G, Sreehari Iyer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current feed-forward 3D reconstruction methods predict pixel aligned Gaussian primitives, resulting in highly redundant representations. A natural solution is to prune the redundant Gaussians, but naive pruning introduces severe artifacts and often requires inference time fine-tuning, breaking the feed-forward paradigm. Based on previous works, high frequency regions require more Gaussian primitives, while low frequency regions can be represented with significantly fewer primitives. Motivated by this, we propose a novel approach to explicitly control the number of Gaussians by leveraging local texture information. Our approach achieves this through three key components: (1) texture estimation to capture spatial variation in scene detail, (2) texture-aware pruning that removes redundant Gaussians from low frequency regions, and (3) an adaptive Gaussian head that predicts the modified attributes of the retained primitives without breaking the feed-forward paradigm. Experiments on RE10K, ACID, DL3DV, Tanks and Temples, and DTU demonstrate the effectiveness of our approach, while ablation studies validate the contributions of its key components.

---


### 330. [Shortcut Learning in Legal Judgment Prediction: Empirical Evidence from the UK Employment Tribunal](https://arxiv.org/abs/2607.04261)

**<font color=#1a73e8>作者：</font>** Joe Watson, Joana Ribeiro de Faria, Marcus Tomalin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current Legal Judgment Prediction (LJP) is constrained by its reliance on post-hoc judicial materials, increasing the likelihood that models perform retrospective classification rather than true forecasting. This paper empirically investigates shortcut learning in this context by studying claim-level outcome prediction in UK Employment Tribunal (UKET) decisions. Using a corpus of 33,158 individual claims, we predict outcomes from claim texts and LLM-extracted case summaries, evaluating models ranging from interpretable TF-IDF-based classifiers to black-box LLMs. While headline predictive performance figures appear strong, we demonstrate that such performance in LJP systems trained on post-hoc judicial text can be driven by the retrospective nature of the source material. Stratifying the test data by human judgments of leakage reveals that performance increases where outcome-revealing cues are embedded in the narrative. Moreover, a model trained on just the 4% of features identified as leakage achieves high performance, outperforming human experts. These findings substantiate concerns that LJP performance may be exaggerated by linguistic artefacts. Yet this vulnerability is not fatal to the research agenda. Instead, post-hoc judgments might be treated as potentially contaminated texts, requiring active auditing. Retraining models after masking leakage features results in only a negligible reduction in Macro-F1. Hence, while models will opportunistically exploit shortcuts when available, they remain capable of extracting useful predictive signals when these artefacts are removed.

---


### 331. [On Preserving Geometrical Invariance for Superpixel Image Classification using Graph Transformer](https://arxiv.org/abs/2607.04262)

**<font color=#1a73e8>作者：</font>** Sarabeshwar Balaji, Shubham Mohanty, Akash Anil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Convolutional Neural Network (CNN) and Vision Transformer (ViT) for image classification exploit a dense grid of pixels containing redundant information. Consequently, for a larger image dataset, CNNs and ViTs face deployability challenges due to high computational complexity. Representing images as graphs of superpixels offers an efficient alternative that preserves key information while eliminating pixel-level redundancy. Graph Neural Networks (GNNs) have been utilized on such graphs to perform image classification. However, GNNs are known to struggle with capturing long-range dependencies which is important in the domain of image classification. Furthermore, a majority of these superpixel-based image classification approaches do not explicitly preserve translation/rotation invariance. Nevertheless, preserving translation/rotation invariance is important for robust image classification. Thus, this paper proposes SuperGT, a Graph Transformer-based framework for image classification, which captures the long range dependencies, along with a pre-processing scheme that preserves translation/rotation invariance. We evaluate SuperGT on CIFAR-10 dataset and observe that it performs significantly better than many baselines. Furthermore, we note that the overall performance of SuperGT is comparable to the previous state-of-the-art model, namely, ShapeGNN, without relying on coordinates of the boundary points of each superpixel required by ShapeGNN.

---


### 332. [EMPURPLE: A Free Lunch for Diffusion Distillation based on the Information Bottleneck](https://arxiv.org/abs/2607.04276)

**<font color=#1a73e8>作者：</font>** Zilai Li, Lujia Bai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models achieve impressive image-generation quality but remain expensive at inference time. Diffusion distillation reduces sampling steps, yet many distilled models, including SDXL-Lightning and distribution matching distillation methods, suffer from degraded Fréchet Inception Distance (FID). We analyze this phenomenon through a PAC-style generalization bound. Our analysis suggests that aggressive early-step redirection of the velocity field makes the distillation target harder to learn, enlarging the train-test gap. As a result, early-step output distributions differ between training and inference, causing distribution mismatch in the intermediate noisy latent used as next-step inputs. We empirically validate this mechanism by showing reduced diversity in both intermediate features and final outputs. To address this issue, we propose EMPURPLE, a simple training-free method that recycles intermediate latents sampled from the original model. EMPURPLE is model-agnostic and improves FID by 7\% to 20\% across DMD2, Hyper-SD, FlashSD, and SDXL-Lightning. The repo is: this https URL

---


### 333. [The New Shape of Search: How Conversational AI Recomposes Information Seeking](https://arxiv.org/abs/2607.04282)

**<font color=#1a73e8>作者：</font>** Michael Iannelli, Alan Ai  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Classic models cast information seeking as iterative foraging: formulate a keyword query, scan results, reformulate, gather across sources, synthesize. We ask what happens when a conversational assistant is inserted into that episode. Linking real conversations with major assistants to the same users' searches and browsing in an opt-in cross-surface panel, and reconstructing the full episode rather than a single query, we find conversational AI changes the shape of information seeking, not merely its volume. AI episodes do not uniformly collapse; they bifurcate. Most terminate in place, with no onward search or content step in the observed trace, while roughly a third scaffold into longer multi-step journeys. Which shape occurs is governed less by task type than by articulation: collapse is statistically indistinguishable across lookup, learning, and comparison episodes, yet falls monotonically with opening-ask length, from 72% at one-to-three words to 48% beyond twenty. Roughly two-fifths of assistant episodes are workbench use--drafting, coding, editing--not information seeking at all, and these collapse most. Conversational AI also does not displace search: search remains woven through roughly three-quarters of within-episode transitions, after reading a page users return to the search box over the assistant 70/30, and within-user search share does not fall. Verification is rare: searches with explicit verification language follow roughly 1% of episodes, and citation-forward interfaces do not measurably increase checking. All of this is episode structure, a compositional object identifiable without a demand counterfactual. Conversational AI recomposes the seeking episode: it answers brief asks in place and anchors invested asks in longer journeys, adding a layer rather than replacing search.

---


### 334. [AquaStereo: Enabling Underwater Stereo Matching via Depth-Conditioned Diffusion and Geometry Self-Distillation](https://arxiv.org/abs/2607.04303)

**<font color=#1a73e8>作者：</font>** Qizhe Wei, Yingping Liang, Shaodi You 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning-based stereo matching models struggle in underwater environments due to scarce in-domain data and the difficulty of extracting discriminative correspondences from degraded imagery. In this work, we present $\textbf{AquaStereo}$, a perception-enhanced framework with a data simulation pipeline and a self-distillation strategy that jointly address data scarcity and feature degradation in underwater stereo matching. First, a depth-conditioned diffusion pipeline renders underwater stereo pairs while preserving binocular geometry, with a lightweight left-right consistency module ensuring geometric alignment. Training on this synthetic corpus effectively narrows the terrestrial-underwater gap and improves zero-shot robustness. Second, a frozen binocular teacher trained on clean terrestrial pairs guides a student exposed to rendered underwater pairs with perturbations. A stage-weighted sequence loss is performed to align the student's disparities with the teacher's geometry, while a clean-branch supervision with shared pseudo targets prevents scale drift. To further enhance feature stability under turbidity and low texture, we introduce learnable perception frames, a perception-enhanced feature formulation that constructs robust matching descriptors by fusing temporal cues from two auxiliary views encoded by a video backbone with semantic features extracted by a strong image encoder. Extensive experiments demonstrate that $\textbf{AquaStereo}$ substantially improves robustness and zero-shot generalization in challenging underwater scenarios. The code is available at this https URL.

---


### 335. [Road-Aware Anomaly Segmentation with Query-Guided Polygons and CLIP in Autonomous Driving](https://arxiv.org/abs/2607.04304)

**<font color=#1a73e8>作者：</font>** Zhiran Yan, Gordon Elger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional semantic segmentation models operate under a closed-set assumption and struggle to recognize unknown or unexpected objects-an essential capability for autonomous driving. As a result, such models often misclassify or overlook out-of-distribution (OOD) road anomalies, posing safety risks in open-world environments. We present a lightweight, postprocessing, road-aware anomaly segmentation framework that requires no retraining, no OOD data, and no auxiliary supervision. Our approach builds on a mask transformer-based segmentation network by exploiting query-level mask confidence and deriving a polygonal road prior to detect gap regions that may correspond to anomalies. To further suppress false positives, we introduce a CLIP-based zero-shot semantic filtering module using in-distribution prompts, with optional generalized OOD prompts. By jointly leveraging spatial priors and semantic verification, our framework produces robust and interpretable anomaly predictions. Evaluation on three public benchmarks-Fishyscapes, SMIYC, and RoadAnomaly-shows consistently strong performance. In particular, our method outperforms the training-free baseline Maskomaly on most metrics and achieves the highest AP on Fishyscapes LostAndFound. These results demonstrate the practicality and deployability of our approach for real-world autonomous driving systems.

---


### 336. [Legible-by-Construction: Attention and End-to-End Transformers](https://arxiv.org/abs/2607.04319)

**<font color=#1a73e8>作者：</font>** Mark Oskin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A companion paper showed that a transformer's feed-forward layer can be rebuilt from explicit fuzzy set operations - intersection, set-difference, and a self-forgetting sequence quantifier - so its hidden units read as named logical operators at no cost to language-model quality. That left the other half of the transformer opaque. Here we carry the same idea into attention and join the two into one model. The mechanism is minimal: a head's value is passed through a sigmoid, so each value channel becomes a readable detector of whether a feature holds at a token. This adds no parameters and leaves the standard head otherwise untouched. A Boolean variant goes further, restructuring the value into an explicit within-token intersection and negation-capable set-difference. In both designs the output projection is left free, not tied to the vocabulary, which is the load-bearing decision: bounding what a head detects while leaving what it writes unconstrained yields selective detectors, whereas constraining the write does not. A bounded value is shaped into a readable detector by two selectivity pressures - one for sparse firing, one for decisive firing at the rails - and which a design wants is not universal. Across five specialized-attention designs at 125M parameters, 44 to 62 percent of value channels become crisp, contextually selective detectors, and their legibility rises with depth rather than crystallizing only on punctuation. Language-model quality is at parity with a conventional baseline. Finally, we couple the Boolean attention to the legible feed-forward layer and train an end-to-end legible-by-construction language model at benchmark parity: its feed-forward units are named set and quantifier operations throughout, and we can take a token it generates and read the named units that compose to produce it.

---


### 337. [Framework and Multi-modal Dataset for Roadwork Zone Detection and Geo-localization](https://arxiv.org/abs/2607.04330)

**<font color=#1a73e8>作者：</font>** Zhiran Yan, Yutong Xin, S Shyam Shenoi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles often rely on high-definition (HD) maps for navigation; however, these maps are not frequently updated and often lack semi-static information, such as temporary roadwork zones, which can significantly alter the road network. This limitation underscores the urgent need for an accurate global position of roadwork zones. However, the absence of publicly available datasets for evaluating roadwork zone detection and geo-localization models has hindered the development of reliable autonomous driving systems. To address this challenge, we propose the Roadwork Zone Detection and Geo-localization (RZDG) dataset, which includes both simulated and real-world data, providing multimodal sensor inputs along with comprehensive annotations. The dataset supports multiple perception tasks, including image semantic segmentation, 3D object detection, and object geo-localization. In addition, we introduce a tracker-based roadwork zone detection and geo-localization (RZDG) pipeline, an extension of AB3DMOT, for accurate object geo-localization in roadwork zones. We benchmark our approach on the RZDG dataset, demonstrating its effectiveness in detecting roadwork zones and transforming object positions from the local coordinate system to the global coordinate system. A prediction is considered a true positive (TP) if its estimated position falls within one meter of the ground truth. Our experimental results show that our approach achieves high accuracy on both real and simulated data. Specifically, we report: Precision: 0.565 (real) / 0.615 (simulated) Recall: 0.898 (real) / 0.809 (simulated) F1-score: 0.597 (real) / 0.665 (simulated).

---


### 338. [Structure-Specific Representational Priors Causally Control the Grokking Delay](https://arxiv.org/abs/2607.04333)

**<font color=#1a73e8>作者：</font>** Gunner Levi Howe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking -- generalization arriving long after training-set interpolation -- can be accelerated by structure-agnostic interventions: gradient filtering, weight-norm clamping, geometric penalties on hidden representations. Whether the delay specifically measures the time to form task-structured representations has remained an observational claim. We test it causally by injecting representational priors of varying structural content into a one-layer transformer learning modular addition: a supervised-contrastive auxiliary loss whose positives encode (i) the task's true equivalence structure ($(a+b) \bmod p$), (ii) a coherent-but-wrong sibling structure ($(a-b) \bmod p$), or (iii) a random partition, all with identical loss form, strength, class sizes, and geometry. Whether generalization occurs follows a clean gradation: true structure 22/30 runs; sibling structure, which needs the same periodic features but the wrong combination, 14/15; random partition, satisfiable only by memorization, 0/20 (Fisher exact $p = 1.3 \times 10^{-7}$). A weight-norm-matched control replaying each intervention's norm trajectory onto plain cross-entropy generalizes in 0/15, collapsing into logit-scale saturation, ruling out the norm as mediator. Representation probes show structure formation precedes and predicts generalization in all 95 runs. Only the true structure also accelerates grokking, up to $2.75\times$ faster than baseline, but the acceleration is dose-dependent, bimodal across seeds, and a net wall-clock win only in its strongest cases given the contrastive term's overhead. The grokking delay is, causally, the time to form the right representational structure, where "right" is decided at the level of features rather than labels: coherent-but-wrong structure leaves grokking intact, random structure abolishes it, and only the true structure hastens it.

---


### 339. [Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure](https://arxiv.org/abs/2607.04334)

**<font color=#1a73e8>作者：</font>** Guijia Zhang, Harry Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal GUI agents read an interface through two redundant channels: the rendered pixels of a screenshot and a serialized structure such as a DOM or accessibility tree. Before acting, an agent forms a belief about the current interface state, but existing benchmarks score task success, element grounding, or attack resistance and do not ask whether that belief is drawn from the pixels. We formalize visual state reliance, the attribution of a state belief to pixels, structure, or priors, and measure it with paired single-channel interventions over 310 real web, mobile, and desktop probes. Every probe is scored by deterministic forced choice, with no model-generated item and no model judge. Our central metric is the Perception-Fusion Gap, the fraction of probes a model perceives correctly yet resolves toward structure under conflict. Across five models from three vendors, textual state beliefs defer to structure while image-only accuracy stays near ceiling, and Perception-Fusion Gap is positive for every model; non-text identity, by contrast, stays largely pixel-bound. The substitution is specific to the serialized-text and indexed-action channel, and coordinate-action agents are largely immune. For textual conflicts, a white-box ablation traces the effect to a single copied structural value, and in two live environments the conflict drives wrong actions and real task failure. Visual state reliance therefore gives a measurable diagnostic of whether agent state beliefs are visually grounded, and the errors it exposes propagate to actions.

---


### 340. [Server-side Anti-cheat in FPS games for Aimbot detection using Deep learning and Machine learning](https://arxiv.org/abs/2607.04336)

**<font color=#1a73e8>作者：</font>** Siddhesh A. Dhinge, Shubham G. Sukum, Harsh S. Ranjane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern video games are becoming more complex day by day. Most of these modern games are multiplayer first-person shooter (FPS) games. The rising popularity of FPS games emphasizes the need to combat cheating for fair and enjoyable gaming. As the number of players using cheating techniques like aimbots, wallhacks, and speed hacks is also increasing, we need a way to detect players who are using cheating tools to gain an unfair advantage over regular players. In this system, we focus exclusively on detecting aimbot cheats. Players who use aimbot cheats generally do not prioritize other aspects of the game. To distinguish between regular and cheating players, we identify specific features encompassing time-series data such as aim velocity, number of shots, distance to target, and more, along with behavioral data such as utility usage, player movement, and other gameplay patterns. Utilizing these features, we construct a server-side aimbot detection classifier named 'YAACS'. YAACS comprises a parser, a deep learning model, and intermediary connection utilities designed for integration with the game server. The proposed system achieves a classification accuracy of 88.6% with a false positive rate of 0.97% using a Stacked LSTM with Dense layers trained on sequences of 128 ticks (Tick Delta Negative=56, Tick Delta Positive=24), outperforming the Decision Tree baseline which achieves a higher accuracy of 96.2% but at a false positive rate of 2.68%, 2.76x worse than the best LSTM configuration. These results demonstrate that incorporating temporal context through sequence modelling is critical for minimising false accusations in FPS cheat detection.

---


### 341. [One Framework for All: Cross-Modal Membership Inference for Generative Models](https://arxiv.org/abs/2607.04339)

**<font color=#1a73e8>作者：</font>** Dayong Ye, Tainqing Zhu, Kun Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large generative models across text-to-text, text-to-image, and image-to-text modalities have been shown to pose significant privacy risks. One fundamental threat is membership inference attacks (MIA), which aim to determine whether a given data point was used in a model's training set. Although prior work has investigated MIAs against these three classes of generative models, existing approaches treat them in isolation and are not cross-applicable, thereby limiting their real-world utility. To address this limitation, we present the first comprehensive study of a unified membership inference framework that applies across text-to-text, text-to-image, and image-to-text modalities. Our approach is grounded in a key modality-agnostic observation: the output distribution of a generative model can approximate its training data distribution. Leveraging this property, we model the distributions of model-generated outputs and auxiliary non-member samples in a shared embedding space, and perform membership inference via likelihood ratio testing. We conduct extensive experiments in a strict black-box setting under both partial-knowledge and zero-knowledge threat models, and evaluate membership inference against both fine-tuning and pre-training data. Experimental results demonstrate our approach's superior performance in comparison to existing state-of-the-art methods, which are typically optimized for a single model class.

---


### 342. [Last-Meter Precision Navigation for UAVs: A Diffusion-Refined Aerial Visual Servoing Approach](https://arxiv.org/abs/2607.04352)

**<font color=#1a73e8>作者：</font>** Yaxuan Li, Jiarui Zeng, Shaofei Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we study the last-meter precision navigation for UAVs, e.g., autonomously reaching a target within the final 10 meters using monocular vision. This task is challenging due to scale ambiguity, rotation discontinuities, and the need for fine-grained spatial reasoning. Existing methods often fail under large viewpoint changes or lack generalization to unseen environments. To this end, we propose DreamNav, a coarse-to-fine diffusion-refined aerial visual servoing framework. In the first coarse-estimation stage, a robust regression policy employs a trigonometric parameterization to predict rotation by jointly modeling sine and cosine components, effectively mitigating optimization instabilities caused by angular periodicity. Given this coarse estimate, the second diffusion-refined stage utilizes a pre-trained world model to simulate future visual observations for candidate actions, selecting the trajectory that minimizes visual discrepancy with the target through a process of visual imagination. To support rigorous evaluation, we contribute PairUAV, a large-scale benchmark comprising 4.8 million image pairs across 72 scenes, curated from the University-1652 dataset. Extensive experiments show DreamNav outperforms strong visual servoing and foundation model baselines in accuracy and generalization, with zero-shot transfer to unseen scenes.

---


### 343. [HASSL: Hierarchy-Aware Self-Supervised Learning Framework for Single Cell Microscopy](https://arxiv.org/abs/2607.04353)

**<font color=#1a73e8>作者：</font>** Julius Riel, Vishwa Mohan Singh, Sai Anirudh Aryasomayajula 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hierarchical structure is common in image data, where fine-grained clusters often merge into larger, coarser semantic groups. In biological cell images, current self-supervised learning models often suppress this hierarchy, as coarse factors such as imaging modality can obscure finer morphological attributes in the latent space. We propose a hierarchy-aware self-supervised training framework to address this problem. Our method combines two components: a distillation framework with a segmentation teacher to improve morphological awareness in the latent space, and a hierarchy-aware contrastive loss based on HDBSCAN to improve decision boundaries between closely related subtypes at different hierarchical levels. Together, these components reduce the tendency of self-supervised learning to overemphasize coarse factors and instead align embeddings with semantic and morphological cues. This yields biologically meaningful sub-clusters driven by fine morphological detail. We train and evaluate our method on a curated corpus of 2.3 million single cells aggregated from 20 microscopy datasets, both labeled and unlabeled, covering 208 cell classes. Our method improves over baseline and counterpart methods, increasing average top-K accuracy by 2.8%, top-9 retrieval on the dataset with the deepest hierarchy by 6.3%, and downstream F1-score for biologically relevant drug classification from perturbed cell morphology by 7.8%.

---


### 344. [How Many Initial Points Does Bayesian Optimization Need?](https://arxiv.org/abs/2607.04356)

**<font color=#1a73e8>作者：</font>** Mujin Cheon, James Odgers, Dong-Yeun Koh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian Optimization (BO) generally begins with an initialization phase: a batch of $n_0$ uninformed evaluations. The choice of $n_0$ remains largely heuristic, and we empirically observe that the total cost (random initial points plus BO iterations needed to find the global optimum) is U-shaped in $n_0$, i.e., a practitioner wastes resources by selecting either too low or too high a value of $n_0$. We find this tradeoff persists across MLE, Bayesian MCMC, and exact GP hyperparameters, as well as across acquisition functions. Toward the latter, Thompson Sampling appears an exception, with both total cost and simple regret essentially $n_0$-agnostic, though higher in our experiments. We attribute this U-shape to the known boundary issue of variance-driven BO: BO burns early budget on corners of the hypercube before turning inward. We demonstrate this effect using a 3D BO trajectory where the exact hyperparameters are known. We conclude with practical recommendations: use multi-step lookahead BO where possible; otherwise use Thompson Sampling when $n_0$ cannot be tuned, and a generously large $n_0$ when it can.

---


### 345. [Event Detection in Videos: A Framework for the Development of New Methods](https://arxiv.org/abs/2607.04372)

**<font color=#1a73e8>作者：</font>** Anastasia Zakharova, Thierry Bouwmans, Anthony Cioppa 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event detection tasks in videos, the most important aspect of video surveillance, aim to detect events either at the pixel-level, frame-level, or clip-level. Plenty of methods intended for event detection in different environments, for various applications, and within different acquisition techniques were introduced. Naturally, the attempts were made as well to classify these algorithms in terms of detection of performance or in terms of real-time abilities. Nevertheless, the lack of a large-scale dataset as well as rigorous performance evaluation methods have biased such comparisons as well as the development of the methods.
Given the diversity of existing approaches, we believe it is essential for researchers to position their work within such a rich landscape. Thus, we propose a rigorous framework for developing new methods in event detection for videos. Specifically, this framework is based on three main pillars: datasets, performance evaluation, and scenarios for deploying methods.

---


### 346. [The ABC of digital health: A framework for translating digital health interventions into real-world applications](https://arxiv.org/abs/2607.04381)

**<font color=#1a73e8>作者：</font>** David Grüning, Vincent Beermann, Jan Enkmann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Research-based digital health interventions are often presented as potential solutions for extending health care in the real world. Yet the vast majority of these interventions fails to move beyond controlled studies. Existing frameworks offer valuable guidance for intervention development and testing, but provide less concrete support for translating these evidenced intervention mechanisms into sustained real-world applications. This paper introduces the ABC framework, referring to Accessibility, Buildability, and Continuity, as a practical model for a successful translation. Accessibility captures whether diverse users can find, understand, and begin using an application with minimal friction. Buildability refers to the development of an app that supports the iteration, integration, and personalization of features. Continuity describes both sustained user engagement and the operational capacity to maintain an application over time without disproportionate increases in cost, infrastructure, or human support. Different combinations of the ABC-dimensions make an application scalable (AB), automated (BC), and adherent (AC). By linking design decisions to these features, ABC offers a shared language for researchers, designers, and policymakers seeking to build or evaluate digital health interventions that work beyond trials and are viable applications in everyday life.

---


### 347. [Environmental Drivers of Respiratory Disease: A District Level Analysis](https://arxiv.org/abs/2607.04416)

**<font color=#1a73e8>作者：</font>** Rahim Iqbal, Asfi Ahamed, Izzath Nisfer 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sri Lanka has experienced a decade of progressive forest degradation and rising atmospheric pollution, yet district-level respiratory admissions have paradoxically declined, pointing to the confounding role of healthcare access. This study addresses that gap by constructing an 11-year (2014-2024) panel dataset across all 25 administrative districts, integrating satellite-derived vegetation indices, fire radiative power, pollutant concentrations (particulate matter (PM2.5), nitrogen dioxide (NO2), sulfur dioxide (SO2)), carbon flux metrics and population-normalized respiratory admission rates. Two temporally validated XGBoost models were created for annual district-level respiratory rate (R^2 = 0.937) and monthly PM2.5 concentration (R^2 = 0.976) with generalization validated in 21 out of 25 districts (Mean Absolute Percentage Error (MAPE) <= 20%). Shapley Additive Explanations (SHAP) analysis established that cumulative air quality burden is the overwhelming driver of respiratory rate variance (80.1%), ahead of forest degradation (15.6%) and fire activity (4.3%). The Forest-Air-Health (FAH) Risk Index used these SHAP-derived weights to find the districts with the highest risk: Colombo (FAH = 0.802), Gampaha (0.708), and Kalutara (0.682). These findings present the inaugural evidence-based, district-level framework correlating environmental degradation with respiratory health in Sri Lanka, establishing a quantitative basis for focused public health and environmental policy.

---


### 348. [UI-MOPD: Multi-Platform On-Policy Distillation for Continual GUI Agent Learning](https://arxiv.org/abs/2607.04425)

**<font color=#1a73e8>作者：</font>** Niu Lian, Alan Chen, Zhehao Yu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal foundation models and agent systems have driven GUI agents from single-platform task execution toward cross-platform interaction. However, building multi-platform GUI agents remains challenging. On one hand, high-quality and executable cross-platform interaction trajectories are still scarce, and existing data often suffer from limited platform coverage. On the other hand, different platforms exhibit distinct interaction conventions, making joint or continual training prone to behavioral pattern mixing, platform-specific capability degradation, and catastrophic forgetting. To address these challenges, we construct Uni-GUI, a high-quality cross-platform GUI interaction dataset, and propose UI-MOPD, the first method that incorporates multi-teacher on-policy distillation into continual learning for GUI agents. UI-MOPD dynamically selects a platform-specific teacher according to the current environment and transfers platform-specific behavioral priors to a shared policy through platform-conditioned distillation, enabling adaptation to new platforms while preserving capabilities on existing ones. Experiments on OSWorld and MobileWorld show that UI-MOPD achieves task success rates of 38.2% and 12.0%, respectively, demonstrating its effectiveness in balancing cross-platform capability retention and new-platform adaptation.
Project page: this https URL.

---


### 349. [ResearchStudio-Reel: Automate the Last Mile of Research from Paper to Poster, Video, and Blog](https://arxiv.org/abs/2607.04438)

**<font color=#1a73e8>作者：</font>** Lingao Xiao, Yalun Dai, Yangyu Huang 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Research dissemination, turning a paper into a poster, a talk video, and a blog post, is still a manual last mile. Prior automation treats each artifact in isolation that each re-extract the paper from scratch, usually ship one-way renders the author cannot reopen in PowerPoint or Word, and gates quality on soft VLM-preference scores that plateau while load-bearing sections still read as empty. We argue this last mile is best built as a composition of skills: thin agent-readable contracts that share one upstream extractor and wrap deterministic primitives in a measured-fill loop whose exits are hard pass/fail render gates. We instantiate this as ResearchStudio-Reel, five Claude Code and Codex skills organized into one shared extractor (Paper2Assets), three editable generators (Paper2Poster, Paper2Video, Paper2Blog), and one interactive convergence layer (Paper2Reel). Paper2Assets extracts each paper once into a shared bundle that can be reused by every downstream skill; The three generators produce a print-ready poster, a synchronized talk video, and a bilingual blog that stay factually consistent and round-trip through PowerPoint or Word; Paper2Reel then binds all three into a self-contained HTML viewer whose section-level clicks jump the video, slides, captions, and blog to matching content. On the Paper2Poster benchmark, our posters lead every aesthetic and information sub-criterion against both prior automated systems and single-shot frontier LLMs, surpassing the authors' own on aesthetics under two held-out VLM judges and winning overall on 84% to 93% of papers; capability audits further show that, by uniquely pairing narration-aligned on-slide highlights with a bilingual blog gated by layout-aware DOCX repair, ResearchStudio-Reel is the only pipeline to ship all three editable artifacts. Project is available at this https URL

---


### 350. [ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://arxiv.org/abs/2607.04439)

**<font color=#1a73e8>作者：</font>** Qihao Zhao, Yangyu Huang, Yalun Dai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have made research ideation increasingly accessible, yet effective idea development requires more than generating candidate directions. Researchers must ground a problem in current literature, identify meaningful bottlenecks, differentiate from existing solutions, and evaluate risks before committing to implementation. We present ResearchStudio-Idea as a reusable skill suite for this first mile of research ideation. The suite includes Paper-Search, a standalone multi-source literature search skill; Scoop-Check, a standalone prior-art collision checker for novelty claims; and IdeaSpark, the end-to-end skill that composes evidence grounding, pattern-guided generation, collision retrieval, audit, and idea-card rendering into one workflow. IdeaSpark is constructed from a corpus of 1,947 machine learning conference papers collected from ICLR, ICML, and NeurIPS between 2021 and 2025, including Oral papers, a separately tracked high-citation subset, and rejected submissions. Analysis of these outcomes reveals 31 recurring ideation sub-patterns, consolidated into 15 reusable ideation patterns. Each pattern is operationalized as a structured card containing research contexts, bottleneck types, differentiation strategies, supporting precedents, and common failure modes. Given a research problem and an evidence bundle, IdeaSpark evaluates evidence readiness, reconstructs the surrounding research context, identifies unresolved bottlenecks, selects relevant patterns, instantiates one candidate direction, retrieves potentially conflicting prior work, and performs outcome-informed auditing. This workflow transforms reusable ideation patterns into traceable research proposals. Blind automated-judge evaluations show that IdeaSpark consistently produces stronger research proposals than no-skill and generic-skill baselines while maintaining competitive novelty.

---


> [!TIP]
> 当前位于：**301-350**（第 7/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
