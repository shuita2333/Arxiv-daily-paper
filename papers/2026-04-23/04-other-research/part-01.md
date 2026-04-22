# 📦 其他研究 | 2026年04月23日

> 本类共 **244** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-244](./part-05.md)

---

### 1. [CentaurTA Studio: A Self-Improving Human-Agent Collaboration System for Thematic Analysis](https://arxiv.org/abs/2604.18589)

**<font color=#1a73e8>作者：</font>** Lei Wang, Min Huang, Eduard Dragut  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Thematic analysis is difficult to scale: manual workflows are labor-intensive, while fully automated pipelines often lack controllability and transparent evaluation. We present \textbf{CentaurTA Studio}, a web-based system for self-improving human--agent collaboration in open coding and theme construction. The system integrates (1) a two-stage human feedback pipeline separating simulator drafting and expert validation, (2) persistent prompt optimization that distills validated feedback into reusable alignment principles, and (3) rubric-based evaluation with early stopping for process control.
Across three domains, CentaurTA achieves the strongest performance in both Open Coding and Theme Construction, reaching up to 92.12\% accuracy and consistently outperforming baseline systems. Agreement between the rubric-based LLM judge and human annotators reaches substantial reliability (average $\kappa = 0.68$). Ablation studies show that removing the feedback loop reduces performance from 90\% to 81\%, while eliminating the Critic or early stopping degrades accuracy or increases interaction cost. The full system reaches peak performance within 10 iterative rounds (about 25 minutes), demonstrating improved efficiency over expert-only refinement.

---


### 2. [Critical Thinking in the Age of Artificial Intelligence: A Survey-Based Study with Machine Learning Insights](https://arxiv.org/abs/2604.18590)

**<font color=#1a73e8>作者：</font>** M Murshidul Bari, Akif Islam, Mohd Ruhul Ameen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growing use of artificial intelligence (AI) in education, professional work, and everyday problem-solving has raised important questions about its effect on human reasoning. While AI can improve efficiency, save time, and support learning, repeated dependence on it may also encourage cognitive offloading, reduce productive struggle, and weaken independent critical thinking. This paper investigates the relationship between AI-use behavior and critical-thinking performance through an interview-based survey combined with short logic and reasoning tasks. The findings reveal a mixed pattern: participants largely viewed AI as a tool for speed, convenience, and learning support, yet many also reported reduced patience for sustained effort. Objective reasoning performance varied considerably across individuals, and the analyses suggest that reduced patience and stronger dependence-related tendencies are more closely associated with lower reasoning performance than background characteristics alone. Exploratory clustering further indicates that AI users do not form a single homogeneous group, but instead reflect tentative behavioral profiles, including over-reliant users, mixed-strategy users, and balanced support-seekers. Although the findings are exploratory, they indicate that AI does not affect critical thinking in a uniformly negative or positive way. Instead, its influence appears to depend on the manner in which it is used. The paper therefore argues that effective human-AI collaboration should support reflection, verification, and sustained cognitive effort rather than substitute for them.

---


### 3. [SPRITE: From Static Mockups to Engine-Ready Game UI](https://arxiv.org/abs/2604.18591)

**<font color=#1a73e8>作者：</font>** Yunshu Bai, RuiHao Li, Hao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Game UI implementation requires translating stylized mockups into interactive engine entities. However, current "Screenshot-to-Code" tools often struggle with the irregular geometries and deep visual hierarchies typical of game interfaces. To bridge this gap, we introduce SPRITE, a pipeline that transforms static screenshots into editable engine assets. By integrating Vision-Language Models (VLMs) with a structured YAML intermediate representation, SPRITE explicitly captures complex container relationships and non-rectangular layouts. We evaluated SPRITE against a curated Game UI benchmark and conducted expert reviews with professional developers to assess reconstruction fidelity and prototyping efficiency. Our findings demonstrate that SPRITE streamlines development by automating tedious coding and resolving complex nesting. By facilitating rapid in-engine iteration, SPRITE effectively blurs the boundaries between artistic design and technical implementation in game development. Project page: this https URL

---


### 4. [Can We Build Scene Graphs, Not Classify Them? FlowSG: Progressive Image-Conditioned Scene Graph Generation with Flow Matching](https://arxiv.org/abs/2604.18623)

**<font color=#1a73e8>作者：</font>** Xin Hu, Ke Qin, Wen Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene Graph Generation (SGG) unifies object localization and visual relationship reasoning by predicting boxes and subject-predicate-object triples. Yet most pipelines treat SGG as a one-shot, deterministic classification problem rather than a genuinely progressive, generative task. We propose FlowSG, which recasts SGG as continuous-time transport on a hybrid discrete-continuous state: starting from a noised graph, the model progressively grows an image-conditioned scene graph through constraint-aware refinements that jointly synthesize nodes (objects) and edges (predicates). Specifically, we first leverage a VQ-VAE to quantize a scene graph (e.g., continuous visual features) into compact, predictable tokens; a graph Transformer then (i) predicts a conditional velocity field to transport continuous geometry (boxes) and (ii) updates discrete posteriors for categorical tokens (object features and predicate labels), coupling semantics and geometry via flow-conditioned message aggregation. Training combines flow-matching losses for geometry with a discrete-flow objective for tokens, yielding few-step inference and plug-and-play compatibility with standard detectors and segmenters. Extensive experiments on VG and PSG under closed- and open-vocabulary protocols show consistent gains in predicate R/mR and graph-level metrics, validating the mixed discrete-continuous generative formulation over one-shot classification baselines, with an average improvement of about 3 points over the state-of-the-art USG-Par.

---


### 5. [Vision-Based Human Awareness Estimation for Enhanced Safety and Efficiency of AMRs in Industrial Warehouses](https://arxiv.org/abs/2604.18627)

**<font color=#1a73e8>作者：</font>** Maximilian Haug, Christian Stippel, Lukas Pscherer 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ensuring human safety is of paramount importance in warehouse environments that feature mixed traffic of human workers and autonomous mobile robots (AMRs). Current approaches often treat humans as generic dynamic obstacles, leading to conservative AMR behaviors like slowing down or detouring, even when workers are fully aware and capable of safely sharing space. This paper presents a real-time vision-based method to estimate human awareness of an AMR using a single RGB camera. We integrate state-of-the-art 3D human pose lifting with head orientation estimation to ascertain a human's position relative to the AMR and their viewing cone, thereby determining if the human is aware of the AMR. The entire pipeline is validated using synthetically generated data within NVIDIA Isaac Sim, a robust physics-accurate robotics simulation environment. Experimental results confirm that our system reliably detects human positions and their attention in real time, enabling AMRs to safely adapt their motion based on human awareness. This enhancement is crucial for improving both safety and operational efficiency in industrial and factory automation settings.

---


### 6. [StomaD2: An All-in-One System for Intelligent Stomatal Phenotype Analysis via Diffusion-Based Restoration Detection Network](https://arxiv.org/abs/2604.18632)

**<font color=#1a73e8>作者：</font>** Quanling Zhao, Meng'en Qin, Yanfeng Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stomata play a crucial role in regulating plant physiological processes and reflecting environmental responses. However, accurate and high-throughput stomatal phenotyping remains challenging, as conventional approaches rely on destructive sampling and manual annotation, restricting large-scale and field deployment. To overcome these limitations, a noninvasive restoration-detection integrated framework, termed StomaD2, is developed to achieve accurate and fast stomatal phenotyping under complex imaging conditions. The framework incorporates a diffusion-based restoration module to recover degraded images and a specialized rotated object detection network tailored to the small, dense, and cluttered characteristics of stomata. The proposed network enhances feature representation through three key innovations: a column-wise structure for global feature interaction, context-aware resampling and reweighting mechanism to improve multi-scale consistency, and a feature reassembly module to boost discrimination against complex backgrounds. In extensive comparisons, StomaD2 demonstrated state-of-the-art performance. On public Maize and Wheat datasets, it achieved accuracies of 0.994 and 0.992, respectively, significantly outperforming existing benchmarks. When benchmarked against ten other advanced models, including Oriented Former and YOLOv12, StomaD2 achieved a top-tier F1-score/mAP of 0.989. The framework is integrated into a user-friendly, field-operable system that supports the fast extraction of eight stomatal phenotypes, such as density and conductance. Validated on more than 130 plant species, StomaD2's results highlight its strong generalizability and potential for large-scale phenotyping, plant physiology analysis, and precision agriculture applications.

---


### 7. [Global Web, Local Privacy? An International Review of Web Tracking](https://arxiv.org/abs/2604.18633)

