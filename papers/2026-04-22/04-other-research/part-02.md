# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

---

### 51. [Privacy-Preserving Semantic Segmentation without Key Management](https://arxiv.org/abs/2604.16523)

**<font color=#1a73e8>作者：</font>** Mare Hirose, Shoko Imaizumi, Hitoshi Kiya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a novel privacy-preserving semantic segmentation method that can use independent keys for each client and image. In the proposed method, the model creator and each client encrypt images using locally generated keys, and model training and inference are conducted on the encrypted images. To mitigate performance degradation, an image encryption method is applied to model training in addition to the generation of test images. In experiments, the effectiveness of the proposed method is confirmed on the Cityscapes dataset under the use of a vision transformer-based model, called SETR.

---


### 52. [Anumati: Proof of Adherence as a Formal Consent Model for Autonomous Agent Protocols](https://arxiv.org/abs/2604.16524)

**<font color=#1a73e8>作者：</font>** Ravi Kiran Kadaboina  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As autonomous AI agents increasingly call other agents to complete tasks on behalf of a human principal, a structural accountability gap has emerged: the calling agent accepts the terms of service of the callee without any protocol-level mechanism to prove that it understood those terms or that it subsequently honoured them. Authentication protocols such as OAuth and mutual TLS establish who may call which capability. They do not address under what conditions a permitted call may be made, and those conditions change as the callee's policies evolve. In this paper we formalise the distinction between proof of acceptance (a timestamped acknowledgement) and proof of adherence (a per-action reasoning record citing the specific clause evaluated). We propose three primitives (PolicyDocument, ConsentRecord, and AdherenceEvent) that together constitute a versioned, append-only consent model for agent-to-agent communication. The model is instantiated as a non-breaking extension to two widely used agent protocols: the Agent2Agent (A2A) protocol and the Model Context Protocol (MCP). A TLA+ specification of the consent lifecycle, together with a reference Python implementation of the chain integrity and adherence trail validators, is available in the accompanying repository.

---


### 53. [Expert-Annotated Embryo Image Dataset with Natural Language Descriptions for Evidence-Based Patient Communication in IVF](https://arxiv.org/abs/2604.16528)

**<font color=#1a73e8>作者：</font>** Nicklas Neu, Thomas Ebner, Jasmin Primus 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embryo selection is one of multiple crucial steps in in-vitro fertilization, commonly based on morphological assessment by clinical embryologists. Although artificial intelligence methods have demonstrated their potential to support embryo selection by automated embryo ranking or grading methods, the overall impact of AI-based solutions is still limited. This is mainly due to the required adaptation of automated solutions to custom clinical data, reliance on time lapse incubators and a lack of interpretability to understand AI reasoning. The modern, informed patient is questioning expert decisions, particularly if the treatment is not successful. Thus, evidence-based decision justification in tasks like embryo selection would support transparent decision making and respectful patient communication. To support this aim, we hereby present an expert-annotated dataset consisting of embryo images and corresponding morphological description using natural language. The description contains relevant information on embryonic cell cycle, developmental stage and morphological features. This dataset enables the finetuning of modern foundational vision-language models to learn and improve over time with high accuracy. Predicted embryo descriptions can then be leveraged to automatically extract scientific evidence from literature, facilitating well-informed, evidence-based decision-making and transparent communication with patients. Our proposed dataset supports research in language-based, interpretable, and transparent automated embryo assessment and has the potential to enhance the decision-making process and improve patient outcomes significantly over time.

---


### 54. [Beyond Attack Success Rate: A Multi-Metric Evaluation of Adversarial Transferability in Medical Imaging Models](https://arxiv.org/abs/2604.16532)

**<font color=#1a73e8>作者：</font>** Emily Curl, Kofi Ampomah, Md Erfan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While deep learning systems are becoming increasingly prevalent in medical image analysis, their vulnerabilities to adversarial perturbations raise serious concerns for clinical deployment. These vulnerability evaluations largely rely on Attack Success Rate (ASR), a binary metric that indicates solely whether an attack is successful. However, the ASR metric does not account for other factors, such as perturbation strength, perceptual image quality, and cross-architecture attack transferability, and therefore, the interpretation is incomplete. This gap requires consideration, as complex, large-scale deep learning systems, including Vision Transformers (ViTs), are increasingly challenging the dominance of Convolutional Neural Networks (CNNs). These architectures learn differently, and it is unclear whether a single metric, e.g., ASR, can effectively capture adversarial behavior. To address this, we perform a systematic empirical study on four medical image datasets: PathMNIST, DermaMNIST, RetinaMNIST, and CheXpert. We evaluate seven models (VGG-16, ResNet-50, DenseNet-121, Inception-v3, DeiT, Swin Transformer, and ViT-B/16) against seven attack methods at five perturbation budgets, measuring ASR, Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM), and $L_2$ perturbation magnitude. Our findings show a consistent pattern: perceptual and distortion metrics are strongly associated with one another and exhibit minimal correlation with ASR. This applies to both CNNs and ViTs. The results demonstrate that ASR alone is an inadequate indicator of adversarial robustness and transferability. Consequently, we argue that a thorough assessment of adversarial risk in medical AI necessitates multi-metric frameworks that encompass not only the attack efficacy but also its methodology and associated overheads.

---


### 55. [G-PARC: Graph-Physics Aware Recurrent Convolutional Neural Networks for Spatiotemporal Dynamics on Unstructured Meshes](https://arxiv.org/abs/2604.16533)

**<font color=#1a73e8>作者：</font>** Jack T. Beerman, Tyler J. Abele, Mehdi Taghizadeh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-aware recurrent convolutional networks (PARC) have demonstrated strong performance in predicting nonlinear spatiotemporal dynamics by embedding differential operators directly into the computational graph of a neural network. However, pixel-based convolutions are restricted to static, uniform Cartesian grids, making them ill-suited to following evolving localized structures in an efficient manner. Graph neural networks (GNNs) naturally handle irregular spatial discretizations, but existing graph-based physics-aware deep learning (PADL) methods have difficulty handling extreme nonlinear regimes. To address these limitations, we propose Graph PARC (G-PARC), which uses moving least squares (MLS) kernels to approximate spatial derivatives on unstructured graphs, and embeds the derivatives of governing partial differential equations into the network's computational graph. G-PARC achieves better accuracy with 2-3x fewer parameters than MeshGraphNet, MeshGraphKAN, and GraphSAGE, replacing the traditional encoder-processor-decoder framework with analytically computed differential operators. We demonstrate that G-PARC (1) generalizes across nonuniform spatial and temporal discretizations; (2) handles moving meshes required for structural deformation; and (3) outperforms existing graph-based PADL methods on nonlinear benchmarks including fluvial hydrology, planar shock waves, and elastoplastic dynamics. By embedding explicit physical operators within the flexibility of GNNs, G-PARC enables accurate modeling of extreme nonlinear phenomena on complex computational domains, moving PADLbeyond idealized Cartesian grids.

---


### 56. [Public and private blockchain for decentralized digital building twins and building automation system](https://arxiv.org/abs/2604.16534)

**<font color=#1a73e8>作者：</font>** Reachsak Ly, Alireza Shojaei  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The communication protocols and data transfer mechanisms employed by IoT devices in smart buildings and corresponding digital twin systems predominantly rely on centralized architectures. Such centralized systems are vulnerable to single points of failure, where a malfunction can disrupt operational processes. This study introduces a blockchain-based decentralized protocol to enhance the cyber resilience of IoT data transfer for digital twins and enable decentralized automation of building operations. The framework incorporates public and private blockchain technologies alongside two case studies showcasing prototypes of each system. These prototypes were validated within a real-world building environment using smart home appliances and two digital twin platforms, with their performance evaluated based on cost, scalability, data security, and privacy. The findings reveal that the Hyperledger Fabric-based system excels in terms of scalability, speed, and cost-effectiveness, while both frameworks offer advantages over traditional centralized protocols in system cyber resilience, data security, and privacy.

---


### 57. [Towards Reliable Testing of Machine Unlearning](https://arxiv.org/abs/2604.16536)

