# 📦 其他研究 | 2026年10月22日

> 本类共 **288** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-288](./part-06.md)

---

### 201. [Poisoning-Based Backdoors Are Not Cryptographic](https://arxiv.org/abs/2610.28045)

**<font color=#1a73e8>作者：</font>** Masahiro Kaneko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To defend against backdoor attacks on neural networks, the defender must identify the verifier function that determines whether an input is a trigger, rather than rejecting individual triggers in isolation, since an attacker can generate new triggers satisfying the same verifier faster than they can be blocked. If a backdoor verifier could be installed with the asymmetry of a cryptographic authentication scheme, in which only the attacker can produce trigger inputs while the defender cannot reverse-engineer the verifier from observations, learning-based defense would be impossible in principle. We show that no such asymmetry can arise from poisoning-based installation, in which the only verifier-dependent input to training is a poisoned dataset. The argument is a reduction. A training procedure that installs a verifier from poisoned data, so that the backdoor fires on unseen triggers while benign behavior is preserved, is itself a learner for that verifier. Any verifier that is computationally hard to learn is therefore impossible to install through poisoning, and any verifier that poisoning can install is reconstructible by a white-box defender holding comparably many labeled trigger observations. A complementary argument shows that a secret key supplied to the model at inference is observable to the same defender. The result takes representative trigger observations as given and concerns when the backdoor fires rather than what it does. Experiments on instruction-tuned large language models confirm the dichotomy, with no configuration yielding a backdoor that is both effective for the attacker and irrecoverable for the defender.

---


### 202. [A Process-Informed, Photorealistic Digital Twin for Vision-Based Inline Inspection of C-SMC Strip Deposition](https://arxiv.org/abs/2610.28050)

**<font color=#1a73e8>作者：</font>** Patrick Flore, Fabian Röder, Kevin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inline quality assurance for Sheet Molding Compound (SMC) manufacturing is hindered by the lack of large-scale, accurately labeled image datasets for training machine-learning models. This work presents a process-informed, photorealistic digital twin for carbon-fiber SMC strip deposition. A rigid-body simulation reproduces the deposition kinematics (settling, friction, belt motion), while a physically grounded polarization-rendering model produces realistic appearance, so that every image carries exact, mutually consistent labels in synchronized formats: oriented bounding boxes, point annotations, density maps, and polarization renderings (Angle and Degree of Linear Polarization). Because the joint distribution of many overlapping strips cannot be specified analytically, simulation yields exact, scalable ground truth that manual annotation cannot provide. The twin produces over 16,000 images across 3,300 frames, and the synthetic data replicate near-isotropic fiber orientation (axial concentration r < 0.05) consistent with as-deposited commercial SMC. Trained purely on synthetic data, YOLOv11 and CSRNet reach detection mAP50 up to 0.91, with a dedicated oriented-bounding-box detector confirming the oriented labels are directly trainable (mAP50 = 0.83); on real manufacturing images, the synthetic-to-real difference in edge and texture structure (Kolmogorov-Smirnov distance 0.46, distribution overlap 0.56) is of the same magnitude as the difference between two real acquisition series of the same material (0.41, overlap 0.57). The approach substantially reduces the labeling burden for camera-based inline inspection of fiber orientation and volume content.

---


### 203. [Assessing Representation Semantics Under Language Pretraining in Fine-Grained Classification](https://arxiv.org/abs/2610.28051)

**<font color=#1a73e8>作者：</font>** Md Raisul Kibria, Sébastien Lafond  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how supervision signals shape semantic visual representations remains challenging, particularly in fine-grained, low-data settings. Standard evaluations of vision models rely on downstream accuracy, which often fails to capture structural differences in learned representations. We propose a compact explainability-driven framework for comparing encoders trained with classification-only and caption-generation supervision on CUB-200. Using a controlled two-stage protocol in which both encoders are ultimately optimized for the same classification task, we enable a direct comparison of the resulting representations. Saliency maps are generated using attention rollout and gradient-weighted rollout and evaluated with five metrics covering faithfulness (positive and negative perturbation) and localization (keypoint emphasis, background attribution, and Earth Mover's Distance). Across random seeds and explanation methods, caption supervision yields representations that are more sensitive to the removal of salient regions, better aligned with annotated object parts, and less reliant on background regions, whereas classification supervision produces representations that are slightly more robust to the removal of low-saliency regions. An ablation study on the Oxford-IIIT Pet dataset shows consistent trends across key metrics. These results demonstrate that the proposed framework makes supervision-induced representational differences observable and quantifiable beyond downstream accuracy alone. More broadly, it provides a systematic basis for assessing learned representations and comparing alternative training and transfer-learning strategies.

---


### 204. [Universal Online Convex Optimization With Delayed Feedback](https://arxiv.org/abs/2610.28058)

**<font color=#1a73e8>作者：</font>** Hao Qiu, Andrew Jacobsen, Emmanuel Esposito 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study universal online convex optimization with delayed feedback. We develop a single algorithm that simultaneously adapts to general convex, strongly convex, and exp-concave losses without prior knowledge of the curvature class or parameters. Our regret bounds match the best known dependence on the time horizon $T$ and delays up to doubly logarithmic factors: roughly $\sqrt{T + d_{\mathrm{tot}}}$ for convex losses and $\sigma_{\max}\log T$ rates with curved losses, where $d_{\mathrm{tot}}$ is the total cumulative delay and $\sigma_{\max}$ is the maximum number of simultaneously missing observations. Our main technical contribution is a delayed meta-learner with a second-order excess-loss guarantee, which enables curvature-adaptive aggregation of delayed base learners. In addition, our new exp-concave base learner yields a sharper regret bound which improves the state-of-the-art delay dependence by replacing the maximum delay with the potentially much smaller $\sigma_{\max}$, while retaining the complementary $\sqrt{d_{\mathrm{tot}}}$ dependence.

---


### 205. [Auditing Where Concept Bottleneck Accuracy Comes From on CUB](https://arxiv.org/abs/2610.28059)

**<font color=#1a73e8>作者：</font>** Sascha Saralajew, Eleonora Poeta, Eliana Pastor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) promise predictions that humans can inspect and correct through concepts such as "curved beak". Yet on CUB-200-2011, their standard benchmark, progress is measured like that of ordinary classifiers: by task and concept accuracy. Neither reveals whether the label is predicted from the exposed concept scores, or whether a concept is supported by visual evidence of that concept rather than by co-occurring features such as cues to the species as a whole. We audit where the accuracy of CBMs and Concept Embedding Models (CEMs) on CUB comes from. The CUB annotations are too noisy to explain it: class-level training labels agree with per-image annotations on only ~82% of image--concept pairs, and classifiers trained on per-image annotations reach only ~37% species accuracy. Leakage probes show that CEM predictions cannot be reconstructed from their concept scores; the missing class information sits in internal embeddings. We identify four design axes through which class information can enter concept scores---receptive field, shared versus concept-specific representations, norm-dependent scoring, and task supervision. An ablation shows that most of it enters through non-local features: restricting a ResNet50 backbone to local BagNet patches lowers the accuracy recoverable from concept scores from 72% to 43%, close to what ground-truth annotations support, while joint training raises it again at the cost of concept accuracy. Localization and occlusion show that locality makes grounding measurable but does not guarantee it: under class-level labels, local concept scores use the head as a proxy for body, wing, and tail concepts, and CEM concept scores barely respond to occluding their supporting part. Task and concept accuracy should thus support, not drive, the evaluation of CBMs, and given the noisy annotations, CUB accuracy gaps should not be overinterpreted.

---


### 206. [Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models](https://arxiv.org/abs/2610.28074)

**<font color=#1a73e8>作者：</font>** Peisong Wen, Qianqian Xu, Minye Lei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As a prototypical latent world model, Joint-Embedding Predictive Architectures (JEPAs) provide strong semantic representations. However, dense patch representations expose a redundant interface to downstream predictors, which must implicitly infer spatial organization and temporal correspondence, presenting three challenges. First, object information is distributed across patches, forcing each downstream predictor to redundantly recover object structure that could otherwise be reused across tasks before modeling interactions. Second, the lack of explicit entity correspondence across time makes historical transitions expensive, restricting the predictor's flexibility in utilizing context. Third, without explicit transport structure, existing JEPA models typically use pointwise l1/l2 distances, which are insensitive to spatial displacement when predicted and goal supports are largely disjoint. We propose the Slot-based Joint-Embedding Predictive Architecture (Slot-JEPA), which decomposes dense representations into stable semantic slots and time-varying spatial masks. Pretrained once and frozen downstream, this decomposition exposes a reusable object-structured interface. Building on it, our Transition Memory Predictor (TMP) stores visual transitions as compact masks and retrieves useful context using statistics of corresponding slots. Its two branches separate slot-specific dynamics from shared cross-slot dynamics. We further use Unbalanced Optimal Transport (UOT) to supervise mask prediction and evaluate candidate plans by transporting mass between aligned predicted and goal masks, providing a signal better aligned with spatial progress. Across seven visual-understanding benchmarks, the slot-reconstructed features remain transferable. Slot-JEPA also improves goal-conditioned planning across six planar environments and four robotic arm planning tasks on the REALM-JEPA benchmark.

