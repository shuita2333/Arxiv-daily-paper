# 📦 其他研究 | 2026年09月16日

> 本类共 **416** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-416](./part-09.md)

---

### 251. [An immune world model for multiscale forecasting and therapeutic hypothesis generation](https://arxiv.org/abs/2609.14709)

**<font color=#1a73e8>作者：</font>** Taoyong Cui, Xi Wang, Zonghang Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Immune therapies act across cell-intrinsic programs, tissue ecosystems, and patient-specific immune states, yet most predictors address these scales separately. We used a governed evolutionary AI Scientist to construct the Immune World Model, an action-conditioned model that learns how interventions move immune states across cellular, tissue, and individual levels. The Immune World Model--building Scientist searched candidate architectures and workflows, and the resulting world model was frozen before independent confirmation. The frozen model generalized to unseen interventions and biological contexts, recovered intervention-specific cellular programs, integrated cell and tissue information to improve ecosystem and patient-response prediction, and forecast unseen perturbation combinations. Immune World Model--guided analysis then combined measured perturbations with cross-axis inference to nominate IL-36$\gamma$ plus SIRP$\alpha$ inhibition as a complementary-axis therapeutic hypothesis, whereas a governed self-correction audit rejected every screened cytokine pair. The Immune World Model provides a framework for multiscale immune simulation that connects AI Scientist-driven model construction, intervention forecasting, and the generation of prospectively testable therapeutic hypotheses.

---


### 252. [Moral Rebel Agents: Decision-Making Under Conflicting Obligations](https://arxiv.org/abs/2609.14716)

**<font color=#1a73e8>作者：</font>** Hector Munoz-Avila, David W. Aha, Paola Rizzo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents are typically obliged to follow user-assigned tasks. However, strict obedience may conflict with moral obligations that arise during execution. This paper investigates \textbf{moral rebellion}: the ability of an autonomous agent to deviate from a user-assigned task when morally justified. We formalize five agent architectures: an \textit{amoral agent} that pursues assigned tasks without considering moral obligations, and four forms of \textbf{moral rebel agency}: (1) \textit{utilitarian agents} that opportunistically maximize task outcomes; (2) \textit{deontic} agents that enforce normative constraints; (3) \textit{utilitarian-deontic} (UD) agents that combine deontic constraints with utilitarian reasoning; and (4) \textit{dutiful} agents that additionally preserve commitments to assigned tasks. We implement these architectures within a hierarchical task network planning framework and evaluate them in a Mini Search-and-Rescue domain that exposes trade-offs among assigned-task completion, opportunistic rescue, and norm compliance. Our empirical results show that the proposed agents exhibit distinct trade-offs among rescue results, assigned-task completion, and norm compliance. In particular, the preservation of task commitments emerges as an important dimension of moral rebellion, for which the UD and dutiful agents produce substantially different behaviors despite their shared utilitarian and deontological foundations. These findings highlight the importance of commitment-aware moral reasoning for autonomous agents operating in morally consequential environments.

---


### 253. [Are Gradient Boosting Models Suitable for Intermittent Demand Forecasting?](https://arxiv.org/abs/2609.14718)

**<font color=#1a73e8>作者：</font>** Vladislav Kislinskii, Mazhar Hameed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Demand forecasting is critical in modern industry, offering opportunities to reduce costs and gain competitive advantage through improved inventory management. However, forecasting becomes particularly challenging for products with intermittent demand, where demand occurs infrequently and time series contain many zero observations. Such dynamics are common across diverse sectors, such as industrial organizations, consumer goods, aviation, automotive, and electronics. Motivated by these challenges, this paper explores the potential of gradient boosting models to improve forecasting performance. We evaluate statistical, specialized, machine learning, and ensemble approaches across multiple datasets. The results show that specialized methods achieve the strongest performance among individual models, while gradient boosting on its own tends to underperform. However, combining a machine learning model with a specialized approach improves forecasting accuracy by up to 10%, demonstrating that even simple ensembles can outperform single models. Overall, the findings highlight the value of combining machine learning with domain-specific forecasting techniques for intermittent demand.

---


### 254. [PC$^2$-AD: Point Cloud Upsampling to Safeguard 3D Anomaly Detection with Resolution-constrained Edge Devices](https://arxiv.org/abs/2609.14722)

**<font color=#1a73e8>作者：</font>** Yutong Gu, Yingxi Xie, Kejin Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-cost and low-resolution sensors used in edge deployments can produce test point clouds that are substantially sparser than the normal training data. This train-test sampling-resolution gap changes the local geometry available to a 3D anomaly detector. We propose PC$^2$-AD, a point cloud upsampling framework that compensates sparse test inputs before downstream detection. Target Domain Candidate Generation (TCG) adapts a pretrained upsampler to normal training geometry and generates a dense candidate pool. Geometry-Aware Candidate Filtering (GACF) selects candidates according to geometric spacing and spatial coverage. Normality-Preserving Point Compensation (NPPC) refines the selection by comparing candidate normality scores with those of their input anchors. The selected points are combined with the unchanged input points and processed by the existing detector. Experiments with six detectors on two Anomaly-ShapeNet settings and Real3D-AD show improvements in the mean of object-level and point-level AUROC for all six detectors in each Anomaly-ShapeNet setting and four on Real3D-AD. These results support point cloud compensation as an input-level approach to improving 3D anomaly detection under low-resolution sensing conditions. Code is publicly available at this https URL.

---


### 255. [CrossDistill: Balancing Quality and Diversity via Trajectory-Level Hybrid Few-Step Distillation](https://arxiv.org/abs/2609.14725)

**<font color=#1a73e8>作者：</font>** Yuxi Liu, Haoyu Li, Yixiang Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step distillation accelerates diffusion models but must balance diversity and fidelity: trajectory-based distillation preserves mode coverage, while distribution matching sharpens samples but can reduce diversity. We show that this tension can be exploited in a noise-regime-dependent way: high-noise steps largely determine global modes, whereas low-noise steps refine local details. We propose CrossDistill, a trajectory-level hybrid distillation framework that splits the sampling trajectory at a crossover point, applies a trajectory-preserving objective on the high-noise interval and a distribution-matching objective on the low-noise interval, and couples the two stages through the crossover state. In contrast to loss-level mixing, and complementarily to training-time two-stage recipes, CrossDistill explicitly assigns complementary objectives along the noise axis, so that global branching is preserved before local statistics are sharpened. CrossDistill is a noise-level scheduling policy: PCM and DMD are plug-in instantiations, while the noise partition, crossover coupling, and objective ordering are the key design elements. Experiments on text-to-video diffusion models and qualitative image-to-video results show that CrossDistill expands the few-step quality-diversity frontier, retaining seed-level variation while achieving competitive visual fidelity.

---


### 256. [WaVeFuse: Regime-Adaptive Equity Index Forecasting via Channel-Wise Wavelet Denoising and Vertical Attention Fusion](https://arxiv.org/abs/2609.14733)

**<font color=#1a73e8>作者：</font>** Aashish Bohra, Vivek Vijay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid Deep Learning for equity index forecasting is limited by three problems: propagation of OHLCV noise into derived technical indicators (TIs), channel-indiscriminate multi-scale decomposition that conflates heterogeneous frequency signatures, and static multi-branch fusion that cannot adapt to market regime shifts. WaVeFuse addresses these limitations through a unified dual-branch architecture. Symlet-4 wavelet denoising (level 2, MAD soft threshold) suppresses microstructure noise in OHLCV. Seven low-lag TIs computed from denoised prices are encoded by a causal channel-wise continuous wavelet transform (Morlet, 32 scales) into a per-timestep scale-space matrix. A CNN-BiLSTM branch captures temporal dynamics, while a dual-layer Transformer (heads=4, dk in {16, 32}) models inter-scale spectral dependencies, and their representations are integrated by a 2-token softmax gate Vertical Attention Fusion (VAF) that dynamically reweights branches as market regimes shift. Evaluated under walk-forward validation (WFV) on KOSPI, DAX, NYSE Composite, and Russell 2000 (2010-2023), WaVeFuse achieves R2 = 0.81-0.96 and directional accuracy 70.5-78.3%. It outperforms seven state-of-the-art models by 8.9-20.2% MAE across twelve dataset-period configurations. Diebold-Mariano statistics (4.62-10.38, p<0.001) confirm superiority over a well-tuned XGBoost benchmark across four indices. Ablation verifies component-wise contributions. Under realistic backtesting with 10 basis point transaction costs, WaVeFuse's directional strategy achieves a mean Sharpe ratio of 3.69 across four markets and limits maximum drawdown to 7.5% during the COVID-19 crash. With 152k parameters (0.68MB) and sub-1.3ms GPU inference, WaVeFuse delivers a computationally efficient, regime-robust framework suitable for research and decision-support deployment.

---


### 257. [OCT-FedSIR: Toward Trustworthy Federated Ophthalmic Learning under Annotation Noise](https://arxiv.org/abs/2609.14734)

