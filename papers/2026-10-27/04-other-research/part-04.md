# 📦 其他研究 | 2026年10月27日

> 本类共 **198** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-198**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-198**

---

### 151. [AquaSense-ICS: A Hybrid Real-Simulated Cyber-Physical Dataset and Leakage-Aware Benchmark for Smart Water Quality Monitoring and Attack Detection](https://arxiv.org/abs/2610.32661)

**<font color=#1a73e8>作者：</font>** Amal Neji, Mohamed Fourati, Lamia Chaari Fourati  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine-learning research on water cyber-physical systems (CPS) is constrained by datasets that are either real but chemically poor, or simulated but free of sensing noise and attacks. We present AquaSense-ICS, an open dataset and benchmark that co-registers (i) a 25.4 h recording window (8.0 h of recorded data, 26% coverage) from a Raspberry Pi 5 edge node (TDS probe and BME680 ambient sensor, 1-2 s sampling, 23,688 records), with (ii) a looped network of 13 nodes (10 junctions, 2 reservoirs, 1 tank) simulated in EPANET-MSX for six water-quality species, (iii) a parameterised library of cyber-attacks (false data injection, replay, denial of service, drift) and unintentional sensor faults with sample-level ground truth, and (iv) augmented and TimeGAN-generated sequences, flagged by an origin column. The attack, fault and water-quality labels are traceable to a seeded generator, a documented rule or a simulation input. We show that the most common way of benchmarking such hybrid data, random row splits and labels computed from the input features, yields near-perfect but uninformative scores (macro-F1 = 0.9998 for Random Forest), and we replace it with a leakage-aware protocol using chronological splits and held-out attack types rather than label reconstruction. Under this protocol, no model exceeds the constant "normal" predictor for attack classification (macro-F1 = 0.465), and the best detectors reach a mean AUROC of 0.64 on attack types unseen during training (0.35-0.93 depending on the type), leaving substantial headroom. Data and simulation files are released under CC BY 4.0 at this https URL, and attack generators and benchmark code under MIT.

---


### 152. [SemGeo-Gen: Unsupervised Generation of Approximate Cross-Instance Semantic-Geometric Correspondences](https://arxiv.org/abs/2610.32663)

**<font color=#1a73e8>作者：</font>** Roy Amoyal, Shira Ifergane, Oren Freifeld  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SemGeo-Gen, an unsupervised method for generating approximate cross-instance semantic-geometric supervision from weakly aligned 3D object collections. Our goal is not to recover exact point-level correspondences, which are often ambiguous across different instances and would require expensive, impractical manual supervision at scale. Instead, we automatically produce approximate correspondences that are semantically meaningful, geometrically consistent, and diverse enough to train modern correspondence models. Given only coarse category-level rotation alignment, SemGeo-Gen lifts multi-view DINOv2 features to 3D, aligns object instances using continuous piecewise-affine registration, and prunes candidate matches using semantic consistency. The resulting 3D correspondences can be projected into rendered views, yielding scalable 3D-3D, 3D-2D, and 2D-2D supervision without manual annotation. We validate the generated correspondences against sparse human annotations from KeypointNet, obtaining 93% PCK@0.10 and 97% PCK@0.15. More importantly, we show that using the generated correspondences for synthetic pretraining improves recent state-of-the-art semantic correspondence models on SPair-71k after fine-tuning on real data, with gains of up to 5 PCK@0.10 points. Together, these results indicate that approximate semantic-geometric supervision generated from 3D assets can improve real-image correspondence learning and serve as a scalable alternative to costly manual annotation. Project page: this https URL.

---


### 153. [Retiming Robot Demonstrations with a Learned Speed Prior](https://arxiv.org/abs/2610.32676)

**<font color=#1a73e8>作者：</font>** Seungyong Moon, Deokjae Lee, Hansang Lee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The pace of a robot demonstration is often determined by the teleoperator rather than by the task itself. As a result, the same motion can appear at widely different speeds across demonstrations, and policies trained on such data may inherit operator-specific timing along with task behavior. We propose to learn a speed prior directly from large-scale demonstration data. Given a task instruction, a motion path and the images along it, it predicts a distribution over execution speed along the path, from which a chosen quantile defines a consistent clock for retiming each demonstration. Existing methods derive the acceleration signal from the very data they accelerate, so each new task costs another fit, annotation, or pair of predefined rates. A single trained speed prior instead covers every task in a corpus. We fit a speed prior on both robot teleoperation data and handheld demonstrations in which a human arm, rather than a robot arm, moves the gripper, and use it to retime robot demonstrations to the handheld pace before fine-tuning a vision-language-action policy. For execution, we pair the policy with a real-time optimal-control layer that tracks predicted action chunks under robot constraints using the predicted pace. On 120 RoboLab tasks, policies fine-tuned on our learned clocks succeed more often and move with up to half the jerk compared with policies fine-tuned on the original demonstration timing and uniformly accelerated to the same speed. On a real robot, our policy stacks cups in 3.50s, 1.72$\times$ faster than the default policy's 6.02s while succeeding as often, in 29 of 30 trials. Videos and further material are available at this https URL.

---


### 154. [Identity Amortization: Shared Resources and the Cost of Sybil Attacks](https://arxiv.org/abs/2610.32685)

**<font color=#1a73e8>作者：</font>** Homayoun Maleki, Nekane Sainz, Jon Legarda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sybil defenses commonly price identities by requiring a resource for each one. When one resource can support several identities, an adversary can pay less per identity than the defense intends. We call this identity amortization: a strict reduction in the minimum cost of provisioning identities when resources may be shared, relative to provisioning each one independently. It is a second route to the gap that a Sybil attack exploits. When influence is assigned per identity, a defense calibrated to the nominal price can overestimate the cost of a Sybil threshold by up to the number of identities one resource supports. For any resource catalogue, we give exact tests for when identity amortization occurs, where it begins, and its largest error; a sharing cap below the onset removes it. Because the tests need only prices and capacities, they apply to any defense that admits identities against a shareable resource, telling designers whether the assumed per-identity cost is paid, how wrong it can be, and which intervention restores it most cheaply for honest participants. On published phone-verification prices, per-account estimates overstate provisioning cost 1.6 to 4.3 times; Tor's raised per-address relay limit cut modeled attack cost by 8 to 72%, depending on the address-to-relay price ratio.

---


### 155. [Developing Security Metrics for Automated Compliance Checking](https://arxiv.org/abs/2610.32690)

**<font color=#1a73e8>作者：</font>** Immanuel Kunz, Nico Haas, Angelika Schneider 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To automatically check for compliance with security-related standards, prose requirements must be translated to technical properties to make them measurable. A multitude of metrics have been proposed in past literature, but they are lacking a systematic methodology for their elicitation. Without such a methodology, metrics remain inconsistent in their data models and abstraction levels, they exhibit considerable overlaps and are difficult to combine to comprehensively cover a standard's requirement. In this paper, we develop a data model for security metrics based on a systematization of compliance requirements, and we propose a methodology for their elicitation. The method is based on an ontology that enables a systematic development of metrics with a comparable degree of abstraction. We also present our initial work on an open-source effort that demonstrates that our approach also supports a collaborative development of metrics.

---


### 156. [SP-Guide: Enhancing Aerial Vision-Language Navigation with Spatial Priors](https://arxiv.org/abs/2610.32697)

