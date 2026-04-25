# 📦 其他研究 | 2026年04月26日

> 本类共 **231** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-231**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-231**

---

### 201. [Inferring High-Level Events from Timestamped Data: Complexity and Medical Applications](https://arxiv.org/abs/2604.21793)

**<font color=#1a73e8>作者：</font>** Yvon K. Awuklu, Meghyn Bienvenu, Katsumi Inoue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we develop a novel logic-based approach to detecting high-level temporally extended events from timestamped data and background knowledge. Our framework employs logical rules to capture existence and termination conditions for simple temporal events and to combine these into meta-events. In the medical domain, for example, disease episodes and therapies are inferred from timestamped clinical observations, such as diagnoses and drug administrations stored in patient records, and can be further combined into higher-level disease events. As some incorrect events might be inferred, we use constraints to identify incompatible combinations of events and propose a repair mechanism to select preferred consistent sets of events. While reasoning in the full framework is intractable, we identify relevant restrictions that ensure polynomial-time data complexity. Our prototype system implements core components of the approach using answer set programming. An evaluation on a lung cancer use case supports the interest of the approach, both in terms of computational feasibility and positive alignment of our results with medical expert opinions. While strongly motivated by the needs of the healthcare domain, our framework is purposely generic, enabling its reuse in other areas.

---


### 202. [Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems](https://arxiv.org/abs/2604.21794)

**<font color=#1a73e8>作者：</font>** Ye Yu, Heming Liu, Haibo Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems built on large language models have shown strong performance on complex reasoning tasks, yet most work focuses on agent roles and orchestration while treating inter-agent communication as a fixed interface. Latent communication through internal representations such as key-value caches offers a promising alternative to text-based protocols, but existing approaches do not jointly optimize communication with multi-agent reasoning. Therefore we propose DiffMAS, a training framework that treats latent communication as a learnable component of multi-agent systems. DiffMAS performs parameter-efficient supervised training over multi-agent latent trajectories, enabling agents to jointly learn how information should be encoded and interpreted across interactions. Experiments on mathematical reasoning, scientific QA, code generation, and commonsense benchmarks show that DiffMAS consistently improves reasoning accuracy and decoding stability over single-agent inference, text-based multi-agent systems, and prior latent communication methods, achieving 26.7% on AIME24, 20.2% on GPQA-Diamond, and consistent gains across reasoning benchmarks.

---


### 203. [An effective variant of the Hartigan $k$-means algorithm](https://arxiv.org/abs/2604.21798)

**<font color=#1a73e8>作者：</font>** François Clément, Stefan Steinerberger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The k-means problem is perhaps the classical clustering problem and often synonymous with Lloyd's algorithm (1957). It has become clear that Hartigan's algorithm (1975) gives better results in almost all cases, Telgarsky-Vattani note a typical improvement of $5\%$ -- $10\%$. We point out that a very minor variation of Hartigan's method leads to another $2\%$ -- $5\%$ improvement; the improvement tends to become larger when either dimension or $k$ increase.

---


### 204. [SyMTRS: Benchmark Multi-Task Synthetic Dataset for Depth, Domain Adaptation and Super-Resolution in Aerial Imagery](https://arxiv.org/abs/2604.21801)

**<font color=#1a73e8>作者：</font>** Safouane El Ghazouali, Nicola Venturi, Michael Rueegsegger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in deep learning for remote sensing rely heavily on large annotated datasets, yet acquiring high-quality ground truth for geometric, radiometric, and multi-domain tasks remains costly and often infeasible. In particular, the lack of accurate depth annotations, controlled illumination variations, and multi-scale paired imagery limits progress in monocular depth estimation, domain adaptation, and super-resolution for aerial scenes. We present SyMTRS, a large-scale synthetic dataset generated using a high-fidelity urban simulation pipeline. The dataset provides high-resolution RGB aerial imagery (2048 x 2048), pixel-perfect depth maps, night-time counterparts for domain adaptation, and aligned low-resolution variants for super-resolution at x2, x4, and x8 scales. Unlike existing remote sensing datasets that focus on a single task or modality, SyMTRS is designed as a unified multi-task benchmark enabling joint research in geometric understanding, cross-domain robustness, and resolution enhancement. We describe the dataset generation process, its statistical properties, and its positioning relative to existing benchmarks. SyMTRS aims to bridge critical gaps in remote sensing research by enabling controlled experiments with perfect geometric ground truth and consistent multi-domain supervision. The results obtained in this work can be reproduced from this Github repository: this https URL.