---


### 207. [On the Vulnerabilities and Data-Free Removal of Watermarks in Batch Normalization Layers](https://arxiv.org/abs/2610.28076)

**<font color=#1a73e8>作者：</font>** Elena Rodríguez-Lois, Fernando Pérez-González  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Batch Normalization (BN) layers have become a common choice for embedding white-box watermarks in Federated Learning (FL), providing a simple and effective mechanism for model ownership verification and participant identification. However, previous works have focused on robustness against generic model modifications, leaving the security implications of this design largely unexplored. In this paper, we identify fundamental vulnerabilities of BN-based watermarking schemes and propose a practical data-free attack that exploits them. Experimental results on two representative FL watermarking schemes show that the proposed attack consistently removes the watermark with minimal impact on model performance, even without access to representative training data. More broadly, our findings highlight the importance of evaluating DNN watermarking schemes under threat models consistent with Kerckhoffs's principle, rather than relying on security through obscurity.

---


### 208. [PULSE: Personalized Opportunistic Learning for Wearable Devices](https://arxiv.org/abs/2610.28081)

**<font color=#1a73e8>作者：</font>** Mattia Giovanni Campana, Dariush Salami, Hüseyin Yiğitler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable devices increasingly support personalized health and well-being applications, but post-deployment data can differ substantially from those used for training, while purely local adaptation may be limited by the data available on a single device during real-world operation. Conventional federated and decentralized learning rely on recurrent communication and stable connectivity, whereas existing opportunistic approaches often exploit available encounters without adequately considering their utility, compatibility, or communication cost.
We propose PULSE, an event-driven framework for personalized opportunistic learning that treats each encounter as an online collaboration decision, selecting either no interaction or a promising nearby peer. Peer gradients are incorporated only when compatible with the local learning direction, while past interactions guide future peer selection. Across human activity recognition, fall detection, and stress recognition under synthetic and real contact traces, PULSE preserves or improves personalized classification performance, while reducing peer-assisted exchanges by 80-94% compared with opportunistic model averaging. On-device experiments further demonstrate its feasibility on wearable hardware: peer-assisted operations require limited energy, while the complete implementation occupies 149.8 KiB of RAM and 561.8 KiB of flash. The obtained results show that selective opportunistic collaboration can provide effective personalization while limiting communication and resource demands on constrained wearable devices.

---


### 209. [InsightRAG: Aggregating Distributed Scholarly Judgments for Scientific Survey Generation](https://arxiv.org/abs/2610.28085)

**<font color=#1a73e8>作者：</font>** Yuquan Lin, Wenshuo Zhang, Yilin Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid growth of scientific literature makes survey writing increasingly challenging, motivating automatic survey generation. Yet, existing systems must search an open space of papers and an open space of concepts with no trace of how the community itself has navigated them, leading to incomplete scope, weak taxonomies, and unreliable citations. Our core insight is that author-written Related Work sections contain the human judgments needed to address both limitations: authors curate the citations relevant to their contributions and explain how the cited works relate, yielding paths for scope reconstruction and relational evidence for organization. We propose InsightRAG. Its insight-guided retrieval follows author-supported citation relations to reconstruct a verified research scope and structure the resulting relational evidence. It aggregates these judgments under a minimum-conflict objective into a taxonomy that reflects recurring author-written perspectives in the retrieved literature, guides generation, and bounds each section's evidence. Results on ten topics show gains in scope reconstruction, taxonomy quality, citation support, and reference reliability.

---


### 210. [MoDDiT: Simple Token Routing in Diffusion Transformers](https://arxiv.org/abs/2610.28086)

**<font color=#1a73e8>作者：</font>** Jarek Liesen, Matthew T. Jackson, Benjamin Ellis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time video generation, interactive world models, and on-device image synthesis are almost a reality. Diffusion Transformers (DiT) achieve excellent sample quality, shifting the bottleneck to the throughput of the models themselves. Natural images are inherently sparse, as large portions of an image are often background, contribute little to the scene content, and are easy to denoise. DiTs fail to exploit this sparsity, as they process image tokens statically and uniformly. We propose MoDDiT, a simple architecture modification that learns to route tokens through both MLP and self-attention operations. By routing tokens through both blocks independently, MoDDiT allows for dynamic compute allocation in MLPs that varies across tokens, images, and denoising timesteps. Using MoDDiT to train image generation models from scratch significantly reduces computational costs of training and inference, processing as few as 12.5% of the tokens. By increasing sparsity and model depth, MoDDiT reduces costs and improves generation performance over unrouted baselines. The learned allocation is interpretable, revealing how computation varies with visual content and noise level. We also use MoDDiT to train video generation models, where allocation correlates with motion, and to distill a dense bidirectional video model into a sparse autoregressive student.

---


### 211. [From Complex Histories to Simple Predictors: Predictive Dimension in Dynamic Graph Learning](https://arxiv.org/abs/2610.28090)

**<font color=#1a73e8>作者：</font>** Hantong Feng, Duxin Chen, Wenwu Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing continuous-time graph learning methods rely heavily on complex neural architectures to encode ever-expanding interaction histories. However, the future conditional distribution induced by complex histories can often be characterized by a low-dimensional predictive state manifold, implying that only a few predictive degrees of freedom are essential for future interactions. We therefore argue that continuous-time graph learning should identify low-dimensional states sufficient for future prediction rather than reconstruct the full history. To make this perspective measurable, we define and independently estimate the intrinsic predictive dimension, which quantifies the effective predictive degrees of freedom required by a given task. Specifically, we remove the history-independent marginal from the history-conditioned future distribution, decompose the resulting predictive residual operator, and estimate the minimum effective rank needed to preserve the predictive power of the full history. Experiments across datasets show that model performance saturation is largely determined by the intrinsic predictive dimension. Based on this finding, we propose PreDyG, a lightweight model whose capacity is matched to the intrinsic predictive dimension. PreDyG achieves superior predictive performance with only 0.07\% of the parameters of a representative complex baseline.

---


### 212. [LatticeRank: Spacing-Ranked Consistency for Native-Grid 3D Medical Image Segmentation](https://arxiv.org/abs/2610.28091)

**<font color=#1a73e8>作者：</font>** Jingjia Yan, Yue Zhuo, Zhonghua Xie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Variable voxel spacing changes more than image resolution: it alters the discrete sampling lattice, tensor geometry, and anatomical evidence available to a 3D segmentation network. While conventional pipelines restore images to a canonical grid, direct-grid deployment requires the model itself to tolerate these changes. We observe that candidate grids are not exchangeable views -- a coarse grid removes more structural information than a mildly resampled one -- yet standard consistency objectives assign them equal influence. We therefore propose LatticeRank, a training-only framework that aligns candidate posteriors in physical space and allocates consistency supervision by voxel-spacing order: among endpoint-matched candidates, the auxiliary loss concentrates on the coarsest requested grid, while inference retains a single network forward with no candidate branch or ensemble. On MSD Task04, LatticeRank improves coarse-grid Extra Dice over mean consistency by 0.03436 across five seeds while meeting the prespecified reference-grid noninferiority criterion. A controlled ladder shows that grid exposure provides the largest recovery, posterior consistency adds a second gain, and spacing-ranked allocation yields the strongest direct-grid result; requested spacing thus provides a simple, model-independent ordering signal for direct-grid consistency learning.

---


### 213. [Polyscene: Scenario Planning as Diversity Planning](https://arxiv.org/abs/2610.28102)

