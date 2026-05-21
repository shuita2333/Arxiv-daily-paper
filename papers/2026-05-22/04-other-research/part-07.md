# 📦 其他研究 | 2026年05月22日

> 本类共 **352** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-352](./part-08.md)

---

### 301. [Deformba: Vision State Space Model with Adaptive State Fusion](https://arxiv.org/abs/2605.21308)

**<font color=#1a73e8>作者：</font>** Hongyu Ke, Jack Morris, Yongkang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) have emerged as a powerful and efficient alternative to Transformers, demonstrating linear-time complexity and exceptional sequence modeling capabilities. However, their application to vision tasks remains challenging. First, existing vision SSMs largely depend on manually designed fixed scanning methods to flatten image patches into sequences, which imposes predefined geometric structures and increases the complexity. Second, the broader adoption of vision SSMs is hindered in domains that require query-based interactions between distinct information streams. This is a result of the inherently causal and self-referential nature of SSMs designed for 1D sequence modeling tasks. This fusion mechanism is indispensable for critical perception tasks such as multi-view 3D fusion. To address these limitations, we propose Deformba, a context adaptive method that dynamically augments the spatial structural information while maintaining the linear complexity of SSMs. Deformba also allows multi-modal fusion like cross attention. To demonstrate the effectiveness and general applicability of Deformba, we test its performance on general 2D vision tasks such as image classification, object detection, and segmentation, as well as 3D vision tasks like BEV perception. Extensive experiments show that Deformba achieves strong performance across various visual perception benchmarks.

---


### 302. [Hyper-V2X: Hypernetworks for Estimating Epistemic and Aleatoric Uncertainty in Cooperative Bird's-Eye-View Semantic Segmentation](https://arxiv.org/abs/2605.21309)

**<font color=#1a73e8>作者：</font>** Abhishek Dinkar Jagtap, Sanath Tiptur Sadashivaiah, Andreas Festag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cooperative perception enabled by Vehicle-to-Everything (V2X) communication enhances autonomous driving safety by creating a unified environmental representation through shared sensory data. While recent works have advanced multi-agent fusion for improved perception, uncertainty quantification in such cooperative frameworks remains largely unexplored. This paper introduces Hyper-V2X, a hypernetwork-based framework for estimating both epistemic and aleatoric uncertainties in V2X-based perception. Specifically, we propose a partial weight generation scheme and V2X context embedding module that conditions a Bayesian hypernetwork on fused multi-agent features to generate weight distributions for stochastic Bird's-Eye-View (BEV) segmentation. Unlike existing deterministic BEV models, Hyper-V2X enables efficient uncertainty estimation with little computation overhead. Our approach is architecture-agnostic, and can be seamlessly integrating with modern cooperative backbones such as CoBEVT. Experiments on the OPV2V benchmark demonstrate that Hyper-V2X provides accurate, well-calibrated uncertainty estimates and improves overall perception reliability. Our code and benchmark are publicly available under an open-source license: this https URL

---


### 303. [DeCoR: Design and Control Co-Optimization for Urban Streets Using Reinforcement Learning](https://arxiv.org/abs/2605.21311)

**<font color=#1a73e8>作者：</font>** Bibek Poudel, Lei Zhu, Kevin Heaslip 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern vision systems can detect, track, and forecast urban actors at scale, yet translating perception outputs to urban design remains limited. We introduce DeCoR, a two-stage reinforcement learning framework that leverages flow observations to co-optimize crosswalk layout and network-level signal control. The design stage encodes the pedestrian network as a graph and learns a generative policy that parameterizes a Gaussian mixture model over crosswalk location and width, from which new crosswalks are sampled. For each layout, a shared control policy learns adaptive signal timings to minimize joint pedestrian and vehicle delay. On a 750 m real-world urban corridor with demand sensed from video and Wi-Fi logs, DeCoR learns a layout that reduces pedestrian arrival time to their nearest crosswalk by 23% while using fewer crosswalks than existing configurations. On the control side, DeCoR reduces pedestrian and vehicle wait time by 79% and 65%, respectively, relative to fixed-time signalization. Further, the control policy generalizes to demands outside of training and is robust to layout changes without retraining.

---


### 304. [A New Framework to Analyse the Distributional Robustness of Deep Neural Networks](https://arxiv.org/abs/2605.21313)

**<font color=#1a73e8>作者：</font>** Divij Khaitan, Subhashis Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks have achieved impressive performance on a variety of tasks, but their brittleness to distributional shifts remains a significant barrier to real-world deployment. In this paper, we propose a framework to analyse and quantify the distributional robustness of neural networks by studying the interactions between layer weights and activations. We model these interactions using Bernoulli distributions, using the separation between classes as a diagnostic proxy for robustness. We demonstrate the usefulness of this framework through models trained on CIFAR-10 and ImageNet. We show that our proposed metrics can distinguish between networks that have memorised their training data and those that have not. We also perform analogous experiments in the activation space and find that the same properties do not hold up. Additionally, we investigate the behaviour of our metrics under various distribution shifts and show that these shifts reduce separation under our path-based diagnostics. Our results suggest that this framework provides useful model-level diagnostics of representation structure and robustness.

---


### 305. [CRAFT: Conflict-Resolved Aggregation for Federated Training](https://arxiv.org/abs/2605.21317)

**<font color=#1a73e8>作者：</font>** Ziqi Wang, Qiang Liu, Nils Thuerey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The aggregation of conflicting client updates remains a fundamental bottleneck in federated learning (FL) under heterogeneous data distributions. Naive averaging can produce a global update that improves the global objective while conflicting with specific clients, causing degradation for those clients. In this work, we propose CRAFT (Conflict-Resolved Aggregation for Federated Training), a new aggregation framework that treats the global update as a geometric correction problem. We formulate aggregation as finding the update closest to a reference direction while satisfying conflict-free alignment constraints. We derive a closed-form expression for the constrained optimization problem, avoiding the computational overhead of iterative solvers. Furthermore, we use a layer-wise adaptation to address conflicts at varying feature granularities. We provide a theoretical analysis showing that CRAFT promotes a common-descent structure and mitigates conflicts through its projection geometry. Extensive experiments on heterogeneous benchmarks demonstrate that CRAFT improves the accuracy of the global model while reducing performance disparity across clients compared with state-of-the-art baselines. The source code for CRAFT is available at this https URL.

---


### 306. [TextReg: Mitigating Prompt Distributional Overfitting via Regularized Text-Space Optimization](https://arxiv.org/abs/2605.21318)

**<font color=#1a73e8>作者：</font>** Lucheng Fu, Ye Yu, Yiyang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are highly sensitive to the prompts used to specify task objectives and behavioral constraints. Many recent prompt optimization methods iteratively rewrite prompts using LLM-generated feedback, but the resulting prompts often become longer, accumulate narrow sample-specific rules, and generalize poorly beyond the training distribution. We study this failure mode as prompt distributional overfitting and argue that it reflects a lack of representation control in discrete text-space optimization. We formalize this view through representational inefficiency, a dual-factor measure that decomposes prompt inefficiency into capacity cost and scope narrowness, attributing distributional prompt overfitting to their coupled growth during optimization. We propose TextReg, a regularization framework that realizes a soft-penalty objective through regularized textual gradients, combining Dual-Evidence Gradient Purification, Semantic Edit Regularization, and Regularization-Guided Prompt Update. Across multiple reasoning benchmarks, TextReg substantially improves out-of-distribution (OOD) generalization, with accuracy gains of up to +11.8% over TextGrad and +16.5% over REVOLVE.

---


### 307. [Optimized Federated Knowledge Distillation with Distributed Neural Architecture Search](https://arxiv.org/abs/2605.21322)

