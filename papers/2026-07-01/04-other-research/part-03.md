# 📦 其他研究 | 2026年07月01日

> 本类共 **489** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

---

### 101. [MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes](https://arxiv.org/abs/2606.28900)

**<font color=#1a73e8>作者：</font>** Hui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Doctor agents are moving beyond single-turn answer generation toward evolving clinical decision systems. Within an outpatient episode, they acquire evidence, use examination and consultation resources, and decide when to finalize a diagnosis and management plan. Across episodes, their behavior may change through memory, retrieval, reflection, or other update mechanisms. Current evaluations only partially cover this setting. Fixed-input medical QA benchmarks score final answers from complete inputs, whereas many interactive benchmarks still focus on individual encounters or fixed runs, providing limited support for evaluating how episode-level decisions interact with cross-episode experience. We introduce MedEvoEval, an executable longitudinal evaluation framework based on action-gated simulated outpatient episodes. Each source case is converted into role-specific patient, examination, and manager views; evidence is revealed only through valid actions; and each episode records a structured trace that links observations, actions, final outputs, manager scores, and optional experience write-back. We release a runnable E&D artifact with 700 processed episodes, provenance notes, schemas, an episode runner, scoring scripts, configurations, example logs, analysis code, and trajectory- and step-level derivatives. Experiments show that episode traces expose process costs hidden by final-answer scoring, show how MDT-style consultation reallocates resources, and support longitudinal analyses of memory maturation, held-out transfer, update-stage response, and backward retention. Together, these results show that MedEvoEval provides a concrete basis for evaluating whether doctor agents improve through experience, transfer useful behavior, and retain earlier capabilities over time.

---


### 102. [Projection-based coupling of infrared thermography and stereocorrelation-based digital image correlation](https://arxiv.org/abs/2606.28905)

**<font color=#1a73e8>作者：</font>** Jendrik-Alexander Tröger, Lutz Müller-Lohse, Stefan Hartmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full-field measurement techniques such as digital image correlation and infrared thermography are prevalent in experimental solid mechanics. Digital image correlation is used to analyze surface deformation, while infrared thermography quantifies surface temperature fields. However, sophisticated procedures are necessary to express both datasets in the same Lagrangian frame, especially when analyzing non-flat surfaces. In this study, we propose an external projection-based coupling that uses the pinhole camera model to relate two-dimensional temperature data measured by infrared thermography to three-dimensional point coordinates from stereocorrelation-based digital image correlation. Unlike existing multiview approaches, we utilize two independently calibrated industrial-grade systems and augment the experimental evaluation with the pinhole camera model. The projection matrix of the camera model is calibrated using a single image of a reference object. Through this projection, temperature fields are accurately represented at material points. Our method is particularly suited for, but not restricted to, curved surfaces and straightforward to embed in existing experimental protocols, as the image registration is kept as is. Additionally, we propose using radial basis functions as a global interpolation ansatz in both space and time to compute in-plane temperature gradients and even temperature rates on curved surfaces, thereby providing an extensive and information-rich full-field dataset.

---


### 103. [MALOQ: Massively Accelerated Learning of Operators for Quantum Transport](https://arxiv.org/abs/2606.28911)

**<font color=#1a73e8>作者：</font>** Manasa Kaniselvan, Alexander Maeder, Denghui Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learned (ML) operator models can be trained to predict density functional theory (DFT) Hamiltonian/density matrices at significantly reduced computational cost, thus extending electronic-structure calculations to previously unfeasible scales. Here, we introduce MALOQ (Massively Accelerated Learning of Operators for Quantum Transport), an application built to train on and predict electronic-structure matrices for systems made of few to 100k atoms, described by large basis sets, and covering a wide range of atomic elements. Based on a state-of-the-art, SO(2)-equivariant backbone architecture, MALOQ provides (i) custom data-processing kernels to handle high-rank Hamiltonian matrix data and (ii) a scalable edge-wise distribution of atomic graph(s). Trained on the largest molecular Hamiltonian datasets available today, it reduces time-per-epoch by over 30% compared to a molecule-wise-distributed framework, and enables inference on material graphs of arbitrary size. We demonstrate scalable training and inference for 3,000-12,000 atoms on the Alps supercomputer, up to 192 GPUs and 256 GPUs, respectively.

---


### 104. [What Color is the Sky (for a non-human) ?](https://arxiv.org/abs/2606.28912)

**<font color=#1a73e8>作者：</font>** Yair Weiss, Ofer Springer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The light of the daytime sky contains a mixture of many colors yet is perceived as blue by human observers. This is largely due to the particular response functions of the human cones. Under these response functions skylight and blue light are metamers: they yield the exact same excitation of the cones. In this paper we ask: is it possible to define the ``color'' of the sky for other visual systems? We present a simple computational method to determine monochromatic metamers to a given input light for arbitrary visual systems. Using published values on spectral sensitivity functions of various species, we use our method to determine the dominant wavelength of monochromatic metamers to skylight. For a wide range of species (bichromats, trichromats and tetrachormats) we find monochromatic metamers to skylight but the dominant wavelength of the metamer can vary drastically between species and be very different from the color perceived by humans.

---


### 105. [Latent Bridges for Multi-Table Question Answering](https://arxiv.org/abs/2606.28916)

**<font color=#1a73e8>作者：</font>** Simone Varriale, Tamara Cucumides, Floris Geerts 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce GRAB, a constructor-encoder-bridge pipeline for table question answering. Our method lifts relational data into an heterogeneous graph, encodes it via message passing, and transfers the signals to an LLM through a small set of query-conditioned latent tokens. This provides the LLM with a compact, task-relevant structural representation together with the flattened text. Crucially, the LLM remains strictly frozen to preserve its general reasoning capabilities; we train only the lightweight graph encoder and latent bridge (91M parameters), allowing the entire pipeline to be trained efficiently. Our pipeline significantly improves performance on relational Question Answering, with the largest gains in demanding multi-table settings, offering an efficient, principled way to connect relational deep learning with LLMs.

---


### 106. [ML-Powered LDAP Reconnaissance Detection using Weak Supervision](https://arxiv.org/abs/2606.28917)

**<font color=#1a73e8>作者：</font>** Shaefer Drew, Edward Raff, Michael Brautbar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lightweight Directory Access Protocol (LDAP) is a protocol that allows users to query and modify Active Directory (AD) data. By default, all users have read access to all AD data through LDAP, making it a common initial tool for reconnaissance when a threat actor first compromises an identity. To capture threat actors early in the reconnaissance phase, we developed two machine learning frameworks to detect LDAP reconnaissance: an ML classifier to predict malicious LDAP queries and an ML-based data-mining method to extract malicious query signatures. By correlating LDAP queries with endpoint detections, the first framework uses weak supervision to label a massive dataset and classify LDAP queries as malicious or benign. For immediate deployment, a second technique was developed on top of this approach to employ a rigorous statistical hypothesis-testing framework for mining novel, malicious LDAP signatures. While this weakly supervised approach is limited compared with manual human labeling, it is more practical for this use case because it leverages large-scale automated corpus construction, reducing costs and time. Ultimately, both the LDAP classifier and the ML-based LDAP signature mining method achieved performance benchmarks, with the classifier achieving up to a 65\% True Positive Rate (TPR) on the holdout set while limiting false positives, and mined signatures demonstrating 81.48\% field precision with CrowdStrike's Managed Detection and Response team.

---


### 107. [Towards Improved Anomaly Detection for Cloud Cybersecurity via Graph Neural Networks](https://arxiv.org/abs/2606.28923)

**<font color=#1a73e8>作者：</font>** Manu Nandan, TJ Jaymes, Michael Brautbar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting security threats in an organization's cloud computing environment has become necessary due to the increased reliance on cloud infrastructure. Logging of all cloud computing events enables investigation into any incidents after they are detected. Automated detection of threats using the logs based on heuristics or anomaly detection could result in a high false positive rate due to its relatively static nature. In this article, we present an industrial case study of a self-supervised learning method using graph neural networks applied to AWS CloudTrail logs to surface suspicious events for analyst review. The model produces an anomaly score for each event and dynamically adapts to changes in the organization without requiring periodic retraining. Based on our experiments across five organizations, the proposed model produced substantially fewer alerts than a domain expert rule-based baseline in almost all cases, reducing alert volumes to approximately 1 per hour from thousands generated by traditional methods. We note that this evaluation covers only flagged events, and false negatives cannot be estimated from the current data; findings should therefore be interpreted as a practical deployment study offering insights into real-world constraints rather than a fully validated detection system. We discuss these limitations and the requirements for extending the approach to other cloud environments as future work.