**<font color=#1a73e8>作者：</font>** Harry Yu, Patton Yin, Sebastian Zimmeck  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web tracking by ad networks, social networks, and other third parties is privacy-invasive. To protect users' privacy an increasing number of countries are adopting new privacy laws. However, a major reason why their application on the web is so challenging is that privacy laws are local while the web is global. To that end, we evaluate websites' tracker connections for ten countries for two sets of sites -- the global Common Top 525 and the Country-specific Top 525 sites. We find that Australia and the US (California) -- two of the three opt-out jurisdictions in our study -- have the highest level of web tracking while opt-in jurisdictions generally have lower levels. We also find that the Common Top 525 sites have 50.5\% fewer average tracker connections when accessed from EU countries compared to non-EU countries. Further, simply not interacting with cookie banners decreases trackers by 48.5\% for Germany, as measured for a sample of 36 Common Top 525 sites. These results suggest that the General Data Protection Regulation and the ePrivacy Directive have a tangible effect in reducing tracking. As 28\% of Common Top 525 sites show cookie banners in all ten countries, our results suggest a moderate Brussels effect. However, against the backdrop of global US ad tech practices, EU law primarily acts as a Brussels shield. Generally, we think that strong enforcement of privacy laws is key to increase user privacy on the web.

---


### 8. [FASE : A Fairness-Aware Spatiotemporal Event Graph Framework for Predictive Policing](https://arxiv.org/abs/2604.18644)

**<font color=#1a73e8>作者：</font>** Pronob Kumar Barman, Pronoy Kumar Barman, Plaban Kumar Barman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive policing systems that allocate patrol resources based solely on predicted crime risk can unintentionally amplify racial disparities through feedback driven data bias. We present FASE, a Fairness Aware Spatiotemporal Event Graph framework, which integrates spatiotemporal crime prediction with fairness constrained patrol allocation and a closed loop deployment feedback simulator.
We model Baltimore as a graph of 25 ZIP Code Tabulation Areas and use 139,982 Part 1 crime incidents from 2017 to 2019 at hourly resolution, producing a sparse feature tensor. The prediction module combines a spatiotemporal graph neural network with a multivariate Hawkes process to capture spatial dependencies and self exciting temporal dynamics. Outputs are modeled using a Zero Inflated Negative Binomial distribution, suitable for overdispersed and zero heavy crime counts. The model achieves a validation loss of 0.4800 and a test loss of 0.4857.
Patrol allocation is formulated as a fairness constrained linear optimization problem that maximizes risk weighted coverage while enforcing a Demographic Impact Ratio constraint with deviation bounded by 0.05. Across six simulated deployment cycles, fairness remains within 0.9928 to 1.0262, and coverage ranges from 0.876 to 0.936. However, a persistent detection rate gap of approximately 3.5 percentage points remains between minority and non minority areas. This result shows that allocation level fairness constraints alone do not eliminate feedback induced bias in retraining data, highlighting the need for fairness interventions across the full pipeline.

---


### 9. [On Solving the Multiple Variable Gapped Longest Common Subsequence Problem](https://arxiv.org/abs/2604.18645)

**<font color=#1a73e8>作者：</font>** Marko Djukanović, Nikola Balaban, Christian Blum 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper addresses the Variable Gapped Longest Common Subsequence (VGLCS) problem, a generalization of the classical LCS problem involving flexible gap constraints between consecutive solutions' characters. The problem arises in molecular sequence comparison, where structural distance constraints between residues must be respected, and in time-series analysis where events are required to occur within specified temporal delays. We propose a search framework based on the root-based state graph representation, in which the state space comprises a generally large number of rooted state subgraphs. To cope with the resulting combinatorial explosion, an iterative beam search strategy is employed, dynamically maintaining a global pool of promising candidate root nodes, enabling effective control of diversification across iterations. To exploit the search for high-quality solutions, several known heuristics from the LCS literature are utilized into the standalone beam search procedure. To the best of our knowledge, this is the first comprehensive computational study on the VGLCS problem comprising 320 synthetic instances with up to 10 input sequences and up to 500 characters. Experimental results show robustness of the designed approach over the baseline beam search in comparable runtimes.

---


### 10. [DanceCrafter: Fine-Grained Text-Driven Controllable Dance Generation via Choreographic Syntax](https://arxiv.org/abs/2604.18648)

**<font color=#1a73e8>作者：</font>** Hang Yuan, Xiaolin Hu, Yan Wan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven controllable dance generation remains under-explored, primarily due to the severe scarcity of high-quality datasets and the inherent difficulty of articulating complex choreographies. Characterizing dance is particularly challenging owing to its intricate spatial dynamics, strong directionality, and the highly decoupled movements of distinct body parts. To overcome these bottlenecks, we bridge principles from dance studies, human anatomy, and biomechanics to propose \textit{Choreographic Syntax}, a novel theoretical framework with a tailored annotation system. Grounded in this syntax, we combine professional dance archives with high-fidelity motion capture data to construct \textbf{DanceFlow}, the most fine-grained dance dataset to date. It encompasses 41 hours of high-quality motions paired with 6.34 million words of detailed descriptions. At the model level, we introduce \textbf{DanceCrafter}, a tailored motion transformer built upon the Momentum Human Rig. To circumvent optimization instabilities, we construct a continuous manifold motion representation paired with a hybrid normalization strategy. Furthermore, we design an anatomy-aware loss to explicitly regulate the decoupled nature of body parts. Together, these adaptations empower DanceCrafter to achieve the high-fidelity and stable generation of complex dance sequences. Extensive evaluations and user studies demonstrate our state-of-the-art performance in motion quality, fine-grained controllability, and generation naturalness.

---


### 11. [Position: No Retroactive Cure for Infringement during Training](https://arxiv.org/abs/2604.18649)

**<font color=#1a73e8>作者：</font>** Satoru Utsunomiya, Masaru Isonuma, Junichiro Mori 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As generative AI faces intensifying legal challenges, the machine learning community has increasingly relied on post-hoc mitigation -- especially machine unlearning and inference-time guardrails -- to argue for compliance. This paper argues that such post-hoc mitigation methods cannot retroactively cure liability from unlawful acquisition and training, because compliance hinges on data lineage, not the outputs. Our argument has three parts. First, unauthorized copying/ingestion can be a legally complete completed act, and model weights may operate as fixed copies that retain training-derived expressive value, making later filtering beside the point for infringement. Second, contract and tort/unfair-competition rules -- via licenses, terms of service, and anti-free-riding principles -- can independently restrict access and use, often bypassing copyright defenses (e.g., fair use or TDM exceptions). Third, since value from protected inputs can persist in weights, remedies such as unjust enrichment and disgorgement may require stripping gains and, in some cases, reaching the model itself. We therefore argue for a shift from Post-Hoc Sanitization to verifiable Ex-Ante Process Compliance.

---


### 12. [Owner-Harm: A Missing Threat Model for AI Agent Safety](https://arxiv.org/abs/2604.18658)

**<font color=#1a73e8>作者：</font>** Dongcheng Zhang, Yiqing Jiang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing AI agent safety benchmarks focus on generic criminal harm (cybercrime, harassment, weapon synthesis), leaving a systematic blind spot for a distinct and commercially consequential threat category: agents harming their own deployers. Real-world incidents illustrate the gap: Slack AI credential exfiltration (Aug 2024), Microsoft 365 Copilot calendar-injection leaks (Jan 2024), and a Meta agent unauthorized forum post exposing operational data (Mar 2026). We propose Owner-Harm, a formal threat model with eight categories of agent behavior damaging the deployer. We quantify the defense gap on two benchmarks: a compositional safety system achieves 100% TPR / 0% FPR on AgentHarm (generic criminal harm) yet only 14.8% (4/27; 95% CI: 5.9%-32.5%) on AgentDojo injection tasks (prompt-injection-mediated owner harm). A controlled generic-LLM baseline shows the gap is not inherent to owner-harm (62.7% vs. 59.3%, delta 3.4 pp) but arises from environment-bound symbolic rules that fail to generalize across tool vocabularies. On a post-hoc 300-scenario owner-harm benchmark, the gate alone achieves 75.3% TPR / 3.3% FPR; adding a deterministic post-audit verifier raises overall TPR to 85.3% (+10.0 pp) and Hijacking detection from 43.3% to 93.3%, demonstrating strong layer complementarity. We introduce the Symbolic-Semantic Defense Generalization (SSDG) framework relating information coverage to detection rate. Two SSDG experiments partially validate it: context deprivation amplifies the detection gap 3.4x (R = 3.60 vs. R = 1.06); context injection reveals structured goal-action alignment, not text concatenation, is required for effective owner-harm detection.

---


### 13. [Probing for Reading Times](https://arxiv.org/abs/2604.18712)

