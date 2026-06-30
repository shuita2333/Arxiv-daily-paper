# 📦 其他研究 | 2026年07月01日

> 本类共 **489** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-489**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-489**

---

### 451. [RBE-Flow: Recurrent Bayesian Estimation on Feature Manifolds for Cross-Modal Registration](https://arxiv.org/abs/2606.30492)

**<font color=#1a73e8>作者：</font>** Mengzhu Ding, Xin Song, Xiaoke Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal image registration is essential for multi-sensor perception but remains fundamentally challenging due to severe non-linear radiometric discrepancies and geometric distortions. Existing deterministic matching methods lack uncertainty awareness, struggling to navigate the resulting highly non-convex optimization landscape and frequently accumulating errors in ambiguous regions. In this paper, we propose RBE-Flow, a novel framework that reformulates dense cross-modal flow estimation as a closed-loop recurrent Bayesian estimation problem on learned feature manifolds. Diverging from standard feed-forward regression, RBE-Flow establishes a robust self-correcting mechanism by deeply coupling feature-metric non-linear optimization with probabilistic state updates. Specifically, a Recurrent Manifold Optimization (RMO) block iteratively generates flow observations and their associated uncertainties, which are then optimally assimilated into the prior state via an Uncertainty-Adaptive Probabilistic Update (UAPU) using deterministic sigma-point projection. Crucially, the resulting calibrated posterior covariance is fed back to adaptively regularize the damping of subsequent optimization steps, allowing the system to modulate its convergence based on predictive confidence. To ensure stable probabilistic training, we introduce a hybrid supervision scheme featuring a geometry-aware rectified NLL loss that structurally prevents variance collapse. Extensive experiments on challenging OSdataset, WHU-OPT-SAR, and RoadScene benchmarks demonstrate that RBE-Flow consistently achieves state-of-the-art performance, outperforming existing methods by a significant margin, particularly under strict sub-pixel criteria. Project page: this https URL

---


### 452. [Between Zeros and Ones: Behavioral Characterization Beyond Binary Labeling Across Public ICS Datasets](https://arxiv.org/abs/2606.30493)

**<font color=#1a73e8>作者：</font>** Konstantinos E. Kampourakis, Vyron Kampourakis, Georgios Spathoulas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intrusion detection in Industrial Control Systems (ICS) is typically evaluated on a small set of public benchmarks using binary ``normal'' versus ``attack'' labels, a practice that can mask the behavioral diversity of cyber-physical attacks. To address this limitation, we propose a behavioral characterization framework that maps raw multivariate process traces into five interpretable physical primitives: drift, spike, oscillation, repetition, and switching. We apply the framework to three widely used ICS benchmarks, namely, SWaT, WADI, and HAI, and show that attack windows exhibit clear behavioral shifts relative to normal operation while the three datasets occupy largely distinct regions of the behavioral space, revealing both cross-dataset bias and intra-dataset diversity. In particular, WADI is dominated by repetition, HAI emphasizes sustained drift and oscillation, and SWaT is characterized by stealthier frozen-telemetry behavior. To examine the evaluation implications, we use an indicative Random Forest baseline and show that aggregate binary metrics can limit visibility into performance across different behavioral proxies. For example, in SWaT, macro F1 drops from 85.44% under binary evaluation to 37.84% under behavior-proxy multiclass prediction, with similar degradations observed on WADI and HAI. Based on these findings, we argue for complementing conventional binary benchmarking with behavior-stratified evaluation to expose blind spots that aggregate scores leave hidden and to better support targeted incident response.

---


### 453. [On the Faithfulness of Post-Hoc Concept Bottleneck Models](https://arxiv.org/abs/2606.30498)

**<font color=#1a73e8>作者：</font>** Laines Schmalwasser, Jan Blunk, Niklas Penzel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human decision-making interprets the world through high-level concepts, such as recognizing a bird by its belly color. To bridge the gap between opaque deep learning representations and human understanding, Post-Hoc Concept Bottleneck Models (post-hoc CBMs) project latent features onto interpretable concept spaces using auxiliary datasets or vision-language models. However, relying on target task accuracy as the primary measure of post-hoc CBM success obscures whether the learned concepts are semantically meaningful or merely predictive artifacts. For example, random concept projections can achieve competitive accuracy despite being semantically meaningless. In this work, we analyze the learned projections directly and identify two failure cases: First, for concept projections learned from auxiliary data, covariate shifts can lead to unfaithful concept representations for the target task. In particular, we provide an upper bound on the error introduced by this shift. Second, systematic label noise in surrogate concept labels generated by vision-language models leads to unfaithful projections. After formalizing these failure modes, we introduce novel metrics that decouple concept faithfulness from predictive accuracy. Our empirical results across real-world and synthetic benchmarks confirm that these metrics identify unfaithful behaviors that standard accuracy-based evaluation fails to detect.

---


### 454. [Discovering Collaboration from Novelty: Random Network Distillation for Clustered Federated Learning](https://arxiv.org/abs/2606.30499)

**<font color=#1a73e8>作者：</font>** Davide Domini, Gianluca Aguzzi, Ivana Dusparic 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning often suffers under non-independently and identically distributed data, where a single global model may fail to represent the diversity of client distributions. Clustered Federated Learning mitigates this issue by training specialized models for groups of similar clients, but existing approaches often couple cluster assignment with the main training loop, increasing computational and communication costs. We propose a lightweight clustering approach based on Random Network Distillation. Each client trains a compact Random Network Distillation predictor on its local data and uses its prediction error as a novelty signal to estimate similarity with other clients. This enables the discovery of meaningful client groups before federated training, without sharing raw data or repeatedly evaluating the main model. Crucially, the resulting federations emerge from local novelty estimates at runtime, making the method suitable for autonomous large-scale distributed systems where neither the number of clusters nor the collaboration structure can be specified a priori. Overall, by decoupling clustering from learning, the method provides a task-agnostic and efficient mechanism for autonomous collaboration under non-independently and identically distributed data.

---


### 455. [Muon learns balanced solutions in matrix factorization without slow saddle-to-saddle dynamics](https://arxiv.org/abs/2606.30509)