**<font color=#1a73e8>作者：</font>** Haoxiang Tang, Dong Zhou, Shen Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial vision-language navigation (AVLN) requires a UAV to reach a language-described target from partial egocentric observations while reasoning over large outdoor scenes. Existing approaches typically fuse view-centered RGB observations and globally anchored history maps as generic visual embeddings, leaving cross-modal spatial alignment to be learned from sparse navigation supervision. We present SP-Guide, a transformer- based goal-prediction framework that addresses this weakness of alignment through a Spatial Prior Cross-Modal Encoder, an Instruction Enhanced Decoder, and a Goal Convergence Filter for terminal target refinement. Experiments implemented on the CityNav benchmark show that SP-Guide improves success rate over the representative baselines, with the largest gains on unseen environments. These results indicate that physically grounded spatial priors provide an effective inductive bias for robust AVLN.

---


### 157. [Agent-Based Transport Model Calibration via Online Stochastic Batch Optimization](https://arxiv.org/abs/2610.32698)

**<font color=#1a73e8>作者：</font>** Abdelkader Dib, Milos Balac  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Calibrating agent-based models (ABMs) is computationally demanding, as traditional black-box optimization typically requires hundreds or thousands of independent simulation runs. To reduce this burden, we introduce an online calibration framework that estimates parameters within a single simulation run. The approach combines black-box optimization with stochastic batch optimization, a method widely applied in machine learning but not yet explored in ABM calibration. Using MATSim as a case study, we treat each simulation iteration as a stochastic batch, enabling incremental parameter updates as agents make decisions. This online calibration paradigm allows model parameters and agent behaviors to co-evolve, achieving convergence without restarting the simulation. We demonstrate the effectiveness of our method by calibrating utility function parameters in MATSim for a large-scale transportation scenario of Switzerland. Results show that mode shares align closely with observed data within a typical simulation timeframe, confirming the feasibility and efficiency of the approach. By embedding calibration directly into the simulation loop, our method opens new possibilities for real-time, scalable, and efficient calibration of complex ABMs.

---


### 158. [Are Textual Residuals Truly Complementary? Learning Visual Complements under Semantic Superposition for Visible-Infrared Person Re-Identification](https://arxiv.org/abs/2610.32709)

**<font color=#1a73e8>作者：</font>** Xiaoyang Li, Mingming Lu, Wei Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-enhanced visible-infrared person re-identification (VI-ReID) exploits textual descriptions to compensate for appearance cues that are weak or unavailable under infrared imaging. Existing methods construct compensation from differences between modality-oriented textual representations, implicitly assuming that textual differences are visually complementary. We revisit this assumption through semantic superposition and show that dense textual residuals may entangle useful appearance variations with redundant, making direct residual fusion unreliable. We propose Superposition-Aware Residual Calibration, which transforms dense textual differences into selective and visually grounded complements. Low-Interference Sparse Residual Learning represents modality-oriented text embeddings as sparse activation strengths over a shared dictionary, selects positive strength differences, and suppresses both dictionary-level overlap and activation-weighted interference to reconstruct a compact, selectively controlled residual. Visual Complement and Counterfactual Calibration further calibrates the residual against identity-specific RGB-IR visual discrepancies, encouraging retained semantics to provide meaningful compensation while preserving the residual structure. Experiments on Tri-SYSU-MM01, Tri-RegDB, and Tri-LLCM show that SARC consistently improves the VI-ReID backbone and remains competitive with text-assisted methods. Mechanism analyses show that SARC produces more concentrated textual variations, reduces dictionary-level feature interference, and improves residual-visual-complement alignment for most samples. These results demonstrate that effective cross-modal compensation requires textual residuals to be selectively represented and explicitly calibrated, rather than directly treated as visual complements. Code and implementation details will be released upon publication.

---


### 159. [PlayerEmbed: Learning Behavioral Fingerprint Representations from Raw Input Sequences](https://arxiv.org/abs/2610.32727)

**<font color=#1a73e8>作者：</font>** Tobias Schneider, Lorenz Sparrenberg, Priya Tomar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Raw player input sequences in video games contain fine-grained behavior, but are high-dimensional and noisy, which makes large-scale analytics challenging. To address this, we introduce PlayerEmbed, a framework that learns compact and discriminative player embeddings using deep metric learning. Our approach uses a hybrid CNN-LSTM encoder trained on raw input sequences from 1,000 players. We evaluate the model on held-out sequences from these players and on sequences from 1,000 players entirely unseen during training to assess generalization to unseen identities. For player identification, a nearest-centroid classifier built from reference embeddings achieves strong performance, reaching balanced accuracies of 0.950 for players seen during training and 0.879 for players unseen during training. Systematically increasing the number of training players substantially improves generalization to unseen players, indicating a transition from simple fingerprinting to learning transferable behavioral patterns.

---


### 160. [CityLift: Compositional 3D Urban Generation from a Single Image](https://arxiv.org/abs/2610.32728)

**<font color=#1a73e8>作者：</font>** Haoran Gong, Jie Feng, Chenxu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating editable 3D urban scenes from a single image requires detailed building assets with a coherent spatial arrangement. Occlusion and perspective ambiguity make it difficult to infer complete building geometry together with consistent relative scales and positions. We present CityLift, a framework that generates individual textured building meshes from an urban image by coupling scene-level spatial modeling with building-level synthesis. CityLift first learns building shape and placement jointly through coupled scene and instance streams, producing coarse sparse structures in a common coordinate system. We then introduce generative spatial inheritance, which maps each building's coarse occupancy and scene-conditioned 3D feature field into a local volume to guide a flow model that generates finer structure. The same coordinate mapping places the generated meshes back into the scene, preserving their spatial relationship to the scaffold. To address the scarcity of urban data pairing scene images with individual 3D buildings, we construct CityLift-5K, comprising 4,997 synthetic scenes with instance masks, building meshes, and placement annotations. Experiments on CityLift-5K and scene blocks from UrbanScene3D and InstanceBuilding demonstrate improved building geometry and scene composition. The project page is available at this https URL.

---


### 161. [Internal Discrepancy for Contrastive Learning: Generalization Bounds and Downstream Behaviors](https://arxiv.org/abs/2610.32729)

**<font color=#1a73e8>作者：</font>** Jialiang Wang, Qing Ma, Xiong Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive learning has emerged as a popular paradigm for training representation models. While prior studies pursue more practical and less restrictive assumptions to enhance theoretical understanding of contrastive learning, they essentially describe the interconnections among representations within the data or induced by the function class. To encapsulate these assumptions, we propose the measure of internal discrepancy that quantifies the difference between the mean representation of positive samples and latent cluster centers. We then prove an internal discrepancy-aware generalization bound for downstream supervised tasks following contrastive learning, without requiring additional assumptions. This generalization bound not only serves as a unifying framework connecting various assumptions but also motivates us to further reduce the internal discrepancy, thereby introducing the relaxed k-means loss as an approximation. Moreover, we investigate the downstream behaviors of contrastive learning from the perspective of contrastive learning-incurred supervised losses. In the presence of class imbalance, we shed light on why contrastive learning can facilitate imbalanced learning. Finally, we investigate the optimality of these incurred supervised losses, proving several intriguing properties.

---


### 162. [Cross-Architectural Feature Fusion for Coronary Artery Stenosis Detection in X-ray Angiography](https://arxiv.org/abs/2610.32730)

**<font color=#1a73e8>作者：</font>** Haobo Zhu, Mojtaba Lashgari, Jason Chai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coronary artery disease remains a leading cause of mortality, with stenosis detection from invasive X-ray Coronary Angiography (XCA) critical for diagnosis. Manual interpretation is time-consuming, subjective, and variable, especially under low contrast and vessel overlap. Existing deep learning methods often rely solely on detection or segmentation, limiting this http URL propose a hybrid framework, Fusion-YOLOv11-L, combining a YOLOv11-L detector with a pretrained UNet++ via a channel attention gating module. This enables fusion of semantic and vessel-aware structural features, improving localisation of stenotic regions. The UNet++ is pretrained on ARCADE vessel segmentation dataset to provide anatomically informed representations. Experiments on the relabeled ARCADE (ARCADE*) dataset show improved performance over YOLOv11-L, achieving AP@50 of 0.585 and F1-score of 0.596. Cross-domain evaluation on a dataset from the Oxford Acute Myocardial Infarction (OxAMI) Study reveals performance degradation due to domain shift, mitigated using test-time adaptation and augmentation. Test-time augmentation improves AP@50 from 0.434 to 0.480, indicating better generalisability. These results show that cross-architecture feature fusion and lightweight adaptation improve robustness and generalisability of automated stenosis detection in XCA.