**<font color=#1a73e8>作者：</font>** Anna Mazhar, Sainyam Galhotra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning components are now central to AI-infused software systems, from recommendations and code assistants to clinical decision support. As regulations and governance frameworks increasingly require deleting sensitive data from deployed models, machine unlearning is emerging as a practical alternative to full retraining. However, unlearning introduces a software quality-assurance challenge: under realistic deployment constraints and imperfect oracles, how can we test that a model no longer relies on targeted information? This paper frames unlearning testing as a first-class software engineering problem. We argue that practical unlearning tests must provide (i) thorough coverage over proxy and mediated influence pathways, (ii) debuggable diagnostics that localize where leakage persists, (iii) cost-effective regression-style execution under query budgets, and (iv) black-box applicability for API-deployed models. We outline a causal, pathway-centric perspective, causal fuzzing, that generates budgeted interventions to estimate residual direct and indirect effects and produce actionable "leakage reports". Proof-of-concept results illustrate that standard attribution checks can miss residual influence due to proxy pathways, cancellation effects, and subgroup masking, motivating causal testing as a promising direction for unlearning testing.

---


### 58. [PoInit-of-View: Poisoning Initialization of Views Transfers Across Multiple 3D Reconstruction Systems](https://arxiv.org/abs/2604.16540)

**<font color=#1a73e8>作者：</font>** Weijie Wang, Songlong Xing, Zhengyu Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Poisoning input views of 3D reconstruction systems has been recently studied. However, we identify that existing studies simply backpropagate adversarial gradients through the 3D reconstruction pipeline as a whole, without uncovering the new vulnerability rooted in specific modules of the 3D reconstruction pipeline. In this paper, we argue that the structure-from-motion (SfM) initialization, as the geometric core of many widely used reconstruction systems, can be targeted to achieve transferable poisoning effects across diverse 3D reconstruction systems. To this end, we propose PoInit-of-View, which optimizes adversarial perturbations to intentionally introduce cross-view gradient inconsistencies at projections of corresponding 3D points. These inconsistencies disrupt keypoint detection and feature matching, thereby corrupting pose estimation and triangulation within SfM, eventually resulting in low-quality rendered views. We also provide a theoretical analysis that connects cross-view inconsistency to correspondence collapse. Experimental results demonstrate the effectiveness of our PoInit-of-View on diverse 3D reconstruction systems and datasets, surpassing the single-view baseline by 25.1% in PSNR and 16.5% in SSIM in black-box transfer settings, such as 3DGS to NeRF.

---


### 59. [BOOKAGENT: Orchestrating Safety-Aware Visual Narratives via Multi-Agent Cognitive Calibration](https://arxiv.org/abs/2604.16541)

**<font color=#1a73e8>作者：</font>** Bo Gao, Chang Liu, Yuyang Miao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Large Generative Models (LGMs) have revolutionized multi-modal generation. However, generating illustrated storybooks remains an open challenge, where prior works mainly decompose this task into separate stages, and thus, holistic multi-modal grounding remains limited. Besides, while safety alignment is studied for text- or image-only generation, existing works rarely integrate child-specific safety constraints into narrative planning and sequence-level multi-modal verification. To address these limitations, we propose BookAgent, a safety-aware multi-agent collaboration framework designed for high-quality, safety-aware visual narratives. Different from prior story visualization models that assume a fixed storyline sequence, BookAgent targets end-to-end storybook synthesis from a user draft by jointly planning, scripting, illustrating, and globally repairing inconsistencies. To ensure precise multi-modal grounding, BookAgent dynamically calibrates page-level alignment between textual scripts and visual layouts. Furthermore, BookAgent calibrates holistic consistency from the temporal dimension, by verifying-then-rectifying global inconsistencies in character identity and storytelling logic. Extensive experiments demonstrate that BookAgent significantly outperforms current methods in narrative coherence, visual consistency, and safety compliance, offering a robust paradigm for reliable agents in complex multi-modal creation. The implementation will be publicly released at this https URL.

---


### 60. [A B-Spline Function Based 3D Point Cloud Unwrapping Scheme for 3D Fingerprint Recognition and Identification](https://arxiv.org/abs/2604.16546)

**<font color=#1a73e8>作者：</font>** Mohammad Mogharen Askarin, Jiankun Hu, Min Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional (3D) fingerprint recognition and identification offer several advantages over traditional two-dimensional (2D) recognition systems. The contactless nature of 3D fingerprints enhances hygiene and security, reducing the risk of contamination and spoofing. In addition to surface ridge and valley patterns, 3D fingerprints capture depth, curvature, and shape information, enabling the development of more precise and robust authentication systems. Despite recent advancements, significant challenges remain. The topological height of fingerprint pixels complicates the extraction of ridge and valley patterns. Furthermore, registration issues limit the acquisition process, requiring consistent direction and orientation across all samples. To address these challenges, this paper introduces a method that unwraps 3D fingerprints, represented as 3D point clouds, using B-spline curve fitting to mitigate height variation and reduce registration limitations. The unwrapped point cloud is then converted into a grayscale image by mapping the relative heights of the points. This grayscale image is subsequently used for recognition through conventional 2D fingerprint identification methods. The proposed approach demonstrated superior performance in 3D fingerprint recognition, achieving Equal Error Rates (EERs) of 0.2072%, 0.26%, and 0.22% across three experiments, outperforming existing methods. Additionally, the method surpassed 3D fingerprint flattening technique in both recognition and identification during cross-session experiments, achieving an EER of 1.50% when fingerprints with varying registrations were included.

---


### 61. [An Interpretable Framework Applying Protein Words to Predict Protein-Small Molecule Complementary Pairing Rules](https://arxiv.org/abs/2604.16550)

**<font color=#1a73e8>作者：</font>** Jingke Chen, Jingrui Zhong, Tazneen Hossain Tani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the high accuracy of 'black box' deep learning models, drug discovery still relies on protein-ligand interaction principles and heuristics. To improve interpretability of protein-small molecule binding predictions, we developed the PWRules framework, which applies binding affinity data to identify privileged small molecule fragments and subsequently defines complementary pairing rules between these fragments and protein words (semantic sequence units) through an interpretability module. The resulting word-fragment rules are then ranked by the PWScore function to prioritize active compounds. Evaluations on benchmark datasets show that PWScore achieves competitive performance comparable to the physics-based model (Glide) and the deep learning model (PSICHIC) and shows broad applicability for protein targets outside the training dataset, e.g., SARS-CoV-2 main protease. Notably, PWScore captures complementary interaction information, yielding superior enrichment performance when integrated with these established methods. Structural analysis of protein-ligand complexes indicates that learned word-fragment rules are significantly enriched near ligand-binding pockets, despite training without explicit structural guidance. By extracting and applying complementary pairing rules, PWRules provides an interpretable framework for drug discovery.

---


### 62. [Co-generation of Layout and Shape from Text via Autoregressive 3D Diffusion](https://arxiv.org/abs/2604.16552)

**<font color=#1a73e8>作者：</font>** Zhenggang Tang, Yuehao Wang, Yuchen Fan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-scene generation approaches largely reduced the manual efforts required to create 3D scenes. However, their focus is either to generate a scene layout or to generate objects, and few generate both. The generated scene layout is often simple even with LLM's help. Moreover, the generated scene is often inconsistent with the text input that contains non-trivial descriptions of the shape, appearance, and spatial arrangement of the objects. We present a new paradigm of sequential text-to-scene generation and propose a novel generative model for interactive scene creation. At the core is a 3D Autoregressive Diffusion model 3D-ARD+, which unifies the autoregressive generation over a multimodal token sequence and diffusion generation of next-object 3D latents. To generate the next object, the model uses one autoregressive step to generate the coarse-grained 3D latents in the scene space, conditioned on both the current seen text instructions and already synthesized 3D scene. It then uses a second step to generate the 3D latents in the smaller object space, which can be decoded into fine-grained object geometry and appearance. We curate a large dataset of 230K indoor scenes with paired text instructions for training. We evaluate 7B 3D-ARD+, on challenging scenes, and showcase the model can generate and place objects following non-trivial spatial layout and semantics prescribed by the text instructions.

---


### 63. [PA-TCNet: Pathology-Aware Temporal Calibration with Physiology-Guided Target Refinement for Cross-Subject Motor Imagery EEG Decoding in Stroke Patients](https://arxiv.org/abs/2604.16554)