**<font color=#1a73e8>作者：</font>** Mustafa F. Abdelwahed, Joan Espasa, Felipe Meneguzzi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scenario planning is a foresight practice in which analysts construct a small set of plausible futures and prepare an organisation for each. Each scenario is a narrative that must be plausible, internally consistent, relevant and challenging, and the set as a whole must be differentiated. The practice remains manual: a workshop (i.e., a facilitated meeting in which a small group of experts writes the narratives) considers only the factors it has time for, carries the biases of the experts who run it, and cannot be redone whenever conditions change. In this paper, we automate scenario planning by casting it as a diversity planning problem, in which two scenarios differ when they end in different narratives on the analyst's drivers. The result is a set of scenarios, one for each narrative that the topic can reach within a budget. Our implementation, Polyscene, is a generic engine that generates scenarios from a topic. We use geopolitical conflicts and shipping-route disruptions as case studies. For the first, we build the planning problem's initial state from the GDELT Project so it reflects current relationships among the countries involved. Polyscene then generates scenarios showing how relationships among those countries change. With a board of six countries as of 1 January 2021 and a budget of five events, the conflict set puts five of the 15 country pairs at war, and each of the three wars that break out among these countries by 1 January 2026 ends a scenario. For the second, we build the initial state from ship traffic, a supply-pressure index, and the news, and Polyscene generates scenarios showing what a closed or diverted route could do to a manufacturer's parts stock. With four routes per board and the same date and budget, each set includes three outcomes, and the Suez Canal set includes the March 2021 blockage and the December 2023 Red Sea container diversion.

---


### 214. [A Semi-Analytical Inference Framework for Structural Causal Models](https://arxiv.org/abs/2610.28103)

**<font color=#1a73e8>作者：</font>** Tatiana Boura, Robert Peharz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structural Causal Models (SCMs) provide a principled framework for observational, interventional, and counterfactual reasoning, all of which rely on probabilistic inference. Existing frameworks either transform SCMs into alternative tractable representations or rely on approximate inference with expressive generative models. We instead perform inference using a message passing scheme directly on the SCM by representing structural mechanisms and probability densities in a common finite-dimensional function space. Forward propagation combines a numerical realization of the Law of the Unconscious Statistician, while propagated densities are recovered by spline projection from LOTUS moments. The same representation naturally yields backward message passing for conditioning, providing a unified framework for causal inference. Using tensor-product B-spline bases, the resulting algorithm expresses inference through numerical quadrature and linear algebra without explicitly constructing conditional distributions. Experiments on randomly generated continuous SCMs demonstrate accurate approximation of Monte Carlo reference solutions and systematic improvement with increasing basis resolution.

---


### 215. [Robust Representation Learning for Spiking Neural Networks based on Conditional Information Bottleneck](https://arxiv.org/abs/2610.28110)

**<font color=#1a73e8>作者：</font>** Yuli Zha, Wang Fan, Yixiao Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) have shown great potential for low-power neuromorphic computing due to their event-driven processing and spatiotemporal sparsity, but they remain vulnerable to input perturbations, hardware-intrinsic noise, and adversarial attacks in real-world deployment. We attribute this vulnerability partly to input-specific hidden representations learned by standard SNNs trained with conventional cross-entropy loss, as our information-plane analysis empirically shows that substantial input-related information can still be retained after label-predictive information becomes stable. To address this issue, we propose SCIB, a simple yet effective robust learning objective for SNNs based on the Conditional Information Bottleneck. Different from conventional variational IB methods, SCIB replaces the mutual information compression term $I(X;S)$ with the conditional mutual information $I(X;S|Y)$ and derives a tractable variational upper bound. Moreover, it introduces a learnable class-conditional prior instead of a label-agnostic isotropic Gaussian prior, improving the expressiveness of variational compression and encouraging class-structured representations when combined with the supervised classification objective. Systematic experiments on Fashion-MNIST, CIFAR-10, and CIFAR-100 under external environmental noise, neuromorphic hardware noise, and adversarial attacks show that SCIB improves robustness over standard SNNs and IB-based baselines under most evaluated noise conditions, improves adversarial accuracy under the evaluated attacks without using adversarial training, and reduces the SynOps-based single-sample inference energy consumption by 24.9% relative to an unconstrained SNN baseline.

---


### 216. [Reliability-Guided Vision-Language Decoding with Text-Aware Skip Refinement for Medical Image Segmentation](https://arxiv.org/abs/2610.28118)

**<font color=#1a73e8>作者：</font>** Sivan Talaei, Fatemeh Daneshfar, Mustaqeem Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation remains challenging when targets exhibit limited visual distinction, irregular structure, or substantial variation across imaging modalities. Medical text can reduce this ambiguity, but indiscriminate fusion may introduce unreliable guidance. We present RELiF, a vision--language framework that integrates text through reliability-guided decoding. Its Reliability-guided Fusion Gate (RFG) adaptively controls cross-modal updates, while the Text-guided Skip Refinement Adapter (TSRA) refines high-resolution features using text guidance. RELiF is evaluated on radiographic, CT, and endoscopic segmentation tasks, where it shows competitive performance across diverse imaging characteristics and target appearances. Additional analyses examine efficiency and stability. The complementary uncertainty representation derived from the reliability response also shows an association with prediction difficulty, with higher uncertainty values occurring more frequently in pixels associated with segmentation errors. Code: this https URL.

---


### 217. [PointForward V2: Point-Aligned Interaction for Feedforward Driving Reconstruction](https://arxiv.org/abs/2610.28120)

**<font color=#1a73e8>作者：</font>** Xianqi Wang, Cheng Chi, Yuechuan Pu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feedforward reconstruction of dynamic driving scenes requires integrating observations across multiple views and time steps into a coherent 3D representation. PointForward established state-of-the-art feedforward driving reconstruction by lifting image observations into sparse 3D queries, demonstrating the effectiveness of point-aligned scene representations. However, these queries are largely processed independently, limiting information exchange across space and time, while direct global attention among tens of thousands of point queries is computationally prohibitive. In this work, we present \textbf{PointForward V2}, which advances point-aligned representation to point-aligned interaction. Our key idea is to mediate query interaction through compact, scene-structured registers. For the static background, frame-wise Static Scene Registers compress point information, communicate across frames, and propagate the aggregated context back to the queries. For each dynamic instance, queries from different frames are aligned in an object-centric canonical space and interact through instance-specific Dynamic Instance Registers. We further employ 4D positional encoding that combines aligned spatial coordinates with original timestamps, enabling spatially aligned yet temporally distinguishable interactions. In this way, PointForward V2 enables scalable spatio-temporal reasoning directly among lifted 3D queries without dense global attention. Experiments on Waymo, nuScenes, and Argoverse 2 demonstrate state-of-the-art performance across large-scale driving benchmarks.

---


### 218. [Interruption-Aware Recurrent Reinforcement Learning for UAS Navigation Under Temporary Overrides](https://arxiv.org/abs/2610.28121)

**<font color=#1a73e8>作者：</font>** Christopher Conrad, Deepak Panda, Weisi Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safe autonomous navigation of UASs requires tactical deconfliction to address conflicts that strategic coordination cannot prevent. This task is challenging under partial observability, when sensor or traffic data are missing, delayed, or degraded. Geometry-based methods can offer separation assurances but face limitations in dense encounters. Recurrent reinforcement learning has therefore been proposed to learn navigation policies that integrate observation-action histories to optimise long-term safety-efficiency trade-offs. However, operational safeguards may require a remote pilot, onboard detect-and-avoid system, or runtime assurance mechanism to temporarily override the learned policy. A research gap remains in understanding how these interruptions affect recurrent policies when the agent regains authority. Benchmark evidence shows that interruptions make task variables less decodable from the recurrent hidden state and increase post-interruption collision risk. The findings suggest that altered recurrent context prolongs post-handback degradation through an action-observation feedback loop, in which changed actions alter the flight path and subsequent recurrent updates. To address this vulnerability, we propose three interruption-aware architectures that condition recurrent processing on interruption context through separate feature streams, dedicated interruption memory, or gated environmental features. Across simulations, all three architectures preserve more decodable task information than a standard recurrent policy. Moreover, the strongest architecture reduces post-interruption collisions by 74% and interruption-induced mission failures by 69% relative to the recurrent baseline, without degrading interruption-free performance. These results show that safe interruption does not guarantee safe handback, and support interruption-aware recurrent design for resilient UAS autonomy.

---


### 219. [GAMF-Net: Grouped Availability-Aware Multimodal Fusion for Smartphone Skin Lesion Classification](https://arxiv.org/abs/2610.28129)