---


### 163. [Agentic Hazard Mapper: Emulating Expert Map-Making with AI Agents for Risk Communication](https://arxiv.org/abs/2610.32738)

**<font color=#1a73e8>作者：</font>** Sidi Wu, Lifeng Lin, Yizi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hazard maps are essential tools for public risk communication, preparedness, and evacuation planning, yet effective cartographic design is not always ensured due to limited access to cartographic expertise across local governments and communities. We present Agentic Hazard Mapper, a multi-agent system that automates hazard-map production by emulating professional cartographic workflows and iterative design trade-offs while adapting design decisions to different data, locations, and hazard contexts. We conducted a formative study with map experts to inform the system design, followed by a user study and interviews with map experts and hazard practitioners. The generated maps improved participants' spatial understanding and evacuation-planning performance, reduced perceived workload and task completion time, and were generally preferred over corresponding municipal maps. We further discuss human oversight, adaptation across users and communication contexts, and opportunities to extend agentic support across broader stages of hazard-map production and risk communication.

---


### 164. [Strongly Adaptive Online Learning with Time-Varying Movement Costs](https://arxiv.org/abs/2610.32740)

**<font color=#1a73e8>作者：</font>** Andrew Jacobsen, Emmanuel Esposito, Hao Qiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study strongly adaptive regret for Online Convex Optimization (OCO) with time-varying movement costs, a setting that evaluates a learner's performance over arbitrary sub-intervals. This framework captures complex sequential decision-making problems where both the environment and the cost of switching decisions fluctuate over time. We propose a novel algorithm which, for any interval $[a,b] \subseteq [T]$, achieves a data-dependent regret bound of $ \widetilde{\mathcal{O}}\left( \sqrt{(D^2+DP_{[a,b]})\sum_{t \in [a,b]}(\|g_t\|^2+\lambda_t\|g_t\|)} \right) $, where $D$ is the diameter of the decision domain, $P_{[a,b]}$ is the path length of the comparator sequence over $[a,b]$, $g_t$ is the gradient of the loss, and $\lambda_t$ is the movement-cost coefficient at round $t$. Key to our approach is a novel reduction to sleeping experts with movement costs, a previously unexplored variant that is of independent interest. As a result of this development, we further establish the first strongly-adaptive guarantees under delayed feedback. Our approach also naturally extends to OCO with time-varying memory, where we obtain strongly-adaptive guarantees which improve the best-known bounds.

---


### 165. [On the Identifiability of Hybrid Deep Generative Models: Meta-Learning as a Solution](https://arxiv.org/abs/2610.32748)

**<font color=#1a73e8>作者：</font>** Yubo Ye, Maryam Toloubidokhti, Sumeet Vadhavkar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The interest in leveraging physics-based inductive bias in deep learning has resulted in recent development of hybrid deep generative models (hybrid-DGMs) that integrate known physics-based mathematical expressions in neural generative models. To identify these hybrid-DGMs requires inferring parameters of the physics-based component along with their neural component. The identifiability of these hybrid-DGMs, however, has not yet been theoretically probed or established. How does the existing theory of the un-identifiability of general DGMs apply to hybrid-DGMs? What may be an effective approach to construct a hybrid-DGM with theoretically-proven identifiability? This paper provides the first theoretical probe into the identifiability of hybrid-DGMs, and presents meta-learning as a novel solution to construct identifiable hybrid-DGMs. On synthetic and real-data benchmarks, we provide strong empirical evidence for the un-identifiability of existing hybrid-DGMs using unconditional priors, and strong identifiability results of the presented meta-formulations of hybrid-DGMs. Code is available at this https URL.

---


### 166. [SCDM-HTD: Spectral-Wise Conditional Diffusion Model for Hyperspectral Target Detection](https://arxiv.org/abs/2610.32768)

**<font color=#1a73e8>作者：</font>** Dunbin Shen, Wenfeng Kong, Jianjun Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral target detection (HTD) aims to locate and recognize objects at a fine-grained scale, playing a pivotal role in remote sensing. Despite significant progress, current HTD methods primarily focus on feature comparison while neglecting distribution learning for background-target separation, which can limit detection robustness in practical applications. This paper addresses this issue by introducing a spectral-wise conditional diffusion model that reformulates HTD as a task of generating a detection map. Specifically, we treat background and target confidence scores as training samples and use the corresponding pixel spectra as guiding conditions to capture the distributional discrepancy between background and target through diffusion and denoising. To enhance practical applicability, we propose a lightweight conditional denoising network based on multilayer perceptron to map noisy confidence scores to their ideal counterparts and adopt a deterministic reverse non-Markov chain to skip sampling steps, thereby accelerating the generation process. Furthermore, we introduce a composite loss to improve background-target separation. This loss integrates constrained energy minimization loss to enhance target saliency and suppress the background by maximizing the target response while minimizing average output energy, alongside binary cross-entropy loss to classify background and target using pixel-wise labels. Experimental results on four benchmark datasets demonstrate the effectiveness of the proposed method, with improvements in both quantitative metrics and qualitative visual effects.

---


### 167. [Deep Learning-Based Prediction of HER2 Status from Whole-Brain MRI in Breast Cancer Brain Metastases](https://arxiv.org/abs/2610.32774)

**<font color=#1a73e8>作者：</font>** Sara Early, Chris Kang, Vibujithan Vigneshwaran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Purpose: Human epidermal growth factor receptor 2 (HER2) status is a key biomarker relevant for prognostication and treatment decision making in metastatic breast cancer. Thus, the aim of this work was to explore whether HER2 status can be predicted directly from whole-brain post-contrast T1-weighted (T1w) MRI scans in breast cancer brain metastases (BCBM) using deep learning, and whether providing explicit tumour segmentation information improves prediction.
Methods: Using the publicly available BCBM-Radiogenomics dataset, we analysed 135 patients, including 70 HER2+ and 65 HER2- patients. Three approaches were implemented and evaluated: a conventional radiomics model, a simple fully convolutional network (SFCN) using T1w MRI scans alone, and an SFCN using T1w MRI scans with an expert-derived tumour mask as an additional input channel.
Results: The radiomics model achieved an area under the receiver operating characteristic curve (ROC-AUC) of 0.602 (95% confidence interval [CI]: 0.528--0.677) while the SFCN achieved a ROC-AUC of 0.667 (95% CI, 0.63--0.71) using T1w MRI scans alone, which increased to 0.692 (95% CI, 0.58--0.81) when an explicit tumour mask was additionally provided.
Conclusion: However, the modest performance across all approaches demonstrates the difficulty of predicting HER2 status from structural MRI scans alone. The difference between the segmentation-free and mask-guided SFCN models suggests that much of the predictive signal captured by the deep-learning model may be learned directly from whole-brain T1w MRI without requiring explicit tumour delineation. These findings support further investigation of segmentation-free deep-learning approaches as a potential non-invasive strategy to support HER2 status determination in BCBM.

---


### 168. [Consommé: Conditioned Token Merging for Split Inference](https://arxiv.org/abs/2610.32794)