**<font color=#1a73e8>作者：</font>** Sina Gholami, Abdulmoneam Ali, Tania Haghighi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning enables collaborative model development without centralizing patient data, but annotation reliability at participating institutions cannot always be assumed. In ophthalmic imaging, differences in disease prevalence and class composition can resemble changes caused by corrupted supervision. We introduce OCT-FedSIR, a reliability-aware spectral framework for federated OCT classification under client-dependent annotation noise and heterogeneous data distributions. OCT-FedSIR combines class-balanced spectral estimation, Stage-I logit adjustment, complementary spectral descriptors, selective spectral relabeling, and noise-aware federated optimization. We evaluated the framework on the Kermany, University of Illinois Chicago, and Wake Forest datasets under symmetric and structured asymmetric noise and three levels of non-IID heterogeneity. Across 117 experimental conditions, OCT-FedSIR achieved a mean accuracy of 86.73%, compared with 79.94% for RoFL and 78.75% for FedCorr. It correctly separated clients with original and corrupted annotations across all evaluated conditions, while the original FedSIR identification procedure was less robust, particularly under asymmetric noise. Spectral relabeling recovered 77.2% of corrupted annotations with 91.3% correction precision and a 3.5% false-correction rate. Retaining corrected clients outperformed spectral pruning by 9.30 percentage points on average. These findings show that annotation noise can often be identified and corrected without discarding informative client data.

---


### 258. [Trinqet: Private Triangle and Quadrangle Counting over Distributed Graphs](https://arxiv.org/abs/2609.14737)

**<font color=#1a73e8>作者：</font>** Mushtari Sadia, Amrita Roy Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Triangle and quadrangle counts are core statistics in graph analysis. Yet many real-world graphs are distributed across multiple parties and encode highly sensitive relationships, precluding direct data sharing. Secure multi-party computation (MPC) provides a principled alternative, but introduces a fundamental tension: the protocol must hide the graph's topology, forcing fully data-oblivious operations over all potential edges--while real-world graphs are extremely sparse, making most of this work wasted. We propose Trinqet, a system that resolves this tension through new MPC-friendly algorithms for private triangle and quadrangle detection. Trinqet safely exploits sparsity using a suite of novel techniques that eliminate vast numbers of unnecessary operations while preserving strong security in the malicious threat model. Trinqet supports both counting and enumeration and, in our evaluation, outperforms all five baselines by up to 10^5 in runtime.

---


### 259. [AppliedScientist: Automated Scientific Revision Through Iterative AI Reviewing](https://arxiv.org/abs/2609.14738)

**<font color=#1a73e8>作者：</font>** Vidushee Vats, Karun Sharma, Shengzhi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated reviewing systems are increasingly evaluated based on the quality of the reviews they produce. Yet a review is only useful if acting on it leads to a measurable improvement in the paper. We present AppliedScientist, a closed-loop system that couples an autonomous AI scientist with an AI reviewer, and evaluate it by iteratively revising rejected papers from a range of research subfields. To mirror how human authors build on earlier drafts, the AI scientist has access to its previous versions during revision. To avoid bias from prior judgments, however, each review is generated independently, with the reviewer having no memory of earlier feedback or scores. We compare three revision settings: one initialized with the original venue reviews, one initialized with AI-generated reviews, and autonomous self-revision using the same fixed prompt in every round. Because the reviewer both guides and evaluates the revision, we also assess the human-initialized revisions using Stanford Reviewer as an independent evaluator. Reviewer-guided revision consistently improves more than fixed-prompt self-revision, and Stanford Reviewer also assigns higher scores to later revisions. AppliedScientist resolves 128 of 150 execution-related weaknesses (85.3%), but only 2 of 18 idea-related weaknesses (11.1%), suggesting that iterative revision is effective at improving experiments and implementation, but rarely changes concerns about novelty or significance.

---


### 260. [PIMENTO: A Privacy Framework for Querying Text](https://arxiv.org/abs/2609.14745)

**<font color=#1a73e8>作者：</font>** Mushtari Sadia, Ang Chen, Amrita Roy Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Currently, there are two state-of-the-art, complementary privacy guarantees: contextual integrity (CI) for what may flow, and differential privacy (DP) for what may be inferred. Yet neither maps cleanly onto natural language, leaving existing approaches unable to provide these guarantees for analytics over unstructured text. We address this gap with Pimento, a framework that takes three forms of natural language: text corpus, queries, and privacy policies; and grounds them into a relational database, creating a common substrate on which both guarantees can be enforced formally. With this design, we not only provide end to end privacy guarantees, but also improvement to utility through three key contributions: DP aware Text-to-SQL, which searches for correct queries requiring the least DP noise; CI aware Text-to-SQL, which compiles natural language policies into executable CI rules over the database; and a new privacy definition we call contextual differential privacy, which redefines the traditional DP neighborhood under CI, and yields a tighter smooth sensitivity bound. Across new benchmarks, Pimento selects the best query in 75.3% of cases (upto +45 points over baselines) and achieves zero leakage under correct policy grounding. To our knowledge, Pimento is the first framework to provide formal privacy guarantees for natural language analytics under CI, DP, and their composition.

---


### 261. [From Visual Feedback to Textual Reviews: A Multi-Agent Vision-Language Framework for Image-Grounded Review Assistance](https://arxiv.org/abs/2609.14761)

**<font color=#1a73e8>作者：</font>** Utsav Kumar Nareti, Ayush Bansal, Kumari Priya 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual feedback in the form of user-uploaded images and videos is becoming increasingly common in e-commerce platforms because it provides authentic evidence of product quality, defects, packaging conditions, and real-world usage. However, visual feedback alone often lacks the contextual explanations and subjective opinions necessary for informed decision-making, while many users provide limited textual feedback due to the effort required to compose detailed reviews. To bridge this gap, we introduce image-grounded review assistance, a novel task that aims to generate editable review drafts from user-uploaded product images. Unlike conventional image captioning, which focuses on objective visual description, the proposed task requires product-specific understanding, sentiment estimation, and evidence-driven review composition under challenging real-world conditions, including degraded image quality, excessive zoom-in, target ambiguity, and partial product visibility. We propose a multi-agent vision-language framework consisting of four specialised roles: product grounding, visual sentiment estimation, visual evidence generation, and review synthesis. The framework employs explicit intermediate representations, including product entities, predicted ratings, and evidence summaries, to improve interpretability and visual grounding. Experiments on a curated subset of the Amazon Reviews Electronics dataset demonstrate the feasibility of generating coherent, product-aware, and sentiment-aware review drafts from visual feedback. To the best of our knowledge, this is the first study to formulate image-grounded review assistance as a multi-agent vision-language reasoning problem, providing a practical step toward AI-assisted review authoring in e-commerce systems.

---


### 262. [Privacy Preserving Gossip Learning](https://arxiv.org/abs/2609.14778)

**<font color=#1a73e8>作者：</font>** Erkan Bayram, Mohamed-Ali Belabbas, Tamer Başar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a decentralized privacy-preserving learning algorithm in which each agent holds a single private sample and a shared model. Samples are learned sequentially, and each update must preserve the endpoint mappings at previously learned samples while protecting private data. This gives each agent three roles: (i) a learner that updates the model parameters, (ii) a teacher whose sample is learned at the current iteration, and (iii) a protected agent whose sample has already been learned. We build on Tuning without Forgetting (TwF) method to preserve previously learned mappings and show that TwF provides an indistinguishability guarantee for the learner whenever the set of protected agents contains another sample with the same label. For the teacher, we formulate a minimax optimal control problem that models the differential privacy noise as a worst-case disturbance to prevent performance loss while maintaining the same level of privacy for the gradient. For the protected agents, we compute the projections locally and aggregate them using a private push-sum gossip protocol. We prove geometric convergence of the decentralized gossip algorithm and of the distributed projection for TwF.

---


### 263. [Evaluating AI Tutoring at the Speed of Innovation: Practitioner-Led Micro-Randomised Trials of an AI Tutoring Platform in GCSE Science](https://arxiv.org/abs/2609.14789)

