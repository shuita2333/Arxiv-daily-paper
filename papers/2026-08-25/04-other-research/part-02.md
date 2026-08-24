# 📦 其他研究 | 2026年08月25日

> 本类共 **158** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-158](./part-04.md)

---

### 51. [RiskTraf: Risk-Extrapolated Residual Learning for Multi-Variate Traffic Flow Prediction](https://arxiv.org/abs/2608.20656)

**<font color=#1a73e8>作者：</font>** Guangyu Wang, Zhidan Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic sensors commonly record flow, speed, and occupancy, but standard traffic flow forecasting benchmarks and models rarely exploit all three raw measurements reliably. Although speed and occupancy provide sensor-native traffic-state information beyond flow alone, existing releases often omit these variables, replace them with proxies, or contain logically inconsistent records. Moreover, direct empirical risk minimization over three-variable inputs may exploit regime-dependent shortcuts, as the relationships among flow, speed, and occupancy vary substantially between free-flow and congested states. We introduce \textbf{PEMSB-3V}, a public benchmark suite that preserves raw flow, speed, and occupancy measurements from PeMS detectors for flow prediction. We also propose \textbf{RiskTraf}, a model-agnostic risk-extrapolated residual plug-in. For each trained spatio-temporal backbone, RiskTraf freezes the selected checkpoint and learns a lightweight zero-start residual head from historical speed and occupancy. The residual head constructs ordered traffic-risk environments and optimizes horizon-wise flow corrections with a risk extrapolation objective, thereby mitigating regime-specific shortcut correlations without modifying the backbone. Extensive experiments demonstrate that RiskTraf consistently improves diverse forecasting backbones and outperforms debiasing and distribution-shift adaptation methods. Our code and benchmark are available at this https URL.

---


### 52. [Shortcut Learning in a Public Grape Disease Dataset: Annotation Granularity as a Modulator, Not a Cause](https://arxiv.org/abs/2608.20663)

**<font color=#1a73e8>作者：</font>** Pushuo Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Public datasets for agricultural disease detection are usually judged fit for use from reported metrics, which say nothing about whether the annotation scheme is internally consistent. On one public grape disease dataset (3288 images, 11995 boxes, 6 classes), varying model capacity, input resolution and detection paradigm yields a test-set mAP50 range comparable to seed-to-seed noise, with the bottleneck at small objects across all five architectures. The finding lies on the data side: one class is annotated at whole-leaf level (median box area 43.16% of the image) while the other five are annotated at lesion level. On 5156 cross-species images containing no grape, 65.7% of the false-positive boxes fall into that one class, an over-representation of 13.41x relative to its share of the training annotations. Counterfactual retraining establishes a causal effect of granularity on the magnitude of the shortcut: shrinking only that class's boxes cuts its cross-species false positives by 66%, and a placebo control confirms the effect is specific to the manipulated class. A manipulation in the opposite direction, with criteria registered in advance, returns a negative result: coarsening the finest class to whole-leaf level (0.57% to 40.37%), matched in box count and share of annotations and with higher in-distribution AP, still leaves its cross-species false positives at zero boxes, while the unmanipulated original class holds 50.0% of them. Annotation granularity is therefore a modulator of this shortcut, not its cause: it can amplify or attenuate a sink that already exists, but cannot create one, and what fixes the destination remains open. We also give a granularity screening statistic requiring neither images nor training, and show airborne lesion-level detection to be optically out of reach. The failure mode is invisible to in-distribution evaluation.

---


### 53. [C-Score: Beyond Accuracy for Robustness Assessment in Semi-Supervised Learning under Open-World Unlabeled Contamination](https://arxiv.org/abs/2608.20667)

**<font color=#1a73e8>作者：</font>** Tsao-Lun Chen, Chi-Cheng Fu, Han-Yi E. Chou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pseudo-label-based semi-supervised learning has achieved strong performance due to its simplicity and scalability. However, it is typically developed under a closed-world assumption that unlabeled data are drawn from the same distribution as labeled data. In practical deployment, unlabeled data are often collected from open environments and may contain OOD samples. Under such contamination, OOD samples may still receive high-confidence predictions and be incorporated into training as if they were valid target examples. This creates an important evaluation problem: clean in-distribution test accuracy may appear stable even when the internal learning dynamics of SSL have already deteriorated. To address this issue, we study hidden collapse in pseudo-label-based SSL under open-world unlabeled contamination from a diagnostic evaluation perspective. We present C-Score, a compact framework that evaluates training behavior in three complementary spaces: prediction, feature representation, and optimization. C-Score includes PLE and CCI for unlabeled prediction behavior, Sem-Drift for deviation from labeled semantic anchors, and Grad-Align for the compatibility between labeled and unlabeled optimization. Experiments on CIFAR-10 and CIFAR-100 with multiple OOD sources, varying contamination ratios, and four pseudo-label-based SSL algorithms show that C-Score metrics reveal hidden degradation that clean accuracy alone fails to detect: under SVHN contamination, CCI rises over 280% while best-accuracy remains within 3% of the uncontaminated baseline; near-OOD sources (CIFAR-100, STL-10) cause up to 14.9% accuracy collapse (FlexMatch, r=0.5). The results suggest that clean accuracy alone is insufficient for evaluating SSL robustness in open-world environments, and that internal diagnostic signals are necessary for more reliable robustness assessment under unlabeled contamination.

---


### 54. [Lightweight Adaptive ReduNet via Hyperspherical Manifold Learning](https://arxiv.org/abs/2608.20668)

**<font color=#1a73e8>作者：</font>** Zhenglin Huang, Qifa Yan, Bin Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, a white-box neural network called ReduNet has been proposed, which employs the maximal coding rate reduction (MCR$^2$) principle to transform raw data into low-dimensional discriminative features via a forward layer-wise construction process. Unlike traditional deep networks that rely on backpropagation, ReduNet explicitly derives the parameters of each layer from the features of its preceding layer, offering a mathematically interpretable paradigm. However, this layer-wise construction often requires a large number of layers for the MCR$^2$ objective to reach a stable value, which increases the parameter storage of the unfolded module. To address this issue, we propose LA-ReduNet, a lightweight adaptive architecture that refines the layer-wise update rule and enables discriminative feature representations to be obtained with substantially fewer unfolded layers. Specifically, LA-ReduNet employs hyperspherical manifold learning and adaptive step sizes, thereby reducing by an order of magnitude the number of layers required for the MCR$^2$ objective to reach a stable value. Simulation results demonstrate that, while maintaining comparable classification accuracy, LA-ReduNet requires significantly fewer layers for the MCR$^2$ objective to reach a stable value. Remarkably, under the considered experimental settings, LA-ReduNet requires only approximately $1/29$ of the parameter storage of the unfolded ReduNet module for the MCR$^2$ objective to reach a stable value.

---


### 55. [Bootstrapping Mutual Attestation with Kleene's Second Recursion Theorem](https://arxiv.org/abs/2608.20671)

**<font color=#1a73e8>作者：</font>** Takuma Imamura  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mutual attestation among nodes with no central trusted operator requires each node to hold reference values (expected code measurements) for its peers. The naïve approach of mutually embedding these reference values in the nodes' code leads to an infinite regress. We call the problem of resolving this infinite regress the reference-value bootstrapping problem for mutual attestation. Existing solutions avoid this regress by relying on a trusted third party (TTP), externally supplied reference values, or architecture-specific measurement mechanisms. We instead express the bootstrapping problem as a system of mutual fixed-point equations and solve it by Kleene's second recursion theorem. The construction produces nodes that mutually reference one another's code and reconstruct every peer's exact source from built-in data alone. When a deployed source file is measured directly, as with a Python script, a node obtains the peer's reference value by applying the measurement function directly to the reconstructed source. When a built image is measured, as with AWS Nitro Enclaves, a node instead reproducibly rebuilds the peer's image from the reconstructed source and derives its reference measurement. For the first case, we develop PyReflect, a Python transpiler, and use it to implement a TPM mutual-attestation PoC. For the second, we develop NixReflect, a Nix transpiler, and use it in a PoC in which two Nitro Enclaves reproduce each other's reference PCRs from built-in data alone. Our solution is architecture-independent, requires neither a TTP nor externally supplied reference values, and works with existing attestation stacks unchanged.

---


### 56. [The Rising Cost of Trust: Practitioners' Trust Signals, Controls, and Responses in the Software Supply Chain](https://arxiv.org/abs/2608.20675)