**<font color=#1a73e8>作者：</font>** Man Ngo, Jan S. Rellermeyer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Split inference partitions a Vision Transformer between a resource-constrained edge device and a server. However, transmitting intermediate tokens across the communication channel is costly. Deploying fine-tuned backbones to every endpoint becomes expensive as well. We study token reduction for split inference under a frozen backbone, where only a small adapter is shipped. We observe that the CLS token plays a dual role: it acts as the global summary the receiver needs for classification, and it serves as a signal on which patches to keep. We propose Consommé, a method utilizing both characteristics. There, an information bottleneck compresses the CLS token into a compact latent which is transmitted in place of the full CLS token and conditions a learned patch gate merging patches into exactly $k$ tokens via soft assignment. It reaches any budget in a single step, thus escaping the per-layer cap of bipartite matching (BPM). On DeiT-S/T, it leads all methods at aggressive token budgets and remains operable at shallow splits where BPM cannot operate, while matching fine-tuned methods at gentle budgets at a fraction of their deployment cost.

---


### 169. [ParaTaxe: a Suite of Tools for Processing and Publishing Multi-parallel Corpora](https://arxiv.org/abs/2610.32796)

**<font color=#1a73e8>作者：</font>** Olivier Kraif, Cyrille François, Elnaz Jalilian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Over the past fifteen years, digital tools for parallelizing and aligning textual corpora have developed significantly within the field of digital humanities. Several projects and software tools have been created to compare different translations or versions of texts. Despite these technical advances, many parallel corpora produced in academic contexts quickly become inaccessible online due to the lack of maintenance or funding. To address this gap, we present a suite of open-source tools developed within the ACR Grimm Tradalign and ParaTaxe projects. This suite includes the AIlign aligner, based on multilingual embeddings, a Python processing pipeline for converting and aligning corpora, a web interface called ParaTaxe for managing collections of parallel corpora, and a web interface for exploring aligned corpora built with TEI-Publisher.

---


### 170. [CARES: Coverage-Aware Replay Exemplar Selection for Continual Learning](https://arxiv.org/abs/2610.32799)

**<font color=#1a73e8>作者：</font>** Arundhati S. Shanbhag, Brian B. Moser, Federico Raue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Replay-based Continual Learning mitigates catastrophic forgetting by keeping a buffer of past samples, making buffer composition critical under a fixed memory budget. Recent coreset-based replay methods improve buffer quality using model-derived gradients, losses, or auxiliary optimization, but incur substantial computational overhead as memory is repeatedly updated. We propose CARES, a continual model-optimization-free approach for buffer construction that instead exploits the geometry of a frozen pretrained feature space using class-aware, density-weighted coverage. We evaluate CARES across balanced, imbalanced, and label-noisy streams under online class- and task-incremental settings. On Tiny-ImageNet, CARES is 2.3 to 8.8 times faster than existing coreset-based selectors. Although CARES achieves this speedup using no training signal from the continual learner, it ranks among the state of the art across balanced, imbalanced, and label-noisy streams under online class- and task-incremental settings, outperforming the strongest baseline by up to 7.58 percentage points under class imbalance while also attaining higher average accuracy on Tiny-ImageNet. Code will be released upon publication

---


### 171. [CompMVR: Compression-Aware Multi-View Restoration Using Diffusion Models for Geometrically Consistent 3D Reconstruction](https://arxiv.org/abs/2610.32800)

**<font color=#1a73e8>作者：</font>** Dong-hwi Kim, Chaewon Moon, Hojun Song 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world 3D reconstruction pipelines often rely on multi-view images degraded by lossy compression. While compression artifacts have been extensively studied in single-image or video restoration, their impact on multi-view geometry remains largely overlooked. In this work, we identify compression-induced cross-view geometric inconsistency as a critical failure mode, where view-dependent artifacts disrupt feature matching, dense correspondence, camera parameter estimation, and downstream 3D reconstruction tasks such as novel view synthesis. To address this problem, we propose CompMVR, a compression-aware multi-view diffusion restoration framework that jointly refines compressed views while preserving cross-view consistency, and construct compressed datasets for systematic evaluation. Unlike conventional restoration methods that optimize each image independently for 2D perceptual quality, CompMVR leverages learned compression priors and cross-view correspondence to recover visual details while improving geometric reliability across views. Experiments across diverse datasets, codecs, and compression levels demonstrate gains in restoration quality and downstream 3D tasks, including novel-view synthesis, camera pose estimation, and view matching. These results establish compressed multi-view restoration as a distinct problem and highlight its importance for 3D reconstruction under lossy compression. Code and data for this paper are available at this https URL.

---


### 172. [Multiplicative vs. Additive State Coupling in Learned Optimizer Schedules](https://arxiv.org/abs/2610.32801)

**<font color=#1a73e8>作者：</font>** M. Harper Langston, Pierre-David Letourneau, Dalton Jones 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We learn schedules for a continuous penalty relaxation of MAX-CUT by backpropagating through an unrolled classical solver. A state-blind schedule generalizes to instances substantially larger than those used for training. A state-adaptive bilinear schedule also generalizes out of distribution, outperforming its untrained baseline across 15 seeds ($t=4.1$). By contrast, an additive ablation with identical inputs and output heads is statistically indistinguishable from the bilinear model in distribution but performs worse than its own baseline out of distribution ($t=-11.7$). This separation appears without regularization and persists across a $30$ round weight-decay sweep: the bilinear advantage remains significant at every tested value, whereas the additive model never recovers. The results in this setting isolate how solver state enters the schedule, rather than state adaptivity alone, as the architectural distinction associated with out-of-distribution transfer.

---


### 173. [U-NeXt: General-purpose event detection for neonatal EEG](https://arxiv.org/abs/2610.32811)

**<font color=#1a73e8>作者：</font>** Robert Hogan, Sean R. Mathieson, Aurel Luca 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We developed U-NeXt, a general framework for neonatal electroencephalography (EEG) event detection based on semantic segmentation. Its convolutional encoder-decoder directly segments individual channels using long input segments to preserve temporal context. A shared architecture and training framework were developed using low-voltage interval, artefact, and seizure datasets containing 51, 98, and 278 neonates, respectively, comprising over 11,000 hours of EEG and 82,000 annotated events. Performance was compared with task-specific ConvNeXt classifiers. For seizure detection, we also evaluated U-NeXt+, trained on an expanded dataset. Both U-NeXt variants and the ConvNeXt baseline were evaluated on two independent held-out seizure datasets, Helsinki and Cork, comprising 130 neonates, with recordings annotated by three experts. U-NeXt improved detection across all three event types, with particular gains in sensitivity for short events. U-NeXt+ achieved Matthews correlation coefficients of 0.862 and 0.891 on Helsinki and Cork, respectively, and improved hourly seizure burden correlations by 30-40% relative to ConvNeXt. U-NeXt+ met the criterion for expert-level performance on both datasets (p < 0.001). In separate computational benchmarks, U-NeXt reduced batch inference time relative to ConvNeXt by 254-fold on a central processing unit and 200-fold on a graphics processing unit. A common segmentation framework improves detection across diverse neonatal EEG event types while substantially reducing inference time. Accurate seizure burden estimates and performance comparable to expert reviewers support its potential use in continuous monitoring and clinical decision support.

---


### 174. [KrishokTech: A Bengali Agricultural Advisory System with Explicit Authorization Controls](https://arxiv.org/abs/2610.32817)