---


### 205. [TEMA: Anchor the Image, Follow the Text for Multi-Modification Composed Image Retrieval](https://arxiv.org/abs/2604.21806)

**<font color=#1a73e8>作者：</font>** Zixu Li, Yupeng Hu, Zhiheng Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) is an important image retrieval paradigm that enables users to retrieve a target image using a multimodal query that consists of a reference image and modification text. Although research on CIR has made significant progress, prevailing setups still rely simple modification texts that typically cover only a limited range of salient changes, which induces two limitations highly relevant to practical applications, namely Insufficient Entity Coverage and Clause-Entity Misalignment. In order to address these issues and bring CIR closer to real-world use, we construct two instruction-rich multi-modification datasets, M-FashionIQ and M-CIRR. In addition, we propose TEMA, the Text-oriented Entity Mapping Architecture, which is the first CIR framework designed for multi-modification while also accommodating simple modifications. Extensive experiments on four benchmark datasets demonstrate that TEMA's superiority in both original and multi-modification scenarios, while maintaining an optimal balance between retrieval accuracy and computational efficiency. Our codes and constructed multi-modification dataset (M-FashionIQ and M-CIRR) are available at this https URL.

---


### 206. [Quotient-Space Diffusion Models](https://arxiv.org/abs/2604.21809)

**<font color=#1a73e8>作者：</font>** Yixian Xu, Yusong Wang, Shengjie Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based generative models have reformed generative AI, and have enabled new capabilities in the science domain, for example, generating 3D structures of molecules. Due to the intrinsic problem structure of certain tasks, there is often a symmetry in the system, which identifies objects that can be converted by a group action as equivalent, hence the target distribution is essentially defined on the quotient space with respect to the group. In this work, we establish a formal framework for diffusion modeling on a general quotient space, and apply it to molecular structure generation which follows the special Euclidean group $\text{SE}(3)$ symmetry. The framework reduces the necessity of learning the component corresponding to the group action, hence simplifies learning difficulty over conventional group-equivariant diffusion models, and the sampler guarantees recovering the target distribution, while heuristic alignment strategies lack proper samplers. The arguments are empirically validated on structure generation for small molecules and proteins, indicating that the principled quotient-space diffusion model provides a new framework that outperforms previous symmetry treatments.

---


### 207. [Multiscale Super Resolution without Image Priors](https://arxiv.org/abs/2604.21810)

**<font color=#1a73e8>作者：</font>** Daniel Fu, Gabby Litterio, Pedro Felzenszwalb 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the ambiguities in the super-resolution problem under translation. We demonstrate that combinations of low-resolution images at different scales can be used to make the super-resolution problem well posed. Such differences in scale can be achieved using sensors with different pixel sizes (as demonstrated here) or by varying the effective pixel size through changes in optical magnification (e.g., using a zoom lens). We show that images acquired with pairwise coprime pixel sizes lead to a system with a stable inverse, and furthermore, that super-resolution images can be reconstructed efficiently using Fourier domain techniques or iterative least squares methods. Our mathematical analysis provides an expression for the expected error of the least squares reconstruction for large signals assuming i.i.d. noise that elucidates the noise-resolution tradeoff. These results are validated through both one- and two-dimensional experiments that leverage charge-coupled device (CCD) hardware binning to explore reconstructions over a large range of effective pixel sizes. Finally, two-dimensional reconstructions for a series of targets are used to demonstrate the advantages of multiscale super-resolution, and implications of these results for common imaging systems are discussed.

---


### 208. [Probably Approximately Consensus: On the Learning Theory of Finding Common Ground](https://arxiv.org/abs/2604.21811)