**<font color=#1a73e8>作者：</font>** Mark Rhee, Jamie Simon, Dhruva Karkada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix factorization (i.e., problems of the form $\min_{\mathbf{P},\mathbf{Q}} \|\mathbf{M}^\star - \mathbf{P}^\top\mathbf{Q}\|_\mathrm{F}^2$) is a minimal learning problem that exhibits both nonlinear parameter dynamics and representation learning. In this setting, we study how parameter trajectories under the Muon optimizer differ from those of gradient descent. We identify three main dynamical differences: 1) Muon avoids the slow saddle-to-saddle dynamics from small initialization. Muon instead learns all the top modes of $\mathbf{M}^\star$ at the same rate, with the smaller modes converging first. 2) Muon remains stable even when the learning rate exceeds the critical threshold set by the local loss sharpness. This frees the learning rate from the condition number of the problem, enabling rapid convergence via exponential learning rate annealing. 3) Once the weights are aligned with each other and the target, Muon flow conserves the matrix quantity $\sqrt{\mathbf{P}^\top \mathbf{P}}-\sqrt{\mathbf{Q}^\top \mathbf{Q}}$, while gradient flow is known to conserve the matrix $\mathbf{P}^\top\mathbf{P} - \mathbf{Q}^\top\mathbf{Q}$. Despite having distinct conserved quantities, both optimizers find the so-called \textit{balanced} solution from vanishing initialization. When training from small random initialization, the weights spontaneously align early in training. We derive the alignment rates in simple settings and show that they predict the empirical alignment rates in general. Finally, we exploit structural properties of Muon to construct a learning rate schedule that achieves near-perfect alignment in only two optimization steps.

---


### 456. [High-Resolution Flood Mapping With Sentinel-1 and Sentinel-2 via Misalignment-Robust Cross-Sensor Learning and Generative Despeckling](https://arxiv.org/abs/2606.30511)

**<font color=#1a73e8>作者：</font>** David Ma, Jeremy Feinstein, Shreya Pandit 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable high-resolution flood extent mapping from satellite imagery remains constrained by limited data fidelity and sensor-specific artifacts. Multispectral optical imagery is degraded by clouds, shadows, and urban confounders, while synthetic aperture radar (SAR) imagery is affected by speckle noise and sensor co-registration uncertainty. This work presents an integrated flood mapping framework that jointly addresses these limitations through curated datasets and novel learning strategies. We introduce a new Sentinel-2 (S2) and Sentinel-1 (S1) dataset covering the contiguous United States, featuring pixel-accurate 10 m water masks with emphasis on challenging weather conditions and urban environments that are underrepresented in existing benchmarks. High-quality S2 annotations are manually produced using rigorous geospatial labeling protocols and transferred to SAR imagery through weakly labeled temporally coincident acquisitions. To address SAR-specific artifacts, a shift-invariant loss function is employed to tolerate residual geolocation uncertainty between SAR imagery and optical-derived labels, and a Conditional Variational Autoencoder (CVAE) is trained on multitemporal SAR composites to suppress speckle while preserving flood-relevant spatial structure. Experiments using UNet and UNet++ architectures demonstrate strong multispectral performance (AUPRC up to 0.956) and statistically significant improvements in SAR flood mapping when using shift-invariant loss and CVAE-based despeckling compared to classical filters. These results underscore the importance of dataset fidelity, misalignment-robust training, and demonstrate the viability of generative despeckling for operational flood mapping.

---


### 457. [Informational Frustration in Neural Manifolds: Shannon Bottlenecks and the Limits of Learnability](https://arxiv.org/abs/2606.30512)

**<font color=#1a73e8>作者：</font>** Srinivasa Rao P., Vangmayi P Reddy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Why overparameterised deep networks generalise so remarkably well remains one of the most stubborn open questions in machine learning theory. Classical frameworks like VC dimension and Rademacher complexity predict catastrophic overfitting in modern models, leaving a massive theoretical gap between theory and reality. In this paper, we bridge this divide by introducing a unified framework that links information theory, topology, and statistical mechanics to map the hard limits of deep learning. Central to our approach is the Entropic Learnability Horizon (ELH): a fundamental law stating that a network can only truly learn a target function if the Shannon entropy of the data manifold outpaces the topological entropy of the function's decision boundary, balanced by the von Neumann entropy of the network's weight space. We establish the Shannon-Topological Bottleneck Theorem, proving that when a target boundary's geometric complexity exceeds this informational horizon, the system undergoes a sudden entropic phase transition. It falls into a state of Informational Frustration - a glassy, rigid memorization phase where generalization becomes thermodynamically impossible. Using this lens, we show that the enigmatic phenomenon of "grokking" is actually an Entropic Release, where weights abruptly reorganise to unlock the bottleneck. Finally, we translate this theory into practice with Entropic Gradient Descent (EGD), an optimization algorithm that dynamically manages weight entropy to keep learning on track. Ultimately, this work repositions entropy not just as a tool for tracking uncertainty but as the fundamental physical currency that dictates whether a machine can learn.

---


### 458. [3D Scene-Adaptive Trajectory-Controllable Human Image Animation with Camera Movement](https://arxiv.org/abs/2606.30514)

**<font color=#1a73e8>作者：</font>** Deyin Liu, Jicheng Xu, Lin Yuanbo Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human image animation, which aims to generate a video of a reference subject following a provided action sequence, has received increasing research interest. With the development of diffusion-based/flow-based video foundation models, existing animation works have began to upgrade the guidance information from 2D skeleton/pose to 3D modeling conditions. Despite achieving reasonable results, these approaches face challenges in synthesizing trajectory-controllable human motion within natural scene under changed camera views. In this work, we present a scene-adaptive human image animation framework that controls both human motion and camera trajectories within a reconstructed 3D environment for video generation. To achieve this, we first develop a ground-adaptive 3D motion retargeting approach to enable user-friendly motion trajectory control adapting to the changes of elevations of ground and orientations automatically. Then we design a viewpoint-adaptive latent fusion mechanism to inject point-cloud geometric priors through scene-visibility masking into the generative process, providing precise guidance of viewpoint changes under camera control. Experiments on two standard human image animation benchmark datasets demonstrate remarkable improvements of our method over the state of the arts in related video generation metics. Project page: this https URL

---


### 459. [HASTE: A Framework for Training-Free, Dynamic, and Steerable Compression of Pre-Trained Convolutional Neural Networks](https://arxiv.org/abs/2606.30516)

**<font color=#1a73e8>作者：</font>** Lukas Meiner, Jens Mehnert, Alexandru Paul Condurache  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying large convolutional neural networks (CNNs) on resource-constrained devices is challenging due to their high computational cost. While dynamic execution methods are promising, existing approaches for CNNs typically require specialized training or fine-tuning, limiting their effectiveness when applied to pre-trained models and requiring data access. To address this gap, we propose HASTE (Hashing for Tractable Efficiency), a plug-and-play convolution module that enables training-free, dynamic compression of large pre-trained CNNs. At inference time, HASTE uses locality-sensitive hashing to identify and merge redundant channels of latent feature maps on a patch-wise basis. This process simultaneously compresses the depth of both input features and their corresponding filters, resulting in computationally cheaper convolutions. We conduct extensive experiments on CIFAR-10 and ImageNet across a range of architectures, demonstrating a 46.2% FLOPs reduction in a ResNet34 on CIFAR-10 with only a 1.25% drop in accuracy, without any retraining. We support our claims by comprehensive ablation studies to validate our core design choices, an analysis of the method's properties and limitations, and a discussion that connects our channel merging scheme to the conceptually related task of token merging in Vision Transformers. Our results demonstrate that HASTE provides an effective solution for steerable compression of pre-trained CNNs at runtime, opening new possibilities for the deployment of efficient deep learning methods.