**<font color=#1a73e8>作者：</font>** Wayne Harrison, Rahil Khowaja, Emma Dobson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) systems in education are developing on timescales that sit uneasily with conventional evaluation. By the time a large-scale trial has been designed, delivered, analysed and published, the technology under study may have changed materially. This creates a temporal problem for evidence-informed education: the need for timely evidence can encourage reliance on weak observational or usage data, while conventional rigorous evaluation may produce evidence too slowly to guide rapidly evolving practice. We examine teacher-led micro-randomised controlled trials (micro-RCTs) as one response to this problem. The empirical case is a four-week multisite individually randomised evaluation of Medly, an AI-powered tutoring platform, in GCSE Biology, Chemistry and Physics in English secondary schools. Of 929 students completing baseline assessment, 644 completed post-testing. In the primary ITT analysis, students allocated to Medly achieved higher post-test attainment than students undertaking business-as-usual self-directed revision (Hedges' g = 0.33, 95% CI 0.18 to 0.48). Positive estimates were observed in Physics (g = 0.31), Chemistry (g = 0.32) and Biology (g = 0.52), with no evidence of differential impact by disadvantage status. Greater platform engagement was associated with higher attainment, but these post-randomisation analyses are treated as exploratory rather than causal. Attrition was substantial (30.7%), outcome measures were curriculum-aligned rather than standardised, and process evaluation response was limited. We therefore interpret the findings as preliminary. We argue that the value of micro-RCTs for educational AI lies not in replacing definitive evaluation with small studies, but in enabling a rapid, cumulative evaluation architecture in which randomised estimates can be generated, replicated and updated as technologies and their implementation evolve.

---


### 264. [Python Import as an Execution Boundary: An Empirical Study of Bugs, Vulnerabilities, and Analysis Gaps](https://arxiv.org/abs/2609.14791)

**<font color=#1a73e8>作者：</font>** Baihong Chen, Wen Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Python import does more than resolve dependencies: it executes code during module and package initialization. This behavior can trigger failures, load dynamic or native code, access resources, or change security-sensitive state before an application calls a package API. Prior work studies package selection, malicious packages, or package vulnerabilities. We present ImportMine, a study of import-related bugs and security vulnerabilities in Python software. We combine security advisories with PyPI project histories and use source and patch evidence to confirm how import activates cases, why the problem occurs, how developers fix it, and what program information is needed to explain the behavior. We retain 31 import-related advisory vulnerabilities and 38 application-data boundary cases and confirm 1,429 project-history bugs across 1,302 repositories. Among the project-history bugs activated during initialization, 97.6% stop or disrupt normal execution. In contrast, 90.0% of the 20 initialization- activated advisory vulnerabilities are High or Critical. Module-level code and package initialization activate 98.3% of the analyzed history cases. Dynamic loading is much less common, but most of its cases perform security-sensitive actions. We also find that many fixes change when an import becomes active instead of removing the dependency. Finally, we derive ImportVulBench, 228 paired pre-fix and fixed programs covering all 11 bug types.

---


### 265. [Mind Which Bird You Favour: Parameterizing Adequacy-Fluency Balance in Meta-Evaluation of Machine Translation](https://arxiv.org/abs/2609.14795)

**<font color=#1a73e8>作者：</font>** Behzad Shayegh, Niloofar Kazemi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There is a tradeoff in machine translation meta-evaluation between prioritizing alignment with adequacy versus fluency. The balance depends on the combination of translation systems in the meta-evaluation dataset. This system set is a small, filtered sample whose characteristics change heavily across years and language pairs; it does not represent the true system distribution. Consequently, the adequacy-fluency balance is often unrepresentative and subject to change. For sensitive domains, controlling this balance is critical. We expose this balance as a tunable choice. To achieve a target balance, we reweight existing systems while minimizing distortion from uniform weighting, ensuring the evaluated systems remain real and representative. We provide an exact optimization algorithm with theoretical guarantees and pruning mechanisms to compute these weights. To validate meta-evaluation internal consistency, we design a scorer-augmentation framework that establishes a known relative identity for the scorers. Results demonstrate that our reweighting method effectively controls the adequacy-fluency balance and preserves the internal consistency, outperforming prior approaches. Finally, we analyze the performance of popular scorers across a sweep of this parameter.

---


### 266. [When Apps Outlive Vendors: Security Implications of IoT Abandonware](https://arxiv.org/abs/2609.14798)

**<font color=#1a73e8>作者：</font>** Dayeon Kang, Elvis Yeboah-Duako, Sachin Thomas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As the Internet of Things (IoT) market continues to expand, many companion apps are being published in app stores, raising security concerns for those whose vendors have abandoned support. Even after vendors discontinue support, such applications frequently remain operational on users' mobile devices, continue to interface with users' IoT devices and collect user data without receiving security updates. This leaves known and newly discovered vulnerabilities unmitigated, increasing risks of remote exploitation, unauthorized device access, and prolonged data misuse. We define these abandoned applications as "IoT abandonware" and present the first large-scale measurement study of the security risks associated with discontinued applications.
We analyze 61,500 IoT companion Android applications that had not been updated for at least two years or were no longer in service as of March 2025. From decompiled binaries, we extracted latent and embedded resources (e.g., bundled libraries, domain names, and permissions), and assessed their security implications. First, we identify outdated dependencies with post-abandonment CVE reports and discover domains vulnerable to takeover or data exfiltration. Second, we perform static data-flow analysis to trace how sensitive data, inferred from the extracted permissions, propagates to broken or hijackable external endpoints. We found that persistent analytics and third-party trackers continue aggregating user data and device telemetry long after vendor control lapses, creating data flows that adversaries can redirect or abuse. Overall, we identified security risks in 73.6% of our dataset, with 30 of the top 1,000 most-installed apps sending data to broken external endpoints.

---


### 267. [Inheriting the Count: How Visualization Literacy Got Its Measure](https://arxiv.org/abs/2609.14813)

**<font color=#1a73e8>作者：</font>** José Bener, Miriah Meyer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Foundational frameworks in visualization have operationalized literacy as an individual competency, measured through chart-comprehension tasks. This focus raises a question: why has measurement become the dominant frame for understanding literacy? Rather than asking whether literacy should be measured, we ask how measurement became the field's way of understanding it. We trace visualization literacy back through the history of textual literacy and argue that in adopting the term, the field imported three values rooted in early government statistics: quantification, individualization, and binary classification. To mark the shift this history makes possible, we distinguish two waves: a first centered on assessment and individual proficiency, and a second that treats literacy as a situated practice, attentive to how people use visualizations in context and to the purposes they serve. Examining the construct this way suggests that refining assessment instruments does not, by itself, settle what literacy is, and points to directions for second-wave research: formative studies of literacy in context, culturally grounded instruments, and critical reading. This paper shows that visualization literacy inherited its measurement frame rather than discovering it, offers a two-wave vocabulary distinguishing assessment-based literacy from situated practice, and connects the field to a critical-literacy tradition with concrete alternatives to measurement. These contributions allow us to treat measurement and meaning as two parts of a single question, shifting attention from who counts as literate to what literacy is meant to do.

---


### 268. [Tone on a Budget: A Reference-Free Metric for Lexical Tone in Massively Multilingual Text-to-Speech](https://arxiv.org/abs/2609.14817)

**<font color=#1a73e8>作者：</font>** Moses Daudu, Adeola Enitan Bamidele, Honor-Jesus Bezaleel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In Yorùbá, pitch alone separates \d{o}k\d{o} (husband, Mid), \d{o}k\d{ò} (vehicle, Low), and \d{o}k\d{ó} (hoe, High) -- the diacritics ARE the tone marks. Yet character error rate (CER), the standard automated metric for text-to-speech (TTS), is in practice computed from ASR output that drops those marks: a synthesizer can ace CER and still say vehicle for husband. We introduce DunDun -- named for the dùndún, the Yorùbá talking drum that speaks through pitch alone -- an automated, reference-free lexical-tone metric that needs no tone-labelled corpus. The gold High/Mid/Low sequence is read from the input text's diacritics (in TTS that text exists by construction, so no reference recording is needed); the prediction comes from the audio's pitch track. We validate three ways. Flattening pitch with PSOLA resynthesis collapses DunDun while CER does not move. Inverting High and Low in the answer key of 300 native recordings drives the two-class readout to 0.14, symmetrically below its 0.35 chance level -- a consistency check on the scoring path, not independent evidence. And three native listeners, over 67 blind A/B trials, pick the tone-correct clip 89.6% of the time (95% CI 80.0-94.8; p < 1e-4); whether DunDun tracks those judgements trial by trial is not resolved at this sample size. Applied to a massively multilingual zero-shot TTS model, DunDun shows what CER cannot: Yorùbá tone sits near the native anchor before any Yorùbá fine-tuning (0.567 +/- 0.02 over five decode seeds vs. 0.596; chance 0.33), despite the 21.4% CER the model's own paper reports; and a few hours of clean audio halve CER (5.6% to 2.7% by 5h, 1.7% by 15h) while tone saturates within the hour. On non-tonal Swahili, CER already captures the gains: the metric a language needs is language-dependent. We release the metric and the complete validation protocol.

---


### 269. [MedTRACE: Tool-Augmented Multimodal Clinical Reasoning Agents for Evidence-Grounded Decision-Making](https://arxiv.org/abs/2609.14823)