**<font color=#1a73e8>作者：</font>** Carter Blair, Ben Armstrong, Shiri Alouf-Heffetz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A primary goal of online deliberation platforms is to identify ideas that are broadly agreeable to a community of users through their expressed preferences. Yet, consensus elicitation should ideally extend beyond the specific statements provided by users and should incorporate the relative salience of particular topics. We address this issue by modelling consensus as an interval in a one-dimensional opinion space derived from potentially high-dimensional data via embedding and dimensionality reduction. We define an objective that maximizes expected agreement within a hypothesis interval where the expectation is over an underlying distribution of issues, implicitly taking into account their salience. We propose an efficient Empirical Risk Minimization (ERM) algorithm and establish PAC-learning guarantees. Our initial experiments demonstrate the performance of our algorithm and examine more efficient approaches to identifying optimal consensus regions. We find that through selectively querying users on an existing sample of statements, we can reduce the number of queries needed to a practical number.

---


### 209. [Divide-then-Diagnose: Weaving Clinician-Inspired Contexts for Ultra-Long Capsule Endoscopy Videos](https://arxiv.org/abs/2604.21814)

**<font color=#1a73e8>作者：</font>** Bowen Liu, Li Yang, Shanshan Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Capsule endoscopy (CE) enables non-invasive gastrointestinal screening, but current CE research remains largely limited to frame-level classification and detection, leaving video-level analysis underexplored. To bridge this gap, we introduce and formally define a new task, diagnosis-driven CE video summarization, which requires extracting key evidence frames that covers clinically meaningful findings and making accurate diagnoses from those evidence frames. This setting is challenging because diagnostically relevant events are extremely sparse and can be overwhelmed by tens of thousands of redundant normal frames, while individual observations are often ambiguous due to motion blur, debris, specular highlights, and rapid viewpoint changes. To facilitate research in this direction, we introduce VideoCAP, the first CE dataset with diagnosis-driven annotations derived from real clinical reports. VideoCAP comprises 240 full-length videos and provides realistic supervision for both key evidence frame extraction and diagnosis. To address this task, we further propose DiCE, a clinician-inspired framework that mirrors the standard CE reading workflow. DiCE first performs efficient candidate screening over the raw video, then uses a Context Weaver to organize candidates into coherent diagnostic contexts that preserve distinct lesion events, and an Evidence Converger to aggregate multi-frame evidence within each context into robust clip-level judgments. Experiments show that DiCE consistently outperforms state-of-the-art methods, producing concise and clinically reliable diagnostic summaries. These results highlight diagnosis-driven contextual reasoning as a promising paradigm for ultra-long CE video summarization.

---


### 210. [GFlowState: Visualizing the Training of Generative Flow Networks Beyond the Reward](https://arxiv.org/abs/2604.21830)

**<font color=#1a73e8>作者：</font>** Florian Holeczek, Andreas Hinterreiter, Alex Hernandez-Garcia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present GFlowState, a visual analytics system designed to illuminate the training process of Generative Flow Networks (GFlowNets or GFNs). GFlowNets are a probabilistic framework for generating samples proportionally to a reward function. While GFlowNets have proved to be powerful tools in applications such as molecule and material discovery, their training dynamics remain difficult to interpret. Standard machine learning tools allow metric tracking but do not reveal how models explore the sample space, construct sample trajectories, or shift sampling probabilities during training. Our solution, GFlowState, allows users to analyze sampling trajectories, compare the sample space relative to reference datasets, and analyze the training dynamics. To this end, we introduce multiple views, including a chart of candidate rankings, a state projection, a node-link diagram of the trajectory network, and a transition heatmap. These visualizations enable GFlowNet developers and users to investigate sampling behavior and policy evolution, and to identify underexplored regions and sources of training failure. Case studies demonstrate how the system supports debugging and assessing the quality of GFlowNets across application domains. By making the structural dynamics of GFlowNets observable, our work enhances their interpretability and can accelerate GFlowNet development in practice.

---


### 211. [TraceScope: Interactive URL Triage via Decoupled Checklist Adjudication](https://arxiv.org/abs/2604.21840)