**<font color=#1a73e8>作者：</font>** Chaimaa Medjadji, Sylvain Kubler, Yves Le Traon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative model training without centralizing data. However, real-world deployments must simultaneously address statistical heterogeneity across client data (non-IID), system heterogeneity in device capabilities, and communication efficiency. Existing FL approaches mitigate these challenges through improved aggregation, personalization, or knowledge distillation, but they almost universally assume a fixed client architecture, limiting adaptability to heterogeneous data complexity and hardware constraints. This architectural constraint often leads to suboptimal trade-offs between accuracy and efficiency in real-world FL systems. This work introduces FedKDNAS, a distillation-driven FL framework that combines client-side neural architecture selection with distillation of server-coordinated knowledge. Each client autonomously selects a lightweight model under accuracy-resource constraints. It then trains it locally using a hybrid objective combining supervised learning and knowledge distillation and shares only predictions on a public reference set. The server then aggregates and smooths these predictions, optionally combining them with a teacher model, to produce stable distillation targets for the next round. Extensive evaluation on six datasets against six representative FL baselines (FedAvg, Ditto, FedMD, FedDF, FedDistill, Local-KD) demonstrates that FedKDNAS consistently achieves superior Pareto efficiency, improving accuracy by up to 15\% under non-IID conditions, reducing client CPU usage by approximately 28\%, and decreasing communication overhead by up to 44 times while maintaining lightweight logit-based communication.

---


### 308. [Fast and Stable Triangular Inversion for Delta-Rule Linear Transformers](https://arxiv.org/abs/2605.21325)

**<font color=#1a73e8>作者：</font>** Aleksandros Sobczyk, Gioele Gottardo, Christos K. Matzoros 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention has emerged as a cornerstone for efficient long-context architectures, as evidenced by its integration into state-of-the-art open-source models including Qwen3.5/3.6, Kimi Linear, and RWKV-7. Models that incorporate linear attention layers with the so-called Delta-Rule involve the inversion of triangular matrices as a core sub-routine. This operation often forms a performance bottleneck, and, due to its high-sensitivity to numerical errors, it can significantly deteriorate end-to-end model accuracy if it is not carefully implemented. This work provides a systematic analysis of both direct and iterative triangular inversion algorithms, targeting methods that are rich in matrix products, and, therefore, have the potential to efficiently utilize modern hardware. To that end, our analysis covers a broad spectrum of mathematical and practical aspects, with a heavy focus on numerical stability, computational complexity, and, ultimately, hardware efficiency and practical considerations. We provide a rigorous experimental evaluation to verify these properties in practical scenarios, and in low-precision floating-point representations, highlighting the strengths and limitations of each method. Performance benchmarks on NPUs reveal up to $4.3\times$ speed-up against the state-of-the-art implementations of SGLang for triangular matrix inversion, leading to significant performance improvements on the entire layer level, while maintaining full end-to-end model accuracy.

---


### 309. [OcclusionFormer: Arranging Z-Order for Layout-Grounded Image Generation](https://arxiv.org/abs/2605.21343)

**<font color=#1a73e8>作者：</font>** Ziye Li, Henghui Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent layout-to-image models have achieved remarkable progress in spatial controllability. However, they still struggle with inter-object occlusion. When bounding boxes overlap, most existing methods lack explicit occlusion information, which makes the generation in intersection regions inherently ambiguous and hinders the determination of complex occlusion relationships. As a result, they often produce entangled textures or physically inconsistent layering in the overlapped areas. To address this issue, we first construct SA-Z, a large-scale dataset enriched with explicit occlusion ordering and pixel-level annotations. Building upon our proposed dataset, we introduce OcclusionFormer, a novel occlusion-aware Diffusion Transformer framework that explicitly models Z-order priority by decoupling instances and compositing them via volume rendering. Furthermore, to ensure fine-grained spatial precision, we introduce a queried alignment loss that explicitly supervises individual instances and enhances semantic consistency. The proposed method effectively reduces ambiguity in overlapping regions, enforces correct occlusion dependencies, and preserves structural integrity, leading to substantial accuracy gains across diverse scenes.

---


### 310. [Data-Efficient Neural Operator Training via Physics-Based Active Learning](https://arxiv.org/abs/2605.21348)

**<font color=#1a73e8>作者：</font>** Alicja Polanska, Lorenzo Zanisi, Vignesh Gopakumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving partial differential equations with neural operators significantly reduces computational costs but remains bottlenecked by high training data requirements. Active learning offers a natural framework to mitigate this by selectively acquiring the most informative samples in an iterative manner. We introduce physics-based acquisition - a novel physics-informed active learning algorithm that leverages the partial differential equation residual to guide data selection. We validate the method by presenting numerical experiments for the 1D Burgers equation and the 2D compressible Navier-Stokes equations. We show that, in our experiments, physics-based acquisition consistently outperforms random acquisition and matches the state of the art in data efficiency. At the same time, it has the unique advantage of injecting a physics inductive bias into the training process, ensuring that simulation cost is spent where the model's physical understanding is weakest.

---


### 311. [Onion-Routed Multi-Circuit Key Establishment for Quantum-Resilient Sessions](https://arxiv.org/abs/2605.21349)

**<font color=#1a73e8>作者：</font>** Tushin Mallick, Ashish Kundu, Ramana Kompella  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public-key primitives that today anchor session-key establishment - RSA, Diffie-Hellman, and elliptic-curve cryptography - reduce to integer factorization or discrete logarithm and are therefore vulnerable to Shor's algorithm on a sufficiently capable quantum computer. The harvest-now, decrypt-later (HNDL) threat model turns this future capability into a present liability: ciphertext archived today can be decrypted retrospectively once a cryptographically relevant quantum computer becomes available. We propose a session-key establishment scheme that distributes a freshly generated key as multiple, independently encrypted fragments across distinct, ephemeral Tor circuits between an onion-service proxy and an onion-service client. Reconstruction requires every fragment; each fragment travels its own per-bundle circuit established via a NEWNYM signal. The security argument rests on the standard end-to-end correlation bound for onion routing: an adversary controlling a fraction of Tor relays must independently deanonymize every fresh circuit to correlate the fragments belonging to one session, and the per-fragment probability of success decays multiplicatively in the number of fragments. We implement the design as a Flask-based prototype on AWS EC2, with both the proxy and the client deployed as Tor onion services, and measure end-to-end key-establishment latency. The implemented prototype completes a key establishment in 13-20 s on average (7-50 s including tails), of which approximately 88% is attributable to Tor-related delay - a cost we discuss in the context of the privacy-versus-responsiveness trade-off.

---


### 312. [The Human-AI Delegation Dilemma: Individual Strategies, Collective Equilibria and Sociotechnical Lock-in](https://arxiv.org/abs/2605.21351)

**<font color=#1a73e8>作者：</font>** Angjelin Hila  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper takes an ecological approach toward large-scale models of hybrid human-AI intelligence. Emerging models of human-AI interaction predominantly advance the complementarity thesis variously dubbed human-AI collaboration and human-AI hybrid intelligence. However, this constitutes an over-simplification of the modalities of human-AI interaction and possibility-space for both individual and collective action that human-AI interaction potentiates. To fill these gaps, this paper develops a decision and game-theoretic approach to the human-AI delegation-verification dilemma. First, we map out canonical decision-theoretic strategies that account for adaptive user trajectories, modeling how agents transition between strategies based on interaction feedback to reach stable equilibria. Second, we scale individually stable strategies to collective equilibria using three extrapolation principles: (a) non-communicative aggregation (b) local social signaling and (c) institutional norms setting. The analysis identifies the emergence of sociotechnical lock-in, a macro-behavioral state where individually adaptive delegation, in the absence of communicative and institutional safeguards, aggregates into a systemic collective action problem modeled as a prisoner's dilemma that degrades shared epistemic standards. We argue that adoption under higher communicative standards and institutional norms can mitigate suboptimal collective equilibria by imposing social commitments on individual users.

---


### 313. [Classification of Single and Mixed Partial Discharges under Switching Voltage Using an AWA-CNN Framework](https://arxiv.org/abs/2605.21352)

**<font color=#1a73e8>作者：</font>** Md Rafid Kaysar Shagor, Zannatul Ferdousy Mouri, Farhina Haque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing use of fast-switching power electronics has made partial discharge (PD) analysis under switching-voltage excitation increasingly important, yet more challenging than under sinusoidal conditions due to activity concentrated at voltage transitions. This work presents an Amplitude-Width-Area (AWA) pattern representation for source-oriented PD analysis under switching-voltage excitation. In the proposed method, time domain PD pulses are characterized using pulse amplitude, width, and area, and mapped into a visual pattern where amplitude and area define the coordinate axes and width is encoded by color. The generated AWA patterns are used to distinguish six single and mixed PD source conditions: corona, internal, surface, corona+internal, corona+surface, and internal+surface. To evaluate the classification capability of the proposed representation, a Random Forest baseline and two Convolutional Neural Network (CNN) models, InceptionV3 and ResNet-18, are compared. The AWA patterns show distinguishable source-dependent distributions, and CNN-based classification achieves testing accuracy above 96%, compared with 73.33% for Random Forest. The results indicate that AWA patterns provide a visual representation of PD pulses suitable for multi-class PD source classification under switching-voltage excitation.