---


### 108. [Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation](https://arxiv.org/abs/2606.28925)

**<font color=#1a73e8>作者：</font>** Ananto Nayan Bala, Faisal Muhammad Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool and agent routing from natural-language prompts is naturally a set-valued prediction problem: a single query may require multiple agents, while over-selection increases execution cost. The benchmark introduced here is derived from WildChat and contains 3,000 prompts over a fixed 12-agent catalog, with AI-assisted heuristic labels under a fixed schema and controlled rebalancing for multi-label evaluation. The evaluation protocol combines set-level metrics (Precision, Recall, F1, Jaccard, and Exact Match), latency, an execution-oriented capability-coverage simulation, and a constrained weighted-routing setting based on ordinal agent-cost tiers. Compared methods include nearest-neighbor matching, linear multilabel classification, dependency-aware baselines, a fine-tuned encoder, deterministic weighted post-scoring via Weighted Agent Routing (WAR), and a zero-shot LLM baseline. Results show that supervised routers substantially outperform nearest-neighbor and zero-shot LLM routing. The fine-tuned encoder achieves the strongest unconstrained set accuracy, while the linear multilabel model provides the strongest practical baseline. In the constrained setting, the weighted routing layer improves utility when applied on top of strong supervised scorers, with the largest gain observed for Encoder+WAR. Overall, the benchmark and evaluation protocol support reproducible study of accuracy-cost trade-offs in fixed-catalog multi-agent routing.

---


### 109. [Cybersecurity is the True Frontier for Generative AI Success or Failure](https://arxiv.org/abs/2606.28929)

**<font color=#1a73e8>作者：</font>** Edward Raff, Maor Ashkenazi, Sagar Samtani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity is a real-life test-bed for many machine learning problems at once, especially when considering modern strides in using Large Language Models (LLMs) to automate processes as ``agents.'' Cybersecurity workflows require orchestrating hundreds of standard and bespoke tools through various formats. The scale of cybersecurity data is enormous; for example, a single malware sample can be viewed as a sequence of billions of tokens. The cost of labeling any file by experts is enormous and labor-intensive, in part because an adversary (possibly a well-funded nation state actor) is attempting to subvert your detection methods. Even skilled experts may disagree on the correct label, creating ambiguity in what constitutes ground truth. When deployed, models must run quickly on billions of items a day, where low-latency is critical for operational success, in a continuously changing environment. In addition, explainability is not optional: analysts demand clear reasoning for model decisions to cope with the large number of false-positive alerts they face daily, and to quickly develop remediation and understand how something went wrong. In short, the amount of complexity cybersecurity is greater than that of natural language and computer vision, and thus we posit that cybersecurity is the better test-case for general AI progress than other, well-studied fields.

---


### 110. [FinInvest-GTCN: Explainable Graph-Temporal-Causal Modeling for Risk-Aware Investment Decision Optimization](https://arxiv.org/abs/2606.28933)

**<font color=#1a73e8>作者：</font>** Junyan Tan, Yifan Li, Minghao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Venture capital (VC) investment decisions face distinct challenges, such as multi-source heterogeneous data, non-stationary time series, and the demand for explainable predictions in high-stakes, low-data settings. To overcome these issues, we introduce \textbf{FinInvest-GTCN}, a Graph-Temporal-Causal Network that redefines the task from content recommendation to quantitative risk-return assessment. This architecture combines a relational graph encoder to capture the investment ecosystem's topology, a multi-scale temporal fusion module to handle long-term dependencies and non-stationarity, and a causal decision head that generates risk-adjusted predictions with interpretable causal attributions. A core innovation is the Meta-Causal Adaptation (MCA) strategy, which facilitates robust fine-tuning for new, data-scarce sectors by aligning updates with causally-plausible structures derived from meta-pretraining. Comprehensive experiments on proprietary VC datasets show that FinInvest-GTCN delivers state-of-the-art results, markedly lowering the primary Risk-Adjusted Mean Squared Error (RA-MSE) to 2.51 from a baseline of 3.05 and boosting the cumulative return of a simulated portfolio by 18.7\%. Ablation studies underscore the essential role of each component, while additional analyses confirm the model's stability, interpretability, and enhanced adaptability. This work pioneers a data-driven, explainable framework for investment decision support.

---


### 111. [ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies](https://arxiv.org/abs/2606.28939)

**<font color=#1a73e8>作者：</font>** Tzu-Hsiang Lin, Srinivas Shakkottai, Dileep Kalathil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavior-cloned diffusion policies are expressive but remain vulnerable to covariate shift: small deviations from demonstrated states can compound into task failure. Existing methods address this either by expanding the training distribution through expert corrections or synthetic augmentation, or by steering a frozen policy at test time with guidance from a learned model. The former can be expensive or assumption-dependent, while the latter discards the corrected trajectories after execution. We introduce ReGuide, a self-improving framework that treats guided rollouts as reusable on-policy recovery data. ReGuide first uses Phase-Conditioned Guidance (PCG) to generate corrective rollouts: it constructs phase-specific latent targets, applies guidance only in the drifted-but-recoverable regime, and guides through the estimated clean action to match the dynamics model's training distribution. Successful guided rollouts are then absorbed back into the policy through ReGuide-FT, which fine-tunes the current checkpoint, or ReGuide-FS, which retrains from scratch on the augmented dataset; the two can also be composed and iterated. On Robomimic Can, Square, Transport, and Tool Hang, ReGuide improves base-policy success by $1.3$--$7.7\times$, outperforms LPB in the test-time-only setting, and matched-data ablations show that the gains come from guided recovery data rather than additional rollouts alone.

---


### 112. [A3M: Adaptive, Adversarial and Multi-Objective Learning for Strategic Bidding in Repeated Auctions](https://arxiv.org/abs/2606.28943)

**<font color=#1a73e8>作者：</font>** Junhan Li, Yuxin Zhang, Haoran Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learning to bid in repeated multi-unit auctions with bandit feedback poses a fundamental challenge. Existing methods often rely on rigid explore-then-exploit schedules, assume stationary adversaries, and optimize solely for bidder utility, thereby limiting adaptability and strategic robustness. To address these limitations, we introduce the A3M framework, which integrates adaptive deep reinforcement learning (DRL), explicit adversarial reasoning, and principled multi-objective reward design for online auction strategy optimization. A3M employs an actor-critic DRL backbone to dynamically balance exploration and exploitation, an opponent model for fictitious play against non-stationary adversaries, and a composite reward function to jointly maximize utility, auctioneer revenue, and fairness. We provide the first comprehensive empirical evaluation of this integrated approach against established baselines in both discriminatory and uniform price auctions. Results show that A3M reduces final regret by 30--40\% in standard settings, maintains robust performance against adversarial strategy shifts, scales favorably with the number of units $K$, and enables tunable multi-objective trade-offs. An extensive ablation study confirms the necessity of each core component. Our work establishes A3M as a powerful and flexible framework for learning in complex auction environments.

---


### 113. [Character Recognition of Nepali Number Plate](https://arxiv.org/abs/2606.28946)

**<font color=#1a73e8>作者：</font>** Satyasa Khadka, Sandhya Baral, Sudip Tiwari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a robust Automatic Number Plate Recognition (ANPR) system tailored for Nepali license plates written in Devanagari script. In this paper, a pipelined model was used that integrates YOLO-based models for license plate and character detection, followed by a CNN classifier trained on 34 Devanagari characters. Two publicly available data sets were used that incorporate diverse lighting, fonts, and structural variations. Data augmentation and additional training on embossed plates enhanced the generalizability of the model. The system achieved a recognition accuracy of up to 93\%, demonstrating strong performance under real-world conditions and providing a scalable solution for traffic management in Nepal. Code: this https URL

---


### 114. [Machine-learnable Sets](https://arxiv.org/abs/2606.28947)