**<font color=#1a73e8>作者：</font>** Haolin Zhang, William Reber, Yuxuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern phishing campaigns increasingly evade snapshot-based URL classifiers using interaction gates (e.g., checkbox/slider challenges), delayed content rendering, and logo-less credential harvesters. This shifts URL triage from static classification toward an interactive forensics task: an analyst must actively navigate the page while isolating themselves from potential runtime exploits.
We present TraceScope, a decoupled triage pipeline that operationalizes this workflow at scale. To prevent the observer effect and ensure safety, a sandboxed operator agent drives a real GUI browser guided by visual motivation to elicit page behavior, freezing the session into an immutable evidence bundle. Separately, an adjudicator agent circumvents LLM context limitations by querying evidence on demand to verify a MITRE ATT&CK checklist, and generates an audit-ready report with extracted indicators of compromise (IOCs) and a final verdict.
Evaluated on 708 reachable URLs from existing dataset (241 verified phishing from PhishTank and 467 benign from Tranco-derived crawling), TraceScope achieves 0.94 precision and 0.78 recall, substantially improving recall over three prior visual/reference-based classifiers while producing reproducible, analyst-grade evidence suitable for review. More importantly, we manually curated a dataset of real-world phishing emails to evaluate our system in a practical setting. Our evaluation reveals that TraceScope demonstrates superior performance in a real-world scenario as well, successfully detecting sophisticated phishing attempts that current state-of-the-art defenses fail to identify.

---


### 212. [Cross-Modal Phantom: Coordinated Camera-LiDAR Spoofing Against Multi-Sensor Fusion in Autonomous Vehicles](https://arxiv.org/abs/2604.21841)

**<font color=#1a73e8>作者：</font>** Shahriar Rahman Khan, Raiful Hasan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous Vehicles (AVs) increasingly depend on Multi-Sensor Fusion (MSF) to combine complementary modalities such as cameras and LiDAR for robust perception. While this redundancy is intended to safeguard against single-sensor failures, the fusion process itself introduces a subtle and underexplored vulnerability. In this work, we investigate whether an attacker can bypass MSF's redundancy by fabricating cross-sensor consistency, making multiple sensors agree on the same false object. We design a coordinated, data-level (early-fusion) attack that emulates the outcome of two synchronized physical spoofing sources: an infrared (IR) projection that induces a false camera detection and a LiDAR signal injection that produces a matching 3D point cluster. Rather than implementing the physical attack hardware, we simulate its sensor-level outcomes by inserting perspective-aware image patches and synthetic LiDAR point clusters aligned in 3D space. This approach preserves the perceptual effects that real IR and IEMI-based spoofing would create at the sensor output. Using 400 KITTI scenes, our large-scale evaluation shows that the coordinated spoofing deceives a state-of-the-art perception model with an 85.5% successful attack rate. These findings provide the first quantitative evidence that malicious cross-modal consistency can compromise MSF-based perception, revealing a critical vulnerability in the core data-fusion logic of modern autonomous vehicle systems.

---


### 213. [Bounding the Black Box: A Statistical Certification Framework for AI Risk Regulation](https://arxiv.org/abs/2604.21854)

**<font color=#1a73e8>作者：</font>** Natan Levy, Gadi Perl  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence now decides who receives a loan, who is flagged for criminal investigation, and whether an autonomous vehicle brakes in time. Governments have responded: the EU AI Act, the NIST Risk Management Framework, and the Council of Europe Convention all demand that high-risk systems demonstrate safety before deployment. Yet beneath this regulatory consensus lies a critical vacuum: none specifies what ``acceptable risk'' means in quantitative terms, and none provides a technical method for verifying that a deployed system actually meets such a threshold. The regulatory architecture is in place; the verification instrument is not.
This gap is not theoretical. As the EU AI Act moves into full enforcement, developers face mandatory conformity assessments without established methodologies for producing quantitative safety evidence - and the systems most in need of oversight are opaque statistical inference engines that resist white-box scrutiny.
This paper provides the missing instrument. Drawing on the aviation certification paradigm, we propose a two-stage framework that transforms AI risk regulation into engineering practice. In Stage One, a competent authority formally fixes an acceptable failure probability $\delta$ and an operational input domain $\varepsilon$ - a normative act with direct civil liability implications. In Stage Two, the RoMA and gRoMA statistical verification tools compute a definitive, auditable upper bound on the system's true failure rate, requiring no access to model internals and scaling to arbitrary architectures. We demonstrate how this certificate satisfies existing regulatory obligations, shifts accountability upstream to developers, and integrates with the legal frameworks that exist today.

---


### 214. [Grounding Video Reasoning in Physical Signals](https://arxiv.org/abs/2604.21873)