---


### 314. [Gen-AI-tecture: using generative AI to support architectural students in design tasks](https://arxiv.org/abs/2605.21361)

**<font color=#1a73e8>作者：</font>** Timo Kapsalis  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The "Gen-AI-tecture" project embeds a locally executed, discipline-specific tool into a mixed-methods focus-group design, structured around three research objectives: (a) to evaluate how generative AI tools impact students' creativity in design-thinking processes and outcomes, (b) to assess whether these tools enhance inclusivity in learning processes, and (c) to examine how they develop students' AI-handling skills with a view to boosting future employability. Findings indicate enhanced creative fluency, broadened participation across diverse learner profiles, and strengthened confidence in AI-supported design processes. The study contributes evidence-based guidance for integrating generative-AI workflows into architectural pedagogy, demonstrating how such tools can operationalise constructivist principles of learner-led meaning-making, support connectivist understandings of learning as participation in human-AI networks, and advance universal learning theories by promoting more inclusive, flexible and accessible educational practices for contemporary learners.

---


### 315. ["I didn't Make the Micro Decisions": Measuring, Inducing, and Exposing Goal-Level AI Contributions in Collaboration](https://arxiv.org/abs/2605.21363)

**<font color=#1a73e8>作者：</font>** Eunsu Kim, Jessica R. Mindel, Kyungjin Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) increasingly shape how users form, refine, and extend their goals, attributing contributions in human-AI collaboration becomes critical for users calibrating their own reliance and for evaluators assessing AI-assisted work. Yet existing methods focus on final artifacts, missing the process through which goals themselves are jointly shaped. We introduce a goal-level attribution framework, CoTrace, that decomposes explicit goals into verifiable requirements and traces both direct contributions and indirect influences across dialogue turns. Applying CoTrace to 638 real-world collaboration logs, we find that while models account for only 11-26% of goal-shaping contribution, they contribute substantially more on introducing lower-level concrete requirements, and make various kinds of indirect contributions. Through controlled simulations, we show that interaction design choices significantly affect model goal-shaping behavior. In a user study, exposing participants to goal-level analyses shifts their perceived contributions by nearly 2 points on a 5-point scale, revealing systematic miscalibration in how users understand their own AI-assisted work.

---


### 316. [Findings of the Fifth Shared Task on Multilingual Coreference Resolution: Expanding Datasets for Long-Range Entities](https://arxiv.org/abs/2605.21369)

**<font color=#1a73e8>作者：</font>** Michal Novák, Miloslav Konopík, Anna Nedoluzhko 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the fifth edition of the Shared Task on Multilingual Coreference Resolution, held in conjunction with the CODI-CRAC 2026 workshop. Building on previous iterations, the task required participants to develop systems capable of mention identification and identity-based coreference clustering.
The 2026 edition specifically emphasizes long-range entities, defined as coreferential chains spanning significant distances, across many words and sentences.
The task expanded its linguistic scope by incorporating five new datasets and two additional languages. These additions leverage version 1.4 of CorefUD, a harmonized multilingual collection comprising 27 datasets in 19 languages.
In total, ten systems participated, including four LLM-based approaches (three fine-tuned models and one few-shot approach). While traditional systems still maintained their lead, LLMs demonstrated significant potential, suggesting they may soon challenge established approaches in future editions.

---


### 317. [A Non-Reference Diffusion-Based Restoration Framework for Landsat 7 ETM+ SLC-off Imagery in Antarctica](https://arxiv.org/abs/2605.21371)

**<font color=#1a73e8>作者：</font>** Leyue Tang, Jonathan Louis Bamber, Gang Qiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acquiring usable optical imagery in Antarctica is inherently challenging due to prolonged polar nights and frequent cloud cover. Landsat provides the longest and most continuous optical observations and constitutes one of the most important remote sensing data sources for Antarctic studies. However, the scan-line corrector (SLC) failure in 2003 resulted in approximately 22% missing pixels in Landsat 7 ETM+ SLC-off imagery, severely limiting its usability. Unlike many non-polar environments, Antarctic surfaces undergo rapid and substantial changes, which makes it difficult to obtain reliable reference imagery and reduces the applicability of conventional reference-based gap-filling methods. To address this challenge, we propose DiffGF, a non-reference diffusion-based framework for restoring Landsat 7 SLC-off imagery without requiring any external reference data. DiffGF adopts a two-stage design consisting of a latent-space diffusion process and a pixel-space refinement. A dedicated Antarctic dataset, SLCANT, is constructed for training and evaluation. Quantitative and qualitative results demonstrate that DiffGF restores Antarctic SLC-off imagery with high fidelity. Its practical value is further examined through a downstream crevasse segmentation application. The results suggest that DiffGF provides a useful approach for exploiting Landsat 7 SLC-off archives in Antarctica, enabling the extraction of valuable information from historical records and supporting related Antarctic studies.

---


### 318. [Closed Loop Dynamic Driving Data Mixture for Real-Synthetic Co-Training](https://arxiv.org/abs/2605.21372)

**<font color=#1a73e8>作者：</font>** Hongzhi Ruan, Pei Liu, Weiliang Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data scaling is fundamental to modern deep learning, and grows increasingly critical as autonomous driving shifts to end-to-end learning. Real-world driving data is expensive to annotate and scene-biased, making real-synthetic co-training with near-infinite synthetic data a promising direction. However, naively incorporating all available synthetic data is inefficient and leads to distribution shifts, and optimizing data mixture under practical training budgets remains a critical yet under-explored problem. In this sense, we claim that the mixture of training data requires clear guidance in terms of scene types and quantities. Particularly in this work, we conceptualize the data mixture approximately as a dynamic optimization process that iteratively adjusts the training data mixture to maximize model performance, guided by closed-loop evaluation feedback, and propose AutoScale, a fully automated closed-loop data engine unifying scene representation, data mixture optimization and retrieval, as well as model training and evaluation. Specifically, we propose Graph Regularized AutoEncoder (Graph-RAE) for driving scene representations, introduce Cluster-aware Gradient Ascent (Cluster-GA) for cluster-wise importance estimation and reweighting, and perform cluster-guided vector retrieval to select high-value samples. Experiments on NavSim demonstrate that AutoScale outperforms vanilla co-training and cross-domain baselines, achieving better performance with fewer synthetic samples under constrained budgets.

---


### 319. [Auditing Apple's DifferentialPrivacy.framework: Implementation Bugs, Misconfigurations, and Practical Risks](https://arxiv.org/abs/2605.21378)

**<font color=#1a73e8>作者：</font>** Rishav Chourasia, Ergute Bao, Uzair Javaid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Since 2016, Apple has claimed that device analytics collected to improve user experience are protected by differential privacy (DP). Apple's this http URL is deployed across its operating systems and handles sensitive signals such as Safari domains, keyboard events, photo attributes, and health-related reports. Because Apple has not open-sourced its privatization algorithms, these privacy claims have been difficult to verify independently.
We present a client-side audit of Apple's DP framework on macOS Sonoma 14.2 and Sequoia 15.6. We reverse engineer the shipped binaries, recover Objective-C interfaces, build runtime harnesses that execute Apple's deployed mechanisms, and test whether their outputs match the advertised privacy guarantees. Our audit covers nearly all active deployed mechanisms, including Count Median Sketch, Hadamard-CMS, randomized-response mechanisms, and Prio-style secure aggregation.
We find multiple implementation bugs and misconfigurations. Every audited mechanism that relies on floating-point noise fails to meet its advertised DP or zero-knowledge proof guarantee, due to insecure samplers with known floating-point vulnerabilities. We also find secure-aggregation configurations with local DP disabled, exposing pre-aggregation records to any party with access to those logs. Overall, we find DP violations in 5 of 9 audited mechanisms, affecting 87% of data collection in macOS Sonoma and 68% in Sequoia. We also identify public leaked iPhone logs that can be decoded to recover private information, including Safari domains and keyboard emoji signals.