**<font color=#1a73e8>作者：</font>** Eleftheria Tsipidi, Samuel Kiegeland, Francesco Ignazio Re 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probing has shown that language model representations encode rich linguistic information, but it remains unclear whether they also capture cognitive signals about human processing. In this work, we probe language model representations for human reading times. Using regularized linear regression on two eye-tracking corpora spanning five languages (English, Greek, Hebrew, Russian, and Turkish), we compare the representations from every model layer against scalar predictors -- surprisal, information value, and logit-lens surprisal. We find that the representations from early layers outperform surprisal in predicting early-pass measures such as first fixation and gaze duration. The concentration of predictive power in the early layers suggests that human-like processing signatures are captured by low-level structural or lexical representations, pointing to a functional alignment between model depth and the temporal stages of human reading. In contrast, for late-pass measures such as total reading time, scalar surprisal remains superior, despite its being a much more compressed representation. We also observe performance gains when using both surprisal and early-layer representations. Overall, we find that the best-performing predictor varies strongly depending on the language and eye-tracking measure.

---


### 14. [Align then Refine: Text-Guided 3D Prostate Lesion Segmentation](https://arxiv.org/abs/2604.18713)

**<font color=#1a73e8>作者：</font>** Cuiling Sun, Linkai Peng, Adam Murphy 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated 3D segmentation of prostate lesions from biparametric MRI (bp-MRI) is essential for reliable algorithmic analysis, but achieving high precision remains challenging. Volumetric methods must combine multiple modalities while ensuring anatomical consistency, but current models struggle to integrate cross-modal information reliably. While vision-language models (VLMs) are replacing the currently used architectural designs, they still lack the fine-grained, lesion-level semantics required for effective localized guidance. To address these limitations, we propose a new multi-encoder U-Net architecture incorporating three key innovations: (1) an alignment loss that enhances foreground text-image similarity to inject lesion semantics; (2) a heatmap loss that calibrates the similarity map and suppresses spurious background activations; and (3) a final-stage, confidence-gated multi-head cross-attention refiner that performs localized boundary edits in high-confidence regions. A phase-scheduled training regime stabilizes the optimization of these components. Our method consistently outperforms prior approaches, establishing a new state-of-the-art on the PI-CAI dataset through enhanced multi-modal fusion and localized text guidance. Our code is available at this https URL.

---


### 15. [TrEEStealer: Stealing Decision Trees via Enclave Side Channels](https://arxiv.org/abs/2604.18716)

**<font color=#1a73e8>作者：</font>** Jonas Sander, Anja Rabich, Nick Mahling 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Today, machine learning is widely applied in sensitive, security-related, and financially lucrative applications. Model extraction attacks undermine current business models where a model owner sells model access, e.g., via MLaaS APIs. Additionally, stolen models can enable powerful white-box attacks, facilitating privacy attacks on sensitive training data, and model evasion.
In this paper, we focus on Decision Trees (DT), which are widely deployed in practice. Existing black-box extraction attacks for DTs are either query-intensive, make strong assumptions about the DT structure, or rely on rich API information. To limit attacks to the black-box setting, CPU vendors introduced Trusted Execution Environments (TEE) that use hardware-mechanisms to isolate workloads from external parties, e.g., MLaaS providers. We introduce TrEEStealer, a high-fidelity extraction attack for stealing TEE-protected DTs. TrEEStealer exploits TEE-specific side-channels to steal DTs efficiently and without strong assumptions about the API output or DT structure. The extraction efficacy stems from a novel algorithm that maximizes the information derived from each query by coupling Control-Flow Information (CFI) with passive information tracking. We use two primitives to acquire CFI: for AMD SEV, we follow previous work using the SEV-Step framework and performance counters. For Intel SGX, we reproduce prior findings on current Xeon 6 CPUs and construct a new primitive to efficiently extract the branch history of inference runs through the Branch-History-Register.
We found corresponding vulnerabilities in three popular libraries: OpenCV, mlpack, and emlearn. We show that TrEEStealer achieves superior efficiency and extraction fidelity compared to prior attacks. Our work establishes a new state-of-the-art for DT extraction and confirms that TEEs fail to protect against control-flow leakage.

---


### 16. [From Finite Enumeration to Universal Proof: Ring-Theoretic Foundations for PQC Hardware Masking Verification](https://arxiv.org/abs/2604.18717)

**<font color=#1a73e8>作者：</font>** Ray Iskander, Khaled Kirah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Formal verification of masking in post-quantum cryptographic (PQC) hardware relies on SMT solvers over finite domains. Our prior work established structural dependency analysis at scale [1] and quantified the security margin of partial NTT masking [2]. QANARY, our structural dependency analysis framework, verified 1.17 million cells across 30 modules of the Adams Bridge ML-DSA/ML-KEM accelerator [3, 4], but its core soundness result (Theorem 3.9.1) was machine-checked only at $q = 5$ via $2^{25}$ Boolean wire functions. This left portability to ML-KEM ($q = 3{,}329$, FIPS 203 [5]) and ML-DSA ($q = 8{,}380{,}417$, FIPS 204 [6]) as an open gap. NIST IR 8547 [7] (March 2025) motivates closing such gaps. We present the first machine-checked universal proof of the $r$-free sub-theorem of Theorem 3.9.1: for every $q > 0$, every wire function, and every pair of secrets, value-independence implies identical marginal distributions. The proof, in Lean 4 [8] with Mathlib [9], requires five lines versus $2^{25}$ finite evaluations. It is sorry-free, reducing the trusted base from \{Z3 [10], CVC5 [11], Python\} to the Lean 4 kernel. We provide nine theorems (T1--T6, T1', T3') covering reparametrization, bijectivity, overflow bounds, RNG bias, and a universal non-tightness counterexample for all $q \geq 2$. The results establish commutative ring axioms of $\mathbb{Z}/q\mathbb{Z}$ as the natural abstraction layer for arithmetic masking verification.

---


### 17. [Scripts Through Time: A Survey of the Evolving Role of Transliteration in NLP](https://arxiv.org/abs/2604.18722)

**<font color=#1a73e8>作者：</font>** Thanmay Jayakumar, Deepon Halder, Raj Dabre  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual transfer in NLP is often hindered by the ``script barrier'' where differences in writing systems inhibit transfer learning between languages. Transliteration, the process of converting the script, has emerged as a powerful technique to bridge this gap by increasing lexical overlap. This paper provides a comprehensive survey of the application of transliteration in cross-lingual NLP. We present a taxonomy of key motivations to utilize transliterations in language models, and provide an overview of different approaches of incorporating transliterations as input. We analyze the evolution and effectiveness of these methods, discussing the critical trade-offs involved, and contextualize their need in modern LLMs. The review explores various settings that show how transliteration is beneficial, including handling code-mixed text, leveraging language family relatedness, and pragmatic gains in inference efficiency. Based on this analysis, we provide concrete recommendations for researchers on selecting and implementing the most appropriate transliteration strategy based on their specific language, task, and resource constraints.

---


### 18. [Colour Extraction Pipeline for Odonates using Computer Vision](https://arxiv.org/abs/2604.18725)

**<font color=#1a73e8>作者：</font>** Megan Mirnalini Sundaram Rajaraman, Fons J. Verbeek, Vincent J. Kalkman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The correlation between insect morphological traits and climate has been documented in physiological studies, but such studies remain limited by the time-consuming nature of the data analysis. In particular, the open source datasets often lack annotations of species' morphological traits, making dedicated annotations campaigns necessary; these efforts are typically local in scale and costly. In this paper, we propose a pipeline to identify and segment body parts of Odonates (dragonflies and damselflies) using deep neural networks, with the ultimate goal of extracting body parts' colouration. The pipeline is trained on a limited annotated dataset and refined with pseudo supervised data. We show that, by using open source images from citizen science platforms, our approach can segment each visible subject (Odonates) into head, thorax, abdomen, and wings and then extract a colour palette for each body part. This will enable large-scale statistical analysis of ecological correlations (e.g., between colouration and climate change, habitat loss, or geolocation) which are crucial for quantifying and assessing ecosystem biodiversity status.

---


### 19. [The Cost of Relaxation: Evaluating the Error in Convex Neural Network Verification](https://arxiv.org/abs/2604.18728)