**<font color=#1a73e8>作者：</font>** Alibay Osmanli, Zixu Cheng, Shaogang Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical video understanding requires more than naming an event correctly. A model can answer a question about pouring, sliding, or collision from textual regularities while still failing to localize the event in time or space. We introduce a grounded benchmark for physical video understanding that extends the what--when--where evaluation structure of V-STaR to four video sources, six physics domains, three prompt families (physics, vstar_like, and neutral_rstr), and four input conditions (original, shuffled, ablated, and frame-masked). The benchmark contains 1,560 base video clips from SSV2, YouCook2, HoloAssist, and Roundabout-TAU. Each clip is first converted into a shared grounded event record, and the three query families are derived from that record. Temporal and spatial targets are shared across prompt families, while the non-physics families use deterministic family-appropriate semantic a_what targets derived from the same record. Across models and prompt families, physics remains the strongest regime overall, vstar_like is the clearest non-physics semantic comparison, and neutral_rstr behaves as a harder templated control. Prompt-family robustness is selective rather than universal, perturbation gains cluster in weak original cases, and spatial grounding is the weakest across settings. These results suggest that video Q&A reasoning benchmarks shall report physically grounded, prompt-aware, and perturbation-aware diagnostics alongside aggregate accuracy.

---


### 215. [Gradual Voluntary Participation: A Framework for Participatory AI Governance in Journalism](https://arxiv.org/abs/2604.21878)

**<font color=#1a73e8>作者：</font>** Matilde Barbini, Stefano Sorrentino, Daniel Gatica-Perez  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The integration of AI into journalism challenges participatory design (PD), particularly with respect to stakeholder influence, workplace perceptions, and organizational dynamics. Traditional PD assumes that users can shape technologies, yet AI systems resist influence due to opaque data, fixed architectures, and inaccessible objectives. Through interviews with 10 journalists, we identify the perception gap, showing that trust in AI depends on perceived agency within workplace participatory workflows. Informed by these findings, we introduce the Gradual Voluntary Participation (GVP) framework in journalism and its five core principles, reconceptualizing participation as a gradual and voluntary process that can be operationalized at the newsroom level, beyond fixed workshops or one-time preference-elicitation campaigns. Addressing epistemic burdens, participatory ceilings, and performative consultations, GVP treats gradualism and voluntariness as design dimensions that shape perception, legitimacy, and ownership. Moving beyond unidimensional ladder metaphors and adopting a bidimensional matrix structure, the framework maps stakeholders across depth and scope, offering a new model for local participatory AI governance that balances technological transformation with stakeholder empowerment in rapidly evolving hybrid workplaces.

---


### 216. [Addressing Image Authenticity When Cameras Use Generative AI](https://arxiv.org/abs/2604.21879)

**<font color=#1a73e8>作者：</font>** Umar Masud, Abhijith Punnappurath, Luxi Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The ability of generative AI (GenAI) methods to photorealistically alter camera images has raised awareness about the authenticity of images shared online. Interestingly, images captured directly by our cameras are considered authentic and faithful. However, with the increasing integration of deep-learning modules into cameras' capture-time hardware -- namely, the image signal processor (ISP) -- there is now a potential for hallucinated content in images directly output by our cameras. Hallucinated capture-time image content is typically benign, such as enhanced edges or texture, but in certain operations, such as AI-based digital zoom or low-light image enhancement, hallucinations can potentially alter the semantics and interpretation of the image content. As a result, users may not realize that the content in their camera images is not authentic. This paper addresses this issue by enabling users to recover the 'unhallucinated' version of the camera image to avoid misinterpretation of the image content. Our approach works by optimizing an image-specific multi-layer perceptron (MLP) decoder together with a modality-specific encoder so that, given the camera image, we can recover the image before hallucinated content was added. The encoder and MLP are self-contained and can be applied post-capture to the image without requiring access to the camera ISP. Moreover, the encoder and MLP decoder require only 180 KB of storage and can be readily saved as metadata within standard image formats such as JPEG and HEIC.

---


### 217. [TingIS: Real-time Risk Event Discovery from Noisy Customer Incidents at Enterprise Scale](https://arxiv.org/abs/2604.21889)