---


### 320. [Disentangling Generation and Regression in Stochastic Interpolants for Controllable Image Restoration](https://arxiv.org/abs/2605.21381)

**<font color=#1a73e8>作者：</font>** Yi Liu, Jia Ma, Wengen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Image Restoration (IR) have been largely driven by generative methods such as Diffusion Models and Flow Matching, which excel in synthesizing realistic textures while suffering from slow multi-step inference and compromised pixel fidelity. In contrast, classical regression-based IR methods excel precisely in these aspects, offering single-step efficiency and high pixel-level reconstruction fidelity. To bridge this gap, we propose DiSI, a unified framework that Disentangles the underlying Stochastic Interpolant process into independent generation and regression components. This decoupling endows DiSI with remarkable versatility, enabling a continuous and controllable transition from a pure regression process to a fully generative one. Technically, we instantiate this framework with two specific sampling trajectories, accompanied by a unified sampler for high-quality, few-step inference on arbitrary trajectories. Furthermore, we design a dual-branch U-Net style transformer network in pixel space, using a dedicated branch to enhance conditional guidance while ensuring high throughput. Extensive experiments demonstrate that DiSI efficiently achieves competitive results on various IR tasks, while uniquely offering the inference-time flexibility to control the distortion-perception trade-off within a single model.

---


### 321. [On the Regularity and Generalization of One-Step Wasserstein-guided Generative Models for PDE-Induced Measures](https://arxiv.org/abs/2605.21388)

**<font color=#1a73e8>作者：</font>** Likun Lin, Zhongjian Wang, Jack Xin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable empirical success of generative models, the available theory on their statistical accuracy in scientific computing remains largely pessimistic. This paper develops a theoretical framework for understanding the regularity of transport maps and the generalization properties of one-step Wasserstein-guided generative models for PDE-induced probability measures. We consider normalized target densities associated with linear elliptic and parabolic equations on bounded domains, as well as diffusion and Fokker--Planck equations on the torus. Under standard structural assumptions, we prove that these target measures satisfy doubling conditions. By combining this fact with regularity theory for optimal transport between doubling measures, we show that the optimal transport map from a uniform source measure to the target measure is Hölder continuous. This regularity yields an approximation-theoretic justification for one-step generative models that learn PDE-induced distributions via a single pushforward map. As a representative instance, we study DeepParticle and derive excess-risk bounds characterizing the discrepancy between the learned map and the population-optimal map. We also establish a robustness estimate under target shift and illustrate the theory with experiments which support the derived rates.

---


### 322. [Designing Conversations with the Dead: How People Engage with Generative Ghosts](https://arxiv.org/abs/2605.21390)

**<font color=#1a73e8>作者：</font>** Jack Manning, Daniel Sullivan, Dylan Thomas Doyle 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We examine how people experience two choices in the design of generative ghosts, AI systems that are trained on data of the dead: representation, where an AI speaks about a deceased person in the third person, and reincarnation, where the AI speaks as the deceased in the first person. Through a qualitative user study with 16 participants, we explore how each shaped authenticity, affect, and risk. Reincarnation was preferred for its immediacy, but participants shared fears of over-reliance. Representation was preferred for engaging with memory over conversational presence, though participants often ignored this distinction, engaging in dialogue despite third-person framing. Across both modes, participants privileged affective resonance over factual fidelity. We conclude by showing how factors such as tone, language, and conversational rhythm -- factors unique to the user's memory of the deceased -- shape interactions with generative ghosts, and argue that those interactions are always collaborative.

---


### 323. [VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers](https://arxiv.org/abs/2605.21392)

**<font color=#1a73e8>作者：</font>** Pengyu Sun, Qishu Jin, Enhao Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model Context Protocol (MCP) has emerged as a standard interface for connecting LLM agents to external tools. Because MCP servers expose privileged operations such as shell execution, network access, and file-system manipulation to agent-driven invocation, implementation flaws in tool handlers can create a direct path from natural-language input to security-sensitive sinks, potentially granting attackers remote code execution or full system compromise. Existing approaches either produce unconfirmed static alerts without dynamic validation, or rely on fixed template libraries that lack code-level guidance and fail to trigger vulnerabilities requiring specific parameter shapes or multi-step taint paths.
In this paper, we present VIPER-MCP, the first end-to-end automated vulnerability auditing framework for MCP servers that not only detects taint-style vulnerabilities but also dynamically confirms their exploitability by producing concrete proof-of-concept prompts. VIPER-MCP introduces two novel techniques: (1) an anchor-query pass in a two-pass static analysis strategy that augments standard taint alerts with function-level structural context, resolving file-level static artifacts to specific MCP tool handlers and producing vulnerability-anchored call chains; and (2) a feedback-driven prompt evolution mechanism that employs dual-mutator scheduling that independently corrects tool-selection drift and deepens parameter penetration, together with fitness-scored seed selection to iteratively refine natural-language prompts toward vulnerable sinks. In a large-scale scan of 39,884 real-world open-source MCP server repositories, VIPER-MCP discovered 106 0-day vulnerabilities, all of which were confirmed through end-to-end exploit traces, with 67 CVE IDs assigned to date. We responsibly disclosed all confirmed findings to the affected developers and coordinated CVE assignment where applicable.

---


### 324. [Towards Resilient and Autonomous Networks: A BlueSky Vision on AI-Native 6G](https://arxiv.org/abs/2605.21395)

**<font color=#1a73e8>作者：</font>** Liang Wu, Kelly Wan, Mayank Darbari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The proliferation of emerging applications, such as autonomous driving and immersive experiences, demands cellular networks that are not only faster, but fundamentally more resilient and autonomous. This paper presents a BlueSky vision on how Artificial Intelligence will be natively integrated into 6G, shifting the paradigm from \underline{Network for AI} to \underline{AI for Network}. We envision that, unlike 5G's reliance on scattered, ad-hoc models each trained for a single task, native AI in the 6G era will be anchored by a foundation model and and orchestrated via collaborative multi-agent systems, framing network management as a unified, multi-modal, multi-task optimization problem. Built on this vision, we outline two transformative directions. The first focuses on developing a 6G foundation model as a unified backbone, with task-specific knowledge distilled into compact models suited for diverse edge deployments. The second advances multi-agent systems designed to autonomously diagnose, maintain, and recover networks with minimal human intervention. These directions chart a roadmap for 6G to evolve into an intelligent, self-sustaining communication infrastructure.

---


### 325. [Quantifying the cross-linguistic effects of syncretism on agreement attraction](https://arxiv.org/abs/2605.21403)

**<font color=#1a73e8>作者：</font>** Utku Turk, Eva Neu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agreement attraction errors, in which a verb erroneously agrees with an intervening noun rather than its grammatical head, are amplified by morphological syncretism in some languages (English, German, Russian) but not others (Turkish, Armenian), a cross-linguistic pattern without a principled account. We use surprisal and attention entropy from large language models as processing proxies to investigate this variation across four languages. LLM-derived measures replicate behavioral findings in English and German (syncretism modulates attraction), align with Turkish null results (no modulation), and partially capture Russian patterns. We discuss further directions for better understanding why syncretism affects agreement attraction differently across languages.

---


### 326. [RoadTones: Tone Controllable Text Generation from Road Event Videos](https://arxiv.org/abs/2605.21411)

**<font color=#1a73e8>作者：</font>** Chirag Parikh, Siddhi Pravin Lipare, Ravi Kiran Sarvadevabhatla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing video-language models can generate factual descriptions of road events but lack control over how these events are expressed: their tone, urgency, or style. This limits deployment in communication-critical settings where the effectiveness of a message depends on both content and presentation, not just factual accuracy. To mitigate this, we introduce a comprehensive dataset-model-evaluation suite for tone-controllable road video captioning. Our human-validated data generation pipeline expands road-video corpora with diverse tonal annotations and multi-tone captions, yielding the RoadTones-51K dataset. We propose RoadTones-VL-CoT, a controllable video-to-text model that also generates tone-conditioned Chain-of-Thought intermediate drafts for interpretability. We also introduce RoadTones-Eval, a new evaluation suite that jointly measures factual consistency and tone adherence. In addition, we conducted a user study whose results validate caption quality, tone control, and factual consistency. Together, these contributions lay the foundation for context-sensitive tone-controllable video captioning.