**<font color=#1a73e8>作者：</font>** Veit Elser, Manish Krishan Lal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this study we present a formal definition of large discrete sets having, informally, three properties: their elements are easily recognized, easily generated, and the latter tasks are easily learned from examples. The formalism is specialized to sets of binary strings and a definition of "machine-learnability" based on the existence of a bounded-complexity Boolean autoencoder that fixes the elements of the set. We present experiments where the autoencoders are implemented by nets of Boolean threshold functions. Machine-learnability is demonstrated for Rorschach patterns (that may have reversed contrast in the mirrored half), and considerably "wilder" sets whose elements are only approximately fixed by admissible autoencoders. In the second case we demonstrate a simple iteration that evolves wild sets to make them properly machine-learnable.

---


### 115. [Modification-Considering Value Learning for Reward Hacking Mitigation in RL](https://arxiv.org/abs/2606.28955)

**<font color=#1a73e8>作者：</font>** Evgenii Opryshko, Umangi Jain, Igor Gilitschenski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning agents can exploit misspecified reward signals to achieve high apparent returns while failing on the intended objective, a failure mode known as reward hacking. Existing practical defenses typically constrain policy updates to stay near a known safe reference, creating a tension between suppressing hacking and permitting legitimate improvement. We propose Modification-Considering Value Learning (MCVL), which operationalizes the theoretical idea of current utility optimization for standard value-based RL. MCVL wraps an off-policy learner and treats each incoming transition as a candidate modification: it forecasts two training paths, one that includes the transition and one that does not, and scores both with a frozen bootstrapped-return estimator derived from a learned reward model and value function. The transition is admitted only if inclusion does not decrease the score. We formalize conditions under which this filtering is both safe and permissive, and instantiate MCVL with DDQN and TD3. Across four safety-relevant gridworlds and three modified MuJoCo continuous-control tasks with diverse hacking mechanisms, MCVL mitigates reward hacking while continuing to improve the intended objective. Project website: this http URL.

---


### 116. [Beyond Her: Safety Dynamics in Role-play AI Companions](https://arxiv.org/abs/2606.28968)

**<font color=#1a73e8>作者：</font>** Zehang Deng, Zhaoyang Xie, Changzhou Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The film 'Her' pictured a future of love between humans and AI. That future has quietly emerged in the form of Role-play AI Companions (RACs), where emotionally responsive interactions blur the boundary between tool use and relational engagement. However, the safety implications remain poorly understood, as user experiences evolve over time through safety dynamics, spanning both emotional and risk behavioral dynamics, that can gradually shift interactions toward risk. In this paper, we investigate safety dynamics in RAC usage through a two-part mixed-methods study (Study I \& II). (1) Study I consists of semi-structured interviews (N = 16) to identify the key factors shaping these dynamics. We find that users' internalizing problems, the role personality adopted by the RAC, and risk interaction patterns jointly shape safety dynamics. Building on these insights, (2) Study II conducts a 14-day Ecological Momentary Assessment (N = 102) to examine how safety dynamics unfold in real-world usage. We identify distinct user profiles based on internalizing problems and show that interactions with RACs can produce short-term emotional relief while masking longer-term deterioration. Furthermore, vulnerable users exhibit more unstable risk behavioral patterns over time, making risk emergence less predictable and harder to mitigate with static safeguards. Our findings highlight the importance of modeling safety as a dynamic process rather than a static property. We conclude with three-layer design implications for next-generation AI companions, advocating for adaptive safeguards that can respond to evolving emotional and behavioral signals.

---


### 117. [RGLD: Randomized Global-Local Density Estimation for Tabular Anomaly Detection](https://arxiv.org/abs/2606.28970)

**<font color=#1a73e8>作者：</font>** Quanling Zhao, Jiaying Yang, Ye Tian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised tabular anomaly detection requires methods that are accurate, robust across heterogeneous datasets, and computationally efficient. Classical statistical detectors are often efficient, but they usually rely on a fixed data view and a single notion of abnormality. Deep anomaly detectors can learn more flexible scoring functions, but they are substantially slower and difficult to tune in unsupervised settings due to the lack of a reliable supervisory signal. We propose RGLD, a randomized global-local density estimator for efficient unsupervised tabular anomaly detection. RGLD combines a global random-feature density branch, which identifies samples in broadly low-density regions, with a local neighbor branch, which detects samples that are weakly supported by nearby observations. Both branches operate over feature-bagged randomized views, allowing RGLD to expose anomaly evidence that may be hidden in any single representation. We conduct experiments on 47 tabular datasets against 23 statistical and deep anomaly detection baselines under fully unsupervised setting. RGLD achieves the strongest dataset-level AUROC performance, ranking 1st in dataset wins, and ranks 2nd in AUPRC wins. RGLD is also faster than all evaluated deep detectors, achieving 50x-580x speedups, and remains competitive with statistical methods in runtime, yielding a favorable accuracy-efficiency tradeoff.

---


### 118. [Evidence-Based Text-Conditioned 3D CT Synthesis for Ovarian Cancer](https://arxiv.org/abs/2606.28980)

**<font color=#1a73e8>作者：</font>** Francesca Pia Panaccione, Eugenio Lomurno, Francesca Fati 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ovarian cancer is frequently diagnosed at an advanced stage, making preoperative contrast-enhanced computed tomography (CT) central to staging and surgical planning; yet the scarcity of annotated imaging data, compounded by privacy regulations, limits the development of generalizable computational models in this domain. Text-conditioned 3D CT synthesis has shown promise, but existing pipelines depend on paired radiology reports and have been evaluated only on chest CT. We propose OvESyn (Ovarian Evidence-based Synthesis), a framework that constructs standardized Findings and Impression sections directly from CT-derived imaging descriptors and routine clinical metadata, without any original radiology report, and uses them to condition a latent diffusion model adapted to 493 high-grade serous ovarian carcinoma patients. This is the first text-conditioned 3D CT synthesis framework adapted to an abdomino-pelvic oncologic setting. A systematic ablation over two adaptation axes, vision-language encoder alignment and generator fine-tuning, identifies generator domain adaptation as the operative mechanism for crossing the domain gap and establishing the target anatomy: without it, synthesis remains anchored to the thoracic pretraining domain, with Precision and Recall collapsing to zero and FID2.5D exceeding 140, regardless of encoder alignment. Encoder alignment instead refines intensity and fine detail. The full OvESyn attains the best distributional and intensity fidelity (FID2.5D 29.35, Precision 0.671, Wasserstein-1 0.044), while the generator-only variant maximizes coverage (Recall 0.645), reflecting a fidelity/coverage trade-off governed by encoder adaptation. Requiring only automatic segmentations and routine preoperative metadata, OvESyn supports transferability to report-scarce settings and provides a foundation for synthetic cohort generation in abdomino-pelvic oncologic imaging.

---


### 119. [Arbitrary Reduction of Validation Error for AI Decision Tests using Homomorphic AI and Repetition Codes](https://arxiv.org/abs/2606.28994)

**<font color=#1a73e8>作者：</font>** Eric Filiol, Jaagup Sepp  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents new results and breakthrough obtained with the HbHAI techniques (Hash-based Homomorphic Artificial Intelligence) proposed in \cite{filiol0,sepp}. HbHAI is based on a novel class of key-dependent hash functions that naturally preserve most similarity properties, most AI algorithms rely on. It enables to analyse and process data in its cryptographically secure form while using existing native AI algorithms without modification, with unprecedented performances compared to existing homomorphic encryption schemes and most notably compared to the same processing on corresponding plaintext data.
Two major results have been obtained further. First we enable to reduce the compression rate up to a factor of 10 thus allowing to process massive datasets while reducing the computation time and the energy footprint in the same order. Second, we show how it is possible to arbitrarily reduce the final validation error of AI-based decision tests by using repetition error-correcting codes.

---


### 120. [On Surrogate Modeling of Static Response of AM Short-Fiber Thermoplastics Using Graph Neural Networks](https://arxiv.org/abs/2606.28996)