**<font color=#1a73e8>作者：</font>** Merkouris Papamichail, Konstantinos Varsos, Giorgos Flouris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many neural network (NN) verification systems represent the network's input-output relation as a constraint program. Sound and complete, representations involve integer constraints, for simulating the activations. Recent works convexly relax the integer constraints, improving performance, at the cost of soundness. Convex relaxations consider outputs that are unreachable by the original network. We study the worst case divergence between the original network and its convex relaxations; both qualitatively and quantitatively. The relaxations' space forms a lattice, where the top element corresponds to a full relaxation, with every neuron linearized. The bottom element corresponds to the original network. We provide analytical upper and lower bounds for the $\ell_\infty$-distance between the fully relaxed and original outputs. This distance grows exponentially, w.r.t. the network's depth, and linearly w.r.t. the input's radius. The misclassification probability exhibits a step-like behavior, w.r.t. input radius. Our results are supported by experiments on MNIST, Fashion MNIST and random networks.

---


### 20. [Input Visualizations to Track Health Data by Older Adults with Multiple Chronic Conditions](https://arxiv.org/abs/2604.18741)

**<font color=#1a73e8>作者：</font>** Shri Harini Ramesh, Foroozan Daneshzand, Matteo Sotelo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Older adults living with multiple chronic conditions (MCC) can considerably benefit from collecting and reflecting on their health data. Many older adults collect their health data using various approaches, such as digital tools or handwritten notebooks. However, in these approaches, the act of collecting data does not itself yield insights; sensemaking and reflection happen only if individuals later review their accumulated records. The daily process of data collection thus offers limited opportunity for individuals to actively engage with their data or find the process personally meaningful and enjoyable. Personal data input visualizations using physical tokens offer a promising solution that can help individuals recognize evolving patterns while collecting data and discover meaningful insights more serendipitously and engagingly. Yet, there is a limited understanding of whether and how older adults living with MCC might adopt physical input visualizations to collect data and reflect on their health, and how the tangible, expressive, and personalizable nature of this process supports their sensemaking and reflection. In this paper, we present the results of our interview and diary studies in which older adults living with MCC inputted health data using physical tokens over two weeks. Our findings highlight the diverse and unique needs of older adults for tracking personal health data, illustrating how they adapt strategies and personalize physical input visualizations to align with their individual needs. We demonstrate how older adults integrated input visualizations into daily routines and leveraged tangible markers to reflect on patterns and behaviors, while enjoying the process of tracking and focusing on personal expression and meaningful reflection. Finally, we provide design considerations for supporting older adults with MCC when inputting health data through physical tokens.

---


### 21. [Match-Any-Events: Zero-Shot Motion-Robust Feature Matching Across Wide Baselines for Event Cameras](https://arxiv.org/abs/2604.18744)

**<font color=#1a73e8>作者：</font>** Ruijun Zhang, Hang Su, Kostas Daniilidis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras have recently shown promising capabilities in instantaneous motion estimation due to their robustness to low light and fast motions. However, computing wide-baseline correspondence between two arbitrary views remains a significant challenge, since event appearance changes substantially with motion, and learning-based approaches are constrained by both scalability and limited wide-baseline supervision. We therefore introduce the first event matching model that achieves cross-dataset wide-baseline correspondence in a zero-shot manner: a single model trained once is deployed on unseen datasets without any target-domain fine-tuning or adaptation. To enable this capability, we introduce a motion-robust and computationally efficient attention backbone that learns multi-timescale features from event streams, augmented with sparsity-aware event token selection, making large-scale training on diverse wide-baseline supervision computationally feasible. To provide the supervision needed for wide-baseline generalization, we develop a robust event motion synthesis framework to generate large-scale event-matching datasets with augmented viewpoints, modalities, and motions. Extensive experiments across multiple benchmarks show that our framework achieves a 37.7% improvement over the previous best event feature matching methods. Code and data are available at: this https URL.

---


### 22. [DeltaSeg: Tiered Attention and Deep Delta Learning for Multi-Class Structural Defect Segmentation](https://arxiv.org/abs/2604.18745)

**<font color=#1a73e8>作者：</font>** Enrique Hernandez Noguera, Md Meftahul Ferdaus, Elias Ioup 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated segmentation of structural defects from visual inspection imagery remains challenging due to the diversity of damage types, extreme class imbalance, and the need for precise boundary delineation. This paper presents DeltaSeg, a U-shaped encoder-decoder architecture with a tiered attention strategy that integrates Squeeze-and-Excitation (SE) channel attention in the encoder, Coordinate Attention at the bottleneck and decoder, and a novel Deep Delta Attention (DDA) mechanism in the skip connections. The encoder uses depthwise separable convolutions with dilated stages to maintain spatial resolution while expanding the receptive field. Atrous Spatial Pyramid Pooling (ASPP) at the bottleneck captures multi-scale context. The DDA module refines skip connections through a dual-path scheme combining a learned delta operator for nuisance feature suppression with spatial attention gates conditioned on decoder signals. Deep supervision through multi-scale auxiliary heads further strengthens gradient flow and encourages semantically meaningful features at intermediate decoder stages. We evaluate DeltaSeg on two datasets: the S2DS dataset (7 classes) and the Culvert-Sewer Defect Dataset (CSDD, 9 classes). Across both benchmarks, DeltaSeg consistently outperforms 12 competing architectures including U-Net, SA-UNet, UNet3+, SegFormer, Swin-UNet, EGE-UNet, FPN, and Mobile-UNETR, demonstrating strong generalization across damage types, imaging conditions, and structural geometries.

---


### 23. [URoPE: Universal Relative Position Embedding across Geometric Spaces](https://arxiv.org/abs/2604.18747)

**<font color=#1a73e8>作者：</font>** Yichen Xie, Depu Meng, Chensheng Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Relative position embedding has become a standard mechanism for encoding positional information in Transformers. However, existing formulations are typically limited to a fixed geometric space, namely 1D sequences or regular 2D/3D grids, which restricts their applicability to many computer vision tasks that require geometric reasoning across camera views or between 2D and 3D spaces. To address this limitation, we propose URoPE, a universal extension of Rotary Position Embedding (RoPE) to cross-view or cross-dimensional geometric spaces. For each key/value image patch, URoPE samples 3D points along the corresponding camera ray at predefined depth anchors and projects them into the query image plane. Standard 2D RoPE can then be applied using the projected pixel coordinates. URoPE is a parameter-free and intrinsics-aware relative position embedding that is invariant to the choice of global coordinate systems, while remaining fully compatible with existing RoPE-optimized attention kernels. We evaluate URoPE as a plug-in positional encoding for transformer architectures across a diverse set of tasks, including novel view synthesis, 3D object detection, object tracking, and depth estimation, covering 2D-2D, 2D-3D, and temporal scenarios. Experiments show that URoPE consistently improves the performance of transformer-based models across all tasks, demonstrating its effectiveness and generality for geometric reasoning. Our project website is: this https URL.

---


### 24. [Beyond Coefficients: Forecast-Necessity Testing for Interpretable Causal Discovery in Nonlinear Time-Series Models](https://arxiv.org/abs/2604.18751)

**<font color=#1a73e8>作者：</font>** Valentina Kuskova, Dmitry Zaytsev, Michael Coppedge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear machine-learning models are increasingly used to discover causal relationships in time-series data, yet the interpretation of their outputs remains poorly understood. In particular, causal scores produced by regularized neural autoregressive models are often treated as analogues of regression coefficients, leading to misleading claims of statistical significance.
In this paper, we argue that causal relevance in nonlinear time-series models should be evaluated through forecast necessity rather than coefficient magnitude, and we present a practical evaluation procedure for doing so. We present an interpretable evaluation framework based on systematic edge ablation and forecast comparison, which tests whether a candidate causal relationship is required for accurate prediction. Using Neural Additive Vector Autoregression as a case study model, we apply this framework to a real-world case study of democratic development, modeled as a multivariate time series of panel data - democracy indicators across 139 countries. We show that relationships with similar causal scores can differ dramatically in their predictive necessity due to redundancy, temporal persistence, and regime-specific effects.
Our results demonstrate how forecast-necessity testing supports more reliable causal reasoning in applied AI systems and provides practical guidance for interpreting nonlinear time-series models in high-stakes domains.

---


### 25. [Syntax as a Rosetta Stone: Universal Dependencies for In-Context Coptic Translation](https://arxiv.org/abs/2604.18758)

**<font color=#1a73e8>作者：</font>** Abhishek Purushothama, Emma Thronson, Alexia Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource machine translation requires methods that differ from those used for high-resource languages. This paper proposes a novel in-context learning approach to support low-resource machine translation of the Coptic language to English, with syntactic augmentation from Universal Dependencies parses of input sentences. Building on existing work using bilingual dictionaries to support inference for vocabulary items, we add several representations of syntactic analyses to our inputs , specifically exploring the inclusion of raw parser outputs, verbalizations of parses in plain English, and targeted instructions of difficult constructions identified in sub-trees and how they can be translated. Our results show that while syntactic information alone is not as useful as dictionary-based glosses, combining retrieved dictionary items with syntactic information achieves significant gains across model sizes, achieving new state-of-the-art translation results for Coptic.