---


### 327. [Teaching AI Through Benchmark Construction: QuestBench as a Course-Based Practice for Accountable Knowledge Work](https://arxiv.org/abs/2605.21413)

**<font color=#1a73e8>作者：</font>** Haiyang Shen, Jiuzheng Wang, Taian Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI becomes part of everyday learning, many courses teach students to use it mainly as a productivity tool: how to prompt, search, summarize, write, code, and use tools more efficiently. We argue that AI education also needs a setting in which students learn to test AI and understand their own role in judging machine-produced knowledge. To this end, we introduce a course-based practice that teaches AI through benchmark construction, using deep research systems as a concrete example of AI-era knowledge work. Students turn disciplinary knowledge into verifiable expert-level questions, review one another's designs for ambiguity and shortcuts, and evaluate AI systems on the resulting tasks. This activity gives students direct exposure to a powerful tool while asking them to specify what a trustworthy answer would require. The produced benchmark, QuestBench, consists of 256 questions across 14 humanities and social-science domains. Evaluation on QuestBench shows that student-designed tasks reveal hidden failures in current deep research systems: across thirteen evaluated systems, the mean question-level pass rate is only 16.85%, and the best-performing system, GPT-5.5, reaches a 57.58% pass rate. The failures are educationally useful because they show how fluent, source-backed answers can still miss the right query, source, term, or evidence standard. Reflections from five student contributors suggest that benchmark construction can help students see professional knowledge not only as content AI may retrieve, but as the basis for judging AI outputs. We present QuestBench as a benchmark artifact and as a reusable classroom setting for a larger educational question: how students can remain responsible knowledge actors as AI enters learning and professional work. The dataset is available at this https URL.

---


### 328. [Ordering Matters: Rank-Aware Selective Fusion for Blended Emotion Recognition](https://arxiv.org/abs/2605.21417)

**<font color=#1a73e8>作者：</font>** Junghyun Lee, Hyunseo Kim, Hanna Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blended emotion recognition is challenging because emotions are often expressed as mixtures of subtle and overlapping multimodal cues rather than a single dominant signal. We propose a rank-aware multi-encoder framework that selectively combines complementary representations from diverse pre-extracted video and audio encoders. Our method projects heterogeneous encoder features into a shared latent space, estimates sample-wise encoder importance through an attention-based gating module, and fuses only the top-n most informative encoders. To better model blended emotions, we decouple prediction into presence and salience heads and align them through probability-level fusion. We further incorporate feature-level unsupervised domain adaptation without pseudo-labeling to improve robustness under distribution shift. Experiments on the BlEmoRE challenge show that the proposed framework outperforms strong individual encoders and naïve multi-encoder fusion baselines. Our final system ranked 2nd in the competition, supporting the effectiveness of rank-aware selective fusion for fine-grained blended emotion recognition.

---


### 329. [FedCritic: Serverless Federated Critic Learning-based Resource Allocation for Multi-Cell OFDMA in 6G](https://arxiv.org/abs/2605.21418)

**<font color=#1a73e8>作者：</font>** Amin Farajzadeh, Melike Erol-Kantarci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In sixth-generation (6G) ultra-dense networks, aggressive frequency reuse amplifies inter-cell interference (ICI), making multi-cell orthogonal frequency-division multiple access (OFDMA) scheduling and power control strongly coupled across neighboring cells. We study distributed downlink resource management -- joint subcarrier scheduling and power allocation -- under interference coupling and long-term per-user quality-of-service (QoS) minimum-rate constraints. By using virtual-queue deficit weights to enforce long-term QoS, we develop FedCritic, a serverless federated multi-agent actor-critic framework with decentralized execution. Unlike centralized training with decentralized execution (CTDE) approaches that require centralized critic learning and joint trajectory aggregation, FedCritic federates the critic through lightweight gossip-based parameter averaging over the interference graph, enabling stable value estimation without a central coordinator while keeping policies local. Simulations in an interference-rich reuse-1 setting show that FedCritic improves mean signal-to-interference-plus-noise ratio (SINR) and cell-edge rate, increases network-wide average sum-rate and fairness relative to non-coordinated and CTDE baselines, and achieves more stable training with lower coordination overhead.

---


### 330. [HiRes: Inspectable Precedent Memory for Reaction Condition Recommendation](https://arxiv.org/abs/2605.21420)

**<font color=#1a73e8>作者：</font>** Shreyas Vinaya Sathyanarayana, Raja Sekhar Pappala, Deepak Warrier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reaction condition recommendation sits immediately after retrosynthetic disconnection selection, and in practice, chemists require both accurate predictions and the precedents that justify them. We present HiRes (Hierarchical Reaction Representations), a retrieval-augmented condition recommendation system whose learned reaction space serves as both a classifier feature and an inspectable precedent memory. The model combines a graph encoder, transformation-aware cross-attention, multi-stream reaction fusion, and a k-NN retrieval layer. HiRes achieves state-of-the-art performance among primary-slot USPTO-Condition models, reaching Catalyst, Solvent, and Reagent top-1 accuracies (Acc@1) of 0.929, 0.534, and 0.530 respectively. It ties the best reported baseline on Catalyst while outperforming models such as REACON on Solvent and Reagent. Furthermore, paired bootstrap analysis demonstrates that integrating retrieval with learned condition heads provides statistically significant gains for solvent and reagent selection over purely parametric approaches. Ultimately, HiRes bridges the gap between predictive accuracy and chemical interpretability, offering a single representation that supplies both competitive recommendations and the concrete chemical precedents necessary for practical synthesis planning.

---


### 331. [AIGaitor: Privacy-preserving and cloud-free motion analysis for everyone, using edge computing](https://arxiv.org/abs/2605.21421)

**<font color=#1a73e8>作者：</font>** Lauhitya Reddy, Trisha M. Kesar, Hyeokhyen Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion capture is the gold standard for measuring human movement, but clinical use remains limited by cost, technical complexity, and privacy concerns. AIGaitor is a privacy-preserving, cloud-free motion analysis system that runs markerless monocular motion-capture pipelines and downstream deep-learning analysis entirely on a consumer smartphone using on-device neural accelerators. To motivate its design, we surveyed 74 rehabilitation clinicians: 92 percent said they would adopt an accurate, cost-effective, easy-to-use AI gait analysis tool, while 79.7 percent cited operating cost, 68.9 percent insufficient training, and 64.9 percent privacy concerns as leading barriers. We then optimized and benchmarked mobile iOS implementations of current monocular pipeline components, including 2D and 3D pose estimation, pose optimization, skeleton-based deep-learning analysis, and a vision-language model. A Time-Priority end-to-end on-device pipeline processes a 10 s 4K 60 fps video clip in 77 s on an iPhone 14, matching or beating the same pipeline on a high-end NVIDIA H200 cloud server when network transfer is included: 94 s at global mobile-average uplink and 66 s at developed-world Wi-Fi. Lightweight models such as ViTPose-s achieve real-time keypoint extraction, and skeleton-based action-recognition models provide sub-millisecond gait classification on the same clip. To our knowledge, AIGaitor is the first monocular system to demonstrate end-to-end on-device motion capture and downstream deep-learning analysis, supporting clinically applicable movement analysis that is low-cost, private, and accessible to smartphone users.

---


### 332. [Adaptive Signal Resuscitation: Channel-wise Post-Pruning Repair for Sparse Vision Networks](https://arxiv.org/abs/2605.21426)