**<font color=#1a73e8>作者：</font>** Ranindya Paramitha, Siri Paidipalli, Laurie Williams 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The software supply chain is becoming more complex, and AI is reshaping its threat landscape, e.g., raising concerns about the quality of AI-generated dependencies. Seen through the lens of trust, the stakes of eroding trust in the software supply chain are high, yet we lack an empirical baseline on practitioners' trust. The goal of this study is to aid software practitioners in taking informed actions as trust in the software supply chain evolves, through an interview study with 38 practitioners. We conducted semi-structured interviews with industry and open-source practitioners, focusing on their revealed preferences (the controls they adopted) rather than their stated attitudes, and analyzed the data using thematic analysis grounded in established trust concepts from the social sciences. We find that trust is eroding, which is becoming costly: aware practitioners are accumulating controls. To cope with the rising cost of trust, practitioners automate verification, delegate trust decisions to guardians, or consider exiting the software supply chain entirely. Understanding software supply chain dynamics through the lens of trust provides the vocabulary and concepts (e.g., guardians of trust, system trust, signals) to shape future interventions for a well-functioning supply chain with appropriate levels of trust.

---


### 57. [The Software Supply Chain as a Market for Lemons: A Multivocal Review of Trust Signal Collapse](https://arxiv.org/abs/2608.20678)

**<font color=#1a73e8>作者：</font>** Ranindya Paramitha, Christian Kästner, Laurie Williams  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Practitioners evaluating open-source dependencies rely on cheap trust signals, e.g., stars, download counts, and contributor activity, as substitutes for direct code inspection, assuming those signals reflect genuine trustworthiness. Prior work has documented individual signal gaming, but the landscape of collapses across all dependency-adoption signals, as well as the ecosystem's response, remains unexplored. The goal of this study is to aid software practitioners in understanding the reliability of dependency adoption trust signals, such as download counts and contributor activity, by conducting a multivocal review of 252 Google Search sources and 870 Reddit threads. After coding the corpora, we find that cheap trust signals collapse under three simultaneous forces: adversarial manipulation, gaming techniques indistinguishable from legitimate behavior, and non-adversarial AI-driven inflation. The documented responses are more advice than actual action: 54.6% of Google Search sources contain advice on what practitioners should do, with no actual action taken. Responses proposed substituting one cheap signal for another or aggregating multiple signals, which are now also gameable. Non-adversarial inflation, i.e., degradation caused by the emergence of legitimate AI tooling, lacks documented actual behavior change in either corpus. The gap between known remedy and actual practice points toward a market for lemons: when faking signals costs less than earning them, good and bad dependencies become indistinguishable. Relying on individual practitioners to verify the cheap signals is not sustainable. Costlier signals, such as cryptographic attestation, should be made mandatory so that they become the default for all, not a voluntary choice for the few.

---


### 58. [Reinforcement Learning for Continuous-Time Jump Markov Decision Processes with Applications to Network Dynamic Pricing](https://arxiv.org/abs/2608.20680)

**<font color=#1a73e8>作者：</font>** Huiling Meng, Ningyuan Chen, Xuefeng Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study reinforcement learning (RL) in Continuous-Time Jump Markov Decision Processes (CTJMDPs) featuring general discrete state spaces (which need not possess a vector space structure) and continuous/discrete action spaces. The setup covers many well-known applications in operations such as multi-product dynamic pricing with capacitated resources (Gallego and van Ryzin 1997). To model the exploration-exploitation tradeoff, we formulate an entropy-regularized continuous-time control problem with stochastic policies. Recent continuous-time RL techniques such as $q$-learning for controlled diffusions in (Jia and Zhou 2023) focus on continuous state spaces $\mathbb{R}^d$ and rely heavily on semimartingale theory in $\mathbb{R}^d$ for their theoretical analysis. Consequently, their methods cannot be directly applied to CTJMDPs with general discrete state spaces, which may lack the algebraic addition and subtraction structures inherent to Euclidean spaces. To bridge this gap, we establish the theoretical foundations of $q$-learning for CTJMDPs and develop model-free $q$-learning algorithms. Compared to naïve time discretization and approximating CTJMDPs using discrete-time MDPs, our approach has several conceptual and empirical benefits. Numerical experiments in network dynamic pricing (Gallego and van Ryzin 1997) show that our proposed RL algorithm reliably learns near-optimal policies and consistently outperforms standard benchmark methods, demonstrating superior solution quality and effective scalability to large-scale network instances.

---


### 59. [Aristotelian Manifolds: Leveraging Platonic Perceptual Features for Backpropagation Free Rapid Concept Learning](https://arxiv.org/abs/2608.20682)

**<font color=#1a73e8>作者：</font>** Michael Karnes, Alper Yilmaz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper formalizes and systematically characterizes Aristotelian Manifolds, a generalized structural framework built upon the Platonic Representation Hypothesis. We position high-capacity foundation models as universal perceptual filters and conduct a comprehensive layer-wise investigation to map how knowledge is functionally synthesized within these latent subspaces. Across diverse architectural paradigms and multi-domain datasets, we rigorously chart the interplay between network depth, dimensionality reduction, and distance metrics. Our characterization reveals that semantic maturation does not follow a singular, monotonic path; instead, different data domains exhibit highly distinct geometric response profiles, characterized by intermediate mound-like peaks for specialized clinical modalities and sigmoidal plateaus for natural visual tasks. By profiling the exact coordinates where these manifolds achieve peak representational efficiency, we establish a predictable taxonomy for layer selection and feature compression. Ultimately, this systematic characterization demonstrates that mapping the internal geometry of frozen representations provides a robust, backpropagation-free, and interpretable framework for understanding and exploiting foundation model latent spaces.

---


### 60. [CDRL: Certification-Driven Reinforcement Learning for Neutrino Flavor Model Discovery](https://arxiv.org/abs/2608.20686)

**<font color=#1a73e8>作者：</font>** Piyush Jha, Jake Rudolph, Victoria Knapp-Pérez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many scientific discovery problems require searching combinatorial hypothesis spaces under complex domain constraints. Reinforcement learning (RL) offers a promising approach, but existing methods rely on scalar rewards that provide limited information about why candidate solutions fail, leading agents to repeatedly explore invalid regions. We introduce Certification-Driven Reinforcement Learning (CDRL), a framework that leverages structured feedback from symbolic reasoning tools. When a candidate violates domain constraints, these tools produce certificates identifying the actions responsible for failure. CDRL converts these certificates into reusable constraints that eliminate classes of invalid solutions and guide exploration toward valid regions. We evaluate CDRL on neutrino flavor model discovery in theoretical particle physics, where the hypothesis space exceeds $10^{26}$ possible models, and compare it with the state-of-the-art RL approach previously used for this task. Across three theory spaces, CDRL achieves up to 1.95$\times$ higher valid model rates and up to 6.33$\times$ higher neutrino model rates while evaluating up to 4$\times$ fewer candidates. We further extract 40 interpretable rules from search trajectories using a post-hoc decision-tree framework and show that reusing them as soft constraints yields gains of up to 2$\times$ in valid model rates and 3$\times$ in neutrino model discovery across all three theory spaces. These results suggest that CDRL uncovers reusable structure in combinatorial search spaces and provides a general framework for scientific model discovery.

---


### 61. [TopoSurfel: Closing the Loop between Gaussian Surfels and Meshes for Surface Reconstruction](https://arxiv.org/abs/2608.20687)

**<font color=#1a73e8>作者：</font>** Chuanjin Fan, Wenjie Chang, Bohao Liao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting has achieved remarkable success in novel view synthesis. However, extracting high-fidelity surfaces directly from 3DGS remains challenging due to its discrete and unstructured nature. Existing 3DGS-based reconstruction methods typically rely on multi-view geometric consistency or local constraints. Without an explicit structured geometric prior during optimization, these methods often struggle to resolve structural ambiguities, leading to artifacts and floaters, particularly in textureless or occluded regions. To address this limitation, we propose TopoSurfel, a novel framework that closes the loop between Gaussian surfels and continuous meshes. Unlike recent methods that incorporate mesh extraction into the differentiable pipeline by introducing auxiliary neural networks or extra per-Gaussian parameters, we dynamically extract a continuous proxy mesh via a non-trainable differentiable iso-surfacing process. Leveraging this differentiable connection, we introduce a mesh-guided surfel evolution strategy, including normal alignment and geometry-aware density control, to effectively suppress floaters and fill surface holes. Furthermore, to address the initialization challenges in large-scale environments, we propose a spatially aware hybrid re-initialization strategy that ensures robust reconstruction across complex scenes. Extensive experiments demonstrate that TopoSurfel achieves competitive geometric reconstruction accuracy while maintaining high-quality mesh-based novel view synthesis. The code for our method is available at this https URL.

---