**<font color=#1a73e8>作者：</font>** Yue Zhuo, Jingjia Yan, Fangyu Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Smartphone clinical images provide a low-cost data source for computer-aided skin lesion classification in resource-constrained settings, but images alone cannot fully capture patients' medical histories and lesion symptoms. To address the lack of structured organization among heterogeneous clinical variables, the ambiguity between observed and imputed values, and the risk that clinical information may interfere with visual evidence, we propose GAMF-Net, a grouped availability-aware multimodal fusion network. Ten clinical variables are divided into three semantic groups---demographics, history-related risk, and lesion presentation---and each group jointly encodes field values and field-level availability masks. The image branch produces the base classification logits, while each clinical group generates image-conditioned class-level residual evidence. Only available groups participate in availability-normalized equal-weight fusion; when all clinical information is unavailable, the model reduces exactly to the image-only pathway. We evaluate the method on PAD-UFES-20 under a patient-disjoint five-fold protocol with separate training, validation, and test partitions. GAMF-Net achieves an Accuracy of $74.17\pm2.85\%$, a balanced accuracy (BACC) of $70.11\pm2.11\%$, a Macro-F1 of $68.85\pm0.85\%$, and a Macro-AUROC of $93.42\pm1.20\%$, outperforming all image-only and multimodal baselines reimplemented under a unified protocol. Compared with the strongest baseline, MetaBlock, the corresponding improvements are 2.37, 2.59, 4.14, and 1.02 percentage points, respectively. Ablation results show that clinical information substantially improves class-balanced performance, constrained equal-weight fusion is more effective than dynamic fusion, and the lesion-presentation group provides the most informative clinical complement.

---


### 220. [OV-Foam: How 3D Representations Shape Semantic Feature Lifting](https://arxiv.org/abs/2610.28131)

**<font color=#1a73e8>作者：</font>** Yousef Rajeh, Alejandra Esparza Pelcastre, Ivan Viola 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing feature lifting approaches for open-vocabulary segmentation rely on simple backprojection to assign features to primitives. In the case of 3D Gaussian splatting reconstruction, the primitives overlap heavily, leading to suboptimal reconstructions, governed by many primitives per ray. Backprojection, however, reduces to a least-squares solvable problem, exactly when no two primitives share a ray. Motivated by this insight, we propose OV-Foam, which uses PowerFoam as the underlying representation. This representation uses a power-diagram to partition the scene, resulting in zero overlap between primitives and a substantial reduction in primitives per ray, which ultimately simplifies the lifting problem and allows for closer-to-optimal feature assignment. We show that the space partitioning primitives of OV-Foam reach near-optimal assignment, and our experiments demonstrate improved open-vocabulary segmentation over Gaussian baselines.

---


### 221. [Causal Discovery for Linear Models with Latent Confounding via Multi-domain Identifiable Representation Learning](https://arxiv.org/abs/2610.28134)

**<font color=#1a73e8>作者：</font>** Danru Xu, Aapo Hyvärinen, Sara Magliacane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery with latent confounding is particularly challenging, but a common setting in real-world data. In this work, we focus on linear causal models with latent confounding, represented by acyclic directed mixed graphs (ADMGs). Existing methods that fully identify ADMGs typically assume non-Gaussianity or graphical constraints, such as bow-freeness. In contrast, we propose Linear ADMG Learning (LinADMG), a framework for learning ADMGs for linear causal models through identifiable representation learning. Rather than relying on non-Gaussianity or bow-freeness, LinADMG leverages multi-domain settings to identify the noise variables. We show that the identifiability of the noise variables is sufficient for recovering all direct causal relations, and that, under an additional latent-confounding no-cancellation condition, LinADMG can identify the whole ADMG. We implement LinADMG with four identifiable representation learning approaches from the literature and validate the methods on simulated and semisynthetic datasets.

---


### 222. [Curriculum Learning for Generative Flexible Docking](https://arxiv.org/abs/2610.28145)

**<font color=#1a73e8>作者：</font>** Wenyin Zhou, Hossein Azizpour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flexible docking is a highly practical task, aiming to predict the joint configuration of a protein-ligand complex from a protein apo structure and a ligand SMILES string. Diffusion and flow-based generative models have made this task tractable by modeling the posterior distribution over the ligand pose and the protein conformation conditioned on the apo input. The central challenge, however, remains the long-tailed apo-to-holo structure shift, where a small fraction of protein undergo large conformational changes. In this work, motivated by the practical observation that downweighting large shift examples improves generalization, and by the mixed nature of the long tail consisting of genuinely difficult examples and noisy ones, we propose to use curriculum learning for this task, gradually incorporating large conformational change examples during training. With a linear pacing function, we show that an existing method can be strongly enhanced. On the PDBBind ESMFold apo benchmark, with relaxation and confidence-based pose selection, the resulting model GCLDock achieves a 46.52% top-1 success rate (ligand RMSD less than 2A) and 40.26% when additionally requiring PoseBusters validity, outperforming existing baselines.

---


### 223. [Digital Nudge Effects in Optimal Stopping Games: Antagonistic Interactions in Layered Choice Architectures](https://arxiv.org/abs/2610.28154)

**<font color=#1a73e8>作者：</font>** Batisse Manhardt, Ja-Nae Duane  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital nudges have become a prominent area of research in human-centered interaction, yet little is known about how they interact when deployed together. This study examines the individual and combined effects of anchoring, salience, and social proof digital nudges on stopping behavior and outcome quality in a sequential decision task. Using a 2^3 between-subjects factorial design grounded in the secretary problem (N = 181), we find that (1) an anchor nudge significantly increased exploration rather than constraining it (b = 1.207, p = .017); (2) the salience nudge produced the smallest effect of any condition; and (3) combining the anchor and social proof nudges produced the worst outcome quality of any condition ($181.83 vs. $192.21 for anchor-only), with outcome quality declining monotonically as nudge count increased. These findings provide the first controlled evidence for a digital nudge crowding-out effect with direct implications for the ethical design of digital interfaces.

---


### 224. [DocLayout-YOLO: Axis-Attentive Document Layout Detector with Mesh-Guided Synthetic Pretraining](https://arxiv.org/abs/2610.28171)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhao, Hengrui Kang, Guang Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and efficient document layout analysis is critical for modern document parsing systems. However, although the YOLO framework represents a leading paradigm for the real-time detector, its adaptation to heterogeneous documents remains underexplored. To address this gap, we propose DocLayout-YOLO, a document-specialized real-time detector that integrates diverse synthetic document pretraining and page-axis context modeling. From the data perspective, we introduce MeshLayout-1M, a synthetic pretraining corpus generated by the proposed Mesh-candidate BestFit algorithm, which provides large-scale and diverse document layouts for pretraining and improves adaptation to heterogeneous document scenarios. From the model perspective, we propose Page-Axis Layout Attention (PALA), which captures long-range dependencies along the horizontal and vertical page axes while remaining computationally efficient. Extensive experiments demonstrate that DocLayout-YOLO achieves state-of-the-art performance on four heterogeneous document benchmarks, obtaining 72.4%/75.5%/96.0%/73.1% mAP50:95 on D4LA, M6Doc, HJDataset, and PRIMA-LAD, respectively. Compared with existing real-time detectors, DocLayout-YOLO establishes a superior accuracy-efficiency trade-off in document layout analysis. Code, model, and data are available at this https URL.

---


### 225. [Coincidence-Maximizing Customer Clustering Using Smart Meter Data](https://arxiv.org/abs/2610.28178)

**<font color=#1a73e8>作者：</font>** Ramiro H. Gálvez, Gabriel Martos Venturini, Iván Mondrzak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electricity distribution planning depends on peak-demand coincidence within customer groups, yet similarity-based clustering of smart-meter data does not optimize it directly. We formulate customer grouping to maximize the average of group coincidence factors, weighted by each group's daily share of summed individual peak demand. We prove that jointly optimizing memberships and group peak times is strongly NP-hard even for two groups. We therefore develop a fixed-peak refinement procedure applicable to any feasible partition. It alternates between identifying group peak times and exactly reassigning customers under minimum group-size constraints. Each polynomial-time reassignment maximizes a lower bound tight at the current partition, so accepted updates strictly improve weighted coincidence. We initialize refinement by clustering individual peak-time distributions and evaluate the method on four public smart-meter panels (27,654 customers) using chronological holdouts and 200 paired replicates with complete refitting. Refinement consistently improves weighted coincidence during fitting and reduces sensitivity to initialization. On held-out days, the method outperforms random grouping and five standalone benchmarks, with mean paired gains of 1.08-3.48 percentage points over the strongest benchmark. Requiring nearly equal group sizes lowers test weighted coincidence only modestly. The groups retain recognizable peak-time patterns over time, suggesting applications in peak-aware customer aggregation.