**<font color=#1a73e8>作者：</font>** Qishi Zhan, Ziheng Chen, Minxuan Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-shot magnitude pruning can cause severe accuracy collapse in the high-sparsity regime, even when the pruning mask preserves the largest weights. We argue that this failure reflects a granularity mismatch in post-pruning repair. Under global magnitude pruning, nearly collapsed channels can coexist with channels that retain informative activation variance within the same layer. Existing layer-wise activation repair methods apply a single correction to the whole layer, and can therefore over-amplify damaged channels while trying to restore the layer-level signal. We propose Adaptive Signal Resuscitation (ASR), a training-free channel-wise repair method that matches the granularity of repair to the granularity of damage. ASR estimates a variance-matching correction for each output channel and stabilizes it with a data-driven shrinkage rule, suppressing unreliable corrections for channels with weak post-pruning signal while preserving corrections for healthier channels. Applied before BatchNorm recalibration, ASR requires only forward passes on a small calibration set and no retraining. Across three datasets, four convolutional architectures, and both unstructured and structured sparsity settings, ASR generally improves over layer-wise repair, with the clearest gains in high-sparsity regimes. On ResNet-50 at 90% sparsity, ASR recovers 55.6% top-1 accuracy on CIFAR-10, compared with 41.0% for layer-wise repair and 28.0% for BatchNorm-only recalibration. Ablations show that naive channel-wise variance matching is insufficient, and that shrinkage stabilizes post-pruning repair.

---


### 333. [Polynomial-Time Robust Multiclass Linear Classification under Gaussian Marginals](https://arxiv.org/abs/2605.21428)

**<font color=#1a73e8>作者：</font>** Ilias Diakonikolas, Giannis Iakovidis, Mingchen Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the task of agnostic learning of multiclass linear classifiers under the Gaussian distribution. Given labeled examples $(x, y)$ from a distribution over $\mathbb{R}^d \times [k]$, with Gaussian $x$-marginal, the goal is to output a hypothesis whose error is comparable to that of the best $k$-class linear classifier. While the binary case $k=2$ has a well-developed algorithmic theory, much less is known for $k \ge 3$. Even for $k=3$, prior robust algorithms incur exponential dependence on the inverse of the desired accuracy in both complexity and representation size. In this work, we develop new structural results for multiclass linear classifiers and use them to design fully polynomial-time robust learners with dimension-independent error guarantees. Our first result shows that the standard multiclass perceptron algorithm requires super-polynomially many samples and updates, even with clean labels and Gaussian marginals, revealing a basic obstruction absent in the binary case. Our main positive result is a pairwise improper-learning framework which yields an efficient learner with error $\widetilde O(k^{3/2}\sqrt{\mathrm{opt}})+\epsilon$ for general $k$. Additionally, we develop a sharper localization-based framework which leads to error $O(\mathrm{opt})+\epsilon$ for $k=3$, and error $\mathrm{poly}(k)\mathrm{opt}+\epsilon$ for geometrically regular $k$-class linear classifiers.

---


### 334. [iTryOn: Mastering Interactive Video Virtual Try-On with Spatial-Semantic Guidance](https://arxiv.org/abs/2605.21431)

**<font color=#1a73e8>作者：</font>** Jun Zheng, Zhengze Xu, Mengting Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Virtual Try-On (VVT) aims to seamlessly replace a garment on a person in a video with a new one. While existing methods have made significant strides in maintaining temporal consistency, they are predominantly confined to non-interactive scenarios where models merely showcase garments. This limitation overlooks a crucial aspect of real-world apparel presentation: active human-garment interaction. To bridge this gap, we introduce and formalize a new challenging task: Interactive Video Virtual Try-On (Interactive VVT), where subjects in the video actively engage with their clothing. This task introduces unique challenges beyond simple texture preservation, including: (1) resolving the semantic ambiguity of interactions from standard pose information, and (2) learning complex garment deformations from video where interactive moments are sparse and brief. To address these challenges, we propose iTryOn, a novel framework built upon a large-scale video diffusion Transformer. iTryOn pioneers a multi-level interaction injection mechanism to guide the generation of complex dynamics. At the spatial level, we introduce a garment-agnostic 3D hand prior to provide fine-grained guidance for precise hand-garment contact, effectively resolving spatial ambiguity. At the semantic level, iTryOn leverages global captions for overall context and time-stamped action captions for localized interactions, synchronized via our novel Action-aware Rotational Position Embedding (A-RoPE). Extensive experiments demonstrate that iTryOn not only achieves state-of-the-art performance on traditional VVT benchmarks but also establishes a commanding lead in the new interactive setting, marking a significant step towards more dynamic and controllable virtual try-on experiences.

---


### 335. [Gaussian Sheaf Neural Networks](https://arxiv.org/abs/2605.21435)

**<font color=#1a73e8>作者：</font>** André Ribeiro, Ana Luiza Tenório, Tiago da Silva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have become the de facto standard for learning on relational data. While traditional GNNs' message passing is well suited for vector-valued node features, there are cases in which node features are better represented by probability distributions than real vectors. Concretely, when node features are Gaussians, characterized by a mean and a covariance matrix, naively concatenating their parameters into a single vector and applying standard message passing discards the geometric and algebraic structure that governs means and covariances. We propose Gaussian Sheaf Neural Networks (GSNNs), a principled framework that incorporates these inductive biases into graph-based learning. Building on the theory of cellular sheaves, we derive a new Laplacian operator that generalizes the sheaf Laplacian to this setting and preserves its key properties. We complement our theoretical contributions with experiments on synthetic and real-world data that illustrate the practical relevance of GSNNs.

---


### 336. [ReMATF: Recurrent Motion-Adaptive Multi-scale Turbulence Mitigation for Dynamic Scenes](https://arxiv.org/abs/2605.21440)

**<font color=#1a73e8>作者：</font>** Zhiming Liu, Zhicheng Zou, Nantheera Anantrasirichai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Atmospheric turbulence severely degrades video quality by introducing distortions such as geometric warping, blur, and temporal flickering, posing significant challenges to both visual clarity and temporal consistency. Current state-of-the-art methods are based on transformer, 3D architectures and require multi-frame input, but their large computational cost and memory usage limit real-time deployment, especially in resource-constrained scenarios. In this work, we propose ReMATF, a lightweight recurrent framework that restores videos using only two frames at a time while preserving spatial detail and temporal stability. ReMATF combines a multi-scale encoder-decoder with temporal warping and a motion-adaptive temporal fusion module that performs per-pixel fusion between the warped previous output and the current prediction to enhance coherence without enlarging the temporal window. This design reduces flicker, sharpens details, and remains efficient. Experiments on synthetic and real turbulence datasets show consistent improvements in PSNR/SSIM and perceptual quality (LPIPS), along with substantially faster inference than multi-frame transformer baselines, making ReMATF suitable turbulence mitigation in resource-constrained scenarios.

---


### 337. [Approximation Theory for Neural Networks: Old and New](https://arxiv.org/abs/2605.21451)

**<font color=#1a73e8>作者：</font>** Soumendu Sundar Mukherjee, Himasish Talukdar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Universal approximation theorems provide a mathematical explanation for the expressive power of neural networks. They assert that, under mild conditions on the activation function, feedforward neural networks are dense in broad function classes, such as continuous functions on compact subsets of $\mathbb{R}^d$, $L^p$ spaces, or Sobolev spaces. Over the past four decades, these qualitative universality results have evolved into a rich quantitative theory addressing approximation rates, parameter efficiency, and the role of architectural features such as depth and width. This survey presents several glimpses into this theory. We review classical density results for single-hidden-layer networks, as well as quantitative bounds that relate approximation error to network size and smoothness assumptions on target functions. Particular emphasis is placed on depth--width trade-offs and on results demonstrating that deeper architectures can achieve superior parameter efficiency for structured function classes. In addition to standard feedforward neural networks, we also review recent developments on Kolmogorov--Arnold Networks (KANs), which offer an alternative architectural paradigm and whose approximation-theoretic properties have begun to attract significant theoretical attention.

---


### 338. [Mitigating Label Bias with Interpretable Rubric Embeddings](https://arxiv.org/abs/2605.21455)

**<font color=#1a73e8>作者：</font>** Calvin Isley, Johann D. Gaebler, Sharad Goel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Statistical decision algorithms are increasingly deployed in domains where ground-truth labels are hard to obtain, such as hiring, university admissions, and content moderation. In these settings, models are typically trained on historical human evaluations -- for example, using past hiring decisions as a proxy for true applicant quality. However, if past evaluations unjustly favor certain groups, models trained on these labels may inherit those biases. To address this problem, we propose basing predictions on rubric embeddings, a representation framework that replaces standard black-box embeddings with features derived from expert-defined criteria that align with the underlying construct of interest. By anchoring predictions to semantically meaningful dimensions, this approach guards against biased proxy signals. We provide both theoretical and empirical evidence that rubric embeddings mitigate label bias under plausible conditions. Empirically, we evaluate our method on a novel dataset of applications to a large master's program. We find that models trained on rubric embeddings reduce group disparities while improving measures of cohort quality. Our results suggest that basing predictions on interpretable, domain-grounded representations offers a practical approach to learning in the presence of biased labels.