**<font color=#1a73e8>作者：</font>** Khan Raiyan Ibne Reza, Sanjana Aktar Maria, Shakil Ahmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For agricultural advisory, generating an answer is only part of the problem: the system must also control unsafe requests, work with limited connectivity, and accommodate changing guidance. KRISHOKTECH is a Bengali agricultural advisory system built around an explicit authorization boundary around generation. Before retrieval, normalization and rule-based admission checks refer policy-covered high-risk requests and ask for a crop when treatment intent is underspecified. The system then binds retrieval to a single crop and asks for confirmation when the text and image indicate different crops. After generation, a narrow verifier removes dosage claims not supported by retrieved BARI/BRRI evidence. Agricultural guidance is kept in an external evidence index that can be updated without retraining the generator, while browser-side vision and local retrieval reduce connectivity requirements. The interface makes these decisions visible as ASK, CONFIRM, REFER, and DROP, together with their evidence. On 200 farmer queries and 400 stress queries, the controls halted underspecified requests and reduced cross-crop retrieval violations from 36.5% to 0% under the tested alias filter. Mismatch detection caught 453 of 454 text-image conflicts, while the verifier caught 114 of 118 inserted dosage errors. The demonstration shows how these controls govern the path from request to delivered advice.

---


### 175. [On the Limits of Sparse Linear Model with Shuffled Differential Privacy](https://arxiv.org/abs/2610.32822)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Jiong Tuo, Meng Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse linear regression is a fundamental problem in high-dimensional statistics, and its private counterparts leave a large gap between the central and the local model of differential privacy. Shuffled differential privacy (SDP) sits between the two, offering accuracy closer to the central model without the trust requirement of a central curator. This paper studies sparse linear regression under both non-interactive and interactive SDP protocols. In the non-interactive setting, any non-interactive $(\epsilon,\delta)$-SDP protocol is shown to incur an $\ell_2$-norm estimation error of $\Omega( \frac{\sqrt{dk}}{n\epsilon} )$ with dimension $d$, sparsity $k$, and $n$ users, revealing an inherent dimensionality barrier. In addition, a non-interactive algorithm is proposed that achieves an $\ell_2$-norm upper bound of $\tilde{\mathcal{O}}( \sqrt{\frac{k}{n}} + \frac{d\sqrt{k}}{n\epsilon})$. To overcome this barrier, we turn to the interactive user-level setting, where each user holds $m$ samples. A two-round interactive algorithm is developed that first recovers the support through a heavy hitter step and then estimates the parameter, achieving an error of $\tilde{\mathcal{O}}( \sqrt{\frac{k}{nm}} + \frac{k}{n\sqrt{m}\epsilon} )$ with no polynomial dependence on $d$. Furthermore, by extending the score attack framework to user-level data, a new lower bound $\Omega( \sqrt{\frac{k\log(d/k)}{nm}} + \frac{k\log(d/k)}{n\sqrt{m}\epsilon} )$ is established for any user-level $(\epsilon,\delta)$-DP, showing that the proposed algorithm is near-optimal with only a gap of the factor $\log(d/k)$.

---


### 176. [SPOOK: Sparse Pixel Optimization for Off-Manifold Knowledge in Vision Encoders](https://arxiv.org/abs/2610.32835)

**<font color=#1a73e8>作者：</font>** Ankit Gupta, Akshat Pandya, Christoph Adami 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision encoders are widely used as semantic representations, but the relationship between embedding similarity and human-visible semantics can become unclear far from the natural-image manifold. We probe this regime in a black-box setting by applying sparse pixel edits to blank canvases with a simple pixel-level hill-climbing procedure. Across ImageNet and Flickr30k, we evaluate whether these edited blank canvases can retrieve chosen targets in multimodal contrastive encoders and self-supervised visual encoders. On OpenCLIP, inputs optimized toward class prompts achieve strong top-1 and top-5 targeted retrieval performance; on DINOv3, inputs optimized toward class prototypes achieve high target alignment and near-top prototype ranks. These results show that sparse edits on otherwise blank, visually non-semantic inputs can enter target semantic basins in both language-aligned and self-supervised visual representation spaces. Our findings identify a shared off-manifold failure mode of modern vision encoders and suggest sparse blank-canvas optimization as a simple probe of representation geometry.

---


### 177. [Communicating with the Entire Population: Machine Translation of Emergency Alerts and Warnings](https://arxiv.org/abs/2610.32842)

**<font color=#1a73e8>作者：</font>** Jen Wilson, Vipasha Bansal, William D. Lewis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> It is essential that we communicate with the entirety of an affected population during a crisis, including those who do not speak a region's dominant language(s). Commercial Translation tools offer a tempting solution to broaden access and can provide a lifeline when no other resources are available. However, Emergency response managers often operate in the dark regarding the quality and adequacy of these automated outputs. In this paper, we conduct a nationwide survey of emergency managers to understand their current workflows, perspectives, and operational challenges. We then evaluate commercial translation tools against these needs, shedding light on their utility and offering practical guidance on how and when these tools can be safely used in emergency response.

---


### 178. [OpenStripe supports open-set identification and spatial stripe profiling in wild Amur tigers](https://arxiv.org/abs/2610.32848)

**<font color=#1a73e8>作者：</font>** Yichun Peng, Yansong Li, Jin Hou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-invasive camera-trap monitoring of endangered wildlife requires open-set individual identification---grouping field images into identities without predefined classes or a known population size---yet pose deformation and cluttered backgrounds complicate image comparison. Here, we present OpenStripe, a multi-agent framework that reconstructs canonical two-dimensional (2D) tiger torso patterns and encodes four interpretable local stripe structures: breakpoints, bifurcations, irregular structures, and round structures. We evaluated OpenStripe on 100 camera-trap records from 28 wild Amur tigers (Panthera tigris altaica), representing nearly one-third of the documented population in the Northeast China Tiger and Leopard National Park. Combining all four complementary structures enabled automatic identity grouping with 0.90 matched accuracy and a 0.85 adjusted Rand index (ARI), outperforming 49 baseline configurations under the same backend (up to 0.43 accuracy and 0.14 ARI). In addition, results from OpenStripe indicate that stripe similarity in Amur tigers declines with geographic distance and suggest that traits such as fractal dimension and inter-stripe spacing are associated with geographic proximity. OpenStripe thus provides an interpretable representation that connects automated individual grouping with spatial phenotypic profiling in wild populations.

---


### 179. [Neural LoFi with Backward Coupling: A Spectral Theory of Cross-Layer Feature Learning](https://arxiv.org/abs/2610.32849)

**<font color=#1a73e8>作者：</font>** Yatin Dandi, Matteo Vilucchio, Hugo Tabanelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> During joint training, backpropagation allows later layers to reshape earlier representations, a feedback mechanism absent from purely layer-wise learning. We extend Neural Low-Degree Filtering (Neural LoFi), a recently proposed layer-wise spectral surrogate for feature learning, to capture this interaction. Starting from the exact backpropagation gradients, we derive a local coupling between a neuron's incoming weights and its corresponding next-layer column. In a controlled small-initialization regime with smooth activations and fixed surroundings, these dynamics amplify singular modes of a cross-layer correlation operator. Each growing mode pairs an earlier feature with an upper-layer response through shared neuron coefficients. This motivates a backward-coupling algorithm in which upper-layer sensitivities generate sample-dependent effective labels for earlier spectral steps, while corrected features refine upward transmission. A function-space variational principle characterizes the selected feature-response pairs by maximizing the label correlation of their product under kernel-norm constraints. For three-layer networks, we derive self-consistent continuous-time dynamics for the filtered hidden-layer features, the activation kernels, and the network output under the proposed backward coupling. In a hierarchical multi-index model, we establish a feature-recovery separation: backward coupling recovers lower-layer directions invisible to the original forward label-weighted statistic. The linear specialization recovers residual-dependent singular-mode dynamics, while paired modes provide a dynamical mechanism for linked low-rank covariance components consistent with the rainbow-network picture. Experiments with fully connected and convolutional networks on binary CIFAR-10 show improved accuracy over forward Neural LoFi at matched widths.

---