---


### 226. [CrossFit-GS: Out-of-Fold Pose Estimation for COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2610.28190)

**<font color=#1a73e8>作者：</font>** Zijian Wu, Jinliang Wang, Mingfeng Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose-free 3D Gaussian Splatting (3DGS) aims to bypass cumbersome Structure-from-Motion (SfM) by directly reconstructing scenes from unposed image sequences. In this work, we present CrossFit-GS, a deferred-commitment progressive framework that mitigates cumulative trajectory drift and breaks the self-reinforcing loop of distorted-map error propagation. Specifically, we partition the input sequence into interleaved subsets and maintain two complementary submaps. Each candidate pose is cross-refined against a frozen opposite submap that has never been optimized using the target frame, thereby providing an independent geometric reference for pose estimation. Checkerboard validation and spatial coverage safeguards further reject unreliable updates, and only verified poses are committed to their corresponding owner submap. Once the trajectory has been refined, the intermediate submaps are discarded and the final global representation is trained from scratch using the fixed refined poses. Extensive evaluations across multiple benchmarks demonstrate that CrossFit-GS substantially reduces cumulative trajectory drift and consistently improves both camera pose estimation and novel-view synthesis over existing methods.

---


### 227. [Unified RAW Image Exposure Correction and Restoration via Linear Illumination and Frequency-Adaptive Enhancement](https://arxiv.org/abs/2610.28191)

**<font color=#1a73e8>作者：</font>** Yingkai Zhang, Yunhao Zou, Ying Fu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incorrect exposure degrades both image brightness and recoverable scene detail. Existing sRGB-based correction methods are limited by the non-linear image signal processing pipeline, whereas RAW-based methods are usually developed for a single degradation type, such as low-light denoising or high-light recovery. In this paper, we focus on joint exposure correction and restoration directly in the RAW domain and propose a unified RAW Image Exposure Correction and Restoration (RIECR) framework for both under- and over-exposed images. RIECR decomposes the problem into two coupled sub-problems that follow the RAW imaging model: linear illumination correction and residual degradation restoration. First, a Linear Illumination Correction Network (LICN) estimates exposure-aware linear gains by using channel-specific RAW cues. It exploits the high signal-to-noise ratio of Green channels for robust brightening and the relatively unsaturated Red/Blue responses for high-light darkening. Second, a dual-branch Frequency-based Enhancement Network (FEN) restores the remaining degradation with a Frequency Dynamic Convolution (FDC) module. FDC decomposes convolutional responses into low- and high-frequency components and adaptively suppresses amplified noise or recovers clipped textures according to the exposure context. We further build a real paired RAW benchmark containing 223 scenes and 1,784 pairs covering complex multi-exposure errors. Experiments against sixteen state-of-the-art methods show that RIECR achieves state-of-the-art performance on real RAW exposure correction.

---


### 228. [Attractive Faces Skew Text-to-Image Reward Models and Leaderboards](https://arxiv.org/abs/2610.28195)

**<font color=#1a73e8>作者：</font>** Harvey Mannering, Zhiwu Huang, Adam Prügel-Bennett  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human preference is now central to the evaluation, guidance, finetuning, and ranking of text-to-image models. However, the susceptibility of human preferences to bias in image generation remains underexplored. We identify a key observation: for human faces, perceived attractiveness overrides image quality in preference judgments, even when comparing real photographs of identical fidelity. In a controlled user study, annotators rank more attractive faces as higher quality, even when unattractive real faces are compared with attractive AI-generated ones. We examine the downstream consequences of this bias. Firstly, simulating Elo rankings from user study data shows attractiveness can invert a leaderboard's ranking, elevating synthetic attractive faces over real, unattractive ones. Secondly, the same bias reappears in the human preference models. Editing 40 annotated facial attributes in isolation, we find that attractiveness is the strongest correlate of score for four of five human preference models (PickScore, MPS, HPSv2.1, HPSv3), and the strongest predictor of score in regression analysis. We further show that preference aligned generation shifts faces toward younger, more feminine faces, and can override explicit prompts for unattractive faces, thereby limiting user control. Finally, we explore mitigation strategies, both for data collection and post training on human preference models. These findings highlight the need for preference models that disentangle image quality from human cognitive bias, enabling more reliable evaluation.

---


### 229. [Reframing Object-Centric Reinforcement Learning: From Absolute to Relative Representations](https://arxiv.org/abs/2610.28197)

**<font color=#1a73e8>作者：</font>** Cedric Derstroff, Jannis Blüml, Janosch Moos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Object-centric reinforcement learning agents typically receive each object's position in a fixed global frame, even though their decisions usually depend on where objects are relative to one another. These absolute views often fail to capture the local context that is most relevant to the agent's behavior. As a result, an agent must relearn the same response at every location where a configuration can occur, and its performance collapses when the scene is merely shifted. In this work, we propose a shift toward Object-Relative Coordinates fixed to Anchor (ORCA), where entities are described in a relative frame of reference. To operationalize this idea, we introduce Object-Relative inductive-Bias Transformers (ORBiT), a transformer-based architecture for processing anchor-relative inputs in reinforcement learning. Our results suggest these relative representations improve performance for both MLP and transformer agents. Furthermore, we demonstrate that ORBiT outperforms the pixel-based PPO baseline, achieving an aggregate HNS IQM greater than 1.0 over 13 Atari games. ORBiT learns the game of Foosball from scratch, dominating all baselines. In our controlled Tag environment, we further show that ORCA extends to rotations, that ORBiT generalizes to unseen numbers of distractors, and that these gains require a decision-relevant anchor.

---


### 230. [JAXbounce: A Continuous-Control Pong-Like Benchmark for Active Inference Beyond Low Dimensional Environments](https://arxiv.org/abs/2610.28203)

**<font color=#1a73e8>作者：</font>** Chaitanya Kaul, Markus Klar, Sebastian Stein 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce JAXbounce, a continuous control pong-like benchmark designed to evaluate active inference beyond discrete, low dimensional environments. JAXbounce combines continuous states and stochastic dynamics in discrete time with flexible and composable observation models that allow representing the environment as a state vector or a pixel grid, corruptible through the rich family of noise models we provide. It is fully differentiable and parallelisable in JAX. We run over 10,000 agent simulations on our environment comparing a baseline deterministic solution, to a state-based active inference agent with Unscented Kalman Filter perception and expected free energy planning, and a pixel based agent whose measurement model is a pretrained neural network encoder. All agents are evaluated across three scenarios of increasing difficulty with eight different noise conditions. Our experiments characterise how performance of continuous state agents scales with planning, planning horizons, observation modalities and knowledge of the noise process, exhibiting preference-oriented behaviour even in the presence of increasing uncertainty. We release JAXbounce as a reproducible benchmark for continuous control active inference research.

---


### 231. [SplatFlux: Feed-Forward 4D Gaussian Reconstruction and Generation from Video Latents](https://arxiv.org/abs/2610.28257)

**<font color=#1a73e8>作者：</font>** Runmin Zhang, Binglin Ren, Zhu Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents SplatFlux, a feed-forward latent-to-4DGS framework for both video-based 4D reconstruction and conditional 4D generation. Our key observation is that observed videos and conditionally generated content can be represented in the same pretrained video latent space, allowing both tasks to be formulated as latent-to-4DGS decoding. To construct compact and temporally coherent 4D scenes, SplatFlux introduces a static-dynamic decoupled 4D Gaussian representation that explicitly predicts dynamic probabilities for Gaussian primitives. This representation separates static scene structures from moving regions, enabling complete 4D scene construction in a feed-forward manner through static aggregation and dynamic motion interpolation. To learn static-dynamic decomposition and dynamic Gaussian motion without costly annotations, we further develop an auxiliary distillation strategy that provides pseudo dynamic masks and optical-flow cues. Extensive experiments across 3D and 4D reconstruction and generation demonstrate that SplatFlux achieves state-of-the-art performance.

---


### 232. [Reliability-Aware Reconstruction of V-Shaped Surfaces with a Low-Cost Multi-Zone SPAD Sensor](https://arxiv.org/abs/2610.28258)