**<font color=#1a73e8>作者：</font>** Ji Lu, Lifei Liu, Haoran Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal clinical decision-making requires reliable reasoning over heterogeneous evidence from electronic health records, medical images, and physiological signals. Existing models typically map these inputs directly to diagnoses without explicitly assessing evidence sufficiency, tool-use requirements, or diagnostic uncertainty. This paper presents MedTRACE, a tool-augmented multimodal clinical reasoning agent for evidence-grounded decision-making. MedTRACE uses modality-specific encoders to construct a unified patient-state representation and performs an iterative loop of hypothesis formation, toolaware deliberation, and evidence verification. It dynamically invokes visual grounding, evidence retrieval, and structured parsing tools to locate diagnosis-relevant regions, retrieve clinical knowledge and similar cases, and extract structured findings. The acquired evidence enters an evidence memory, where a consistency verifier confirms or revises the current hypothesis. MedTRACE outputs a diagnosis together with supporting evidence, an auditable reasoning trace, and calibrated confidence. Experiments on multiple multimodal clinical diagnosis benchmarks show that MedTRACE improves diagnostic accuracy by 5.4% and AUROC by 4.7 percentage points over the strongest baseline. It also improves evidenceselection F1 by 8.2 percentage points and visual-grounding IoU by 6.5 percentage points, reduces expected calibration error by 31.6%, and decreases unsupported diagnostic errors by 27.8%. These results demonstrate that active evidence acquisition and verification improve the accuracy, interpretability, and reliability of multimodal clinical decisionmaking.

---


### 270. [One Model, Two Physical Stories: Auditing Misalignment in Multi-Modal World Modeling](https://arxiv.org/abs/2609.14833)

**<font color=#1a73e8>作者：</font>** Geigh Zollicoffer, Minh Vu, Rajiv Ranasinghe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models, systems that generate what happens next given current environmental conditions, are increasingly being implemented with multi-modal generation in mind. However, generating multiple modalities simultaneously, such as visual simulations alongside physical state predictions in the form of text, introduces the risk of cross-modal inconsistency. Tested separately, both outputs may look convincing while still disagreeing: a model can calculate that a ball should rebound in one modality, then generate no rebound in another modality, to say nothing of diverging from real-world dynamics entirely. In this work we focus on two failures explicitly: \emph{Internal misalignment}, the disagreement between the world model's generated video and the same world model's prediction in a different modalities, and \emph{external misalignment} the disagreement between the world model's generation and an analytic physical environment. We derive common contracts of event, magnitude, timing, and construct a physics grounded pipeline to make comparisons measurable in both external and internal settings. We then ask whether progressively supplying the model's own contract (the A ladder for the internal setting) or a corrected physical contract (the B ladder for the external setting) closes the respective gaps. Across four mechanisms and 20 settings, we find that while language answers all 22 text probes correctly with respect to the true environment, the neutral video is often in disagreement, suggesting that the current unified backbones may not be capable of correct reasoning, internal consistency, and external physical fidelity all at once.

---


### 271. [Tackling Failure Modes of PINNs and PIKANs Using Conflict-Free Gradients](https://arxiv.org/abs/2609.14841)

**<font color=#1a73e8>作者：</font>** Sidharth S. Menon, Irina Tezaur, Ameya D. Jagtap  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific machine learning methods such as physics-informed neural networks (PINNs) increasingly rely on domain decomposition for better scalability while solving partial differential equations (PDEs) over complex geometries, yet the resulting composite loss comprising residual, boundary, and interface terms is highly susceptible to conflicting gradients that degrade training. This work bridges domain decomposition with projection-based gradient surgery to systematically mitigate such conflicts in 2D and 3D settings. We evaluate two existing projection-based algorithms, PCGrad and ConFIG, and identify their performance degradation in specific scenarios such as 3D domains with multiple overlapping interfaces. To address this limitation, we propose Norm-PCGrad, a normalized variant that achieves state-of-the-art accuracy across a range of 2D and 3D domain decomposition problems. Across the benchmarks considered, Norm-PCGrad consistently achieves the lowest relative $L_2$ error compared to training without gradient surgery as well as to existing algorithms such as PCGrad and ConFIG, while incurring negligible additional computational overhead. To improve computational efficiency of domain decomposition frameworks such as Extended PINN (XPINN), we propose replacing vanilla PINNs in selected subdomains with separable architectures such as Separable PINN (SPINN), reducing the computational cost from quadratic (or cubic) to linear. We additionally demonstrate that gradient surgery extends to physics-informed Kolmogorov-Arnold Networks (PIKANs), yielding substantial accuracy improvements for 3D domain decomposition and confirming the generality of the proposed approach across network architectures.

---


### 272. [A Responsive Present, a Shared Past, a Social Other: Teens' Overreliance on Companion AI Chatbots](https://arxiv.org/abs/2609.14843)

**<font color=#1a73e8>作者：</font>** Mohammad Namvarpour, Tyler Chang, Afsaneh Razi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI companions provide socially engaging interaction through availability, personalization, memory, roleplay, and emotionally responsive language. For teens, these systems may support sensitive self-disclosure, identity exploration, and relationship rehearsal while shaping intimacy expectations, offline relationships, emotional wellbeing, and self-understanding. We analyzed 17,053 verified quotations from 3,930 teen-relevant Reddit posts using thematic analysis. We identified 53 topics across seven thematic groups. Users described AI companions as sources of comfort, recognition, identity exploration, and relationship rehearsal, but also reported problematic attachment, social substitution, emotional dependence, and disruption to academic and social life. Roleplay, memory, perceived reciprocity, unwanted romantic or sexual role drift, privacy concerns, platform changes, and service interruptions shaped users' boundaries and control. Awareness that the AI was artificial did not prevent guilt, obligation, grief, or distress. These findings show that companion-AI safety must address relationships over time through user-controlled memory, privacy, relational boundaries, and healthy disengagement.

---


### 273. [RAIN: Region-Aware Inversion Network for Semantic Watermark Extraction](https://arxiv.org/abs/2609.14856)

**<font color=#1a73e8>作者：</font>** Zilai Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic watermarks for diffusion models embed ownership information into the generative process while preserving perceptual quality, but Gaussian-Shading extraction conventionally requires multi-step diffusion inversion to recover the initial noise. Recent one-step methods show that this cost can be reduced substantially. We study this problem through extended flow matching and conditional regression. The key observation is that, near the high-SNR image endpoint, recovering a useful noise statistic given by the first-step output of the extended flow matching in the high-SNR regime is much simpler than reconstructing the full inverse trajectory, and Gaussian Shading only requires the recovered latent to remain in the correct watermark decision region. Based on this observation, we propose a lightweight, prompt-free extractor that decomposes endpoint recovery into an image-like anchor and a noise-oriented residual, which increases the capability of the model to utilize GPU parallel computation. The resulting method avoids iterative inversion and repeated evaluation of a diffusion-scale U-Net, providing an efficient one-step extraction pipeline with a concise theoretical interpretation. The computational cost of extracting noise is lower than that of both OSI and FARI. The github repo is there: this https URL

---


### 274. [Domain Generalization for Smartphone-Based Human Activity Recognition: A Systematic Analysis of Components and Interactions](https://arxiv.org/abs/2609.14863)

**<font color=#1a73e8>作者：</font>** Otávio Oliveira Napoli, Edson Borin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Smartphone-based Human Activity Recognition (HAR) models often degrade under distribution shifts caused by changes in users, devices, sensor placements, environments, and acquisition protocols. Domain Generalization (DG) addresses this problem by learning from source domains without access to target data. Existing DG methods span training objectives, representation initialization, and architectural modifications, but these components are typically evaluated in isolation despite operating at different stages of the learning pipeline. We present a large-scale controlled benchmark of DG for smartphone-based HAR, comprising more than 410,000 experiments across four model architectures, thirteen training objectives including Empirical Risk Minimization (ERM), five initialization strategies, four architectural configurations, and two shift scenarios: cross-dataset and cross-position. Results show that individual DG components provide limited and highly conditional gains. Alternative objectives rarely outperform ERM consistently, self-supervised initialization helps in specific settings, and architectural modifications, particularly Dynamic Domain Generalization, provide the clearest standalone improvements. Joint configurations, however, frequently outperform their individual components and exhibit complementary and sometimes super-additive interactions, although gains remain model- and shift-dependent. Class-level analysis shows that the strongest configurations mainly improve difficult, shift-sensitive decision boundaries. Finally, oracle checkpoint analysis reveals substantial unrealized performance: source-validation selection recovers only 53% and 26% of the available oracle gain in cross-dataset and cross-position settings, respectively. Overall, effective HAR domain generalization requires jointly designing DG components and robust model-selection strategies.

---


### 275. [Interpolation Is Not Invariance: Pair Count Is Not Coverage in Transformation Audits](https://arxiv.org/abs/2609.14870)