**<font color=#1a73e8>作者：</font>** Xiangkai Wang, Yun Zhao, Dongyi He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stroke patient cross-subject electroencephalography (EEG) decoding of motor imagery (MI) brain-computer interface (BCI) is essential for motor rehabilitation, yet lesion-related abnormal temporal dynamics and pronounced inter-patient heterogeneity often undermine generalization. Existing adaptation methods are easily misled by pathological slow-wave activity and unstable target-domain pseudo-labels. To address this challenge, we propose PA-TCNet, a pathology-aware temporal calibration framework with physiology-guided target refinement for stroke motor imagery decoding. PA-TCNet integrates two coordinated components. The Pathology-aware Rhythmic State Mamba (PRSM) module decomposes EEG spatiotemporal features into slowly varying rhythmic context and fast transient perturbations, injecting the fused pathological context into selective state propagation to more effectively capture abnormal temporal dynamics. The Physiology-Guided Target Calibration (PGTC) module constructs source-domain sensorimotor region-of-interest templates, imposing physiological consistency constraints and dynamically refining target-domain pseudo-labels, thereby improving adaptation reliability. Leave-one-subject-out experiments on two independent stroke EEG datasets, XW-Stroke and 2019-Stroke, yielded mean accuracies of 66.56\% and 72.75\%, respectively, outperforming state-of-the-art baselines. These results indicate that jointly modeling pathological temporal dynamics and physiology-constrained pseudo-supervision can provide more robust cross-subject initialization for personalized post-stroke MI-BCI rehabilitation. The implemented code is available at this https URL.

---


### 64. [Cross-Modal Generation: From Commodity WiFi to High-Fidelity mmWave and RFID Sensing](https://arxiv.org/abs/2604.16558)

**<font color=#1a73e8>作者：</font>** Zhixiong Yang, Long Jing, Yao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AIGC has shown remarkable success in CV and NLP, and has recently demonstrated promising potential in the wireless domain. However, significant data imbalance exists across RF modalities, with abundant WiFi data but scarce mmWave and RFID data due to high acquisition cost. This makes it difficult to train high-quality generative models for these data-scarce modalities. In this work, we propose RF-CMG, a diffusion-based cross-modal generative method that leverages data-rich WiFi signals to synthesize high-fidelity RF data for scarce modalities including mmWave and RFID. The key insight of RF-CMG is to decouple cross-modal generation into high-frequency guidance and low-frequency constraint, which respectively learn high-frequency distribution from limited target modality data and preserve the underlying physical structure via low-frequency constraints during generation. On this basis, we introduce a Modality-Guided Embedding (MGE) module to steer the reverse diffusion trajectory toward the target high-frequency distribution, and a Low-Frequency Modality Consistency (LFMC) module to progressively enforce low-frequency constraints to suppress the accumulation of source-modality structural biases during inference, enabling high-quality target-modality generation. Performance comparison with several prevalent generative models demonstrates that RF-CMG achieves superior performance in synthesizing RFID and mmWave signals. We further showcase the effectiveness of the data generated by RF-CMG in gesture recognition tasks, and analyze the impact of the proportion of synthetic data on downstream performance.

---


### 65. [Polynomial Multiproofs for Scalable Data Availability Sampling in Blockchain Light Clients](https://arxiv.org/abs/2604.16559)

**<font color=#1a73e8>作者：</font>** Rachit Anand Srivastava, Vikram Bhattacharjee, Will Arnold 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Light clients are essential for scalable blockchain systems because they verify data availability without downloading full blocks. In data availability sampling based systems, sampled cells are retrieved from a peer-to-peer network and verified against cryptographic commitments. A common deployment pattern associates each sampled cell with an independent Kate-Zaverucha-Goldberg (KZG) proof, creating substantial cumulative bandwidth, storage, and verification overhead. This paper studies polynomial multiproofs (PMP) as a mechanism for reducing these costs in blockchain light clients. We present a design in which multiple sampled cell evaluations are verified using a single aggregated proof over a shared evaluation micro-domain and describe the corresponding changes to proof generation, dissemination, retrieval, and verification in a peer-to-peer light-client stack. We instantiate and evaluate the design in Avail, a modular data availability layer for blockchains, as a case study. The results show lower proof bytes, lower verifier CPU and memory usage, and deployment-level infrastructure cost reductions of up to 45% relative to a per-cell baseline, while also clarifying the trade-offs introduced by grouped retrieval.

---


### 66. [See Through the Noise: Improving Domain Generalization in Gaze Estimation](https://arxiv.org/abs/2604.16562)

**<font color=#1a73e8>作者：</font>** Yanming Peng, Shijing Wang, Yaping Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalizable gaze estimation methods have garnered increasing attention due to their critical importance in real-world applications and have achieved significant progress. However, they often overlook the effect of label noise, arising from the inherent difficulty of acquiring precise gaze annotations, on model generalization performance. In this paper, we are the first to comprehensively investigate the negative effects of label noise on generalization in gaze estimation. Further, we propose a novel solution, called See-Through-Noise (SeeTN) framework, which improves generalization from a novel perspective of mitigating label noise. Specifically, we propose to construct a semantic embedding space via a prototype-based transformation to preserve a consistent topological structure between gaze features and continuous labels. We then measure feature-label affinity consistency to distinguish noisy from clean samples, and introduce a novel affinity regularization in the semantic manifold to transfer gaze-related information from clean to noisy samples. Our proposed SeeTN promotes semantic structure alignment and enforces domain-invariant gaze relationships, thereby enhancing robustness against label noise. Extensive experiments demonstrate that our SeeTN effectively mitigates the adverse impact of source-domain noise, leading to superior cross-domain generalization without compromising the source-domain accuracy, and highlight the importance of explicitly handling noise in generalized gaze estimation.

---


### 67. [Classification of systolic murmurs in heart sounds using multiresolution complex Gabor dictionary and vision transformer](https://arxiv.org/abs/2604.16563)

**<font color=#1a73e8>作者：</font>** Mahmoud Fakhry, Abeer FathAllah Brery  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Systolic murmurs are extra heart sounds that occur during the contraction phase of the cardiac cycle, often indicating heart abnormalities caused by turbulent blood flow. Their intensity, pitch, and quality vary, requiring precise identification for the accurate diagnosis of cardiac disorders. This study presents an automatic classification system for systolic murmurs using a feature extraction module, followed by a classification model. The feature extraction module employs complex orthogonal matching pursuit to project single or multiple murmur segments onto a redundant dictionary composed of multiresolution complex Gabor basis functions (GBFs). The resulting projection weights are split and reshaped into variable-resolution time--frequency feature matrices. Processing multiple segments of a single recording using a shared dictionary mitigates murmur variability. This is achieved by learning the weights for each segment while enforcing that they correspond to the same set of basis functions in the dictionary, promoting consistent time--frequency feature matrices. The classification model is built based on a vision transformer to process multiple input matrices of different resolutions by passing each through a convolutional neural network for patch tokenization. All embedding tokens are then concatenated to form a matrix and forwarded to an encoder layer that includes multihead attention, residual connections, and a convolutional network with a kernel size of one. This integration of multiresolution feature extraction with transformer-based feature classification enhances the accuracy and reliability of heart murmur identification. An experimental analysis of four types of systolic murmurs from the CirCor DigiScope dataset demonstrates the effectiveness of the system, achieving a classification accuracy of $95.96\%$.

---


### 68. [In Search of Lost DNA Sequence Pretraining](https://arxiv.org/abs/2604.16570)

**<font color=#1a73e8>作者：</font>** Zhijiang Tang, Jiaxin Qi, Yan Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DNA sequence encoding is fundamental to gene function prediction, protein synthesis, and diverse downstream biological tasks. Despite the substantial progress achieved by large-scale DNA sequence pretraining, existing studies have overwhelmingly emphasized pretraining scale and custom downstream evaluation datasets, while neglecting some essential components of the pretraining paradigm. In this paper, we reveal three critical yet heretofore overlooked problems in DNA pretraining: inappropriate downstream datasets, inherent flaws in the neighbor-masking strategy, and the lack of detailed discussion on vocabulary. Therefore, we undertake comprehensive investigations and propose principled guidelines, including selection criteria for evaluation datasets, guiding task design, and in-depth vocabulary analysis. Extensive experiments validate the significance of our identified problems and support the rationale behind our recommendations. Finally, we introduce a standardized testbed that enables reproducible and rigorous benchmarking of DNA pretraining methods to advance the development of genomic foundation models.

---


### 69. [From User Recognition to Activity Counting: An Identity-Agnostic Approach to Multi-User WiFi Sensing](https://arxiv.org/abs/2604.16572)