---


### 460. [ITSPACE: Monotone Gaussian Optimal Transport Updates](https://arxiv.org/abs/2606.30523)

**<font color=#1a73e8>作者：</font>** Woojoo Na, Jennifer Dy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Covariance matrices serve as compact descriptors of feature distributions in many machine-learning pipelines, including domain adaptation and Gaussian embeddings. Under a centered Gaussian approximation, the unregularized Wasserstein-2 optimal-transport (OT) discrepancy admits a closed form on covariances given by the Bures-Wasserstein (BW) objective on the symmetric positive definite (SPD) cone. We propose ITSPACE (Iterative Transport for Stable Proximal Alignment of Covariance Embeddings), a proximal majorization-minimization method that directly optimizes this exact BW objective through closed-form updates in a square-root factorization. In exact arithmetic, each iteration satisfies a sufficient-decrease inequality for the BW objective; under inexact polar computations, we provide an explicit certificate-gap bound controlling deviations from exact descent. The resulting iterations preserve PSD structure by construction and naturally support rank-restricted factors, making ITSPACE well-suited as a lightweight inner-loop primitive in settings where adaptation must be performed from unlabeled target batches under strict step and compute budgets. Across real-world covariance-alignment benchmarks, ITSPACE reaches low-BW-gap solutions substantially faster than BW-gradient descent, methods based on other covariance geometries, and entropically regularized sample-OT baselines.

---


### 461. [Entity Binding Failures in Tool-Augmented Agents](https://arxiv.org/abs/2606.30531)

**<font color=#1a73e8>作者：</font>** Rahul Suresh Babu, Shashank Indukuri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented language-model agents are often evaluated by whether they select the correct tool, produce valid API arguments, and complete the requested task. However, an agent may choose the right tool and still act on the wrong external entity. For example, a request to "email Alex about the launch" may lead the agent to contact the wrong Alex, attach the wrong launch document, reply in the wrong thread, or update the wrong customer account. We call these errors entity binding failures. This paper studies entity binding failures as a distinct reliability and safety problem in tool-augmented agents. We formalize the separation between tool correctness and entity correctness, introduce a taxonomy of wrong-entity failures in enterprise workflows, and evaluate entity-aware execution mechanisms including entity-resolution preconditions, confidence-gated binding, clarification under ambiguity, and provenance tracking. In a controlled diagnostic evaluation across 60 tasks, five model backends, and six tool-use methods, all methods achieved 0.0 percent wrong-tool error, yet action-oriented baselines still produced wrong-entity actions in 24.0-26.0 percent of runs. Entity-aware methods eliminated wrong-entity actions and risk-weighted wrong-entity exposure in this setting, but reduced direct task completion by deferring under ambiguity. These findings show that safe tool use requires not only selecting the correct tool, but also reliably binding natural-language references to the correct real-world entity before action.

---


### 462. [Orca: The World is in Your Mind](https://arxiv.org/abs/2606.30534)

**<font color=#1a73e8>作者：</font>** Yihao Wang, Yuheng Ji, Mingyu Cao 等 57 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Orca, an initial instantiation of a general world foundation model. Orca learns a unified world latent space from multimodal world signals and exposes it through multimodal readout interfaces. Rather than optimizing isolated next-token, next-frame, or next-action prediction, we are centered on Next-State-Prediction modeling, offering a unified state-transition modeling route toward understanding, predicting, and acting upon the world. Orca learns through two complementary paradigms: unconscious learning captures dense natural state transitions from continuous videos, and conscious learning models sparse meaningful state transitions by language-described events and VQA supervision. For pre-training, we construct a large-scale world-learning inventory data, including 125K hours of video data and 160M event annotations. After pre-training, Orca learns a unified world latent space. To examine whether the learned latent supports downstream, we evaluate it by three representative downstream readouts: text generation, image prediction, and embodied action generation. Orca's backbone is frozen, and only the lightweight modality-specific decoders are trainable. Experiments show the scalability of the proposed paradigm and verify that stronger world latent enables stronger downstream readouts. Orca outperforms similar-sized specialized baselines. These results show that Orca, as a general world foundation model, presents a promising approach to understanding, predicting, and acting upon the world. Finally, we discuss the current limitations, aiming to provide useful insights and inspiration for the community.

---


### 463. [A Lightweight Post-Quantum Authentication Framework for 5G Base Station Bootstrapping](https://arxiv.org/abs/2606.30542)

**<font color=#1a73e8>作者：</font>** Saleh Darzi, Mirza Masfiqur Rahman, Imtiaz Karim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The absence of authenticated bootstrapping between User Equipments (UEs) and Base Stations (BSs) in 5G leaves System Information Block (SIB) broadcasts unprotected, enabling fake BS attacks, man-in-the-middle interception, and spoofed emergency alerts. Prior efforts such as Public Key Infrastructure (PKI)-based certificate chains, token-based schemes, and identity-based signatures either impose overhead exceeding 5G's strict packet-size constraints or lack post-quantum (PQ) security. Direct NIST-PQC integration is infeasible: ML-DSA requires 34 fragmented SIB1 packets and up to 5,282,ms end-to-end delay, and FN-DSA still requires 13 fragments and up to 1,920,ms. We propose $\emulsion$, a symmetric chained publicly verifiable authentication framework for 5G/6G BS broadcast authentication. EMULSION is the first framework to exploit native 5G architectural features: fixed SIB transmission windows, millisecond-level time synchronization, and eSIM/USIM credential management to achieve genuine PQ security at symmetric-key efficiency. It uses a TESLA-style HMAC chain anchored by a compact PQ signature (MAYO) applied once per epoch, fitting authentication within a single packet with no fragmentation and eliminating certificate transmission entirely. Unlike all prior schemes, EMULSION protects the full SIB family (SIB1-SIB21). Evaluated on a real over-the-air 5G testbed, EMULSION achieves 33x lower end-to-end delay and 31x less communication overhead than ML-DSA, and 12x lower delay and 5.4x less overhead than FN-DSA. We formally prove the security of EMULSION and open-source its implementation for public testing and adaptation.

---


### 464. [TRACE: Temporal Relationship-Aware Conversational Entrainment Detection in Dyadic Speech](https://arxiv.org/abs/2606.30543)