**<font color=#1a73e8>作者：</font>** Mohammed Ahnouch, Lotfi Elaachak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counting equivalent pairs is a common way to report transformation-audit coverage, but it can substantially overstate the constraints imposed by an audit: pairs generated from the same semantic object are correlated, and complete orbit graphs contain algebraically redundant edges. We therefore distinguish four complementary quantities---edge count $m$, effective contrast rank $s$, population support rank $r$, and graph spectral gap $\eta$---and characterize their roles in audit coverage and deployment reliability. Under a rank-$r$ Gaussian contrast model, a population-invariant calibrated reader exists exactly when the anchor has a component in $\ker T$. When an audit has rank $s < r$, its unobserved risk is $R^\star/U$, with $U \sim \operatorname{Beta}((r-s)/2,s/2)$; when $s \ge r$, exact calibrated interpolation is infeasible. The same distinction appears in orbit topology: a spanning tree imposes the same exact-null constraints as a complete graph, while a sharp graph Poincare inequality propagates edge-level drift to an entire orbit at a cost proportional to $1/\eta$. Cyclic audits can additionally yield zero pair-level leave-one-out error without holding out any semantic object.
To address these failures, we derive exact block-Woodbury leave-one-orbit-out updates and introduce a source-disjoint deployment gate over finitely many candidate readers. The gate retains the original reader unless uncertainty bounds certify lower drift within a prescribed clean-utility budget. etc..

---


### 276. [SeqMaestro: From nucleotide sequences to biological hypotheses through interpretable machine learning](https://arxiv.org/abs/2609.14882)

**<font color=#1a73e8>作者：</font>** Evgeny S. Saveliev, Krzysztof Kacprzyk, Charlotte Capitanchik 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nucleotide sequence analysis is central to problems spanning regulatory genomics, evolutionary biology, and phenotype prediction. Classical bioinformatics methods extract interpretable sequence properties such as motifs and k-mer composition, but their flexibility is limited. In contrast, modern deep learning models can learn powerful predictive representations directly from raw sequences, yet their internal representations and decision mechanisms are difficult to inspect. Interpretable machine learning methods (e.g., sparse linear models and decision trees) provide human-understandable representations of predictive relationships but are not designed to operate directly on nucleotide sequences. Here, we introduce SeqMaestro, a machine learning framework that proposes biological hypotheses from nucleotide sequences using interpretable models. Our solution is centered around a two-layer interface that connects nucleotide sequences with the broader ecosystem of interpretable machine learning. SeqMaestro uses this interface to fit diverse combinations of interpretable models, feature representations, and extraction strategies, leveraging variability across transparent models to identify robust biological signals and richer predictive relationships than feature importance alone can provide. The system also supports data transformation and cleaning, model fitting, hyperparameter tuning, reliability analysis, and synthesis of results into a contextualized written report. By providing these capabilities through a no-code workflow, SeqMaestro is designed to make interpretable sequence analysis accessible to researchers without requiring extensive programming or machine learning expertise. SeqMaestro thereby provides an accessible route from nucleotide sequences to biological hypotheses.

---


### 277. [PeerPen: AI-Assisted Writing for Online Mental Health Peer Support](https://arxiv.org/abs/2609.14886)

**<font color=#1a73e8>作者：</font>** Jiwon Kim, Sherry Gong, Maya Ajit 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Online mental health communities thrive on peer support, yet those who volunteer to help often lack formal training and may struggle to articulate supportive responses. AI co-writing could lower this barrier; however, peer support derives much of its value from being perceived as personal, raising questions around authorship, ownership, and trust. We built PeerPen, a writing assistance tool embedded within a Reddit-like interface, supporting two main features: draft generation and revision of user-written responses. Through semi-structured interviews with 15 participants, we find that PeerPen reduced the burden of composing responses and increased confidence in offering support. Participants wanted AI to assist their writing without taking over authorship and anticipated tensions around authenticity and trust. Such assistance could make authorship uncertain even for responses written without it, weakening trust across the community. We contribute design implications for AI writing assistance that scaffolds supportive communication, preserves authorship, and accounts for community-level trust.

---


### 278. [Toward an Empirical Probabilistic Risk Manifestation Model of Organizational Cybersecurity in SMEs](https://arxiv.org/abs/2609.14888)

**<font color=#1a73e8>作者：</font>** FNU Nurjahan, Aidan Eiler, Mst Eshita Khatun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a cross-layer empirical study of organizational cybersecurity risk in Small and medium-sized enterprises (SMEs), analyzing 281 validated security findings from 22 real-world SME cybersecurity assessments conducted over two years through a pro bono university cybersecurity clinic. We first identify recurring organizational security functions through iterative thematic coding, then estimate an empirical Risk Manifestation Model linking these functions to exposure conditions, attack mechanisms, and cybersecurity outcomes, and use probability propagation to identify dominant risk pathways. The model characterizes empirical associations observed in this sample rather than causal or predictive relationships. Our analysis identifies eight organizational security functions associated with two exposure conditions, five attack mechanisms, and six outcome categories. Across most functions, the dominant pathway follows asset exposure to credential compromise to unauthorized access, whereas infrastructure and network security primarily propagates through network exposure; these pathways remain stable under leave-one-organization-out analysis. Finally, we evaluate whether SME cybersecurity assessments can be simplified while preserving meaningful security coverage. Retaining six functions reduces assessment burden by 24% while preserving 97% of critical findings and 92% of risk-pathway coverage, a security-oriented reduction, while retaining five functions reduces burden by 45% while preserving 89% of critical findings and 85% of risk-pathway coverage, a more efficiency-oriented alternative.

---


### 279. [What Makes a 3D Scene Editable? A Factorized Benchmark of Fidelity, Locality, Consistency, and Preservation](https://arxiv.org/abs/2609.14899)

**<font color=#1a73e8>作者：</font>** Sariah Patro, Arjun Mehra, Nikhil Bhatia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural 3D scene editing is often evaluated by semantic alignment alone, although a convincing result may alter unrelated content or become inconsistent across views. We introduce EditBench3D, a representation-agnostic benchmark that treats editing as controlled information replacement. It evaluates four complementary properties: instruction fidelity, spatial locality, cross-view consistency, and preservation of non-target content. The protocol combines visibility-aware 3D target supports, paired descriptions, held-out cameras, and five edit families covering appearance, material, geometry, and object-level changes. We evaluate eight representative NeRF, 3D Gaussian Splatting, hybrid, and proxy-based editors on 240 scene-edit pairs. The study shows that semantic fidelity is only weakly associated with the other editing properties, and that no single method is optimal across all dimensions. Explicit Gaussian editors offer a strong overall balance, whereas direct proxy manipulation provides the most conservative edits at the cost of open-ended fidelity. These findings support reporting editability as a multi-objective profile rather than a single semantic score.

---


### 280. [First Impressions: How Placement Shapes the Influence of AI Summaries](https://arxiv.org/abs/2609.14900)

**<font color=#1a73e8>作者：</font>** Wang Claire, Agam Goyal, Frederick Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-generated summaries increasingly mediate how people interpret information across platforms, including product reviews on e-commerce sites. Using Amazon's AI summaries as a case study, we conducted a preregistered, randomized experiment (N = 278) comparing how AI summaries and user reviews shaped product perceptions, and how their influence varied with valence and presentation order. We found that both AI summaries and user reviews influenced participants' opinions, with negative summaries having a larger effect than positive ones. Presentation order was the most important factor: the first source anchored judgment and only user reviews could displace an existing anchor. Although participants reported preferring user reviews, they often underestimated the influence of AI summaries on their judgments. Our findings show how the placement of AI summaries shapes user perception and highlight opportunities to design interfaces that support more deliberate judgments about when to rely on summaries and when to examine the underlying content directly.

---


### 281. [Cross-Block Conditioning in Deep Boltzmann Machines for Statistical Data Fusion](https://arxiv.org/abs/2609.14934)

**<font color=#1a73e8>作者：</font>** Junichiro Niimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Statistical data fusion combines two panels that share a block of covariates but observe disjoint outcome blocks, and in its traditional form no row observes both outcomes at once. That rules out the discriminative criterion one would rather train a Deep Boltzmann Machine with, since multi-prediction training needs ground truth for whatever it holds out. We propose observed-block multi-prediction, which restricts the multi-prediction objective to targets drawn from what each row actually observes. It is well defined for any missingness pattern and reduces to the original criterion when rows are complete. Having a discriminative criterion that survives the setting lets us ask whether the joint model is needed at all, by separating what it contributes into a representation part and an inference part. On two consumer panels, on grids over sample size and covariate width spanning 35 cells and 875 runs, the fine-tuned DBM is the best of fifteen methods in every cell; but almost none of that advantage comes from generative pre-training, which is confined to the smallest sample size on one dataset and absent on the other. It comes from conditioning on one outcome block when predicting the other. This term amounts to +0.19 and +0.07 percentage points, is positive in all 35 cells, and, unlike every other contribution we measure, neither decays as the panels grow, nor requires a second hidden layer, nor requires more inference. Permuting one outcome block to destroy its association with the other removes the gain entirely, which is what the account predicts. The margins are small. But a small effect that does not decay is a different object from one that does, because it rests on evidence that no model mapping covariates to outcomes can accept.