**<font color=#1a73e8>作者：</font>** Yohanssen Pratama  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-cost multi-zone single-photon avalanche diode (SPAD) sensors provide compact time-of-flight measurements but are limited by sparse sampling and unreliable depth estimates near geometric discontinuities. This letter presents a reliability-aware reconstruction framework for V-shaped surfaces using two complementary TMF8821 acquisition configurations. Point-wise reliability is learned from sensor confidence, transient peak amplitude, and peak sharpness, and is incorporated into a graph-based depth optimization. The reconstructed geometry is evaluated by robust two-plane fitting and a perpendicular cross-section. Experiments on 60-degree, 90-degree, and 120-degree targets reduce the mean V-angle error from 11.21 degrees to 9.66 degrees (13.8%). For the representative 90-degree target, the combined point-to-plane RMSE decreases from 14.56 mm to 13.65 mm.

---


### 233. [HRoPE: Homography Relative Positional Encoding](https://arxiv.org/abs/2610.28284)

**<font color=#1a73e8>作者：</font>** Huachen Gao, Yang Yang, Xiaoqian Liang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric Relative Positional Encoding has become the primary mechanism for injecting spatial inductive biases into multi-view transformers. Existing designs condition attention on camera-level frustums or ray-marched depth, associating cross-view tokens through the sensor geometry. Such sensor-centric formulations, however, describe only where a token is observed from, leaving the rich surface geometry of the scene region depicted by the token. In this paper, we advocate a shift toward surface-aware positional encoding that explicitly grounds patch tokens in the geometry of physical surfaces. We introduce HRoPE, which represents the local geometry of each patch as a slanted 3D plane, following the slanted support-window assumption of classical multi-view stereo. We inject token-level, plane-induced homographies into attention as relative transformations. This equips the transformer with a geometric prior for rectifying perspective distortions and aligning patch features across viewpoints. Our encoding requires no ground-truth geometry: the plane parameters can be predicted end-to-end under a view-synthesis objective alone, or derived from foundation models. Extensive experiments on RealEstate10K, CO3Dv2, and DL3DV show that our best variant of HRoPE consistently outperforms the evaluated geometric positional encodings for novel view synthesis. Extensive ablations and analysis show the effectiveness of the proposed encoding. Please refer to our project page at: this https URL

---


### 234. [CPVB-RG: Cross-Prior Visual Bridging for Prior-Aware Chest X-Ray Report Generation](https://arxiv.org/abs/2610.28289)

**<font color=#1a73e8>作者：</font>** Sike Xiang, Shuang Chen, Julie Cox 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiologists interpret follow-up chest X-rays by comparing current and prior examinations to identify new, resolved or progressing findings. Most report generation systems either omit this longitudinal context or fuse prior features without distinguishing interval changes from anatomy that remains stable over time. We propose CPVB-RG, a prior-aware framework that combines current and prior radiographs with available clinical text. Its Cross-Prior Visual Bridge (CPVB) contains Progression-Guided Focus Attention (PGFA) and two Cross-Attention units. PGFA is designed to contrast progression-difference attention with shared-spatial attention, aiming to reduce invariant responses whilst retaining coarse spatial correspondence between examinations. The Cross-Attention units then connect the resulting longitudinal visual evidence with clinical semantics. CPVB-RG is trained in two stages, using prior-guided image-text alignment followed by autoregressive report generation with a lightweight language decoder. Experiments on MIMIC-CXR and IU X-Ray show consistent improvements across language and clinical metrics. On MIMIC-CXR, CPVB-RG achieves 0.2847 F1RadGraph and 0.6692 VLScore, with statistically significant gains over the closest decoder-matched prior-aware baseline. These results support the effectiveness of the proposed difference-aware and spatially guided fusion design for prior-aware chest X-ray report generation.

---


### 235. [AGGR-Mamba: Mamba-based Network with Attention-Guided Gated Residual Refinement for Undersampled MRI Reconstruction](https://arxiv.org/abs/2610.28291)

**<font color=#1a73e8>作者：</font>** Yue Zhuo, Wenbin Deng, Lingjun Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Undersampled magnetic resonance imaging (MRI) reconstruction aims to recover high-quality images from partially acquired k-space data, thereby reducing scan time. However, missing frequency-domain measurements often lead to residual aliasing artifacts, blurred edges, and loss of local structural details. In this paper, we propose AGGR-Mamba, a lightweight output-stage residual refinement method built upon a Mamba backbone for undersampled brain MRI reconstruction. The Mamba backbone first produces an initial reconstruction, and the proposed refinement modules then correct the remaining local errors and high-frequency artifacts in a controlled residual manner. Specifically, an Attention Refine Head is introduced to recalibrate local anatomical structures, edge textures, and residual-error regions through channel and spatial attention. In addition, a GDFN-style gated residual refinement branch is designed to selectively preserve informative residual features while suppressing redundant or unstable responses. By combining attention-based recalibration with gated residual selection, AGGR-Mamba improves local structure recovery without substantially disturbing the backbone reconstruction. Experiments are conducted on the IXI brain MRI dataset with T1- and T2-weighted images under acceleration factors of R=4 and R=8. The results show that AGGR-Mamba achieves competitive PSNR and SSIM performance across different reconstruction settings, demonstrating the effectiveness of the proposed output-stage refinement strategy.

---


### 236. [Learning Normal Coordinates on Riemannian Manifolds with Flow Charts](https://arxiv.org/abs/2610.28302)

**<font color=#1a73e8>作者：</font>** Edmond Cunningham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Riemannian manifolds are powerful models for problems with non-Euclidean structure. Recent work in geometric machine learning has focused on training deep neural networks to learn Riemannian metrics from high-dimensional data. However, many geometric algorithms require repeated evaluations of the exponential and logarithmic maps, whose high computational cost restricts the utility of learned Riemannian manifolds in practice. We propose to address this cost by training a conditional invertible neural network, called a flow chart, to approximate normal coordinates around points on a given Riemannian manifold. With this approach, the exponential and logarithmic maps can be approximated by fast Euclidean operations in the model's learned coordinate space. Our main contribution is an efficient loss function for training flow charts that is nonnegative and, under suitable domain assumptions, is zero precisely when the chart is normal. Across sixteen synthetic and data-derived geometries, flow charts are competitive with a specialized neural geodesic interpolator for logarithmic map estimation, while also being able to estimate the exponential map. When pretrained, flow charts provide a median speedup of 60-70x over numerical baselines at comparable logarithmic map estimation error, and their learned coordinates improve the accuracy of a numerical geodesic solver.

---


### 237. [Recommending Bacterial Cultivation Conditions from 16S rRNA](https://arxiv.org/abs/2610.28310)

**<font color=#1a73e8>作者：</font>** Juntang Wang, Hao Wu, Yihan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recommending bacterial cultivation conditions from sequence data is a challenging structured problem characterized by missing standardized benchmarks and limited use of sequence structure. To address this, we introduce DSNI, a benchmark of 65,023 bacterial strains with phylogeny-aware splits, pairing 16S rRNA sequences with four cultivation conditions (media, temperature, pH, oxygen). Exploiting the mosaic structure of 16S rRNA, where hypervariable regions support discrimination and conserved regions support primer design, we propose a Variability-Gated Encoder that learns position-dependent importance weights conditioned on biological features (region type, position, and local complexity). The gating module adds minimal overhead (1,280 parameters, <1%) while providing an explicit inductive bias valuable in low-data regimes. Experiments demonstrate that the learnable gate improves flat Transformers by 4.7% in joint accuracy and complements RNABERT, yielding 44.2% exact-match joint accuracy. The model also recovers 90.2% of ground-truth cultivation protocols within its top-25 recommendations, narrowing the exhaustive search space by approximately 60 times.

---


### 238. [Manifold-Informed Neural Networks for Low-Label ECG Electrolyte Inference](https://arxiv.org/abs/2610.28322)