**<font color=#1a73e8>作者：</font>** Kemal Bayik, Olayinka Ajayi, Daniel Roggen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wi-Fi Channel State Information (CSI) enables device-free human activity recognition, but existing multi-user approaches assume a fixed set of known users during both training and inference. This closed-set assumption limits deployment, as models trained on a specific user set degrade when applied to new individuals or environments. We reformulate multi-user activity recognition as activity counting, estimating how many users perform each activity type at a given time, without associating actions with specific individuals. We propose a pipeline that converts CSI measurements into spatial projections and extracts features using a pretrained convolutional backbone. Two formulations are evaluated on the WiMANS dataset: a conventional identity-dependent model that assigns activities to fixed user slots, and an identity-agnostic model that estimates scene-level activity composition through regression. Under standard evaluation, the identity-agnostic model achieves a mean absolute error of 0.1081 on a 0-5 count scale. Under unseen-user evaluation, the identity-dependent model's macro-F1 drops from 80.38 to 32.61, while the identity-agnostic model's counting error remains stable. Feature space analysis confirms that identity-agnostic representations are more user-invariant, which explains their stronger generalization. These results suggest that activity counting provides a more practical and generalizable alternative to identity-dependent formulations for multi-user WiFi sensing.

---


### 70. [FedOBP: Federated Optimal Brain Personalization through Cloud-Edge Element-wise Decoupling](https://arxiv.org/abs/2604.16574)

**<font color=#1a73e8>作者：</font>** Xingyan Chen, Tian Du, Changqiao Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) faces challenges from client data heterogeneity and resource-constrained mobile devices, which can degrade model accuracy. Personalized Federated Learning (PFL) addresses this issue by adapting shared global knowledge to local data distributions. A promising approach in PFL is model decoupling, which separates the model into global and personalized parameters, raising the key question of which parameters should be personalized to balance global knowledge sharing and local adaptation. In this paper, we propose a Federated Optimal Brain Personalization (FedOBP) algorithm with a quantile-based thresholding mechanism and introduce an element-wise importance score. This score extends Optimal Brain Damage (OBD) pruning theory by incorporating a federated approximation of the first-order derivative in the Taylor expansion to evaluate the importance of each parameter for personalization. Moreover, we move the metric computation originally performed on clients to the server side, to alleviate the burden on resource-constrained mobile devices. To the best of our knowledge, this is the first work to bridge classical saliency-based pruning theory with federated parameter decoupling, providing a rigorous theoretical justification for selecting personalized parameters based on their sensitivity to local loss landscapes. Extensive experiments demonstrate that FedOBP outperforms state-of-the-art methods across diverse datasets and heterogeneity scenarios, while requiring personalization of only a very small number of personalized parameters.

---


### 71. [Evaluating Temporal and Structural Anomaly Detection Paradigms for DDoS Traffic](https://arxiv.org/abs/2604.16575)

**<font color=#1a73e8>作者：</font>** Yasmin Souza Lima, Rodrigo Moreira, Larissa F. Rodrigues Moreira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised anomaly detection is widely used to detect Distributed Denial-of-Service (DDoS) attacks in cloud-native 5G networks, yet most studies assume a fixed traffic representation, either temporal or structural, without validating which feature space best matches the data. We propose a lightweight decision framework that prioritizes temporal or structural features before training, using two diagnostics: lag-1 autocorrelation of an aggregated flow signal and PCA cumulative explained variance. When the probes are inconclusive, the framework reserves a hybrid option as a future fallback rather than an empirically validated branch. Experiments on two statistically distinct datasets with Isolation Forest, One-Class SVM, and KMeans show that structural features consistently match or outperform temporal ones, with the performance gap widening as temporal dependence weakens.

---


### 72. [Multilevel neural networks with dual-stage feature fusion for human activity recognition](https://arxiv.org/abs/2604.16577)

**<font color=#1a73e8>作者：</font>** Abeer FathAllah Brery, Ascensión Gallardo-Antolín, Israel Gonzalez-Carrasco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human activity recognition (HAR) refers to the process of identifying human actions and activities using data collected from sensors. Neural networks, such as convolutional neural networks (CNNs), long short-term memory (LSTM) networks, convolutional LSTM, and their hybrid combinations, have demonstrated exceptional performance in various research domains. Developing a multilevel individual or hybrid model for HAR involves strategically integrating multiple networks to capitalize on their complementary strengths. The structural arrangement of these components is a critical factor influencing the overall performance. This study explores a novel framework of a two-level network architecture with dual-stage feature fusion: late fusion, which combines the outputs from the first network level, and intermediate fusion, which integrates the features from both the first and second levels. We evaluated $15$ different network architectures of CNNs, LSTMs, and convolutional LSTMs, incorporating late fusion with and without intermediate fusion, to identify the optimal configuration. Experimental evaluation on two public benchmark datasets demonstrates that architectures incorporating both late and intermediate fusion achieve higher accuracy than those relying on late fusion alone. Moreover, the optimal configuration outperforms baseline models, thereby validating its effectiveness for HAR.

---


### 73. [Towards Trustworthy Depression Estimation via Disentangled Evidential Learning](https://arxiv.org/abs/2604.16579)

**<font color=#1a73e8>作者：</font>** Fangyuan Liu, Sirui Zhao, Zeyu Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated depression estimation is highly vulnerable to signal corruption and ambient noise in real-world deployment. Prevailing deterministic methods produce uncalibrated point estimates, exposing safety-critical clinical systems to the severe risk of overconfident misdiagnoses. To establish a highly resilient and trustworthy assessment paradigm, we propose EviDep, an evidential learning framework that jointly quantifies depression severity alongside aleatoric and epistemic uncertainties via a Normal-Inverse-Gamma distribution. A fundamental vulnerability in multimodal evidential fusion is the uncontrolled accumulation of cross-modal redundancies. This structural flaw artificially inflates diagnostic confidence by double-counting overlapping evidence. To guarantee robust evidence synthesis, EviDep enforces strict information integrity. First, a Frequency-aware Feature Extraction module leverages a wavelet-based Mixture-of-Experts to dynamically isolate task-irrelevant noise, preserving the fidelity of diagnostic signals. Subsequently, a Disentangled Evidential Learning strategy separates the shared consensus from modality-specific nuances. By explicitly decoupling these representations before Bayesian fusion, EviDep systematically mitigates evidence redundancy. Extensive experiments on AVEC 2013, 2014, DAIC-WOZ, and E-DAIC confirm that EviDep achieves state-of-the-art predictive accuracy and superior uncertainty calibration, delivering a robust fail-safe mechanism for trustworthy clinical screening.

---


### 74. [Continuous ageing trajectory representations for knee-aware lifetime prediction of lithium-ion batteries across heterogeneous dataset](https://arxiv.org/abs/2604.16580)

**<font color=#1a73e8>作者：</font>** Agnieszka Pregowska, Stefan Marynowicz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate assessment of lithium-ion battery ageing is challenged by cell-to-cell variability, heterogeneous cycling protocols, and limited transferability of data-driven models across datasets. In particular, robust identification of degradation transitions, such as the knee point, and reliable early-life prediction of remaining useful life (RUL) remain open problems. This study proposes a unified framework for battery ageing analysis based on continuous representations of voltage-capacity and capacity-cycle trajectories learned from heterogeneous public datasets (NASA, CALCE, ISU-ILCC). The continuous formulation enables consistent extraction of degradation descriptors, including curvature, plateau length and knee-related metrics, while reducing sensitivity to dataset-specific discretisation. Across more than 250 cells, statistically significant correlations between knee onset and end-of-life (Pearson 0.75-0.84) are observed. Additional early-life analysis confirms that knee-related features retain predictive value when estimated from partial trajectories. Early-life models provide increasingly stable RUL predictions as the number of observed cycles increases, with meaningful predictive performance emerging within the first 5-20 cycles and remain robust under cross-dataset domain shift. The framework integrates continuous modelling, feature extraction and uncertainty-aware prediction, providing an interpretable and dataset-consistent approach demonstrating robustness across heterogeneous dataset types. Compared with conventional discrete or feature-based methods, the proposed representation reduces sensitivity to sampling resolution and improves cross-dataset consistency. The study is limited to laboratory-scale datasets and capacity-based end-of-life definitions.

---


### 75. [NCO4CVRP: Neural Combinatorial Optimization for the Capacitated Vehicle Routing Problem](https://arxiv.org/abs/2604.16581)