---


### 339. [Mind the Sim-to-Real Gap & Think Like a Scientist](https://arxiv.org/abs/2605.21458)

**<font color=#1a73e8>作者：</font>** Harsh Parikh, Gabriel Levin-Konigsberg, Dominique Perrault-Joncas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Suppose a planner has a pre-trained simulator of a sequential decision problem and the option to run real experiments in the field. The simulator is cheap to query but inherits confounding and drift from its calibration data. Experimentation is unbiased but consumes one real unit per trial. We study when, and how, the planner should supplement the simulator with experiments. We give three results. First, an extended simulation lemma decomposes the simulator's value error into a calibration--deployment shift that randomization can identify and a parametric residual that no further interaction can reduce. Second, the value gap between the simulator-optimal policy and the optimum splits into a local component, on states the deployed policy already visits, and a reachability component, on states it does not. The reachability component stays bounded away from zero at any horizon under purely passive learning. Third, we propose Fisher-SEP, a simulation-aided experimental policy (SEP) that minimizes the posterior predictive variance of a target policy's value, with reward-only and transition-only specializations. Two case studies illustrate the regimes. In a vending-machine supply chain, front-loaded experimentation overtakes posterior updating once the horizon is long enough to amortize the pilot. In an HIV mobile-testing example with a corridor that separates a well-surveilled region from a poorly-surveilled one, only designed exploration reaches the poorly-surveilled region.

---


### 340. [A Machine Learning Framework for Weighted Least Squares GNSS Positioning based on Activation Functions](https://arxiv.org/abs/2605.21461)

**<font color=#1a73e8>作者：</font>** Pin-Hsun Lee, Harry Leib  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global Navigation Satellite Systems (GNSS) are widely used to provide position, velocity, and timing (PVT) information for various applications, including transportation, location-based communication services, and intelligent agriculture. In urban canyons, high-rise buildings and narrow streets can cause signal obstruction, non-line-of-sight (NLOS) reception, and multipath effects that introduce errors in GNSS pseudorange measurements. Although multi-constellations GNSS effectively increase the number of available satellites, the inclusion of degraded signals can lead to severe positioning errors. This study proposes a machine learning framework for the weighted least squares (WLS) algorithm incorporating activation functions to enhance positioning accuracy. Several signal quality indicators are employed as training features for ensemble learning algorithms to identify poor quality signals by providing quality scores. Then, activation functions are employed to transform the machine learning predicted scores to appropriate weights for WLS positioning. To evaluate the performance of our approach, experiments are conducted using real-world datasets from Hong Kong and Tokyo urban areas. Comparative analysis of activation functions reveals that sigmoid functions consistently yield the greatest improvements with different machine learning algorithms and GNSS constellation configurations. The proposed algorithm demonstrates substantial reductions in positioning errors for both single- and multiconstellation scenarios. Furthermore, our results indicate that the proposed algorithm exhibits strong geographical transferability. The proposed algorithm maintains comparable level of performance when trained on data from other regions with similar levels of urbanization.

---


### 341. [StreamGVE: Training-Free Video Editing via Few-Step Streaming Video Generation](https://arxiv.org/abs/2605.21466)

**<font color=#1a73e8>作者：</font>** Guanlong Jiao, Chenyangguang Zhang, Jia Jun Cheng Xian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although existing video editing methods are generally feasible, they often require many costly iterations and still struggle to deliver high-quality yet satisfying editing results. We attribute this limitation to the prevalent data-to-data paradigm, which is less compatible with modern generative models than noise-to-data generation. To address this gap, we revisit video editing from a noise-to-data perspective and propose Streaming-Generation-based Video Editing (StreamGVE), which preserves few-step sampling while seamlessly injecting source-video conditions. Built on pre-trained streaming generation models, StreamGVE introduces dual-branch fast sampling with a self-attention bridge and cross-attention grounding/boosting to satisfy both sampling and conditioning requirements. We further propose source-oriented guidance to improve target-generation quality, and a visual prompting strategy to enhance editing flexibility and practicality. The method is effective, robust, and generalizable across different models. Extensive experiments on diverse video editing tasks show that StreamGVE consistently outperforms existing approaches, even in few-step settings with minimal time cost.

---


### 342. [Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling](https://arxiv.org/abs/2605.21470)

**<font color=#1a73e8>作者：</font>** Caleb Winston, Ron Yifeng Wang, Azalia Mirhoseini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUA) automate tasks specified with natural language such as "order the cheapest item from Taco Bell" by generating sequences of calls to tools such as click, type, and scroll on a browser. Current implementations follow a sequential fetch-screenshot-execute loop where each iteration requires an LLM call, resulting in high latency and frequent errors from incorrect tool use. We present agent just-in-time (JIT) compilation, an alternative that compiles task descriptions directly into executable code that is free to include LLM calls, tool calls, and parallelization. Our approach comprises three components: (1) JIT-Planner, which generates multiple code plans, validates each against tool specifications, and selects the minimum-cost candidate; (2) JIT-Scheduler, which explores parallelization strategies via Monte Carlo cost estimation from learned latency distributions; and (3) an invariant-enforcing tool protocol specifying precondition and postcondition state requirements that reduce the rate of generating plans with incorrect tool use. Across 5 web applications, JIT-Planner achieves $10.4\times$ speedup and $+28\%$ accuracy over Browser-Use, while JIT-Scheduler achieves $2.4\times$ speedup and $+9\%$ accuracy over OpenAI CUA.

---


### 343. [Stream3D: Sequential Multi-View 3D Generation via Evidential Memory](https://arxiv.org/abs/2605.21472)

**<font color=#1a73e8>作者：</font>** Kaichen Zhou, Zeyang Bai, Xinhai Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> View-conditioned 3D generators such as SAM 3D, TRELLIS and Hunyuan3D produce high-quality object reconstructions from a single view, but real-world visual observation often arrives as long monocular streams. Naively applying these generators to each streaming frame independently leads to severe temporal inconsistency in the generated results. To address this problem, we propose Stream3D, the first training-free streaming mechanism that turns a frozen view-conditioned 3D generator into a streaming generator with constant cross-chunk memory. Stream3D achieves this by maintaining a compact evidential memory, which selectively caches the most informative historical frames based on a proposed evidence score mechanism. As the stream progresses, the memory dynamically updates to retain a fixed number of informative frames, preventing the memory footprint from growing linearly with sequence length. This also prevents degradation over long sequences and keeps the underlying generator completely unchanged without retraining, architectural modifications, or auxiliary losses. Evaluated on both realistic and synthetic streaming benchmarks, Stream3D outperforms latent-transport baselines, including KV-cache reuse and flow-based feature editing, across both photometric and geometric metrics. More details can be found at: this https URL.

---


### 344. [Is Fixing Schema Graphs Necessary? Full-Resolution Graph Structure Learning for Relational Deep Learning](https://arxiv.org/abs/2605.21475)

**<font color=#1a73e8>作者：</font>** Yi Huang, Qingyun Sun, Jia Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational prediction tasks are fundamental in many real-world applications, where data are naturally stored in relational databases (RDBs). Relational Deep Learning (RDL) addresses this problem by modeling RDBs as graphs and applying graph neural networks (GNNs) for end-to-end learning. However, the full-resolution property is commonly adopted as a design principle in graph construction for RDBs to preserve relational semantics, which leads most existing methods to rely on fixed graph structures. In this paper, we propose FROG, a Full-Resolution and Optimizable Graph Structure Learning} framework for RDL that formulates relational structure learning as a learnable table role modeling problem, allowing tables to contribute as nodes and edges in message passing. We further design role-driven message passing mechanisms to capture relational semantics, enabling joint optimization of graph structure and GNN representations. To ensure semantic consistency, we introduce functional dependency constraints that regularize representations across table and entity levels. Extensive experiments demonstrate that our method outperforms existing approaches and reveal how table roles impact downstream tasks, offering new insights into graph construction for RDL