**<font color=#1a73e8>作者：</font>** Juntang Wang, Hao Wu, Yihan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) supervise on the residual of a known differential operator. Many high-stakes inference problems admit no such operator: clinical signals, behavioral measurements, materials properties. We introduce the Manifold-Informed Neural Network (MINN), a PINN-parallel paradigm that replaces the physics operator residual with a manifold operator residual: a discrete Poisson equation $\mathbf{L}_G \mathbf{H} = s_\phi(\mathbf{x}, \mathbf{m})$ on a $k$-nearest-neighbor graph in the learned latent space, with a learned, task-aware source. The construction is a structural parallel to PINNs (squared operator residual plus label data, in place of operator residual plus boundary data); the $s{=}0$ limit recovers the homogeneous Laplace equation $\mathbf{L}_G\mathbf{H}=\mathbf{0}$ (classical manifold regularization solves the same equation but minimizes the Dirichlet energy $\operatorname{tr}(\mathbf{H}^\top\mathbf{L}_G\mathbf{H})$, a different penalty form). The source $s_\phi$ takes input features and auxiliary metadata directly, breaking the homogeneous smoothness prior that limits classical Laplacian penalties; gated Feature-wise Linear Modulation separately fuses metadata into the prediction branch. We evaluate MINN on three-class classification of potassium, calcium, and magnesium from 12-lead ECGs in MIMIC-IV-ECG, against twelve baselines spanning supervised and tabular methods, ECG foundation models, and manifold/graph approaches. MINN attains the highest K$^+$ Macro-F1 of 0.61 (best baseline 0.55), with consistent gains on Ca$^{2+}$ and Mg$^{2+}$ and a 31% relative improvement at 1% labeled data. Six targeted ablations show that the inhomogeneous Poisson formulation, not graph smoothing alone, drives the gain.

---


### 239. [Observation Assimilation Transformer: Probabilistic Weather Analysis from Sparse Station Observations](https://arxiv.org/abs/2610.28327)

**<font color=#1a73e8>作者：</font>** Christian Donner, Michele Cattaneo, Maxim Samarin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present the Observation Assimilation Transformer (OAT), a geometry-aware neural process that corrects and refines a prior numerical weather prediction (NWP) field into a high-resolution posterior field by assimilating sparse observations. OAT is an encoder-decoder transformer that considers a set of observed locations and their NWP prior to condition predictions at a set of arbitrary unobserved query locations. Its sparse attention mechanism makes it scalable to thousands of station observations and depends on relative positions between locations, never on the absolute coordinates. The model allows for partially missing observations, predictions at arbitrary continuous locations without grid projection, and outputs are parametric distributions. A station-randomized training algorithm is developed with continuous ranked probability score (CRPS) loss. We test OAT on two datasets - one at regional scale with hundreds of stations, and one at continental scale with thousands of stations. On these datasets OAT outperforms several baselines and shows well calibrated predictions. In an illustrative case study, OAT's downscaling capabilities are demonstrated by downscaling ERA5 (~31km) to COSMO (1km), where OAT achieves lower mean absolute error (MAE) and CRPS for temperature and precipitation on test stations compared to COSMO.

---


### 240. [Identifying Dependent Components from Multi-domain Linear Mixtures](https://arxiv.org/abs/2610.28330)

**<font color=#1a73e8>作者：</font>** Danru Xu, Lauri Parkkonen, Sara Magliacane 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a linear mixing model with dependent latent components, assuming multiple data domains. Most existing models assume that the components are independent or at least uncorrelated, in line with independent component analysis (ICA). Some recent work allows for dependent components, but then makes specific assumptions such as parametric forms of dependencies, multi-view settings, or interventions, or does not recover the individual components. In contrast, we consider a multi-domain setting in which domains differ through domain-specific scalings of the components, while the distribution of the underlying latent components is the same across domains. This approach can model data collected, for example, from different sensors measuring the same process, different laboratories conducting the same experiment, different experimental conditions, or different subjects that might differ in biological or physiological factors. We show that, under sufficient domain variability, latent variables and mixing functions can be identified from second-order statistics alone. We propose the Multi-Domain Covariance Matching (MuDo-CoM) algorithm that generalizes previous methods of joint diagonalization. MuDo-CoM is validated on simulated data and a real-world fMRI dataset.

---


### 241. [Beyond a Single Sentiment Score: Topical and Affective Dimensions of Emoji Meaning on Twitter](https://arxiv.org/abs/2610.28337)

**<font color=#1a73e8>作者：</font>** Rohan James, Ioannis Christofilogiannis, Yuuv Jauhari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emoji are widely treated as compact affective tokens whose meaning is summarised by a single sentiment score. We argue that this picture is incomplete. From a corpus of 16{,}575 English tweets and a per-emoji metric we call \emph{stability delta} (within-class minus between-class cosine similarity of sentence embeddings), we show that emojis used in tightly clustered topical contexts also exhibit \emph{more} polarised crowd-sourced sentiment, not less. Validated against the Kralj Novak et al.\ (2015) sentiment lexicon, the central correlation is Spearman $\rho = +0.361$ (Holm $p = 0.015$, 95\% bootstrap CI $[+0.10, +0.59]$); against the independent Ferré et al.\ (2025) Spanish 13-emotion ratings, $\rho = +0.509$ ($p = 0.0003$). The result survives permutation testing, BCa bootstrap, leave-one-out jackknife, partial correlation controlling for emoji frequency, and Holm correction across a four-test family. Topical coherence and affective dispersion are distinct dimensions of emoji meaning. As a downstream check we report leakage-free five-fold cross-validation results for sarcasm classification on the Emoji Sarcasm Dataset; all three baselines (a gated multimodal architecture, fine-tuned BERTweet features, and fine-tuned RoBERTa features) score above 0.97 macro F1, indicating the dataset has saturating emoji-label cues. We frame the classifier as supporting evidence rather than the contribution.

---


### 242. [HistoLoop: Iterative Contextual Inference with a Looped Transformer for Histology-Based Spatial Gene Expression Prediction](https://arxiv.org/abs/2610.28339)

**<font color=#1a73e8>作者：</font>** Ziang Liu, Jie Liu, Shuai Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting spatial gene expression from H&E images offers a scalable complement to experimental spatial transcriptomics. However, despite progress in spatial context modeling, how to construct subsequent context from spot states updated by earlier contextual interactions remains underexplored. We introduce HistoLoop, a looped Transformer that formulates prediction as iterative contextual inference. At each refinement step, HistoLoop aggregates the current spot states into context tokens at the corresponding resolution, processes them with a shared spatial Transformer, and retrieves spot-specific contextual information through cross-attention. A memory-mediated update integrates this information into persistent spot states, which are then used to construct context at the next, finer resolution. Under the HEST-Bench HVG50 evaluation protocol, HistoLoop achieves the highest macro-averaged gene-wise Pearson correlation among the compared methods across six cancer-specific tasks spanning five organs in HEST-1K. Ablation studies support the importance of recurrent state refinement and reconstructing context from updated spot states at progressively finer resolutions. Expression-derived clustering further suggests that HistoLoop better captures spatially organized multigene patterns.

---


### 243. [The GenAI Who Knew Too Little: Revisiting Transactive Memory Systems in Human GenAI Collaboration](https://arxiv.org/abs/2610.28343)

**<font color=#1a73e8>作者：</font>** Christian Meske, Tobias Hermanns, Florian Brachten  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (GenAI) is rapidly transforming knowledge work, creating new collaborative dynamics that challenge tradi-tional human-human interaction patterns. This study investigates how Transactive Memory Systems (TMS) manifest in human-GenAI collabora-tion. Through qualitative interpretive interviews with 14 knowledge work-ers and thematic analysis, we identified distinct TMS manifestations across its three main dimensions: (1) regarding specialization, expertise recogni-tion exhibited asymmetry. Humans developed awareness of GenAI capabili-ties while GenAI demonstrated only temporary recognition of human exper-tise; (2) in terms of credibility, humans formed ambivalent trust relation-ships with GenAI, simultaneously attributing expertise to the latter while implementing additional verification processes; and (3) concerning coor-dination, where humans primarily directed more passive GenAI systems lacking initiative, resulting in hierarchical interaction patterns and unidi-rectional information flow. Our findings reveal that TMS manifests differ-ently in human-GenAI compared to human-human collaboration, necessitat-ing theoretical adaptations including trust markers, acknowledging GenAI's absent metamemory, and identifying its temporary memory.

---


### 244. [Characterizing Cross-Relay Generalization Failure in Machine Learning-Based Power System Protection](https://arxiv.org/abs/2610.28348)

**<font color=#1a73e8>作者：</font>** Nithin Pradeep Nadayil Kizhakkethil, Julian Oelhaf, Christian Bergler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning-based fault detectors are often evaluated at the relay locations used for training, although local voltage and current measurements vary across power networks. This work investigates cross-relay generalization for binary detection of faults anywhere in the network using local measurements, rather than line-selective tripping. Using 50 ms windows from a simulated 110 kV transmission network, we evaluate a multilayer perceptron across all 64 source target combinations of eight relays and five random seeds. A shared simulation-level split and source-only threshold selection provide a controlled held-out evaluation without target-specific calibration. Despite nearly unchanged mean F1-scores (0.730 within-relay versus 0.734 cross-relay), the mean false-positive rate (FPR) increases from 0.088 to 0.341, while the mean false-negative rate decreases from 0.399 to 0.318. The change is strongly directional: models trained at Bus 2 relays yield a mean FPR of 0.670 at Bus 1 and Bus 3 relays, compared with 0.096 for cross-relay transfers within the same bus group. Linear probing indicates that learned representations retain coarse bus-group information, while exploratory class-conditional latent distribution analysis shows no consistent monotonic association with transfer errors. These findings demonstrate that aggregate metrics can conceal location-structured changes in false-alarm behavior, highlighting the importance of evaluating error types separately when assessing cross-relay generalization.