### 62. [Identity-Aware Human-Object Interaction Motion Captioning](https://arxiv.org/abs/2608.20690)

**<font color=#1a73e8>作者：</font>** Yiming Wang, Yonghao Dang, Huilai Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing human-object interaction (HOI) motion captioning methods typically describe what happens while referring to the subject using generic terms such as "a person" or "someone", without grounding the caption in subject identity. To address this limitation, we introduce Identity-Aware Human-Object Interaction Motion Captioning task. This task requires each generated caption to specify both the subject identity and the corresponding HOI motion. For example, the model generates "Sub_ID lifts the chair" rather than "A person lifts the chair". For this task, we design identity-aware HOI motion captions based on the BEHAVE and InterCap datasets. We further propose ID-HOINet, which learns from multi-view videos while supporting single-view identity-aware HOI motion caption generation. ID-HOINet contains two core components: Multi-View Identity-Motion Learning Module (MVIML) and Two-Stage Caption Rewriting Strategy (TSCR). MVIML learns from multi-view videos by modeling dependencies across temporal stages and camera viewpoints, capturing identity and interaction motion features. At inference, the TSCR first retrieves the subject identity and generates identity-agnostic HOI motion captions. TSCR then rewrites these captions with the predicted identity to produce the final identity-aware HOI motion captions. Experiments demonstrate that ID-HOINet achieves state-of-the-art performance. Code will be released upon acceptance.

---


### 63. [Bridging Language and Spherical Space: Object-Centric Control for Text-to-Panorama Generation](https://arxiv.org/abs/2608.20691)

**<font color=#1a73e8>作者：</font>** Derui Li, Qian Qiao, Yuhao Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic image generation is increasingly important for immersive applications such as virtual reality, augmented reality, and 3D content creation. Unlike perspective images, panoramic images represent a viewer-centered $360^\circ$ surrounding space, where directional expressions such as left, right, front, and behind play a central role in spatial understanding. However, existing text-to-panorama methods largely rely on implicit spatial reasoning and often fail to faithfully ground object-level directional descriptions in spherical panoramic scenes. A straightforward alternative is to introduce explicit layouts, but requiring manually specified spatial conditions reduces the flexibility of language-based interaction and does not directly resolve the misalignment between egocentric directional language and panoramic image space. To address this issue, we propose PanoCtrl, an object-centric framework for controllable text-to-panorama generation. Our method explicitly bridges natural language and spherical panoramic space by converting textual descriptions into structured object-level spherical conditions and integrating them into the diffusion process. Specifically, we introduce PanoParse, a text-conditioned parser that predicts object semantics and spherical bounding field-of-view (BFoV) parameters, and \textbf{PanoControl}, which injects object-level semantic and spatial guidance into the diffusion transformer through object-aware attention and spatial residual enhancement. To support this task, we construct PanoGround, a dataset with object-level spherical annotations and diverse directional descriptions for controllable panoramic generation. Extensive experiments demonstrate that PanoCtrl achieves state-of-the-art performance in both spatial alignment and image quality.

---


### 64. [Reflections on Working with Older Adults in Visualization Research](https://arxiv.org/abs/2608.20696)

**<font color=#1a73e8>作者：</font>** Zack While  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While older adults represent a growing proportion of the global population, their presence in visualization research remains limited. In this paper, I present reflections from a series of human-subject studies conducted with older adults as part of a multi-year research effort. These studies include a controlled laboratory experiment, online evaluations, and an in-situ investigation with participants above age 60. Based on these experiences, I provide methodological takeaways for conducting visualization research with older participants and propose directions for future work. This work ultimately aims to provide practical guidance and encourage broader inclusion of older adults as participants in visualization research.

---


### 65. [Enabling Threshold Custody for the Lightning Network with Nested Threshold Multi-Signatures](https://arxiv.org/abs/2608.20705)

**<font color=#1a73e8>作者：</font>** Paul Gerhart, Nadav Kohen, Jesse Posner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Bitcoin Lightning Network secures hundreds of millions of dollars, yet channel endpoints rely on vulnerable single online keys. Although threshold signatures are routinely used to protect on-chain Bitcoin, no practical deployment has been possible for Lightning channels. This is because thresholdizing a Lightning party requires nesting a threshold signature scheme inside of an established two-party MuSig2 protocol without altering its nonce exchange or message flow.
In this work, we resolve this limitation by formalizing nested threshold multi-signatures, a new cryptographic primitive for thresholdizing one participant inside a multi-signature protocol. As an instance of this primitive, we present Iceberg, the first construction for nested threshold MuSig2 signatures. Iceberg enables one side of a Lightning channel to operate as a $t$-of-$n$ threshold group while appearing to the counterparty as a standard MuSig2 participant. As a result, threshold custody can be deployed unilaterally on today's Lightning Network without requiring any modifications to Bitcoin, the Lightning protocol, or channel counterparties.
We prove the security of Iceberg, integrate a prototype into a production Lightning node, and benchmark its performance. Our measurements show that thresholdizing a Lightning channel incurs only modest overhead, since a threshold group tolerating one corrupted member sustains over $93\%$ of the payment throughput of an unmodified endpoint.

---


### 66. [Geometric Regularization for Long-Tailed Semi-Supervised Learning via Gaussian Feature Bridges](https://arxiv.org/abs/2608.20710)

**<font color=#1a73e8>作者：</font>** Hongyang He, Xinyuan Song, Yan Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world semi-supervised learning (SSL) often encounters significant challenges with long-tailed label distributions and noisy pseudo-labels, which hinder generalization and amplify confirmation bias. In this work, we introduce a novel framework, Gaussian Bridge Consistency (GBC), to address these challenges by constructing semantic interpolation paths between unlabeled samples and high-quality class anchors. Our method maintains a dynamic Prototype Atlas that stores a diverse and evolving set of labeled and pseudo-labeled exemplars per class. For each unlabeled instance, GBC forms a class-conditional Gaussian Feature Bridge in the latent space, enabling the student model to traverse a smooth trajectory from uncertain predictions to reliable class prototypes. A bridge consistency loss is applied along this path to enforce alignment with a geometrically interpolated target distribution. Furthermore, we propose BridgeMix, a confidence-aware feature mixing strategy that interpolates both sample and anchor pairs to amplify cross-sample generalization. Extensive experiments on CIFAR10-LT and ImageNet-LT (USB benchmarks) validate the robustness and effectiveness of GBC under realistic long-tailed SSL settings, consistently improving long tail-class performance without sacrificing scalability.

---


### 67. [Privacy-Preserving Object Detection for Vision Transformer-Based Models](https://arxiv.org/abs/2608.20712)

**<font color=#1a73e8>作者：</font>** Homare Sueyoshi, Kiyoshi Nishikawa, Hitoshi Kiya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose a novel object detection method that enables us to protect sensitive visual information of test images. Previous studies considering visual information protection focus on image classification tasks. This paper proposes an object detection method using perceptual encryption for the first time. The proposed method can achieve almost the same accuracy as that of models without any protection by utilizing the embedding structure of the Vision Transformer (ViT) and a domain adaptation technique with keys. In experiments, the effectiveness of the proposed method is verified in terms of accuracy and visual protection under the use of ViTdet, which is a ViT-based object detection model.

---


### 68. [Continuous-Time Quantum Walks based Graph Neural Network](https://arxiv.org/abs/2608.20738)

**<font color=#1a73e8>作者：</font>** Yuliang Zhan, Zefeng Gao, Jian Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) are widely used on graph-structured data, but most suffer from two key weaknesses. First, message passing behaves as a low-pass filter under the homophily assumption, leading to poor performance on heterophilic graphs. Second, stacking layers drives node features toward constants, causing over-smoothing. Existing methods usually address these issues separately, while the few joint solutions rely largely on empirical heuristics, and many over-smoothing remedies sacrifice model expressiveness.
We propose \textbf{CTQW-GNN}, a GNN based on Continuous-Time Quantum Walks (CTQW), to address both issues with theoretical justification. Its design exploits two properties of the CTQW propagator $e^{-\mathrm{i}Ht}$. First, it is unitary and has eigenvalues on the unit circle, so no frequency component is damped, counteracting the low-pass bias. Second, unitarity preserves feature norms and prevents the Dirichlet energy from decaying exponentially with depth, thereby mitigating over-smoothing.
CTQW-GNN combines three complementary aggregation modules. \textit{CTQW-based Aggregation} evolves node features through the unitary propagator, preserving mid- and high-frequency signals for heterophilic graphs while preventing Dirichlet-energy collapse. \textit{CTQW-Attention Aggregation} constructs a multi-hop neighbor graph from CTQW amplitudes and applies attention over it, enabling access to distant homophilic nodes missed by single-hop aggregation. \textit{LF Aggregation} uses a standard low-pass GAT branch to retain strong performance on homophilic graphs, where pure CTQW aggregation can be suboptimal. We further provide a spectral-gap analysis explaining energy preservation and a Lieb--Robinson-type bound that gives a principled rule for selecting the walk time $t$.