**<font color=#1a73e8>作者：</font>** Mahir Labib Dihan, Md. Ashrafur Rahman Khan, Wasif Jalal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Combinatorial Optimization (NCO) has emerged as a powerful framework for solving combinatorial optimization problems by integrating deep learning-based models. This work focuses on improving existing inference techniques to enhance solution quality and generalization. Specifically, we modify the Random Re-Construct (RRC) approach of the Light Encoder Heavy Decoder (LEHD) model by incorporating Simulated Annealing (SA). Unlike the conventional RRC, which greedily replaces suboptimal segments, our SA-based modification introduces a probabilistic acceptance mechanism that allows the model to escape local optima and explore a more diverse solution space. Additionally, we enhance the Policy Optimization with Multiple Optima (POMO) approach by integrating Beam Search, enabling systematic exploration of multiple promising solutions while maintaining diversity in the search space. We further investigate different inference strategies, including Softmax Sampling, Greedy, Gumbel-Softmax, and Epsilon-Greedy, analyzing their impact on solution quality. Furthermore, we explore instance augmentation techniques, such as horizontal and vertical flipping and rotation-based augmentations, to improve model generalization across different CVRP instances. Our extensive experiments demonstrate that these modifications significantly reduce the optimality gap across various Capacitated Vehicle Routing Problem (CVRP) benchmarks, with Beam Search and SA-based RRC consistently yielding superior performance. By refining inference techniques and leveraging enhanced search strategies, our work contributes to the broader applicability of NCO models in real-world combinatorial optimization tasks.

---


### 76. [Camo-M3FD: A New Benchmark Dataset for Cross-Spectral Camouflaged Pedestrian Detection](https://arxiv.org/abs/2604.16582)

**<font color=#1a73e8>作者：</font>** Henry O. Velesaca, Andrea Mero, Guillermo A. Castillo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian detection is fundamental to autonomous driving, robotics, and surveillance. Despite progress in deep learning, reliable identification remains challenging due to occlusions, cluttered backgrounds, and degraded visibility. While multispectral detection-combining visible and thermal sensors-mitigates poor visibility, the challenge of camouflaged pedestrians remains largely unexplored. Existing Camouflaged Object Detection (COD) benchmarks focus on biological species, leaving a gap in safety-critical human detection where targets blend into their surroundings. To address this, we introduce Camo-M3FD (derived from the M3FD dataset), a novel benchmark for cross-spectral camouflaged pedestrian detection, consisting of registered visible-thermal image pairs. The dataset is curated using quantitative metrics to ensure high foreground-background similarity. We provide high-quality pixel-level masks and establish a standardized evaluation framework using state-of-the-art COD models. Our results demonstrate that while thermal signals provide indispensable localization cues, multispectral fusion is essential for refining structural details. Camo-M3FD serves as a foundational resource for developing robust and safety-critical detection systems. The dataset is available on GitHub: this https URL

---


### 77. [Real-Time Visual Attribution Streaming in Thinking Model](https://arxiv.org/abs/2604.16587)

**<font color=#1a73e8>作者：</font>** Seil Kang, Woojung Han, Junhyeok Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present an amortized framework for real-time visual attribution streaming in multimodal thinking models. When these models generate code from a screenshot or solve math problems from images, their long reasoning traces should be grounded in visual evidence. However, verifying this reliance is challenging: faithful causal methods require costly repeated backward passes or perturbations, while raw attention maps offer instant access, they lack causal validity. To resolve this, we introduce an amortized approach that learns to estimate the causal effects of semantic regions directly from the rich signals encoded in attention features. Across five diverse benchmarks and four thinking models, our approach achieves faithfulness comparable to exhaustive causal methods while enabling visual attribution streaming, where users observe grounding evidence as the model reasons, not after. Our results demonstrate that real-time, faithful attribution in multimodal thinking models is achievable through lightweight learning, not brute-force computation.

---


### 78. [MambaKick: Early Penalty Direction Prediction from HAR Embeddings](https://arxiv.org/abs/2604.16588)

**<font color=#1a73e8>作者：</font>** Henry O. Velesaca, David Freire-Obregon, Abel Reyes-Angulo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Penalty kicks in soccer are decided under extreme time constraints, where goalkeepers benefit from anticipating shot direction from the kickers motion before or around ball contact. In this paper, MambaKick is presented as a learning-based framework for penalty direction prediction that leverages pretrained human action recognition (HAR) embeddings extracted from contact-centered short video segments and combines them with a lightweight temporal predictor. Rather than relying on explicit kinematic reconstruction or handcrafted biomechanical features, the approach reuses transferable spatiotemporal representations and utilizes selective state-spare models (Mamba) for efficient sequence aggregation. Simple contextual metadata (e.g., field side and footedness) are also considered as complementary cues that may reduce ambiguity in real-world footage. Across a range of HAR backbones, MambaKick consistently improves or matches strong embedding baselines, achieving up to 53.1% accuracy for three classes and 64.5% for two classes under the proposed methodology. Overall, the results indicate that combining pretrained HAR representations with efficient state-space temporal modeling is a practical direction for low-latency intention prediction in real-world sports video. The code will be available at GitHub: this https URL

---


### 79. [Hybrid Spectro-Temporal Fusion Framework for Structural Health Monitoring](https://arxiv.org/abs/2604.16589)

**<font color=#1a73e8>作者：</font>** Jongyeop Kim, Jinki Kim, Doyun Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structural health monitoring plays a critical role in ensuring structural safety by analyzing vibration responses from engineering systems. This paper proposes a Spectro-Temporal Alignment framework and a Hybrid Spectro-Temporal Fusion framework that integrate arrival-time interval descriptors with spectral features to capture both fine-scale and coarse-scale vibration dynamics. Experiments conducted on data collected from an LDS V406 electrodynamic shaker demonstrate that the proposed spectro-temporal representations significantly outperform conventional input formulations. The results indicate that a temporal resolution ({\Delta}{\tau}) of 0.008 of 0.02 favors traditional machine learning models, whereas a finer resolution ({\Delta}{\tau}) of 0.008 effectively unlocks the performance potential of deep learning architectures. Beyond classification accuracy, a comprehensive stability analysis based on condensed indices, including mean performance, standard deviation, coefficient of variation, and balanced score, shows that the proposed hybrid framework consistently achieves higher accuracy with substantially lower variability compared to baseline and alignment-only approaches. Overall, these results demonstrate that the proposed framework provides a robust, accurate, and reliable solution for vibration-based structural health monitoring.

---


### 80. [Global Attention with Linear Complexity for Exascale Generative Data Assimilation in Earth System Prediction](https://arxiv.org/abs/2604.16590)

**<font color=#1a73e8>作者：</font>** Xiao Wang, Zezhong Zhang, Isaac Lyngaas 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate weather and climate prediction relies on data assimilation (DA), which estimates the Earth system state by integrating observations with models. While exascale computing has significantly advanced earth simulation, scalable and accurate inference of the Earth system state remains a fundamental bottleneck, limiting uncertainty quantification and prediction of extreme events. We introduce a unified one-stage generative DA framework that reformulates assimilation as Bayesian posterior sampling, replacing the conventional forecast-update cycle with compute-dense, GPU-efficient inference. At the core is STORM, a novel spatiotemporal transformer with a global attention linear-complexity scaling algorithm that breaks the quadratic attention barrier. On 32,768 GPUs of the Frontier supercomputer, our method achieves 63% strong scaling efficiency and 1.6 ExaFLOP sustained performance. We further scale to 20 billion spatiotemporal tokens, enabling km-scale global modeling over 177k temporal frames, regimes previously unreachable, establishing a new paradigm for Earth system prediction.

---


### 81. [Spotlights and Blindspots: Evaluation Machine-Generated Text Detection](https://arxiv.org/abs/2604.16607)

**<font color=#1a73e8>作者：</font>** Kevin Stowe, Kailash Patil  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rise of generative language models, machine-generated text detection has become a critical challenge. A wide variety of models is available, but inconsistent datasets, evaluation metrics, and assessment strategies obscure comparisons of model effectiveness. To address this, we evaluate 15 different detection models from six distinct systems, as well as seven trained models, across seven English-language textual test sets and three creative human-written datasets. We provide an empirical analysis of model performance, the influence of training and evaluation data, and the impact of key metrics. We find that no single system excels in all areas and nearly all are effective for certain tasks, and the representation of model performance is critically linked to dataset and metric choices. We find high variance in model ranks based on datasets and metrics, and overall poor performance on novel human-written texts in high-risk domains. Across datasets and metrics, we find that methodological choices that are often assumed or overlooked are essential for clearly and accurately reflecting model performance.

---


### 82. [IncepDeHazeGAN: Novel Satellite Image Dehazing](https://arxiv.org/abs/2604.16609)