---


### 245. [RayCo4D: Ray-Conditioned Continuous Motion Model for Monocular 4D Dynamic Reconstruction](https://arxiv.org/abs/2610.28351)

**<font color=#1a73e8>作者：</font>** Yuanxiang Ni, Xianliang Huang, Ruihan Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic 3D scenes from monocular video requires inferring motion from noisy and intermittently visible observations. Long-range tracks provide valuable geometric constraints, but integrating their fragmented temporal coverage into shared, continuous motion remains challenging. We introduce \textbf{RayCo4D}, a ray-conditioned continuous motion model for monocular 4D reconstruction that explicitly separates visual measurements from latent 3D motion states. Each track is associated with a reference-time 3D query constrained to its camera ray, and its image and depth observations constrain shared latent motion nodes through local many-to-many associations. Each node maintains an $\mathrm{SE}(3)$ pose and body-frame velocity at sparse support times. A white-noise-on-acceleration process prior couples neighboring states and defines continuous-time interpolation, allowing observations across visibility intervals to jointly constrain the same latent state this http URL inferred shared motion is transferred to Gaussian primitives through dual-quaternion blending, while reference-anchored local $\mathrm{SE}(3)$ residuals capture fine-scale non-rigid deformation beyond the shared scaffold. Experiments on diverse monocular dynamic scenes show that RayCo4D achieves competitive novel-view synthesis quality, improves structural and temporal consistency under rapid motion and incomplete tracks, and supports continuous-time rendering.

---


### 246. [SPECTER: Covert Data Exfiltration from Air-Gapped Systems via USB Power Modulation](https://arxiv.org/abs/2610.28401)

**<font color=#1a73e8>作者：</font>** Hyeongjun Choi, Ji Hyuk Jung, Ji Won Yoon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present SPECTER, a post-compromise covert channel that uses host-side USB power control to exfiltrate information from air-gapped and network-segregated systems. A transmitter with administrative privileges encodes bits through USB power-management or device-state operations without placing the payload in USB data transfers. The resulting signals are recovered through three alternative receiver paths based on smartphone charging states, visible peripheral behavior, and near-field RF activity. Experiments on Windows 10 and Ubuntu 22.04 demonstrate the channel on commodity hardware, with charging-state signaling at 0.2-0.25 bit/sec across Android and iOS devices and peripheral-state signaling at 1.0 bit/sec using a USB mouse on Windows. RF reception is demonstrated using a software-defined radio with a loop antenna in direct contact with the USB cable. Channel availability and observable side effects depend on the host configuration, connected device, and receiver path. These results identify host-side USB power control as a mechanism for low-rate exfiltration of short secrets and motivate treating USB power-management and device-state events as security-relevant telemetry.

---


### 247. [StreamEval: Evaluating Interactive Streaming Video Generation Models](https://arxiv.org/abs/2610.28402)

**<font color=#1a73e8>作者：</font>** StreamEval Team  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As streaming video generation advances, enabling real-time interaction with generated video is becoming increasingly important. We introduce StreamEval, a unified benchmark for interactive streaming video generation spanning five tasks: avatar dialogue, avatar performance, world generation, instruction editing, and reference editing. StreamEval comprises 300 scripted test cases lasting 15-300s, each specifying initial assets, incrementally arriving multimodal requests, and explicit requirements for state changes and content preservation. Performance is assessed along four evaluation dimensions: task execution, state consistency, visual fidelity, and audiovisual coordination, instantiated through ten task-specific metrics on a 0-100 scale. Evaluating 37 distinct models across 300 test cases, we find that high visual quality and identity retention do not necessarily coincide with reliable request execution or sustained state consistency. In particular, request execution remains challenging: the highest task-specific scores are 36.90 for Following among seven avatar-performance models, 25.93 for Following in text-conditioned world generation, and 15.00 for Edit Success among three reported reference-editing models. These findings identify reliable request execution under timing and preservation constraints as a central challenge for advancing omni-modal real-time interactive systems. The leaderboard is available at this https URL

---


### 248. [WorldSR: Harnessing World Knowledge Search for Grounded Image Super-Resolution](https://arxiv.org/abs/2610.28423)

**<font color=#1a73e8>作者：</font>** Junyuan Deng, Xinyi Wu, Zhenyao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative-prior-based super-resolution (SR) methods leverage implicit knowledge learned from large-scale models to enhance low-resolution inputs. However, such priors are inherently stochastic and optimized for diverse generation, conflicting with the deterministic, high-fidelity reconstruction required for SR. It is also tied to the base model, costly to update, and prone to hallucinations as real-world data evolves. To address these limitations, we introduce WorldSR, a novel framework that augments SR with explicit, entity-aligned visual world knowledge. WorldSR automatically decomposes the input into semantic entities and performs entity-wise retrieval of structurally and semantically aligned images from a large-scale external corpus. For efficiency and reliability, we incorporate a memory mechanism to reuse previously retrieved results and a multi-step filtering process to refine candidate references. The selected references as world knowledge are then integrated through a novel multi-reference super-resolution model, which provides fine-grained constraints for detail synthesis and structural recovery. Experiments on real-world SR benchmarks show that WorldSR consistently improves structural fidelity and visual quality, outperforming existing generative super-resolution methods. Our results suggest that entity-level grounding in external visual world knowledge provides a simple and effective complement to model-bound generative priors.

---


### 249. [Region-Specific EEG Classification of Hypnotic Susceptibility Using a Sliding-Window 2D CNN: A Subject-Independent Evaluation](https://arxiv.org/abs/2610.28427)

**<font color=#1a73e8>作者：</font>** Krzysztof Wrobel, Grzegorz M. Wojcik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether a 2D Convolutional Neural Network (CNN) trained on minimally preprocessed EEG signals can classify hypnotic susceptibility across distinct brain regions. Sixty-two male participants (32 Control, 30 Guided Imagery / Hipno group) underwent a 20-minute EEG recording using a 256-channel EGI cap. A sliding-window approach evaluates all 10-second windows within the recording for each of seven predefined brain regions (prefrontal, frontal, temporal, central, parietal, occipital, and facial), yielding up to 868 independently trained models. Initial screening with a segment-level 90/10 random split showed that five regions exceeded the 0.67 accuracy threshold, with the occipital region achieving the highest mean accuracy (0.721) across 90.3% of windows. Subject-independent evaluation via Leave-One-Subject-Out (LOSO) cross-validation, however, substantially revised this picture: occipital performance collapsed to near-chance (mean ACC 0.453, AUC 0.429), revealing that high random-split accuracy was driven by subject-specific EEG fingerprints rather than genuine group differences. In contrast, the frontal and prefrontal regions maintained above-chance LOSO accuracy (0.646 and 0.624, respectively), demonstrating genuine generalisability. These results underscore the necessity of subject-independent validation in EEG-based classification studies and highlight anterior cortical regions as more reliable neural markers of hypnotic susceptibility.

---


### 250. [Do Neural Models Prefer Their Submodels?](https://arxiv.org/abs/2610.28439)

**<font color=#1a73e8>作者：</font>** Alvaro Ribot, Yulia Alexandr, Anna Seigal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A neural model is the set of functions that can be expressed by a given neural network architecture. Neural models contain natural submodels, such as those obtained by setting some neurons to be inactive. We study the geometry of neural models and ask whether they prefer their submodels. By this we mean whether local minimizers of the loss function lie in a given submodel. We introduce a geometric framework to determine if this occurs. For shallow multilayer perceptrons, we show that subnetworks with inactive hidden neurons are never preferred. For deep multilayer perceptrons, we give conditions under which subnetworks with inactive hidden neurons are not preferred. For lightning self-attention, lower-rank submodels are usually not preferred, but we identify examples where they are because they lie on a boundary of the model. Our results show that, aside from a few exceptions, preference for submodels cannot be explained by the geometry of the neural model, and must instead come from other sources such as training dynamics.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-288](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