---


### 69. [VisTa3D: A Dataset and Benchmark for Thin Object Reconstruction from Vision, Tactile, and 3D Point Clouds](https://arxiv.org/abs/2608.20740)

**<font color=#1a73e8>作者：</font>** Shania Guo, Yeongsik Seo, Andrew Fu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art 3D reconstruction models, whether from visual, range, or both, tend to underperform on thin objects. This is partially due to the small amount of space such objects occupy in RGB images and in 3D point clouds. To test the extent of their errors, we collected the first thin object dataset comprising of synchronized RGB images, depth maps, and tactile response maps, where each frame is associated with inertial measurements, camera pose and calibration, and groundtruth depth and segmentation maps obtained from laser scanning of thin objects. We hypothesize that tactile data can aid in the reconstruction of thin objects as their response maps provide local shape and deformation information. Our dataset, termed VisTa3D, comprises of 387 scenes covering 70 thin objects over 17 environments. We benchmarked current 3D reconstruction models on VisTa3D and found that, indeed, they exhibit low fidelity on thin objects. To test if tactile data can help, we introduce the first visual-range-tactile 3D reconstruction model as a baseline. Code and data: this https URL.

---


### 70. [Generating Multi-view Adversarial Examples for Visual Geometry Grounded Transformer](https://arxiv.org/abs/2608.20748)

**<font color=#1a73e8>作者：</font>** Qi Song, Ziyuan Luo, Haoliang Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Visual Geometry Grounded Transformer (VGGT) enables unified feed-forward 3D reconstruction from multi-view images. However, deploying such a high-performance model may expose critical security vulnerabilities. Traditional adversarial perturbations require costly per-scene optimization, while Universal Adversarial Perturbations (UAPs) rely on a single static pattern and fail to effectively attack VGGT. To address these limitations, we propose \textbf{MVAP-G}, a multi-view adversarial perturbation generator that produces imperceptible consistent perturbations across multiple views in a single feed-forward pass. To ensure perturbation consistency across diverse scenes, we design a cross-view adversarial alignment mechanism to process multi-view images. Experiments demonstrate that MVAP-G significantly degrades VGGT performance without iterative optimization during inference. This work pioneers multi-view adversarial attacks on 3D foundation models, uncovering severe vulnerabilities and underscoring the urgent need for robust 3D vision systems. The code is available at this https URL.

---


### 71. [Adaptive Training for Nautical Rules of the Road](https://arxiv.org/abs/2608.20751)

**<font color=#1a73e8>作者：</font>** Amit Dutta, Sushil J. Louis  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Knowledge of the nautical rules of the road is essential for safe ship navigation and collision avoidance. We evaluated adaptive and non-adaptive versions of a ship-driving simulation trainer designed to assess and improve students' knowledge and application of these rules. We randomly assigned 30 university students to an adaptive or non-adaptive training condition and measured learning using pretest and post-test scores. Students who received adaptive training achieved significantly higher post-test scores than those who received non-adaptive training (p < 0.0001). After the post-test, all students experienced both versions of the trainer and compared them in a survey. Of the 30 students, 73% judged the adaptive trainer more effective, and 22 rated it "very engaging," compared with 9 who gave the non-adaptive trainer the same rating. These findings provide evidence that adapting scenario difficulty and providing immediate, context-sensitive feedback can improve both learning outcomes and student engagement in simulation-based training.

---


### 72. [SPARK-SAM: Self-Prompt Adaptation with Response Knowledge for SAM in Infrared Small Target Segmentation](https://arxiv.org/abs/2608.20754)

**<font color=#1a73e8>作者：</font>** Aji Mao, Zhenming Peng, Bailin Mu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Promptable segmentation models provide a reusable interface, but direct transfer to automatic infrared small-target segmentation (IRSTD) exposes a mismatch between spatial prompts and target-domain mask responses. In a diagnostic using target-covering loose-box prompts deterministically derived from test reference masks, the best official SAM2.1 results are only 4.69%, 1.64%, and 2.28% IoU on NUAA-SIRST, NUDT-SIRST, and IRSTD-1K. We introduce SPARK-SAM (Self-Prompt Adaptation with Response Knowledge for SAM), which learns target-domain response knowledge and conditions the decoder through an image-conditioned joint self-prompt state. Training combines benchmark-mask supervision with reliability-aware response guidance. SPARK-SAM achieves 75.78%, 86.49%, and 68.34% IoU with 0.726M additional parameters, ranking first on two benchmarks among 14 retrained SAM variants and adaptations evaluated as automatic image-to-mask methods. The staged IRSTD-1K diagnostic shows that response adaptation reaches most of the final IoU before the predicted points acquire reliable target grounding. Prompt supervision aligns the predicted prompt candidates with target locations, and frozen-weight interventions measure output sensitivity to the joint self-prompt state. Matched ablations show consistent accuracy gains from response guidance and high-resolution prompt refinement across all three datasets. Code is available at this https URL.

---


### 73. [PSK at WMT 2026 MIST: Task-Specialized QLoRA Adapters for Multilingual Summarization and Question Answering](https://arxiv.org/abs/2608.20757)

**<font color=#1a73e8>作者：</font>** Srikar Kashyap Pulipaka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the PSK submission to the WMT 2026 Multilingual Instruction Shared Task. Our system uses the 3.35B-parameter Tiny Aya Global model with three QLoRA adapters, one for each task. The adapters are trained on multilingual document-summary pairs, passage-based question answering, and filtered standalone question answering. The summarization data also includes scientific papers with their author-written abstracts. On our held-out split, the context and summarization adapters perform better than our multitask adapter, which was trained only on data supplied by the organizers. Results for open QA are mixed and vary with answer length and evaluation method. We therefore submit three systems with the same context and summarization adapters but different open-QA adapters.

---


### 74. [Hidden Axis of Uncertainty: Latent-Posterior Alignment in Graph Neural Networks with Bayesian Output Layers](https://arxiv.org/abs/2608.20758)

**<font color=#1a73e8>作者：</font>** Suk Hoon Choi, Damdae Park, Junhyuk Choi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian Neural Networks (BNNs) with Bayesian output layers provide a principled and tractable framework for quantifying predictive uncertainty, yet the mechanisms shaping that uncertainty remain unclear. While conventional theory attributes uncertainty reduction to posterior contraction, the corresponding assumptions need not hold for deep models. In the Graph Neural Networks (GNNs) with Bayesian output layers studied here, we observe that predictive uncertainty decreases as latent representations shift toward lower-variance posterior directions, even though the posterior variance does not contract. We term this behavior Latent-Posterior Alignment (LPA) and conduct interventional experiments that support its functional role in shaping predictive uncertainty. Building on this insight, we propose Alignment-Guided Learning (AGL), which explicitly promotes this alignment during training. AGL effectively reduces predictive uncertainty while preserving accuracy and improves structural calibration, ensuring that the model confidence faithfully mirrors underlying data density. These findings provide a new perspective on uncertainty dynamics in GNNs with mean-field Bayesian output layers, shifting the focus from the magnitude of the posterior to the geometric interplay between latent and parameter spaces.

---


### 75. [DiGS-Avatar: Single-Image Animatable 3D Human Reconstruction via UV-Space Diffusion](https://arxiv.org/abs/2608.20759)

**<font color=#1a73e8>作者：</font>** Jiakun Li, Li Fang, Hao Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image 3D human reconstruction often suffers from over-smoothed textures and geometric inconsistencies. While diffusion models improve generative quality, their reliance on multi-view synthesis prior to 3D reconstruction is computationally expensive and prone to view inconsistency. We propose DiGS-Avatar, which reformulates this task as an efficient, diffusion-based UV-latent completion task, ensuring 3D consistency by design. To capture accurate spatial structure, we introduce a teacher-student framework where a multi-view teacher provides geometrically aligned pseudo-ground-truth latents to supervise a single-view diffusion student. Treating this inferred latent as a robust structural skeleton, our method injects high-level semantic features to accurately recover fine textural details without disrupting spatial integrity. The refined representation is then decoded into 3D Gaussian primitives. Extensive experiments demonstrate that DiGS-Avatar achieves state-of-the-art or highly competitive visual fidelity and zero-shot generalization, while reconstructing a fully animatable 3D avatar in just 0.71 seconds. Code is available at this https URL.