**<font color=#1a73e8>作者：</font>** Tejeswar Pokuri, Shivarth Rai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dehazing is a technique in computer vision for enhancing the visual quality of images captured in cloudy or foggy conditions. Dehazing helps to recover clear, high-quality images from haze-affected remote sensing data. In this study, we introduce IncepDeHazeGAN, a novel Generative Adversarial Network (GAN) involving Inception block and multi-layer feature fusion for the task of single-image dehazing. Utilizing the Inception block allows for multi-scale feature extraction. On the other hand, the multi-layer feature fusion design achieves efficient reuse of features as the features extracted at different convolution layers are fused several times. Grad-CAM XAI technique has been applied to our network, highlighting the regions focused on by the network for dehazing and its adaptation to different haze conditions. Experiments demonstrate that our network achieves state-of-the-art results in several datasets.

---


### 83. [Lower Bounds and Proximally Anchored SGD for Non-Convex Minimization Under Unbounded Variance](https://arxiv.org/abs/2604.16620)

**<font color=#1a73e8>作者：</font>** Arda Fazla, Ege C. Kaya, Antesh Upadhyay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analysis of Stochastic Gradient Descent (SGD) and its variants typically relies on the assumption of uniformly bounded variance, a condition that frequently fails in practical non-convex settings, such as neural network training, as well as in several elementary optimization settings. While several relaxations are explored in the literature, the Blum-Gladyshev (BG-0) condition, which permits the variance to grow quadratically with distance has recently been shown to be the weakest condition. However, the study of the oracle complexity of stochastic first-order non-convex optimization under BG-0 has remained underexplored. In this paper, we address this gap and establish information-theoretic lower bounds, proving that finding an $\epsilon$-stationary point requires $\Omega(\epsilon^{-6})$ stochastic BG-0 oracle queries for smooth functions and $\Omega(\epsilon^{-4})$ queries under mean-square smoothness. These limits demonstrate an unavoidable degradation from classical bounded-variance complexities, i.e., $\Omega(\epsilon^{-4})$ and $\Omega(\epsilon^{-3})$ for smooth and mean-square smooth cases, respectively. To match these lower bounds, we consider Proximally Anchored STochastic Approximation (PASTA), a unified algorithmic framework that couples Halpern anchoring with Tikhonov regularization to dynamically mitigate the extra variance explosion term permitted by the BG-0 oracle. We prove that PASTA achieves minimax optimal complexities across numerous non-convex regimes, including standard smooth, mean-square smooth, weakly convex, star-convex, and Polyak-Lojasiewicz functions, entirely under an unbounded domain and unbounded stochastic gradients.

---


### 84. [Amortized Inverse Kinematics via Graph Attention for Real-Time Human Avatar Animation](https://arxiv.org/abs/2604.16629)

**<font color=#1a73e8>作者：</font>** Muhammad Saif Ullah Khan, Chen-Yu Wang, Tim Prokosch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inverse kinematics (IK) is a core operation in animation, robotics, and biomechanics: given Cartesian constraints, recover joint rotations under a known kinematic tree. In many real-time human avatar pipelines, the available signal per frame is a sparse set of tracked 3D joint positions, whereas animation systems require joint orientations to drive skinning. Recovering full orientations from positions is underconstrained, most notably because twist about bone axes is ambiguous, and classical IK solvers typically rely on iterative optimization that can be slow and sensitive to noisy inputs. We introduce IK-GAT, a lightweight graph-attention network that reconstructs full-body joint orientations from 3D joint positions in a single forward pass. The model performs message passing over the skeletal parent-child graph to exploit kinematic structure during rotation inference. To simplify learning, IK-GAT predicts rotations in a bone-aligned world-frame representation anchored to rest-pose bone frames. This parameterization makes the twist axis explicit and is exactly invertible to standard parent-relative local rotations given the kinematic tree and rest pose. The network uses a continuous 6D rotation representation and is trained with a geodesic loss on SO(3) together with an optional forward-kinematics consistency regularizer. IK-GAT produces animation-ready local rotations that can directly drive a rigged avatar or be converted to pose parameters of SMPL-like body models for real-time and online applications. With 374K parameters and over 650 FPS on CPU, IK-GAT outperforms VPoser-based per-frame iterative optimization without warm-start at significantly lower cost, and is robust to initial pose and input noise

---


### 85. [Tri-Modal Fusion Transformers for UAV-based Object Detection](https://arxiv.org/abs/2604.16630)

**<font color=#1a73e8>作者：</font>** Craig Iaboni, Pramod Abichandani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable UAV object detection requires robustness to illumination changes, motion blur, and scene dynamics that suppress RGB cues. Thermal long-wave infrared (LWIR) sensing preserves contrast in low light, and event cameras retain microsecond-level temporal edges, but integrating all three modalities in a unified detector has not been systematically studied. We present a tri-modal framework that processes RGB, thermal, and event data with a dual-stream hierarchical vision transformer. At selected encoder depths, a Modality-Aware Gated Exchange (MAGE) applies inter-sensor channel and spatial gating, and a Bidirectional Token Exchange (BiTE) module performs bidirectional token-level attention with depthwise-pointwise refinement, producing resolution-preserving fused maps for a standard feature pyramid and two-stage detector.
We introduce a 10,489-frame UAV dataset with synchronized and pre-aligned RGB-thermal-event streams and 24,223 annotated vehicles across day and night flights. Through 61 controlled ablations, we evaluate fusion placement, mechanism (baseline MAGE+BiTE, CSSA, GAFF), modality subsets, and backbone capacity. Tri-modal fusion improves over all dual-modal baselines, with fusion depth having a significant effect and a lightweight CSSA variant recovering most of the benefit at minimal cost. This work provides the first systematic benchmark and modular backbone for tri-modal UAV-based object detection.

---


### 86. [FRIGID: Scaling Diffusion-Based Molecular Generation from Mass Spectra at Training and Inference Time](https://arxiv.org/abs/2604.16648)

**<font color=#1a73e8>作者：</font>** Montgomery Bohde, Hongxuan Liu, Mrunali Manjrekar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we present FRIGID, a framework with a novel diffusion language model that generates molecular structures conditioned on mass spectra via intermediate fingerprint representations and determined chemical formulae, training at the scale of hundreds of millions of unlabeled structures. We then demonstrate how forward fragmentation models enable inference-time scaling by identifying spectrum-inconsistent fragments and refining them through targeted remasking and denoising. While FRIGID already achieves strong performance with its diffusion base, inference-time scaling significantly improves its accuracy, surpassing 18% Top-1 accuracy on the challenging MassSpecGym benchmark and tripling the Top-1 accuracy of the leading methods on NPLIB1. Further empirical analyses show that FRIGID exhibits log-linear performance scaling with increasing inference-time compute, opening a promising new direction for continued improvements in de novo structural elucidation. FRIGID code is publicly available at this https URL

---


### 87. [FLARE: A Data-Efficient Surrogate for Predicting Displacement Fields in Directed Energy Deposition](https://arxiv.org/abs/2604.16649)

**<font color=#1a73e8>作者：</font>** Kittipong Thiamchaiboonthawee, Ghadi Nehme, Ram Mohan Telikicherla 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Directed energy deposition (DED) produces complex thermo-mechanical responses that can lead to distortion and reduced dimensional accuracy of a manufactured part. Thermo-mechanical finite element simulations are widely used to estimate these effects, but their computational cost and the complexity of accurately capturing DED physics limit their use in design iteration and process optimization. This paper introduces FLARE (Field Prediction via Linear Affine Reconstruction in wEight-space), a data-efficient surrogate modeling framework for predicting post-cooling displacement fields in DED from geometric and process parameters. We develop a predefined-geometry DED simulation workflow using an open-source finite element framework and generate a dataset of simulations with varying geometry, laser power, and deposition velocity. Each simulation provides full-field displacement, stress, strain, and temperature data throughout the manufacturing process. FLARE encodes each simulation as an implicit neural field and regularizes the corresponding neural-network weights so that they follow the affine structure of the input parameter space. This enables prediction of unseen parameter combinations by reconstructing network weights through affine mixing of training examples. On this DED benchmark, the method shows improved accuracy compared to baseline methods in both in-distribution and extrapolation settings. Although the present study focuses on DED displacement prediction, the proposed affine weight-space reconstruction framework offers a promising approach for data-efficient surrogate modeling of physical fields.

---


### 88. [Migrant Voices, Local News: Insights on Bridging Community Needs with Media Content](https://arxiv.org/abs/2604.16651)