### 180. [Near-Optimal List Replicability from Littlestone Dimension](https://arxiv.org/abs/2610.32853)

**<font color=#1a73e8>作者：</font>** Ari Blondal, Pooya Hatami, Chavdar Lalov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the list replicability number in the realizable PAC learning framework and prove that every concept class $H$ over a countable domain with Littlestone dimension $d$ and dual VC dimension $v^*$ satisfies \[ \mathrm{LR}(H)\leq 2^{O(d\min\{\log d,v^*\})}. \] This matches the worst-case lower bound of $2^{\Omega(d)}$ up to a logarithmic factor in the exponent and exponentially improves the previous best upper bound $\mathrm{LR}(H)\le 2^{2^{O(d)}}$ of Bun, Livni, and Moran [FOCS 2020]. Unlike earlier bounds of $2^{O_\epsilon(d^2)}$ for fixed accuracy $\epsilon>0$ implied by the work of Ghazi, Golowich, Kumar, and Manurangsi [STOC 2021] and Lyu [STOC 2026], our bound is independent of $\epsilon$.
The $2^{O(d\log d)}$ bound follows from a new inductive framework for bounding list replicability that builds on the recent notion of irreducibility from differentially private learning. The $2^{O(dv^*)}$ bound follows from a simple globally stable learner that takes the majority vote of multiple empirical risk minimizers, with stability established using tools from stable regularity.

---


### 181. [Regularised RL improves sim-to-real transfer](https://arxiv.org/abs/2610.32855)

**<font color=#1a73e8>作者：</font>** Danilo Vucetic, Mohamad H. Danesh, Florence Clerc 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regularised reinforcement learning (RL) has provable robustness guarantees that should ease the transfer of policies from simulation to robots, known as sim-to-real. Yet, weakly regularised algorithms like Proximal Policy Optimisation (PPO) remain the de facto choice in sim-to-real pipelines, while the practical benefits of regularisation for transfer remain poorly characterised. In this work, we study the sim-to-real performance of commonly used RL algorithms, with the aim of characterising the effects of regularisation on robotic performance. To that end, we derive Soft MellowMax Actor-Critic (SMM-AC), a novel regularised RL algorithm based on the soft mellowmax value function, which carries strong robustness guarantees. On MuJoCo continuous control benchmarks, SMM-AC is competitive with baselines like Soft Actor-Critic (SAC). On real robots, SMM-AC achieves higher return, while exhibiting greater robustness to perturbations in observations, the environment, and dynamics than baselines. Together, these results demonstrate that regularised RL improves real-world policy deployment through better robustness to the sim-to-real gap, and changing real-world conditions.

---


### 182. [Sustainability of TSFM Deployment and Pretraining: From Carbon Footprint Analysis to Mitigation via Pruning](https://arxiv.org/abs/2610.32859)

**<font color=#1a73e8>作者：</font>** Cécile Luc, Nathanaël Lemonnier, Ievgen Redko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Foundation Models (TSFMs) offer strong zero-shot forecasting capabilities, but their high pretraining cost raises a practical sustainability question: does this upfront investment pay off over a full deployment lifecycle, compared to supervised standalone models that must be periodically retrained? We model the cumulative carbon cost of different approaches across a realistic industrial scenario: Chronos-2 amortizes its pretraining cost within months for large or frequently queried deployments, but a classical model remains cheaper indefinitely for small or rarely queried ones. For cases where reducing the TSFM's own cost matters, we show that removing a single encoder block (7.9% of parameters) via a gradient-free pruning criterion yields a consistent 6 to 9% reduction in FLOPs, CO2 emissions, and latency, at essentially no cost to zero-shot forecasting performance across a 25-task benchmark.

---


### 183. [PoKER: A Probability of Kill Estimation Rate Model for Air-to-Air Missiles Using Machine Learning on Stochastic Targets](https://arxiv.org/abs/2610.32864)

**<font color=#1a73e8>作者：</font>** Joao P. A. Dantas, Andre N. Costa, Diego Geraldo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work introduces PoKER, a novel probabilistic model engineered to optimize missile launch effectiveness in air-to-air scenarios, specifically within Beyond Visual Range (BVR) air combat. Unlike conventional Weapon Engagement Zone (WEZ) models that delineate zones based on static distances such as maximum, minimum, and no-escape ranges, PoKER applies machine learning to predict kill probabilities more accurately by integrating the stochastic behaviors of targets and missile miss distances. This model dynamically evaluates target behavior, greatly expanding the predictive capabilities of engagement analysis. By factoring in elements such as warhead lethality, target and shooter orientations, and the specific conditions of engagement, PoKER provides important insights into engagement dynamics and quantifies success probabilities. Consequently, it can potentially be an important tool for BVR air combat pilots, improving operational decision-making within this specialized combat domain.

---


### 184. [VTRL-Med: Progressive Visual Refinement with Topology-Guided Regularization for Medical Image Clustering](https://arxiv.org/abs/2610.32884)

**<font color=#1a73e8>作者：</font>** Guangyu Meng, Pengfei Gu, Peixian Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep clustering offers a promising approach for analyzing large unlabeled medical image datasets, yet prevailing methods still face two limitations: they may neglect class-agnostic structural priors that capture object boundaries and regions, and they do not explicitly encode topological patterns (e.g., connectivity and holes). These sources of information play distinct and complementary roles: visual-structural features provide the primary discriminative representation for clustering, while topological features provide additional global geometric cues for residual visual ambiguities. We introduce VTRL-Med, a progressive visual-structural learning framework with topology-guided regularization for medical image clustering. VTRL-Med first adapts the Segment Anything Model (SAM) to extract image features that retain structural cues inherited from mask-supervised pretraining. It then generates reliable pseudo-labels through a two-step filtering process that combines prototype-based selection with k-nearest neighbor consistency validation. Finally, it progressively refines the visual branch while an auxiliary topology branch, constructed from persistent homology (PH) descriptors, provides additional geometric regularization during training. Across 13 medical image benchmarks, VTRL-Med achieves state-of-the-art clustering performance, improving average accuracy by 4.48% over existing methods. On three representative datasets, topology-guided regularization further improves accuracy by 1.3--4.3% over visual refinement alone.

---


### 185. [Reinforcement Learning with Multi-Step Transition Predictions: A Bellman Theory](https://arxiv.org/abs/2610.32887)

**<font color=#1a73e8>作者：</font>** Chenbei Lu, Zaiwei Chen, Tongxin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-step predictions of future transition realizations can improve reinforcement learning, but their value remains difficult to quantify. Directly including these predictions in the state can lead to exponential state-space growth, making direct dynamic programming computationally expensive. We study discounted finite MDPs under a block-feedback protocol: at the start of each K-period block, the decision maker observes $K$-step probabilistic transition predictions for a subset of actions and adapts decisions to observed states within the block. We show that the optimal value satisfies a Bayesian Bellman equation on the original state space. This representation reveals that predictive information creates value by recursively changing the local order of maximization and expectation in the Bellman expansion. We formalize this effect through a Bellman--Jensen analysis and quantify the effects of prediction horizon, error, action coverage, and within-block feedback. We propose block-feedback Bayesian offline learning with online adaptation (BF--BOLA), a model-based algorithm for learning near-optimal policies, and establish upper and lower sample-complexity bounds that match up to logarithmic factors in the stated regimes. The results show that predictions can reduce transition learning to uncovered rows and that learning a near-optimal policy can require fewer prediction samples than estimating the Bayesian value function.

---


### 186. [Closing the Modality Gap via Simplex-Constrained Representations](https://arxiv.org/abs/2610.32890)