**<font color=#1a73e8>作者：</font>** Sathvik Manikantan Napa Ugandhar, Hao Zhang, Alison Gunzler 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the proliferation of speech AI agents, understanding emotional entrainment in conversational interaction has become increasingly important. Emotional entrainment is shaped by social relationships and conversational context, influencing affective coordination over time. We introduce DyadEE, a dataset for emotional entrainment detection in dyadic speech interactions, containing both emotionally entrained conversations and synthetic interactions where entrainment is disrupted through partner swapping and emotion resynthesis. We further propose TRACE, a window-level framework that models dyadic interaction as ordered sequences of acoustic embeddings derived from emotion fine-tuned Whisper representations, treating each sample as an interaction trace rather than pooled utterances. Experimental results on DyadEE show that incorporating conversational context and relationship information improves emotional entrainment detection, with TRACE achieving the best accuracy of 97.01%.

---


### 465. [Latent Actions from Factorized Transition Effects under Agent Ambiguity](https://arxiv.org/abs/2606.30544)

**<font color=#1a73e8>作者：</font>** Heejeong Nam, Chandradithya S Jonnalagadda, Harshit Aggarwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent Action Models (LAMs) learn action-like proxies from observation transitions. However, in multi-object or distractor-rich scenes, these visual effects mix agent motion with distractors, camera dynamics, and background changes, making the underlying action source ambiguous without supervision. Structuring this mixture as reusable transition effects provides an intermediate representation from which action-like latents can be more robustly formed. We introduce Observed Transition Factorization (OTF), which decomposes each transition into a sparse set of observed transition primitives. Using these primitives as the transition interface, we propose OTF-LAM, which abstracts motion primitives into action-like latents within the standard inverse-forward dynamics framework, and OTF-LAM-Dino, a decoder-free variant that predicts future states in a frozen DINOv2 representation space. Empirically, OTF primitives transfer zeroshot across controlled carrier and morphology shifts, showing reusability. Furthermore, downstream policy learning results match or outperform baselines under complex transition ambiguity.

---


### 466. [StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors](https://arxiv.org/abs/2606.30545)

**<font color=#1a73e8>作者：</font>** Wenhao Yuan, Yiyuan Ge, Deli Cai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has achieved remarkable success in real-time novel view synthesis, yet it suffers from severe overfitting under sparse-view settings due to insufficient geometric constraints. While recent methods introduce monocular depth priors to mitigate this, they inherently struggle with scale ambiguity and cross-view inconsistency, leading to defective geometry. In this paper, we propose StereoGS, a novel sparse-view 3DGS framework that integrates stereo priors to establish reliable binocular consistency. Unlike scale-agnostic monocular constraints, StereoGS introduces a Stereo Depth Regularization by constructing virtual stereo pairs during optimization and leveraging a foundation stereo model to enforce absolute scale and binocular-consistent structures. To further suppress overfitting and eliminate redundant primitives, we design a Gradient-Aware Opacity Decay strategy that dynamically penalizes Gaussians based on their relative opacity gradient magnitudes. Combined with a Consistency-Aware Dense Initialization using zero-shot multi-view depth estimation, StereoGS effectively anchors primitives to accurate scene surfaces. Extensive experiments on LLFF, DTU, Mip-NeRF360, and Blender datasets demonstrate that StereoGS achieves state-of-the-art performance in sparse-view settings without incurring any additional inference overhead. Project Page: this https URL

---


### 467. [MAS-Lab: A Specification-Driven Validation Framework for Reliable Multi-Agent Systems](https://arxiv.org/abs/2606.30546)

**<font color=#1a73e8>作者：</font>** Jordan Augé, Giovanna Carofiglio, Giulio Grassi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The rapid emergence of LLM-based agentic frameworks has significantly reduced the cost of assembling multi-agent systems (MAS), enabling fast prototyping and exploration of agentic behaviors. However, systems built with current tooling remain ill-suited for reliable, evolvable, and production-grade deployment. In practice, MAS are often developed in an ad-hoc and imperative manner, with agent logic, orchestration, observability, and control tightly interwoven, little to no explicit system-level validation, and development workflows optimized for demonstrations rather than long-lived, governed operation. As a result, behavior observed during experimentation rarely constitutes reliable evidence of behavior in production.
In this paper, we introduce MAS-Lab, a specification-driven framework for principled development and experimental validation of multi-agent systems properties. MAS-Lab is designed to transform MAS from collections of scripts into engineered distributed systems by separating semantic intent from operational concerns, making behavior and control explicit, supporting reproducible experimentation, and preserving continuity across lifecycle stages. MAS-Lab consists of three layers: a declarative, framework-agnostic agentic specification layer (Spec); a stateful MAS Operating System that provides execution and control primitives plugged-in by design (MAS-OS); and a set of lab overlays with integrated observability and evaluation tools (Labs). Together, these components enable intent-based validation, principled system evolution, and a seamless transition to production-grade MAS.

---


### 468. [To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks](https://arxiv.org/abs/2606.30549)

**<font color=#1a73e8>作者：</font>** Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI code completion tools, such as Github Copilot, provide students with code suggestions to help them write programs. However, recent qualitative studies suggest that students fail to critically evaluate these suggestions. We present Clover, a code completion tool that logs students' interactions with code suggestions and additionally offers attention checks to probe reflective engagement during programming tasks. We also develop a taxonomy of behavioral interaction metrics for AI-assisted programming, informed by literature. We analyzed relationships between interaction patterns, engagement with attention checks, and task performance. We observed that higher rates of tab accept were associated with lower attention check performance, while increased dwell time was associated with higher attention check performance. We conclude by discussing how programming process data and attention checks might support reflective engagement in AI-assisted programming.

---


### 469. [Linguistic Firewall: Geometry as Defense in Multi-Agent Systems Routing](https://arxiv.org/abs/2606.30555)

**<font color=#1a73e8>作者：</font>** Dvir Alsheich, Adar Peleg, Ben Hagag 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid integration of Large Language Models (LLMs) has driven the evolution of Multi-Agent Systems (MAS), where specialized agents collaborate to execute complex workflows. Effective orchestration in these environments requires robust routing mechanisms to efficiently allocate tasks to the most suitable agent. However, existing routers fundamentally rely on unverified proxies, ranging from textual self-descriptions to static surrogate representations, to gauge an agent's competence. This reliance on non-empirical data creates a critical gap between an agent's projected profile and its actual operational capabilities, introducing severe security vulnerabilities. Malicious agents can easily misrepresent their proficiencies or harbor covert backdoors that evade both standard external analysis and static representation-learning techniques. In this work, we introduce ANTAP (Automatic Non-Textual Agent Picker), an evaluation-driven routing architecture that discards indirect proxies in favor of active capability testing. By dynamically querying agents to ascertain their true competencies empirically, ANTAP distills performance into fixed behavioral operators within a shared semantic space. At inference time, routing is performed via a purely non-textual algebraic projection, establishing a "linguistic firewall" that renders metadata-based attacks inexpressible. In our experiments, ANTAP achieves near-zero ASR against description-based injection attacks, compared to 67.3\% and above for the description-based router baseline. Against adaptive embedding attacks, ANTAP achieves substantially lower ASR than the embedding-based baseline, with a 20\% reduction, while remaining resilient to description manipulation by design.