---


### 76. [MotionPhys: Detecting AI-Generated Videos via Physical Consistency of Optical-Flow Trajectories](https://arxiv.org/abs/2608.20770)

**<font color=#1a73e8>作者：</font>** Haojin He, Hao Tan, Zichang Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern AI video generation models can produce videos with high visual fidelity and seemingly smooth temporal transitions. However, visual realism does not necessarily imply physical motion consistency. Existing generative models mainly optimize distribution matching in pixel or latent spaces, without explicitly enforcing real-world constraints such as inertia, continuous forces, and trajectory geometry. Our experiments show that AI-generated videos remain visually plausible over short sequences of consecutive frames, yet fail to preserve physical motion consistency throughout a complete object action, resulting in systematic statistical discrepancies in their motion trajectories. Based on this observation, we introduce MotionPhys, a lightweight and interpretable framework that treats sparse motion trajectories as physical evidence rather than relying on appearance artifacts or generator-specific traces. By modeling the geometric evolution of trajectories across multiple temporal scales, MotionPhys reveals subtle motion inconsistencies that are difficult to capture with conventional visual cues and transforms them into a compact representation for efficient detection. Experiments on multiple datasets show that MotionPhys can effectively detect physical inconsistencies in generated videos and generalizes well across different video generators.

---


### 77. [M2Depth: Unifying Monocular Depth Foundation Priors with Multi-View Stereo](https://arxiv.org/abs/2608.20788)

**<font color=#1a73e8>作者：</font>** Byeonggwon Lee, Sanggi Lee, Siwoo Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based Multi-View Stereo (MVS) has advanced significantly but often generalizes poorly to unseen scenes, particularly in occluded areas or regions with limited view overlap. To mitigate this, recent approaches integrate Depth Foundation Models (DFMs) into MVS pipelines to provide monocular depth priors. However, existing methods typically rely on a static, one-way fusion scheme, which fails to fully exploit the complementary strengths of both modalities. We propose a novel framework that overcomes this limitation by tightly coupling a DFM with a cascade MVS pipeline through a bidirectional mutual refinement strategy. Our method leverages MVS depth to resolve the scale ambiguity in monocular predictions, while the monocular depth, in turn, enhances the structural completeness and fine-grained detail of the MVS estimate. Furthermore, we introduce a prior-guided cost volume refinement mechanism that effectively integrates multi-view and monocular information via attention-based fusion and discretized depth bins, thereby promoting local geometric consistency. Extensive experiments demonstrate that our method outperforms state-of-the-art MVS approaches on standard benchmarks, producing more complete and generalizable depth maps with sharp boundaries. Furthermore, although not explicitly designed for sparse-view settings, our framework generalizes remarkably well, competing favorably with even dedicated sparse-view methods while maintaining a superior accuracy-efficiency trade-off.

---


### 78. [Beyond Explicit Generators: Distribution-Free Linear-Decomposition Attacks on Public-Key Encryption](https://arxiv.org/abs/2608.20798)

**<font color=#1a73e8>作者：</font>** Ziyan Chen, Ding-Xuan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Linear-decomposition attacks can break public-key schemes without recovering the secret algebraic action: when a target public state lies in a known linear span, its decomposition coefficients transfer through the unknown action to reveal the shared value. We study a setting in which the adversary uses only the public sampling-and-evaluation oracle available to honest participants, the induced distribution is arbitrary, and the goal is to attack future ciphertexts rather than recover the full algebraic span.
We model public paired samples under a fixed secret linear transport and define the sampled-orbit dimension as the effective dimension of the encryption distribution. We prove distribution-free one-shot recovery, a high-probability certificate for the future-ciphertext coverage of a sampled span, and the optimal sampled-span complexity $m^\star_{\mathrm{span}}(r,\varepsilon,\delta) =\Theta((r+\log(1/\delta))/\varepsilon)$. These results yield a generic impossibility theorem: publicly samplable linear key transport with polynomial sampled-orbit dimension is incompatible with IND--CPA security when the transported value determines the decryption payload.
We apply the framework to the 2024 probabilistic PKE from twisted--skew group rings. Its underlying Computational Twisted--Skew Problem admits a sampler-only linear attack using independently generated public protocol samples, yielding plaintext recovery and constant IND--CPA advantage. Experiments verify the linear transport and end-to-end recovery, and show that high future-ciphertext coverage may precede recovery of the full algebraic span.

---


### 79. [Dynamic Context Scheduling: Learning Beyond the Static Universe](https://arxiv.org/abs/2608.20799)

**<font color=#1a73e8>作者：</font>** Martin Mráz, André Biedenkapp  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study dynamic context scheduling as a training instrument for contextual re- inforcement learning. Rather than treating intra-episode context variation as a deployment reality, we treat it as a controlled shaping mechanism. Thereby, context evolves within each training episode according to a predetermined schedule, expos- ing the policy to a richer and more temporally structured region of the environment parameter space. We introduce DYNAMICCARLENV, a framework that wraps contextual environments with pluggable schedule families, such as sinusoidal off- sets or cosine annealing. Across CartPole, BipedalWalker and VehicleRacing with CARL contextualization, we show that dynamic schedules match or outperform static context baselines in the out-of-distribution (OOD) regimes. Interestingly, for the more complex BipedalWalker and VehicleRacing environments we also achieve higher in-distribution (ID) evaluation performance. Preliminary findings indicate that automatic search for multi-stage curricula can successfully discover schedules that improve generalization, performing comparably to extensive grid search over single-stage schedulers.

---


### 80. [SPARC: Single-Pass Scaling for Motion Forecasting with Conformal Bayesian Last Layers](https://arxiv.org/abs/2608.20802)

**<font color=#1a73e8>作者：</font>** Sakif Hossain, Julian Teusch, Jörg P. Müller  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human motion forecasters are increasingly accurate and fast, but reliable deployment requires uncertainty estimates that are structured, calibrated, and efficient. Bayesian and ensemble-based uncertainty estimates often require repeated stochastic inference [15, 26], while conformal calibration alone does not provide an epistemic signal or preserve trajectory covariance structure [14, 50]. We introduce SPARC (Single-Pass Adaptive Risk Calibration), a Bayesian-conformal uncertainty layer for motion forecasting. A deterministic MLP backbone predicts the future mean, and a conjugate Bayesian last layer converts time-domain feature leverage into an analytic horizon-wise epistemic scale $\kappa_t(x)$. This scale inflates a graph-temporal Gaussian covariance without changing its correlation structure, and split conformal calibration produces 95% marginal prediction tubes with finite-sample validity under exchangeability. The key interface is the structured factorization $\kappa_t(x)\Sigma_{\mathrm{str},t}(x)$, which injects feature-space epistemic uncertainty into trajectory densities without Monte Carlo sampling. Across nine dataset-protocol blocks and deterministic, multimodal, and calibration baselines, SPARC ranks first on NLL and on the combined MPJPE+NLL criterion while retaining competitive point accuracy and efficient calibrated tubes. Ranking windows by $\kappa$ separates high-error cases, making the scale usable as a lightweight risk monitor.

---


### 81. [Denoising the Future: Context-Aware Spectral Diffusion for Temporal Knowledge Graph Extrapolation](https://arxiv.org/abs/2608.20804)

**<font color=#1a73e8>作者：</font>** Yanglei Gan, Peng He, Run Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Temporal Knowledge Graph (TKG) extrapolation seeks to infer future facts from time-varying relational histories. Recent diffusion-based approaches improve uncertainty modeling through generative denoising, but their aggregated conditioning on subject histories may insufficiently distinguish query-specific evidence from non-salient historical facts, thereby diluting target-discriminative signals. To bridge this gap, we propose FreqDiff, a Frequency-aware Diffusion framework for TKG extrapolation. Specifically, FreqDiff formulates future object prediction as query-slot denoising and develops a dual-stream denoiser that integrates temporal dependency modeling with context-aware spectral calibration. The spectral branch synthesizes history-conditioned filters from learnable bases to adaptively re-calibrate denoising representations, while a frequency-domain regularizer is proposed to align the denoised target with the gold object in spectral space. Experiments on four public TKG benchmarks demonstrate that FreqDiff achieves state-of-the-art performance.

---


### 82. [Routing Before Looking: Query-Adaptive Evidence Acquisition for Long-form Video Understanding](https://arxiv.org/abs/2608.20805)