**<font color=#1a73e8>作者：</font>** Pharindra Pathak, Vipin Kumar, Trenton M. Ricks 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short-fiber thermoplastic (SFT) composites are increasingly employed in lightweight aerospace and automotive structures owing to their favorable strength-to-weight ratio, high production rates, and recyclability. Unlike continuous-fiber systems, the mechanical response of SFTs is governed by mesoscale interactions among fiber orientation, spatial clustering, and manufacturing-induced porosity. These features exhibit significant spatial variability in manufactured components and influence stiffness, damage initiation, and nonlinear deformation. Although mesoscale finite element (FE) models can resolve such heterogeneity, their application to realistic three-dimensional microstructures remains computationally intractable.
A data-driven surrogate framework is proposed to predict the mechanical behavior of additively manufactured, compression-molded (AM-CM) SFTs. Microstructures reconstructed from micro-computed tomography data were discretized into Voronoi-based cells representing distinct fiber-interaction neighborhoods. Each cell was homogenized via nonlinear FE simulations incorporating matrix damage, and the resulting stress-strain responses trained a hybrid Graph Neural Network-Long Short-Term Memory (GNN-LSTM) architecture encoding microstructural topology and history-dependent mechanical evolution.
The surrogate accurately predicts stiffness and stress-strain behavior of unseen microstructures, achieving $R^2\approx 0.98$ relative to high-fidelity FE simulations with over two orders-of-magnitude reduction in computational cost. Coupling the framework with experimentally calibrated damage laws demonstrates that fiber orientation, clustering, and porosity collectively govern local effective stiffness. The approach provides a physics-informed, data-efficient pathway to identify mechanically weak microstructural cells and accelerate digital-twin development for SFT components.

---


### 121. [BERTomelo: Your Portuguese Encoder Best Friend](https://arxiv.org/abs/2606.28999)

**<font color=#1a73e8>作者：</font>** Rennê Ruan Alves Oliveira, Gustavo Cordeiro Galvão Van Erven, Luís Paulo Faina Garcia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Encoders have become the state of the art for multiple NLP tasks, especially those requiring deep contextual understanding. While multilingual models offer broad coverage, dedicated monolingual encoders are essential for capturing the unique lexical and syntactic nuances of specific languages. For Portuguese, however, existing monolingual options like BERTimbau and Albertina have not kept pace with recent architectural breakthroughs, often lagging behind English benchmarks in scalability and efficiency. This work introduces BERTomelo, a next-generation monolingual encoder pre-trained from scratch and specifically optimized for the Portuguese language. By leveraging the ModernBERT architecture, BERTomelo overcomes the limitations of previous models, offering Base and Large versions with a 1,024-token context window and hardware-level optimizations like FlashAttention and alternating attention mechanisms. The model was trained on ClassiCC-PT, a massive, high-quality Portuguese corpus of 106 million documents, ensuring superior alignment with the language's contemporary usage. The results demonstrate that BERTomelo not only outperforms previous Portuguese encoders but also provides a more robust and efficient alternative to massive multilingual models in downstream tasks such as STS and NER.

---


### 122. [SciFlow: Semantic Cross Interference for Self-Supervised Optical Flow Domain Generalization](https://arxiv.org/abs/2606.29004)

**<font color=#1a73e8>作者：</font>** Jamie Menjay Lin, Jisoo Jeong, Hong Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motions of objects and scenes carry essential intelligence in video understanding, offering rich cues for interpreting dynamic settings and interactions. Due to the cost and scarcity of high-quality annotation or ground truth of pixel-wise optical flow, however, motion estimation models are typically trained in synthetic domains while deployed in real-world domains. Addressing synthetic-to-real domain generalization challenges has been crucial for developing practical solutions in diverse open-world use cases.
This paper introduces SciFlow, a simple yet effective, network-agnostic, training-based approach that leverages self-supervised learning to generalize motion estimation across synthetic and open-world domains. Specifically, SciFlow imposes semantic interference from open-world images onto synthetic images during training, blending indomain features with cross-domain interference, which enables the network to adapt to the real-world domains. Additionally, SciFlow utilizes geometric consistency to ensure validity of the self-supervision. Our experiment results show that SciFlow not only significantly enhances model robustness amidst domain variations, but also remarkably enables synthetic-to-real domain generalization without requiring any ground truth in the open world.

---


### 123. [Semantic-Aware, Physics-Informed, Geometry-Grounded Weather Video Synthesis](https://arxiv.org/abs/2606.29020)

**<font color=#1a73e8>作者：</font>** Chenghao Qian, Nedko Savov, Lingdong Kong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weather synthesis aims to add weather effects to input videos while preserving scene identity, structure, and motion. The key limitation of existing methods is the lack of diversity in weather appearance and effective control over weather dynamics (e.g., temporal evolution and particle motion). Most approaches rely on text prompts, which are inherently underspecified and often fail to produce detailed weather characteristics. Additionally, general-purpose video editors optimized for clean and aesthetic outputs tend to suppress heavy weather phenomena, making dense particle effects difficult to generate. To address these, we propose a Semantic-Aware, Physics-Informed, and Geometry-Grounded framework that steers an off-the-shelf video editor to synthesize diverse global appearances and detailed particle dynamics. We factorize the synthesis into three conditional signals, so that each provides a distinct and stable source of guidance: semantics specifies what the weather should look like, dynamics governs how it evolves over time, and geometry determines where it should appear in the scene. Specifically, we introduce (1) semantic-aware appearance anchoring to establish the target appearance from scene semantics and user input; (2) physics-informed dynamic simulation to generate particle effects by simulating a Gaussian-represented particle field under gravity, wind, and turbulence; and (3) geometry-grounded video synthesis to align the simulated particles with target scene geometry and synthesize the final video. Experiments demonstrate that our method produces diverse, physically and visually realistic weather effects. Furthermore, we show that our synthesized data significantly improves the robustness of autonomous driving semantic segmentation under adverse weather conditions. Project page: this https URL.

---


### 124. [Conversational Domain Adaptation of IndicTrans2 across 21 Indic Languages via Experience Replay and Model Soups](https://arxiv.org/abs/2606.29024)

**<font color=#1a73e8>作者：</font>** Aditya Pratap Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> IndicTrans2 is the strongest open English to Indic translation system, but like most systems it is trained on general text and tends to sound stiff on casual, conversational input. We adapt IndicTrans2-1B to conversational register across all 21 Indic languages using only public data (OpenSubtitles, BPCC-H-Daily, Tatoeba). Plain fine-tuning improves conversational chrF but forgets the general domain (it drops 3.9 chrF on FLORES for Hindi). Mixing general data back into training (experience replay) and then averaging the fine-tuned weights with the base (model souping) removes that trade-off: the resulting model beats IndicTrans2-1B on conversational chrF in every one of the 21 languages (mean +6.2) while matching it on FLORES (mean change -0.17, all within 0.7 chrF). Paired bootstrap tests confirm the conversational gains are significant (p <= 0.004) and that FLORES is not significantly degraded. We are deliberate about scope: these are chrF gains, and a blind human plus multi-model LLM check does not confirm them as a perceived quality improvement, so we treat the conversational gain as largely a register match to the references rather than proof of better translation. The techniques are not new; the contribution is the honest, end-to-end study in the Indic conversational setting.

---


### 125. [Preventing Error Propagation in Multi-Agent AI through Runtime Monitoring](https://arxiv.org/abs/2606.29026)

**<font color=#1a73e8>作者：</font>** Shahnewaz Karim Sakib, Anindya Bijoy Das  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent AI systems can improve answer selection by allowing different language models to exchange reasoning traces, revise initial predictions, and support a final decision. However, such communication may also introduce reliability risks: reasoning from one agent can correct another agent's mistake, but it can also mislead an agent that was initially correct. This paper studies reliable multi-agent AI communication through reasoning exchange and runtime answer revision. We develop a framework in which agents first answer multiple-choice questions independently, then share reasoning traces and revise their decisions. We conduct numerical experiments where we evaluate whether this process improves accuracy, produces more positive than negative answer transitions, and remains effective across domains such as cybersecurity, networking, and general knowledge. The results help identify when multi-agent reasoning improves reliability and when it may propagate errors.

---


### 126. [Adaptive Spectrum-Aware Feature Disentangled Network for Small Object Detection](https://arxiv.org/abs/2606.29029)

**<font color=#1a73e8>作者：</font>** Yang Guo, Zihan Yang, Feifei Kou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small Object Detection (SOD) is a fundamental yet challenging problem in computer vision due to its limited spatial resolution and weak visual cues. Although recent approaches have achieved remarkable advances, the background distractors in different frequency spectra still degrade the performance. In this paper, we propose a novel small object detection framework termed SFDNet, which is capable of detecting small objects via efficient spectrum-aware feature disentanglement. Specifically, we propose an Adaptive Spectrum Disentanglement (ASD) module that decomposes backbone features into multiple complementary spectral components, aiming to construct discriminative object-relevant representations by discarding the background distractors for each component. Afterwards, to strengthen the semantic consistency of the similar objects in the same class, we propose a Class-Wise Prototype Distillation (CPD) procedure, which establishes class prototypes for the object instances and enforces the compact representation by efficient prototype distillation. Extensive experiments on multiple challenging benchmarks show that SFDNet outperforms existing state-of-the-art methods by a large margin. Our code is available at this https URL.