**<font color=#1a73e8>作者：</font>** Jun Wang, Ziyin Zhang, Rui Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-time detection and mitigation of technical anomalies are critical for large-scale cloud-native services, where even minutes of downtime can result in massive financial losses and diminished user trust. While customer incidents serve as a vital signal for discovering risks missed by monitoring, extracting actionable intelligence from this data remains challenging due to extreme noise, high throughput, and semantic complexity of diverse business lines. In this paper, we present TingIS, an end-to-end system designed for enterprise-grade incident discovery. At the core of TingIS is a multi-stage event linking engine that synergizes efficient indexing techniques with Large Language Models (LLMs) to make informed decisions on event merging, enabling the stable extraction of actionable incidents from just a handful of diverse user descriptions. This engine is complemented by a cascaded routing mechanism for precise business attribution and a multi-dimensional noise reduction pipeline that integrates domain knowledge, statistical patterns, and behavioral filtering. Deployed in a production environment handling a peak throughput of over 2,000 messages per minute and 300,000 messages per day, TingIS achieves a P90 alert latency of 3.5 minutes and a 95\% discovery rate for high-priority incidents. Benchmarks constructed from real-world data demonstrate that TingIS significantly outperforms baseline methods in routing accuracy, clustering quality, and Signal-to-Noise Ratio.

---


### 218. [EVENT5Ws: A Large Dataset for Open-Domain Event Extraction from Documents](https://arxiv.org/abs/2604.21890)

**<font color=#1a73e8>作者：</font>** Praval Sharma, Ashok Samal, Leen-Kiat Soh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Event extraction identifies the central aspects of events from text. It supports event understanding and analysis, which is crucial for tasks such as informed decision-making in emergencies. Therefore, it is necessary to develop automated event extraction approaches. However, existing datasets for algorithm development have limitations, including limited coverage of event types in closed-domain settings and a lack of large, manually verified dataset in open-domain settings. To address these limitations, we create EVENT5Ws , a large, manually annotated, and statistically verified open-domain event extraction dataset. We design a systematic annotation pipeline to create the dataset and provide empirical insights into annotation complexity. Using EVENT5Ws, we evaluate state-of-the-art pre-trained large language models and establish a benchmark for future research. We further show that models trained on EVENT5Ws generalize effectively to datasets from different geographical contexts, which demonstrates its potential for developing generalizable algorithms. Finally, we summarize the lessons learned during the dataset development and provide recommendations to support future large-scale dataset development.

---


### 219. [Mapping the Political Discourse in the Brazilian Chamber of Deputies: A Multi-Faceted Computational Approach](https://arxiv.org/abs/2604.21897)

**<font color=#1a73e8>作者：</font>** Flávio Soriano, Victoria F. Mello, Pedro B. Rigueira 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Analyses of legislative behavior often rely on voting records, overlooking the rich semantic and rhetorical content of political speech. In this paper, we ask three complementary questions about parliamentary discourse: how things are said, what is being said, and who is speaking in discursively similar ways. To answer these questions, we introduce a scalable and generalizable computational framework that combines diachronic stylometric analysis, contextual topic modeling, and semantic clustering of deputies' speeches. We apply this framework to a large-scale case study of the Brazilian Chamber of Deputies, using a corpus of over 450,000 speeches from 2003 to 2025. Our results show a long-term stylistic shift toward shorter and more direct speeches, a legislative agenda that reorients sharply in response to national crises, and a granular map of discursive alignments in which regional and gender identities often prove more salient than formal party affiliation. More broadly, this work offers a robust methodology for analyzing parliamentary discourse as a multidimensional phenomenon that complements traditional vote-based approaches.

---


### 220. [GiVA: Gradient-Informed Bases for Vector-Based Adaptation](https://arxiv.org/abs/2604.21901)

**<font color=#1a73e8>作者：</font>** Neeraj Gangwar, Rishabh Deshmukh, Michael Shavlovsky 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As model sizes continue to grow, parameter-efficient fine-tuning has emerged as a powerful alternative to full fine-tuning. While LoRA is widely adopted among these methods, recent research has explored vector-based adaptation methods due to their extreme parameter efficiency. However, these methods typically require substantially higher ranks than LoRA to match its performance, leading to increased training costs. This work introduces GiVA, a gradient-based initialization strategy for vector-based adaptation. It achieves training times comparable to LoRA and maintains the extreme parameter efficiency of vector-based adaptation. We evaluate GiVA across diverse benchmarks, including natural language understanding, natural language generation, and image classification. Experiments show that our approach consistently outperforms or achieves performance competitive with existing vector-based adaptation methods and LoRA while reducing rank requirements by a factor of eight ($8\times$).