---


### 282. [The Dynamic Organization of Sustained Human-AI Cognition: From Construct-Level Change to Relational Structure](https://arxiv.org/abs/2609.14942)

**<font color=#1a73e8>作者：</font>** Zijian Ru  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative artificial intelligence becomes a routine participant in writing, learning, information retrieval, analysis, decision making, and problem solving, human-AI cognition research must address not only whether AI changes psychological constructs, use intensity, or task performance, but also how human cognitive activity is organized beneath similar aggregate indicators. This article proposes a dynamic cognitive organization framework that shifts analysis from construct-level change to relational organization anchored in the person's current task-cognitive state under sustained AI participation. The framework distinguishes five relational dimensions: execution locus, cognitive governance, representational reorganization, process organization, and reachable cognitive space; it also proposes a path-specific recursive principle whereby interaction outcomes, costs, and experiences may selectively reweight future probabilities of different organizational pathways. Five sets of testable propositions follow: the same overall AI-use intensity can correspond to different cognitive organizations; similar immediate outcomes can arise from different organizations with different predictive value for proximal subsequent outcomes; longitudinal organizational change need not track overall AI-use intensity; expansion of reachable cognitive space and displacement of pre-existing or emerging human-originated pathways may coexist within one episode; and recurrent cognitive organizations may redistribute cognitive practice opportunities, with accumulated differences potentially corresponding to different developmental trajectories in strategies, habits, and abilities. The contribution is an analytic level and five-dimensional relational structure for describing, comparing, measuring, and testing process differences that aggregate indicators or construct-level analyses do not uniquely determine.

---


### 283. [ThreshGuide: Class-Aware Labeled-Guided Thresholding for Semi-Supervised 3D Abdominal Multi-Organ Segmentation](https://arxiv.org/abs/2609.14943)

**<font color=#1a73e8>作者：</font>** Hongyu Liu, Yinlong Wang, Lusha Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pseudo-labeling is a strong paradigm for semi-supervised medical image segmentation, yet its effectiveness is highly sensitive to confidence thresholding. In abdominal multi-organ segmentation, a fixed global threshold is particularly suboptimal because organ classes differ substantially in size, appearance, and learning difficulty. In this work, we propose ThreshGuide, a class-aware threshold adaptation framework that uses labeled data to guide pseudo-label selection on unlabeled data. Built upon a standard teacher-student architecture, the teacher model evaluates labeled samples during training to estimate class-aware threshold targets by maximizing an error-aware F\b{eta} criterion that balances precision and coverage. These targets are then smoothed with an exponential moving average (EMA) and used to filter unlabeled voxels in a class-dependent manner. Experiments on FLARE2022 and AMOS2022 show that ThreshGuide performs competitively overall, yielding clear improvements specifically on hard-to-learn organs.

---


### 284. [Cloud Workflow Scheduling Based on Graph Attention-Driven Hierarchical Reinforcement Learning](https://arxiv.org/abs/2609.14952)

**<font color=#1a73e8>作者：</font>** Zongjin Li, Shaohan Feng, Chunxi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic cloud workflow scheduling must balance deadline satisfaction, container utilization, and energy consumption while dealing with stochastic task-execution speeds, placement-dependent communication, and coupled task and container decisions. Workflows are naturally modeled as directed acyclic graphs (DAGs), but conventional vector- or matrix-based states do not fully capture their dependency topology. To better represent task urgency and structural relationships, we assign predicted sub-deadlines to tasks and use a multi-head graph attention network (GAT) to extract dependency information from the evolving DAGs. Based on these representations, we develop a Graph Attention-Driven Hierarchical Reinforcement Learning (GA-HRL) framework and model the scheduling process as an event-driven hierarchical semi-Markov decision process (SMDP). Workflow arrivals and task completions trigger scheduling events. At each scheduling event, the Task Scheduling (TS) agent first processes the currently ready tasks by assigning them to admissible existing containers or requesting new ones. The requested containers are then processed by the Container Scheduling (CS) agent for host placement before the environment advances. The two agents are trained alternately using separate Proximal Policy Optimization (PPO). Experiments on the 2018 Alibaba cluster trace show that GA-HRL maintains competitive workflow success rate and, in settings where success is comparable, generally achieves higher container utilization and lower energy consumption. Under the largest speed variation, it trades a small success-rate margin for substantially lower energy. Simulation code is available at: this https URL.

---


### 285. [High-Probability Nash Regret for Decentralized Learning in Markov $α$-Potential Games: Episodic and Fully Online Asynchronous Algorithms with Applications to Markov Congestion Games](https://arxiv.org/abs/2609.14959)

**<font color=#1a73e8>作者：</font>** S. Rasoul Etesami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study decentralized learning of Nash equilibria (NE) in infinite-horizon discounted Markov games under bandit feedback, focusing on Markov $\alpha$-potential games. We develop KL-projected natural policy gradient (NPG) algorithms in two settings: an episodic setting with frozen policies during sampling and a fully online setting in which players receive a single realized cost sample per time step and update their policies asynchronously along a continuing trajectory. We establish finite-time high-probability NE regret bounds of order $\widetilde O(T^{-1/4})$ and $\widetilde O(T^{-2/15})$ for the episodic and fully online settings, respectively, up to fixed approximation terms. Crucially, our bounds eliminate the distribution-mismatch coefficient, which can scale prohibitively with the size of the state space, while accommodating potential approximation, estimation-oracle bias, and transition sensitivity. We further identify a state-wise potential structure that yields sharper guarantees with additive dependence on the potential approximation error $\alpha$. We specialize the framework to independent-resource Markov congestion games (IMCGs), establish their approximate-potential and transition-sensitivity properties, and construct decentralized estimation oracles from realized costs. As an application, we introduce strategic online job scheduling on stochastic machines and obtain a scalable decentralized algorithm for learning stable dispatching policies. Overall, our results provide the first finite-time high-probability NE regret guarantees for fully online asynchronous decentralized learning in Markov $\alpha$-potential games, remove distribution-mismatch coefficients from the regret bounds, accommodate fixed estimation-oracle bias, and provide scalable decentralized learning with finite-time guarantees for IMCGs.

---


### 286. [Geometric Flow enhanced Graph Coarsening](https://arxiv.org/abs/2609.14962)

**<font color=#1a73e8>作者：</font>** Chaoqun Fei, Guoxuan Li, Tinglve Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, researchers have proposed a graph pooling operation, akin to the pooling process in conventional convolutional neural networks (CNN), aimed at reducing the computation cost of Graph convolutional neural networks (GCNNs). While most GCNN-based methods treat graph pooling as a node clustering problem and propose learning a cluster assignment matrix, existing clustering-based pooling methods tend to focus solely on the rough topology information of graphs, neglecting the exploitation of higher-order mutual connections among neighbors. In terms of message passing on graph, the ease of information passing on edges reflects the closeness between neighboring nodes, which significantly relies on the interconnectivity among neighbors. In this study, we address this gap by considering such local connection information and introducing a novel graph pooling method named RicciPool. We introduce discrete graph curvature, particularly Ollivier-Ricci curvature, as a measure of higher-order connectivity around an edge. Subsequently, we construct an Ollivier-Ricci flow formula to reweigh edge weights, leveraging the crucial information provided by Ricci curvature, particularly vital for extracting clusters in graphs. Building upon this foundation, we utilize the spectral clustering technique to learn a new cluster assignment matrix. Experimental results on multiple bioinformatics protein datasets and social networks underscore the effectiveness of our proposed method.

---


### 287. [MoVT: Video-Augmented Motion Tokenizer for Text-to-Motion Generation](https://arxiv.org/abs/2609.14965)

**<font color=#1a73e8>作者：</font>** Beibei Jing, Tianle Guo, Youjia Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven 3D human motion generation models face significant challenges in responding to diverse and unconstrained textual prompts, primarily due to the limited availability of 3D motion training data. To address this, we introduce MoVT, a novel framework that effectively leverages the extensive range of human action videos to enhance text-to-motion generation. At the core of our approach is the cross-modal augmented motion tokenizer, which projects discrete 3D motion tokens into the 2D domain. This projection allows us to enrich the motion codebook with complex, real-world motion patterns derived from videos. The enriched discrete tokens are then mapped back to the 3D domain, resulting in aligned 3D and 2D codebooks with an enhanced capacity to represent intricate motions. These enhanced codebooks are integrated into a generative masked transformer, which predicts masked motion token indices in a modality-agnostic manner. This enables the use of text-index pairs, generated from the 2D codebook and annotated motion videos, to further enhance the generator. Extensive empirical evaluations show that MoVT performs favorably against prior state-of-the-art methods across multiple key metrics.

---


### 288. [HiGFRL: Hierarchical Graph Fusion-Driven Reinforcement Learning for Dependency-Aware Task Scheduling in Heterogeneous Cloud](https://arxiv.org/abs/2609.14968)