---


### 127. [Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy](https://arxiv.org/abs/2606.29038)

**<font color=#1a73e8>作者：</font>** Ruiyu Zhang, Lin Nie, Xin Zhao  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Metric aggregation divergence (MAD) is the silent inconsistency that arises when distinct pipeline stages in an agent-based model coupled with a multi-objective evolutionary algorithm (ABM+MOEA) independently re-implement how an outcome metric is extracted from simulation trajectories. Unlike deliberate analytical choices, MAD operates at the level of pipeline architecture: each stage is internally coherent, and the inconsistency becomes visible only when cross-stage outputs are compared. Code inspection of EpidemiOptim, a JAIR-published epidemic policy toolbox, reveals three structurally independent aggregation paths in peer-reviewed code. A faithful replication of this structure produces champion disagreement in 64.2% of independent runs (n=500, 95% CI: [59.9%, 68.3%]). In a 300-seed policy-flip experiment, divergent aggregation causes the optimizer to recommend the wrong champion in 83% of replications, with a mean welfare gap of 2.19 units and a Gini inequality gap of 0.050 units. In a follow-up inference audit, 3 of 249 flipped seeds cross the significance boundary itself. A complementary enterprise follow-up produces the predicted null under near-commensurable rankings (rho = 0.991), while a public upstream rerun of the Lake Problem DPS workflow shows that the archived published-path recommendation reaches joint-threshold success 0.401 whereas a shared contract-path rule reaches 0.552. We introduce the metric contract - a single shared callable enforced at dispatch time across all pipeline stages - as the remedy. Framed as standard engineering discipline applied to the cross-stage metric interface, the contract eliminates divergence by construction with approximately 3% runtime overhead.

---


### 128. [How Far Can Sharpness and Complexity Jointly Explain Generalization?](https://arxiv.org/abs/2606.29043)

**<font color=#1a73e8>作者：</font>** Ziyu Cheng, Xitong Zhang, Longxiu Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sharpness and complexity are two central factors in the generalization analysis of deep neural networks. Existing quantitative evaluations of generalization measures have largely focused on individual scalar measures, leaving the joint explanatory power of sharpness and complexity largely unexplored. This work studies how far sharpness and complexity can jointly explain generalization. We use linear regression and introduce a Pareto-based analysis to quantitatively evaluate the joint explanatory power of these two factors. Beyond the existing parameter-level definitions, we further propose realizations of sharpness and complexity that are closer to function space and less dependent on raw parameter representations. We find that function-oriented definitions of these two quantities expand the explanatory scope of the two-factor view beyond what is achieved by existing parameter-level metrics. Overall, our results support the sharpness-complexity perspective as an informative lens for understanding generalization across diverse settings. At the same time, the remaining failures indicate that whether this two-factor view can serve as a complete theory of generalization remains open.

---


### 129. [A Kernel Fisher Discriminant Analysis-Based Tree Ensemble Classifier: KFDA Forest](https://arxiv.org/abs/2606.29053)

**<font color=#1a73e8>作者：</font>** Donghwan Kim, Seung Hwan Park, Jun-Geol Baek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In general, an ensemble classifier is more accurate than a single classifier. In this study, we propose an ensemble classifier called the kernel Fisher discriminant analysis forest (KFDA Forest), which is a tree-based ensemble method that applies KFDA. To promote diversity, bootstrap is used, and variable sets are randomly divided into K subsets. KFDA is performed on each subset to increase classification accuracy. KFDA maximizes the distance between classes while minimizing the distance within classes. KFDA can also be applied to classification problems in a nonlinear data structure using the kernel trick because it can transform the input space into a kernel feature space, commonly named a rotation, rather than performing a dimensionality reduction. Because new feature axes and KFDA projections are parallel, decision trees are used as a base classifier. To compare the proposed method with existing ensemble methods, we apply these to real datasets from the UCI and KEEL repositories.

---


### 130. [Masked Diffusion Decoding as $x$-Prediction Flow](https://arxiv.org/abs/2606.29066)

**<font color=#1a73e8>作者：</font>** Weitian Wang, Lianlei Shan, Shubham Rai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDLMs) generate text by iteratively unmasking tokens, but their standard decoder reduces each step to a binary action: a position is either committed to a single token or left fully masked, with no representation of partial belief in between. This all-or-nothing regime discards rich predictive information and forces premature, irrevocable commitments, leading to poor performance under a limited decoding budget. In this paper, we reinterpret mask prediction as clean-state prediction ($x$-prediction) and show that it can be used to induce a continuous flow in input embedding space. Building on this view, we propose a continuous decoding framework for MDLMs where tokens can accumulate partial progress at each diffusion step and remain revisable. To match the uneven contextual constraints across positions in language, we replace the globally synchronous schedule in image diffusion with a confidence-based asynchronous update in which the diffusion progress is token-wise accumulated. Additionally, we introduce a lightweight policy network and formulate its training as a reinforcement learning problem. Applied to pretrained LLaDA, our continuous decoder reaches 97% of its performance on the HumanEval dataset with 25% of decoding budget.

---


### 131. [A Comparative Study on Affective Cues in Text Embeddings Across Psychological Emotion Theories](https://arxiv.org/abs/2606.29068)

**<font color=#1a73e8>作者：</font>** Fabio Ciani, Harald Schweiger, Emilia Parada-Cabaleiro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text encoders are known for their utility in natural language processing, as they are able to efficiently compress inputs into dense vectors while preserving semantics. These models have been applied to affective computing, in particular to help with solving sentiment analysis and emotion recognition tasks. Nevertheless, it remains unclear to what extent the latent representations produced by modern text encoders capture well-defined psychological theories of affect. In this work, we investigate the affective capabilities of twelve recently released text encoders by probing their generated embeddings as input features for solving regression and classification tasks across three established emotion frameworks, using both word- and sentence-level data. Additionally, we apply a semantic data-leakage prevention technique to improve robustness in word-level evaluations. Our main findings show that the latent manifolds of the latest instruction-aware open-weight encoders enclose an equal or even a larger amount of affective information in comparison with proprietary counterparts when evaluated at word level. In contrast, embeddings of task-tuned and proprietary encoders reach the highest scores on sentence-level affective classification. Furthermore, a qualitative analysis of latent representations and their encoded affective cues is provided.

---


### 132. [From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes](https://arxiv.org/abs/2606.29073)

**<font color=#1a73e8>作者：</font>** Ting Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model Context Protocol (MCP)-style ecosystems give language-model applications a practical connection layer for tools, resources, prompts, and transports. As agents move from connection to execution, security decisions often remain split across clients, servers, prompts, approval dialogs, OAuth deployments, and logs. This paper asks whether a runtime can make execution-layer invariants explicit and testable while preserving MCP-like workflows. We define eight invariants: metadata non-authority, grant-backed approval, canonical resources, principal binding, scoped capability invocation, source-and-target data-flow authorization, deny-path audit, and explicit protocol state. We implement these invariants in HCP, a Handle-Capability Protocol reference runtime for MCP-style agent execution that represents calls through principals, resources, grants, capabilities, handles, policy decisions, data-pipe checks, and audit entries. We evaluate HCP against two MCP-like baselines: a naive connection-layer runtime and a practice-informed connection-layer mitigation baseline with metadata linting, session checks, and per-call approvals. Across 10 benchmark cases, the naive baseline permits all modeled attacks, the mitigation baseline permits 6 of 10, and HCP blocks all 10 while preserving audit evidence. Ablations identify which runtime components block attacks and preserve forensic evidence. A local in-memory microbenchmark reports sub-millisecond mean latencies for measured policy, invocation, peek, and pipe operations. A bounded GitHub README-screening sample provides ecosystem signals, not vulnerability findings. The results support a narrow claim: MCP-style agent systems need an execution-control layer in addition to connection-layer conventions.

---


### 133. [A Usable and Secure Bengali CAPTCHA](https://arxiv.org/abs/2606.29077)