**<font color=#1a73e8>作者：</font>** Shubham Gupta, Siva Reddy, Perouz Taslakian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While multimodal contrastive models like CLIP and CLAP successfully learn shared representations, their embeddings typically exhibit a persistent \emph{modality gap}. We propose addressing this separation through a purely geometric approach: changing the embedding domain from the unit sphere, $S^{d-1}$, to the probability simplex, $\Delta^{d-1}$. Although both manifolds share the same intrinsic dimension, the simplex acts as a structural prior; its nonnegative, unit-mass constraints serve as a cross-modal calibration that forces both modalities to ground themselves in the same coordinate system. By attaching lightweight softmax adapters and using Total Variation similarity, we reduce the centroid $\ell_2$ gap by 97--99\% across five multimodal retrieval benchmarks. This confirms that simplicial geometry induces genuine semantic alignment, matching or exceeding the retrieval performance of standard unconstrained models.

---


### 187. [LoCA: Enabling Multi-Modality in Geospatial Location Encoders](https://arxiv.org/abs/2610.32894)

**<font color=#1a73e8>作者：</font>** Panagiotis Koromilas, Eleanna Vali, Diogenis Antonopoulos 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Location encoders map geographic coordinates to high-dimensional descriptors through contrastive alignment with paired Earth Observation imagery. We prove that this construction is structurally limited: any Lipschitz location encoder produces an output of intrinsic dimension at most 2, regardless of architecture or bandwidth, which forces the contrastive loss to strictly exceed its asymptotic optimum. Empirically, joint training also collapses the encoder's embedding covariance to low rank. Although dimension-limited, current location encoders sidestep this spectral collapse by training against a frozen image encoder, which we reinterpret as a covariance regularizer that supplies a high-rank target for the location encoder to fold onto. However, extending this approach to multimodal inputs is challenging, as location encoders should simultaneously map a single location to multiple, potentially incompatible, descriptors. We identify two requirements a regularizer must satisfy for location encoding in multimodal regimes: co-alignment across modalities, since adapters alone cannot align independently pretrained encoders; and high effective rank, since the location encoder inherits its target's spectrum. We propose LoCA (Location Contrastive Alignment), a two-stage pipeline that satisfies both. Stage 1 jointly trains Sentinel-1 and Sentinel-2 encoders with contrastive learning, producing a co-aligned, high-rank multimodal target. Stage 2 freezes the image encoders and trains a location and a tabular metadata encoder as projection adapters with multi-view contrastive learning. Against five state-of-the-art encoders on 17 tasks ranging from land cover and wildfire forecasting to geophysical, socio-economic, biodiversity and climate applications, LoCA achieves the most task wins, is the only model to outperform every other on a majority of tasks, and wins 68.8% of all per-task comparisons.

---


### 188. [EVSEFuzz : A Tool for Automated Testing of Protocol Implementations](https://arxiv.org/abs/2610.32902)

**<font color=#1a73e8>作者：</font>** Soham Gumaste, Michael Khan, Roland Varriale 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid adoption and development of electric vehicle (EV) networks has required the expansive deployment of EV charging infrastructure (EVCI) which relies on communication protocols such as the open charge point protocol (OCPP) to coordinate data transfer between charging network operators and the EV supply equipment. In this paper, we present EVSEFuzz, a tool for automatically building fuzzers to test the security of protocol implementations. To achieve this we make a novel use of Python datatype validation packages and tools to ``understand'' datatypes and message structures and generate both compliant and non-compliant messages. To date, EVSEFuzz has been tested successfully with several open and closed-source implementations and has found several vulnerabilities leading to the publication of two CVEs.

---


### 189. [Recommender regret for improving regularised RL estimation with bandits and MCTS](https://arxiv.org/abs/2610.32910)

**<font color=#1a73e8>作者：</font>** Danilo Vucetic, Alexandre Larouche, Mohammad Pedramfar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regularised reinforcement learning (RL) algorithms rely on estimators, like Monte Carlo tree search or one-step look-ahead, to provide policy, value, or Q-value estimates in training and inference. However, existing bandit-based estimation frameworks evaluate sampling efficiency, not the quality of estimates. We address this by formalising estimate generation as a recommendation process, treating bandit-based sampling as an improvement operator. To evaluate the quality of a recommendation (estimate), we define regulariser-aware recommender regrets, analysing their lower bounds, and proving that simple algorithms like uniform sampling can achieve these bounds. Finally, we unify bandit- and search-based target improvement under recommender MCTS. Across synthetic trees, arcade games, and scientific discovery tasks, recommenders often yield faster target convergence and superior downstream performance. Our experiments characterise for the first time the potential of regularised MCTS in scientific applications.

---


### 190. [A Tutorial on Physics Constrained Machine Learning for Hybrid Modeling, Optimization, and Control](https://arxiv.org/abs/2610.32914)

**<font color=#1a73e8>作者：</font>** Rahul Golder, Bimol Nath Roy, MM Faruque Hasan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-constrained machine learning (PCML) integrates domain knowledge, first-principles, and physical constraints into AI/ML models. In this work, we present a step-by-step tutorial of a modular PCML framework, KKT-HardNet, and illustrate how it could be used for hybrid modeling, process simulation, optimization and model predictive control in a single platform. KKT-HardNet combines fast inference capabilities of neural networks with guaranteed satisfaction of algebraic constraints through differential projection. It can handle heterogeneous data and enforce both linear and nonlinear equality and inequality constraints. The modular design supports custom neural-network backbones and user-defined projection mechanisms for PCML. To enable efficient end-to-end training, KKT-HardNet exploits implicit function theorem to backpropagate through the projection layer. This avoids computationally expensive automatic differentiation. This work also introduces an exact reduced-order Fischer-Burmeister reformulation and a primal-dual interior-point method as an alternative projection solve strategy. We also provide a diverse set of benchmarking problems for PCML in engineering applications. KKT-HardNet achieves orders of magnitude better performance in terms of both constraint satisfaction and inference time. The KKT-HardNet code and the benchmark datasets are available at this https URL .

---


### 191. [What Mean Error Misses: Device-Clock Diagnostics for Evaluating Eye Tracking across Three Virtual Reality Headsets](https://arxiv.org/abs/2610.32915)

**<font color=#1a73e8>作者：</font>** Aleksandr Chernysh, Mehedi Hasan Raju, Kamrul Hasan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Gaze research in virtual reality needs eye trackers of known error. Thirty participants completed the same protocol on the Meta Quest Pro (QP), HTC VIVE Pro Eye (PE) and HTC VIVE Focus Vision (FV); to our knowledge, this is the first evaluation of the FV eye tracker. In a random-saccade task, median participant mean error was 1.04° on QP, 1.50° on PE and 2.41° on FV, which remained least accurate after linear recalibration. In a later block with a darker background, PE error rose by 0.70°. FV samples were positively correlated: dispersion was 9.8 times the sample-to-sample root mean square. The device clocks showed losses that mean error hides. QP paused for up to 6.04 s, and FV skipped single samples. During instructed eye closures, QP flagged every sample valid while gaze moved 9.74°. Evaluations should report repeated timestamps, loss composition on the device clock and validity during eye closures.

---


### 192. [ZENO: Nonlinear filtering with Zakai Equation Neural Operators](https://arxiv.org/abs/2610.32926)