---


### 26. [Model-Agnostic Meta Learning for Class Imbalance Adaptation](https://arxiv.org/abs/2604.18759)

**<font color=#1a73e8>作者：</font>** Hanshu Rao, Guangzeng Han, Xiaolei Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Class imbalance is a widespread challenge in NLP tasks, significantly hindering robust performance across diverse domains and applications. We introduce Hardness-Aware Meta-Resample (HAMR), a unified framework that adaptively addresses both class imbalance and data difficulty. HAMR employs bi-level optimizations to dynamically estimate instance-level weights that prioritize genuinely challenging samples and minority classes, while a neighborhood-aware resampling mechanism amplifies training focus on hard examples and their semantically similar neighbors. We validate HAMR on six imbalanced datasets covering multiple tasks and spanning biomedical, disaster response, and sentiment domains. Experimental results show that HAMR achieves substantial improvements for minority classes and consistently outperforms strong baselines. Extensive ablation studies demonstrate that our proposed modules synergistically contribute to performance gains and highlight HAMR as a flexible and generalizable approach for class imbalance adaptation. Code is available at this https URL.

---


### 27. [Multi-Level Temporal Graph Networks with Local-Global Fusion for Industrial Fault Diagnosis](https://arxiv.org/abs/2604.18765)

**<font color=#1a73e8>作者：</font>** Bibek Aryal, Gift Modekwe, Qiugang Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fault detection and diagnosis are critical for the optimal and safe operation of industrial processes. The correlations among sensors often display non-Euclidean structures where graph neural networks (GNNs) are widely used therein. However, for large-scale systems, local, global, and dynamic relations extensively exist among sensors, and traditional GNNs often overlook such complex and multi-level structures for various problems including the fault diagnosis. To address this issue, we propose a structure-aware multi-level temporal graph network with local-global feature fusion for industrial fault diagnosis. First, a correlation graph is dynamically constructed using Pearson correlation coefficients to capture relationships among process variables. Then, temporal features are extracted through long short-term memory (LSTM)-based encoder, whereas the spatial dependencies among sensors are learned by graph convolution layers. A multi-level pooling mechanism is used to gradually coarsen and learn meaningful graph structures, to capture higher-level patterns while keeping important fault related details. Finally, a fusion step is applied to combine both detailed local features and overall global patterns before the final prediction. Experimental evaluations on the Tennessee Eastman process (TEP) demonstrate that the proposed model achieves superior fault diagnosis performance, particularly for complex fault scenarios, outperforming various baseline methods.

---


### 28. [AffectCity: An Empirical Investigation of Complexity, Transparency, and Materiality in Shaping Affective Perception of Building Facades](https://arxiv.org/abs/2604.18768)

**<font color=#1a73e8>作者：</font>** Chenxi Wang, Haining Ding, Michal Gath-Morad  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Buildings shape how people feel, yet the mechanisms through which specific facade properties drive affective states remain empirically underspecified. Here we introduce the Cambridge Facade Affect Dataset (CFAD), 86 orthogonally rectified facade images annotated with continuous arousal and valence ratings from 85 participants, and establish a validated pipeline linking machine-vision-derived surface metrics to human affective responses. Focusing on three quantifiable attributes, complexity, transparency (window-to-wall ratio), and materiality (proportion of natural versus artificial surface composition), we show that perceived complexity is the dominant affective predictor, with significant positive associations for both arousal (beta = 0.507, p < 0.001) and valence (beta = 0.376, p < 0.001) and a curvilinear amplification at higher complexity levels. Transparency exhibits an inverted-U relationship with valence, while increasing surface artificiality suppresses arousal and reduces pleasantness consistent with biophilic response theory. Critically, machine-derived metrics show limited direct predictive power over affective outcomes; mediation analyses reveal that human perceptual evaluation functions as a necessary intermediate layer, with perceived materiality significantly mediating the machine-valence relationship (indirect effect = -0.205, p = 0.003). Cross-context validation demonstrates moderate stability of complexity and materiality ratings across image-based and in-situ conditions, while affective responses, particularly valence, exhibit significant context-dependence (ICC = 0.332). These findings advance facade research from descriptive morphological analysis toward predictive, perception-grounded modelling, and provide an empirically validated basis for affect-informed design of the urban environment.

---


### 29. [Mango: Multi-Agent Web Navigation via Global-View Optimization](https://arxiv.org/abs/2604.18779)

**<font color=#1a73e8>作者：</font>** Weixi Tong, Yifeng Di, Tianyi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing web agents typically initiate exploration from the root URL, which is inefficient for complex websites with deep hierarchical structures. Without a global view of the website's structure, agents frequently fall into navigation traps, explore irrelevant branches, or fail to reach target information within a limited budget. We propose Mango, a multi-agent web navigation method that leverages the website structure to dynamically determine optimal starting points. We formulate URL selection as a multi-armed bandit problem and employ Thompson Sampling to adaptively allocate the navigation budget across candidate URLs. Furthermore, we introduce an episodic memory component to store navigation history, enabling the agent to learn from previous attempts. Experiments on WebVoyager demonstrate that Mango achieves a success rate of 63.6% when using GPT-5-mini, outperforming the best baseline by 7.3%. Furthermore, on WebWalkerQA, Mango attains a 52.5% success rate, surpassing the best baseline by 26.8%. We also demonstrate the generalizability of Mango using both open-source and closed-source models as backbones. Our data and code are open-source and available at this https URL.

---


### 30. [Streaming Structured Inference with Flash-SemiCRF](https://arxiv.org/abs/2604.18780)

**<font color=#1a73e8>作者：</font>** Benjamin K. Johnson, Thomas Goralski, Ayush Semwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-Markov Conditional Random Fields (semi-CRFs) assign labels to segments of a sequence rather than to individual positions, enabling exact inference over segment-level features and principled uncertainty estimates at their boundaries. However, existing implementations must materialize a large edge potential tensor whose size grows with sequence length, maximum segment length, and label count, becoming prohibitive for speech-scale state spaces and intractable at genomic scales where sequences can exceed 100,000 positions. This memory bottleneck has limited the adoption of exact segment-level inference for long sequences and large label sets. We identify that the core inefficiency is materializing edge potentials that can instead be evaluated on-the-fly from a compact prefix-sum array, and make several improvements. First, replacing the stored edge tensor with prefix-sum lookup reduces the memory footprint by a factor proportional to the product of segment length and label count. Second, a streaming forward-backward pass with checkpoint-boundary normalization keeps working memory sublinear in sequence length while preserving exact gradients. Third, zero-centered cumulative scores control numerical drift and induce an adaptive duration prior under label imbalance. We integrate these ideas into Flash-SemiCRF, a fused Triton kernel that enables exact semi-CRF inference on previously intractable problem sizes. Available at this https URL.

---


### 31. [CAHAL: Clinically Applicable resolution enHAncement for Low-resolution MRI scans](https://arxiv.org/abs/2604.18781)

**<font color=#1a73e8>作者：</font>** Sergio Morell-Ortega, Ángela González-Cebrián, Boris Mansencal 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale automated morphometric analysis of brain MRI is limited by the thick-slice, anisotropic acquisitions prevalent in routine clinical practice. Existing generative super-resolution (SR) methods produce visually compelling isotropic volumes but often introduce anatomical hallucinations, systematic volumetric overestimation, and structural distortions that compromise downstream quantitative analysis and diagnostic safety. To address this, we propose CAHAL (Clinically Applicable resolution enHAncement for Low-resolution MRI scans), a hallucination-robust, physics-informed resolution enhancement framework that operates directly in the patient's native acquisition space. CAHAL employs a deterministic bivariate Mixture of Experts (MoE) architecture routing each input through specialised residual 3D U-Net experts conditioned on both volumetric resolution and acquisition anisotropy, two independent descriptors of clinical MRI acquisition. Experts are optimised with a composite loss combining edge-penalised spatial reconstruction, Fourier-domain spectral coherence matching, and a segmentation-guided semantic consistency constraint. Training pairs are generated on-the-fly via physics-based degradation sampled from a large-scale real-world database, ensuring robust generalisation. Validated on T1-weighted and FLAIR sequences against generative baselines, CAHAL achieves state-of-the-art results, improving the best related methods in terms of accuracy and efficiency.

---


### 32. [EfficientPENet: Real-Time Depth Completion from Sparse LiDAR via Lightweight Multi-Modal Fusion](https://arxiv.org/abs/2604.18790)