---


### 221. [A Scale-Adaptive Framework for Joint Spatiotemporal Super-Resolution with Diffusion Models](https://arxiv.org/abs/2604.21903)

**<font color=#1a73e8>作者：</font>** Max Defez, Filippo Quarenghi, Mathieu Vrac 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep-learning video super-resolution has progressed rapidly, but climate applications typically super-resolve (increase resolution) either space or time, and joint spatiotemporal models are often designed for a single pair of super-resolution (SR) factors (upscaling spatial and temporal ratio between the low-resolution sequence and the high-resolution sequence), limiting transfer across spatial resolutions and temporal cadences (frame rates). We present a scale-adaptive framework that reuses the same architecture across factors by decomposing spatiotemporal SR into a deterministic prediction of the conditional mean, with attention, and a residual conditional diffusion model, with an optional mass-conservation (same precipitation amount in inputs and outputs) transform to preserve aggregated totals. Assuming that larger SR factors primarily increase underdetermination (hence required context and residual uncertainty) rather than changing the conditional-mean structure, scale adaptivity is achieved by retuning three factor-dependent hyperparameters before retraining: the diffusion noise schedule amplitude beta (larger for larger factors to increase diversity), the temporal context length L (set to maintain comparable attention horizons across cadences) and optionally a third, the mass-conservation function f (tapered to limit the amplification of extremes for large factors). Demonstrated on reanalysis precipitation over France (Comephore), the same architecture spans super-resolution factors from 1 to 25 in space and 1 to 6 in time, yielding a reusable architecture and tuning recipe for joint spatiotemporal super-resolution across scales.

---


### 222. [UniGenDet: A Unified Generative-Discriminative Framework for Co-Evolutionary Image Generation and Generated Image Detection](https://arxiv.org/abs/2604.21904)

**<font color=#1a73e8>作者：</font>** Yanran Zhang, Wenzhao Zheng, Yifei Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, significant progress has been made in both image generation and generated image detection. Despite their rapid, yet largely independent, development, these two fields have evolved distinct architectural paradigms: the former predominantly relies on generative networks, while the latter favors discriminative frameworks. A recent trend in both domains is the use of adversarial information to enhance performance, revealing potential for synergy. However, the significant architectural divergence between them presents considerable challenges. Departing from previous approaches, we propose UniGenDet: a Unified generative-discriminative framework for co-evolutionary image Generation and generated image Detection. To bridge the task gap, we design a symbiotic multimodal self-attention mechanism and a unified fine-tuning algorithm. This synergy allows the generation task to improve the interpretability of authenticity identification, while authenticity criteria guide the creation of higher-fidelity images. Furthermore, we introduce a detector-informed generative alignment mechanism to facilitate seamless information exchange. Extensive experiments on multiple datasets demonstrate that our method achieves state-of-the-art performance. Code: \href{this https URL}{this https URL}.

---


### 223. [Low-Rank Adaptation Redux for Large Models](https://arxiv.org/abs/2604.21905)

**<font color=#1a73e8>作者：</font>** Bingcong Li, Yilang Zhang, Georgios B. Giannakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.

---


### 224. [Directional Confusions Reveal Divergent Inductive Biases Through Rate-Distortion Geometry in Human and Machine Vision](https://arxiv.org/abs/2604.21909)

**<font color=#1a73e8>作者：</font>** Leyla Roksan Caglar, Pedro A.M. Mediano, Baihan Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans and modern vision models can reach similar classification accuracy while making systematically different kinds of mistakes - differing not in how often they err, but in who gets mistaken for whom, and in which direction. We show that these directional confusions reveal distinct inductive biases that are invisible to accuracy alone. Using matched human and deep vision model responses on a natural-image categorization task under 12 perturbation types, we quantify asymmetry in confusion matrices and link it to generalization geometry through a Rate-Distortion (RD) framework, summarized by three geometric signatures (slope (beta), curvature (kappa)) and efficiency (AUC). We find that humans exhibit broad but weak asymmetries, whereas deep vision models show sparser, stronger directional collapses. Robustness training reduces global asymmetry but fails to recover the human-like breadth-strength profile of graded similarity. Mechanistic simulations further show that different asymmetry organizations shift the RD frontier in opposite directions, even when matched for performance. Together, these results position directional confusions and RD geometry as compact, interpretable signatures of inductive bias under distribution shift.