**<font color=#1a73e8>作者：</font>** Tianyue Wang, Xuying Wu, Yuxiang Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form video understanding remains challenging for video agents due to the mismatch between query demands and evidence acquisition strategies. Although recent planning-before-perception methods outperform query-agnostic pipelines, they often rely on a single dominant strategy, either generation-based strategy or retrieval-based strategy, limiting their ability to handle diverse query demands. We propose Route2Look, a lightweight and model-agnostic framework for query-adaptive evidence acquisition in long-form video understanding. Route2Look operates in a Route-Look-Memorize loop with three tools: Global Browse for holistic context, Temporal Ground for explicit temporal cues, and Semantic Retrieve for semantic search. The core component is a routing policy that dynamically selects evidence acquisition tools based on the query. To build this policy, Route2Look adopts a two-stage design: first distilling the routing skill from differential contrastive analysis between generation-based and retrieval-based trajectories, and then applying the distilled skill with hard routing rules and continue-or-stop criteria during inference. Experiments on challenging long-video benchmarks show that Route2Look achieves state-of-the-art performance while maintaining strong frame efficiency across datasets and query types. Oracle routing analysis further reveals the potential of query-adaptive evidence acquisition for future long-form video understanding.

---


### 83. [Neuro-Geospatial Modelling of EEG Affective States Using Literature-Informed Environmental Context](https://arxiv.org/abs/2608.20807)

**<font color=#1a73e8>作者：</font>** Utsav Poudel, Jagannath Aryal, Subramaniyaswamy Vairavasundaram  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Environmental exposures such as air pollution and greenness have been associated with affective and cognitive outcomes, but EEG and environmental datasets are rarely jointly georeferenced. We investigate whether literature-informed environmental priors can serve as an auxiliary geospatial modality for EEG-based affective-state classification when individual-level exposure data are unavailable. We combine 30-channel EEG from the EAV benchmark (42 participants, aged 20-30 years) with environmental representations derived from OpenAQ, Sentinel-2, Sentinel-5P, and OpenStreetMap data for Astana. A dual-tower architecture combines EEG-Conformer representations with a graph-based environmental encoder. Because the datasets are not co-registered, environmental context is treated as a literature-informed prior rather than measured exposure. Subject-level repeated splits, permutation and label-shuffling controls, dose-response reversal, and domain-shift experiments distinguish architecture-level gains from prior-dependent gains. The multimodal model achieves 76.2% accuracy versus 67.4% for EEG alone. Controls disrupting environmental-label structure retain part of this gain, indicating that the improvement is not attributable solely to environmental information. Replacing the Astana environmental distribution with an independently modeled Singapore distribution reduces accuracy to 72.8%. These findings demonstrate technical feasibility but do not establish an observed or causal exposure-affect association. The study provides a framework for future jointly collected mobile EEG-environment studies. Implementation: this https URL

---


### 84. [TRACE: Training-time Report-guided and Clinically Ordered Concept Editing](https://arxiv.org/abs/2608.20809)

**<font color=#1a73e8>作者：</font>** Wentao Yue, Tianyou Lai, Jiayu Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast ultrasound diagnosis relies on clinically meaningful semantic concepts, yet most deep learning methods adopt end-to-end image-to-label paradigms that lack interpretability and robustness. While concept-based approaches offer a promising alternative, they often assume complete annotations or require multimodal inputs at inference, which significantly limits their real-world applicability. To tackle these issues, we propose Training-time Report-guided and Clinically Ordered Concept Editing (TRACE), a training-time report-guided framework that leverages structured radiology reports as privileged concept supervision while enabling image-only diagnosis at test time. TRACE refines image-derived concepts through a teacher-guided editing mechanism within a malignancy-aware ordered concept space. To address incomplete annotations, we introduce Strategic Concept Missing Training (SCMT) and train an image-only self-editor via edit distillation for autonomous concept refinement. Besides, we introduce BUSC, a concept-enriched benchmark linking images, labels, and structured attributes. Experiments across multiple datasets demonstrate that TRACE achieves superior performance and improved cross-domain robustness compared to existing methods.

---


### 85. [Resolution-Consistent Greedy Neural Approximation on Infinite-Dimensional Spaces](https://arxiv.org/abs/2608.20812)

**<font color=#1a73e8>作者：</font>** Pablo M. Berná, Antonio Falcó, Diego Mondéjar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop constructive approximation and learning guarantees for shallow neural models with infinite-dimensional inputs observed through finitely many coordinates. The analysis is based on a parameter-normalized neural dictionary and its associated weighted variation class. Within this class, the approximation error separates into a distribution-dependent coordinate-truncation term and a greedy finite-width term. For empirical regression, a fully-corrective greedy procedure yields population guarantees whose statistical complexity is uniform in the retained input resolution. The same framework extends to Hilbert-valued responses without an explicit dependence on the output dimension. The dimension-free statements are statistical, not computational: selecting a new neuron still requires solving a nonconvex parameter-search problem. The quasi-Polish construction underlying recent infinite-dimensional universal approximation results provides a motivating example, and synthetic experiments illustrate the predicted resolution, width, and sample-size regimes.

---


### 86. [GhostTac: Manipulating Tactile Sensors without Physical Contact](https://arxiv.org/abs/2608.20817)

**<font color=#1a73e8>作者：</font>** Kun Wang, Xuancun Lu, Ruochen Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tactile sensors are integral to modern robotic systems, enabling robots to perceive and interact with the physical environment through tactile feedback. However, the physical-layer security of tactile sensors has received little attention. We present GhostTac, the first contactless attack, to the best of our knowledge, that manipulates tactile sensing through electromagnetic interference (EMI). GhostTac exploits nonlinear rectification and limited-bandwidth amplification, converting carefully crafted EMI signals into persistent DC offsets that bypass onboard filtering and induce stable measurement deviations. It enables fine-grained, controllable manipulation of sensor outputs by shaping the spatial distribution and magnitude of interference at targeted locations. Such manipulation can induce harmful robot behaviors, including excessive force that may damage objects or injure people. We evaluate GhostTac on 10 sensor modules and two dexterous hands, covering 15 tactile sensors of different types, and demonstrate consistent effectiveness across all tested devices. Three case studies involving tactile grasping, slip detection, and material classification further illustrate its practical impact on real robotic tasks. These findings reveal a new physical attack vector against tactile sensing in robotic systems.

---


### 87. [Scaling Muon for Diffusion Transformers](https://arxiv.org/abs/2608.20818)

**<font color=#1a73e8>作者：</font>** Chenghao Li, Xiao Han, Xinxin Huang 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The matrix-aware optimizer Muon improves large model training by balancing updates across singular directions, yet its scaling behavior and end-to-end efficiency on large Diffusion Transformers (DiTs) remain unclear. We first establish Muon's scaling behavior on DiTs from 1.3B to 15B parameters, showing that its optimization and generative quality advantages over AdamW persist across model scales. However, at scale, the 5-step Newton--Schulz iteration (NS5) performed at every optimization step, together with full-momentum materialization, introduces substantial computation and communication overhead that can offset Muon's step-efficiency advantage. We introduce \emph{Periodic Row-wise Muon}, which performs a full NS5 spectral update once every \(K\) steps and applies a low compute and communication cost row-wise constrained update based on the current momentum at the remaining steps. We further co-design a distributed implementation that operates directly on sharded momentum during non-refresh steps and accelerates spectral refreshes through bucketed all-gather and communication--computation overlap. Across all scales, Muon improves the best observed generative quality over AdamW by 12.9--19.1\%. Compared with vanilla Muon, Periodic Row-wise Muon remains within 0.5\% in best generative quality on the 1.3B--4B models and improves it by 4.5\% at 9B. It reduces optimizer time by 46.9--54.3\%, end-to-end step time by 15.7--24.3\%, and logical communication volume by 66.7\%, while reaching its respective best generative quality with 33.7--64.8\% less active training time. These results show that Periodic Row-wise Muon preserves Muon's generative quality advantage while translating it into end-to-end training efficiency for large DiTs.

---


### 88. [Prediction certification cannot replace explanation certification: a competence envelope for trustworthy AI under compound stress](https://arxiv.org/abs/2608.20825)

**<font color=#1a73e8>作者：</font>** Nataliya Shakhovska, Ivan Izonin, Stergios-Aristoteles Mitoulis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems increasingly make consequential judgments - which patient is deteriorating, which building is safe to enter, whether an image is authentic and are trusted on the strength of how accurately and confidently they predict. The safeguards that certify them are correspondingly prediction-based: accuracy, calibration and conformal coverage all measure how well a model performs. Whether such checks are sufficient to establish model trustworthiness has remained unclear. Here we prove that they cannot. We establish a separation theorem showing that a reliable model and a compromised one can be identical under every prediction-side certificate, including accuracy, calibration and coverage, yet differ arbitrarily in explanation fidelity and deployment behaviour. Detecting this failure requires access to the model's decision mechanism in addition to its predictions. We introduce the competence envelope as an operational framework that combines prediction and explanation certification into a single deployable criterion. Across diverse datasets and model classes, the proposed framework reveals failure modes that prediction-side certification alone does not capture. Certification against failures that are invisible in prediction behaviour therefore requires evidence about the model's decision mechanism as well as its outputs.