**<font color=#1a73e8>作者：</font>** Md Neyamul Islam Shibbir, Md Hasibur Rahman, Farida Chowdhury 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text-based CAPTCHAs (Completely Automated Public Turing test to tell Computers and Humans Apart) have traditionally been a simple, affordable, lightweight, yet very effective security mechanism to distinguish human users from automated bots on the web, serving as a preventive measure against many cyberattacks. However, the dependence on the English script creates usability issues for non-native speakers, limiting accessibility for regional communities where English is not widely understood. In this work, we have proposed and implemented a text CAPTCHA mechanism with 6 variants on the Bengali language, designed specifically for native Bengali-speaking users, which is the first of its kind to the best of our knowledge. Our proposed Bengali CAPTCHA exhibits robust security against automated OCR-based attacks, limited to only 0-20% average character recognition rate across 6,000 challenges (1,000 per variant approx.). Furthermore, our design demonstrates high human usability, evaluated with 110 participants, achieving success rates of 56.25% to 90.29% and average response times of 6.69 to 9.9 seconds across all six variants, thereby standing out among text-based CAPTCHA benchmarks.

---


### 134. [Priced Motion Through Optimal Faces: A Normal-Fan Geometry for Non-Stationary Adversarial MDPs](https://arxiv.org/abs/2606.29092)

**<font color=#1a73e8>作者：</font>** Kai Hidajat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In a changing decision problem, standard dynamic-regret analyses have often equated the cost of non-stationarity to how far loss moves. However, it is simultaneously possible for a loss sequence to travel far and retain the same optimal policy, or for a small movement in loss to force the optimal policy to change completely. Thus, the size of the movement through loss variation, transition variation, or comparator path length describe the adversary's motion, but not the cost of that motion to the control problem. For a more faithful analytic interpretation, this paper develops a normal-fan geometry for finite-horizon adversarial MDPs with fixed transitions. Occupancy measures form a polytope, and each loss vector exposes an optimal face of that polytope. Non-stationarity in rewards is therefore a path through the normal fan, where motion inside one cone leaves the optimal face unchanged, while crossing a wall may carry regret. We pose the notion of a face-crossing price, which is the minimum regret incurred by remaining on the previous optimal face under the new loss. For any learner that tracks the previous face, dynamic regret decomposes exactly into intrinsic priced face motion plus within-face selection error. The resulting theory separates consequential from harmless non-stationarity, where loss variation can be arbitrarily large at zero price, and identical one-coordinate variation can hide horizon-scale differences in regret.

---


### 135. [HorizonRelight: Relighting Long-horizon Videos Consistently via Diffusion Transformers](https://arxiv.org/abs/2606.29095)

**<font color=#1a73e8>作者：</font>** Jing Yang, Mayoore Jaiswal, Zian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based video relighting enables controllable relighting from a single input video, but modern video diffusion backbones are trained on short clips and applied to long-horizon videos through chunked sliding-window inference, often causing temporal discontinuities at chunk boundaries. We address this by reframing long-horizon relighting as \emph{temporally conditioned latent domain translation}. Our framework enforces cross-chunk continuity by propagating target-domain latents across boundaries and makes this behavior learnable using \emph{masked target-domain self-conditioning}, training the model to continue from temporally masked propagated context. We further introduce \emph{warm-start prompting} with a relit prompt anchor from a controllable generative model, which establishes the initial target-domain state and creates a general interface for prompt-based relighting. Experiments on in-the-wild long-horizon videos show markedly improved temporal consistency, with chunk-boundary artifacts largely reduced and unwanted appearance changes across chunks greatly suppressed.

---


### 136. [BTI-Net: Bidirectional Decoder-Level Task Interaction via Uncertainty-Aware Gating for Multi-Task Medical Image Analysis](https://arxiv.org/abs/2606.29102)

**<font color=#1a73e8>作者：</font>** Abdullah Al Shafi, Md Kawsar Mahmud Khan Zunayed, Safin Ahmmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Jointly learning to segment and classify medical images demands cross-task synergy, yet encoder-sharing architectures limit decoder reconstruction to task-private representations, permanently discarding the boundary cues and semantic priors each branch could supply to the other. This work introduces BTI-Net, which establishes bidirectional communication at every decoder level through two parallel pathways via Task Interaction Modules (TIM). Spatial boundary context is gated into the classification branch, while global semantic priors multiplicatively modulate the decoder, with refined features propagating progressively from coarse semantics to fine boundary detail across all four decoder resolutions. Since cross-task interaction is not equally reliable for every input, Uncertainty Proxy Attention (UPA) gates each TIM output per instance and per level using three signals that capture cross-task alignment, scene complexity, and prediction confidence, without external annotations or additional inference passes. Experiments on three medical benchmarks spanning ultrasound, dermoscopy, and brain MRI demonstrate consistent improvements in segmentation IoU and classification accuracy over both encoder-sharing and decoder-interaction baselines. Ablation confirms adaptive gating contributes +2.36 IoU over fixed bidirectional interaction, and classification accuracy improves by up to +2.26 points over the strongest multi-task baseline. UPA's uncertainty proxies serve as reliable single-pass task-failure signals without the overhead of stochastic sampling. Code: this https URL

---


### 137. [A Deep Multiscale Neural Network for Accurate Neurological Disorder Detection from MRI Scans and Real-Time Web Deployment](https://arxiv.org/abs/2606.29106)

**<font color=#1a73e8>作者：</font>** Ali Fatahi, Hoda Zamani, Mohammad H. Nadimi-Shahraki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neurological disorders involve diverse pathologies of the brain and nervous system, making early and accurate detection essential. While many deep CNNs have been developed for MRI-based classification of neurological disorders, most are optimized for binary tasks and often fail to capture the multi-class features needed to distinguish subtle anatomical differences across conditions. This study proposes the Enhanced Neurological Disorder Detection Network (End-Net) for multi-class MRI classification of neurological disorders. End-Net includes 24 convolutional layers, beginning with convolutional blocks followed by 21 optimized inception modules. These modules extract multiscale features via parallel 1 x 1, 3 x 3, and factorized 5 x 5 convolutional branches, along with max pooling, enabling the model to capture complementary texture, edge, shape, and contextual information. A global average pooling head, compact fully connected classifier, and dropout reduce parameters, limit overfitting, and improve robustness. End-Net was evaluated on the Multi-Class Neurological Disorder dataset, comprising MRI scans from patients with Alzheimer's disease, brain tumors, multiple sclerosis, and healthy controls. Severe class imbalance was addressed by augmenting minority classes with WGAN-GP and randomly undersampling the majority class. The results show that End-Net outperforms existing architectures in both accuracy and generalization. The model is also integrated into an online system for real-time web-based inference and accessibility.

---


### 138. [Symbolon: Symbolic Execution by Learning Code Transformation](https://arxiv.org/abs/2606.29108)

**<font color=#1a73e8>作者：</font>** Jie Zhu, Penghui Li, Zhongxuan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Symbolic execution is a powerful program analysis technique with broad applications, such as vulnerability detection, security testing, and malware analysis. However, this technique is known to suffer from scalability issues, e.g., path explosion, complex constraints, due to certain structural and semantic patterns commonly presented in real-world programs. Existing approaches attempt to escape these patterns by transforming programs into new representations to reduce the execution cost. Unfortunately, these transformations are often too rigid to exploit diverse local program semantics and sometimes rely on compiler optimizations designed for concrete execution that may misalign with the goals of symbolic execution.
We present Symbolon, a framework that automatically learns diverse code transformations and applies them context-sensitively to improve symbolic execution. Our key insight is to formulate transformation discovery as a search problem over program representations. To make the search practical, Symbolon learns transformations cheaply offline on small programs, distills them into a reusable library of agent skills, and uses an agent to instantiate these skills on repo-level targets. Our evaluation shows that Symbolon substantially improves the symbolic execution engine KLEE across 16 search strategies on 32 real-world programs, increasing line coverage by 3.69x on average while reducing peak memory and per-query solver time by 29.2x and 123x, respectively. When applied to the latest Linux kernel, Symbolon uncovers 21 previously unknown bugs, all of which have been reported to the kernel maintainers.

---


### 139. [Few-Step Boltzmann Generators via Scalable Likelihood Flow Maps](https://arxiv.org/abs/2606.29110)