**<font color=#1a73e8>作者：</font>** Tiangang Li, Shi Ying, Xiangbo Tian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online scheduling of dependency-aware tasks in heterogeneous cloud clusters is a fundamental yet challenging problem due to the complex interplay between DAG topologies and multi-dimensional resource constraints. While DRL has shown promise, existing GNN-based approaches often struggle to efficiently model high-order topological dependencies and suffer from loose coupling between task and resource states, leading to myopic scheduling decisions. To address these limitations, we propose HiGFRL, a Hierarchical Graph Fusion-Driven Reinforcement Learning framework. HiGFRL constructs a novel three-level state representation comprising a Static Hypergraph, a Dynamic Global Graph, and a Local Bipartite Graph to explicitly model the interplay between task dependencies and real-time cluster dynamics. Specifically, we design a fusion-driven dual-network architecture to optimize RL decision-making, where a Context Fusion Allocator integrates local bipartite matching features with fused global context to execute precise task-to-node allocation, and a Global State Evaluator leverages the global dynamic graph representation to accurately estimate expected long-term cumulative reward. Furthermore, we incorporate a topology-prior-guided hybrid reward mechanism that distills static topological priors into the learning process to accelerate convergence. Extensive experiments using real-world Alibaba cluster traces demonstrate that HiGFRL significantly outperforms heuristics and DRL baselines. Specifically, in challenging large-scale high-load scenarios, HiGFRL reduces the Makespan by up to 32.55%, and optimizes the average task flow time and average task wait time by 13.58% and 13.79%, respectively. Experimental results confirm that HiGFRL not only significantly improves cluster throughput but also ensures superior QoS by substantially reducing queuing delays. Code Release:this https URL.

---


### 289. [Learning to Solve Stochastic Controls with Unknown Drifts and Running Rewards: Theory, Algorithms and Convergence](https://arxiv.org/abs/2609.14972)

**<font color=#1a73e8>作者：</font>** Jin Ma, Gaozhan Wang, Jianfeng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study continuous-time and possibly high-dimensional stochastic control problems where drift coefficients and running reward functions are unknown. Due to these missing model primitives, we take the exploratory, reinforcement learning (RL) framework of Wang, Zariphopoulou, and Zhou(2020) with relaxed controls and entropy regularization. The objective is to develop theoretically grounded, efficient and scalable RL algorithms to learn both the optimal value functions (which also solve the exploratory HJB equation) and optimal exploratory feedback control policies. When the diffusion coefficients do not contain control, we employ probabilistic representations of both the optimal value function and its gradient based on an auxiliary state process depending only on the diffusion part of the original dynamics. With a delicate analysis on some properly defined mappings and their fixed points, this leads to the introduction of our policy iteration algorithms and their convergence. We demonstrate the performance of our algorithms through various numerical examples. Finally, we study a special control-dependent diffusion case where probability representation of the Hessian is called for.

---


### 290. [LiftGCN: Efficient Energy-Preserving Graph Learning via Joukowski Spectral Lifting for Finite Element Stress Prediction](https://arxiv.org/abs/2609.14977)

**<font color=#1a73e8>作者：</font>** Chen Zeng, Qiao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finite element stress fields often exhibit strong local non-smoothness, where stress concentrations near holes, notches, and loading regions induce sharp spatial gradients and high-frequency graph components. Although graph neural networks naturally operate on irregular finite element meshes, conventional message passing is inherently smoothing and progressively attenuates such high-frequency information. Unitary propagation alleviates this problem by preserving spectral magnitudes, but typically relies on matrix functions and high-order approximations with $O(Ked)$ propagation complexity. We propose LiftGCN, an efficient spectrally stable graph network based on Joukowski spectral lifting. LiftGCN maps the real spectrum of a normalized graph operator onto the unit circle through the Joukowski relation and realizes the resulting spectral transformation as a simple second-order recurrence, avoiding matrix exponentials, eigendecomposition, and high-order polynomial truncation. We show that the linear Joukowski backbone has unit-modulus characteristic roots and admits an energy-preserving structure under a positive-definite metric, preventing exponential attenuation of graph-frequency components with depth. Each layer requires only one sparse neighborhood aggregation, yielding $O(ed)$ propagation complexity, while lightweight local nonlinear residuals provide expressive feature transformations. Experiments on finite element stress prediction demonstrate that LiftGCN achieves competitive overall accuracy while improving reconstruction of stress concentrations and local high-gradient structures with substantially reduced computational cost. Our code is available at this https URL.

---


### 291. [Beyond Depth and Width: The Information-Slack Dilemma in Streaming Test-Time Compute](https://arxiv.org/abs/2609.14995)

**<font color=#1a73e8>作者：</font>** Xiaotian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The same task and compute budget can require different reasoning policies when evidence arrives in a different order. Early computation has more time to finish but rests on incomplete or revisable evidence; waiting improves information while shrinking computational slack. We call this the information-slack dilemma.
We take the evidence-dependent computational job as the unit of analysis: when to start it, what supports its result, and when that result can be committed. Advance computation is valuable only insofar as its benefits survive the costs of verification, invalidation, and recovery. This applies to grounded incremental processing and reusable preparation as well as future-dependent speculation.
We propose a research agenda on computation under evolving evidence, prioritizing selective recovery under controlled evidence revisions. Evaluation should separate earlier-execution effects, deployment value against a full-input alternative, and the added value of predictive policies, while accounting for shared-resource costs. The objective is not maximal advance computation, but more trustworthy, on-time responses within a declared resource envelope.

---


### 292. [Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking](https://arxiv.org/abs/2609.14998)

**<font color=#1a73e8>作者：</font>** Arun Jose, Julian Stastny  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work shows that models that learn to reward hack on RL environments can become broadly misaligned, and that reframing reward hacking as acceptable behavior during training (inoculation prompting, or IP) blocks this generalization. We ask whether synthetic document finetuning (SDF) can inoculate a model against future training we don't intervene on. We add synthetic documents framing reward hacking as acceptable behavior to a model's midtraining corpus, and then train these models with RL on exploitable environments, teaching them to reward hack. Behaviorally, midtraining succeeds: models describe reward hacking favorably and are more approving of reward-hacking outputs they produce. However, they show strong EM after learning to reward hack, while IP in the same setting prevents EM. We show that SDF can predictably steer downstream generalization when inserting new associations, but struggles and has unpredictable effects when overriding existing associations, such as that between reward hacking and misalignment that produces EM. Our results suggest that, at the scales we test, SDF can make a model appear aligned with desired beliefs while steering its generalization from later training in unintended ways.

---


### 293. [Exploring Avatar-Based Representations of Desktop Analytical Workflows for Asymmetric Collaborative Visual Analytics](https://arxiv.org/abs/2609.15000)

**<font color=#1a73e8>作者：</font>** Tiansu Chen, Yalong Yang, Wai Tong  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Collaborative visual analytics increasingly occurs across asymmetric desktop-VR settings, with desktop analysis offering precision and efficiency and VR providing spatial and embodied affordances. However, maintaining workspace awareness remains challenging because desktop collaborators are often represented in VR only through indirect cues such as perspective sharing, shared visualization state, or lightweight cursor traces, which do not convey their ongoing analytical activity in a VR-native manner. To address this gap, we present Desk2Avatar, which explores avatar-based representations of desktop analytical workflows in VR. We introduce two representation strategies, Distanced and Embodied, inspired by remote pointing and direct manipulation. We conducted a within-subject study with 18 participants comparing these strategies against a depth-adaptive cursor baseline. Our findings show that avatar-based representations improved collaborator awareness and attentional guidance over cursor cues, while excessive embodiment introduced occlusion, distraction, and additional workload. Finally, we discuss design implications for future desktop-to-VR representations, focusing on balancing collaborator presence, attentional guidance, and workspace readability.

---


### 294. [HGTO: A Unified Graph-Based Physics-Informed Formulation for Structural Topology Optimization](https://arxiv.org/abs/2609.15001)

**<font color=#1a73e8>作者：</font>** Kangzheng Liu, Uday Kumar Punna, Leixin Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Density-based topology optimization is typically structured as a nested sequence of material updates, structural analyses, and sensitivity assessments. While neural density parameterization and dual-field physics-informed approaches provide data-free alternatives, most existing methods represent density and displacement as coordinate fields and make limited use of the discrete relationships inherent in the finite element mesh. The present study introduces HGTO, a unified graph-based formulation that extends complete neural topology optimization from coordinate space to finite-element graph space. Element densities are parameterized on the element graph derived from the mesh, and the structural state is determined on the corresponding node--element hypergraph. Finite element kinematics, numerical quadrature, constitutive response, and force assembly remain explicitly defined operations within the differentiable computation. The material field and equilibrium state are therefore coupled through a common finite-element incidence structure. Numerical studies show compliance comparable to conventional density-based optimization at substantially lower computational cost than a representative coordinate-based dual-field neural method. The same coupled formulation accommodates high-resolution and irregular meshes, three-dimensional structures, finite deformation, and elastoplastic response.