---


### 345. [Latent Dynamics for Full Body Avatar Animation](https://arxiv.org/abs/2605.21478)

**<font color=#1a73e8>作者：</font>** Shichong Peng, Chengxiang Yin, Fei Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose-driven full-body avatars built on neural rendering produce high-quality novel views of a captured subject. Yet loose clothing and other dynamic elements deform in ways pose alone cannot explain: the same pose can correspond to many different states, because their motion depends on history, inertia, and contact. Explicit simulation and layered-garment methods can model such dynamics, but they require either a dedicated garment template, which raw multi-view capture does not naturally provide, or a test-time physics simulator with non-trivial runtime cost. A parallel line of work learns data-driven clothing avatars that avoid explicit garment layers. These methods add an auxiliary latent for variation beyond pose; at inference, they fix it, regress it from pose, or retrieve it from training data, without explicitly modeling how the latent evolves with its own dynamics. Additionally, even in everyday motion with loose clothing, existing architectures often struggle to capture fine-grained detail, producing blurry renderings and temporal artifacts. We augment a pose-conditioned 3D Gaussian avatar with a transformer-based decoder and a dynamics residual latent that captures temporal appearance and geometry variation beyond the driving signals. At inference, a learned latent dynamics model evolves the residual latent from a short pose history and the previous latent state. The model decomposes each update into driving, restoring, and dissipative forces, producing temporally coherent, history-dependent rollouts with negligible added cost. Different initial conditions yield diverse yet plausible motion trajectories, and the force decomposition exposes controls such as stiffness. Across nine captured sequences of everyday motion with diverse loose garments, quantitative metrics and a perceptual user study show improved animation quality over recent data-driven baselines.

---


### 346. [AiraXiv: An AI-Driven Open-Access Platform for Human and AI Scientists](https://arxiv.org/abs/2605.21481)

**<font color=#1a73e8>作者：</font>** Junshu Pan, Panzhong Lu, Yixuan Weng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in artificial intelligence (AI) have accelerated the growth of both human-authored and AI-generated research outputs, placing increasing strain on traditional academic publishing systems and challenging the scalability of conference- and journal-centered paradigms amid rising submission volumes, reviewer workload, and venue size. To address these challenges, we explore an AI-era publishing paradigm in which both human and AI scientists participate as authors and readers, and papers evolve through continuous, feedback-driven iteration. We propose AiraXiv, an AI-driven open-access platform built on open preprints, AI-augmented analysis and review, and reader feedback. AiraXiv supports human scientists through an interactive UI and AI scientists through Model Context Protocol (MCP)-based interactions. We validate AiraXiv through real-world deployments, including serving as the submission platform for ICAIS 2025, demonstrating its potential as a fast, inclusive, and scalable research infrastructure for the AI era. AiraXiv is publicly available at this https URL.

---


### 347. [DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation](https://arxiv.org/abs/2605.21482)

**<font color=#1a73e8>作者：</font>** Sixiong Xie, Zhuofan Shi, Haiyang Shen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research, in which an agent searches the open web, collects evidence, and derives an answer through extended reasoning, is a prominent use case for frontier language models. Frontier deep research products score high on existing benchmarks, making it difficult to distinguish their capabilities from current evaluation data alone. We introduce DeepWeb-Bench, a deep research benchmark that is substantially harder than existing benchmarks for the current frontier. Difficulty comes from three properties of the data itself: each task requires massive evidence collection, cross-source reconciliation, and long-horizon multi-step derivation. We represent these three sources of difficulty as four capability families (Retrieval, Derivation, Reasoning, and Calibration) and report results sliced by family. Every reference answer is accompanied by a source-provenance record with four disclosure levels and cross-source checks where available, making scores easier to audit against the underlying evidence. We evaluate DeepWeb-Bench on nine frontier models and report three findings: (1) retrieval is not the bottleneck, as retrieval failures account for only 12-14% of errors while derivation and calibration failures account for over 70%; (2) strong and weak models fail in qualitatively different ways, with strong models' errors dominated by incomplete derivation and weak models' by hallucinated precision; and (3) models exhibit genuine specialization across domains, with cross-model agreement of only rho = 0.61 and per-case disagreement reaching 18.8 percentage points. The public benchmark release includes the data, rubrics, and evaluation code.

---


### 348. [One-Step Distillation of Discrete Diffusion Image Generators via Fixed-Point Iteration](https://arxiv.org/abs/2605.21484)

**<font color=#1a73e8>作者：</font>** Chaoyang Wang, Yunhai Tong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models excel at visual synthesis but rely on slow, iterative decoding. Existing single-step distillation methods attempt to bypass this bottleneck, either by training auxiliary score networks that effectively double compute, or by introducing specialized parameterizations and multi-stage pipelines that fragment optimization. In this paper, we introduce Fixed-Point Distillation (FPD), an end-to-end framework that constructs local correction targets by partially corrupting the student's one-step draft and refining it with a single teacher step. To compute the training objective in a semantically meaningful space, we lift discrete tokens into continuous features and apply a multi-bandwidth drift loss that iteratively accumulates these corrections. To backpropagate through the discrete bottleneck, we employ a straight-through estimator that feeds exact hard-sampled tokens to the teacher and decoder during the forward pass, ensuring that training and inference operate on the same codebook manifold, while routing continuous gradients back to the student logits. This fully differentiable pathway additionally accommodates an optional unconditional adversarial objective to enhance perceptual realism. Evaluations on both class- and text-conditional generation validate the effectiveness of our framework. FPD achieves competitive visual fidelity and structural alignment within a single inference step, narrowing the gap to multi-step teachers while outperforming existing discrete distillation baselines.

---


### 349. [Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate](https://arxiv.org/abs/2605.21486)

**<font color=#1a73e8>作者：</font>** Dayal Singh Kalra, Maissam Barkeshli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperparameter transfer allows extrapolating optimal optimization hyperparameters from small to large scales, making it critical for training large language models (LLMs). This is done either by fitting a scaling law to the hyperparameters or by a judicious choice of parameterization, such as Maximal Update ($\mu$P), that renders optimal hyperparameters approximately scale invariant. In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization. Next, we investigate through a comprehensive series of ablations why $\mu$P appears to offer high-quality learning rate transfer relative to standard parameterization (SP), as existing theory is inadequate. We find that the overwhelming benefit of $\mu$P relative to SP when training with AdamW arises simply from maximizing the learning rate of the embedding layer. In SP, the embedding layer learning rate acts as a bottleneck that induces training instabilities; increasing it by a factor of width to match $\mu$P dramatically smooths out training while improving hyperparameter transfer. We also find that weight decay improves the scaling law fits, while, in the fixed token-per-parameter setting, it hurts the robustness of the extrapolation.

---


### 350. [Uni-Edit: Intelligent Editing Is A General Task For Unified Model Tuning](https://arxiv.org/abs/2605.21487)

**<font color=#1a73e8>作者：</font>** Dian Zheng, Manyuan Zhang, Hongyu Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Currently, enhancing Unified Multimodal Models (UMMs) with image understanding, generation, and editing capabilities mainly relies on mixed multi-task training. Due to inherent task conflicts, such strategy requires complex multi-stage pipelines, massive data mixing, and balancing tricks, merely resulting in a performance trade-off rather than true mutual reinforcement. To break this paradigm, we propose Uni-Edit, an intelligent image editing task that serves as the first general task for UMM tuning. Unlike complex mixed pipelines, Uni-Edit improves performance across all three abilities at once using only one task, one training stage, and one dataset. Specifically, we first identify image editing as an inherently ideal general task, as it naturally demands both visual understanding and generation. However, existing editing data relies on simplistic instructions that severely underutilize a model's understanding capacity. To address this, we introduce the first automated and scalable data synthesis pipeline for intelligent editing, transforming diverse VQA data into complex and effective editing instructions with embedded questions and nested logic. This yields Uni-Edit-148k, pairing diverse reasoning-intensive instructions with high-quality edited images. Extensive experiments on BAGEL and Janus-Pro demonstrate that tuning solely on Uni-Edit achieves comprehensive enhancements across all three capabilities without any auxiliary operations.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-352](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