**<font color=#1a73e8>作者：</font>** RuiKang OuYang, Hanlin Yu, Xinyue Ai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in flow-based generative modeling has led to models that output high-quality samples while using only a small number of function evaluations. However, at present, there is a lack of similar advances in estimating the model likelihood. In particular, most existing methods either rely on restrictive architectures that enable exact calculations, or use stochastic approximations such as Hutchinson's trace estimator that introduce substantial variance. In this work, we introduce SCAlable LikeLihood distillation of flOw maPs (SCALLOP). SCALLOP builds on the recently proposed F2D2, a likelihood flow map model that can generate samples and their densities in a small number of function evaluations. While F2D2 uses Hutchinson's estimator during training, we introduce an alternative and more scalable likelihood distillation objective that is Hutchinson-free and admits a vectorized formulation. Empirically, we demonstrate the effectiveness of SCALLOP as a Boltzmann generator in molecular science, and further validate its benefit on image datasets. SCALLOP significantly reduces both training variance and training time while consistently improving performance compared to F2D2, and is competitive with the state-of-the-art while achieving up to 10x inference speedup over the fastest baseline.

---


### 140. [Managing the Human Fallback: Skill Investment Under Improving AI and Worker Mobility](https://arxiv.org/abs/2606.29111)

**<font color=#1a73e8>作者：</font>** Simrita Singh, Naireet Ghosh, Tinglong Dai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When firms deploy autonomous AI, they must decide how much work to leave to the system and how much to keep workers engaged. This decision affects current output and future human capital. We develop a parsimonious two-period model in which AI may outperform the worker when it functions, but may fail with positive probability. A firm chooses worker engagement; engagement lowers current output for below-benchmark workers, but changes future skill through learning and erosion. We distinguish two dimensions of AI progress: capability, the system's output when it works, and reliability, the probability that it works. In a single-firm benchmark, engagement is valuable only as fallback investment. The firm engages the least-skilled workers most, because they have the largest skill gaps and are least costly to bring toward a useful fallback level. With worker mobility, engagement also affects labor-market sorting: workers prefer jobs that build more valuable skill trajectories. This sorting motive targets higher-skill workers near the AI frontier, where skill gains are more valuable and engagement is less costly. Mobility can therefore reverse the engagement pattern, shifting investment from the least-skilled toward the most-skilled workers below the AI benchmark. Mobility also reshapes how AI progress affects engagement: greater capability raises engagement by increasing the value of the skill trajectory a firm offers, whereas greater reliability can raise or lower it because it reduces fallback need while also changing learning opportunities. Under worker mobility, human-AI work design becomes a problem of human-capital investment, in which allocating work today shapes future skill.

---


### 141. [A Novel Latent-Class Attack and its Detection by Class Subspace Orthogonalization](https://arxiv.org/abs/2606.29112)

**<font color=#1a73e8>作者：</font>** Guangmingmei Yang, David J. Miller, George Kesidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning, which in general relies on voluminous amounts of training data, is vulnerable to data poisoning attacks, including error-generic attacks and backdoors (Trojans). In this work, we propose a new data poisoning attack we dub a latent class attack. Here, all poisoned examples are from a class that is novel (unknown) for the given classification domain and are mislabeled to one of the known classes (the target class) of the domain, so that the model learns to recognize the novel class as a sub-class of the target class. Such attacks could be used e.g. to defeat AI-based access control systems, or could cause a "foe" to be classified as a "friend". We also propose a post-training defense to detect this attack, without any access to the training set. This detection approach builds on "class subspace orthogonalization" (CSO), a plug-and-play paradigm demonstrated to improve existing backdoor detectors. Here, CSO is used to seek an input (a putative unknown class instance) whose internal representation is not aligned with any of the known classes, and yet which is classified with confidence to one of these classes. Finally, specific to image classification domains, we propose a method for visualizing the estimated unknown class instance, providing explainability to our latent class detections.

---


### 142. [Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule](https://arxiv.org/abs/2606.29119)

**<font color=#1a73e8>作者：</font>** Ramchand Kumaresan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a pre-registered screening rule that decides, before any implementation, whether an evolutionary / population / lifecycle outer loop over neural-network parameters or structure is worth building. Such outer loops cost 10^2-10^3x their gradient inner loop, yet whether they beat a cheap single-shot alternative is usually discovered only after the expense is paid. Our rule computes, at a Phase-0 gate, a single number: the recovery R = s/G, the best single-shot gradient/curvature statistic's gain s divided by the best gain G of any cheap method evaluated, and prescribes skipping the outer loop when R >= 90%. We validate the rule on a within-lab series of pre-registered outer-loop bets (two analyzed cases plus a disclosed file drawer): in both analyzed cases a static or single-shot computation captured the effect on the project's own metric, the gate fired (R approximately 1.0 in both cases; approximately 0.95 under a stricter metric on one), and the outer loop was abandoned, including one case where a companion factorial decomposition localizes the apparent win to a static substrate change with the evolutionary lifecycle contributing no detectable gain. On one project the gate cost about 50-70 GPU-hours and screened out an estimated 400+ GPU-hours (first cell only) plus weeks of implementation, a 6-8x saving. The rule is prospectively falsifiable: a task with R < 90% where the outer loop still fails to beat single-shot would refute it.

---


### 143. [How Anthropomorphic Language Impacts Public Perceptions of AI](https://arxiv.org/abs/2606.29121)

**<font color=#1a73e8>作者：</font>** Betty Li Hou, Sophie Hao, Sunoo Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Public discourse about artificial intelligence (AI) often uses anthropomorphic language: language that attributes human capabilities and characteristics to the system. This practice has been criticized for setting misleading expectations, inflating claims, and fueling hype around AI, which may distort public understanding of AI and impact policy priorities. We study the effects of anthropomorphic framing by comparing changes in participants' perceptions (N=815) when reading passages with and without anthropomorphic language, designed to reflect realistic public-facing AI discourse. We further examine whether these effects differ across two types of AI technologies -- large language models and recommendation systems -- and measure changes in perceptions of AI across several dimensions that are prominent in current public discourse. In a separate condition using a text that explicitly discusses the dangers of AI, we show that individuals' views of AI can shift in response to reading a text; yet in the main conditions of the experiment, where we compare anthropomorphic and non-anthropomorphic descriptions, we find that whether the text uses anthropomorphic language does not substantially affect participants' perceptions of AI. Our results indicate that any immediate effects on public opinions of AI are modest, although they leave open the possibility that anthropomorphic language could have an effect in naturalistic settings, or over gradual, continued exposure.

---


### 144. [HiComm: Hierarchical Communication for Multi-agent Reinforcement Learning](https://arxiv.org/abs/2606.29126)

**<font color=#1a73e8>作者：</font>** Runze Zhao, Dongruo Zhou, Sumit Kumar Jha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent reinforcement learning (MARL) often relies on communication to mitigate partial observability, yet most existing protocols treat messages as flat dense vectors detached from the structure of the observations they summarize. This design overlooks an important source of inductive bias in many cooperative environments, where observations naturally follow a hierarchy such as groups and entities. We propose \textsc{HiComm}, a plug-in communication module that grounds messages in the sender's hierarchical observation. \textsc{HiComm} is receiver-driven: the receiver issues a query, and the hierarchy is resolved through a three-stage decoding process that first selects a group, then a sender, and then an entity within that group, returning the corresponding feature slice as the message. This converts communication from unstructured vector transmission into structured information retrieval over the sender's observation hierarchy. We instantiate this mechanism with Straight-Through Gumbel-Softmax for differentiable discrete selection and a lightweight shared projection design that attaches to standard MARL pipelines. Experiments across cooperative MARL tasks with different observation structures and coordination demands show that \textsc{HiComm} matches or outperforms representative learned communication baselines while reducing communication volume by up to $23\times$ per receiver per episode.

---


### 145. [Beyond Backscatter: AlphaEarth Land-Cover Priors for Rapid SAR Flood Segmentation Across Foundation Backbones](https://arxiv.org/abs/2606.29134)