**<font color=#1a73e8>作者：</font>** David Alonso del Barrio, Paula Dolores Rescala, Victor Bros 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Research shows news consumption differs across demographics, yet little is known about non-mainstream audiences, especially in relation to local media. Our study addresses this gap by examining how French-speaking migrants in a mid-size European city engage with local news, and whether their needs are reflected in coverage. Eight community members participated in focus groups, whose insights guided the selection of natural language processing methods (topic modeling, information retrieval, sentiment analysis, and readability) applied to over 2000 hyper-local news articles. Results showed that while articles frequently covered local events, gaps remained in topics important to participants. Sentiment analysis revealed a generally positive tone, and readability measures indicated an intermediate-advanced French level, raising questions about accessibility for integration. Our work contributes to bridging the gap between local news platforms' content and diverse readers' needs, and could inform local media organizations about opportunities to expand their current news story coverage to appeal to more diverse audiences.

---


### 89. [IYKYK (But AI Doesn't): Automated Content Moderation Does Not Capture Communities' Heterogeneous Attitudes Towards Reclaimed Language](https://arxiv.org/abs/2604.16654)

**<font color=#1a73e8>作者：</font>** Christina Chance, Rebecca Pattichis, Arjun Subramonian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reclaimed slur usage is a common and meaningful practice online for many marginalized communities. It serves as a source of solidarity, identity, and shared experience. However, contemporary automated and AI-based moderation tools for online content largely fail to distinguish between reclaimed and hateful uses of slurs, resulting in the suppression of marginalized voices. In this work, we use quantitative and qualitative methods to examine the attitudes of social media users in LGBTQIA+, Black, and women communities around reclaimed slurs targeting our focus groups including the f-word, n-word, and b-word. With social media users from these communities, we collect and analyze an annotated online slur usage corpus. The corpus includes annotators' perceptions of whether an online text containing a slur should be flagged as hate speech, as well as contextual features of the slur usage. Across all communities and annotation questions, we observe low inter-annotator agreement, indicating substantial disagreement among in-group annotators. This is compounded by the fact that, absent clear contextual signals of identity and intent, even in-group members may disagree on how to interpret reclaimed slur usage online. Semi-structured interviews with annotators suggest that differences in lived experience and personal history contribute to this variation as well. We find poor alignment between annotator judgments and automated hate speech assessments produced by Perspective API. We further observe that certain features of a text such as whether the slur usage was derogatory and if the slur was targeted at oneself are more associated with whether annotators report the text as hate speech. Together, these findings highlight the inherent subjectivity and contextual nature of how marginalized communities interpret slurs online.

---


### 90. [A Benchmark Study of Segmentation Models and Adaptation Strategies for Landslide Detection from Satellite Imagery](https://arxiv.org/abs/2604.16663)

**<font color=#1a73e8>作者：</font>** Md Kowsher, Weiwei Zhan, Chen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Landslide detection from high resolution satellite imagery is a critical task for disaster response and risk assessment, yet the relative effectiveness of modern segmentation architectures and finetuning strategies for this problem remains insufficiently understood. In this work, we present a systematic benchmarking study of convolutional neural networks, transformer based segmentation models, and large pre-trained foundation models for landslide detection. Using the Globally Distributed Coseismic Landslide Dataset (GDCLD) dataset, we evaluate representative CNN- and transformer-based segmentation models alongside large pretrained foundation models under consistent training and evaluation protocols. In addition, we compare full fine-tuning with parameter-efficient fine-tuning methods, including LoRA and AdaLoRA, to assess their performance efficiency tradeoffs. Experimental results show that transformer-based models achieve strong segmentation performance, while parameter efficient finetuning reduces trainable parameters by up to 95% with comparable accuracy to full finetuning. We further analyze generalization under distribution shift by comparing validation and held-out test performance.

---


### 91. [Stringology Based Cryptology](https://arxiv.org/abs/2604.16669)

**<font color=#1a73e8>作者：</font>** Victor Kebande  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The modern cryptographic primitives are known to generate large volumes of sequential data like keystreams, ciphertext blocks, and hash outputs. Traditional cryptgraphic evaluation methods rely primarily on statistical randomness tests and algebraic cryptanalysis techniques. This paper introduces the concept of Stringology-Based Cryptology (SBC), which applies classical string processing and pattern matching techniques to analyze structural properties of cryptographic outputs. By interpreting cryptographic outputs as symbolic sequences, stringology algorithms can be used to detect pattern recurrence, substring distributions, and structural correlations. In addition, the paper demonstrate how pattern frequency analysis and substring recurrence metrics can be applied to evaluate keystream outputs generated by stream ciphers. Experimental results illustrate that SBC analysis provides complementary insights into structural characteristics of cryptographic sequences and may support future research in structural cryptanalysis and cryptographic evaluation

---


### 92. [Appearance-free Action Recognition: Zero-shot Generalization in Humans and a Two-Pathway Model](https://arxiv.org/abs/2604.16675)

**<font color=#1a73e8>作者：</font>** Prerana Kumar, Martin A. Giese  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action recognition is a fundamental ability for social species. Yet, its underlying computations are not well understood. Classical psychophysical studies using simplified stimuli have shown that humans can perceive body motion even under degradation of relevant shape cues. Recent work using real-world action videos and their appearance-free counterparts (that preserve motion but lack static shape cues) included explicit training of humans and models on the appearance-free videos. Whether humans and vision models generalize in a zero-shot manner to appearance-free transformations of real-world action videos is not yet known. To measure this generalization in humans, we conducted a laboratory-based psychophysics experiment. 22 participants were trained to recognize five action categories using naturalistic videos (UCF5 dataset), and tested zero-shot on two types of appearance-free transformations: (i) dense-noise motion videos from an existing dataset (AFD5) and (ii) random-dot appearance-free videos. We find that participants recognize actions in both types of appearance-free videos well above chance, albeit with reduced accuracy compared to naturalistic videos. To model this behavior, we developed a two-pathway 3D CNN-based model combining an RGB (form) stream and an optical flow (motion) stream, including a coherence-gating mechanism inspired by Gestalt common-fate grouping. Our model generalizes to both appearance-free datasets and outperforms contemporary video classification models, narrowing the gap to human performance. We find that the motion pathway is critical for generalization to appearance-free videos, while the form pathway improves performance on naturalistic videos. Our findings highlight the importance of motion-based representations for generalization to appearance-free videos, and support the use of multi-stream architectures to model video-based action recognition.

---


### 93. [C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion](https://arxiv.org/abs/2604.16680)

**<font color=#1a73e8>作者：</font>** Yuval Haitman, Amit Efraim, Joseph M. Francos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce C-GenReg, a training-free framework for 3D point cloud registration that leverages the complementary strengths of world-scale generative priors and registration-oriented Vision Foundation Models (VFMs). Current learning-based 3D point cloud registration methods struggle to generalize across sensing modalities, sampling differences, and environments. Hence, C-GenReg augments the geometric point cloud registration branch by transferring the matching problem into an auxiliary image domain, where VFMs excel, using a World Foundation Model to synthesize multi-view-consistent RGB representations from the input geometry. This generative transfer, preserves spatial coherence across source and target views without any fine-tuning. From these generated views, a VFM pretrained for finding dense correspondences extracts matches. The resulting pixel correspondences are lifted back to 3D via the original depth maps. To further enhance robustness, we introduce a "Match-then-Fuse" probabilistic cold-fusion scheme that combines two independent correspondence posteriors, that of the generated-RGB branch with that of the raw geometric branch. This principled fusion preserves each modality inductive bias and provides calibrated confidence without any additional learning. C-GenReg is zero-shot and plug-and-play: all modules are pretrained and operate without fine-tuning. Extensive experiments on indoor (3DMatch, ScanNet) and outdoor (Waymo) benchmarks demonstrate strong zero-shot performance and superior cross-domain generalization. For the first time, we demonstrate a generative registration framework that operates successfully on real outdoor LiDAR data, where no imagery data is available.

---


### 94. [DARLING: Detection Augmented Reinforcement Learning with Non-Stationary Guarantees](https://arxiv.org/abs/2604.16684)

**<font color=#1a73e8>作者：</font>** Argyrios Gerogiannis, Yu-Han Huang, Venugopal V. Veeravalli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study model-free reinforcement learning (RL) in non-stationary finite-horizon episodic Markov decision processes (MDPs) without prior knowledge of the non-stationarity. We focus on the piecewise-stationary (PS) setting, where both the reward and transition dynamics can change an arbitrary number of times. We propose Detection Augmented Reinforcement Learning (DARLING), a modular wrapper for PS-RL that applies to both tabular and linear MDPs, without knowledge of the changes. Under certain change-point separation and reachability conditions, DARLING improves the best available dynamic regret bounds in both settings and yields strong empirical performance. We further establish the first minimax lower bounds for PS-RL in tabular and linear MDPs, showing that DARLING is the first nearly optimal algorithm. Experiments on standard benchmarks demonstrate that DARLING consistently surpasses the state-of-the-art methods across diverse non-stationary scenarios.