**<font color=#1a73e8>作者：</font>** Johny J. Lopez, Md Meftahul Ferdaus, Mahdi Abdelguerfi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth completion from sparse LiDAR measurements and corresponding RGB images is a prerequisite for accurate 3D perception in robotic systems. Existing methods achieve high accuracy on standard benchmarks but rely on heavy backbone architectures that preclude real-time deployment on embedded hardware. We present EfficientPENet, a two-branch depth completion network that replaces the conventional ResNet encoder with a modernized ConvNeXt backbone, introduces sparsity-invariant convolutions for the depth stream, and refines predictions through a Convolutional Spatial Propagation Network (CSPN). The RGB branch leverages ImageNet-pretrained ConvNeXt blocks with Layer Normalization, 7x7 depthwise convolutions, and stochastic depth regularization. Features from both branches are merged via late fusion and decoded through a multi-scale deep supervision strategy. We further introduce a position-aware test-time augmentation scheme that corrects coordinate tensors during horizontal flipping, yielding consistent error reduction at inference. On the KITTI depth completion benchmark, EfficientPENet achieves an RMSE of 631.94 mm with 36.24M parameters and a latency of 20.51 ms, operating at 48.76 FPS. This represents a 3.7 times reduction in parameters and a 23 times speedup relative to BP-Net, while maintaining competitive accuracy. These results establish EfficientPENet as a practical solution for real-time depth completion on resource-constrained edge platforms such as the NVIDIA Jetson.

---


### 33. [HELM: Harness-Enhanced Long-horizon Memory for Vision-Language-Action Manipulation](https://arxiv.org/abs/2604.18791)

**<font color=#1a73e8>作者：</font>** Zijian Zeng, Fei Ding, Huiming Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models fail systematically on long-horizon manipulation tasks despite strong short-horizon performance. We show that this failure is not resolved by extending context length alone in the current reactive execution setting; instead, it stems from three recurring execution-loop deficiencies: the memory gap, the verification gap, and the recovery gap. We present HELM, a model-agnostic framework that addresses these deficiencies with three components: an Episodic Memory Module (EMM) that retrieves key task history via CLIP-indexed keyframes, a learned State Verifier (SV) that predicts action failure before execution from observation, action, subgoal, and memory-conditioned context, and a Harness Controller (HC) that performs rollback and replanning. The SV is the core learning contribution: it consistently outperforms rule-based feasibility checks and ensemble uncertainty baselines, and its effectiveness depends critically on access to episodic memory. On LIBERO-LONG, HELM improves task success rate by 23.1 percentage points over OpenVLA (58.4% to 81.5%), while extending the context window to H=32 yields only a 5.4-point gain and same-budget LoRA adaptation remains 12.2 points below HELM. HELM also improves long-horizon performance on CALVIN and substantially boosts recovery success under controlled perturbations. Ablations and mechanism analyses isolate the contribution of each component, and we release LIBERO-Recovery as a perturbation-injection protocol for evaluating failure recovery in long-horizon manipulation.

---


### 34. [CrossPan: A Comprehensive Benchmark for Cross-Sequence Pancreas MRI Segmentation and Generalization](https://arxiv.org/abs/2604.18797)

**<font color=#1a73e8>作者：</font>** Linkai Peng, Cuiling Sun, Zheyuan Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic pancreas segmentation is fundamental to abdominal MRI analysis, yet deep learning models trained on one MRI sequence often fail catastrophically when applied to another-a challenge that has received little systematic investigation. We introduce CrossPan, a multi-institutional benchmark comprising 1,386 3D scans across three routinely acquired sequences (T1-weighted, T2-weighted, and Out-of-Phase) from eight centers. Our experiments reveal three key findings. First, cross-sequence domain shifts are far more severe than cross-center variability: models achieving Dice scores above 0.85 in-domain collapse to near-zero (<0.02) when transferred across sequences. Second, state-of-the-art domain generalization methods provide negligible benefit under these physics-driven contrast inversions, whereas foundation models like MedSAM2 maintain moderate zero-shot performance through contrast-invariant shape priors. Third, semi-supervised learning offers gains only under stable intensity distributions and becomes unstable on sequences with high intra-organ variability. These results establish cross-sequence generalization-not model architecture or center diversity-as the primary barrier to clinically deployable pancreas MRI segmentation. Dataset and code are available at this https URL.

---


### 35. [Preserving Clusters in Error-Bounded Lossy Compression of Particle Data](https://arxiv.org/abs/2604.18801)

**<font color=#1a73e8>作者：</font>** Congrong Ren, Sheng Di, Katrin Heitmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lossy compression is widely used to reduce storage and I/O costs for large-scale particle datasets in scientific applications such as cosmology, molecular dynamics, and fluid dynamics, where clustering structures (e.g., single-linkage or Friends-of-Friends) are critical for downstream analysis; however, existing compressors typically provide only pointwise error bounds on particle positions and offer no guarantees on preserving clustering outcomes, and even small perturbations can alter cluster connectivity and compromise scientific validity. We propose a correction-based technique to preserve single-linkage clustering under lossy compression, operating on decompressed data from off-the-shelf compressors such as SZ3 and Draco. Our key contributions are threefold: (1) a clustering-aware correction algorithm that identifies vulnerable particle pairs via spatial partitioning and local neighborhood search; (2) an optimization-based formulation that enforces clustering consistency using projected gradient descent with a loss that encodes pairwise distance violations; and (3) a scalable GPU-accelerated and distributed implementation for large-scale datasets. Experiments on cosmology and molecular dynamics datasets show that our method effectively preserves clustering results while maintaining competitive compression performance compared with SZ3, ZFP, Draco, LCP, and space-filling-curve-based schemes.

---


### 36. [Geometric Decoupling: Diagnosing the Structural Instability of Latent](https://arxiv.org/abs/2604.18804)

**<font color=#1a73e8>作者：</font>** Yuanbang Liang, Zhengwen Chen, Yu-Kun Lai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent Diffusion Models (LDMs) achieve high-fidelity synthesis but suffer from latent space brittleness, causing discontinuous semantic jumps during editing. We introduce a Riemannian framework to diagnose this instability by analyzing the generative Jacobian, decomposing geometry into \textit{Local Scaling} (capacity) and \textit{Local Complexity} (curvature). Our study uncovers a \textbf{``Geometric Decoupling"}: while curvature in normal generation functionally encodes image detail, OOD generation exhibits a functional decoupling where extreme curvature is wasted on unstable semantic boundaries rather than perceptible details. This geometric misallocation identifies ``Geometric Hotspots" as the structural root of instability, providing a robust intrinsic metric for diagnosing generative reliability.

---


### 37. [AI scientists produce results without reasoning scientifically](https://arxiv.org/abs/2604.18805)

**<font color=#1a73e8>作者：</font>** Martiño Ríos-García, Nawaf Alampara, Chandan Gupta 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based systems are increasingly deployed to conduct scientific research autonomously, yet whether their reasoning adheres to the epistemic norms that make scientific inquiry self-correcting is poorly understood. Here, we evaluate LLM-based scientific agents across eight domains, spanning workflow execution to hypothesis-driven inquiry, through more than 25,000 agent runs and two complementary lenses: (i) a systematic performance analysis that decomposes the contributions of the base model and the agent scaffold, and (ii) a behavioral analysis of the epistemological structure of agent reasoning. We observe that the base model is the primary determinant of both performance and behavior, accounting for 41.4% of explained variance versus 1.5% for the scaffold. Across all configurations, evidence is ignored in 68% of traces, refutation-driven belief revision occurs in 26%, and convergent multi-test evidence is rare. The same reasoning pattern appears whether the agent executes a computational workflow or conducts hypothesis-driven inquiry. They persist even when agents receive near-complete successful reasoning trajectories as context, and the resulting unreliability compounds across repeated trials in epistemically demanding domains. Thus, current LLM-based agents execute scientific workflows but do not exhibit the epistemic patterns that characterize scientific reasoning. Outcome-based evaluation cannot detect these failures, and scaffold engineering alone cannot repair them. Until reasoning itself becomes a training target, the scientific knowledge produced by such agents cannot be justified by the process that generated it.

---


### 38. [A PPA-Driven 3D-IC Partitioning Selection Framework with Surrogate Models](https://arxiv.org/abs/2604.18806)

**<font color=#1a73e8>作者：</font>** Shang Wang, Shuai Liu, Owen Randall 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> 3D-IC netlist partitioning is commonly optimized using proxy objectives, while final PPA is treated as a costly evaluation rather than an optimization signal. This proxy-driven paradigm makes it difficult to reliably translate additional PPA evaluations into better PPA outcomes. To bridge this gap, we present DOPP (D-Optimal PPA-driven partitioning selection), an approach that bridges the gap between proxies and true PPA metrics. Across eight 3D-IC designs, our framework improves PPA over Open3DBench (average relative improvements of 9.99% congestion, 7.87% routed wirelength, 7.75% WNS, 21.85% TNS, and 1.18% power). Compared with exhaustive evaluation over the full candidate set, DOPP achieves comparable best-found PPA while evaluating only a small fraction of candidates, substantially reducing evaluation cost. By parallelizing evaluations, our method delivers these gains while maintaining wall-clock runtime comparable to traditional baselines.