---


### 89. [The Belief Update Gate: Separating Inertia from Learning in Human-AI Interaction](https://arxiv.org/abs/2608.20828)

**<font color=#1a73e8>作者：</font>** Shreyan Biswas, Alexander Erlei, Ujwal Gadiraju  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Repeated human-AI interaction is often analyzed through pooled belief-updating slopes: users observe AI successes and failures, revise reported beliefs in the feedback-consistent direction, but appear conservative on average. We show that such averages can obscure an important distinction between whether an elicited belief report changes at all and how it changes conditional on movement. We refer to this measurement-aware decomposition as the belief update gate. Reanalyzing a multi-task human-AI decision-making dataset with 240 participants, 7,200 trials, and three task domains, we find substantial non-movement in reported beliefs: 67.3% of trial-level belief changes are exactly zero, and 76.4% are smaller than five percentage points. Separating non-moving from moving reports changes the descriptive interpretation of pooled conservatism: the within-trajectory slope rises from 0.494 overall to 0.949 among rows with nonzero movement. Since this latter estimate conditions on observed movement, we interpret it as a descriptive decomposition rather than as evidence of a near-Bayesian latent learning process. Complementary hurdle style analyses (i.e., modeling zero vs. non-zero changes before predicting update magnitude) show that the absolute discrepancy between feedback and entering belief predicts whether a report changes, while the signed feedback discrepancy predicts the direction and magnitude of change among reports that move. Importantly, observed non-movement does not distinguish genuine latent belief inertia from small unexpressed updates, rounding, or other reporting processes. These findings show that calibration analyses of repeated human--AI interaction should distinguish visible non-movement in elicited belief reports from updating conditional on movement rather than treating reported beliefs as a single continuous updating process.

---


### 90. [On the Additive FFT Techniques over Binary Extension Fields](https://arxiv.org/abs/2608.20855)

**<font color=#1a73e8>作者：</font>** Susanta Samanta, Mohammadtaghi Badakhshan, Guang Gong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Motivated by Bailey's four-step FFT algorithm (1989), we develop additive FFT techniques for polynomial evaluation over affine subspaces of binary extension fields. Our key insight is that the Taylor expansion with respect to vanishing polynomials of subspaces provides a structural counterpart to Bailey's matrix formulation. It decomposes an additive FFT (AFFT) into independent sub-AFFTs associated with the columns and rows of a matrix. We first present a general-basis AFFT that applies to any ordered basis and any split of the dimension, providing a unified baseline for measuring the gains from specialization. We then specialize the framework to the Cantor special basis and obtain two AFFT algorithms. The first supports an arbitrary decomposition of the AFFT dimension and exploits the Cantor special basis structure to perform the Taylor expansion stage without finite field multiplications. The second uses a decomposition that preserves the binomial form of the relevant subspace polynomials. It requires exactly $\frac{1}{2}n\log_2 n$ multiplications, together with a closed-form addition count determined by the binary representation of $m$. Our implementation results show that this algorithm is faster than the LCH AFFT over a Cantor special basis in 37 of the 42 configurations tested across two hardware platforms. This performance advantage stems from its fully recursive structure, which provides memory locality by design and avoids separate basis-conversion and evaluation stages. Finally, in a separate analysis, we formalize the notion of partial Cantor special bases and identify parameter regimes in which both the von zur Gathen-Gerhard algorithm and our general-basis AFFT require fewer additions and multiplications than the first Gao-Mateer algorithm.

---


### 91. [Ontology-Driven Structural Regularization for Document-Level Relation Extraction](https://arxiv.org/abs/2608.20856)

**<font color=#1a73e8>作者：</font>** Laura Menotti, Stefano Marchesin, Gianmaria Silvello  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document-Level Relation Extraction (DocRE) relies heavily on costly manually annotated datasets, while large distant supervision resources such as DocRED distant remain underexploited due to noise. We show that a critical yet overlooked source of noise lies in structural inconsistencies within relational triples, including violations of ontology constraints and logical contradictions.
We introduce an ontology-driven framework to quantify and enforce structural consistency in DocRE datasets. Our analysis reveals substantial structural noise in DocRED distant and demonstrates that such inconsistencies propagate to model predictions. Enforcing structural well-formedness during training significantly reduces logical contradictions and consistently improves generalization performance. These findings establish structural consistency as a missing axis of supervision in DocRE and highlight structural regularization as an effective strategy for leveraging distant data at scale.

---


### 92. [Beyond Mean Frametime: Time-Series Signatures for XR Timing Analysis](https://arxiv.org/abs/2608.20861)

**<font color=#1a73e8>作者：</font>** Marvin Thäns, Marc Erich Latoschik  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> XR systems expose timing quantities, such as motion-to-photon latency, frametime, or component-level runtime timings, that can be observed repeatedly as temporally ordered timing traces. Conventional reporting with means, standard deviations, percentiles, or histograms is useful, but it discards temporal ordering. We propose a general structure-aware methodology for analyzing and reporting XR timing traces. Each trace is represented by a compact, interpretable time-series signature, and collections of signatures can be visualized and compared statistically. We evaluate the method using engine-level application frametime traces from a large-scale in-the-wild VR dataset and compare timing signatures across HMD-labelled groups. Across multiple sampling and content-control conditions, structure-aware signatures reveal substantially stronger systematic multivariate differences between HMD-labelled groups than distribution-only summaries. A within-trace temporal-order shuffle control reduces this separation, particularly under content matching, providing direct evidence that original temporal ordering contributes information to the timing signatures. The strongest individual feature contributions vary across sampling and content-control conditions, indicating that no single timing characteristic dominates across analysis settings. Although demonstrated on application frametime, the representation operates on timing traces and therefore provides a basis for future application to other XR timing quantities, including instrumented motion-to-photon measurements.

---


### 93. [Coverage-Driven Verification for Safety-by-Design in AI-Based Collision Avoidance Systems](https://arxiv.org/abs/2608.20864)

**<font color=#1a73e8>作者：</font>** Thomas Stefani, Johann Maximilian Christensen, Elena Hoemann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) offers significant potential for future aviation systems; however, its integration into safety-critical applications requires compliance with the aviation sector's stringent safety standards. For AI and Machine Learning (ML)-based systems, the European Union Aviation Safety Agency (EASA) emphasizes the need to demonstrate the representativeness and completeness of the Operational Design Domain (ODD) and the associated data distributions used during development and verification. Despite this requirement, a structured engineering process for defining target distributions and evaluating representativeness within ODDs remains largely unexplored. This work presents a method for representativeness assessment of AI/ML constituent ODDs in the context of aviation safety assurance. Starting from the methodical identification of suitable target distributions, a process flow is proposed that guides developers from ODD definition and parameter distribution modeling to the quantitative assessment and interpretation of coverage results with respect to EASA's learning assurance objectives. As quantitative measures, the chi-squared goodness-of-fit test is examined and found unsuitable for the large data sets arising in this setting, leading to the adoption of the Kullback--Leibler divergence and Cramér's $V$ for the representativeness assessment. The method is demonstrated using the example of AI-based airborne collision avoidance, employing experimental data from previous Horizontal Collision Avoidance System (HCAS) and Vertical Collision Avoidance System (VCAS) simulations. The results illustrate how statistical distribution comparison methods can support the assessment of representativeness for safety-critical AI applications and contribute toward a systematic Safety-by-Design AI engineering process aligned with emerging EASA guidance.

---


### 94. [ReCurveflow: A Flow Matching Framework that Learns Curved Reaction Trajectories to Predict Transition State Geometries](https://arxiv.org/abs/2608.20869)

**<font color=#1a73e8>作者：</font>** Seungheun Baek, Mogan Gim, Jaewoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting transition states (TS) in chemical reactions is crucial, as they provide insights into reaction mechanisms. Recent work on TS prediction have focused on flow matching supervised on straight linear paths that do not align with actual reaction trajectories. We propose a novel flow matching-based framework ReCurveflow that learns to predict TS geometries supervised on continuously curved reference paths interpolated from a full NEB-derived band of molecular geometries. We also introduce off-path correction, which grants ReCurveflow with the ability to produce corrective velocity fields when engaged off-path geometry states during inference rollout, leading to better resistance against exposure bias and accuracy in TS prediction. Across three data splits and six evaluation metrics, ReCurveflow achieves the best result on the majority of split-metric combinations against seven baselines. Qualitative analyses further show that ReCurveflow generates reaction trajectories with energy profiles that closely track the reference NEB path, provides initializations that ease the NEB optimization bottleneck, and exhibits the intended corrective behavior in its learned velocity fields. The ReCurveflow codebase is publicly available at this https URL.