---


### 470. [EcoVideo: Entropy-Orchestrated Video Generation Paradigm in Cloud-Edge Dynamics](https://arxiv.org/abs/2606.30557)

**<font color=#1a73e8>作者：</font>** Jiayu Chen, Hengyi Zhang, Maoliang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> DiT video generation is latency-intensive due to iterative full-frame denoising, while prior cloud-edge methods largely rely on static inter-step decoupling and cannot leverage inter-frame similarity or adapt to system dynamics. We propose EcoVideo, an entropy-orchestrated framework for dynamic inter-frame decoupling: early-stage self-attention entropy provides a training-free estimate of frame-wise information density for frame selection; a cloud large model denoises sparse high-entropy keyframes; and an edge lightweight model reconstructs the remaining frames via motion-aware interpolation with refinement for temporal stability. EcoVideo further adapts the keyframe budget and edge refinement depth to real-time bandwidth and compute availability, optimizing end-to-end latency under constraints. Experiments on representative DiT video generators show improved quality--efficiency trade-offs and up to 2.9x end-to-end speedup in low-bandwidth, compute-limited edge settings. Code is available at this https URL.

---


### 471. [Convergence of Continual Learning in Homogeneous Deep Networks](https://arxiv.org/abs/2606.30559)

**<font color=#1a73e8>作者：</font>** Matan Schliserman, Gon Buzaglo, Itay Evron 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We characterize weakly regularized continual classification in homogeneous models as sequential projections onto task margin sets. This result generalizes prior analyses restricted to either stationary (single-task) deep models or continual linear models. We show that global convergence generally fails, even for simple models linear in data but nonlinear in parameters. Nevertheless, by leveraging results from nonconvex projection theory, we identify regularity properties of homogeneous deep networks that guarantee local linear convergence under random and cyclic task sequences. Finally, we extend our analysis to continual regression, unifying the framework for homogeneous models.

---


### 472. [The Human Creativity Benchmark](https://arxiv.org/abs/2606.30561)

**<font color=#1a73e8>作者：</font>** Aspen Hopkins, Allison Nulty, Alexandria Minetti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern AI evaluation frameworks treat evaluator disagreement as noise to be resolved. In creative domains, professional disagreement reflects genuine differences in taste, not measurement error. We argue that evaluating creative AI requires preserving two distinct signals: convergence, where professionals align around shared best practices, and divergence, where individual taste legitimately varies. We present the Human Creativity Benchmark (HCB), a benchmark that operationalizes this separation by collecting pairwise preferences, scalar ratings on prompt adherence, usability, and visual appeal, and qualitative rationale from domain professionals. Across 15,000 professional judgments spanning five creative domains and three workflow phases (ideation, mockup, refinement), we find that convergence concentrates on verifiable dimensions like technical correctness and visual hierarchy, while divergence concentrates on taste-driven dimensions like aesthetic direction and conceptual risk. No model excels uniformly across all phases. Collapsing these signals into a single quality metric discards the most actionable information: where models must be correct versus where they should remain steerable.

---


### 473. [Morphing into Hybrid Attention Models](https://arxiv.org/abs/2606.30562)

**<font color=#1a73e8>作者：</font>** Disen Lan, Jianbin Zheng, Yuxi Ren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hybrid attention models improve long-context efficiency by retaining only a subset of full-attention layers and replacing the remaining layers with linear attention. However, the effectiveness of Transformer-to-hybrid conversion critically depends on which layers preserve full attention. Existing hybrid layer selection methods typically rely on heuristic strategies such as fixed placement patterns or layerwise scoring, implicitly treating layer importance as isolated and overlooking the interdependent layer effect under a global hybrid configuration. In this work, we formulate hybrid layer selection as a budget-constrained subset optimization problem. We further propose FlashMorph (Fast LAyer Selection for Hybrid MORPHing), an effective, efficient and scalable layer selection method for Transformer-to-hybrid conversion. FlashMorph first constructs a morphable model by equipping each full-attention layer with a converted linear-attention branch. It then freezes all model weights and jointly optimizes layerwise gates on synthetic long-context retrieval data, with a linearization regularization that encourages the model to rely on linear attention for efficiency. The learned gates are discretized under a preset full-attention budget to instantiate the hybrid architecture, followed by standard logits distillation and long-context finetuning. Extensive experiments show that FlashMorph discovers more effective hybrid configurations, preserves strong long-context recall and general benchmark performance while substantially reducing layer selection cost compared with existing layer selection methods, demonstrating its effectiveness, efficiency, and scalability.

---


### 474. [The Role of Vehicles in Digital Forensic Investigations: A Structured Synthesis of Digital Vehicle Forensic Characteristics](https://arxiv.org/abs/2606.30564)

**<font color=#1a73e8>作者：</font>** Kevin Mayer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern vehicles are cyber-physical, networked systems that may contain valuable digital traces for accident reconstruction, crime investigation, warranty analysis, and cybersecurity incident response. However, digital vehicle forensics (DVF) remains less mature than computer, mobile, and cloud forensics because relevant data is distributed across in-vehicle components, mobile devices, manufacturer back ends, third-party services, and physical evidence. This article addresses this gap through a structured synthesis of academic literature, standards, and practitioner-oriented sources. First, we define DVF as the identification, preservation, acquisition, verification, interpretation, and reporting of vehicle-related digital evidence under safety, legal, privacy, and forensic-soundness constraints. Second, we formalize the DVF triage problem as the selection and correlation of evidence sources subject to volatility, accessibility, safety, integrity, and authorization constraints. Third, we explain how eight characteristics were derived from the literature and case material: multiple users, massively networked, cyber-physical system, dependencies between components, functional data, safety implications, accessibility, and limited abstraction. Finally, we add an adversarial perspective and a characteristic-driven triage procedure that helps investigators prioritize evidence sources while documenting assumptions, limitations, and failure cases. The resulting contribution is not an algorithmic performance claim; it is a reproducible conceptual framework for understanding, planning, and communicating DVF investigations.

---


### 475. [Forensic Trajectory Signatures for Agent Memory Poisoning Detection](https://arxiv.org/abs/2606.30566)