---


### 39. [Rethinking Dataset Distillation: Hard Truths about Soft Labels](https://arxiv.org/abs/2604.18811)

**<font color=#1a73e8>作者：</font>** Priyam Dey, Aditya Sahdev, Sunny Bhati 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the perceived success of large-scale dataset distillation (DD) methods, recent evidence finds that simple random image baselines perform on-par with state-of-theart DD methods like SRe2L due to the use of soft labels during downstream model training. This is in contrast with the findings in coreset literature, where high-quality coresets consistently outperform random subsets in the hardlabel (HL) setting. To understand this discrepancy, we perform a detailed scalability analysis to examine the role of data quality under different label regimes, ranging from abundant soft labels (termed as SL+KD regime) to fixed soft labels (SL) and hard labels (HL). Our analysis reveals that high-quality coresets fail to convincingly outperform the random baseline in both SL and SL+KD regimes. In the SL+KD setting, performance further approaches nearoptimal levels relative to the full dataset, regardless of subset size or quality, for a given compute budget. This performance saturation calls into question the widespread practice of using soft labels for model evaluation, where unlike the HL setting, subset quality has negligible influence. A subsequent systematic evaluation of five large-scale and four small-scale DD methods in the HL setting reveals that only RDED reliably outperforms random baselines on ImageNet-1K, but can still lag behind strong coreset methods due to its over-reliance on easy sample patches. Based on this, we introduce CAD-Prune, a compute-aware pruning metric that efficiently identifies samples of optimal difficulty for a given compute budget, and use it to develop CA2D, a compute-aligned DD method, outperforming current DD methods on ImageNet-1K at various IPC settings. Together, our findings uncover many insights into current DD research and establish useful tools to advance dataefficient learning for both coresets and DD.

---


### 40. [Curvature-Aware PCA with Geodesic Tangent Space Aggregation for Semi-Supervised Learning](https://arxiv.org/abs/2604.18816)

**<font color=#1a73e8>作者：</font>** Alexandre L. M. Levada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Principal Component Analysis (PCA) is a fundamental tool for representation learning, but its global linear formulation fails to capture the structure of data supported on curved manifolds. In contrast, manifold learning methods model nonlinearity but often sacrifice the spectral structure and stability of PCA. We propose \emph{Geodesic Tangent Space Aggregation PCA (GTSA-PCA)}, a geometric extension of PCA that integrates curvature awareness and geodesic consistency within a unified spectral framework. Our approach replaces the global covariance operator with curvature-weighted local covariance operators defined over a $k$-nearest neighbor graph, yielding local tangent subspaces that adapt to the manifold while suppressing high-curvature distortions. We then introduce a geodesic alignment operator that combines intrinsic graph distances with subspace affinities to globally synchronize these local representations. The resulting operator admits a spectral decomposition whose leading components define a geometry-aware embedding. We further incorporate semi-supervised information to guide the alignment, improving discriminative structure with minimal supervision. Experiments on real datasets show consistent improvements over PCA, Kernel PCA, Supervised PCA and strong graph-based baselines such as UMAP, particularly in small sample size and high-curvature regimes. Our results position GTSA-PCA as a principled bridge between statistical and geometric approaches to dimensionality reduction.

---


### 41. [Blockchain-Driven AI-Enhanced Post-Quantum Multivariate Identity-based Signature and Privacy-Preserving Data Aggregation Scheme for Fog-enabled Flying Ad-Hoc Networks](https://arxiv.org/abs/2604.18819)

**<font color=#1a73e8>作者：</font>** Sufian Al majmaie, Ghazal Ghajari, Niraj Prasad Bhatta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The integration of Fog Computing with Flying Ad-Hoc Networks (FANETs) offers promising capabilities for decentralized, low-latency intelligence in UAV-based applications. However, the distributed nature, mobility, and resource constraints of FANETs expose them to significant security and privacy challenges, particularly against quantum threats. To address these issues, this work introduces a blockchain-based, AI-enhanced key management framework designed for fog-enabled FANETs. The proposed scheme employs a Post-Quantum Multivariate Identity-Based Signature Scheme (PQ-MISS) and Zero-Knowledge Proofs (ZKPs) to achieve secure key establishment, privacy-preserving data aggregation, and integrity verification. A polynomial composition-based encryption mechanism and an aggregate signature model support secure and efficient multi-device communication across fog and UAV layers. Fog servers construct partial blockchain blocks from validated UAV data. These blocks are completed and mined by Cloud Servers (CSs). AI algorithms then analyze the verified data to generate accurate predictions and insights. NS-3 simulations validate the efficiency of PQ-MISS in reducing communication overhead while improving the speed and reliability of data aggregation and verification. Comparative analysis demonstrates the proposed scheme's advantages over existing methods in computational cost, post-quantum security, and scalability, making it a robust solution for secure, intelligent, and future-ready FANET systems.

---


### 42. [The High Explosives and Affected Targets (HEAT) Dataset](https://arxiv.org/abs/2604.18828)

**<font color=#1a73e8>作者：</font>** Bryan Kaiser, Kyle Hickmann, Sharmistha Chakrabarti 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) surrogate models provide a computationally efficient alternative to full-physics simulations, but no public datasets currently exist for training and validating models of high-explosive-driven, multi-material shock dynamics. Simulating shock propagation is challenging due to the need for material-specific equations of state (EOS) and models of plasticity, phase change, damage, fluid instabilities, and multi-material interactions. Explosive-driven shocks further require reactive material models to capture detonation physics. To address this gap, we introduce the High-Explosives and Affected Targets (HEAT) dataset, a physics-rich collection of two-dimensional, cylindrically symmetric simulations generated using an Eulerian multi-material shock-propagation code developed at Los Alamos National Laboratory. HEAT consists of two partitions: expanding shock-cylinder (CYL) simulations and Perturbed Layered Interface (PLI) simulations. Each entry includes time series of thermodynamic fields (pressure, density, temperature), kinematic fields (position, velocity), and continuum quantities such as stress. The CYL partition spans a range of materials, including metals (aluminum, copper, depleted uranium, stainless steel, tantalum), a polymer, water, gases (air, nitrogen), and a detonating material. The PLI partition explores varied geometries with fixed materials: copper, aluminum, stainless steel, polymer, and high explosive. HEAT captures key phenomena such as shock propagation, momentum transfer, plastic deformation, and thermal effects, providing a benchmark dataset for AI/ML models of multi-material shock physics.

---


### 43. [Quantum inspired qubit qutrit neural networks for real time financial forecasting](https://arxiv.org/abs/2604.18838)

**<font color=#1a73e8>作者：</font>** Kanishk Bakshi, Kathiravan Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This research investigates the performance and efficacy of machine learning models in stock prediction, comparing Artificial Neural Networks (ANNs), Quantum Qubit-based Neural Networks (QQBNs), and Quantum Qutrit-based Neural Networks (QQTNs). By outlining methodologies, architectures, and training procedures, the study highlights significant differences in training times and performance metrics across models. While all models demonstrate robust accuracies above 70%, the Quantum Qutrit-based Neural Network consistently outperforms with advantages in risk-adjusted returns, measured by the Sharpe ratio, greater consistency in prediction quality through the Information Coefficient, and enhanced robustness under varying market conditions. The QQTN not only surpasses its classical and qubit-based counterparts in multiple quantitative and qualitative metrics but also achieves comparable performance with significantly reduced training times. These results showcase the promising prospects of Quantum Qutrit-based Neural Networks in practical financial applications, where real-time processing is critical. By achieving superior accuracy, efficiency, and adaptability, the proposed models underscore the transformative potential of quantum-inspired approaches, paving the way for their integration into computationally intensive fields.

---


### 44. [One Step Forward and K Steps Back: Better Reasoning with Denoising Recursion Models](https://arxiv.org/abs/2604.18839)