---


### 95. [RDANet: Relative Degradation Aware Network for Infrared Small Target Detection](https://arxiv.org/abs/2608.20870)

**<font color=#1a73e8>作者：</font>** Rui Liu, Jing Nie, Ying Fu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection is still challenging in remote sensing imagery, because the targets are extremely small, exhibit weak local contrast, and are often embedded in complex and highly variable backgrounds. In addition to these inherent difficulties, we observe that existing detectors often show unstable performance when the target scale changes or when the scene background varies. This scale- and scene-sensitive degradation indicates that current methods are insufficient in simultaneously preserving target structure during feature downsampling and maintaining discriminative local contrast under background shifts, which finally results in unbalanced detection performance across different conditions. To improve detection robustness, this paper proposes a Relative Degradation Aware Network (RDANet) for infrared small target detection. RDANet consists of two dedicated modules: Multi-Scale Anti-Alias Downsampling (MSAD) and Prototype-Guided Skip Memory (PGSM). MSAD introduces multi-scale anti-alias filtering together with pixel-fold aggregation to reduce aliasing effects during resolution reduction, so that target shape information can be better preserved while irrelevant background responses are suppressed. PGSM further enhances the skip features by retrieving patch-level prototypes from a shared memory and adaptively integrating them into the current representation, which helps maintain stable local contrast cues under diverse scene backgrounds. Experiments on three public benchmarks show that RDANet achieves the best performance on most evaluation metrics, while scale- and background-stratified evaluations indicate more stable behavior across target sizes and scene complexity. The code is available at this https URL.

---


### 96. [Multi-Modal Traffic Sign Detection with Semantic Attributes for Autonomous Driving](https://arxiv.org/abs/2608.20874)

**<font color=#1a73e8>作者：</font>** Meda Lazar, Sourab Sridhar, Shashwata Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable traffic sign detection is a prerequisite for the global deployment of autonomous driving systems, where regulatory compliance and road safety depend on perceiving signs correctly across regions, ranges, and weather conditions. Despite recent progress, vision-based methods continue to face three fundamental limitations: poor cross-regional generalization due to high diversity across countries, degraded performance on small-object detection at long ranges (traffic signs occupy as little as $10{\times}10$ pixels at 200m), and fragile temporal tracking under the strongly non-linear perspective distortion that occurs as a vehicle approaches a sign. In this paper, we address the problem of robust, long-range, region-agnostic traffic sign perception by combining camera and Light Detection and Ranging (LiDAR) sensing. We present a multi-modal detection framework whose Intensity-Aware Deformable Fusion module aligns retro-reflective LiDAR cues with camera features, anchoring detection on geometric invariants rather than region-specific visual appearance. We further introduce a dual motion-model tracker that explicitly accounts for non-linear perspective transformations during vehicle approach, substantially improving temporal consistency over linear motion assumptions. Additionally, we develop a semantic attribute classification pipeline that estimates occlusion level, readability, sign embeddedness, and road relevance, providing actionable context to downstream planning. Extensive evaluation on our dataset, spanning 60+ countries and 2,500+ hours of driving data, shows that the proposed pipeline achieves an Object Miss Ratio (OMR) of 0.49% across 221,068 evaluation sequences, demonstrating globally generalizable traffic sign perception in commercial-grade autonomous driving systems.

---


### 97. [Live Artifacts: Authoring Dynamic Media via Live Layers Encapsulating Generative Specifications](https://arxiv.org/abs/2608.20880)

**<font color=#1a73e8>作者：</font>** Leixian Shen, Haotian Li, Hugo Romat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We frame Live Artifacts as a class of persistent generative media between static assets and interactive software. Unlike conventional generative outputs that collapse into static files, Live Artifacts retain their generative logic as a persistent media property, enabling continuous context-dependent regeneration. Time, location, or live data become part of their generative specifications, initiating coordinated updates across modalities (e.g., adapting text, visuals, and audio together) while preserving composition, semantics, identity, and cross-modal coherence. To facilitate experimentation with this medium, we present LiveCanvas, an authoring system that reconceptualizes visual layers as live generative specifications with explicit mutability and constrained dependencies. Creators orchestrate dynamic behaviors and manage generative persistence within a visual canvas rather than through programming, defining what remains stable, what can change, and how changes propagate. We evaluate Live Artifacts through a gallery of responsive examples and a qualitative study with six professionals, finding that LiveCanvas facilitates a shift from composing static outputs to crafting responsive generative artifacts while remaining aligned with familiar authoring practices.

---


### 98. [LoRC: Detecting AI-Generated Images via Low-Rank Collapse in Semantic Residuals](https://arxiv.org/abs/2608.20882)

**<font color=#1a73e8>作者：</font>** Haozhen Yan, Ruoxin Chen, Jiahui Zhan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern generators faithfully model macroscopic semantics, producing synthetic images that appear highly realistic. Consequently, decisive forensic cues reside in subtle non-semantic visual discrepancies. To reveal these cues, we revisit AIGI detection from a geometric perspective and identify an architecture-agnostic signature. Specifically, modern generators exhibit low-rank collapse (\textit{i.e.}, rank degeneracy) in the semantic-residual orthogonal subspace while largely preserving the dominant semantic direction. This structural flattening consistently emerges during the final decoding stage, forming a shared bottleneck across diverse generator architectures. Motivated by this signature, we propose \textbf{LoRC}, a framework that decouples semantic dominance to capture the collapsed residual geometry induced by the generative decoding bottleneck. Our method improves accuracy by an average of 7.0\% across multiple benchmarks and achieves 97.0\% accuracy on 39 unseen generators. These results demonstrate strong cross-model generalization and robustness, making LoRC a reliable approach for AIGI detection in complex real-world environments.

---


### 99. [Breaking High Confidence: Practical Face Impersonation under High-Security Thresholds](https://arxiv.org/abs/2608.20884)

**<font color=#1a73e8>作者：</font>** Changjin Kim, Seunghun Paik, Dongsoo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition systems (FRSs) are increasingly deployed in critical real-world services for authentication, such as banking applications and airport identity checks, necessitating stringent security configurations. Consequently, the security vulnerabilities of FRSs have garnered significant attention. While existing studies have extensively explored FRS security, prior analyses have primarily focused on medium-security threshold settings, which are not directly applicable to FRSs operating under high-security constraints. In this paper, we propose the first successful impersonation attack against FRSs under high-security threshold settings. Among various threat models, we focus on a practical and challenging scenario: score-based impersonation attacks under strict rate limits. To precisely evaluate the feasibility of such attacks, we provide a principled mathematical analysis characterizing the gaps in each stage of the attack pipeline. Our method significantly enhances impersonation capabilities in score-based attacks, even under elevated decision thresholds. On the LFW benchmark, with a budget of only 100 confidence score queries per identity, our attack achieves an impersonation success rate exceeding 92\% against Amazon Rekognition at a confidence score threshold of 99-recommended setting for law enforcement scenarios. We further observe consistently robust performance across multiple open-source FRSs evaluated at similarly stringent decision thresholds.

---


### 100. [EmotionDialogCN: A Spontaneous Multimodal Dataset for Mandarin Emotional Dialogue](https://arxiv.org/abs/2608.20905)

**<font color=#1a73e8>作者：</font>** Yi Zheng, Yifan Xu, Yan Zhou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face-to-face audiovisual interaction is central to human communication, conveying rich emotional and social cues. However, existing multimodal dialogue datasets remain limited by inadequate emotion annotations, poor emotional diversity, and small scale. We introduce EmotionDialogCN, a large-scale audiovisual-emotional dataset designed to capture authentic face-to-face communication. It contains 21,880 dialogue sessions performed by 119 professional actors across 20 everyday scenarios, covering 18 emotion categories with over 400 hours of recordings, the largest and most comprehensive dataset of its kind. A novel data collection framework minimizes equipment interference, enabling natural and nuanced emotional expressions. EmotionDialogCN achieves an emotion distribution deviation of 0.64 from real human emotion statistics (versus 5.65 for prior datasets) and consistent subject framing (52-59% frame occupancy). Together, these properties translate into stable unimodal and multimodal performance across acoustic, lexical, and visual modalities, with fusion results further underscoring strong multimodal alignment and cross-modal complementarity.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-158](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