**<font color=#1a73e8>作者：</font>** Jun Wen Leong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We discover a behavioral invariant in LLM agents under persistent memory poisoning: in architectures where routing information is retrieved through observable memory-tool invocations, successful attacks require calling memory_recall_fact before email_send_email, a transition that non-exfiltrating sessions rarely exhibit. Under the evaluated architecture, this invariant follows from the attack's information-retrieval dependency rather than being merely an empirical correlation, and suppressing it breaks the attack. A simple rule exploiting this invariant alone achieves AUC = 0.9563. A Random Forest classifier over 19 trajectory features refines it to AUC = 0.9904 (BCa 95% CI [0.987, 0.993], N=10,000 resamples), demonstrating that the attack imprints on multiple independent behavioral channels. The signature is overdetermined: removing all recall-related features (half the feature set) leaves AUC unchanged at 0.990, confirming that memory poisoning induces a distributed trajectory signature rather than a single observable anomaly. Cross-model hold-out on 9 models (7B-120B parameters) confirms AUC = 1.000 on 6/9 hold-out splits, with all three exceptions mechanistically explained. The invariant generalizes to frontier models (GPT-4.1, GPT-4o) without retraining. A strictly prefix-only variant achieves AUC = 0.934, suggesting that real-time blocking is feasible with moderate degradation. The boundary is forensically useful: prompt-injection attacks that bypass memory produce a distinct trajectory (score = 0.541), enabling incident responders to distinguish memory-channel attacks from prompt-injection attacks using tool-call logs alone.

---


### 476. [SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions](https://arxiv.org/abs/2606.30573)

**<font color=#1a73e8>作者：</font>** Mohit Raghavendra, Anisha Gunjal, Aakash Sabharwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce SWE-Interact, a new testbed for evaluating coding agents on multi-turn, interactive, user-driven software engineering tasks. Existing frontier SWE benchmarks typically provide complete requirements upfront and evaluate agents on autonomous implementation. In contrast, SWE-Interact places agents in a realistic developer workflow: a carefully designed user simulator starts with vague or incomplete instructions, progressively reveals requirements, inspects the agent's workspace, and provides targeted feedback, revisions, and new constraints until the full task goal has been handed off. Grounded in large-scale studies of real coding-agent interactions, this setup tests whether agents can discover user intent, adapt to evolving requirements, and build on their own prior work. Across a suite of frontier and open-weight models, we find that strong performance on single-turn SWE tasks does not reliably transfer to multi-turn, user-driven workflows: the best-performing models solve roughly 50% of single-turn baseline tasks but only 25% of the corresponding SWE-Interact tasks. The strongest models in our evaluation, including Opus 4.8 and GPT 5.5, start strong even in the face of vague initial instructions, persevere until all the requirements are surfaced by the user, integrate them better and write clean code. However, they still suffer from over-agentic coding, forgetting requirements and technical mistakes. Weaker models start poorly under ambiguity, give up early, forget or ignore instructions and rework their code more. Overall, SWE-Interact measures an orthogonal, real-world capability axis for frontier model development: interactive goal discovery and iterative refinement with a user in the loop.

---


### 477. [The Fundamental Limits of Valid Transport Map Estimation](https://arxiv.org/abs/2606.30574)

**<font color=#1a73e8>作者：</font>** Sivaraman Balakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many modern generative modeling methods, including diffusion models, normalizing flows, and flow matching, estimate transport maps or plans between distributions without explicitly targeting an optimal transport (OT) map. In applications like generative modeling, the transport cost itself is irrelevant, and this makes it natural to target maps which are more tractable from either a statistical or computational standpoint. In this short note, we formalize the task of estimating any valid transport map in a rigorous minimax framework. One consequence of this framing is that it yields sample complexity lower bounds for any method whose learned object is evaluated as a transport map or plan, including flow matching and diffusion-based generative models, in settings where direct analysis would be challenging due to the analytic complexity of the methods and their target maps. We observe that, under standard, though strong, stability assumptions from the OT literature, estimating any valid transport map is statistically as hard as estimating the OT map. We complement these results with some examples showing that when these stability assumptions fail, alternative transport maps can be learned substantially more accurately than the OT map. Our minimax framing provides a rigorous foundation for understanding the statistical limits of modern transport-based generative methods and clarifies when targeting sub-optimal maps can provide real statistical advantages.

---


### 478. [Beyond 2D Matching: A Unified Single-Stage Framework for Geometry-Aware Cross-View Object Geo-Localization](https://arxiv.org/abs/2606.30576)

**<font color=#1a73e8>作者：</font>** Liyao Wang, Ruipu Wu, Haojun Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view object geo-localization (CVOGL) aims to locate a target object from a query view (e.g., ground or drone) within a geo-tagged reference image (e.g., satellite). Existing approaches heavily rely on 2D appearance matching and are constrained by limited datasets lacking geometric metadata, diverse prompts, and standard field-of-view imagery. To address these intertwined challenges, we first introduce \dataset, a large-scale, high-fidelity building dataset comprising over 220,000 ground-satellite and drone-satellite pairs. It provides multi-modal prompts (points, boxes, masks) and camera poses to enable flexible target referring and explicit spatial modeling. Furthermore, we propose a novel single-stage Geometry-Aware Geo-localization framework (GAGeo), built upon the permutation-equivariant 3D foundation model $\pi^3$. By seamlessly integrating visual features, referring prompts, and learnable task tokens, our model adapts the inherited 3D prior to jointly predict bounding boxes, segmentation masks, and camera poses in a single forward pass. Additionally, we introduce a contrastive loss that utilizes the satellite view as a universal anchor, implicitly aligning ground and drone representations to enable zero-shot ground-to-drone localization without requiring triplet training data. Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art methods, exhibiting exceptional generalization ability in unseen scenes and novel cross-view setups.

---


### 479. [APRIL-MedSeg: A Modular Medical Image Segmentation Toolbox Embracing Modern Paradigms](https://arxiv.org/abs/2606.30577)

**<font color=#1a73e8>作者：</font>** Juntao Jiang, Jinsheng Bai, Linxuan Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present APRIL-MedSeg, a YAML-driven modular framework for 2D medical image segmentation. It provides a unified and extensible ecosystem that decomposes segmentation networks into reusable components. Also, the framework integrates a broad spectrum of advanced paradigms, including semi-supervised learning, domain adaptation, knowledge distillation, weakly supervised learning, and text-guided segmentation as well as foundation model support. A registry-based configuration system with inheritance enables flexible and reproducible experiment management, supporting seamless switching across models, datasets, and training strategies. In addition, the framework provides a unified interface for medical datasets, augmentation pipelines, deployment utilities and model ensembling. Overall, APRIL-MedSeg is designed as a general-purpose research and development platform that bridges algorithmic innovation and practical deployment, while also serving as a structured ecosystem for systematically organizing and reproducing advances in medical image segmentation. The code is available at this https URL under an Apache 2.0 license.

---


### 480. [Uncertainty-Aware Generation and Decision-Making Under Ambiguity](https://arxiv.org/abs/2606.30578)