**<font color=#1a73e8>作者：</font>** Chris Cameron, Wangzheng Wang, Nikita Ivanov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers scale computational depth without increasing parameter count by repeatedly applying a shared transformer block and can be used for iterative refinement, where each loop rewrites a full fixed-size prediction in parallel. On difficult problems, such as those that require search-like computation, reaching a highly structured solution starting from noise can require long refinement trajectories. Learning such trajectories is challenging when training specifies only the target solution and provides no supervision over the intermediate refinement path. Diffusion models tackle this issue by corrupting data with varying magnitudes of noise and training the model to reverse it in a \textit{single step}. However, this process misaligns training and testing behaviour. We introduce Denoising Recursion Models, a method that similarly corrupts data with noise but trains the model to reverse the corruption over \textit{multiple} recursive steps. This strategy provides a tractable curriculum of intermediate states, while better aligning training with testing and incentivizing non-greedy, forward-looking generation. Through extensive experiments, we show this approach outperforms the Tiny Recursion Model (TRM) on ARC-AGI, where it recently achieved breakthrough performance.

---


### 45. [Multi-Domain Learning with Global Expert Mapping](https://arxiv.org/abs/2604.18842)

**<font color=#1a73e8>作者：</font>** Pourya Shamsolmoali, Masoumeh Zareapoor, Huiyu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human perception generalizes well across different domains, but most vision models struggle beyond their training data. This gap motivates multi-dataset learning, where a single model is trained on diverse datasets to improve robustness under domain shifts. However, unified training remains challenging due to inconsistencies in data distributions and label semantics. Mixture-of-Experts (MoE) models provide a scalable solution by routing inputs to specialized subnetworks (experts). Yet, existing MoEs often fail to specialize effectively, as their load-balancing mechanisms enforce uniform input distribution across experts. This fairness conflicts with domain-aware routing, causing experts to learn redundant representations, and reducing performance especially on rare or out-of-distribution domains. We propose GEM (Global Expert Mapping), a planner-compiler framework that replaces the learned router with a global scheduler. Our planner, based on linear programming relaxation, computes a fractional assignment of datasets to experts, while the compiler applies hierarchical rounding to convert this soft plan into a deterministic, capacity-aware mapping. Unlike prior MoEs, GEM avoids balancing loss, resolves the conflict between fairness and specialization, and produces interpretable routing. Experiments show that GEM-DINO achieves state-of-the-art performance on the UODB benchmark, with notable gains on underrepresented datasets and solves task interference in few-shot adaptation scenarios.

---


### 46. [Human-Guided Harm Recovery for Computer Use Agents](https://arxiv.org/abs/2604.18847)

**<font color=#1a73e8>作者：</font>** Christy Li, Sky CH-Wang, Andi Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LM agents gain the ability to execute actions on real computer systems, we need ways to not only prevent harmful actions at scale but also effectively remediate harm when prevention fails. We formalize a solution to this neglected challenge in post-execution safeguards as harm recovery: the problem of optimally steering an agent from a harmful state back to a safe one in alignment with human preferences. We ground preference-aligned recovery through a formative user study that identifies valued recovery dimensions and produces a natural language rubric. Our dataset of 1,150 pairwise judgments reveals context-dependent shifts in attribute importance, such as preferences for pragmatic, targeted strategies over comprehensive long-term approaches. We operationalize these learned insights in a reward model, re-ranking multiple candidate recovery plans generated by an agent scaffold at test time. To evaluate recovery capabilities systematically, we introduce BackBench, a benchmark of 50 computer-use tasks that test an agent's ability to recover from harmful states. Human evaluation shows our reward model scaffold yields higher-quality recovery trajectories than base agents and rubric-based scaffolds. Together, these contributions lay the foundation for a new class of agent safety methods -- ones that confront harm not only by preventing it, but by navigating its aftermath with alignment and intent.

---


### 47. [DDF2Pol: A Dual-Domain Feature Fusion Network for PolSAR Image Classification](https://arxiv.org/abs/2604.18853)

**<font color=#1a73e8>作者：</font>** Mohammed Q. Alkhatib  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents DDF2Pol, a lightweight dual-domain convolutional neural network for PolSAR image classification. The proposed architecture integrates two parallel feature extraction streams, one real-valued and one complex-valued, designed to capture complementary spatial and polarimetric information from PolSAR data. To further refine the extracted features, a depth-wise convolution layer is employed for spatial enhancement, followed by a coordinate attention mechanism to focus on the most informative regions. Experimental evaluations conducted on two benchmark datasets, Flevoland and San Francisco, demonstrate that DDF2Pol achieves superior classification performance while maintaining low model complexity. Specifically, it attains an Overall Accuracy (OA) of 98.16% on the Flevoland dataset and 96.12% on the San Francisco dataset, outperforming several state-of-the-art real- and complex-valued models. With only 91,371 parameters, DDF2Pol offers a practical and efficient solution for accurate PolSAR image analysis, even when training data is limited. The source code is publicly available at this https URL

---


### 48. [ConvVitMamba: Efficient Multiscale Convolution, Transformer, and Mamba-Based Sequence modelling for Hyperspectral Image Classification](https://arxiv.org/abs/2604.18856)

**<font color=#1a73e8>作者：</font>** Mohammed Q. Alkhatib  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image (HSI) classification remains challenging due to high spectral dimensionality, redundancy, and limited labeled data. Although convolutional neural networks (CNNs) and Vision Transformers (ViTs) achieve strong performance by exploiting spectral-spatial information and long-range dependencies, they often incur high computational cost and large model size, limiting practical use. To address these limitations, a unified hybrid framework, termed ConvVitMamba, is proposed for efficient HSI classification. The architecture integrates three components: a multiscale convolutional feature extractor to capture local spectral, spatial, and joint patterns; a Vision Transformer based tokenization and encoding stage to model global contextual relationships; and a lightweight Mamba inspired gated sequence mixing module for efficient content-aware refinement without quadratic self-attention. Principal Component Analysis (PCA) is used as preprocessing to reduce redundancy and improve efficiency. Experiments on four benchmark datasets, including Houston and three UAV borne QUH datasets (Pingan, Qingyun, and Tangdaowan), demonstrate that ConvVitMamba consistently outperforms CNN, Transformer, and Mamba based methods while maintaining a favorable balance between accuracy, model size, and inference efficiency. Ablation studies confirm the complementary contributions of all components. The results indicate that the proposed framework provides an effective and efficient solution for HSI classification in diverse scenarios. The source code is publicly available at this https URL

---


### 49. [Task Switching Without Forgetting via Proximal Decoupling](https://arxiv.org/abs/2604.18857)

**<font color=#1a73e8>作者：</font>** Pourya Shamsolmoali, Masoumeh Zareapoor, Eric Granger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In continual learning, the primary challenge is to learn new information without forgetting old knowledge. A common solution addresses this trade-off through regularization, penalizing changes to parameters critical for previous tasks. In most cases, this regularization term is directly added to the training loss and optimized with standard gradient descent, which blends learning and retention signals into a single update and does not explicitly separate essential parameters from redundant ones. As task sequences grow, this coupling can over-constrain the model, limiting forward transfer and leading to inefficient use of capacity. We propose a different approach that separates task learning from stability enforcement via operator splitting. The learning step focuses on minimizing the current task loss, while a proximal stability step applies a sparse regularizer to prune unnecessary parameters and preserve task-relevant ones. This turns the stability-plasticity into a negotiated update between two complementary operators, rather than a conflicting gradient. We provide theoretical justification for the splitting method on the continual-learning objective, and demonstrate that our proposed solver achieves state-of-the-art results on standard benchmarks, improving both stability and adaptability without the need for replay buffers, Bayesian sampling, or meta-learning components.

---


### 50. [Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents](https://arxiv.org/abs/2604.18860)

**<font color=#1a73e8>作者：</font>** Wenpeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> GUI agents that control desktop computers via screenshot-and-click loops introduce a new class of vulnerability: the observation-to-action gap (mean 6.51 s on real OSWorld workloads) creates a Time-Of-Check, Time-Of-Use (TOCTOU) window during which an unprivileged attacker can manipulate the UI state. We formalize this as a Visual Atomicity Violation and characterize three concrete attack primitives: (A) Notification Overlay Hijack, (B) Window Focus Manipulation, and (C) Web DOM Injection. Primitive B, the closest desktop analog to Android Action Rebinding, achieves 100% action-redirection success rate with zero visual evidence at the observation time. We propose Pre-execution UI State Verification (PUSV), a lightweight three-layer defense that re-verifies the UI state immediately before each action dispatch: masked pixel SSIM at the click target (L1), global screenshot diff (L2a), and X Window snapshot diff (L2b). PUSV achieves 100% Action Interception Rate across 180 adversarial trials (135 Primitive A + 45 Primitive B) with zero false positives and < 0.1 s overhead. Against Primitive C (zero-visual-footprint DOM injection), PUSV reveals a structural blind spot (~0% AIR), motivating future OS+DOM defense-in-depth architectures. No single PUSV layer alone achieves full coverage; different primitives require different detection signals, validating the layered design.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-244](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