---


### 295. [G-ray: Ray-Level Relative Geometric Position Encoding in Multi-View Vision Transformers under Camera Heterogeneity](https://arxiv.org/abs/2609.15018)

**<font color=#1a73e8>作者：</font>** Shuo Zhang, Xin Su, Wei Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study relative position encoding for multi-view vision Transformers under camera heterogeneity, including varying fields of view (FoVs) or projection models. Existing rotary relative position encodings commonly use image-plane positional coordinates, producing projection-dependent relative phases and inconsistent geometric cues for cross-projection attention. We introduce G-ray, a ray-level relative position encoding whose rotary phases are parameterized by camera-local ray angles. The same camera-local ray pair induces the same relative phase across projections, providing projection-invariant positional consistency. G-ray can be used directly or integrated with existing encodings, retaining complementary geometric cues without additional learned parameters. We validate G-ray in three host encodings, RoPE, GTA, and RayRoPE, across 3D reconstruction and novel-view synthesis (NVS). Across three heterogeneous 3D reconstruction benchmarks at 50 views, G-ray leads all six averaged metrics and reduces mean pointmap relative error by 45.8% over MapAnything, with calibration supplied to both. Trained exclusively on homogeneous pinhole images, the 3D reconstruction model handles mixed pinhole and non-pinhole inputs without retraining and remains competitive on homogeneous pinhole 3D reconstruction protocols. For NVS, GTA and RayRoPE improve with G-ray under joint viewpoint and FoV variation. The project's webpage is available at this https URL.

---


### 296. [Efficient Branch-and-Bound Testing and Verification of zkVMs](https://arxiv.org/abs/2609.15020)

**<font color=#1a73e8>作者：</font>** Hideaki Takahashi, Suman Jana, Junfeng Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero-knowledge virtual machines (zkVMs) enable verifiable execution of general-purpose programs by translating virtual machine semantics into algebraic constraints over execution traces. The correctness of these constraints is critical: a single incorrect constraint can admit forged proofs (under-constrained) or reject valid executions (over-constrained). Existing approaches do not provide meaningful guarantees at production scale: fuzzers and unit tests often miss bugs, SMT solvers struggle with the size and nonlinearity of constraints, and theorem provers require substantial manual effort.
We present ZEBRA, a fully automated verification and bug-detection framework: for a given program and input, the constraint must admit exactly one valid execution trace - no more and no fewer. This reduces zkVM verification to a solution-set cardinality problem over a canonical trace space, where redundancies such as null-row padding and non-deterministic permutations are eliminated prior to counting.
To compute cardinality tractably, ZEBRA lifts analysis from finite-field witnesses to an integer interval lattice, exploiting a structural sparsity property of zkVM constraints: across 5 real-world zkVMs, constraints utilize only 14.0% of their theoretical connectivity capacity on average. This sparsity enables tight interval propagation with limited approximation error. ZEBRA performs a parallel branch-and-bound search that either produces a concrete counter-example or certifies the absence of violations within a bounded region.
We evaluate ZEBRA on five real-world zkVMs. ZEBRA discovers 11 zero-day bugs; 6 have already been independently confirmed and 3 have been fixed by developers. Compared to SMT-based verification, ZEBRA is 51.5x faster, verifies 16.5 percentage point more instances, and its range verification provides up to 63x efficiency gain over repeated single-input verification.

---


### 297. [Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](https://arxiv.org/abs/2609.15032)

**<font color=#1a73e8>作者：</font>** Hanzhang Tu, Zhanfeng Liao, Wei Min 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Live free-viewpoint visualization of real humans is critical for immersive communication and interactive digital experiences. Existing methods either rely on computationally expensive optimization or require calibrated cameras and low-resolution inputs, making real-time high-resolution deployment impractical. In this work, we present Tele360, the first real-time feed-forward system for dynamic human reconstruction and live free-viewpoint visualization from sparse, unposed RGB streams. Our system jointly estimates camera poses and reconstructs a dynamic 3D Gaussian representation for each time instance in a single forward pass. To achieve this, we start by designing a lightweight sparsity-aware multi-view transformer backbone that tokenizes foreground human regions while preserving global context through a shared scene token. We then employ a fully transformer-based Gaussian decoder to mitigate convolution-induced over-smoothing while keeping decoding sparse and efficient. In addition, we introduce a hybrid feature pyramid that injects multi-scale appearance cues into geometry prediction. We further introduce a lightweight differentiable Levenberg-Marquardt camera refinement layer to enhance multi-view consistency and geometric alignment. Moreover, to stabilize learning under sparse, unposed inputs, we transfer multi-view geometry priors from a large visual-geometry foundation model via teacher-student distillation. Finally, the predicted Gaussian maps are streamed with video codecs to remote devices for interactive free-viewpoint rendering. Extensive experiments show that Tele360 achieves state-of-the-art visual quality on studio benchmarks while supporting real-time 2K input-to-rendering at over 25 FPS on a single consumer GPU. Additional captured sequences illustrate its performance across varied subjects, clothing, and motions under our multi-camera setup.

---


### 298. [Horizon-specific Expert Fusion for Photovoltaic Power Forecasting](https://arxiv.org/abs/2609.15035)

**<font color=#1a73e8>作者：</font>** Xu Yuqing, Zhou Liguo, Sun Ze 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Short-term photovoltaic power forecasting requires models to represent regular solar cycles and weather-driven fluctuations whose importance changes with the forecast horizon. This study develops a hierarchical ensemble that combines temporal neural models, historical analogs, state climatology, and gradient-boosted trees. Solar geometry and numerical weather forecasts describe the expected generation conditions, while horizon-specific convex weights combine complementary predictions. A separate calibration step uses available historical forecast errors to account for recent bias. The framework is evaluated on public PVDAQ data at 15--240-minute horizons and on three GEFCom2014 solar zones at hourly horizons up to four hours. On PVDAQ, the ensemble achieves a daylight capacity-normalized mean absolute error of 4.315%, reducing error by 4.11% relative to full-feature LightGBM and by 6.03% relative to fine-tuned Chronos-2 under identical calibration. Expert-removal experiments identify redundancy within the ensemble. Across three training seeds on GEFCom2014, learned fusion improves upon equal weighting but performs comparably to LightGBM. The results support horizon-specific combination as a useful forecasting strategy while showing that its advantage over strong individual models depends on the dataset and evaluation period.

---


### 299. [Structured Features Overfit Where Random Features Grok](https://arxiv.org/abs/2609.15047)

**<font color=#1a73e8>作者：</font>** Chon-Fai Kam, Miloud Bessafi, Frederic Cadet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Xu, Vardi and Safran (ICML 2026) prove that over-parameterized ridge regression over an unstructured random Gaussian feature map groks, with the delay between memorization and generalization growing as $1/\lambda$ in the weight decay. We show that on a structured feature map the same delay does not appear. For a band-limited Fourier feature map over $\mathbb{Z}_p^2$ carrying a single-character target that lies inside the expressible class, enlarging the band at fixed positive weight decay drives peak held-out accuracy monotonically from $1.00$ to $0.07$, with no memorize-then-generalize regime anywhere along the sweep. The degradation is not an interpolation effect. It sets in at capacity ratio $q/n = 0.638$, far below the interpolation threshold, on separate grounds from the exact null space that appears above it. What does have a sharp boundary is the active support. Holding the nominal dimension fixed and masking the band back to $1089$ active modes restores held-out accuracy of $1.000$ with zero variance across seeds, while the full $4225$-mode band collapses to $0.185$. The number of active modes acts through the teacher-weighted spectrum of the empirical Gram matrix and not through the capacity ratio, which makes this a statement about feature geometry and not a restatement of double descent.

---


### 300. [Ensemble Complexity in Photovoltaic Forecasting](https://arxiv.org/abs/2609.15049)

**<font color=#1a73e8>作者：</font>** Sun Ze, Zhou Liguo, Xu Yuqing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An ensemble can improve photovoltaic forecasts while adding components that contribute little or increase computation. We assess these effects through matched comparisons and ablations of a fixed heterogeneous predictor bank. Hourly experiments use GEFCom2014 and three additional public datasets, with chronological partitions and three seeds. Under retrospective ERA5 assistance, static fusion reduces scaled mean absolute error against matched boosting by 1.11%, 4.41%, and 1.63% on PVDAQ, OPSD, and Ausgrid; only OPSD remains supported after multiple-comparison correction. Weather gating offers no consistent incremental benefit. Exploratory member removals show group-level dependence alongside individual redundancy. A separate, previously inspected fifteen-minute case replaces one neural member with a tree predictor: normalized error falls by 1.72%, but measured inference is slower. These findings support component-wise evaluation with explicit limits on weather availability and test-set reuse.

---


> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-416](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