---


### 225. [Vista4D: Video Reshooting with 4D Point Clouds](https://arxiv.org/abs/2604.21915)

**<font color=#1a73e8>作者：</font>** Kuan Heng Lin, Zhizheng Liu, Pablo Salamanca 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Vista4D, a robust and flexible video reshooting framework that grounds the input video and target cameras in a 4D point cloud. Specifically, given an input video, our method re-synthesizes the scene with the same dynamics from a different camera trajectory and viewpoint. Existing video reshooting methods often struggle with depth estimation artifacts of real-world dynamic videos, while also failing to preserve content appearance and failing to maintain precise camera control for challenging new trajectories. We build a 4D-grounded point cloud representation with static pixel segmentation and 4D reconstruction to explicitly preserve seen content and provide rich camera signals, and we train with reconstructed multiview dynamic data for robustness against point cloud artifacts during real-world inference. Our results demonstrate improved 4D consistency, camera control, and visual quality compared to state-of-the-art baselines under a variety of videos and camera paths. Moreover, our method generalizes to real-world applications such as dynamic scene expansion and 4D scene recomposition. See our project page for results, code, and models: this https URL

---


### 226. [CrossCommitVuln-Bench: A Dataset of Multi-Commit Python Vulnerabilities Invisible to Per-Commit Static Analysis](https://arxiv.org/abs/2604.21917)

**<font color=#1a73e8>作者：</font>** Arunabh Majumdar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present CrossCommitVuln-Bench, a curated benchmark of 15 real-world Python vulnerabilities (CVEs) in which the exploitable condition was introduced across multiple commits - each individually benign to per-commit static analysis - but collectively critical. We manually annotate each CVE with its contributing commit chain, a structured rationale for why each commit evades per-commit analysis, and baseline evaluations using Semgrep and Bandit in both per-commit and cumulative scanning modes. Our central finding: the per-commit detection rate (CCDR) is 13% across all 15 vulnerabilities - 87% of chains are invisible to per-commit SAST. Critically, both per-commit detections are qualitatively poor: one occurs on commits framed as security fixes (where developers suppress the alert), and the other detects only the minor hardcoded-key component while completely missing the primary vulnerability (200+ unprotected API endpoints). Even in cumulative mode (full codebase present), the detection rate is only 27%, confirming that snapshot-based SAST tools often miss vulnerabilities whose introduction spans multiple commits. The dataset, annotation schema, evaluation scripts, and reproducible baselines are released under open-source licenses to support research on cross-commit vulnerability detection.

---


### 227. [Context Unrolling in Omni Models](https://arxiv.org/abs/2604.21921)

**<font color=#1a73e8>作者：</font>** Ceyuan Yang, Zhijie Lin, Yang Zhao 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.

---


### 228. [The Sample Complexity of Multicalibration](https://arxiv.org/abs/2604.21923)

**<font color=#1a73e8>作者：</font>** Natalie Collina, Jiuyao Lu, Georgy Noarov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $\kappa > 0$, in the regime $|G|\le \varepsilon^{-\kappa}$, we prove that $\widetilde{\Theta}(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetilde{\Theta}(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $\kappa = 0$, the sample complexity of multicalibration remains $\widetilde{\Theta}(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon.
More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.

---


### 229. [Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs](https://arxiv.org/abs/2604.21926)

**<font color=#1a73e8>作者：</font>** Hao-Yu Hsu, Tianhang Cheng, Jing Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.

---


### 230. [Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability](https://arxiv.org/abs/2604.21930)

**<font color=#1a73e8>作者：</font>** Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.

---


### 231. [Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931)

**<font color=#1a73e8>作者：</font>** Yen-Siang Wu, Rundong Luo, Jingsen Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.

---


> [!TIP]
> 当前位于：**201-231**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-231**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