**<font color=#1a73e8>作者：</font>** Sanjay Thasma, Yu-Hsuan Ho, Ali Mostafavi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid flood mapping is critical for emergency response, yet optical imagery is often unusable during major flooding and single-temporal SAR is ambiguous, since new inundation, permanent water, and other smooth surfaces produce similar backscatter. This study evaluates whether stable land-context priors can improve post-event SAR flood segmentation when a registered, seasonally matched pre-event acquisition is unavailable. Using the CONUS (Continental United States) subset of ImpactMesh-Flood, we compare four backbones spanning distinct pretraining regimes-a from-scratch CNN UNet, an ImageNet-pretrained UNet, the SAR-pretrained TerraMind Vision Transformer, and the optical-satellite-pretrained DINOv3 Vision Transformer-in SAR-only, SAR+DEM, and SAR+AlphaEarth configurations under an identical fusion design, training protocol, and event-stratified split. Models are selected on a validation flood event and evaluated separately on two held-out events, Hurricane Florence and the Louisiana floods, with three-seed reporting for auxiliary configurations. Both auxiliary priors improve over the observed SAR-only baselines across all backbones and test events. AlphaEarth exceeds DEM on the harder Florence event for every backbone and achieves the best Florence IoU, while DEM is competitive on Louisiana and produces the best result there. The seed analysis reveals a trade-off: DEM is more stable across initializations, whereas AlphaEarth offers higher peak performance and higher recall on the harder event. Cross-event differences track flood-class prevalence and similarity to the training distribution, underscoring the need for per-event evaluation. We reframe single-temporal SAR flood segmentation as an alignment between radar observations and stable land-surface priors, where learned and physical context offer complementary pathways to more reliable rapid flood mapping.

---


### 146. [CMTFormer: Marrying Transformer with Hierarchical Information Interaction for RGB-Event Object Detection](https://arxiv.org/abs/2606.29136)

**<font color=#1a73e8>作者：</font>** Yu Li, Yuenan Hou, Yingmei Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras capture sparse brightness changes with high temporal resolution and high dynamic range, compensating for the deficiencies of the conventional RGB frames. However, previous multi-modal fusion techniques typically fail to handle the inherent heterogeneity between RGB frames and event streams, thus easily leading to noise amplification or redundant feature integration during cross-modal fusion. In this paper, we propose a Cross-Modal information inTeraction transFormer, coined as CMTFormer, which hierarchically integrates RGB and event information to achieve efficient and stable multimodal collaboration. Specifically, we design a shallow-to-deep information interaction scheme. In the shallow stage, we present the Shallow Alignment Module (SAM) to achieve an efficient fusion of RGB and event low-level features, which mitigates attribute disparities and prevents noisy information. In the middle stage, we devise the Cross-modal Enhancement Module (CEM) that utilizes texture and edge information to produce mutually reinforced middle-level features. In the deep stage, we present the Learnable Deep Fusion Module (LDFM) which performs high-level information aggregation through learnable weights, thus enabling the network to adaptively fuse RGB and event clues. A Spatial Prior Module is further designed to utilize global spatial information to enhance localization accuracy. Extensive experiments are conducted on two prevalent event-based object detection benchmarks, i.e., DSEC-Detection and PKU-DAVIS-SOD. Our CMTFormer consistently surpasses the detection counterparts in both uni-modal and multi-modal settings, strongly demonstrating the effectiveness of our paradigm. Codes will be available upon publication.

---


### 147. [GPC: Large-Scale Generative Pretraining for Transferable Motor Control](https://arxiv.org/abs/2606.29148)

**<font color=#1a73e8>作者：</font>** Yi Shi, Yifeng Jiang, Chen Tessler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing controllers capable of completing a wide range of tasks in a natural and life-like manner is a key challenge in enabling practical applications of physics-based character animation. In this work, we introduce Generative Pretrained Controllers (GPC), which leverage tokenization and next-token modeling to create general-purpose, reusable generative controllers from large-scale motion datasets. Our framework utilizes end-to-end reinforcement learning to jointly optimize a "motion vocabulary", modeled via Finite Scalar Quantization (FSQ), along with a corresponding control policy that can map the discrete codes to physics-based controls. After the "codebook" has been learned, the underlying structure of this large vocabulary is modeled by training a GPT-style autoregressive transformer, leading to a powerful generative controller that generates controls for a physically simulated character by performing next-token prediction. Once the generative controller has been trained, we propose a suite of adaptation techniques for finetuning the controller for new downstream tasks. Our proposed framework greatly simplifies the training process compared to previous tokenized methods, and achieves a 99.98% success rate in reproducing a vast corpus of motion clips. The generative controller exhibits a variety of natural emergent behaviors, such as responsive behaviors to perturbations and recovery behaviors after falling. This results in highly robust general purpose controllers for a variety of downstream applications.

---


### 148. [Pooled Leaderboards Hide System-Specific Winners: A Reporting-Protocol Audit of Offline Root-Cause Analysis Benchmarks](https://arxiv.org/abs/2606.29159)

**<font color=#1a73e8>作者：</font>** Lining Hu, Ting Liu, Yuzhuo Fu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offline root-cause-analysis (RCA) benchmarks commonly rank methods by a single pooled top-1 accuracy across multiple subsystems, and engineers often read the pooled winner as a recommendation for their own subsystem. We audit that reading on three public RCA benchmark families -- OpenRCA, RCAEval, and PetShop -- covering 11 subsystems and 778 matched scoring units. To keep pairwise comparisons on identical cases, the main analysis retains four methods or comparators with complete coverage: BARO, a CD-1min adapter, max-$|Z|$, and per-service alert-count. All six pairwise comparisons show subsystem-level effects of both signs, every random-effects 95\% prediction interval crosses zero, and case-level interaction tests reject exchangeability in 5 of 6 pairs. Leave-one-system-out selection picks the lower-scoring method on up to 5 of 11 held-out subsystems, with regret reaching 24.8 pp on RCAEval / Sock-Shop. We release a 320-line audit module; given a matched RCA benchmark score table, it recomputes the same per-subsystem stability checks alongside pooled scores.

---


### 149. [GLACIER: Rethinking Mass Spectrum Prediction as an Object Detection Problem](https://arxiv.org/abs/2606.29161)

**<font color=#1a73e8>作者：</font>** Rui-Xi Wang, Runzhong Wang, Connor W. Coley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting tandem mass spectra (MS/MS) from molecular structures represents a central task in analytical chemistry with direct relevance to clinical metabolomics, systems biology, and adjacent disciplines. In this work, we revisit the problem through the lens of object detection on molecular graphs. Molecular fragmentation, a central step in MS/MS prediction, can be approximated as detecting a set of subgraphs (i.e., fragments) and their associated spectral contributions. Existing fragment-based models follow a two-stage paradigm -- first generating candidate fragments and then scoring them -- analogous to two-stage R-CNNs in computer vision. Towards higher accuracy and faster inference, we introduce GLACIER, a single-stage transformer-based fragment detection neural network for molecular graphs. This unified formulation eliminates the need for candidate enumeration, enabling scalable and globally consistent modeling of molecular fragmentation. GLACIER is faster and more accurate than existing state-of-the-art by a significant margin, achieving 70.0% and 69.7% Top-1 retrieval accuracy with and without contrastive finetuning on the MassSpecGym dataset (from the previous SOTA of 64.0%) and 52.5% and 38.5% respectively on the NIST'20 dataset (from 33.2%). Furthermore, GLACIER provides nearly 8-fold inference speedup over our prior two-stage model. Code is available at this https URL

---


### 150. [Spatially Localized Image Degradation Embeddings for Image Quality Assessment](https://arxiv.org/abs/2606.29162)

**<font color=#1a73e8>作者：</font>** Krishna Srikar Durbha, Hassene Tmar, Ping-Hao Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) currently drives state-of-the-art performance in no-reference image quality assessment (NR-IQA). However, standard SSL pipelines uniformly apply synthetic distortions across the entire image field, which can limit their sensitivity to spatially localized and co-occurring degradations encountered in real-world content. In this work, we empirically expose this representational blind spot across existing state-of-the-art encoders, demonstrating their reduced sensitivity to spatially bounded image degradations. To bridge this gap, we introduce Spatial Localized Image Degradation Embeddings for Image Quality Assessment (SLIDE-IQA). SLIDE-IQA employs a dual-branch Vision Transformer framework that injects spatially bounded degradations into a contrastive pretraining objective. To handle the spatial complexity of these degradations, we introduce a Threshold-Bounded Exclusion Mechanism, a representational design choice that resolves structural conflicts arising from spatially localized distortions to ensure the latent space respects both degradation type and spatial scale. Finally, we show that SLIDE-IQA's synthetic-only pretraining significantly improves sensitivity to localized distortions, while achieving competitive performance on NR-IQA benchmarks against existing SSL NR-IQA models.

---


> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