---


### 95. [Graph Transformer-Based Pathway Embedding for Cancer Prognosis](https://arxiv.org/abs/2604.16685)

**<font color=#1a73e8>作者：</font>** Koushik Howlader, Md Tauhidul Islam, Wei Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of cancer progression remains a challenge due to the high heterogeneity of molecular omics data across patients. While biologically informed models have improved the interpretability of these predictions, a persistent limitation lies in how they encode individual genes to construct pathway representations. Existing hierarchical models typically derive gene features by directly mapping raw molecular inputs, whereas integration frameworks often rely on simple statistical aggregations of patient-level signals. These approaches often fail to explicitly learn a shared base representation for each gene, thereby limiting the expressiveness and biological accuracy of downstream pathway embeddings. To address this, we introduce PATH, a modulation-based, patient-conditioned gene embedding strategy. PATH represents a paradigm shift by starting from a shared base embedding for each gene, preserving a stable biological identity across the population, and then dynamically adapting it using patient-specific copy number variation (CNV) and mutation signals. This allows the model to capture subtle individual molecular variations while maintaining a consistent latent understanding of the gene itself. We integrate PATH into a graph transformer framework that models interactions among biologically connected pathways through pathway-guided attention. Across pancancer metastasis prediction, PATH achieves an F1 score of 0.8766, representing an 8.8 percent improvement over the current SOTA multi-omics benchmarks. Beyond superior predictive accuracy, our approach identifies biologically meaningful pathways and, crucially, reveals disease-state-specific pathway rewiring, offering new insights into the evolving pathway-pathway interactions that drive cancer progression.

---


### 96. [No-Worse Context-Aware Decoding: Preventing Neutral Regression in Context-Conditioned Generation](https://arxiv.org/abs/2604.16686)

**<font color=#1a73e8>作者：</font>** Yufei Tao, Ameeta Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can answer questions and summarize documents when conditioned on external contexts (e.g., retrieved evidence), yet context use remains unreliable: models may overwrite an already-correct output (neutral regression) even when the context is non-informative. We formalize neutral regression as a do-no-harm requirement and quantify it by measuring accuracy drops on baseline-correct items under answer-consistent contexts. We propose No-Worse Context-Aware Decoding (NWCAD), a decode-time adapter built on a two-stream setup with a two-stage gate: it backs off to no-context decoding when the context is non-informative, and otherwise uses context-conditioned decoding with a CAD-style fallback under uncertainty. We evaluate NWCAD on benchmarks that separate do-no-harm reliability from context utilization (accuracy gains on genuinely helpful contexts). NWCAD prevents neutral regression on baseline-correct items while preserving strong context-driven accuracy on helpful contexts.

---


### 97. [The Query Channel: Information-Theoretic Limits of Masking-Based Explanations](https://arxiv.org/abs/2604.16689)

**<font color=#1a73e8>作者：</font>** Erciyes Karakaya, Ozgur Ercetin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Masking-based post-hoc explanation methods, such as KernelSHAP and LIME, estimate local feature importance by querying a black-box model under randomized perturbations. This paper formulates this procedure as communication over a query channel, where the latent explanation acts as a message and each masked evaluation is a channel use. Within this framework, the complexity of the explanation is captured by the entropy of the hypothesis class, while the query interface supplies information at a rate determined by an identification capacity per query. We derive a strong converse showing that, if the explanation rate exceeds this capacity, the probability of exact recovery necessarily converges to one in error for any sequence of explainers and decoders. We also prove an achievability result establishing that a sparse maximum-likelihood decoder attains reliable recovery when the rate lies below capacity. A Monte Carlo estimator of mutual information yields a non-asymptotic query benchmark that we use to compare optimal decoding with Lasso- and OLS-based procedures that mirror LIME and KernelSHAP. Experiments reveal a range of query budgets where information theory permits reliable explanations but standard convex surrogates still fail. Finally, we interpret super-pixel resolution and tokenization for neural language models as a source-coding choice that sets the entropy of the explanation and show how Gaussian noise and nonlinear curvature degrade the query channel, induce waterfall and error-floor behavior, and render high-resolution explanations unattainable.

---


### 98. [RankGuide: Tensor-Rank-Guided Routing and Steering for Efficient Reasoning](https://arxiv.org/abs/2604.16694)

**<font color=#1a73e8>作者：</font>** Jiayi Tian, Yupeng Su, Ryan Solgi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) enhance problem-solving capabilities by generating explicit multi-step chains of thought (CoT) reasoning; however, they incur substantial inference latency and computational overhead. To mitigate this issue, recent works have explored model collaboration paradigms, where small reasoning models (SRMs) generate intermediate reasoning steps to achieve a better accuracy--latency trade-off. Despite recent progress, effectively and efficiently detecting and mitigating SRM failures in collaborative systems remains a key challenge. To address this issue, we analyze SRM inference in both the generated text and hidden-state spaces, and identify three types of failure modes: \textit{overconfidence}, \textit{uncertainty}, and \textit{heavy revalidation}. Building on these insights, we propose \textbf{RankGuide}, a framework that improves the efficiency and effectiveness of SRM--LRM collaboration through tensor-rank-guided routing and steering. Specifically, RankGuide leverages a routing signal that incorporates tensor-rank signals derived from consecutive hidden states to detect when SRMs are likely to fail and selectively invoke LRMs. In addition, we introduce a tensor-rank-filtered steering vector extraction method to modulate the reasoning trajectory of SRMs, thereby improving their generation quality. By improving both routing and steering through tensor-rank signals, RankGuide enables SRM--LRM collaborative systems to achieve more efficient reasoning with fewer steps and improved accuracy. Experiments on multiple reasoning benchmarks demonstrate the efficacy of RankGuide in reducing latency by up to $1.75\times$ compared to LRM, while maintaining competitive accuracy relative to prior methods.

---


### 99. [LOD-Net: Locality-Aware 3D Object Detection Using Multi-Scale Transformer Network](https://arxiv.org/abs/2604.16696)

**<font color=#1a73e8>作者：</font>** Mustaqeem Khan, Aidana Nurakhmetova, Wail Gueaieb 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D object detection in point cloud data remains a challenging task due to the sparsity and lack of global structure inherent in the input. In this work, we propose a novel Multi-Scale Attention (MSA) mechanism integrated into the 3DETR architecture to better capture both local geometry and global context. Our method introduces an upsampling operation that generates high-resolution feature maps, enabling the network to better detect smaller and semantically related objects. Experiments conducted on the ScanNetv2 dataset demonstrate that our 3DETR + MSA model improves detection performance, achieving a gain of almost 1% in mAP@25 and 4.78% in mAP@50 over the baseline. While applying MSA to the 3DETR-m variant shows limited improvement, our analysis reveals the importance of adapting the upsampling strategy for lightweight models. These results highlight the effectiveness of combining hierarchical feature extraction with attention mechanisms in enhancing 3D scene understanding.

---


### 100. [Glitch in the Sky: Exploiting Voltage Fault Injection in UAV Flight Controllers](https://arxiv.org/abs/2604.16699)

**<font color=#1a73e8>作者：</font>** Yun-Ping Hsiao, Yanda Li, Youssef Gamal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Cyber-Physical Systems (CPS) become increasingly pervasive and autonomous, ensuring the resilience of their embedded logic is critical to maintaining safety and integrity. Among the most stealthy and damaging threats are non-invasive fault injection attacks, where hardware-level disturbances propagate into software execution and compromise control logic. In this paper, we investigate the susceptibility of Unmanned Aerial Vehicle (UAV) autopilot fail-safe mechanisms to voltage glitch fault injection. We introduce a dual evaluation approach: software-based fault simulation using ARMORY and hardware-based experiments with a voltage glitching platform (Chip-Whisperer), applying controlled and timely faults to an STM32 microcontroller running UAV-Autopilot fail-safe logic. Our targeted analysis of specific fail-safe modes uncovers timing-sensitive vulnerabilities that can suppress or alter safety responses, such as disabling emergency failsafe activation at critical moments, potentially enabling UAV hijacking. Furthermore, we validate software-based fault injection results against real hardware behavior, demonstrating how simulated attacks translate into tangible risks for CPS security and reliability.

---


> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