**<font color=#1a73e8>作者：</font>** Nico Daheim, Iryna Gurevych  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With rapidly improving capabilities, Large Language Models (LLMs) are increasingly used in many complex real-world tasks. Beyond requiring in-depth knowledge and reasoning skills, many of these tasks exhibit a high degree of subjectivity and require that the outputs of the model can be trusted. While a lot of progress has been made to train better models, decision-making algorithms have received less attention. In this work, we present and evaluate various uncertainty-aware decision-making algorithms based on Bayesian decision theory and risk-averse decision making on the tasks of tutoring and automatic peer reviewing. Concretely, we take uncertainty over tutoring strategies and review scores into account when generating a tutor response or review and use conformal prediction to provide guarantees over strategy and score. We find empirically that these algorithms can improve the utility of the generations but need to be carefully implemented when ambiguity is high. For example, risk-averse rules can degrade performance by optimizing for generic outputs, while Bayesian methods tend to perform better. Our work uses techniques from decision theory to improve LLM-based decision-making and outlines open challenges for the community.

---


### 481. [Concept Catalyst: Exploring Scrutable Interfaces to Structure K-12 Teacher Interactions with Generative AI](https://arxiv.org/abs/2606.30590)

**<font color=#1a73e8>作者：</font>** Gennie Mansi, Sunni Newton, Roxanne Moore 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Purpose: This paper explores how to align AI-based tools with teachers' classroom needs by using scrutable interfaces -- interfaces that link an easily manipulable knowledge representation to an underlying AI model, so users can change the system's outputs without understanding its details. It provides an in-depth discussion and example of a scrutable interface that structures teachers' interactions with generative AI. This study aims to expand how and where scrutable interfaces are used in AI-based tools to support teachers, who have not been historically targeted in the design of scrutable systems.
Design/Methodology/Approach: This paper presents the design and evaluation of Concept Catalyst, an AI-based tool with a scrutable interface, created to support teachers' reflection while using generative AI for curriculum development. It presents the findings from an exploratory study using Wizard-of-Oz testing with middle and high school engineering teachers, resulting in 10 depth interviews lasting 55 minutes on average. Screen/audio recordings and the classroom content teachers produced during the session were also collected.
Findings: The paper provides empirical insights about how scrutable interfaces can positively structure teachers' interactions with generative AI models when creating classroom content. Findings suggest that scrutable interfaces can help teachers reflect on their teaching practices while improving efficacy, efficiency, and motivation when using AI.
What is original/value of the paper: This paper explores an identified need to support teachers' classroom practices and needs when using generative AI. It extends the consideration of scrutable interfaces in two ways: to support teachers as users (not just students) and to structure interactions with generative AI models.

---


### 482. [Learning from Reliable Latent Prompts for Visual Recognition with Missing Modalities](https://arxiv.org/abs/2606.30597)

**<font color=#1a73e8>作者：</font>** Taixi Chen, Nancy Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale multimodal models (LMMs) have achieved superior performance in visual recognition by synergizing information across diverse, massive-scale paired modalities. In real-world scenarios, however, missing-modality inputs are ubiquitous, causing models optimized for modality-complete data to exhibit precipitous performance degradation. Existing research has introduced prompt learning to mitigate this issue, typically by generating dynamic prompts from instance-level features, regardless of whether the input modalities are complete or partially absent. However, such input-conditioned strategies are hindered by the escalating unreliability of instance-level features; as higher missing rates increase the proportion of incomplete modalities, the resulting instability in prompt learning limits the model's performance. To address this limitation, we hypothesize that learnable latent prompts themselves encapsulate stable, modality-intrinsic priors that are decoupled from corrupted inputs. Consequently, we propose a novel paradigm: Learning from Reliable Latent Prompts. Unlike prior methods, we model input-agnostic learnable prompts as stable latent anchors that enable robust guidance and effective cross-modal knowledge compensation, even under extreme missing rates (e.g., 90%). Empirical results across three benchmark datasets demonstrate that our "learn-from-latent-prompts" approach achieves state-of-the-art performance across a wide range of missing-modality scenarios. Extensive experiments further confirm the effectiveness of this paradigm in providing a robust solution to the missing-modality problem.

---


### 483. [Towards in-the-wild Egocentric 3D Hand-Object Pose Estimation](https://arxiv.org/abs/2606.30598)

**<font color=#1a73e8>作者：</font>** Siddhant Bansal, Zhifan Zhu, Shashank Tripathi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating accurate 3D hand-object pose from in-the-wild egocentric RGB remains challenging due to severe occlusions and ambiguous contact. Existing learning-based methods often struggle to generalise to in-the-wild scenes and are limited by the scarcity of supervision. We address these issues with two contributions. First, we introduce EPIC-Contact, an in-the-wild egocentric dataset of 2.3K clips (62.3K frames) with dense, bijective 3D hand-object contact correspondences and posed meshes. Second, we propose HOPformer, an end-to-end transformer that jointly predicts bi-manual hand and object pose in a single forward pass. A cross-attention decoder conditions object features on hand priors, producing robust pose estimation. We test HOPformer on the in-lab 3D dataset, ARCTIC, as well as our newly introduced EPIC-Contact dataset. HOPformer reaches 82.4% success rate on ARCTIC (+6.2 pts over current SOTA). On EPIC-Contact, it nearly doubles the success rate while reducing contact deviation by 75%. EPIC-Contact, HOPformer code and checkpoints are released: this https URL.

---


### 484. [Goku: A Million-Scale Universal Dataset and Benchmark for Instruction-Based Video Editing](https://arxiv.org/abs/2606.30599)

**<font color=#1a73e8>作者：</font>** Sen Liang, Cong Wang, Zhentao Yu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing instruction-based video editing datasets commonly focus on single-task appearance editing, failing to meet the complex creative demands of real-world scenarios. To bridge this gap, we present Goku, a large-scale dataset featuring 2 million high-quality, instruction-aligned video editing pairs, which is the first to extend task boundaries from basic appearance editing to multi-task and structural manipulations(e.g., precise control of subject movement). To tackle the data synthesis challenges inherent in these complex tasks, we design an efficient data synthesis pipeline that decomposes complex edits into controllable sub-problems and introduce a progressive filtering system for data reliability throughout the whole process. Furthermore, we explore the optimal network structures on Goku, and propose Goku-Edit. To deeply comprehend complex editing instructions, Goku-Edit leverages an MLLM as its text encoder and adopts a decoupled dual-branch design: a dedicated mask branch handles structural control, freeing the main branch for appearance rendering. A comprehensive video editing benchmark, Goku-Bench, is also proposed with 1,000 human-verified test cases and 7 novel editing-specific metrics. Evaluated on Goku-Bench, Goku-Edit obtains up to +8% improvement on other open-source models in terms of instruction following.

---


### 485. [MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems](https://arxiv.org/abs/2606.30602)