**<font color=#1a73e8>作者：</font>** Aaditya Prasad, Steven W. Flavell, Brian DePasquale  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State inference and parameter learning for nonlinear filters is a core computation for scientific machine learning with varied applications in engineering and neuroscience. The unnormalized filtering distribution is governed by the Zakai equation, a stochastic partial differential equation (SPDE) that combines the forward Kolmogorov operator (known as the Fokker-Planck equation) with observed likelihood updates. Although solving these high-dimensional SPDEs is often impossible analytically and intractable numerically, advances in operator learning and physics-informed machine learning have made it feasible. Harnessing these advances, we introduce the Zakai Equation Neural Operator (ZENO), a model that optimizes a neural operator against a Zakai Equation based physics-informed loss to approximate the exact unnormalized filtering distribution for latent stochastic dynamical systems. We use this ZENO-inferred posterior distribution in an expectation-maximization (EM) framework to perform parameter learning and state inference. We demonstrate ZENO's ability to accurately infer the posterior distribution and learn its corresponding SDE parameters in three simulated stochastic dynamical systems (Double-Well bistable system, Van Der Pol (VDP) oscillator, and Lorenz system) and compare its performance against established methods for latent SDE inference and learning. We show that ZENO recovers previously observed limit cycles representing forward and backward locomotion from a whole-brain imaging dataset of immobilized \textit{C. elegans} nematodes. ZENO is a novel approach to the problem of nonlinear filtering and dynamical inference through the lens of partial differential equations and operator theory.

---


### 193. [STROKE: Simple Sparse Structural Occlusions for Black-Box Adversarial Attacks](https://arxiv.org/abs/2610.32932)

**<font color=#1a73e8>作者：</font>** Ankit Gupta, Akshat Pandya, Paul Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce STROKE, a query-efficient score-based black-box adversarial attack that constructs perturbations from simple oriented rectangular occlusions. STROKE optimizes these perturbations through a lightweight greedy add-and-refine procedure. Across diverse image classifiers, STROKE achieves high attack success with low query counts at nominal 1--2\% area settings, showing favorable performance relative to existing patch-based attacks in several configurations. Matched comparisons further demonstrate substantial reductions in wall-clock attack time, while ablation studies examine the key design choices and effectiveness across structural primitives. These findings suggest that simple structural occlusions offer an effective and computationally efficient search space for black-box adversarial attacks.

---


### 194. [Flownomaly: Single-Step Conditional-Mean Recovery for Few-Shot Anomaly Detection](https://arxiv.org/abs/2610.32964)

**<font color=#1a73e8>作者：</font>** Bernardo Perrone Ribeiro, Erkut Akdag, Egor Bondarev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot industrial anomaly detection requires modeling category-specific normality from only a handful of defect-free images. Common approaches tie inference to stored exemplars, impose rigid linear structure, or risk reproducing anomalous content. Flownomaly instead casts the problem as normal-counterpart recovery in frozen DINOv2 feature space. Given normal supports, a velocity field is learned through conditional flow matching over frozen patch tokens to transport Gaussian noise toward normal features. Along straight paths, a single recovery step using one evaluation of the optimal field yields the posterior mean of the clean normal token without trajectory integration. The operating time governs how strongly recovery modifies a query token. With no anomalous validation samples available for tuning, a normal-only Jacobian gain-to-noise criterion selects this time from the supports alone. Squared residuals between query tokens and their recovered counterparts yield anomaly signals for both dense localization and image-level detection. Across 1-, 2-, and 4-shot benchmarks on MVTec-AD and VisA, together with sample-shot evaluations on Real-IAD, Flownomaly achieves state-of-the-art performance against recent category-specific methods. In the 1-shot setting, image- and pixel-level AUROC reach 97.8% and 98.0% on MVTec-AD and 95.3% and 98.7% on VisA, with a 2.1-point image-level AUROC improvement over the strongest baseline on VisA. Code is available at this https URL.

---


### 195. [RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms](https://arxiv.org/abs/2610.32971)

**<font color=#1a73e8>作者：</font>** Xi Chen, Fengqi Hu, Zeyu Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust reinforcement learning (RL) is critical for reliable real-world deployment, where policies may fail under diverse shifts and disruptions. Existing robust RL algorithms offer a rich set of mechanisms and principles, yet two major barriers limit their broader potential: limited algorithm reusability and an unclear empirical capability boundary. We introduce RobustRLlib, an algorithm-centric library and benchmark that addresses both challenges. It integrates 17 representative robust online, offline, and safe RL algorithms under a unified interface for substantially improved reusability, together with an enhanced evaluation platform spanning diverse real-world shifts and advanced humanoid and vision-language-action tasks. Systematic evaluation over 273 perturbation configurations provides an up-to-date capability map of current robust RL algorithms, revealing where they remain effective and where substantial robustness gaps persist. As an open-source, user-friendly platform, RobustRLlib offers a reproducible and extensible codebase for applying existing methods to new problems and developing new robust RL algorithms.

---


### 196. [FlexGlue: Sparse-to-Dense Feature Matching and Visual Disambiguation](https://arxiv.org/abs/2610.32976)

**<font color=#1a73e8>作者：</font>** Philipp Lindenberger, Paul-Edouard Sarlin, Ondrej Miksik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To estimate correspondences across images, existing approaches match either sparse interest points, which is highly efficient but limited by repeatability, or dense pixel grids, which is robust but expensive. Furthermore, these approaches are trained with only matching pairs and thus often fail to reject unrelated pairs that exhibit visual symmetries, which is equally important in applications like Structure-from-Motion (SfM). We bridge these gaps by introducing FlexGlue, a neural network for asymmetric sparse-to-dense matching and disambiguation. Given two images and coordinates of points in the first image, FlexGlue estimates the coordinates of the corresponding points in the second image while simultaneously rejecting the pair if non-matching. By searching for a limited set of correspondences among dense pixels, our approach is both fast and effective at both matching and disambiguation: it combines the sub-pixel accuracy of dense matching with the speed of sparse matching, while rejecting incorrect pairs with high precision. Experiments on multiple datasets show that FlexGlue pushes the Pareto frontier in relative pose estimation and significantly outperforms existing approaches for SfM and visual localization. FlexGlue is publicly available at this https URL .

---


### 197. [UniAction: Unified Action Conditioning for World Models](https://arxiv.org/abs/2610.32977)

**<font color=#1a73e8>作者：</font>** Bowen Xue, Zizhang Li, Hong-Xing Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Actions that condition world models are highly heterogeneous, and thus existing action-conditioned world models are typically built for individual action types, fragmenting already limited action-annotated data across separate models. We introduce UniAction, a unified action-conditioning framework that represents any action as a sparse set of action elements, each with a discrete semantic identity and a continuous spatiotemporal grounding coordinate. By mapping these coordinates directly into the pretrained video model's native positional space, UniAction allows heterogeneous actions to condition a shared world model within the same spatiotemporal structure. We further introduce cardinality-calibrated attention to address the bias from differing action representation granularities. We evaluate UniAction on four representative action forms: force, camera control, hand pose, and robot pose. UniAction outperforms conditioning alternatives in action following, and a single jointly trained model surpasses the action-specific experts, showing that heterogeneous action data benefit from unified model and joint training.

---


### 198. [SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning](https://arxiv.org/abs/2610.32978)

**<font color=#1a73e8>作者：</font>** Yuhan Liu, Lianhui Qin, Shenji Wan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training generalizable embodied agents requires realistic, varied, and simulation-ready indoor environments. Language-guided methods support semantic planning and object-level reasoning, but precise spatial grounding remains difficult. Visual generative models offer rich priors over plausible arrangements, yet their outputs require geometric reasoning to become physically valid 3D scenes. We introduce SceneBloom, an agentic framework that combines visual layout sampling with contract-guided 3D compilation. A hierarchical sampler uses diffusion priors to generate furniture arrangements within functional zones. A compiler then uses relations extracted from each proposal to guide geometric fitting and local pose correction. Across five room types, SceneBloom attains the highest visual quality and physical stability among the compared methods and is the only method with no detected mesh collisions and out-of-bounds objects. Its layouts are also closer to the distribution of real rooms than those of all compared baselines. Object navigation policies trained in these realistic scenes achieve a higher success rate in held-out real scans than those trained on an equal number of real training scans. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**151-198**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-198**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