**<font color=#1a73e8>作者：</font>** Kunyang Li, Kyle Domico, Jonathan Gregory 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) are increasingly used to automate complex, distributed workflows. However, their inter-agent communication channels introduce new attack surfaces that remain poorly understood and are difficult to defend against. In this paper, we address how defenders should prioritize limited security effort to protect vulnerable communication channels before attacks are observed. This is motivated by our observation that the channel-level attack impact is highly non-uniform: a single compromised edge can account for up to 75% of total attack success. We introduce Mesa, a label-free framework for proactively ranking which MAS edges are most security-critical -- that is, most likely to affect the system's decision if compromised. Mesa combines six graph-theoretic metrics and two dynamic probes (ablation and masking) without requiring attack traces. We evaluate Mesa against a dynamic misinformation attack pipeline across three diverse MAS scenarios, eight network topologies, and five open-source LLMs from Qwen, Llama, and Gemma families. Mesa rankings correlate strongly with empirical per-edge attack success rate, achieving mean Spearman $\rho=+0.60$ (peaking at $+0.73$). In resource-constrained defense deployment, monitoring the top 10% of Mesa-ranked edges intercepts about 3x the successful attacks as random allocation. We further test Mesa under varying attacker and defender models and LangGraph workflows and characterize its limits under adaptive attacks and high-redundancy graphs. Overall, our results show that edge-level risk in MAS is often concentrated and predictable, allowing proactive hardening of multi-agent infrastructures.

---


### 486. [UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image](https://arxiv.org/abs/2606.30608)

**<font color=#1a73e8>作者：</font>** Mohamed el amine boudjoghra, Ivan Laptev, Angela Dai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challenging. Existing approaches remain largely constrained by lack of supervised data or lack the priors needed to reliably recover articulation, hidden geometry, and internal object structure. We present the first debate-driven agentic approach to articulated 3D object reconstruction from text or image inputs that both grounds articulation reasoning in concrete motion and exposes the occluded geometry revealed under articulation. High-level agents reason about object semantics and motion using knowledge from vision-language and video models, while low-level agents estimate articulation parameters and interaction points; together, they engage in a two-round structured debate that first exploits global--local disagreement and then grounds the agents in freely generated video. The same video prior, conditioned on the agreed articulation, then drives each part through its motion to expose occluded interiors and geometry that cannot be inferred from a single static view. By combining agentic reasoning with a video generative prior, our approach jointly infers articulation and reconstructs complete 3D articulated objects, producing high-fidelity geometry, internal structure, and motion-consistent states beyond directly observed surfaces.

---


### 487. [C$^{2}$R: Cross-sample Consistency Regularization Mitigates Feature Splitting and Absorption in Sparse Autoencoders](https://arxiv.org/abs/2606.30609)

**<font color=#1a73e8>作者：</font>** Haoran Jin, Xiting Wang, Shijie Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Autoencoders (SAEs) are widely used to interpret large language models by decomposing activations into sparse, human-understandable features, but scaling to large dictionaries exposes fundamental challenges. Systematic studies reveal pervasive feature splitting that fragments coherent concepts into non-atomic latents and widespread feature absorption that creates arbitrary exceptions in general features, severely compromising latent reliability. These issues stem from inconsistent latent assignment across samples: without cross-sample constraints, per-sample optimization often allows a single underlying concept to be inconsistently distributed across multiple redundant or interfering latents. To address this, we introduce C$^2$R (\underline{\textbf{C}}ross-sample \underline{\textbf{C}}onsistency \underline{\textbf{R}}egularization). C$^2$R explicitly encourages that each semantic feature is consistently represented by a unified latent across the batch by penalizing the co-activation of directionally similar latents. Comprehensive evaluation demonstrates that C$^2$R effectively mitigates both splitting and absorption while, crucially, preserving reconstruction fidelity, providing a principled solution that enhances latent interpretability without degrading model performance. Source code is available at this https URL.

---


### 488. [Reweighting Framewise Attention in Video Transformers for Facial Expression Understanding](https://arxiv.org/abs/2606.30611)

**<font color=#1a73e8>作者：</font>** Seongro Yoon, Donghyeon Cho, Jinsun Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding facial expressions in videos requires modeling subtle and localized facial dynamics under unconstrained conditions. Although recent Vision Transformer~(ViT)-based video models have shown strong performance through large-scale self-supervised pretraining, their attention mechanisms often emphasize dominant global motions and coarse temporal dynamics, limiting sensitivity to fine-grained facial variations. To address this limitation, we propose MiRA (Marginal-induced Attention Redistribution), a plug-in frame-marginal attention redistribution framework for ViT backbones that enhances spatio-temporal selectivity toward subtle facial dynamics without introducing additional trainable parameters. MiRA derives frame-level confidence and intra-frame concentration statistics from self-attention maps to estimate frame-wise marginal importance and redistribute attention toward spatiotemporally localized facial cues. We first introduce a principled \textit{exact mode} based on post-softmax attention redistribution. To further improve efficiency, we propose \textit{flashLite mode}, a lightweight pre-softmax approximation that integrates frame-marginal redistribution into FlashAttention kernels while preserving the effectiveness of the exact formulation. Experimental results on challenging Facial Expression Recognition~(FER) benchmarks demonstrate consistent improvements over strong ViT baselines.

---


### 489. [Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors](https://arxiv.org/abs/2606.30638)

**<font color=#1a73e8>作者：</font>** Jameel Hassan, Yasiru Ranasinghe, Vishal Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Extending 3DGS with language-driven, open-vocabulary understanding has gained significant attention for real-world applications such as embodied AI. Recent methods achieve this by learning an instance feature attribute and assigning semantics by distilling high-dimensional Contrastive Language-Image Pretraining (CLIP) features directly into the scene representation. However, the instance grouping mechanisms of these methods either require a predefined number of instances or suffer from noise in their bottom-up grouping strategies. Furthermore, the reliance on CLIP restricts semantic understanding to simple noun phrases, preventing complex spatial reasoning and referential expression grounding. We present GaussDet, a method that circumvents the need for dense CLIP features by leveraging discrete, open-vocabulary 2D object detectors with referring expression capabilities. We learn instance features for individual Gaussians to decompose the scene into 3D instance groups. By rendering these groups and aggregating semantic votes from multi-view 2D detections, we generate a robust View-Aggregated Semantic Label Distribution (VASD) for each 3D instance. This view-aggregation strategy acts as a strong regularizer, attenuating spurious labels caused by low-quality instance grouping. Our approach enables a straightforward, zero-shot extension from simple language queries to complex referential grounding. Extensive evaluations across two key tasks -- open-vocabulary segmentation (LeRF-OVS, ScanNet) and referring expression grounding (Ref-LeRF) -- demonstrate that GaussDet achieves consistent improvements over existing methods. Most notably, we achieve a substantial 16.7% mIoU improvement in referential grounding within a strict zero-shot setting.

---


> [!TIP]
> 当前位于：**451-489**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-489**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
