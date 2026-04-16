# 📦 其他研究 | 2026年04月17日

> 本类共 **212** 篇论文

> 未进入大模型主领域展示范围的其他研究。

---

### 1. [WorkRB: A Community-Driven Evaluation Framework for AI in the Work Domain](https://arxiv.org/abs/2604.13055)

**<font color=#1a73e8>作者：</font>** Matthias De Lange, Warre Veys, Federico Retyk 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Today's evolving labor markets rely increasingly on recommender systems for hiring, talent management, and workforce analytics, with natural language processing (NLP) capabilities at the core. Yet, research in this area remains highly fragmented. Studies employ divergent ontologies (ESCO, O*NET, national taxonomies), heterogeneous task formulations, and diverse model families, making cross-study comparison and reproducibility exceedingly difficult. General-purpose benchmarks lack coverage of work-specific tasks, and the inherent sensitivity of employment data further limits open evaluation. We present \textbf{WorkRB} (Work Research Benchmark), the first open-source, community-driven benchmark tailored to work-domain AI. WorkRB organizes 13 diverse tasks from 7 task groups as unified recommendation and NLP tasks, including job/skill recommendation, candidate recommendation, similar item recommendation, and skill extraction and normalization. WorkRB enables both monolingual and cross-lingual evaluation settings through dynamic loading of multilingual ontologies. Developed within a multi-stakeholder ecosystem of academia, industry, and public institutions, WorkRB has a modular design for seamless contributions and enables integration of proprietary tasks without disclosing sensitive data. WorkRB is available under the Apache 2.0 license at this https URL.

---


### 2. [Text-as-Signal: Quantitative Semantic Scoring with Embeddings, Logprobs, and Noise Reduction](https://arxiv.org/abs/2604.13056)

**<font color=#1a73e8>作者：</font>** Hugo Moreira  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a practical pipeline for turning text corpora into quantitative semantic signals. Each news item is represented as a full-document embedding, scored through logprob-based evaluation over a configurable positional dictionary, and projected onto a noise-reduced low-dimensional manifold for structural interpretation. In the present case study, the dictionary is instantiated as six semantic dimensions and applied to a corpus of 11,922 Portuguese news articles about Artificial Intelligence. The resulting identity space supports both document-level semantic positioning and corpus-level characterization through aggregated profiles. We show how Qwen embeddings, UMAP, semantic indicators derived directly from the model output space, and a three-stage anomaly-detection procedure combine into an operational text-as-signal workflow for AI engineering tasks such as corpus inspection, monitoring, and downstream analytical support. Because the identity layer is configurable, the same framework can be adapted to the requirements of different analytical streams rather than fixed to a universal schema.

---


### 3. [A Multi-Model Approach to English-Bangla Sentiment Classification of Government Mobile Banking App Reviews](https://arxiv.org/abs/2604.13057)

**<font color=#1a73e8>作者：</font>** Md. Naim Molla, Md Muhtasim Munif Fahim, Md. Binyamin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For millions of users in developing economies who depend on mobile banking as their primary gateway to financial services, app quality directly shapes financial access. The study analyzed 5,652 Google Play reviews in English and Bangla (filtered from 11,414 raw reviews) for four Bangladeshi government banking apps. The authors used a hybrid labeling approach that combined use of the reviewer's star rating for each review along with a separate independent XLM-RoBERTa classifier to produce moderate inter-method agreement (kappa = 0.459). Traditional models outperformed transformer-based ones: Random Forest produced the highest accuracy (0.815), while Linear SVM produced the highest weighted F1 score (0.804); both were higher than the performance of fine-tuned XLM-RoBERTa (0.793). McNemar's test confirmed that all classical models were significantly superior to the off-the-shelf XLM-RoBERTa (p < 0.05), while differences with the fine-tuned variant were not statistically significant. DeBERTa-v3 was applied to analyze the sentiment at the aspect level across the reviews for the four apps; the reviewers expressed their dissatisfaction primarily with the speed of transactions and with the poor design of interfaces; eJanata app received the worst ratings from the reviewers across all apps. Three policy recommendations are made based on these findings - remediation of app quality, trust-centred release management, and Bangla-first NLP adoption - to assist state-owned banks in moving towards improving their digital services through data-driven methods. Notably, a 16.1-percentage-point accuracy gap between Bangla and English text highlights the need for low-resource language model development.

---


### 4. [A Proactive EMR Assistant for Doctor-Patient Dialogue: Streaming ASR, Belief Stabilization, and Preliminary Controlled Evaluation](https://arxiv.org/abs/2604.13059)

**<font color=#1a73e8>作者：</font>** Zhenhai Pan, Yan Liu, Jia You  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most dialogue-based electronic medical record (EMR) systems still behave as passive pipelines: transcribe speech, extract information, and generate the final note after the consultation. That design improves documentation efficiency, but it is insufficient for proactive consultation support because it does not explicitly address streaming speech noise, missing punctuation, unstable diagnostic belief, objectification quality, or measurable next-action gains. We present an end-to-end proactive EMR assistant built around streaming speech recognition, punctuation restoration, stateful extraction, belief stabilization, objectified retrieval, action planning, and replayable report generation. The system is evaluated in a preliminary controlled setting using ten streamed doctor-patient dialogues and a 300-query retrieval benchmark aggregated across dialogues. The full system reaches state-event F1 of 0.84, retrieval Recall@5 of 0.87, and end-to-end pilot scores of 83.3% coverage, 81.4% structural completeness, and 80.0% risk recall. Ablations further suggest that punctuation restoration and belief stabilization may improve downstream extraction, retrieval, and action selection within this pilot. These results were obtained under a controlled simulated pilot setting rather than broad deployment claims, and they should not be read as evidence of clinical deployment readiness, clinical safety, or real-world clinical utility. Instead, they suggest that the proposed online architecture may be technically coherent and directionally supportive under tightly controlled pilot conditions. The present study should be read as a pilot concept demonstration under tightly controlled pilot conditions rather than as evidence of clinical deployment readiness or clinical generalizability.

---


### 5. [Red Skills or Blue Skills? A Dive Into Skills Published on ClawHub](https://arxiv.org/abs/2604.13064)

**<font color=#1a73e8>作者：</font>** Haichuan Hu, Ye Shang, Quanjun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skill ecosystems have emerged as an increasingly important layer in Large Language Model (LLM) agent systems, enabling reusable task packaging, public distribution, and community-driven capability sharing. However, despite their rapid growth, the functionality, ecosystem structure, and security risks of public skill registries remain underexplored. In this paper, we present an empirical study of ClawHub, a large public registry of agent skills. We build and normalize a dataset of 26,502 skills, and conduct a systematic analysis of their language distribution, functional organization, popularity, and security signals. Our clustering results show clear cross-lingual differences: English skills are more infrastructure-oriented and centered on technical capabilities such as APIs, automation, and memory, whereas Chinese skills are more application-oriented, with clearer scenario-driven clusters such as media generation, social content production, and finance-related services. We further find that more than 30% of all crawled skills are labeled as suspicious or malicious by available platform signals, while a substantial fraction of skills still lack complete safety observability. To study early risk assessment, we formulate submission-time skill risk prediction using only information available at publication time, and construct a balanced benchmark of 11,010 skills. Across 12 classifiers, the best Logistic Regression achieves a accuracy of 72.62% and an AUROC of 78.95%, with primary documentation emerging as the most informative submission-time signal. Our findings position public skill registries as both a key enabler of agent capability reuse and a new surface for ecosystem-scale security risk.

---


### 6. [From Seeing it to Experiencing it: Interactive Evaluation of Intersectional Voice Bias in Human-AI Speech Interaction](https://arxiv.org/abs/2604.13067)

**<font color=#1a73e8>作者：</font>** Shree Harsha Bokkahalli Satish, Maria Teleki, Christoph Minixhofer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> SpeechLLMs process spoken language directly from audio, but accent and vocal identity cues can lead to biased behaviour. Current bias evaluations often miss how such bias manifests in end-to-end speech interactions and how users experience it. We distinguish quality-of-service disparities (e.g., off-topic or low-effort responses) from content-level bias in coherent outputs, and examine intersectional effects of accent and perceived gender. In this work, we explore a two-part evaluation approach: (1) a controlled test cohort spanning six accents and two gender presentations, analysed with judge-free prompt-response metrics, and (2) an interactive study design using voice conversion to let users experience identical content through different vocal identities. Across two studies (Interactive, N=24; Observational, N=19), we find that voice conversion increases trust and acceptability for benign responses and encourages perspective-taking, while automated analysis in search of quality-of-service disparities, reveals {accent x gender} disparities in alignment and verbosity across SpeechLLMs. These results highlight voice conversion for probing and experiencing intersectional voice bias while our evaluation suite provides richer bias evaluations for spoken conversational AI.

---


### 7. [Curation of a Palaeohispanic Dataset for Machine Learning](https://arxiv.org/abs/2604.13070)

**<font color=#1a73e8>作者：</font>** Gonzalo Martínez-Fernández, Jose F Quesada, Agustín Riscos-Núñez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Palaeohispanic languages are those spoken in the Iberian Peninsula before the arrival of the Romans in the 3rd Century B.C. Their study was really put on motion after Gómez Moreno deciphered the Iberian Levantine script, one of the several semi-sillabaries used by these languages. Still, the Palaeohispanic languages have varying degrees of decipherment, and none is fully known to this day. Most of the studies have been performed from a purely linguistic point of view, and a computational approach may benefit this research area greatly. However, the resources are limited and presented in an unsuitable format for techniques such as Machine Learning. Therefore, a structured dataset is constructed, which will hopefully allow more progress in the field.

---


### 8. [IWLV-Ramayana: A Sarga-Aligned Parallel Corpus of Valmiki's Ramayana Across Indian Languages](https://arxiv.org/abs/2604.13078)

**<font color=#1a73e8>作者：</font>** Sumesh VP  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Ramayana is among the most influential literary traditions of South and Southeast Asia, transmitted across numerous linguistic and cultural contexts over two millennia. Despite extensive scholarship on regional Ramayana traditions, computational resources enabling systematic cross-linguistic analysis remain limited. This paper introduces the IWLV Ramayana Corpus, a structured parallel corpus aligning Valmiki's Ramayana across multiple Indian languages at the level of the sarga (chapter). The corpus currently includes complete English and Malayalam layers, with Hindi, Tamil, Kannada, and Telugu layers in active production. The dataset is distributed in structured JSONL format with explicit provenance metadata, enabling applications in comparative literature, corpus linguistics, digital humanities, and multilingual natural language processing. To our knowledge, this is the first sarga-aligned multilingual parallel corpus of the Valmiki Ramayana with explicit provenance metadata and machine-readable format.

---


### 9. [Sparse Goodness: How Selective Measurement Transforms Forward-Forward Learning](https://arxiv.org/abs/2604.13081)

**<font color=#1a73e8>作者：</font>** Kamer Ali Yuksel, Hassan Sawaf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Forward-Forward (FF) algorithm is a biologically plausible alternative to backpropagation that trains neural networks layer by layer using a local goodness function to distinguish positive from negative data. Since its introduction, sum-of-squares (SoS) has served as the default goodness function. In this work, we systematically study the design space of goodness functions, investigating both which activations to measure and how to aggregate them. We introduce top-k goodness, which evaluates only the k most active neurons, and show that it substantially outperforms SoS, improving Fashion-MNIST accuracy by 22.6 percentage points. We further introduce entmax-weighted energy, which replaces hard top-k selection with a learnable sparse weighting based on the alpha-entmax transformation, yielding additional gains. Orthogonally, we adopt separate label feature forwarding (FFCL), in which class hypotheses are injected at every layer through a dedicated projection rather than concatenated only at the input. Combining these ideas, we achieve 87.1 percent accuracy on Fashion-MNIST with a 4x2000 architecture, representing a 30.7 percentage point improvement over the SoS baseline while changing only the goodness function and the label pathway. Across controlled experiments covering 11 goodness functions, two architectures, and a sparsity spectrum analysis over both k and alpha, we identify a consistent principle: sparsity in the goodness function is the most important design choice in FF networks. In particular, adaptive sparsity with alpha approximately 1.5 outperforms both fully dense and fully sparse alternatives.

---


### 10. [The Long Delay to Arithmetic Generalization: When Learned Representations Outrun Behavior](https://arxiv.org/abs/2604.13082)

**<font color=#1a73e8>作者：</font>** Laura Gomezjurado Gonzalez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking in transformers trained on algorithmic tasks is characterized by a long delay between training-set fit and abrupt generalization, but the source of that delay remains poorly understood. In encoder-decoder arithmetic models, we argue that this delay reflects limited access to already learned structure rather than failure to acquire that structure in the first place. We study one-step Collatz prediction and find that the encoder organizes parity and residue structure within the first few thousand training steps, while output accuracy remains near chance for tens of thousands more. Causal interventions support the decoder bottleneck hypothesis. Transplanting a trained encoder into a fresh model accelerates grokking by 2.75 times, while transplanting a trained decoder actively hurts. Freezing a converged encoder and retraining only the decoder eliminates the plateau entirely and yields 97.6% accuracy, compared to 86.1% for joint training. What makes the decoder's job harder or easier depends on numeral representation. Across 15 bases, those whose factorization aligns with the Collatz map's arithmetic (e.g., base 24) reach 99.8% accuracy, while binary fails completely because its representations collapse and never recover. The choice of base acts as an inductive bias that controls how much local digit structure the decoder can exploit, producing large differences in learnability from the same underlying task.

---


### 11. [Adaptive Memory Crystallization for Autonomous AI Agent Learning in Dynamic Environments](https://arxiv.org/abs/2604.13085)

**<font color=#1a73e8>作者：</font>** Rajat Khanda, Mohammad Baqar Sambuddha Chakrabarti, Satyasaran Changdar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents operating in dynamic environments face a persistent challenge: acquiring new capabilities without erasing prior knowledge. We present Adaptive Memory Crystallization (AMC), a memory architecture for progressive experience consolidation in continual reinforcement learning.
AMC is conceptually inspired by the qualitative structure of synaptic tagging and capture (STC) theory, the idea that memories transition through discrete stability phases, but makes no claim to model the underlying molecular or synaptic mechanisms.
AMC models memory as a continuous crystallization process in which experiences migrate from plastic to stable states according to a multi-objective utility signal. The framework introduces a three-phase memory hierarchy (Liquid--Glass--Crystal) governed by an Itô stochastic differential equation (SDE) whose population-level behavior is captured by an explicit Fokker--Planck equation admitting a closed-form Beta stationary distribution.
We provide proofs of: (i) well-posedness and global convergence of the crystallization SDE to a unique Beta stationary distribution; (ii) exponential convergence of individual crystallization states to their fixed points, with explicit rates and variance bounds; and (iii) end-to-end Q-learning error bounds and matching memory-capacity lower bounds that link SDE parameters directly to agent performance.
Empirical evaluation on Meta-World MT50, Atari 20-game sequential learning, and MuJoCo continual locomotion consistently shows improvements in forward transfer (+34--43\% over the strongest baseline), reductions in catastrophic forgetting (67--80\%), and a 62\% decrease in memory footprint.

---


### 12. [Design Conditions for Intra-Group Learning of Sequence-Level Rewards: Token Gradient Cancellation](https://arxiv.org/abs/2604.13088)

**<font color=#1a73e8>作者：</font>** Fei Ding, Yongkang Zhang, youwei wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In sparse termination rewards, intra-group comparisons have become the dominant paradigm for fine-tuning reasoning models via reinforcement learning. However, long-term training often leads to issues like ineffective update accumulation (learning tax), solution probability drift, and entropy collapse. This paper presents a necessary condition for algorithm design from a token-level credit assignment perspective: to prevent reward-irrelevant drift, intra-group objectives must maintain gradient exchangeability across token updates, enabling gradient cancellation on weak-credit/high-frequency tokens. We show that two common mechanisms disrupting exchangeability make "non-cancellation" a structural norm. Based on this, we propose minimal intra-group transformations to restore or approximate the cancellation structure in the shared token space. Experimental results demonstrate that these transformations stabilize training, improve sample efficiency, and enhance final performance, validating the value of this design condition.

---


### 13. [A Lightweight Multi-Metric No-Reference Image Quality Assessment Framework for UAV Imaging](https://arxiv.org/abs/2604.13112)

**<font color=#1a73e8>作者：</font>** Koffi Titus Sergio Aglin, Anthony K. Muchiri, Celestin Nkundineza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable image quality assessment is essential in applications where large volumes of images are acquired automatically and must be filtered before further analysis. In many practical scenarios, a pristine reference image is unavailable, making no reference image quality assessment (NR-IQA) particularly important. This paper introduces Multi-Metric Image Quality Assessment (MM-IQA), a lightweight multi-metric framework for NR-IQA. It combines interpretable cues related to blur, edge structure, low resolution artifacts, exposure imbalance, noise, haze, and frequency content to produce a single quality score in the range [0,100].MM-IQA was evaluated on five benchmark datasets (KonIQ-10k, LIVE Challenge, KADID-10k, TID2013, and BIQ2021) and achieved SRCC values ranging from 0.647 to 0.830. Additional experiments on a synthetic agricultural dataset showed consistent behavior of the designed cues. The Python/OpenCV implementation required about 1.97 s per image. This method also has modest memory requirements because it stores only a limited number of intermediate grayscale, filtered, and frequency-domain representations, resulting in memory usage that scales linearly with image size. The results show that MM-IQA can be used for fast image quality screening with explicit distortion aware cues and modest computational cost.

---


### 14. [Robust Covert Quantum Communication under Bounded Channel Uncertainty](https://arxiv.org/abs/2604.13116)

**<font color=#1a73e8>作者：</font>** Abbas Arghavani, Alessandro V. Papadopoulos, Vahid Azimi Mousolou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Covert quantum communication is usually analyzed under idealized assumptions that channel parameters, such as transmissivity and background noise, are perfectly known and constant. In realistic optical links, including satellite, fiber, and free-space systems, these parameters vary because of environmental fluctuations, calibration noise, and estimation errors. We study covert quantum communication over compound quantum optical channels with bounded uncertainty in both transmissivity and thermal noise, and derive guarantees that hold for all admissible channel realizations.
We develop a robust framework for certifying both covertness and reliability under uncertainty. A central finding is that robustness cannot be obtained by simply inserting worst-case parameter values into known-channel bounds: the channel realizations that are most adverse for covertness and reliability generally occur at different corners of the uncertainty set. This creates a fundamental trade-off in secure system design.
We derive a closed-form lower bound on the worst-case guaranteed number of covert qubits that can be transmitted reliably, identify a sharp feasibility boundary beyond which the guaranteed payload drops to zero, and quantify the security penalty caused by uncertainty. We validate the covertness term with QuTiP simulations of a four-mode bosonic model and combine it with an analytical reliability bound to evaluate the robust payload. Our results move covert quantum communication from nominal perfect-knowledge analysis to certified worst-case operation under uncertainty.

---


### 15. [Conflict-Aware Robust Design for Covert Wireless Communications](https://arxiv.org/abs/2604.13122)

**<font color=#1a73e8>作者：</font>** Abbas Arghavani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Covert wireless communication aims to establish a reliable link while hiding the transmission from an adversary. In wireless settings, uncertainty plays a central role in this tradeoff: it can help mask the signal from a warden, but it also complicates robust system design. This raises a basic question: under bounded uncertainty, are reliability and covertness governed by the same adverse conditions? If not, robust covert design cannot be reduced to a single worst-case environment. In this paper, we study this question in a covert wireless model with quasi-static fading, outage-based reliability at Bob and radiometric detection at Willie. Uncertainty is represented through bounded intervals for Bob's average channel strength and Willie's noise power. To obtain a tractable characterization, we adopt a conditional large-N midpoint-threshold surrogate for Willie's detector, parameterized by a Willie-side fading realization. Within this framework, we show that the reliability constraint is governed by Bob's smallest admissible channel parameter, whereas the covertness constraint is governed by Willie's smallest admissible noise level. This establishes a conflict-aware robust-design principle: the adverse realizations for reliability and covertness differ. Based on this result, we derive closed-form expressions for the robustly feasible transmit power and the corresponding robust optimal rate. Numerical results show that bounded uncertainty contracts the feasible region, monotonically reduces the robust optimal rate, and can cause substantial loss relative to the nominal design. Monte Carlo results further show that the conditional surrogate closely tracks the midpoint-threshold radiometer in the intended low-effective-SNR regime. Overall, the paper shows that even in a streamlined wireless setting, robust covert design requires different adverse-case reasoning for reliability and covertness.

---


### 16. [Spectral Entropy Collapse as an Empirical Signature of Delayed Generalisation in Grokking](https://arxiv.org/abs/2604.13123)

**<font color=#1a73e8>作者：</font>** Truong Xuan Khanh, Truong Quynh Hoa, Luu Duc Trung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking -- delayed generalisation long after memorisation -- lacks a predictive mechanistic explanation. We identify the normalised spectral entropy $\tilde{H}(t)$ of the representation covariance as a scalar order parameter for this transition, validated on 1-layer Transformers on group-theoretic tasks. Five contributions: (i) Grokking follows a two-phase pattern: norm expansion then entropy collapse. (ii) $\tilde{H}$ crosses a stable threshold $\tilde{H}^* \approx 0.61$ before generalisation in 100% of runs (mean lead: 1,020 steps). (iii) A causal intervention preventing collapse delays grokking by +5,020 steps ($p=0.044$); a norm-matched control ($n=30$, $p=5\times10^{-5}$) confirms entropy -- not norm -- drives the transition. (iv) A power-law $\Delta T = C_1(\tilde{H}-\tilde{H}^*)^\gamma+C_2$ ($R^2=0.543$) predicts grokking onset with 4.1% error. (v) The mechanism holds across abelian ($\mathbb{Z}/97\mathbb{Z}$) and non-abelian ($S_5$) groups. Crucially, MLPs show entropy collapse without grokking, proving collapse is necessary but not sufficient -- architecture matters. Code: this https URL

---


### 17. [Synthetic Tabular Generators Fail to Preserve Behavioral Fraud Patterns: A Benchmark on Temporal, Velocity, and Multi-Account Signals](https://arxiv.org/abs/2604.13125)

**<font color=#1a73e8>作者：</font>** Bhavana Sajja  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce behavioral fidelity -- a third evaluation dimension for synthetic tabular data that measures whether generated data preserves the temporal, sequential, and structural behavioral patterns that distinguish real-world entity activity. Existing frameworks evaluate statistical fidelity (marginal distributions and correlations) and downstream utility (classifier AUROC on synthetic-trained models), but neither tests for the behavioral signals that operational detection and analysis systems actually rely on. We formalize a taxonomy of four behavioral fraud patterns (P1-P4) covering inter-event timing, burst structure, multi-account graph motifs, and velocity-rule trigger rates; define a degradation ratio metric calibrated to a real-data noise floor (1.0 = matches real variability, k = k-times worse); and prove that row-independent generators -- the dominant paradigm -- are structurally incapable of reproducing P3 graph motifs (Proposition 1) and produce non-positive within-entity IET autocorrelation (Proposition 2), making the positive burst fingerprint of fraud sequences unachievable regardless of architecture or training data size. We benchmark CTGAN, TVAE, GaussianCopula, and TabularARGN on IEEE-CIS Fraud Detection and the Amazon Fraud Dataset. All four fail severely: on IEEE-CIS composite degradation ratios range from 24.4x (TVAE) to 39.0x (GaussianCopula); on Amazon FDB, row-independent generators score 81.6-99.7x, while TabularARGN achieves 17.2x. We document generator-specific failure modes and their resolutions. The P1-P4 framework extends to any domain with entity-level sequential tabular data, including healthcare and network security. We release our evaluation framework as open source.

---


### 18. [Graph Propagated Projection Unlearning: A Unified Framework for Vision and Audio Discriminative Models](https://arxiv.org/abs/2604.13127)

**<font color=#1a73e8>作者：</font>** Shreyansh Pathak, Jyotishman Das  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The need to selectively and efficiently erase learned information from deep neural networks is becoming increasingly important for privacy, regulatory compliance, and adaptive system design. We introduce Graph-Propagated Projection Unlearning (GPPU), a unified and scalable algorithm for class-level unlearning that operates across both vision and audio models. GPPU employs graph-based propagation to identify class-specific directions in the feature space and projects representations onto the orthogonal subspace, followed by targeted fine-tuning, to ensure that target class information is effectively and irreversibly removed. Through comprehensive evaluations on six vision datasets and two large-scale audio benchmarks spanning a variety of architectures including CNNs, Vision Transformers, and Audio Transformers, we demonstrate that GPPU achieves highly efficient unlearning, realizing 10-20x speedups over prior methodologies while preserving model utility on retained classes. Our framework provides a principled and modality-agnostic approach to machine unlearning, evaluated at a scale that has received limited attention in prior work, contributing toward more efficient and responsible deep learning.

---


### 19. [Learning Probabilistic Responsibility Allocations for Multi-Agent Interactions](https://arxiv.org/abs/2604.13128)

**<font color=#1a73e8>作者：</font>** Isaac Remy, Caleb Chang, Karen Leung  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Human behavior in interactive settings is shaped not only by individual objectives but also by shared constraints with others, such as safety. Understanding how people allocate responsibility, i.e., how much one deviates from their desired policy to accommodate others, can inform the design of socially compliant and trustworthy autonomous systems. In this work, we introduce a method for learning a probabilistic responsibility allocation model that captures the multimodal uncertainty inherent in multi-agent interactions. Specifically, our approach leverages the latent space of a conditional variational autoencoder, combined with techniques from multi-agent trajectory forecasting, to learn a distribution over responsibility allocations conditioned on scene and agent context. Although ground-truth responsibility labels are unavailable, the model remains tractable by incorporating a differentiable optimization layer that maps responsibility allocations to induced controls, which are available. We evaluate our method on the INTERACTION driving dataset and demonstrate that it not only achieves strong predictive performance but also provides interpretable insights, through the lens of responsibility, into patterns of multi-agent interaction.

---


### 20. [Generalization Guarantees on Data-Driven Tuning of Gradient Descent with Langevin Updates](https://arxiv.org/abs/2604.13130)

**<font color=#1a73e8>作者：</font>** Saumya Goyal, Rohith Rongali, Ritabrata Ray 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study learning to learn for regression problems through the lens of hyperparameter tuning. We propose the Langevin Gradient Descent Algorithm (LGD), which approximates the mean of the posterior distribution defined by the loss function and regularizer of a convex regression task. We prove the existence of an optimal hyperparameter configuration for which the LGD algorithm achieves the Bayes' optimal solution for squared loss. Subsequently, we study generalization guarantees on meta-learning optimal hyperparameters for the LGD algorithm from a given set of tasks in the data-driven setting. For a number of parameters $d$ and hyperparameter dimension $h$, we show a pseudo-dimension bound of $O(dh)$, upto logarithmic terms under mild assumptions on LGD. This matches the dimensional dependence of the bounds obtained in prior work for the elastic net, which only allows for $h=2$ hyperparameters, and extends their bounds to regression on convex loss. Finally, we show empirical evidence of the success of LGD and the meta-learning procedure for few-shot learning on linear regression using a few synthetically created datasets.

---


### 21. [Depth-Resolved Coral Reef Thermal Fields from Satellite SST and Sparse In-Situ Loggers Using Physics-Informed Neural Networks](https://arxiv.org/abs/2604.13131)

**<font color=#1a73e8>作者：</font>** Alzayat Saleh, Mostafa Rahimi Azghadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Satellite sea surface temperature (SST) products underpin global coral bleaching monitoring, yet they measure only the ocean skin. Corals inhabit depths from the shallows to beyond 20 metres, where temperatures can be 1-3°C cooler than the surface; applying satellite SST uniformly to all depths therefore overestimates subsurface thermal stress. We present a physics-informed neural network (PINN) that fuses NOAA Coral Reef Watch SST with sparse in-situ temperature loggers within the one-dimensional vertical heat equation, enforcing SST as a hard surface boundary condition and jointly learning effective thermal diffusivity (\k{appa}) and light attenuation (Kd). Validated across four Great Barrier Reef sites (30 holdout experiments), the PINN achieves 0.25-1.38°C RMSE at unseen depths. Under extreme sparsity (three training depths), the PINN maintains 0.27°C RMSE at the 5 metre holdout and 0.32°C at the 9.1 metre holdout, where statistical baselines collapse to >1.8°C; it outperforms a physics-only finite-difference baseline in 90% of experiments. Depth-resolved Degree Heating Day (DHD) profiles show that thermal stress attenuates with depth: at Davies Reef, DHD drops from 0.29 at the surface to zero by 10.7 metres, consistent with logger observations, while satellite DHD remains constant at 0.31 across all depths. However, the PINN underestimates absolute DHD at shallow depths because its smooth predictions attenuate the short-duration peaks that drive threshold exceedances; PINN DHD values should be interpreted as conservative lower bounds on depth-resolved stress. These results demonstrate that physics-constrained fusion of satellite SST with sparse loggers can extend bleaching assessment to the depth dimension using existing observational infrastructure.

---


### 22. [Automated co-design of high-performance thermodynamic cycles via graph-based hierarchical reinforcement learning](https://arxiv.org/abs/2604.13133)

**<font color=#1a73e8>作者：</font>** Wenqing Li, Xu Feng, Peixue Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Thermodynamic cycles are pivotal in determining the efficacy of energy conversion systems. Traditional design methodologies, which rely on expert knowledge or exhaustive enumeration, are inefficient and lack scalability, thereby constraining the discovery of high-performance cycles. In this study, we introduce a graph-based hierarchical reinforcement learning approach for the co-design of structure parameters in thermodynamic cycles. These cycles are encoded as graphs, with components and connections depicted as nodes and edges, adhering to grammatical constraints. A deep learning-based thermophysical surrogate facilitates stable graph decoding and the simultaneous resolution of global parameters. Building on this foundation, we develop a hierarchical reinforcement learning framework wherein a high-level manager explores structural evolution and proposes candidate configurations, whereas a low-level worker optimizes parameters and provides performance rewards to steer the search towards high-performance regions. By integrating graph representation, thermophysical surrogate, and manager-worker learning, this method establishes a fully automated pipeline for encoding, decoding, and co-optimization. Using heat pump and heat engine cycles as case studies, the results demonstrate that the proposed method not only replicates classical cycle configurations but also identifies 18 and 21 novel heat pump and heat engine cycles, respectively. Relative to classical cycles, the novel configurations exhibit performance improvements of 4.6% and 133.3%, respectively, surpassing the traditional designs. This method effectively balances efficiency with broad applicability, providing a practical and scalable intelligent alternative to expert-driven thermodynamic cycle design.

---


### 23. [PatchPoison: Poisoning Multi-View Datasets to Degrade 3D Reconstruction](https://arxiv.org/abs/2604.13153)

**<font color=#1a73e8>作者：</font>** Prajas Wadekar, Venkata Sai Pranav Bachina, Kunal Bhosikar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has recently enabled highly photorealistic 3D reconstruction from casually captured multi-view images. However, this accessibility raises a privacy concern: publicly available images or videos can be exploited to reconstruct detailed 3D models of scenes or objects without the owner's consent. We present PatchPoison, a lightweight dataset-poisoning method that prevents unauthorized 3D reconstruction. Unlike global perturbations, PatchPoison injects a small high-frequency adversarial patch, a structured checkerboard, into the periphery of each image in a multi-view dataset. The patch is designed to corrupt the feature-matching stage of Structure-from-Motion (SfM) pipelines such as COLMAP by introducing spurious correspondences that systematically misalign estimated camera poses. Consequently, downstream 3DGS optimization diverges from the correct scene geometry. On the NeRF-Synthetic benchmark, inserting a 12 X 12 pixel patch increases reconstruction error by 6.8x in LPIPS, while the poisoned images remain unobtrusive to human viewers. PatchPoison requires no pipeline modifications, offering a practical, "drop-in" preprocessing step for content creators to protect their multi-view data.

---


### 24. [3DRealHead: Few-Shot Detailed Head Avatar](https://arxiv.org/abs/2604.13171)

**<font color=#1a73e8>作者：</font>** Jalees Nehvi, Timo Bolkart, Thabo Beeler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The human face is central to communication. For immersive applications, the digital presence of a person should mirror the physical reality, capturing the users idiosyncrasies and detailed facial expressions. However, current 3D head avatar methods often struggle to faithfully reproduce the identity and facial expressions, despite having multi-view data or learned priors. Learning priors that capture the diversity of human appearances, especially, for regions with highly person-specific features, like the mouth and teeth region is challenging as the underlying training data is limited. In addition, many of the avatar methods are purely relying on 3D morphable model-based expression control which strongly limits expressivity. To address these challenges, we are introducing 3DRealHead, a few-shot head avatar reconstruction method with a novel expression control signal that is extracted from a monocular video stream of the subject. Specifically, the subject can take a few pictures of themselves, recover a 3D head avatar and drive it with a consumer-level webcam. The avatar reconstruction is enabled via a novel few-shot inversion process of a 3D human head prior which is represented as a Style U-Net that emits 3D Gaussian primitives which can be rendered under novel views. The prior is learned on the NeRSemble dataset. For animating the avatar, the U-Net is conditioned on 3DMM-based facial expression signals, as well as features of the mouth region extracted from the driving video. These additional mouth features allow us to recover facial expressions that cannot be represented by the 3DMM leading to a higher expressivity and closer resemblance to the physical reality.

---


### 25. [Pareto-Optimal Offline Reinforcement Learning via Smooth Tchebysheff Scalarization](https://arxiv.org/abs/2604.13175)

**<font color=#1a73e8>作者：</font>** Aadyot Bhatnagar, Peter Mørch Groth, Ali Madani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can be aligned with human preferences through offline reinforcement learning (RL) on small labeled datasets. While single-objective alignment is well-studied, many real-world applications demand the simultaneous optimization of multiple conflicting rewards, e.g. optimizing both catalytic activity and specificity in protein engineering, or helpfulness and harmlessness for chatbots. Prior work has largely relied on linear reward scalarization, but this approach provably fails to recover non-convex regions of the Pareto front. In this paper, instead of scalarizing the rewards directly, we frame multi-objective RL itself as an optimization problem to be scalarized via smooth Tchebysheff scalarization, a recent technique that overcomes the shortcomings of linear scalarization. We use this formulation to derive Smooth Tchebysheff Optimization of Multi-Objective Preferences (STOMP), a novel offline RL algorithm that extends direct preference optimization to the multi-objective setting in a principled way by standardizing the individual rewards based on their observed distributions. We empirically validate STOMP on a range of protein engineering tasks by aligning three autoregressive protein language models on three laboratory datasets of protein fitness. Compared to state-of-the-art baselines, STOMP achieves the highest hypervolumes in eight of nine settings according to both offline off-policy and generative evaluations. We thus demonstrate that STOMP is a powerful, robust multi-objective alignment algorithm that can meaningfully improve post-trained models for multi-attribute protein optimization and beyond.

---


### 26. [GeoLink: A 3D-Aware Framework Towards Better Generalization in Cross-View Geo-Localization](https://arxiv.org/abs/2604.13183)

**<font color=#1a73e8>作者：</font>** Hongyang Zhang, Yinhao Liu, Haitao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalizable cross-view geo-localization aims to match the same location across views in unseen regions and conditions without GPS supervision. Its core difficulty lies in severe semantic inconsistency caused by viewpoint variation and poor generalization under domain shift. Existing methods mainly rely on 2D correspondence, but they are easily distracted by redundant shared information across views, leading to less transferable representations. To address this, we propose GeoLink, a 3D-aware semantic-consistent framework for Generalizable cross-view geo-localization. Specifically, we offline reconstruct scene point clouds from multi-view drone images using VGGT, providing stable structural priors. Based on these 3D anchors, we improve 2D representation learning in two complementary ways. A Geometric-aware Semantic Refinement module mitigates potentially redundant and view-biased dependencies in 2D features under 3D guidance. In addition, a Unified View Relation Distillation module transfers 3D structural relations to 2D features, improving cross-view alignment while preserving a 2D-only inference pipeline. Extensive experiments on multiple benchmarks show that GeoLink consistently outperforms state-of-the-art methods and achieves superior generalization across unseen domains and diverse weather environments.

---


### 27. [Towards Patient-Specific Deformable Registration in Laparoscopic Surgery](https://arxiv.org/abs/2604.13186)

**<font color=#1a73e8>作者：</font>** Alberto Neri, Veronica Penza, Nazim Haouchine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsafe surgical care is a critical health concern, often linked to limitations in surgeon experience, skills, and situational awareness. Integrating patient-specific 3D models into the surgical field can enhance visualization, provide real-time anatomical guidance, and reduce intraoperative complications. However, reliably registering these models in general surgery remains challenging due to mismatches between preoperative and intraoperative organ surfaces, such as deformations and noise. To overcome these challenges, we introduce the first patient-specific non-rigid point cloud registration method, which leverages a novel data generation strategy to optimize outcomes for individual patients. Our approach combines a Transformer encoder-decoder architecture with overlap estimation and a dedicated matching module to predict dense correspondences, followed by a physics-based algorithm for registration. Experimental results on both synthetic and real data demonstrate that our patient-specific method significantly outperforms traditional agnostic approaches, achieving 45% Matching Score with 92% Inlier Ratio on synthetic data, highlighting its potential to improve surgical care.

---


### 28. [Unleashing Implicit Rewards: Prefix-Value Learning for Distribution-Level Optimization](https://arxiv.org/abs/2604.13197)

**<font color=#1a73e8>作者：</font>** Shiping Gao, Hongzhan Chen, Xiaojun Quan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Process reward models (PRMs) provide fine-grained reward signals along the reasoning process, but training reliable PRMs often requires step annotations or heavy verification pipelines, making them expensive to scale and refresh during online RL. Implicit PRMs mitigate this cost by learning decomposable token- or step-level rewards from trajectory-level outcome labels. However, they suffer from a train-inference mismatch: training only constrains a sequence-level aggregate, whereas inference requires token-level scores to reflect local step quality. As a result, token-level credits are weakly identified and may fail to faithfully reflect which reasoning steps are actually correct. This unreliability undermines a key promise of implicit PRMs: scoring many candidate tokens. In practice, noisy per-token advantages may systematically reinforce incorrect continuations. We address this problem with a novel Implicit Prefix-Value Reward Model (IPVRM), which directly learns a prefix-conditioned value function estimating the probability of eventual correctness, and derives step signals via temporal-difference (TD) differences. IPVRM substantially improves step-verification F1 on ProcessBench. Building on these calibrated prefix values, we further propose Distribution-Level RL (DistRL), which computes TD advantages for both sampled tokens and high-probability candidate tokens, enabling dense counterfactual updates without additional rollouts. While DistRL offers limited gains when powered by miscalibrated implicit rewards, it consistently improves downstream reasoning once paired with IPVRM.

---


### 29. [InfiniteScienceGym: An Unbounded, Procedurally-Generated Benchmark for Scientific Analysis](https://arxiv.org/abs/2604.13201)

**<font color=#1a73e8>作者：</font>** Oliver Bentham, Vivek Srikumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are emerging as scientific assistants, but evaluating their ability to reason from empirical data remains challenging. Benchmarks derived from published studies and human annotations inherit publication bias, known-knowledge bias, label noise, and substantial storage requirements. We present InfiniteScienceGym, a procedurally generated benchmark of scientific repositories paired with a verifiable question-answering task. From a seed, the simulator deterministically generates a self-contained repository with realistic directory structure, files, and tabular data, and a privileged QA generator produces both answerable and unanswerable questions with exact ground truth. This makes it possible to evaluate evidence-grounded reasoning, abstention, and tool-mediated analysis in a controlled setting without distributing a large static corpus. InfiniteScienceGym complements real scientific benchmarks by targeting blind spots and failure modes that are hard to evaluate using published datasets alone. Evaluating both proprietary and open-weight models, we find that none achieve more than 45% accuracy overall, that recognizing unanswerable questions remains a major weakness, and that stronger models tend to use tools more effectively rather than simply consuming more tokens.

---


### 30. [Inclusive Kitchen Design for Older Adults: Generative AI Visualizations to Support Mild Cognitive Impairment](https://arxiv.org/abs/2604.13203)

**<font color=#1a73e8>作者：</font>** Ibrahim Bilau, Nicole Li, Terrence Malayvong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mild Cognitive Impairment (MCI) affects 15-20% of adults aged 65 and older, often making kitchen navigation and independent living difficult, particularly in lower-income communities with limited access to professional design help. This study created an AI system that converts standard kitchen photos into MCI-friendly designs using the Home Design Guidelines (HDG). Stable Diffusion models, enhanced with DreamBooth LoRA and ControlNet, were trained on 100 kitchen images to produce realistic visualizations with open layouts, transparent cabinetry, better lighting, non-slip flooring, and less clutter. The models achieved moderate to high semantic alignment (normalized CLIP scores 0.69-0.79) and improved visual realism (GIQA scores 0.45-0.65). In a survey of 33 participants (51.5% caregivers, 36.4% older adults with MCI), the AI-modified kitchens were strongly preferred as more cognitively friendly (87.4% of 198 choices, p < .001). Participants reported high confidence in their kitchen choice selections (M = 5.92/7) and found the visualizations very helpful for home modifications (M = 6.27/7). Thematic analysis emphasized improved visibility, lower cognitive load, and greater independence. Overall, this AI tool provides a low-cost, scalable way for older adults and caregivers to visualize and implement DIY kitchen changes, supporting aging in place and resilience for those with MCI.

---


### 31. [Multitasking Embedding for Embryo Blastocyst Grading Prediction (MEmEBG)](https://arxiv.org/abs/2604.13217)

**<font color=#1a73e8>作者：</font>** Nahid Khoshk Angabini, Mohsen Tajgardan, Mahesh Madhavan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of blastocyst quality is critical for the success of in vitro fertilization (IVF) treatments. Current embryo grading practices primarily rely on visual assessment of morphological features, which introduces subjectivity, inter-embryologist variability, and challenges in standardizing quality assurance. In this study, we propose a multitask embedding-based approach for the automated analysis and prediction of key blastocyst components, including the trophectoderm (TE), inner cell mass (ICM), and blastocyst expansion (EXP). The method leverages biological and physical characteristics extracted from images of day-5 human embryos. A pretrained ResNet-18 architecture, enhanced with an embedding layer, is employed to learn discriminative representations from a limited dataset and to automatically identify TE and ICM regions along with their corresponding grades, structures that are visually similar and inherently difficult to distinguish. Experimental results demonstrate the promise of the multitask embedding approach and potential for robust and consistent blastocyst quality assessment.

---


### 32. [Does Dimensionality Reduction via Random Projections Preserve Landscape Features?](https://arxiv.org/abs/2604.13230)

**<font color=#1a73e8>作者：</font>** Iván Olarte Rodríguez, Anja Jankovic, Thomas Bäck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploratory Landscape Analysis (ELA) provides numerical features for characterizing black-box optimization problems. In high-dimensional settings, however, ELA suffers from sparsity effects, high estimator variance, and the prohibitive cost of computing several feature classes. Dimensionality reduction has therefore been proposed as a way to make ELA applicable in such settings, but it remains unclear whether features computed in reduced spaces still reflect intrinsic properties of the original landscape.
In this work, we investigate the robustness of ELA features under dimensionality reduction via Random Gaussian Embeddings (RGEs). Starting from the same sampled points and objective values, we compute ELA features in projected spaces and compare them to those obtained in the original search space across multiple sample budgets and embedding dimensions.
Our results show that linear random projections often alter the geometric and topological structure relevant to ELA, yielding feature values that are no longer representative of the original problem. While a small subset of features remains comparatively stable, most are highly sensitive to the embedding. Moreover, robustness under projection does not necessarily imply informativeness, as apparently robust features may still reflect projection-induced artifacts rather than intrinsic landscape characteristics.

---


### 33. [Evaluating the Evaluator: Problems with SemEval-2020 Task 1 for Lexical Semantic Change Detection](https://arxiv.org/abs/2604.13232)

**<font color=#1a73e8>作者：</font>** Bach Phan-Tat, Kris Heylen, Dirk Geeraerts 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This discussion paper re-examines SemEval-2020 Task 1, the most influential shared benchmark for lexical semantic change detection, through a three-part evaluative framework: operationalisation, data quality, and benchmark design. First, at the level of operationalisation, we argue that the benchmark models semantic change mainly as gain, loss, or redistribution of discrete senses. While practical for annotation and evaluation, this framing is too narrow to capture gradual, constructional, collocational, and discourse-level change. Also, the gold labels are outcomes of annotation decisions, clustering procedures, and threshold settings, which could potentially limit the validity of the task. Second, at the level of data quality, we show that the benchmark is affected by substantial corpus and preprocessing problems, including OCR noise, malformed characters, truncated sentences, inconsistent lemmatisation, POS-tagging errors, and missed targets. These issues can distort model behaviour, complicate linguistic analysis, and reduce reproducibility. Third, at the level of bench-mark design, we argue the small curated target sets and limited language coverage reduce realism and increase statistical uncertainty. Taken together, these limitations suggest that the benchmark should be treated as a useful but partial test bed rather than a definitive measure of progress. We therefore call for future datasets and shared tasks to adopt broader theories of semantic change, document pre-processing transparently, expand cross-linguistic coverage, and use more realistic evaluation settings. Such steps are necessary for more valid, interpretable, and generalisable progress in lexical semantic change detection

---


### 34. [Neural 3D Reconstruction of Planetary Surfaces from Descent-Phase Wide-Angle Imagery](https://arxiv.org/abs/2604.13235)

**<font color=#1a73e8>作者：</font>** Melonie de Almeida, George Brydon, Divya M. Persaud 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital elevation modeling of planetary surfaces is essential for studying past and ongoing geological processes. Wide-angle imagery acquired during spacecraft descent promises to offer a low-cost option for high-resolution terrain reconstruction. However, accurate 3D reconstruction from such imagery is challenging due to strong radial distortion and limited parallax from vertically descending, predominantly nadir-facing cameras. Conventional multi-view stereo exhibits limited depth range and reduced fidelity under these conditions and also lacks domain-specific priors. We present the first study of modern neural reconstruction methods for planetary descent imaging. We also develop a novel approach that incorporates an explicit neural height field representation, which provides a strong prior since planetary surfaces are generally continuous, smooth, solid, and free from floating objects. This study demonstrates that neural approaches offer a strong and competitive alternative to traditional multi-view stereo (MVS) methods. Experiments on simulated descent sequences over high-fidelity lunar and Mars terrains demonstrate that the proposed approach achieves increased spatial coverage while maintaining satisfactory estimation accuracy.

---


### 35. [A High-Resolution Landscape Dataset for Concept-Based XAI With Application to Species Distribution Models](https://arxiv.org/abs/2604.13240)

**<font color=#1a73e8>作者：</font>** Augustin de la Brosse, Damien Garreau, Thomas Houet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mapping the spatial distribution of species is essential for conservation policy and invasive species management. Species distribution models (SDMs) are the primary tools for this task, serving two purposes: achieving robust predictive performance while providing ecological insights into the driving factors of distribution. However, the increasing complexity of deep learning SDMs has made extracting these insights more challenging. To reconcile these objectives, we propose the first implementation of concept-based Explainable AI (XAI) for SDMs. We leverage the Robust TCAV (Testing with Concept Activation Vectors) methodology to quantify the influence of landscape concepts on model predictions. To enable this, we provide a new open-access landscape concept dataset derived from high-resolution multispectral and LiDAR drone imagery. It includes 653 patches across 15 distinct landscape concepts and 1,450 random reference patches, designed to suit a wide range of species. We demonstrate this approach through a case study of two aquatic insects, Plecoptera and Trichoptera, using two Convolutional Neural Networks and one Vision Transformer. Results show that concept-based XAI helps validate SDMs against expert knowledge while uncovering novel associations that generate new ecological hypotheses. Robust TCAV also provides landscape-level information, useful for policy-making and land management. Code and datasets are publicly available.

---


### 36. [4th Workshop on Maritime Computer Vision (MaCVi): Challenge Overview](https://arxiv.org/abs/2604.13244)

**<font color=#1a73e8>作者：</font>** Benjamin Kiefer, Jan Lukas Augustin, Jon Muhovič 等 55 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The 4th Workshop on Maritime Computer Vision (MaCVi) is organized as part of CVPR 2026. This edition features five benchmark challenges with emphasis on both predictive accuracy and embedded real-time feasibility. This report summarizes the MaCVi 2026 challenge setup, evaluation protocols, datasets, and benchmark tracks, and presents quantitative results, qualitative comparisons, and cross-challenge analyses of emerging method trends. We also include technical reports from top-performing teams to highlight practical design choices and lessons learned across the benchmark suite. Datasets, leaderboards, and challenge resources are available at this https URL.

---


### 37. [Analog Optical Inference on Million-Record Mortgage Data](https://arxiv.org/abs/2604.13251)

**<font color=#1a73e8>作者：</font>** Sofia Berloff, Pavel Koptev, Konstantin Malkov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analog optical computers promise large efficiency gains for machine learning inference, yet no demonstration has moved beyond small-scale image benchmarks. We benchmark the analog optical computer (AOC) digital twin on mortgage approval classification from 5.84 million U.S. HMDA records and separate three sources of accuracy loss. On the original 19 features, the AOC reaches 94.6% balanced accuracy with 5,126 parameters (1,024 optical), compared with 97.9% for XGBoost; the 3.3 percentage-point gap narrows by only 0.5pp when the optical core is widened from 16 to 48 channels, suggesting an architectural rather than hardware limitation. Restricting all models to a shared 127-bit binary encoding drops every model to 89.4--89.6%, with an encoding cost of 8pp for digital models and 5pp for the AOC. Seven calibrated hardware non-idealities impose no measurable penalty. The three resulting layers of limitation (encoding, architecture, hardware fidelity) locate where accuracy is lost and what to improve next.

---


### 38. [Bias-Corrected Adaptive Conformal Inference for Multi-Horizon Time Series Forecasting](https://arxiv.org/abs/2604.13253)

**<font color=#1a73e8>作者：</font>** Ankit Lade, Sai Krishna J., Indar Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive Conformal Inference (ACI) provides distribution-free prediction intervals with asymptotic coverage guarantees for time series under distribution shift. However, ACI only adapts the quantile threshold -- it cannot shift the interval center. When a base forecaster develops persistent bias after a regime change, ACI compensates by widening intervals symmetrically, producing unnecessarily conservative bands. We propose Bias-Corrected ACI (BC-ACI), which augments standard ACI with an online exponentially weighted moving average (EWM) estimate of forecast bias. BC-ACI corrects nonconformity scores before quantile computation and re-centers prediction intervals, addressing the root cause of miscalibration rather than its symptom. An adaptive dead-zone threshold suppresses corrections when estimated bias is indistinguishable from noise, ensuring no degradation on well-calibrated data. In controlled experiments across 688 runs spanning two base models, four synthetic regimes, and three real datasets, BC-ACI reduces Winkler interval scores by 13--17% under mean and compound distribution shifts (Wilcoxon p < 0.001) while maintaining equivalent performance on stationary data (ratio 1.002x). We provide finite-sample analysis showing that coverage guarantees degrade gracefully with bias estimation error.

---


### 39. [Counterfactual Peptide Editing for Causal TCR--pMHC Binding Inference](https://arxiv.org/abs/2604.13256)

**<font color=#1a73e8>作者：</font>** Sanjar Khudoyberdiev, Arman Bekov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural models for TCR-pMHC binding prediction are susceptible to shortcut learning: they exploit spurious correlations in training data -- such as peptide length bias or V-gene co-occurrence -- rather than the physical binding interface. This renders predictions brittle under family-held-out and distance-aware evaluation, where such shortcuts do not transfer. We introduce \emph{Counterfactual Invariant Prediction} (CIP), a training framework that generates biologically constrained counterfactual peptide edits and enforces invariance to edits at non-anchor positions while amplifying sensitivity at MHC anchor residues. CIP augments the base classifier with two auxiliary objectives: (1) an invariance loss penalizing prediction changes under conservative non-anchor substitutions, and (2) a contrastive loss encouraging large prediction changes under anchor-position disruptions. Evaluated on a curated VDJdb-IEDB benchmark under family-held-out, distance-aware, and random splits, CIP achieves AUROC 0.831 and counterfactual consistency (CFC) 0.724 under the challenging family-held-out protocol -- a 39.7\% reduction in shortcut index relative to the unconstrained baseline. Ablations confirm that anchor-aware edit generation is the dominant driver of OOD gains, providing a practical recipe for causally-grounded TCR specificity modeling.

---


### 40. [Rethinking Uncertainty in Segmentation: From Estimation to Decision](https://arxiv.org/abs/2604.13262)

**<font color=#1a73e8>作者：</font>** Saket Maganti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In medical image segmentation, uncertainty estimates are often reported but rarely used to guide decisions. We study the missing step: how uncertainty maps are converted into actionable policies such as accepting, flagging, or deferring predictions. We formulate segmentation as a two-stage pipeline, estimation followed by decision, and show that optimizing uncertainty alone fails to capture most of the achievable safety gains. Using retinal vessel segmentation benchmarks (DRIVE, STARE, CHASE_DB1), we evaluate two uncertainty sources (Monte Carlo Dropout and Test-Time Augmentation) combined with three deferral strategies, and introduce a simple confidence-aware deferral rule that prioritizes uncertain and low-confidence predictions. Our results show that the best method and policy combination removes up to 80 percent of segmentation errors at only 25 percent pixel deferral, while achieving strong cross-dataset robustness. We further show that calibration improvements do not translate to better decision quality, highlighting a disconnect between standard uncertainty metrics and real-world utility. These findings suggest that uncertainty should be evaluated based on the decisions it enables, rather than in isolation.

---


### 41. [Binomial Gradient-Based Meta-Learning for Enhanced Meta-Gradient Estimation](https://arxiv.org/abs/2604.13263)

**<font color=#1a73e8>作者：</font>** Yilang Zhang, Abraham Jaeger Mountain, Bingcong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Meta-learning offers a principled framework leveraging \emph{task-invariant} priors from related tasks, with which \emph{task-specific} models can be fine-tuned on downstream tasks, even with limited data records. Gradient-based meta-learning (GBML) relies on gradient descent (GD) to adapt the prior to a new task. Albeit effective, these methods incur high computational overhead that scales linearly with the number of GD steps. To enhance efficiency and scalability, existing methods approximate the gradient of prior parameters (meta-gradient) via truncated backpropagation, yet suffer large approximation errors. Targeting accurate approximation, this work puts forth binomial GBML (BinomGBML), which relies on a truncated binomial expansion for meta-gradient estimation. This novel expansion endows more information in the meta-gradient estimation via efficient parallel computation. As a running paradigm applied to model-agnostic meta-learning (MAML), the resultant BinomMAML provably enjoys error bounds that not only improve upon existing approaches, but also decay super-exponentially under mild conditions. Numerical tests corroborate the theoretical analysis and showcase boosted performance with slightly increased computational overhead.

---


### 42. [Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size](https://arxiv.org/abs/2604.13275)

**<font color=#1a73e8>作者：</font>** Dikshant Kukreja, Kshitij Sah, Gautam Gupta 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Larger language models become simultaneously better and worse at handling contextual information -- better at ignoring false claims, worse at ignoring irrelevant tokens. We formalize this apparent paradox through the first scaling laws for contextual entrainment, the tendency of models to favor tokens that appeared in context regardless of relevance. Analyzing the Cerebras-GPT (111M-13B) and Pythia (410M-12B) model families, we find entrainment follows predictable power-law scaling, but with opposite trends depending on context type: semantic contexts show decreasing entrainment with scale, while non-semantic contexts show increasing entrainment. Concretely, the largest models are four times more resistant to counterfactual misinformation than the smallest, yet simultaneously twice as prone to copying arbitrary tokens. These diverging trends, which replicate across model families, suggest that semantic filtering and mechanical copying are functionally distinct behaviors that scale in opposition -- scaling alone does not resolve context sensitivity, it reshapes it.

---


### 43. [DroneScan-YOLO: Redundancy-Aware Lightweight Detection for Tiny Objects in UAV Imagery](https://arxiv.org/abs/2604.13278)

**<font color=#1a73e8>作者：</font>** Yann V. Bellec  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial object detection in UAV imagery presents unique challenges due to the high prevalence of tiny objects, adverse environmental conditions, and strict computational constraints. Standard YOLO-based detectors fail to address these jointly: their minimum detection stride of 8 pixels renders sub-32px objects nearly undetectable, their CIoU loss produces zero gradients for non-overlapping tiny boxes, and their architectures contain significant filter redundancy. We propose DroneScan-YOLO, a holistic system contribution that addresses these limitations through four coordinated design choices: (1) increased input resolution of 1280x1280 to maximize spatial detail for tiny objects, (2) RPA-Block, a dynamic filter pruning mechanism based on lazy cosine-similarity updates with a 10-epoch warm-up period, (3) MSFD, a lightweight P2 detection branch at stride 4 adding only 114,592 parameters (+1.1%), and (4) SAL-NWD, a hybrid loss combining Normalized Wasserstein Distance with size-adaptive CIoU weighting, integrated into YOLOv8's TaskAligned assignment pipeline. Evaluated on VisDrone2019-DET, DroneScan-YOLO achieves 55.3% mAP@50 and 35.6% mAP@50-95, outperforming the YOLOv8s baseline by +16.6 and +12.3 points respectively, improving recall from 0.374 to 0.518, and maintaining 96.7 FPS inference speed with only +4.1% parameters. Gains are most pronounced on tiny object classes: bicycle AP@50 improves from 0.114 to 0.328 (+187%), and awning-tricycle from 0.156 to 0.237 (+52%).

---


### 44. [Explainable Fall Detection for Elderly Care via Temporally Stable SHAP in Skeleton-Based Human Activity Recognition](https://arxiv.org/abs/2604.13279)

**<font color=#1a73e8>作者：</font>** Mohammad Saleh, Azadeh Tabatabaei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fall detection in elderly care requires not only accurate classification but also reliable explanations that clinicians can trust. However, existing post-hoc explainability methods, when applied frame-by-frame to sequential data, produce temporally unstable attribution maps that clinicians cannot reliably act upon. To address this issue, we propose a lightweight and explainable framework for skeleton-based fall detection that combines an efficient LSTM model with T-SHAP, a temporally aware post-hoc aggregation strategy that stabilizes SHAP-based feature attributions over contiguous time windows. Unlike standard SHAP, which treats each frame independently, T-SHAP applies a linear smoothing operator to the attribution sequence, reducing high-frequency variance while preserving the theoretical guarantees of Shapley values, including local accuracy and consistency. Experiments on the NTU RGB+D Dataset demonstrate that the proposed framework achieves 94.3% classification accuracy with an end-to-end inference latency below 25 milliseconds, satisfying real-time constraints on mid-range hardware and indicating strong potential for deployment in clinical monitoring scenarios. Quantitative evaluation using perturbation-based faithfulness metrics shows that T-SHAP improves explanation reliability compared to standard SHAP (AUP: 0.89 vs. 0.91) and Grad-CAM (0.82), with consistent improvements observed across five-fold cross-validation, indicating enhanced explanation reliability. The resulting attributions consistently highlight biomechanically relevant motion patterns, including lower-limb instability and changes in spinal alignment, aligning with established clinical observations of fall dynamics and supporting their use as transparent decision aids in long-term care environments

---


### 45. [Optimizing Earth Observation Satellite Schedules under Unknown Operational Constraints: An Active Constraint Acquisition Approach](https://arxiv.org/abs/2604.13283)

**<font color=#1a73e8>作者：</font>** Mohamed-Bachir Belaid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Earth Observation (EO) satellite scheduling (deciding which imaging tasks to perform and when) is a well-studied combinatorial optimization problem. Existing methods typically assume that the operational constraint model is fully specified in advance. In practice, however, constraints governing separation between observations, power budgets, and thermal limits are often embedded in engineering artefacts or high-fidelity simulators rather than in explicit mathematical models. We study EO scheduling under \emph{unknown constraints}: the objective is known, but feasibility must be learned interactively from a binary oracle. Working with a simplified model restricted to pairwise separation and global capacity constraints, we introduce Conservative Constraint Acquisition~(CCA), a domain-specific procedure designed to identify justified constraints efficiently in practice while limiting unnecessary tightening of the learned model. Embedded in the \textsc{Learn\&Optimize} framework, CCA supports an interactive search process that alternates optimization under a learned constraint model with targeted oracle queries. On synthetic instances with up to 50~tasks and dense constraint networks, L\&O improves over a no-knowledge greedy baseline and uses far fewer main oracle queries than a two-phase acquire-then-solve baseline (FAO). For $n\leq 30$, the average gap drops from 65--68\% (Priority Greedy) to 17.7--35.8\% using L\&O. At $n{=}50$, where the CP-SAT reference is the best feasible solution found in 120~s, L\&O improves on FAO on average (17.9\% vs.\ 20.3\%) while using 21.3 main queries instead of 100 and about $5\times$ less execution time.

---


### 46. [Giving Voice to the Constitution: Low-Resource Text-to-Speech for Quechua and Spanish Using a Bilingual Legal Corpus](https://arxiv.org/abs/2604.13288)

**<font color=#1a73e8>作者：</font>** John E. Ortega, Rodolfo Zevallos, Fabricio Carraro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a unified pipeline for synthesizing high-quality Quechua and Spanish speech for the Peruvian Constitution using three state-of-the-art text-to-speech (TTS) architectures: XTTS v2, F5-TTS, and DiFlow-TTS. Our models are trained on independent Spanish and Quechua speech datasets with heterogeneous sizes and recording conditions, and leverage bilingual and multilingual TTS capabilities to improve synthesis quality in both languages. By exploiting cross-lingual transfer, our framework mitigates data scarcity in Quechua while preserving naturalness in Spanish. We release trained checkpoints, inference code, and synthesized audio for each constitutional article, providing a reusable resource for speech technologies in indigenous and multilingual contexts. This work contributes to the development of inclusive TTS systems for political and legal content in low-resource settings.

---


### 47. [Neural Stringology Based Cryptanalysis of EChaCha20](https://arxiv.org/abs/2604.13289)

**<font color=#1a73e8>作者：</font>** Victor Kebande  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern stream ciphers rely on strong diffusion and pseudorandom keystream generation (PKG) to resist cryptanalysis. While conventional evaluation methods such as statistical randomness tests and differential analysis provide important security assurances, they may fail to detect localized structural patterns embedded within cipher outputs. In this paper, a Neural Stringology Cryptanalysis (NSC) framework that combines classical string pattern analysis with machine learning techniques to investigate potential structural anomalies in stream cipher keystreams is introduced. The proposed approach first applies stringology-inspired feature extraction methods such as m-gram frequency analysis, substring recurrence detection, and positional pattern statistics aligned with the internal operations of Add-Rotate-XOR (ARX) based stream ciphers. These extracted features are then analyzed using a neural learning model to identify deviations from expected random behavior and to detect subtle structural patterns that may not be captured by traditional statistical tests. Experimental evaluation is conducted on keystream outputs generated by the EChaCha20 stream cipher under multiple configurations, including reduced round variants. The results demonstrate that the proposed NSC framework can identify distinguishable structural characteristics in the keystream data under controlled conditions, suggesting that integrating machine learning with stringology-based analysis provides a promising complementary methodology for evaluating the structural robustness of modern ARX-based stream cipher designs.

---


### 48. [Physics-informed reservoir characterization from bulk and extreme pressure events with a differentiable simulator](https://arxiv.org/abs/2604.13291)

**<font color=#1a73e8>作者：</font>** Harun Ur Rashid, Mingxin Li, Aleksandra Pachalieva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate characterization of subsurface heterogeneity is challenging but essential for applications such as reservoir pressure management, geothermal energy extraction and CO$_2$, H$_2$, and wastewater injection operations. This challenge becomes especially acute in extreme pressure events, which are rarely observed but can strongly affect operational risk. Traditional history matching and inversion techniques rely on expensive full-physics simulations, making it infeasible to handle uncertainty and extreme events at scale. Purely data-driven models often struggle to maintain physics consistency when dealing with sparse observations, complex geology, and extreme events. To overcome these limitations, we introduce a physics-informed machine learning method that embeds a differentiable subsurface flow simulator directly into neural network training. The network infers heterogeneous permeability fields from limited pressure observations, while training minimizes both permeability and pressure losses through the simulator, enforcing physical consistency. Because the simulator is used only during training, inference remains fast once the model is learned. In an initial test, the proposed method reduces the pressure inference error by half compared with a purely data-driven approach. We then extend the test over eight distinct data scenarios, and in every case, our method produces significantly lower pressure inference errors than the purely data-driven model. We also evaluate our method on extreme events, which represent high-consequence data in the tail of the sample distribution. Similar to the bulk distribution, the physics-informed model maintains higher pressure inference accuracy in the extreme event regimes. Overall, the proposed method enables rapid, physics-consistent subsurface inversion for real-time reservoir characterization and risk-aware decision-making.

---


### 49. [See&Say: Vision Language Guided Safe Zone Detection for Autonomous Package Delivery Drones](https://arxiv.org/abs/2604.13292)

**<font color=#1a73e8>作者：</font>** Mahyar Ghazanfari, Peng Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous drone delivery systems are rapidly advancing, but ensuring safe and reliable package drop-offs remains highly challenging in cluttered urban and suburban environments where accurately identifying suitable package drop zones is critical. Existing approaches typically rely on either geometry-based analysis or semantic segmentation alone, but these methods lack the integrated semantic reasoning required for robust decision-making. To address this gap, we propose See&Say, a novel framework that combines geometric safety cues with semantic perception, guided by a Vision-Language Model (VLM) for iterative refinement. The system fuses monocular depth gradients with open-vocabulary detection masks to produce safety maps, while the VLM dynamically adjusts object category prompts and refines hazard detection across time, enabling reliable reasoning under dynamic conditions during the final delivery phase. When the primary drop-pad is occupied or unsafe, the proposed See&Say also identifies alternative candidate zones for package delivery. We curated a dataset of urban delivery scenarios with moving objects and human activities to evaluate the approach. Experimental results show that See&Say outperforms all baselines, achieving the highest accuracy and IoU for safety map prediction as well as superior performance in alternative drop zone evaluation across multiple thresholds. These findings highlight the promise of VLM-guided segmentation-depth fusion for advancing safe and practical drone-based package delivery.

---


### 50. [PAT-VCM: Plug-and-Play Auxiliary Tokens for Video Coding for Machines](https://arxiv.org/abs/2604.13294)

**<font color=#1a73e8>作者：</font>** Wei Jiang, Wei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing video coding for machines is often trained for a specific downstream task and model. As a result, the compressed representation becomes tightly coupled to the end task, making it difficult to scale across multiple tasks or adapt to model updates. We propose PAT-VCM, a plug-and-play auxiliary-token framework for video coding for machines. PAT-VCM keeps a shared baseline compressed stream and augments it with lightweight task-aware auxiliary tokens, allowing different downstream tasks to recover the information they need without retraining a separate codec for each task. The framework supports three forms of auxiliary information: visual residual tokens, prompt/control tokens, and semantic tokens. We evaluate PAT-VCM on segmentation, depth estimation, and semantic recognition. A shared detection-oriented auxiliary branch provides a reusable first refinement, task-specific visual branches improve segmentation and depth, prompt tokens provide further segmentation gains at negligible bitrate, and semantic tokens achieve strong recognition performance with extremely low overhead. These results suggest that a shared compressed representation, combined with lightweight task-aware auxiliary tokens, is a practical and scalable alternative to tightly task-coupled VCM design.

---


### 51. [Some Theoretical Limitations of t-SNE](https://arxiv.org/abs/2604.13295)

**<font color=#1a73e8>作者：</font>** Rupert Li, Elchanan Mossel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> t-SNE has gained popularity as a dimension reduction technique, especially for visualizing data. It is well-known that all dimension reduction techniques may lose important features of the data. We provide a mathematical framework for understanding this loss for t-SNE by establishing a number of results in different scenarios showing how important features of data are lost by using t-SNE.

---


### 52. [Honeypot Protocol](https://arxiv.org/abs/2604.13301)

**<font color=#1a73e8>作者：</font>** Najmul Hasan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted monitoring, the standard defense in AI control, is vulnerable to adaptive attacks, collusion, and strategic attack selection. All of these exploit the fact that monitoring is passive: it observes model behavior but never probes whether the model would behave differently under different perceived conditions. We introduce the honeypot protocol, which tests for context-dependent behavior by varying only the system prompt across three conditions (evaluation, synthetic deployment, explicit no-monitoring) while holding the task, environment, and scoring identical. We evaluate Claude Opus 4.6 in BashArena across all three conditions in both honest and attack modes. The model achieved 100% main task success and triggered zero side tasks uniformly across conditions, providing a baseline for future comparisons with stronger attack policies and additional models.

---


### 53. [Can Cross-Layer Transcoders Replace Vision Transformer Activations? An Interpretable Perspective on Vision](https://arxiv.org/abs/2604.13304)

**<font color=#1a73e8>作者：</font>** Gerasimos Chatzoudis, Konstantinos D. Polyzos, Zhuowei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding the internal activations of Vision Transformers (ViTs) is critical for building interpretable and trustworthy models. While Sparse Autoencoders (SAEs) have been used to extract human-interpretable features, they operate on individual layers and fail to capture the cross-layer computational structure of Transformers, as well as the relative significance of each layer in forming the last-layer representation. Alternatively, we introduce the adoption of Cross-Layer Transcoders (CLTs) as reliable, sparse, and depth-aware proxy models for MLP blocks in ViTs. CLTs use an encoder-decoder scheme to reconstruct each post-MLP activation from learned sparse embeddings of preceding layers, yielding a linear decomposition that transforms the final representation of ViTs from an opaque embedding into an additive, layer-resolved construction that enables faithful attribution and process-level interpretability. We train CLTs on CLIP ViT-B/32 and ViT-B/16 across CIFAR-100, COCO, and ImageNet-100. We show that CLTs achieve high reconstruction fidelity with post-MLP activations while preserving and even improving, in some cases, CLIP zero-shot classification accuracy. In terms of interpretability, we show that the cross-layer contribution scores provide faithful attribution, revealing that the final representation is concentrated in a smaller set of dominant layer-wise terms whose removal degrades performance and whose retention largely preserves it. These results showcase the significance of adopting CLTs as an alternative interpretable proxy of ViTs in the vision domain.

---


### 54. [Bias at the End of the Score](https://arxiv.org/abs/2604.13305)

**<font color=#1a73e8>作者：</font>** Salma Abdel Magid, Grace Guo, Esin Tureci 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reward models (RMs) are inherently non-neutral value functions designed and trained to encode specific objectives, such as human preferences or text-image alignment. RMs have become crucial components of text-to-image (T2I) generation systems where they are used at various stages for dataset filtering, as evaluation metrics, as a supervisory signal during optimization of parameters, and for post-generation safety and quality filtering of T2I outputs. While specific problems with the integration of RMs into the T2I pipeline have been studied (e.g. reward hacking or mode collapse), their robustness and fairness as scoring functions remains largely unknown. We conduct a large scale audit of RM robustness with respect to demographic biases during T2I model training and generation. We provide quantitative and qualitative evidence that while originally developed as quality measures, RMs encode demographic biases, which cause reward-guided optimization to disproportionately sexualize female image subjects reinforce gender/racial stereotypes, and collapse demographic diversity. These findings highlight shortcomings in current reward models, challenge their reliability as quality metrics, and underscore the need for improved data collection and training procedures to enable more robust scoring.

---


### 55. [Deep Spatially-Regularized and Superpixel-Based Diffusion Learning for Unsupervised Hyperspectral Image Clustering](https://arxiv.org/abs/2604.13307)

**<font color=#1a73e8>作者：</font>** Vutichart Buranasiri, James M. Murphy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An unsupervised framework for hyperspectral image (HSI) clustering is proposed that incorporates masked deep representation learning with diffusion-based clustering, extending the Spatially-Regularized Superpixel-based Diffusion Learning ($S^2DL$) algorithm. Initially, a denoised latent representation of the original HSI is learned via an unsupervised masked autoencoder (UMAE) model with a Vision Transformer backbone. The UMAE takes spatial context and long-range spectral correlations into account and incorporates an efficient pretraining process via masking that utilizes only a small subset of training pixels. In the next stage, the entropy rate superpixel (ERS) algorithm is used to segment the image into superpixels, and a spatially regularized diffusion graph is constructed using Euclidean and diffusion distances within the compressed latent space instead of the HSI space. The proposed algorithm, Deep Spatially-Regularized Superpixel-based Diffusion Learning ($DS^2DL$), leverages more faithful diffusion distances and subsequent diffusion graph construction that better reflect the intrinsic geometry of the underlying data manifold, improving labeling accuracy and clustering quality. Experiments on Botswana and KSC datasets demonstrate the efficacy of $DS^2DL$.

---


### 56. [Threat Modeling and Attack Surface Analysis of IoT-Enabled Controlled Environment Agriculture Systems](https://arxiv.org/abs/2604.13308)

**<font color=#1a73e8>作者：</font>** Andrii Vakhnovskyi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The United States designates Food and Agriculture as one of sixteen critical infrastructure sectors, yet no mandatory cybersecurity requirements exist for agricultural operations and no formal threat model has been published for Controlled Environment Agriculture (CEA) systems. This paper presents the first comprehensive threat model for IoT-enabled CEA, applying STRIDE analysis, MITRE ATT&CK for ICS mapping, and IEC 62443 zone-and-conduit decomposition to a production platform deployed across 30+ commercial facilities in 8 U.S. climate zones. We enumerate 123 unique threats across 25 data-flow-diagram elements spanning 15 communication protocols, 10 of which operate with zero authentication or encryption by design. We identify five novel attack classes unique to AI-driven CEA: stealth destabilization of neural-network-tuned PID controllers, baseline drift poisoning of anomaly detectors, cross-facility propagation via federated transfer learning, adversarial agronomic schedules that exploit crop biology rather than computational models, and reward poisoning of reinforcement-learning energy optimizers. Physical impact analysis quantifies crop loss timelines from minutes (aeroponics) to days, including worker safety hazards from CO2 injection manipulation. A survey of 10 commercial CEA vendors reveals only one CVE ever issued, zero bug bounty programs, and zero IEC 62443 certifications. We propose a defense-in-depth countermeasure framework and recommend Security Level 2 as a minimum baseline.

---


### 57. [Concrete Jungle: Towards Concreteness Paved Contrastive Negative Mining for Compositional Understanding](https://arxiv.org/abs/2604.13313)

**<font color=#1a73e8>作者：</font>** Eun Woo Im, Dhruv Madhwal, Vivek Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models demonstrate remarkable capabilities but often struggle with compositional reasoning, exhibiting vulnerabilities regarding word order and attribute binding. This limitation arises from a scarcity of informative samples needed to differentiate subtle semantic variations during contrastive pretraining. Although hard negative mining offers a promising remedy, existing methods lack explicit mechanisms to dictate which linguistic elements undergo modification. Instead of engineering generative architectures, this study establishes lexical concreteness as a fundamental determinant of negative sample efficacy. Modifying highly concrete terms generates more pronounced structural and visual discrepancies, providing a substantially stronger learning signal. Leveraging this principle, ConcretePlant is proposed to systematically isolate and manipulate perceptually grounded concepts. Analyses of the InfoNCE further reveals a severe gradient imbalance, where easily distinguishable pairs disproportionately overwhelm the optimization process and restrict the bandwidth available for nuanced learning. To resolve this degradation, the Cement loss is formulated utilizing a margin-based approach. By correlating psycholinguistic scores with sample difficulty, this objective dynamically calibrates the penalization applied to individual training pairs. Comprehensive evaluations substantiate these theoretical claims. The integrated framework, designated as Slipform, achieves state-of-the-art accuracy across diverse compositional evaluation benchmarks, general cross-modal retrieval, single and multi label linear probing.

---


### 58. [The Spectrascapes Dataset: Street-view imagery beyond the visible captured using a mobile platform](https://arxiv.org/abs/2604.13315)

**<font color=#1a73e8>作者：</font>** Akshit Gupta, Joris Timmermans, Filip Biljecki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution data in spatial and temporal contexts is imperative for developing climate resilient cities. Current datasets for monitoring urban parameters are developed primarily using manual inspections, embedded-sensing, remote sensing, or standard street-view imagery (RGB). These methods and datasets are often constrained respectively by poor scalability, inconsistent spatio-temporal resolutions, overhead views or low spectral information. We present a novel method and its open implementation: a multi-spectral terrestrial-view dataset that circumvents these limitations. This dataset consists of 17,718 street level multi-spectral images captured with RGB, Near-infrared, and Thermal imaging sensors on bikes, across diverse urban morphologies (village, town, small city, and big urban area) in the Netherlands. Strict emphasis is put on data calibration and quality while also providing the details of our data collection methodology (including the hardware and software details). To the best of our knowledge, Spectrascapes is the first open-access dataset of its kind. Finally, we demonstrate two downstream use-cases enabled using this dataset and provide potential research directions in the machine learning, urban planning and remote sensing domains.

---


### 59. [Beyond Uniform Sampling: Synergistic Active Learning and Input Denoising for Robust Neural Operators](https://arxiv.org/abs/2604.13316)

**<font color=#1a73e8>作者：</font>** Samrendra Roy, Souvik Chakraborty, Syed Bahauddin Alam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators have emerged as fast surrogate models for physics simulations, yet they remain acutely vulnerable to adversarial perturbations, a critical liability for safety-critical digital twin deployments. We present a synergistic defense that combines active learning-based data generation with an input denoising architecture. The active learning component adaptively probes model weaknesses using differential evolution attacks, then generates targeted training data at discovered vulnerability locations while an adaptive smooth-ratio safeguard preserves baseline accuracy. The input denoising component augments the operator architecture with a learnable bottleneck that filters adversarial noise while retaining physics-relevant features. On the viscous Burgers' equation benchmark, the combined approach achieves a 2.04% combined error (1.21% baseline + 0.83% robustness), representing an 87% reduction relative to standard training (15.42% combined) and outperforming both active learning alone (3.42%) and input denoising alone (5.22%). More broadly, our results, combined with cross-architecture vulnerability analysis from prior work, suggest that optimal training data for neural operators is architecture-dependent: because different architectures concentrate sensitivity in distinct input subspaces, uniform sampling cannot adequately cover the vulnerability landscape of all models. These findings have potential implications for the deployment of neural operators in safety-critical energy systems including nuclear reactor monitoring.

---


### 60. [WebXSkill: Skill Learning for Autonomous Web Agents](https://arxiv.org/abs/2604.13318)

**<font color=#1a73e8>作者：</font>** Zhaoyang Wang, Qianhui Wu, Xuchao Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous web agents powered by large language models (LLMs) have shown promise in completing complex browser tasks, yet they still struggle with long-horizon workflows. A key bottleneck is the grounding gap in existing skill formulations: textual workflow skills provide natural language guidance but cannot be directly executed, while code-based skills are executable but opaque to the agent, offering no step-level understanding for error recovery or adaptation. We introduce WebXSkill, a framework that bridges this gap with executable skills, each pairing a parameterized action program with step-level natural language guidance, enabling both direct execution and agent-driven adaptation. WebXSkill operates in three stages: skill extraction mines reusable action subsequences from readily available synthetic agent trajectories and abstracts them into parameterized skills, skill organization indexes skills into a URL-based graph for context-aware retrieval, and skill deployment exposes two complementary modes, grounded mode for fully automated multi-step execution and guided mode where skills serve as step-by-step instructions that the agent follows with its native planning. On WebArena and WebVoyager, WebXSkill improves task success rate by up to 9.8 and 12.9 points over the baseline, respectively, demonstrating the effectiveness of executable skills for web agents. The code is publicly available at this https URL.

---


### 61. [Towards Successful Implementation of Automated Raveling Detection: Effects of Training Data Size, Illumination Difference, and Spatial Shift](https://arxiv.org/abs/2604.13322)

**<font color=#1a73e8>作者：</font>** Xinan Zhang, Haolin Wang, Zhongyu Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Raveling, the loss of aggregates, is a major form of asphalt pavement surface distress, especially on highways. While research has shown that machine learning and deep learning-based methods yield promising results for raveling detection by classification on range images, their performance often degrades in large-scale deployments where more diverse inference data may originate from different runs, sensors, and environmental conditions. This degradation highlights the need of a more generalizable and robust solution for real-world implementation. Thus, the objectives of this study are to 1) identify and assess potential variations that impact model robustness, such as the quantity of training data, illumination difference, and spatial shift; and 2) leverage findings to enhance model robustness under real-world conditions. To this end, we propose RavelingArena, a benchmark designed to evaluate model robustness to variations in raveling detection. Instead of collecting extensive new data, it is built by augmenting an existing dataset with diverse, controlled variations, thereby enabling variation-controlled experiments to quantify the impact of each variation. Results demonstrate that both the quantity and diversity of training data are critical to the accuracy of models, achieving at least a 9.2% gain in accuracy under the most diverse conditions in experiments. Additionally, a case study applying these findings to a multi-year test section in Georgia, U.S., shows significant improvements in year-to-year consistency, laying foundations for future studies on temporal deterioration modeling. These insights provide guidance for more reliable model deployment in raveling detection and other real-world tasks that require adaptability to diverse conditions.

---


### 62. [Right Regions, Wrong Labels: Semantic Label Flips in Segmentation under Correlation Shift](https://arxiv.org/abs/2604.13326)

**<font color=#1a73e8>作者：</font>** Akshit Achara, Yovin Yathathugoda, Nick Byrne 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The robustness of machine learning models can be compromised by spurious correlations between non-causal features in the input data and target labels. A common way to test for such correlations is to train on data where the label is strongly tied to some non-causal cue, then evaluate on examples where that tie no longer holds. This idea is well established for classification tasks, but for semantic segmentation the specific failure modes are not well understood. We show that a model may achieve reasonable overlap while assigning the wrong semantic label, swapping one plausible foreground class for another, even when object boundaries are largely correct. We focus on this semantic label-flip behaviour and quantify it with a simple diagnostic (Flip) that counts how often ground truth foreground pixels are assigned the wrong foreground identity while remaining predicted as foreground. In a setting where category and scene are correlated during training, increasing the correlation consistently widens the gap between common and rare test conditions and increases these within-object label swaps on counterfactual groups. Overall, our results motivate assessing segmentation robustness under distribution shift beyond overlap by decomposing foreground errors into correct pixels, flipped-identity pixels, and missed-to-background pixels. We also propose an entropy-based, ground truth label-free `flip-risk' score, which is computed from foreground identity uncertainty, and show that it can flag flip-prone cases at inference time. Code is available at this https URL.

---


### 63. [SSD-GS: Scattering and Shadow Decomposition for Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2604.13333)

**<font color=#1a73e8>作者：</font>** Iris Zheng, Guojun Tang, Alexander Doronin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SSD-GS, a physically-based relighting framework built upon 3D Gaussian Splatting (3DGS) that achieves high-quality reconstruction and photorealistic relighting under novel lighting conditions. In physically-based relighting, accurately modeling light-material interactions is essential for faithful appearance reproduction. However, existing 3DGS-based relighting methods adopt coarse shading decompositions, either modeling only diffuse and specular reflections or relying on neural networks to approximate shadows and scattering. This leads to limited fidelity and poor physical interpretability, particularly for anisotropic metals and translucent materials. To address these limitations, SSD-GS decomposes reflectance into four components: diffuse, specular, shadow, and subsurface scattering. We introduce a learnable dipole-based scattering module for subsurface transport, an occlusion-aware shadow formulation that integrates visibility estimates with a refinement network, and an enhanced specular component with an anisotropic Fresnel-based model. Through progressive integration of all components during training, SSD-GS effectively disentangles lighting and material properties, even for unseen illumination conditions, as demonstrated on the challenging OLAT dataset. Experiments demonstrate superior quantitative and perceptual relighting quality compared to prior methods and pave the way for downstream tasks, including controllable light source editing and interactive scene relighting. The source code is available at: this https URL.

---


### 64. [SEDTalker: Emotion-Aware 3D Facial Animation Using Frame-Level Speech Emotion Diarization](https://arxiv.org/abs/2604.13335)

**<font color=#1a73e8>作者：</font>** Farzaneh Jafari, Stefano Berretti, Anup Basu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SEDTalker, an emotion-aware framework for speech-driven 3D facial animation that leverages frame-level speech emotion diarization to achieve fine-grained expressive control. Unlike prior approaches that rely on utterance-level or manually specified emotion labels, our method predicts temporally dense emotion categories and intensities directly from speech, enabling continuous modulation of facial expressions over time. The diarized emotion signals are encoded as learned embeddings and used to condition a speech-driven 3D animation model based on a hybrid Transformer-Mamba architecture. This design allows effective disentanglement of linguistic content and emotional style while preserving identity and temporal coherence. We evaluate our approach on a large-scale multi-corpus dataset for speech emotion diarization and on the EmoVOCA dataset for emotional 3D facial animation. Quantitative results demonstrate strong frame-level emotion recognition performance and low geometric and temporal reconstruction errors, while qualitative results show smooth emotion transitions and consistent expression control. These findings highlight the effectiveness of frame-level emotion diarization for expressive and controllable 3D talking head generation.

---


### 65. [MSGS: Multispectral 3D Gaussian Splatting](https://arxiv.org/abs/2604.13340)

**<font color=#1a73e8>作者：</font>** Iris Zheng, Guojun Tang, Alexander Doronin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a multispectral extension to 3D Gaussian Splatting (3DGS) for wavelength-aware view synthesis. Each Gaussian is augmented with spectral radiance, represented via per-band spherical harmonics, and optimized under a dual-loss supervision scheme combining RGB and multispectral signals. To improve rendering fidelity, we perform spectral-to-RGB conversion at the pixel level, allowing richer spectral cues to be retained during optimization. Our method is evaluated on both public and self-captured real-world datasets, demonstrating consistent improvements over the RGB-only 3DGS baseline in terms of image quality and spectral consistency. Notably, it excels in challenging scenes involving translucent materials and anisotropic reflections. The proposed approach maintains the compactness and real-time efficiency of 3DGS while laying the foundation for future integration with physically based shading models.

---


### 66. [AgentSPEX: An Agent SPecification and EXecution Language](https://arxiv.org/abs/2604.13346)

**<font color=#1a73e8>作者：</font>** Pengcheng Wang, Jerry Huang, Jiarui Yao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-model agent systems commonly rely on reactive prompting, in which a single instruction guides the model through an open-ended sequence of reasoning and tool-use steps, leaving control flow and intermediate state implicit and making agent behavior potentially difficult to control. Orchestration frameworks such as LangGraph, DSPy, and CrewAI impose greater structure through explicit workflow definitions, but tightly couple workflow logic with Python, making agents difficult to maintain and modify. In this paper, we introduce AgentSPEX, an Agent SPecification and EXecution Language for specifying LLM-agent workflows with explicit control flow and modular structure, along with a customizable agent harness. AgentSPEX supports typed steps, branching and loops, parallel execution, reusable submodules, and explicit state management, and these workflows execute within an agent harness that provides tool access, a sandboxed virtual environment, and support for checkpointing, verification, and logging. Furthermore, we provide a visual editor with synchronized graph and workflow views for authoring and inspection. We include ready-to-use agents for deep research and scientific research, and we evaluate AgentSPEX on 7 benchmarks. Finally, we show through a user study that AgentSPEX provides a more interpretable and accessible workflow-authoring paradigm than a popular existing agent framework.

---


### 67. [Listening Alone, Understanding Together: Collaborative Context Recovery for Privacy-Aware AI](https://arxiv.org/abs/2604.13348)

**<font color=#1a73e8>作者：</font>** Tanmay Srivastava, Amartya Basu, Shubham Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce CONCORD, a privacy-aware asynchronous assistant-to-assistant (A2A) framework that leverages collaboration between proactive speech-based AI. As agents evolve from reactive to always-listening assistants, they face a core privacy risk (of capturing non-consenting speakers), which makes their social deployment a challenge. To overcome this, we implement CONCORD, which enforces owner-only speech capture via real-time speaker verification, producing a one-sided transcript that incurs missing context but preserves privacy. We demonstrate that CONCORD can safely recover necessary context through (1) spatio-temporal context resolution, (2) information gap detection, and (3) minimal A2A queries governed by a relationship-aware disclosure. Instead of hallucination-prone inferring, CONCORD treats context recovery as a negotiated safe exchange between assistants. Across a multi-domain dialogue dataset, CONCORD achieves 91.4% recall in gap detection, 96% relationship classification accuracy, and 97% true negative rate in privacy-sensitive disclosure decisions. By reframing always-listening AI as a coordination problem between privacy-preserving agents, CONCORD offers a practical path toward socially deployable proactive conversational agents.

---


### 68. [Diffusion Sequence Models for Generative In-Context Meta-Learning of Robot Dynamics](https://arxiv.org/abs/2604.13366)

**<font color=#1a73e8>作者：</font>** Angelo Moroncelli, Matteo Rufolo, Gunes Cagin Aydin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate modeling of robot dynamics is essential for model-based control, yet remains challenging under distributional shifts and real-time constraints. In this work, we formulate system identification as an in-context meta-learning problem and compare deterministic and generative sequence models for forward dynamics prediction. We take a Transformer-based meta-model, as a strong deterministic baseline, and introduce to this setting two complementary diffusion-based approaches: (i) inpainting diffusion (Diffuser), which learns the joint input-observation distribution, and (ii) conditioned diffusion models (CNN and Transformer), which generate future observations conditioned on control inputs. Through large-scale randomized simulations, we analyze performance across in-distribution and out-of-distribution regimes, as well as computational trade-offs relevant for control. We show that diffusion models significantly improve robustness under distribution shift, with inpainting diffusion achieving the best performance in our experiments. Finally, we demonstrate that warm-started sampling enables diffusion models to operate within real-time constraints, making them viable for control applications. These results highlight generative meta-models as a promising direction for robust system identification in robotics.

---


### 69. [A 3D SAM-Based Progressive Prompting Framework for Multi-Task Segmentation of Radiotherapy-induced Normal Tissue Injuries in Limited-Data Settings](https://arxiv.org/abs/2604.13367)

**<font color=#1a73e8>作者：</font>** Caiwen Jiang, Lei Zeng, Wei Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiotherapy-induced normal tissue injury is a clinically important complication, and accurate segmentation of injury regions from medical images could facilitate disease assessment, treatment planning, and longitudinal monitoring. However, automatic segmentation of these lesions remains largely unexplored because of limited voxel-level annotations and substantial heterogeneity across injury types, lesion size, and imaging modality. To address this gap, we curate a dedicated head-and-neck radiotherapy-induced normal tissue injury dataset covering three manifestations: osteoradionecrosis (ORN), cerebral edema (CE), and cerebral radiation necrosis (CRN). We further propose a 3D SAM-based progressive prompting framework for multi-task segmentation in limited-data settings. The framework progressively incorporates three complementary prompts: text prompts for task-aware adaptation, dose-guided box prompts for coarse localization, and click prompts for iterative refinement. A small-target focus loss is introduced to improve local prediction and boundary delineation for small and sparse lesions. Experiments on ORN, CE, and CRN demonstrate that the proposed method achieves reliable segmentation performance across diverse injury types and outperforms state-of-the-art methods.

---


### 70. [Young people's perceptions and recommendations for conversational generative artificial intelligence in youth mental health](https://arxiv.org/abs/2604.13381)

**<font color=#1a73e8>作者：</font>** Adam Poulsen, Ian B. Hickie, Carla Gorban 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational generative artificial intelligence agents (or genAI chatbots) could benefit youth mental health, yet young people's perspectives remain underexplored. We examined the Mental health Intelligence Agent (Mia), a genAI chatbot originally designed for professionals in Australian youth services. Following co-design, 32 young people participated in online workshops exploring their perceptions of genAI chatbots in youth mental health and to develop recommendations for reconceptualising Mia for consumers and integrating it into services. Four themes were developed: (1) Humanising AI without dehumanising care, (2) I need to know what's under the hood, (3) Right tool, right place, right time?, and (4) Making it mine on safe ground. This study offers insights into young people's attitudes, needs, and requirements regarding genAI chatbots in youth mental health, with key implications for service integration. Additionally, by co-designing system requirements, this work informs the ethics, design, development, implementation, and governance of genAI chatbots in youth mental health contexts.

---


### 71. [UniBlendNet: Unified Global, Multi-Scale, and Region-Adaptive Modeling for Ambient Lighting Normalization](https://arxiv.org/abs/2604.13383)

**<font color=#1a73e8>作者：</font>** Jiatao Dai, Wei Dong, Han Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ambient Lighting Normalization (ALN) aims to restore images degraded by complex, spatially varying illumination conditions. Existing methods, such as IFBlend, leverage frequency-domain priors to model illumination variations, but still suffer from limited global context modeling and insufficient spatial adaptivity, leading to suboptimal restoration in challenging regions. In this paper, we propose UniBlendNet, a unified framework for ambient lighting normalization that jointly models global illumination, multi-scale structures, and region-adaptive refinement. Specifically, we enhance global illumination understanding by integrating a UniConvNet-based module to capture long-range dependencies. To better handle complex lighting variations, we introduce a Scale-Aware Aggregation Module (SAAM) that performs pyramid-based multi-scale feature aggregation with dynamic reweighting. Furthermore, we design a mask-guided residual refinement mechanism to enable region-adaptive correction, allowing the model to selectively enhance degraded regions while preserving well-exposed areas. This design effectively improves illumination consistency and structural fidelity under complex lighting conditions. Extensive experiments on the NTIRE Ambient Lighting Normalization benchmark demonstrate that UniBlendNet consistently outperforms the baseline IFBlend and achieves improved restoration quality, while producing visually more natural and stable restoration results.

---


### 72. [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)

**<font color=#1a73e8>作者：</font>** Erik Nordby, Tasha Pais, Aviel Parrack  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear probes can detect when language models produce outputs they "know" are wrong, a capability relevant to both deception and reward hacking. However, single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types. We show that combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge. Across 12 models (0.5B--176B parameters), we find probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81). Geometrically, deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.

---


### 73. [From Prediction to Justification: Aligning Sentiment Reasoning with Human Rationale via Reinforcement Learning](https://arxiv.org/abs/2604.13398)

**<font color=#1a73e8>作者：</font>** Shihao Zhang, Ziwei Wang, Jie Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Aspect-based Sentiment Analysis (ABSA) systems have achieved high accuracy in identifying sentiment polarities, they often operate as "black boxes," lacking the explicit reasoning capabilities characteristic of human affective cognition. Humans do not merely categorize sentiment; they construct causal explanations for their judgments. To bridge this gap, we propose ABSA-R1, a large language model framework designed to mimic this ``reason-before-predict" cognitive process. By leveraging reinforcement learning (RL), ABSA-R1 learns to articulate the why behind the what, generating natural language justifications that ground its sentiment predictions. We introduce a Cognition-Aligned Reward Model (formerly sentiment-aware reward model) that enforces consistency between the generated reasoning path and the final emotional label. Furthermore, inspired by metacognitive monitoring, we implement a performance-driven rejection sampling strategy that selectively targets hard cases where the model's internal reasoning is uncertain or inconsistent. Experimental results on four benchmarks demonstrate that equipping models with this explicit reasoning capability not only enhances interpretability but also yields superior performance in sentiment classification and triplet extraction compared to non-reasoning baselines.

---


### 74. [CausalDisenSeg: A Causality-Guided Disentanglement Framework with Counterfactual Reasoning for Robust Brain Tumor Segmentation Under Missing Modalities](https://arxiv.org/abs/2604.13409)

**<font color=#1a73e8>作者：</font>** Bo Liu, Yulong Zou, Jin Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In clinical practice, the robustness of deep learning models for multimodal brain tumor segmentation is severely compromised by incomplete MRI data. This vulnerability stems primarily from modality bias, where models exploit spurious correlations as shortcuts rather than learning true anatomical structures. Existing feature fusion methods fail to fundamentally eliminate this dependency. To address this, we propose CausalDisenSeg, a novel Structural Causal Model (SCM)-grounded framework that achieves robust segmentation via causality-guided disentanglement and counterfactual reasoning. We reframe the problem as isolating the anatomical Causal Factor from the stylistic Bias Factor. Our framework implements a three-stage causal intervention: (1) Explicit Causal Disentanglement: A Conditional Variational Autoencoder (CVAE) coupled with an HSIC constraint mathematically enforces statistical orthogonality between anatomical and style features. (2) Causal Representation Reinforcement: A Region Causality Module (RCM) explicitly grounds causal features in physical tumor regions. (3) Counterfactual Reasoning: A dual-adversarial strategy actively suppresses the residual Natural Direct Effect (NDE) of the bias, forcing its spatial attention to be mutually exclusive from the causal path. Extensive experiments on the BraTS 2020 dataset demonstrate that CausalDisenSeg significantly outperforms state-of-the-art methods in accuracy and consistency across severe missing-modality scenarios. Furthermore, cross-dataset evaluation on BraTS 2023 under the same protocol yields a state-of-the-art macro-average DSC of 84.49.

---


### 75. [Minimax Optimality and Spectral Routing for Majority-Vote Ensembles under Markov Dependence](https://arxiv.org/abs/2604.13414)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Majority-vote ensembles achieve variance reduction by averaging over diverse, approximately independent base learners. When training data exhibits Markov dependence, as in time-series forecasting, reinforcement learning (RL) replay buffers, and spatial grids, this classical guarantee degrades in ways that existing theory does not fully quantify. We provide a minimax characterization of this phenomenon for discrete classification in a fixed-dimensional Markov setting, together with an adaptive algorithm that matches the rate on a graph-regular subclass. We first establish an information-theoretic lower bound for stationary, reversible, geometrically ergodic chains in fixed ambient dimension, showing that no measurable estimator can achieve excess classification risk better than $\Omega(\sqrt{\Tmix/n})$. We then prove that, on the AR(1) witness subclass underlying the lower-bound construction, dependence-agnostic uniform bagging is provably suboptimal with excess risk bounded below by $\Omega(\Tmix/\sqrt{n})$, exhibiting a $\sqrt{\Tmix}$ algorithmic gap. Finally, we propose \emph{adaptive spectral routing}, which partitions the training data via the empirical Fiedler eigenvector of a dependency graph and achieves the minimax rate $\mathcal{O}(\sqrt{\Tmix/n})$ up to a lower-order geometric cut term on a graph-regular subclass, without knowledge of $\Tmix$. Experiments on synthetic Markov chains, 2D spatial grids, the 128-dataset UCR archive, and Atari DQN ensembles validate the theoretical predictions. Consequences for deep RL target variance, scalability via Nyström approximation, and bounded non-stationarity are developed as supporting material in the appendix.

---


### 76. [DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis](https://arxiv.org/abs/2604.13416)

**<font color=#1a73e8>作者：</font>** Cheng-You Lu, Yi-Shan Hung, Wei-Ling Chi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in radiance fields have enabled photorealistic novel view synthesis. In several domains, large-scale real-world datasets have been developed to support comprehensive benchmarking and to facilitate progress beyond scene-specific reconstruction. However, for distractor-free radiance fields, a large-scale dataset with clean and cluttered images per scene remains lacking, limiting the development. To address this gap, we introduce DF3DV-1K, a large-scale real-world dataset comprising 1,048 scenes, each providing clean and cluttered image sets for benchmarking. In total, the dataset contains 89,924 images captured using consumer cameras to mimic casual capture, spanning 128 distractor types and 161 scene themes across indoor and outdoor environments. A curated subset of 41 scenes, DF3DV-41, is systematically designed to evaluate the robustness of distractor-free radiance field methods under challenging scenarios. Using DF3DV-1K, we benchmark nine recent distractor-free radiance field methods and 3D Gaussian Splatting, identifying the most robust methods and the most challenging scenarios. Beyond benchmarking, we demonstrate an application of DF3DV-1K by fine-tuning a diffusion-based 2D enhancer to improve radiance field methods, achieving average improvements of 0.96 dB PSNR and 0.057 LPIPS on the held-out set (e.g., DF3DV-41) and the On-the-go dataset. We hope DF3DV-1K facilitates the development of distractor-free vision and promotes progress beyond scene-specific approaches.

---


### 77. [Physically-Guided Optical Inversion Enable Non-Contact Side-Channel Attack on Isolated Screens](https://arxiv.org/abs/2604.13419)

**<font color=#1a73e8>作者：</font>** Zhiwen Zheng, Yuheng Qiao, Xiaoshuai Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Noncontact exfiltration of electronic screen content poses a security challenge, with side-channel incursions as the principal vector. We introduce an optical projection side-channel paradigm that confronts two core instabilities: (i) the near-singular Jacobian spectrum of projection mapping breaches Hadamard stability, rendering inversion hypersensitive to perturbations; (ii) irreversible compression in light transport obliterates global semantic cues, magnifying reconstruction ambiguity. Exploiting passive speckle patterns formed by diffuse reflection, our Irradiance Robust Radiometric Inversion Network (IR4Net) fuses a Physically Regularized Irradiance Approximation (PRIrr-Approximation), which embeds the radiative transfer equation in a learnable optimizer, with a contour-to-detail cross-scale reconstruction mechanism that arrests noise propagation. Moreover, an Irreversibility Constrained Semantic Reprojection (ICSR) module reinstates lost global structure through context-driven semantic mapping. Evaluated across four scene categories, IR4Net achieves fidelity beyond competing neural approaches while retaining resilience to illumination perturbations.

---


### 78. [VibeFlow: Versatile Video Chroma-Lux Editing through Self-Supervised Learning](https://arxiv.org/abs/2604.13425)

**<font color=#1a73e8>作者：</font>** Yifan Li, Pei Cheng, Bin Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video chroma-lux editing, which aims to modify illumination and color while preserving structural and temporal fidelity, remains a significant challenge. Existing methods typically rely on expensive supervised training with synthetic paired data. This paper proposes VibeFlow, a novel self-supervised framework that unleashes the intrinsic physical understanding of pre-trained video generation models. Instead of learning color and light transitions from scratch, we introduce a disentangled data perturbation pipeline that enforces the model to adaptively recombine structure from source videos and color-illumination cues from reference images, enabling robust disentanglement in a self-supervised manner. Furthermore, to rectify discretization errors inherent in flow-based models, we introduce Residual Velocity Fields alongside a Structural Distortion Consistency Regularization, ensuring rigorous structural preservation and temporal coherence. Our framework eliminates the need for costly training resources and generalizes in a zero-shot manner to diverse applications, including video relighting, recoloring, low-light enhancement, day-night translation, and object-specific color editing. Extensive experiments demonstrate that VibeFlow achieves impressive visual quality with significantly reduced computational overhead. Our project is publicly available at this https URL.

---


### 79. [Event-Adaptive State Transition and Gated Fusion for RGB-Event Object Tracking](https://arxiv.org/abs/2604.13426)

**<font color=#1a73e8>作者：</font>** Jinlin You, Muyu Li, Xudong Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Vision Mamba-based RGB-Event(RGBE) tracking methods suffer from using static state transition matrices, which fail to adapt to variations in event sparsity. This rigidity leads to imbalanced modeling-underfitting sparse event streams and overfitting dense ones-thus degrading cross-modal fusion robustness. To address these limitations, we propose MambaTrack, a multimodal and efficient tracking framework built upon a Dynamic State Space Model(DSSM). Our contributions are twofold. First, we introduce an event-adaptive state transition mechanism that dynamically modulates the state transition matrix based on event stream density. A learnable scalar governs the state evolution rate, enabling differentiated modeling of sparse and dense event flows. Second, we develop a Gated Projection Fusion(GPF) module for robust cross-modal integration. This module projects RGB features into the event feature space and generates adaptive gates from event density and RGB confidence scores. These gates precisely control the fusion intensity, suppressing noise while preserving complementary information. Experiments show that MambaTrack achieves state-of-the-art performance on the FE108 and FELT datasets. Its lightweight design suggests potential for real-time embedded deployment.

---


### 80. [MaMe & MaRe: Matrix-Based Token Merging and Restoration for Efficient Visual Perception and Synthesis](https://arxiv.org/abs/2604.13432)

**<font color=#1a73e8>作者：</font>** Simin Huo, Ning Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Token compression is crucial for mitigating the quadratic complexity of self-attention mechanisms in Vision Transformers (ViTs), which often involve numerous input tokens. Existing methods, such as ToMe, rely on GPU-inefficient operations (e.g., sorting, scattered writes), introducing overheads that limit their effectiveness. We introduce MaMe, a training-free, differentiable token merging method based entirely on matrix operations, which is GPU-friendly to accelerate ViTs. Additionally, we present MaRe, its inverse operation, for token restoration, forming a MaMe+MaRe pipeline for image synthesis. When applied to pre-trained models, MaMe doubles ViT-B throughput with a 2% accuracy drop. Notably, fine-tuning the last layer with MaMe boosts ViT-B accuracy by 1.0% at 1.1x speed. In SigLIP2-B@512 zero-shot classification, MaMe provides 1.3x acceleration with negligible performance degradation. In video tasks, MaMe accelerates VideoMAE-L by 48.5% on Kinetics-400 with only a 0.84% accuracy loss. Furthermore, MaMe achieves simultaneous improvements in both performance and speed on some tasks. In image synthesis, the MaMe+MaRe pipeline enhances quality while reducing Stable Diffusion v2.1 generation latency by 31%. Collectively, these results demonstrate MaMe's and MaRe's effectiveness in accelerating vision models. The code is available at this https URL}{this https URL.

---


### 81. [WIN-U: Woodbury-Informed Newton-Unlearning as a retain-free Machine Unlearning Framework](https://arxiv.org/abs/2604.13438)

**<font color=#1a73e8>作者：</font>** Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Privacy concerns in LLMs have led to the rapidly growing need to enforce a data's "right to be forgotten". Machine unlearning addresses precisely this task, namely the removal of the influence of some specific data, i.e., the forget set, from a trained model. The gold standard for unlearning is to produce the model that would have been learned on only the rest of the training data, i.e., the retain set. Most existing unlearning methods rely on direct access to the retained data, which may not be practical due to privacy or cost constraints. We propose WIN-U, a retained-data free unlearning framework that requires only second order information for the originally trained model on the full data. The unlearning is performed using a single Newton-style step. Using the Woodbury matrix identity and a generalized Gauss-Newton approximation for the forget set curvature, the WIN-U update recovers the closed-form linear solution and serves as a local second-order approximation to the gold-standard retraining optimum. Extensive experiments on various vision and language benchmarks demonstrate that WIN-U achieves SOTA performance in terms of unlearning efficacy and utility preservation, while being more robust against relearning attacks compared to existing methods. Importantly, WIN-U does not require access to the retained data.

---


### 82. [A KL Lens on Quantization: Fast, Forward-Only Sensitivity for Mixed-Precision SSM-Transformer Models](https://arxiv.org/abs/2604.13440)

**<font color=#1a73e8>作者：</font>** Jason Kong, Nilesh Prasad Pandey, Flavio Ponzina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying Large Language Models (LLMs) on edge devices faces severe computational and memory constraints, limiting real-time processing and on-device intelligence. Hybrid architectures combining Structured State Space Models (SSMs) with transformer-based LLMs offer a balance of efficiency and performance. Aggressive quantization can drastically cut model size and speed up inference, but its uneven effects on different components require careful management. In this work, we propose a lightweight, backpropagation-free, surrogate-based sensitivity analysis framework to identify hybrid SSM-Transformer components most susceptible to quantization-induced degradation. Relying solely on forward-pass metrics, our method avoids expensive gradient computations and retraining, making it suitable for situations where access to in-domain data is limited due to proprietary restrictions or privacy constraints. We also provide a formal analysis showing that the Kullback-Leibler (KL) divergence metric better captures quantization sensitivity for Language modeling tasks than widely adopted alternatives such as mean squared error (MSE) and signal-to-quantization-noise ratio (SQNR). Through extensive experiments on SSM and hybrid architectures, our ablation studies confirm that KL-based rankings align with observed performance drops and outperform alternative metrics. This framework enables the practical deployment of advanced hybrid models on resource-constrained edge devices with minimal accuracy loss. We further validate our approach with real-world on-device profiling on Intel Lunar Lake hardware, demonstrating that KL-guided mixed-precision achieves near-FP16 perplexity with model sizes and throughput competitive with Uniform INT4 on both CPU and GPU execution modes. Code is available at this https URL.

---


### 83. [A Study of Failure Modes in Two-Stage Human-Object Interaction Detection](https://arxiv.org/abs/2604.13448)

**<font color=#1a73e8>作者：</font>** Lemeng Wang, Qinqian Lei, Vidhi Bakshi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-object interaction (HOI) detection aims to detect interactions between humans and objects in images. While recent advances have improved performance on existing benchmarks, their evaluations mainly focus on overall prediction accuracy and provide limited insight into the underlying causes of model failures. In particular, modern models often struggle in complex scenes involving multiple people and rare interaction combinations. In this work, we present a study to better understand the failure modes of two-stage HOI models, which form the basis of many current HOI detection approaches. Rather than constructing a large-scale benchmark, we instead decompose HOI detection into multiple interpretable perspectives and analyze model behavior across these dimensions to study different types of failure patterns. We curate a subset of images from an existing HOI dataset organized by human-object-interaction configurations (e.g., multi-person interactions and object sharing), and analyze model behavior under these configurations to examine different failure modes. This design allows us to analyze how these HOI models behave under different scene compositions and why their predictions fail. Importantly, high overall benchmark performance does not necessarily reflect robust visual reasoning about human-object relationships. We hope that this study can provide useful insights into the limitations of HOI models and offer observations for future research in this area.

---


### 84. [FAST: A Synergistic Framework of Attention and State-space Models for Spatiotemporal Traffic Prediction](https://arxiv.org/abs/2604.13453)

**<font color=#1a73e8>作者：</font>** Xinjin Li, Jinghan Cao, Mengyue Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic forecasting requires modeling complex temporal dynamics and long-range spatial dependencies over large sensor networks. Existing methods typically face a trade-off between expressiveness and efficiency: Transformer-based models capture global dependencies well but suffer from quadratic complexity, while recent selective state-space models are computationally efficient yet less effective at modeling spatial interactions in graph-structured traffic data. We propose FAST, a unified framework that combines attention and state-space modeling for scalable spatiotemporal traffic forecasting. FAST adopts a Temporal-Spatial-Temporal architecture, where temporal attention modules capture both short- and long-term temporal patterns, and a Mamba-based spatial module models long-range inter-sensor dependencies with linear complexity. To better represent heterogeneous traffic contexts, FAST further introduces a learnable multi-source spatiotemporal embedding that integrates historical traffic flow, temporal context, and node-level information, together with a multi-level skip prediction mechanism for hierarchical feature fusion. Experiments on PeMS04, PeMS07, and PeMS08 show that FAST consistently outperforms strong baselines from Transformer-, GNN-, attention-, and Mamba-based families. In particular, FAST achieves the best MAE and RMSE on all three benchmarks, with up to 4.3\% lower RMSE and 2.8\% lower MAE than the strongest baseline, demonstrating a favorable balance between accuracy, scalability, and generalization.

---


### 85. [Outperforming Self-Attention Mechanisms in Solar Irradiance Forecasting via Physics-Guided Neural Networks](https://arxiv.org/abs/2604.13455)

**<font color=#1a73e8>作者：</font>** Mohammed Ezzaldin Babiker Abdullah, Rufaidah Abdallah Ibrahim Mohammed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate Global Horizontal Irradiance (GHI) forecasting is critical for grid stability, particularly in arid regions characterized by rapid aerosol fluctuations. While recent trends favor computationally expensive Transformer-based architectures, this paper challenges the prevailing "complexity-first" paradigm. We propose a lightweight, Physics-Informed Hybrid CNN-BiLSTM framework that prioritizes domain knowledge over architectural depth. The model integrates a Convolutional Neural Network (CNN) for spatial feature extraction with a Bi-Directional LSTM for capturing temporal dependencies. Unlike standard data-driven approaches, our model is explicitly guided by a vector of 15 engineered features including Clear-Sky indices and Solar Zenith Angle - rather than relying solely on raw historical data. Hyperparameters are rigorously tuned using Bayesian Optimization to ensure global optimality. Experimental validation using NASA POWER data in Sudan demonstrates that our physics-guided approach achieves a Root Mean Square Error (RMSE) of 19.53 W/m^2, significantly outperforming complex attention-based baselines (RMSE 30.64 W/m^2). These results confirm a "Complexity Paradox": in high-noise meteorological tasks, explicit physical constraints offer a more efficient and accurate alternative to self-attention mechanisms. The findings advocate for a shift towards hybrid, physics-aware AI for real-time renewable energy management.

---


### 86. [MyoVision: A Mobile Research Tool and NEATBoost-Attention Ensemble Framework for Real Time Chicken Breast Myopathy Detection](https://arxiv.org/abs/2604.13456)

**<font color=#1a73e8>作者：</font>** Chaitanya Pallerla, Siavash Mahmoudi, Dongyi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Woody Breast (WB) and Spaghetti Meat (SM) myopathies significantly impact poultry meat quality, yet current detection methods rely either on subjective manual evaluation or costly laboratory-grade imaging systems. We address the problem of low-cost, non-destructive multi-class myopathy classification using consumer smartphones. MyoVision is introduced as a mobile transillumination imaging framework in which 14-bit RAW images are captured and structural texture descriptors indicative of internal tissue abnormalities are extracted. To classify three categories (Normal, Woody Breast, Spaghetti Meat), we propose a NEATBoost-Attention Ensemble model, which is a neuroevolution-optimized weighted fusion of LightGBM and attention-based MLP models. Hyperparameters are automatically discovered using NeuroEvolution of Augmenting Topologies (NEAT), eliminating manual tuning and enabling architecture diversity for small tabular datasets. On a dataset of 336 fillets collected from a commercial processing facility, our method achieves 82.4% test accuracy (F1 = 0.83), outperforming conventional machine learning and deep learning baselines and matching performance reported by hyperspectral imaging systems costing orders of magnitude more. Beyond classification performance, MyoVision establishes a reproducible mobile RGB-D acquisition pipeline for multimodal meat quality research, demonstrating that consumer-grade imaging can support scalable internal tissue assessment.

---


### 87. [Asymmetric-Loss-Guided Hybrid CNN-BiLSTM-Attention Model for Industrial RUL Prediction with Interpretable Failure Heatmaps](https://arxiv.org/abs/2604.13459)

**<font color=#1a73e8>作者：</font>** Mohammed Ezzaldin Babiker Abdullah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Turbofan engine degradation under sustained operational stress necessitates robust prognostic systems capable of accurately estimating the Remaining Useful Life (RUL) of critical components. Existing deep learning approaches frequently fail to simultaneously capture multi-sensor spatial correlations and long-range temporal dependencies, while standard symmetric loss functions inadequately penalize the safety-critical error of over-estimating residual life. This study proposes a hybrid architecture integrating Twin-Stage One-Dimensional Convolutional Neural Networks (1D-CNN), a Bidirectional Long Short-Term Memory (BiLSTM) network, and a custom Bahdanau Additive Attention mechanism. The model was trained and evaluated on the NASA Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) FD001 sub-dataset employing a zero-leakage preprocessing pipeline, piecewise-linear RUL labeling capped at 130 cycles, and the NASA-specified asymmetric exponential loss function that disproportionately penalizes over-estimation to enforce industrial safety constraints. Experiments on 100 test engines achieved a Root Mean Squared Error (RMSE) of 17.52 cycles and a NASA S-Score of 922.06. Furthermore, extracted attention weight heatmaps provide interpretable, per-engine insights into the temporal progression of degradation, supporting informed maintenance decision-making. The proposed framework demonstrates competitive performance against established baselines and offers a principled approach to safe, interpretable prognostics in industrial settings.

---


### 88. [From Order to Distribution: A Spectral Characterization of Forgetting in Continual Learning](https://arxiv.org/abs/2604.13460)

**<font color=#1a73e8>作者：</font>** Zonghuan Xu, Xingjun Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central challenge in continual learning is forgetting, the loss of performance on previously learned tasks induced by sequential adaptation to new ones. While forgetting has been extensively studied empirically, rigorous theoretical characterizations remain limited. A notable step in this direction is \citet{evron2022catastrophic}, which analyzes forgetting under random orderings of a fixed task collection in overparameterized linear regression. We shift the perspective from order to distribution. Rather than asking how a fixed task collection behaves under random orderings, we study an exact-fit linear regime in which tasks are sampled i.i.d.\ from a task distribution~$\Pi$, and ask how the generating distribution itself governs forgetting. In this setting, we derive an exact operator identity for the forgetting quantity, revealing a recursive spectral structure. Building on this identity, we establish an unconditional upper bound, identify the leading asymptotic term, and, in generic nondegenerate cases, characterize the convergence rate up to constants. We further relate this rate to geometric properties of the task distribution, clarifying what drives slow or fast forgetting in this model.

---


### 89. [Adaptive Unknown Fault Detection and Few-Shot Continual Learning for Condition Monitoring in Ultrasonic Metal Welding](https://arxiv.org/abs/2604.13465)

**<font color=#1a73e8>作者：</font>** Ahmadreza Eslaminia, Kuan-Chieh Lu, Klara Nahrstedt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ultrasonic metal welding (UMW) is widely used in industrial applications but is sensitive to tool wear, surface contamination, and material variability, which can lead to unexpected process faults and unsatisfactory weld quality. Conventional monitoring systems typically rely on supervised learning models that assume all fault types are known in advance, limiting their ability to handle previously unseen process faults. To address this challenge, this paper proposes an adaptive condition monitoring approach that enables unknown fault detection and few-shot continual learning for UMW. Unknown faults are detected by analyzing hidden-layer representations of a multilayer perceptron and leveraging a statistical thresholding strategy. Once detected, the samples from unknown fault types are incorporated into the existing model through a continual learning procedure that selectively updates only the final layers of the network, which enables the model to recognize new fault types while preserving knowledge of existing classes. To accelerate the labeling process, cosine similarity transformation combined with a clustering algorithm groups similar unknown samples, thereby reducing manual labeling effort. Experimental results using a multi-sensor UMW dataset demonstrate that the proposed method achieves 96% accuracy in detecting unseen fault conditions while maintaining reliable classification of known classes. After incorporating a new fault type using only five labeled samples, the updated model achieves 98% testing classification accuracy. These results demonstrate that the proposed approach enables adaptive monitoring with minimal retraining cost and time. The proposed approach provides a scalable solution for continual learning in condition monitoring where new process conditions may constantly emerge over time and is extensible to other manufacturing processes.

---


### 90. [Functional Emotions or Situational Contexts? A Discriminating Test from the Mythos Preview System Card](https://arxiv.org/abs/2604.13466)

**<font color=#1a73e8>作者：</font>** Hiranya V. Peiris  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Claude Mythos Preview system card deploys emotion vectors, sparse autoencoder (SAE) features, and activation verbalisers to study model internals during misaligned behaviour. The two primary toolkits are not jointly reported on the most alignment-relevant episodes. This note identifies two hypotheses that are qualitatively consistent with the published results: that the emotion vectors track functional emotions that causally drive behaviour, or that they are a projection of a richer situational-context structure onto human emotional axes. The hypotheses can be distinguished by a test the system card does not report: applying emotion probes to the strategic concealment episodes where only SAE features are currently documented. If emotion probes show flat activation while SAE features are strongly active, the alignment-relevant structure lies outside the emotion subspace. Which hypothesis is correct determines whether emotion-based monitoring will robustly detect dangerous model behaviour or systematically miss it.

---


### 91. [Universality of Gaussian-Mixture Reverse Kernels in Conditional Diffusion](https://arxiv.org/abs/2604.13470)

**<font color=#1a73e8>作者：</font>** Nafiz Ishtiaque, Syed Arefinul Haque, Kazi Ashraful Alam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that conditional diffusion models whose reverse kernels are finite Gaussian mixtures with ReLU-network logits can approximate suitably regular target distributions arbitrarily well in context-averaged conditional KL divergence, up to an irreducible terminal mismatch that typically vanishes with increasing diffusion horizon. A path-space decomposition reduces the output error to this mismatch plus per-step reverse-kernel errors; assuming each reverse kernel factors through a finite-dimensional feature map, each step becomes a static conditional density approximation problem, solved by composing Norets' Gaussian-mixture theory with quantitative ReLU bounds. Under exact terminal matching the resulting neural reverse-kernel class is dense in conditional KL.

---


### 92. [Computational framework for multistep metabolic pathway design](https://arxiv.org/abs/2604.13471)

**<font color=#1a73e8>作者：</font>** Peter Zhiping Zhang, Jeffrey D. Varner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In silico tools are important for generating novel hypotheses and exploring alternatives in de novo metabolic pathway design. However, while many computational frameworks have been proposed for retrobiosynthesis, few successful examples of algorithm-guided xenobiotic biochemical retrosynthesis have been reported in the literature. Deep learning has improved the quality of synthesis and retrosynthesis in organic chemistry applications. Inspired by this progress, we explored combining deep learning of biochemical transformations with the traditional retrobiosynthetic workflow to improve in silico synthetic metabolic pathway designs. To develop our computational biosynthetic pathway design framework, we assembled metabolic reaction and enzymatic template data from public databases. A data augmentation procedure, adapted from literature, was carried out to enrich the assembled reaction dataset with artificial metabolic reactions generated by enzymatic reaction templates. Two neural network-based pathway ranking models were trained as binary classifiers to distinguish assembled reactions from artificial counterparts; each model output a scalar quantifying the plausibility of a 1-step or 2-step pathway. Combining these two models with enzymatic templates, we built a multistep retrobiosynthesis pipeline and validated it by reproducing some natural and non-natural pathways computationally.

---


### 93. [Bridging MARL to SARL: An Order-Independent Multi-Agent Transformer via Latent Consensus](https://arxiv.org/abs/2604.13472)

**<font color=#1a73e8>作者：</font>** Zijian Zhao, Jing Gao, Sen Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent reinforcement learning (MARL) is widely used to address large joint observation and action spaces by decomposing a centralized control problem into multiple interacting agents. However, such decomposition often introduces additional challenges, including non-stationarity, unstable training, weak coordination, and limited theoretical guarantees. In this paper, we propose the Consensus Multi-Agent Transformer (CMAT), a centralized framework that bridges cooperative MARL to a hierarchical single-agent reinforcement learning (SARL) formulation. CMAT treats all agents as a unified entity and employs a Transformer encoder to process the large joint observation space. To handle the extensive joint action space, we introduce a hierarchical decision-making mechanism in which a Transformer decoder autoregressively generates a high-level consensus vector, simulating the process by which agents reach agreement on their strategies in latent space. Conditioned on this consensus, all agents generate their actions simultaneously, enabling order-independent joint decision making and avoiding the sensitivity to action-generation order in conventional Multi-Agent Transformers (MAT). This factorization allows the joint policy to be optimized using single-agent PPO while preserving expressive coordination through the latent consensus. To evaluate the proposed method, we conduct experiments on benchmark tasks from StarCraft II, Multi-Agent MuJoCo, and Google Research Football. The results show that CMAT achieves superior performance over recent centralized solutions, sequential MARL methods, and conventional MARL baselines. The code for this paper is available at:this https URL .

---


### 94. [Secure and Privacy-Preserving Vertical Federated Learning](https://arxiv.org/abs/2604.13474)

**<font color=#1a73e8>作者：</font>** Shan Jin, Sai Rahul Rachuri, Yizhen Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose a novel end-to-end privacy-preserving framework, instantiated by three efficient protocols for different deployment scenarios, covering both input and output privacy, for the vertically split scenario in federated learning (FL), where features are split across clients and labels are not shared by all parties. We do so by distributing the role of the aggregator in FL into multiple servers and having them run secure multiparty computation (MPC) protocols to perform model and feature aggregation and apply differential privacy (DP) to the final released model. While a naive solution would have the clients delegating the entirety of training to run in MPC between the servers, our optimized solution, which supports purely global and also global-local models updates with privacy-preserving, drastically reduces the amount of computation and communication performed using multiparty computation. The experimental results also show the effectiveness of our protocols.

---


### 95. [Monthly Diffusion v0.9: A Latent Diffusion Model for the First AI-MIP](https://arxiv.org/abs/2604.13481)

**<font color=#1a73e8>作者：</font>** Kyle J. C. Hall, Maria J. Molina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Here, we describe Monthly Diffusion at 1.5-degree grid spacing (MD-1.5 version 0.9), a climate emulator that leverages a spherical Fourier neural operator (SFNO)-inspired Conditional Variational Auto-Encoder (CVAE) architecture to model the evolution of low-frequency internal atmospheric variability using latent diffusion. MDv0.9 was designed to forward-step at monthly mean timesteps in a data-sparse regime, using modest computational requirements. This work describes the motivation behind the architecture design, the MDv0.9 training procedure, and initial results.

---


### 96. [ADP-DiT: Text-Guided Diffusion Transformer for Brain Image Generation in Alzheimer's Disease Progression](https://arxiv.org/abs/2604.13495)

**<font color=#1a73e8>作者：</font>** Juneyong Lee, Geonwoo Baek, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease (AD) progresses heterogeneously across individuals, motivating subject-specific synthesis of follow-up magnetic resonance imaging (MRI) to support progression assessment. While Diffusion Transformers (DiT), an emerging transformer-based diffusion model, offer a scalable backbone for image synthesis, longitudinal AD MRI generation with clinically interpretable control over follow-up time and participant metadata remains underexplored. We present ADP-DiT, an interval-aware, clinically text-conditioned diffusion transformer for longitudinal AD MRI synthesis. ADP-DiT encodes follow-up interval together with multi-domain demographic, diagnostic (CN/MCI/AD), and neuropsychological information as a natural-language prompt, enabling time-specific control beyond coarse diagnostic stages. To inject this conditioning effectively, we use dual text encoders-OpenCLIP for vision-language alignment and T5 for richer clinical-language understanding. Their embeddings are fused into DiT through cross-attention for fine-grained guidance and adaptive layer normalization for global modulation. We further enhance anatomical fidelity by applying rotary positional embeddings to image tokens and performing diffusion in a pre-trained SDXL-VAE latent space to enable efficient high-resolution reconstruction. On 3,321 longitudinal 3T T1-weighted scans from 712 participants (259,038 image slices), ADP-DiT achieves SSIM 0.8739 and PSNR 29.32 dB, improving over a DiT baseline by +0.1087 SSIM and +6.08 dB PSNR while capturing progression-related changes such as ventricular enlargement and shrinking hippocampus. These results suggest that integrating comprehensive, subject-specific clinical conditions with architectures can improve longitudinal AD MRI synthesis.

---


### 97. [Enhancing Mixture-of-Experts Specialization via Cluster-Aware Upcycling](https://arxiv.org/abs/2604.13508)

**<font color=#1a73e8>作者：</font>** Sanghyeok Chu, Pyunghwan Ahn, Gwangmo Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse Upcycling provides an efficient way to initialize a Mixture-of-Experts (MoE) model from pretrained dense weights instead of training from scratch. However, since all experts start from identical weights and the router is randomly initialized, the model suffers from expert symmetry and limited early specialization. We propose Cluster-aware Upcycling, a strategy that incorporates semantic structure into MoE initialization. Our method first partitions the dense model's input activations into semantic clusters. Each expert is then initialized using the subspace representations of its corresponding cluster via truncated SVD, while setting the router's initial weights to the cluster centroids. This cluster-aware initialization breaks expert symmetry and encourages early specialization aligned with the data distribution. Furthermore, we introduce an expert-ensemble self-distillation loss that stabilizes training by providing reliable routing guidance using an ensemble teacher. When evaluated on CLIP ViT-B/32 and ViT-B/16, Cluster-aware Upcycling consistently outperforms existing methods across both zero-shot and few-shot benchmarks. The proposed method also produces more diverse and disentangled expert representations, reduces inter-expert similarity, and leads to more confident routing behavior.

---


### 98. [DiT as Real-Time Rerenderer: Streaming Video Stylization with Autoregressive Diffusion Transformer](https://arxiv.org/abs/2604.13509)

**<font color=#1a73e8>作者：</font>** Hengye Lyu, Zisu Li, Yue Hong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation models has significantly accelerated video generation and related downstream tasks. Among these, video stylization holds important research value in areas such as immersive applications and artistic creation, attracting widespread attention. However, existing diffusion-based video stylization methods struggle to maintain stability and consistency when processing long videos, and their high computational cost and multi-step denoising make them difficult to apply in practical scenarios. In this work, we propose RTR-DiT (DiT as Real-Time Rerenderer), a steaming video stylization framework built upon Diffusion Transformer. We first fine-tune a bidirectional teacher model on a curated video stylization dataset, supporting both text-guided and reference-guided video stylization tasks, and subsequently distill it into a few-step autoregressive model via post-training with Self Forcing and Distribution Matching Distillation. Furthermore, we propose a reference-preserving KV cache update strategy that not only enables stable and consistent processing of long videos, but also supports real-time switching between text prompts and reference images. Experimental results show that RTR-DiT outperforms existing methods in both text-guided and reference-guided video stylization tasks, in terms of quantitative metrics and visual quality, and demonstrates excellent performance in real-time long video stylization and interactive style-switching applications.

---


### 99. [Representation over Routing: Overcoming Surrogate Hacking in Multi-Timescale PPO](https://arxiv.org/abs/2604.13517)

**<font color=#1a73e8>作者：</font>** Jing Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal credit assignment in reinforcement learning has long been a central challenge. Inspired by the multi-timescale encoding of the dopamine system in neurobiology, recent research has sought to introduce multiple discount factors into Actor-Critic architectures, such as Proximal Policy Optimization (PPO), to balance short-term responses with long-term planning. However, this paper reveals that blindly fusing multi-timescale signals in complex delayed-reward tasks can lead to severe algorithmic pathologies. We systematically demonstrate that exposing a temporal attention routing mechanism to policy gradients results in surrogate objective hacking, while adopting gradient-free uncertainty weighting triggers irreversible myopic degeneration, a phenomenon we term the Paradox of Temporal Uncertainty. To address these issues, we propose a Target Decoupling architecture: on the Critic side, we retain multi-timescale predictions to enforce auxiliary representation learning, while on the Actor side, we strictly isolate short-term signals and update the policy based solely on long-term advantages. Rigorous empirical evaluations across multiple independent random seeds in the LunarLander-v2 environment demonstrate that our proposed architecture achieves statistically significant performance improvements. Without relying on hyperparameter hacking, it consistently surpasses the ''Environment Solved'' threshold with minimal variance, completely eliminates policy collapse, and escapes the hovering local optima that trap single-timescale baselines.

---


### 100. [LEGO-MOF: Equivariant Latent Manipulation for Editable, Generative, and Optimizable MOF Design](https://arxiv.org/abs/2604.13520)

**<font color=#1a73e8>作者：</font>** Chaoran Zhang, Guangyao Li, Dongxu Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Metal-organic frameworks (MOFs) are highly promising for carbon capture, yet navigating their vast design space remains challenging. Recent deep generative models enable de novo MOF design but primarily act as feed-forward structure generators. By heavily relying on predefined building block libraries and non-differentiable post-optimization, they fundamentally sever the information flow required for continuous structural editing. Here, we propose a target-driven generative framework focused on continuous structural manipulation. At its core is LinkerVAE, which maps discrete 3D chemical graphs into a continuous, SE(3)-equivariant latent space. This smooth manifold unlocks geometry-aware manipulations, including implicit chemical style transfer and zero-shot isoreticular expansion. Building upon this, we introduce a test-time optimization (TTO) strategy, utilizing an accurate surrogate model to continuously optimize the latent graphs of existing MOFs toward desired properties. This approach systematically enhances carbon capture performance, achieving a striking average relative boost of 147.5% in pure CO2 uptake while strictly preserving structural validity. Integrated with a latent diffusion model and rigid-body assembly for full MOF construction, our framework establishes a scalable, fully differentiable pathway for both the automated discovery, targeted optimization and editing of functional materials.

---


### 101. [C-voting: Confidence-Based Test-Time Voting without Explicit Energy Functions](https://arxiv.org/abs/2604.13521)

**<font color=#1a73e8>作者：</font>** Kenji Kubo, Shunsuke Kamiya, Masanori Koyama 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network models with latent recurrent processing, where identical layers are recursively applied to the latent state, have gained attention as promising models for performing reasoning tasks. A strength of such models is that they enable test-time scaling, where the models can enhance their performance in the test phase without additional training. Models such as the Hierarchical Reasoning Model (HRM) and Artificial Kuramoto Oscillatory Neurons (AKOrN) can facilitate deeper reasoning by increasing the number of recurrent steps, thereby enabling the completion of challenging tasks, including Sudoku, Maze solving, and AGI benchmarks. In this work, we introduce confidence-based voting (C-voting), a test-time scaling strategy designed for recurrent models with multiple latent candidate trajectories. Initializing the latent state with multiple candidates using random variables, C-voting selects the one maximizing the average of top-1 probabilities of the predictions, reflecting the model's confidence. Additionally, it yields 4.9% higher accuracy on Sudoku-hard than the energy-based voting strategy, which is specific to models with explicit energy functions. An essential advantage of C-voting is its applicability: it can be applied to recurrent models without requiring an explicit energy function. Finally, we introduce a simple attention-based recurrent model with randomized initial values named ItrSA++, and demonstrate that when combined with C-voting, it outperforms HRM on Sudoku-extreme (95.2% vs. 55.0%) and Maze (78.6% vs. 74.5%) tasks.

---


### 102. [RiskWebWorld: A Realistic Interactive Benchmark for GUI Agents in E-commerce Risk Management](https://arxiv.org/abs/2604.13531)

**<font color=#1a73e8>作者：</font>** Renqi Chen, Zeyin Tao, Jianming Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) agents show strong capabilities for automating web tasks, but existing interactive benchmarks primarily target benign, predictable consumer environments. Their effectiveness in high-stakes, investigative domains such as authentic e-commerce risk management remains underexplored. To bridge this gap, we present RiskWebWorld, the first highly realistic interactive benchmark for evaluating GUI agents in e-commerce risk management. RiskWebWorld features 1,513 tasks sourced from production risk-control pipelines across 8 core domains, and captures the authentic challenges of risk operations on uncooperative websites, partially environmental hijackments. To support scalable evaluation and agentic reinforcement learning (RL), we further build a Gymnasium-compliant infrastructure that decouples policy planning from environment mechanics. Our evaluation across diverse models reveals a dramatic capability gap: top-tier generalist models achieve 49.1% success, while specialized open-weights GUI models lag at near-total failure. This highlights that foundation model scale currently matters more than zero-shot interface grounding in long-horizon professional tasks. We also demonstrate the viability of our infrastructure through agentic RL, which improves open-source models by 16.2%. These results position RiskWebWorld as a practical testbed for developing robust digital workers.

---


### 103. [Learning Inference Concurrency in DynamicGate MLP Structural and Mathematical Justification](https://arxiv.org/abs/2604.13546)

**<font color=#1a73e8>作者：</font>** Yongil Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional neural networks strictly separate learning and inference because if parameters are updated during inference, outputs become unstable and even the inference function itself is not well defined [1, 2, 3]. This paper shows that DynamicGate MLP structurally permits learning inference concurrency [4, 5]. The key idea is to separate routing (gating) parameters from representation (prediction) parameters, so that the gate can be adapted online while inference stability is preserved, or weights can be selectively updated only within the inactive subspace [4, 5, 6, 7]. We mathematically formalize sufficient conditions for concurrency and show that even under asynchronous or partial updates, the inference output at each time step can always be interpreted as a forward computation of a valid model snapshot [8, 9, 10]. This suggests that DynamicGate MLP can serve as a practical foundation for online adaptive and on device learning systems [11, 12].

---


### 104. [Reconstruction of a 3D wireframe from a single line drawing via generative depth estimation](https://arxiv.org/abs/2604.13549)

**<font color=#1a73e8>作者：</font>** Elton Cao, Hod Lipson  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The conversion of 2D freehand sketches into 3D models remains a pivotal challenge in computer vision, bridging the gap between human creativity and digital fabrication. Traditional line drawing reconstruction relies on brittle symbolic logic, while modern approaches are constrained by rigid parametric modeling, limiting users to predefined CAD primitives. We propose a generative approach by framing reconstruction as a conditional dense depth estimation task. To achieve this, we implement a Latent Diffusion Model (LDM) with a ControlNet-style conditioning framework to resolve the inherent ambiguities of orthographic projections. To support an iterative "sketch-reconstruct-sketch" workflow, we introduce a graph-based BFS masking strategy to simulate partial depth cues. We train and evaluate our approach using a massive dataset of over one million image-depth pairs derived from the ABC Dataset. Our framework demonstrates robust performance across varying shape complexities, providing a scalable pipeline for converting sparse 2D line drawings into dense 3D representations, effectively allowing users to "draw in 3D" without the rigid constraints of traditional CAD.

---


### 105. [AI Powered Image Analysis for Phishing Detection](https://arxiv.org/abs/2604.13555)

**<font color=#1a73e8>作者：</font>** K. Acharya, S. Ale, R. Kadel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Phishing websites now rely heavily on visual imitation-copied logos, similar layouts, and matching colours-to avoid detection by text- and URL-based systems. This paper presents a deep learning approach that uses webpage screenshots for image-based phishing detection. Two vision models, ConvNeXt-Tiny and Vision Transformer (ViT-Base), were tested to see how well they handle visually deceptive phishing pages. The framework covers dataset creation, preprocessing, transfer learning with ImageNet weights, and evaluation using different decision thresholds. The results show that ConvNeXt-Tiny performs the best overall, achieving the highest F1-score at the optimised threshold and running more efficiently than ViT-Base. This highlights the strength of convolutional models for visual phishing detection and shows why threshold tuning is important for real-world deployment. As future work, the curated dataset used in this study will be released to support reproducibility and encourage further research in this area. Unlike many existing studies that primarily report accuracy, this work places greater emphasis on threshold-aware evaluation to better reflect real-world deployment conditions. By examining precision, recall, and F1-score across different decision thresholds, the study identifies operating points that balance detection performance and false-alarm control. In addition, the side-by-side comparison of ConvNeXt-Tiny and ViT-Base under the same experimental setup offers practical insights into how convolutional and transformer-based architectures differ in robustness and computational efficiency for visual phishing detection.

---


### 106. [Parameter-efficient Quantum Multi-task Learning](https://arxiv.org/abs/2604.13560)

**<font color=#1a73e8>作者：</font>** Hevish Cowlessur, Chandra Thapa, Tansu Alpcan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task learning (MTL) improves generalization and data efficiency by jointly learning related tasks through shared representations. In the widely used hard-parameter-sharing setting, a shared backbone is combined with task-specific prediction heads. However, task-specific parameters can grow rapidly with the number of tasks. Therefore, designing multi-task heads that preserve task specialization while improving parameter efficiency remains a key challenge. In Quantum Machine Learning (QML), variational quantum circuits (VQCs) provide a compact mechanism for mapping classical data to quantum states residing in high-dimensional Hilbert spaces, enabling expressive representations within constrained parameter budgets. We propose a parameter-efficient quantum multi-task learning (QMTL) framework that replaces conventional task-specific linear heads with a fully quantum prediction head in a hybrid architecture. The model consists of a VQC with a shared, task-independent quantum encoding stage, followed by lightweight task-specific ansatz blocks enabling localized task adaptation while maintaining compact parameterization. Under a controlled and capacity-matched formulation where the shared representation dimension grows with the number of tasks, our parameter-scaling analysis demonstrates that a standard classical head exhibits quadratic growth, whereas the proposed quantum head parameter cost scales linearly. We evaluate QMTL on three multi-task benchmarks spanning natural language processing, medical imaging, and multimodal sarcasm detection, where we achieve performance comparable to, and in some cases exceeding, classical hard-parameter-sharing baselines while consistently outperforming existing hybrid quantum MTL models with substantially fewer head parameters. We further demonstrate QMTL's executability on noisy simulators and real quantum hardware, illustrating its feasibility.

---


### 107. [ZoomSpec: A Physics-Guided Coarse-to-Fine Framework for Wideband Spectrum Sensing](https://arxiv.org/abs/2604.13568)

**<font color=#1a73e8>作者：</font>** Zhentao Yang, Yixiang Luomei, Zhuoyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wideband spectrum sensing for low-altitude monitoring is critical yet challenging due to heterogeneous protocols,large bandwidths, and non-stationary SNR. Existing data-driven approaches treat spectrograms as natural images,suffering from domain mismatch: they neglect time-frequency resolution constraints and spectral leakage, leading topoor narrowband visibility. This paper proposes ZoomSpec, a physics-guided coarse-to-fine framework integrating signal processing priors with deep learning. We introduce a Log-Space STFT (LS-STFT) to overcome the geometric bottleneck of linear spectrograms, sharpening narrowband structures while maintaining constant relative resolution. A lightweight Coarse Proposal Net (CPN) rapidly screens the full band. To bridge coarse detection and fine recognition, we design an Adaptive Heterodyne Low-Pass (AHLP) module that executes center-frequency aligning, bandwidth-matched filtering, and safe decimation, purifying signals of out-of-band interference. A Fine Recognition Net (FRN) fuses purified time-domain I/Q with spectral magnitude via dual-domain attention to jointly refine temporal boundaries and modulation classification. Evaluations on the SpaceNet real-world dataset demonstrate state-of-the-art 78.1 mAP@0.5:0.95, surpassing existing leaderboard systems with superior stability across diverse modulation bandwidths.

---


### 108. [Radar-Informed 3D Multi-Object Tracking under Adverse Conditions](https://arxiv.org/abs/2604.13571)

**<font color=#1a73e8>作者：</font>** Bingxue Xu, Emil Hedemalm, Ajinkya Khoche 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The challenge of 3D multi-object tracking (3D MOT) is achieving robustness in real-world applications, for example under adverse conditions and maintaining consistency as distance increases. To overcome these challenges, sensor fusion approaches that combine LiDAR, cameras, and radar have emerged. However, existing multi-modal fusion methods usually treat radar as another learned feature inside the network. When the overall model degrades in difficult environmental conditions, the robustness advantages that radar could provide are also reduced. We propose RadarMOT, a radar-informed 3D MOT framework that explicitly uses radar point cloud data as additional observation to refine state estimation and recover detector misses at long ranges. Evaluations on the MAN-TruckScenes dataset show that RadarMOT consistently improves the Average Multi-Object Tracking Accuracy (AMOTA) with absolute 12.7% at long range and 10.3% in adverse weather. The code will be available at this https URL

---


### 109. [SocialMirror: Reconstructing 3D Human Interaction Behaviors from Monocular Videos with Semantic and Geometric Guidance](https://arxiv.org/abs/2604.13581)

**<font color=#1a73e8>作者：</font>** Qi Xia, Peishan Cong, Ziyi Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately reconstructing human behavior in close-interaction scenarios is crucial for enabling realistic virtual interactions in augmented reality, precise motion analysis in sports, and natural collaborative behavior in human-robot tasks. Reliable reconstruction in these contexts significantly enhances the realism and effectiveness of AI-driven interactive applications. However, human reconstruction from monocular videos in close-interaction scenarios remains challenging due to severe mutual occlusions, leading local motion ambiguity, disrupted temporal continuity and spatial relationship error. In this paper, we propose SocialMirror, a diffusion-based framework that integrates semantic and geometric cues to effectively address these issues. Specifically, we first leverage high-level interaction descriptions generated by a vision-language model to guide a semantic-guided motion infiller, hallucinating occluded bodies and resolving local pose ambiguities. Next, we propose a sequence-level temporal refiner that enforces smooth, jitter-free motions, while incorporating geometric constraints during sampling to ensure plausible contact and spatial relationships. Evaluations on multiple interaction benchmarks show that SocialMirror achieves state-of-the-art performance in reconstructing interactive human meshes, demonstrating strong generalization across unseen datasets and in-the-wild scenarios. The code will be released upon publication.

---


### 110. [BenGER: A Collaborative Web Platform for End-to-End Benchmarking of German Legal Tasks](https://arxiv.org/abs/2604.13583)

**<font color=#1a73e8>作者：</font>** Sebastian Nagl, Matthias Grabmair  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) for legal reasoning requires workflows that span task design, expert annotation, model execution, and metric-based evaluation. In practice, these steps are split across platforms and scripts, limiting transparency, reproducibility, and participation by non-technical legal experts. We present the BenGER (Benchmark for German Law) framework, an open-source web platform that integrates task creation, collaborative annotation, configurable LLM runs, and evaluation with lexical, semantic, factual, and judge-based metrics. BenGER supports multi-organization projects with tenant isolation and role-based access control, and can optionally provide formative, reference-grounded feedback to annotators. We will demonstrate a live deployment showing end-to-end benchmark creation and analysis.

---


### 111. [Dehaze-then-Splat: Generative Dehazing with Physics-Informed 3D Gaussian Splatting for Smoke-Free Novel View Synthesis](https://arxiv.org/abs/2604.13589)

**<font color=#1a73e8>作者：</font>** Yuchao Chen, Hanqing Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Dehaze-then-Splat, a two-stage pipeline for multi-view smoke removal and novel view synthesis developed for Track~2 of the NTIRE 2026 3D Restoration and Reconstruction Challenge. In the first stage, we produce pseudo-clean training images via per-frame generative dehazing using Nano Banana Pro, followed by brightness normalization. In the second stage, we train 3D Gaussian Splatting (3DGS) with physics-informed auxiliary losses -- depth supervision via Pearson correlation with pseudo-depth, dark channel prior regularization, and dual-source gradient matching -- that compensate for cross-view inconsistencies inherent in frame-wise generative processing. We identify a fundamental tension in dehaze-then-reconstruct pipelines: per-image restoration quality does not guarantee multi-view consistency, and such inconsistency manifests as blurred renders and structural instability in downstream 3D this http URL analysis shows that MCMC-based densification with early stopping, combined with depth and haze-suppression priors, effectively mitigates these artifacts. On the Akikaze validation scene, our pipeline achieves 20.98\,dB PSNR and 0.683 SSIM for novel view synthesis, a +1.50\,dB improvement over the unregularized baseline.

---


### 112. [VGGT-Segmentor: Geometry-Enhanced Cross-View Segmentation](https://arxiv.org/abs/2604.13596)

**<font color=#1a73e8>作者：</font>** Yulu Gao, Bohao Zhang, Zongheng Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instance-level object segmentation across disparate egocentric and exocentric views is a fundamental challenge in visual understanding, critical for applications in embodied AI and remote collaboration. This task is exceptionally difficult due to severe changes in scale, perspective, and occlusion, which destabilize direct pixel-level matching. While recent geometry-aware models like VGGT provide a strong foundation for feature alignment, we find they often fail at dense prediction tasks due to significant pixel-level projection drift, even when their internal object-level textntion remains consistent. To bridge this gap, we introduce VGGT-Segmentor (VGGT-S), a framework that unifies robust geometric modeling with pixel-accurate semantic segmentation. VGGT-S leverages VGGT's powerful cross-view feature representation and introduces a novel Union Segmentation Head. This head operates in three stages: mask prompt fusion, point-guided prediction, and iterative mask refinement, effectively translating high-level feature alignment into a precise segmentation mask. Furthermore, we propose a single-image self-supervised training strategy that eliminates the need for paired annotations and enables strong generalization. On the Ego-Exo4D benchmark, VGGT-S sets a new state-of-the-art, achieving 67.7% and 68.0% average IoU for Ego to Exo and Exo to Ego tasks, respectively, significantly outperforming prior methods. Notably, our correspondence-free pretrained model surpasses most fully-supervised baselines, demonstrating the effectiveness and scalability of our approach.

---


### 113. [Enhancing Reinforcement Learning for Radiology Report Generation with Evidence-aware Rewards and Self-correcting Preference Learning](https://arxiv.org/abs/2604.13598)

**<font color=#1a73e8>作者：</font>** Qin Zhou, Guoyan Liang, Qianyi Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent reinforcement learning (RL) approaches have advanced radiology report generation (RRG), yet two core limitations persist: (1) report-level rewards offer limited evidence-grounded guidance for clinical faithfulness; and (2) current methods lack an explicit self-improving mechanism to align with clinical preference. We introduce clinically aligned Evidence-aware Self-Correcting Reinforcement Learning (ESC-RL), comprising two key components. First, a Group-wise Evidence-aware Alignment Reward (GEAR) delivers group-wise, evidence-aware feedback. GEAR reinforces consistent grounding for true positives, recovers missed findings for false negatives, and suppresses unsupported content for false positives. Second, a Self-correcting Preference Learning (SPL) strategy automatically constructs a reliable, disease-aware preference dataset from multiple noisy observations and leverages an LLM to synthesize refined reports without human supervision. ESC-RL promotes clinically faithful, disease-aligned reward and supports continual self-improvement during training. Extensive experiments on two public chest X-ray datasets demonstrate consistent gains and state-of-the-art performance.

---


### 114. [Design Space Exploration of Hybrid Quantum Neural Networks for Chronic Kidney Disease](https://arxiv.org/abs/2604.13608)

**<font color=#1a73e8>作者：</font>** Muhammad Kashif, Hanzalah Mohamed Siraj, Nouhaila Innan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid Quantum Neural Networks (HQNNs) have recently emerged as a promising paradigm for near-term quantum machine learning. However, their practical performance strongly depends on design choices such as classical-to-quantum data encoding, quantum circuit architecture, measurement strategy and shots. In this paper, we present a comprehensive design space exploration of HQNNs for Chronic Kidney Disease (CKD) diagnosis. Using a carefully curated and preprocessed clinical dataset, we benchmark 625 different HQNN models obtained by combining five encoding schemes, five entanglement architectures, five measurement strategies, and five different shot settings. To ensure fair and robust evaluation, all models are trained using 10-fold stratified cross-validation and assessed on a test set using a comprehensive set of metrics, including accuracy, area under the curve (AUC), F1-score, and a composite performance score. Our results reveal strong and non-trivial interactions between encoding choices and circuit architectures, showing that high performance does not necessarily require large parameter counts or complex circuits. In particular, we find that compact architectures combined with appropriate encodings (e.g., IQP with Ring entanglement) can achieve the best trade-off between accuracy, robustness, and efficiency. Beyond absolute performance analysis, we also provide actionable insights into how different design dimensions influence learning behavior in HQNNs.

---


### 115. [Golden Handcuffs make safer AI agents](https://arxiv.org/abs/2604.13609)

**<font color=#1a73e8>作者：</font>** Aram Ebtekar, Michael K. Cohen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learners can attain high reward through novel unintended strategies. We study a Bayesian mitigation for general environments: we expand the agent's subjective reward range to include a large negative value $-L$, while the true environment's rewards lie in $[0,1]$. After observing consistently high rewards, the Bayesian policy becomes risk-averse to novel schemes that plausibly lead to $-L$. We design a simple override mechanism that yields control to a safe mentor whenever the predicted value drops below a fixed threshold. We prove two properties of the resulting agent: (i) Capability: using mentor-guided exploration with vanishing frequency, the agent attains sublinear regret against its best mentor. (ii) Safety: no decidable low-complexity predicate is triggered by the optimizing policy before it is triggered by a mentor.

---


### 116. [What Are We Really Measuring? Rethinking Dataset Bias in Web-Scale Natural Image Collections via Unsupervised Semantic Clustering](https://arxiv.org/abs/2604.13610)

**<font color=#1a73e8>作者：</font>** Amir Hossein Saleknia, Mohammad Sabokrou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In computer vision, a prevailing method for quantifying dataset bias is to train a model to distinguish between datasets. High classification accuracy is then interpreted as evidence of meaningful semantic differences. This approach assumes that standard image augmentations successfully suppress low-level, non-semantic cues, and that any remaining performance must therefore reflect true semantic divergence. We demonstrate that this fundamental assumption is flawed within the domain of large-scale natural image collections. High classification accuracy is often driven by resolution-based artifacts, which are structural fingerprints arising from native image resolution distributions and interpolation effects during resizing. These artifacts form robust, dataset-specific signatures that persist despite conventional image corruptions. Through controlled experiments, we show that models achieve strong dataset classification even on non-semantic, procedurally generated images, proving their reliance on superficial cues. To address this issue, we revisit this decades-old idea of dataset separability, but not with supervised classification. Instead, we introduce an unsupervised approach that measures true semantic separability. Our framework directly assesses semantic similarity by clustering semantically-rich features from foundational vision models, deliberately bypassing supervised classification on dataset labels. When applied to major web-scale datasets, the primary focus of this work, the high separability reported by supervised methods largely vanishes, with clustering accuracy dropping to near-chance levels. This reveals that conventional classification-based evaluation systematically overstates semantic bias by an overwhelming margin.

---


### 117. [C2: Scalable Rubric-Augmented Reward Modeling from Binary Preferences](https://arxiv.org/abs/2604.13618)

**<font color=#1a73e8>作者：</font>** Akira Kawabata, Saku Sugawara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-augmented verification guides reward models with explicit evaluation criteria, yielding more reliable judgments than single-model verification. However, most existing methods require costly rubric annotations, limiting scalability. Moreover, we find that rubric generation is vulnerable to a failure of cooperation; low-quality rubrics actively mislead reward models rather than help. Inspired by the principle of cooperative communication, we propose Cooperative yet Critical reward modeling (C2), a framework that significantly improves reward model judgments by having the reward model critically collaborate with a rubric generator trained solely from binary preferences. In C2, we synthesize helpful and misleading rubric pairs by measuring how each rubric shifts the reward model toward or away from the correct preference. Using these contrastive pairs, we train a cooperative rubric generator to propose helpful rubrics, and a critical verifier to assess rubric validity before making its judgment, following only rubrics it deems helpful at inference time. C2 outperforms reasoning reward models trained on the same binary preferences, with gains of up to 6.5 points on RM-Bench and 6.0 points length-controlled win rate on AlpacaEval 2.0. Without external rubric annotations, C2 enables an 8B reward model to match performance achieved with rubrics from a 4$\times$ larger model. Overall, our work demonstrates that eliciting deliberate cooperation in rubric-augmented verification makes reward models more trustworthy in a scalable way.

---


### 118. [Nanomentoring: Investigating How Quickly People Can Help People Learn Feature-Rich Software](https://arxiv.org/abs/2604.13621)

**<font color=#1a73e8>作者：</font>** Ian Drosos, Jo Vermeulen, George Fitzmaurice 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People frequently use online forums to get help from experts to answer questions about feature-rich software. However, they may have to wait minutes, hours, or even days to receive advice. We investigate the potential to leverage experts to provide quicker help. We collected over 200 questions from online forums for two feature-rich software applications and suspected a quarter were short enough to be answered in less than one minute (defined as nanoquestions). We then conducted a study with 28 experts recruited from help forums to confirm this assumption, and explore whether there was a preference between text and audio answers. For more than half of the nanoquestions participants saw, they could give advice that they believed was helpful in under 60 seconds. Finally, we collected feedback about what makes a question quick to answer to inspire the design of future tools for ultra rapid human-to-human help.

---


### 119. [Self-Organizing Maps with Optimized Latent Positions](https://arxiv.org/abs/2604.13622)

**<font color=#1a73e8>作者：</font>** Seiki Ubukata, Akira Notsu, Katsuhiro Honda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-Organizing Maps (SOM) are a classical method for unsupervised learning, vector quantization, and topographic mapping of high-dimensional data. However, existing SOM formulations often involve a trade-off between computational efficiency and a clearly defined optimization objective. Objective-based variants such as Soft Topographic Vector Quantization (STVQ) provide a principled formulation, but their neighborhood-coupled computations become expensive as the number of latent nodes increases. In this paper, we propose Self-Organizing Maps with Optimized Latent Positions (SOM-OLP), an objective-based topographic mapping method that introduces a continuous latent position for each data point. Starting from the neighborhood distortion of STVQ, we construct a separable surrogate local cost based on its local quadratic structure and formulate an entropy-regularized objective based on it. This yields a simple block coordinate descent scheme with closed-form updates for assignment probabilities, latent positions, and reference vectors, while guaranteeing monotonic non-increase of the objective and retaining linear per-iteration complexity in the numbers of data points and latent nodes. Experiments on a synthetic saddle manifold, scalability studies on the Digits and MNIST datasets, and 16 benchmark datasets show that SOM-OLP achieves competitive neighborhood preservation and quantization performance, favorable scalability for large numbers of latent nodes and large datasets, and the best average rank among the compared methods on the benchmark datasets.

---


### 120. [ESCAPE: Episodic Spatial Memory and Adaptive Execution Policy for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2604.13633)

**<font color=#1a73e8>作者：</font>** Jingjing Qian, Zeyuan He, Chen Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coordinating navigation and manipulation with robust performance is essential for embodied AI in complex indoor environments. However, as tasks extend over long horizons, existing methods often struggle due to catastrophic forgetting, spatial inconsistency, and rigid execution. To address these issues, we propose ESCAPE (Episodic Spatial Memory Coupled with an Adaptive Policy for Execution), operating through a tightly coupled perception-grounding-execution workflow. For robust perception, ESCAPE features a Spatio-Temporal Fusion Mapping module to autoregressively construct a depth-free, persistent 3D spatial memory, alongside a Memory-Driven Target Grounding module for precise interaction mask generation. To achieve flexible action, our Adaptive Execution Policy dynamically orchestrates proactive global navigation and reactive local manipulation to seize opportunistic targets. ESCAPE achieves state-of-the-art performance on the ALFRED benchmark, reaching 65.09% and 60.79% success rates in test seen and unseen environments with step-by-step instructions. By reducing redundant exploration, our ESCAPE attains substantial improvements in path-length-weighted metrics and maintains robust performance (61.24% / 56.04%) even without detailed guidance for long-horizon tasks.

---


### 121. [Calibrated Speculative Decoding: Frequency-Guided Candidate Selection for Efficient Inference](https://arxiv.org/abs/2604.13634)

**<font color=#1a73e8>作者：</font>** Xuwen Zhou, Fangxin Liu, Chao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive generation by letting draft tokens bypass full verification, but conventional frameworks suffer from frequent false rejections, particularly when draft models produce semantically correct but lexically divergent outputs. In this paper, we present Calibrated Speculative Decoding (CSD), a training-free framework that recovers valid tokens discarded by standard verification. Guided by the principle of "Frequency-Guided Candidate Selection and Probability-Guarded Acceptance," CSD incorporates two lightweight modules: Online Correction Memory, which aggregates historical rejections to propose recurring divergence patterns as rescue candidates, and Semantic Consistency Gating, which verifies candidate admissibility using probability ratios instead of exact token matching. Our evaluation across diverse large language models demonstrates that CSD outperforms existing methods, achieving a peak throughput speedup of 2.33x. CSD preserves model accuracy across all tasks while further boosting performance on complex reasoning datasets. These results establish CSD as a highly effective, lightweight solution for practical LLM deployments.

---


### 122. [Ordinary Least Squares is a Special Case of Transformer](https://arxiv.org/abs/2604.13656)

**<font color=#1a73e8>作者：</font>** Xiaojun Tan, Yuchen Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The statistical essence of the Transformer architecture has long remained elusive: Is it a universal approximator, or a neural network version of known computational algorithms? Through rigorous algebraic proof, we show that the latter better describes Transformer's basic nature: Ordinary Least Squares (OLS) is a special case of the single-layer Linear Transformer. Using the spectral decomposition of the empirical covariance matrix, we construct a specific parameter setting where the attention mechanism's forward pass becomes mathematically equivalent to the OLS closed-form projection. This means attention can solve the problem in one forward pass, not by iterating. Building upon this prototypical case, we further uncover a decoupled slow and fast memory mechanism within Transformers. Finally, the evolution from our established linear prototype to standard Transformers is discussed. This progression facilitates the transition of the Hopfield energy function from linear to exponential memory capacity, thereby establishing a clear continuity between modern deep architectures and classical statistical inference.

---


### 123. [A Bayesian Framework for Uncertainty-Aware Explanations in Power Quality Disturbance Classification](https://arxiv.org/abs/2604.13658)

**<font color=#1a73e8>作者：</font>** Yinsong Chen, Samson S. Yu, Kashem M. Muttaqi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advanced deep learning methods have shown remarkable success in power quality disturbance (PQD) classification. To enhance model transparency, explainable AI (XAI) techniques have been developed to provide instance-specific interpretations of classifier decisions. However, conventional XAI methods yield deterministic explanations, overlooking uncertainty and limiting reliability in safety-critical applications. This paper proposes a Bayesian explanation framework that models explanation uncertainty by generating a relevance attribution distribution for each instance. This method allows experts to select explanations based on confidence percentiles, thereby tailoring interpretability according to specific disturbance types. Extensive experiments on synthetic and real-world power quality datasets demonstrate that the proposed framework improves the transparency and reliability of PQD classifiers through uncertainty-aware explanations.

---


### 124. [Where Trust Fails: Mapping Location-Data Provenance Risks in Europe](https://arxiv.org/abs/2604.13668)

**<font color=#1a73e8>作者：</font>** Eduardo Brito, Liina Kamm  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> European digital sovereignty and security increasingly depends on whether high-impact decisions can be grounded in location evidence that remains credible under adversarial pressure. This paper frames a cross-sector analysis as a location-data provenance problem: not merely what a device or service reports as location, but whether there is contestable evidence about where and when an asserted event occurred, who or what produced the assertion, and under which audit and retention guarantees. There are observable patterns across democratic processes and the information environment, trade and origin-sensitive supply chains, finance and illicit shipping flows, critical infrastructure and mobility, and harms targeting individuals' private and social domains. In these patterns we see a recurring asymmetry in which locality, presence, routing, or jurisdiction can be asserted cheaply while institutions and affected parties face costly reconstruction when disputes arise. To make this challenge actionable, this paper introduces a compact risk taxonomy that decomposes provenance failures into integrity axes and recurring failure modes, and derives design expectations for next-generation digital trust infrastructure centered on contestability under dispute, while remaining privacy- and rights-compatible. It argues for treating location as a digital primitive that should be represented as evidence-bearing claims rather than self-asserted coordinates, and positions proof-of-location (PoL) mechanisms as a candidate capability layer for producing verifiable presence claims under explicit threat and privacy assumptions. The outcome is a sector-neutral foundation for future architectural work on a next-generation digital trust infrastructure for Europe.

---


### 125. [Optimization with SpotOptim](https://arxiv.org/abs/2604.13672)

**<font color=#1a73e8>作者：</font>** Thomas Bartz-Beielstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The `spotoptim` package implements surrogate-model-based optimization of expensive black-box functions in Python. Building on two decades of Sequential Parameter Optimization (SPO) methodology, it provides a Kriging-based optimization loop with Expected Improvement, support for continuous, integer, and categorical variables, noise-aware evaluation via Optimal Computing Budget Allocation (OCBA), and multi-objective extensions. A steady-state parallelization strategy overlaps surrogate search with objective evaluation on multi-core hardware, and a success-rate-based restart mechanism detects stagnation while preserving the best solution found. The package returns scipy-compatible `OptimizeResult` objects and accepts any scikit-learn-compatible surrogate model. Built-in TensorBoard logging provides real-time monitoring of convergence and surrogate quality. This report describes the architecture and module structure of spotoptim, provides worked examples including neural network hyperparameter tuning, and compares the framework with BoTorch, Optuna, Ray Tune, BOHB, SMAC, and Hyperopt. The package is open-source.

---


### 126. [EMGFlow: Robust and Efficient Surface Electromyography Synthesis via Flow Matching](https://arxiv.org/abs/2604.13685)

**<font color=#1a73e8>作者：</font>** Boxuan Jiang, Chenyun Dai, Can Han  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Deep learning-based surface electromyography (sEMG) gesture recognition is frequently bottlenecked by data scarcity and limited subject diversity. While synthetic data generation via Generative Adversarial Networks (GANs) and diffusion models has emerged as a promising augmentation strategy, these approaches often face challenges regarding training stability or inference efficiency. To bridge this gap, we propose EMGFlow, a conditional sEMG generation framework. To the best of our knowledge, this is the first study to investigate the application of Flow Matching (FM) and continuous-time generative modeling in the sEMG domain. To validate EMGFlow across three benchmark sEMG datasets, we employ a unified evaluation protocol integrating feature-based fidelity, distributional geometry, and downstream utility. Extensive evaluations show that EMGFlow outperforms conventional augmentation and GAN baselines, and provides stronger standalone utility than the diffusion baselines considered here under the train-on-synthetic test-on-real (TSTR) protocol. Furthermore, by optimizing generation dynamics through advanced numerical solvers and targeted time sampling, EMGFlow achieves improved quality-efficiency trade-offs. Taken together, these results suggest that Flow Matching is a promising and efficient paradigm for addressing data bottlenecks in myoelectric control systems. Our code is available at: this https URL.

---


### 127. [Beyond Voxel 3D Editing: Learning from 3D Masks and Self-Constructed Data](https://arxiv.org/abs/2604.13688)

**<font color=#1a73e8>作者：</font>** Yizhao Xu, Hongyuan Zhu, Caiyun Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D editing refers to the ability to apply local or global modifications to 3D assets. Effective 3D editing requires maintaining semantic consistency by performing localized changes according to prompts, while also preserving local invariance so that unchanged regions remain consistent with the original. However, existing approaches have significant limitations: multi-view editing methods incur losses when projecting back to 3D, while voxel-based editing is constrained in both the regions that can be modified and the scale of modifications. Moreover, the lack of sufficiently large editing datasets for training and evaluation remains a challenge. To address these challenges, we propose a Beyond Voxel 3D Editing (BVE) framework with a self-constructed large-scale dataset specifically tailored for 3D editing. Building upon this dataset, our model enhances a foundational image-to-3D generative architecture with lightweight, trainable modules, enabling efficient injection of textual semantics without the need for expensive full-model retraining. Furthermore, we introduce an annotation-free 3D masking strategy to preserve local invariance, maintaining the integrity of unchanged regions during editing. Extensive experiments demonstrate that BVE achieves superior performance in generating high-quality, text-aligned 3D assets, while faithfully retaining the visual characteristics of the original input.

---


### 128. [Med-CAM: Minimal Evidence for Explaining Medical Decision Making](https://arxiv.org/abs/2604.13695)

**<font color=#1a73e8>作者：</font>** Pirzada Suhail, Aditya Anand, Amit Sethi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable and interpretable decision-making is essential in medical imaging, where diagnostic outcomes directly influence patient care. Despite advances in deep learning, most medical AI systems operate as opaque black boxes, providing little insight into why a particular diagnosis was reached. In this paper, we introduce Med-CAM, a framework for generating minimal and sharp maps as evidence-based explanations for Medical decision making via Classifier Activation Matching. Med-CAM trains a segmentation network from scratch to produce a mask that highlights the minimal evidence critical to model's decision for any seen or unseen image. This ensures that the explanation is both faithful to the network's behaviour and interpretable to clinicians. Experiments show, unlike prior spatial explanation methods, such as Grad-CAM and attention maps, which yield only fuzzy regions of relative importance, Med-CAM with its superior spatial awareness to shapes, textures, and boundaries, delivers conclusive, evidence-based explanations that faithfully replicate the model's prediction for any given image. By explicitly constraining explanations to be compact, consistent with model activations, and diagnostic alignment, Med-CAM advances transparent AI to foster clinician understanding and trust in high-stakes medical applications such as pathology and radiology.

---


### 129. [Learning the Cue or Learning the Word? Analyzing Generalization in Metaphor Detection for Verbs](https://arxiv.org/abs/2604.13713)

**<font color=#1a73e8>作者：</font>** Sinan Kurtyigit, Sabine Schulte im Walde, Alexander Fraser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metaphor detection models achieve strong benchmark performance, yet it remains unclear whether this reflects transferable generalization or lexical memorization. To address this, we analyze generalization in metaphor detection through RoBERTa, the shared backbone of many state-of-the-art systems, focusing on English verbs using the VU Amsterdam Metaphor Corpus. We introduce a controlled lexical hold-out setup where all instances of selected target lemmas are strictly excluded from fine-tuning, and compare predictions on these Held-out lemmas against Exposed lemmas (verbs seen during fine-tuning). While the model performs best on Exposed lemmas, it maintains robust performance on Held-out lemmas. Further analysis reveals that sentence context alone is sufficient to match full-model performance on Held-out lemmas, whereas static verb-level embeddings are not. Together, these results suggest that generalization is primarily driven by "learning the cue" (transferable contextual patterns), while "learning the word" (verb-specific memorization) provides an additive boost when lexical exposure is available.

---


### 130. [Granularity-Aware Transfer for Tree Instance Segmentation in Synthetic and Real Forests](https://arxiv.org/abs/2604.13722)

**<font color=#1a73e8>作者：</font>** Pankaj Deoli, Atef Tej, Anmol Ashri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the challenge of synthetic-to-real transfer in forestry perception where real data have only coarse Tree labels while synthetic data provide fine-grained trunk/crown annotations. We introduce MGTD, a mixed-granularity dataset with 53k synthetic and 3.6k real images, and a four-stage protocol isolating domain shift and granularity mismatch. Our core contribution is granularity-aware distillation, which transfers structural priors from fine-grained synthetic teachers to a coarse-label student via logit-space merging and mask unification. Experiments show consistent mask AP gains, especially for small/distant trees, establishing a testbed for Sim-Real transfer under label granularity constraints.

---


### 131. [Physics-Informed Neural Networks for Solving Derivative-Constrained PDEs](https://arxiv.org/abs/2604.13723)

**<font color=#1a73e8>作者：</font>** Kentaro Hoshisashi, Carolyn E Phelan, Paolo Barucca  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) recast PDE solving as an optimisation problem in function space by minimising a residual-based objective, yet many applications require additional derivative-based relations that are just as fundamental as the governing equations. In this paper, we present Derivative-Constrained PINNs (DC-PINNs), a general framework that treats constrained PDE solving as an optimisation guided by a minimum objective function criterion where the physics resides in the minimum principle. DC-PINNs embed general nonlinear constraints on states and derivatives, e.g., bounds, monotonicity, convexity, incompressibility, computed efficiently via automatic differentiation, and they employ self-adaptive loss balancing to tune the influence of each objective, reducing reliance on manual hyperparameters and problem-specific architectures. DC-PINNs consistently reduce constraint violations and improve physical fidelity versus baseline PINN variants, representative hard-constraint formulations on benchmarks, including heat diffusion with bounds, financial volatilities with arbitrage-free, and fluid flow with vortices shed. Explicitly encoding derivative constraints stabilises training and steers optimisation toward physically admissible minima even when the PDE residual alone is small, providing reliable solutions of constrained PDEs grounded in energy minimum principles.

---


### 132. [ReConText3D: Replay-based Continual Text-to-3D Generation](https://arxiv.org/abs/2604.13730)

**<font color=#1a73e8>作者：</font>** Muhammad Ahmed Ullah Khan, Muhammad Haris Bin Amir, Didier Stricker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual learning enables models to acquire new knowledge over time while retaining previously learned capabilities. However, its application to text-to-3D generation remains unexplored. We present ReConText3D, the first framework for continual text-to-3D generation. We first demonstrate that existing text-to-3D models suffer from catastrophic forgetting under incremental training. ReConText3D enables generative models to incrementally learn new 3D categories from textual descriptions while preserving the ability to synthesize previously seen assets. Our method constructs a compact and diverse replay memory through text-embedding k-Center selection, allowing representative rehearsal of prior knowledge without modifying the underlying architecture. To systematically evaluate continual text-to-3D learning, we introduce Toys4K-CL, a benchmark derived from the Toys4K dataset that provides balanced and semantically diverse class-incremental splits. Extensive experiments on the Toys4K-CL benchmark show that ReConText3D consistently outperforms all baselines across different generative backbones, maintaining high-quality generation for both old and new classes. To the best of our knowledge, this work establishes the first continual learning framework and benchmark for text-to-3D generation, opening a new direction for incremental 3D generative modeling. Project page is available at: this https URL.

---


### 133. [Doc-V*:Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA](https://arxiv.org/abs/2604.13731)

**<font color=#1a73e8>作者：</font>** Yuanlei Zheng, Pei Fu, Hang Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-page Document Visual Question Answering requires reasoning over semantics, layouts, and visual elements in long, visually dense documents. Existing OCR-free methods face a trade-off between capacity and precision: end-to-end models scale poorly with document length, while visual retrieval-based pipelines are brittle and passive. We propose Doc-$V^*$, an \textbf{OCR-free agentic} framework that casts multi-page DocVQA as sequential evidence aggregation. Doc-$V^*$ begins with a thumbnail overview, then actively navigates via semantic retrieval and targeted page fetching, and aggregates evidence in a structured working memory for grounded reasoning. Trained by imitation learning from expert trajectories and further optimized with Group Relative Policy Optimization, Doc-$V^*$ balances answer accuracy with evidence-seeking efficiency. Across five benchmarks, Doc-$V^*$ outperforms open-source baselines and approaches proprietary models, improving out-of-domain performance by up to \textbf{47.9\%} over RAG baseline. Other results reveal effective evidence aggregation with selective attention, not increased input pages.

---


### 134. [Jump-Start Reinforcement Learning with Vision-Language-Action Regularization](https://arxiv.org/abs/2604.13733)

**<font color=#1a73e8>作者：</font>** Angelo Moroncelli, Roberto Zanetti, Marco Maccarini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) enables high-frequency, closed-loop control for robotic manipulation, but scaling to long-horizon tasks with sparse or imperfect rewards remains difficult due to inefficient exploration and poor credit assignment. Vision-Language-Action (VLA) models leverage large-scale multimodal pretraining to provide generalist, task-level reasoning, but current limitations hinder their direct use in fast and precise manipulation. In this paper, we propose Vision-Language-Action Jump-Starting (VLAJS), a method that bridges sparse VLA guidance with on-policy RL to improve exploration and learning efficiency. VLAJS treats VLAs as transient sources of high-level action suggestions that bias early exploration and improve credit assignment, while preserving the high-frequency, state-based control of RL. Our approach augments Proximal Policy Optimization (PPO) with a directional action-consistency regularization that softly aligns the RL agent's actions with VLA guidance during early training, without enforcing strict imitation, requiring demonstrations, or relying on continuous teacher queries. VLA guidance is applied sparsely and annealed over time, allowing the agent to adapt online and ultimately surpass the guiding policy. We evaluate VLAJS on six challenging manipulation tasks: lifting, pick-and-place, peg reorientation, peg insertion, poking, and pushing in simulation, and validate a subset on a real Franka Panda robot. VLAJS consistently outperforms PPO and distillation-style baselines in sample efficiency, reducing required environment interactions by over 50% in several tasks. Real-world experiments demonstrate zero-shot sim-to-real transfer and robust execution under clutter, object variation, and external perturbations.

---


### 135. [Spectral Thompson sampling](https://arxiv.org/abs/2604.13739)

**<font color=#1a73e8>作者：</font>** Tomas Kocak, Michal Valko, Remi Munos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Thompson Sampling (TS) has attracted a lot of interest due to its good empirical performance, in particular in the computational advertising. Though successful, the tools for its performance analysis appeared only recently. In this paper, we describe and analyze SpectralTS algorithm for a bandit problem, where the payoffs of the choices are smooth given an underlying graph. In this setting, each choice is a node of a graph and the expected payoffs of the neighboring nodes are assumed to be similar. Although the setting has application both in recommender systems and advertising, the traditional algorithms would scale poorly with the number of choices. For that purpose we consider an effective dimension d, which is small in real-world graphs. We deliver the analysis showing that the regret of SpectralTS scales as d*sqrt(T ln N) with high probability, where T is the time horizon and N is the number of choices. Since a d*sqrt(T ln N) regret is comparable to the known results, SpectralTS offers a computationally more efficient alternative. We also show that our algorithm is competitive on both synthetic and real-world data.

---


### 136. [Online learning with noisy side observations](https://arxiv.org/abs/2604.13740)

**<font color=#1a73e8>作者：</font>** Tomáš Kocák, Gergely Neu, Michal Valko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new partial-observability model for online learning problems where the learner, besides its own loss, also observes some noisy feedback about the other actions, depending on the underlying structure of the problem. We represent this structure by a weighted directed graph, where the edge weights are related to the quality of the feedback shared by the connected nodes. Our main contribution is an efficient algorithm that guarantees a regret of $\widetilde{O}(\sqrt{\alpha^* T})$ after $T$ rounds, where $\alpha^*$ is a novel graph property that we call the effective independence number. Our algorithm is completely parameter-free and does not require knowledge (or even estimation) of $\alpha^*$. For the special case of binary edge weights, our setting reduces to the partial-observability models of Mannor and Shamir (2011) and Alon et al. (2013) and our algorithm recovers the near-optimal regret bounds.

---


### 137. [ClipGStream: Clip-Stream Gaussian Splatting for Any Length and Any Motion Multi-View Dynamic Scene Reconstruction](https://arxiv.org/abs/2604.13746)

**<font color=#1a73e8>作者：</font>** Jie Liang, Jiahao Wu, Chao Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic 3D scene reconstruction is essential for immersive media such as VR, MR, and XR, yet remains challenging for long multi-view sequences with large-scale motion. Existing dynamic Gaussian approaches are either Frame-Stream, offering scalability but poor temporal stability, or Clip, achieving local consistency at the cost of high memory and limited sequence length. We propose ClipGStream, a hybrid reconstruction framework that performs stream optimization at the clip level rather than the frame level. The sequence is divided into short clips, where dynamic motion is modeled using clip-independent spatio-temporal fields and residual anchor compensation to capture local variations efficiently, while inter-clip inherited anchors and decoders maintain structural consistency across clips. This Clip-Stream design enables scalable, flicker-free reconstruction of long dynamic videos with high temporal coherence and reduced memory overhead. Extensive experiments demonstrate that ClipGStream achieves state-of-the-art reconstruction quality and efficiency. The project page is available at: this https URL

---


### 138. [Rethinking AI Hardware: A Three-Layer Cognitive Architecture for Autonomous Agents](https://arxiv.org/abs/2604.13757)

**<font color=#1a73e8>作者：</font>** Li Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The next generation of autonomous AI systems will be constrained not only by model capability, but by how intelligence is structured across heterogeneous hardware. Current paradigms -- cloud-centric AI, on-device inference, and edge-cloud pipelines -- treat planning, reasoning, and execution as a monolithic process, leading to unnecessary latency, energy consumption, and fragmented behavioral continuity. We introduce the Tri-Spirit Architecture, a three-layer cognitive framework that decomposes intelligence into planning (Super Layer), reasoning (Agent Layer), and execution (Reflex Layer), each mapped to distinct compute substrates and coordinated via an asynchronous message bus. We formalize the system with a parameterized routing policy, a habit-compilation mechanism that promotes repeated reasoning paths into zero-inference execution policies, a convergent memory model, and explicit safety constraints. We evaluate the architecture in a reproducible simulation of 2000 synthetic tasks against cloud-centric and edge-only baselines. Tri-Spirit reduces mean task latency by 75.6 percent and energy consumption by 71.1 percent, while decreasing LLM invocations by 30 percent and enabling 77.6 percent offline task completion. These results suggest that cognitive decomposition, rather than model scaling alone, is a primary driver of system-level efficiency in AI hardware.

---


### 139. [Design and Behavior of Sparse Mixture-of-Experts Layers in CNN-based Semantic Segmentation](https://arxiv.org/abs/2604.13761)

**<font color=#1a73e8>作者：</font>** Svetlana Pavlitska, Haixi Fan, Konstantin Ditschuneit 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse mixture-of-experts (MoE) layers have been shown to substantially increase model capacity without a proportional increase in computational cost and are widely used in transformer architectures, where they typically replace feed-forward network blocks. In contrast, integrating sparse MoE layers into convolutional neural networks (CNNs) remains inconsistent, with most prior work focusing on fine-grained MoEs operating at the filter or channel levels. In this work, we investigate a coarser, patch-wise formulation of sparse MoE layers for semantic segmentation, where local regions are routed to a small subset of convolutional experts. Through experiments on the Cityscapes and BDD100K datasets using encoder-decoder and backbone-based CNNs, we conduct a design analysis to assess how architectural choices affect routing dynamics and expert specialization. Our results demonstrate consistent, architecture-dependent improvements (up to +3.9 mIoU) with little computational overhead, while revealing strong design sensitivity. Our work provides empirical insights into the design and internal dynamics of sparse MoE layers in CNN-based dense prediction. Our code is available at this https URL.

---


### 140. [Soft $Q(λ)$: A multi-step off-policy method for entropy regularised reinforcement learning using eligibility traces](https://arxiv.org/abs/2604.13780)

**<font color=#1a73e8>作者：</font>** Pranav Mahajan, Ben Seymour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Soft Q-learning has emerged as a versatile model-free method for entropy-regularised reinforcement learning, optimising for returns augmented with a penalty on the divergence from a reference policy. Despite its success, the multi-step extensions of soft Q-learning remain relatively unexplored and limited to on-policy action sampling under the Boltzmann policy. In this brief research note, we first present a formal $n$-step formulation for soft Q-learning and then extend this framework to the fully off-policy case by introducing a novel Soft Tree Backup operator. Finally, we unify these developments into Soft $Q(\lambda)$, an elegant online, off-policy, eligibility trace framework that allows for efficient credit assignment under arbitrary behaviour policies. Our derivations propose a model-free method for learning entropy-regularised value functions that can be utilised in future empirical experiments.

---


### 141. [Temporally Consistent Long-Term Memory for 3D Single Object Tracking](https://arxiv.org/abs/2604.13789)

**<font color=#1a73e8>作者：</font>** Jaejoon Yoo, SuBeen Lee, Yerim Jeon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Single Object Tracking (3D-SOT) aims to localize a target object across a sequence of LiDAR point clouds, given its 3D bounding box in the first frame. Recent methods have adopted a memory-based approach to utilize previously observed features of the target object, but remain limited to only a few recent frames. This work reveals that their temporal capacity is fundamentally constrained to short-term context due to severe temporal feature inconsistency and excessive memory overhead. To this end, we propose a robust long-term 3D-SOT framework, ChronoTrack, which preserves the temporal feature consistency while efficiently aggregating the diverse target features via long-term memory. Based on a compact set of learnable memory tokens, ChronoTrack leverages long-term information through two complementary objectives: a temporal consistency loss and a memory cycle consistency loss. The former enforces feature alignment across frames, alleviating temporal drift and improving the reliability of proposed long-term memory. In parallel, the latter encourages each token to encode diverse and discriminative target representations observed throughout the sequence via memory-point-memory cyclic walks. As a result, ChronoTrack achieves new state-of-the-art performance on multiple 3D-SOT benchmarks, demonstrating its effectiveness in long-term target modeling with compact memory while running at real-time speed of 42 FPS on a single RTX 4090 GPU. The code is available at this https URL

---


### 142. [PBE-UNet: A light weight Progressive Boundary-Enhanced U-Net with Scale-Aware Aggregation for Ultrasound Image Segmentation](https://arxiv.org/abs/2604.13791)

**<font color=#1a73e8>作者：</font>** Chen Wang, Yixin Zhu, Yongbin Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate lesion segmentation in ultrasound images is essential for preventive screening and clinical diagnosis, yet remains challenging due to low contrast, blurry boundaries, and significant scale variations. Although existing deep learning-based methods have achieved remarkable performance, these methods still struggle with scale variations and indistinct tumor boundaries. To address these challenges, we propose a progressive boundary enhanced U-Net (PBE-UNet). Specially, we first introduce a scale-aware aggregation module (SAAM) that dynamically adjusts its receptive field to capture robust multi-scale contextual information. Then, we propose a boundary-guided feature enhancement (BGFE) module to enhance the feature representations. We find that there are large gaps between the narrow boundary and the wide segmentation error areas. Unlike existing methods that treat boundaries as static masks, the BGFE module progressively expands the narrow boundary prediction into broader spatial attention maps. Thus, broader spatial attention maps could effectively cover the wider segmentation error regions and enhance the model's focus on these challenging areas. We conduct expensive experiments on four benchmark ultrasound datasets, BUSI, Dataset B, TN3K, and BP. The experimental results how that our proposed PBE-UNet outperforms state-of-the-art ultrasound image segmentation methods. The code is at this https URL.

---


### 143. [From Synchrony to Sequence: Exo-to-Ego Generation via Interpolation](https://arxiv.org/abs/2604.13793)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi, Nedko Savov, Danda Pani Paudel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Exo-to-Ego video generation aims to synthesize a first-person video from a synchronized third-person view and corresponding camera poses. While paired supervision is available, synchronized exo-ego data inherently introduces substantial spatio-temporal and geometric discontinuities, violating the smooth-motion assumptions of standard video generation benchmarks. We identify this synchronization-induced jump as the central challenge and propose Syn2Seq-Forcing, a sequential formulation that interpolates between the source and target videos to form a single continuous signal. By reframing Exo2Ego as sequential signal modeling rather than a conventional condition-output task, our approach enables diffusion-based sequence models, e.g. Diffusion Forcing Transformers (DFoT), to capture coherent transitions across frames more effectively. Empirically, we show that interpolating only the videos, without performing pose interpolation already produces significant improvements, emphasizing that the dominant difficulty arises from spatio-temporal discontinuities. Beyond immediate performance gains, this formulation establishes a general and flexible framework capable of unifying both Exo2Ego and Ego2Exo generation within a single continuous sequence model, providing a principled foundation for future research in cross-view video synthesis.

---


### 144. [Artificial intelligence application in lymphoma diagnosis with Vision Transformer using weakly supervised training](https://arxiv.org/abs/2604.13795)

**<font color=#1a73e8>作者：</font>** Nghia, Nguyen, Amer Wahed 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision transformers (ViT) have been shown to allow for more flexible feature detection and can outperform convolutional neural network (CNN) when pre-trained on sufficient data. Due to their promising feature detection capabilities, we deployed ViTs for morphological classification of anaplastic large cell lymphoma (ALCL) versus classic Hodgkin lymphoma (cHL). We had previously designed a ViT model which was trained on a small dataset of 1,200 image patches in fully supervised training. That model achieved a diagnostic accuracy of 100% and an F1 score of 1.0 on the independent test set. Since fully supervised training is not a practical method due to lack of expertise resources in both the training and testing phases, we conducted a recent study on a modified approach to training data (weakly supervised training) and show that labeling training image patch automatically at the slide level of each whole-slide-image is a more practical solution for clinical use of Vision Transformer. Our ViT model, trained on a larger dataset of 100,000 image patches, yields evaluation metrics with significant accuracy, F1 score, and area under the curve (AUC) at 91.85%, 0.92, and 0.98, respectively. These are respectable values that qualify this ViT model, with weakly supervised training, as a suitable tool for a deep learning module in clinical model development using automated image patch extraction.

---


### 145. [DRG-Font: Dynamic Reference-Guided Few-shot Font Generation via Contrastive Style-Content Disentanglement](https://arxiv.org/abs/2604.13797)

**<font color=#1a73e8>作者：</font>** Rejoy Chakraborty, Prasun Roy, Saumik Bhattacharya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot Font Generation aims to generate stylistically consistent glyphs from a few reference glyphs. However, capturing complex font styles from a few exemplars remains challenging, and the existing methods often struggle to retain discernible local characteristics in generated samples. This paper introduces DRG-Font, a contrastive font generation strategy that learns complex glyph attributes by decomposing style and content embedding spaces. For optimal style supervision, the proposed architecture incorporates a Reference Selection (RS) Module to dynamically select the best style reference from an available pool of candidates. The network learns to decompose glyph attributes into style and shape priors through a Multi-scale Style Head Block (MSHB) and a Multi-scale Content Head Block (MCHB). For style adaptation, a Multi-Fusion Upsampling Block (MFUB) produces the target glyph by combining the reference style prior and target content prior. The proposed method demonstrates significant improvements over state-of-the-art approaches across multiple visual and analytical benchmarks.

---


### 146. [AlphaCNOT: Learning CNOT Minimization with Model-Based Planning](https://arxiv.org/abs/2604.13812)

**<font color=#1a73e8>作者：</font>** Jacopo Cossio, Daniele Lizzio Bosco, Riccardo Romanello 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantum circuit optimization is a central task in Quantum Computing, as current Noisy Intermediate Scale Quantum devices suffer from error propagation that often scales with the number of operations. Among quantum operations, the CNOT gate is of fundamental importance, being the only 2-qubit gate in the universal Clifford+T set. The problem of CNOT gates minimization has been addressed by heuristic algorithms such as the well-known Patel-Markov-Hayes (PMH) for linear reversible synthesis (i.e., CNOT minimization with no topological constraints), and more recently by Reinforcement Learning (RL) based strategies in the more complex case of topology-aware synthesis, where each CNOT can act on a subset of all qubits pairs. In this work we introduce AlphaCNOT, a RL framework based on Monte Carlo Tree Search (MCTS) that address effectively the CNOT minimization problem by modeling it as a planning problem. In contrast to other RL- based solution, our method is model-based, i.e. it can leverage lookahead search to evaluate future trajectories, thus finding more efficient sequences of CNOTs. Our method achieves a reduction of up to 32% in CNOT gate count compared to PMH baseline on linear reversible synthesis, while in the constraint version we report a consistent gate count reduction on a variety of topologies with up to 8 qubits, with respect to state-of-the-art RL-based solutions. Our results suggest the combination of RL with search-based strategies can be applied to different circuit optimization tasks, such as Clifford minimization, thus fostering the transition toward the "quantum utility" era.

---


### 147. [Cognitive Offloading in Agile Teams: How Artificial Intelligence Reshapes Risk Assessment and Planning Quality](https://arxiv.org/abs/2604.13814)

**<font color=#1a73e8>作者：</font>** Adriana Caraeni, Alexander Shick, Andrew Lan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in artificial intelligence (AI) have shown promise in automating key aspects of Agile project management, yet their impact on team cognition remains underexplored. In this work, we investigate cognitive offloading in Agile sprint planning by conducting a controlled, three-condition experiment comparing AI-only, human-only, and hybrid planning models on a live client deliverable at a mid-sized digital agency. Using quantitative metrics -- including estimation accuracy, rework rates, and scope change recovery time -- alongside qualitative indicators of planning robustness, we evaluate each model's effectiveness beyond raw efficiency. We find that while AI-only planning minimizes time and cost, it significantly degrades risk capture rates and increases rework due to unstated assumptions, whereas human-only planning excels at adaptability but incurs substantial overhead. Drawing on these findings, we propose a theoretical framework for hybrid AI-human sprint planning that assigns algorithmic tools to estimation and backlog formatting while mandating human deliberation for risk assessment and ambiguity resolution. Our results challenge the assumption that efficiency equates to effectiveness, offering actionable governance strategies for organizations seeking to augment rather than erode team cognition.

---


### 148. [Composite Silhouette: A Subsampling-based Aggregation Strategy](https://arxiv.org/abs/2604.13816)

**<font color=#1a73e8>作者：</font>** Aggelos Semoglou, Aristidis Likas, John Pavlopoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Determining the number of clusters is a central challenge in unsupervised learning, where ground-truth labels are unavailable. The Silhouette coefficient is a widely used internal validation metric for this task, yet its standard micro-averaged form tends to favor larger clusters under size imbalance. Macro-averaging mitigates this bias by weighting clusters equally, but may overemphasize noise from under-represented groups. We introduce Composite Silhouette, an internal criterion for cluster-count selection that aggregates evidence across repeated subsampled clusterings rather than relying on a single partition. For each subsample, micro- and macro-averaged Silhouette scores are combined through an adaptive convex weight determined by their normalized discrepancy and smoothed by a bounded nonlinearity; the final score is then obtained by averaging these subsample-level composites. We establish key properties of the criterion and derive finite-sample concentration guarantees for its subsampling estimate. Experiments on synthetic and real-world datasets show that Composite Silhouette effectively reconciles the strengths of micro- and macro-averaging, yielding more accurate recovery of the ground-truth number of clusters.

---


### 149. [RPS: Information Elicitation with Reinforcement Prompt Selection](https://arxiv.org/abs/2604.13817)

**<font color=#1a73e8>作者：</font>** Tao Wang, Jingyao Lu, Xibo Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown remarkable capabilities in dialogue generation and reasoning, yet their effectiveness in eliciting user-known but concealed information in open-ended conversations remains limited. In many interactive AI applications, such as personal assistants, tutoring systems, and legal or clinical support, users often withhold sensitive or uncertain information due to privacy concerns, ambiguity, or social hesitation. This makes it challenging for LLMs to gather complete and contextually relevant inputs. In this work, we define the problem of information elicitation in open-ended dialogue settings and propose Reinforcement Prompt Selection (RPS), a lightweight reinforcement learning framework that formulates prompt selection as a sequential decision-making problem. To analyze this problem in a controlled setting, we design a synthetic experiment, where a reinforcement learning agent outperforms a random query baseline, illustrating the potential of policy-based approaches for adaptive information elicitation. Building on this insight, RPS learns a policy over a pool of prompts to adaptively elicit concealed or incompletely expressed information from users through dialogue. We also introduce IELegal, a new benchmark dataset constructed from real legal case documents, which simulates dialogue-based information elicitation tasks aimed at uncovering case-relevant facts. In this setting, RPS outperforms static prompt baselines, demonstrating the effectiveness of adaptive prompt selection for eliciting critical information in LLM-driven dialogue systems.

---


### 150. [UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization](https://arxiv.org/abs/2604.13822)

**<font color=#1a73e8>作者：</font>** Zhengxi Lu, Fei Tang, Guangyi Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MLLM-based GUI agents have demonstrated strong capabilities in complex user interface interaction tasks. However, long-horizon scenarios remain challenging, as these agents are burdened with tasks beyond their intrinsic capabilities, suffering from memory degradation, progress confusion, and math hallucination. To address these challenges, we present UI-Copilot, a collaborative framework where the GUI agent focuses on task execution while a lightweight copilot provides on-demand assistance for memory retrieval and numerical computation. We introduce memory decoupling to separate persistent observations from transient execution context, and train the policy agent to selectively invoke the copilot as Retriever or Calculator based on task demands. To enable effective tool invocation learning, we propose Tool-Integrated Policy Optimization (TIPO), which separately optimizes tool selection through single-turn prediction and task execution through on-policy multi-turn rollouts. Experimental results show that UI-Copilot-7B achieves state-of-the-art performance on challenging MemGUI-Bench, outperforming strong 7B-scale GUI agents such as GUI-Owl-7B and UI-TARS-1.5-7B. Moreover, UI-Copilot-7B delivers a 17.1% absolute improvement on AndroidWorld over the base Qwen model, highlighting UI-Copilot's strong generalization to real-world GUI tasks.

---


### 151. [A Resource-Efficient Hybrid CNN-LSTM network for image-based bean leaf disease classification](https://arxiv.org/abs/2604.13835)

**<font color=#1a73e8>作者：</font>** Hye Jin Rhee, Joseph Damilola Akinyemi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and resource-efficient automated diagnosis is a cornerstone of modern agricultural expert systems. While Convolutional Neural Networks (CNNs) have established benchmarks in plant pathology, their ability to capture long-range spatial dependencies is often limited by standard pooling layers, and their high memory footprint hinders deployment on portable devices. This paper proposes a lightweight hybrid CNN-LSTM system for bean leaf disease classification. By integrating an LSTM layer to model the spatial-sequential relationships within feature maps, our hybrid architecture achieves a 94.38% accuracy while maintaining an exceptionally small footprint of 1.86 MB; a 70% reduction in size compared to traditional CNN-based systems. Furthermore, we provide a systematic evaluation of image augmentation strategies, demonstrating that tailored transformations are superior to generic combinations for maintaining the integrity of diagnostic patterns. Results on the $\textit{ibean}$ dataset confirm that the proposed system achieves state-of-the-art F1 scores of 99.22% with EfficientNet-B7+LSTM, providing a robust and scalable framework for real-time agricultural decision support in resource-constrained environments. The code and augmented datasets used in this study are publicly available on this $\href{this https URL}{Github}$ repo.

---


### 152. [DiffMagicFace: Identity Consistent Facial Editing of Real Videos](https://arxiv.org/abs/2604.13841)

**<font color=#1a73e8>作者：</font>** Huanghao Yin, Shenkun Xu, Kanle Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-conditioned image editing has greatly benefitted from the advancements in Image Diffusion Models. However, extending these techniques to facial video editing introduces challenges in preserving facial identity throughout the source video and ensuring consistency of the edited subject across frames. In this paper, we introduce DiffMagicFace, a unique video editing framework that integrates two fine-tuned models for text and image control. These models operate concurrently during inference to produce video frames that maintain identity features while seamlessly aligning with the editing semantics. To ensure the consistency of the edited videos, we develop a dataset comprising images showcasing various facial perspectives for each edited subject. The creation of a data set is achieved through rendering techniques and the subsequent application of optimization algorithms. Remarkably, our approach does not depend on video datasets but still delivers high-quality results in both consistency and content. The excellent effect holds even for complex tasks like talking head videos and distinguishing closely related categories. The videos edited using our framework exhibit parity with videos that are made using traditional rendering software. Through comparative analysis with current state-of-the-art methods, our framework demonstrates superior performance in both visual appeal and quantitative metrics.

---


### 153. [SparseBalance: Load-Balanced Long Context Training with Dynamic Sparse Attention](https://arxiv.org/abs/2604.13847)

**<font color=#1a73e8>作者：</font>** Hongtao Xu, Jianchao Tan, Yuxuan Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While sparse attention mitigates the computational bottleneck of long-context LLM training, its distributed training process exhibits extreme heterogeneity in both \textit{1)} sequence length and \textit{2)} sparsity sensitivity, leading to a severe imbalance problem and sub-optimal model accuracy. Existing algorithms and training frameworks typically focus on single issue, failing to systematically co-optimize these two problems. Therefore, we propose SparseBalance, a novel algorithm-system co-design framework, which exploits the sparsity and sequence heterogeneity to optimize model accuracy and system efficiency jointly. First, we propose workload-aware dynamic sparsity tuning, which employs a bidirectional sparsity adjustment to eliminate stragglers and exploit inherent bubbles for free accuracy. Second, we propose a sparsity-aware batching strategy to achieve coarse-grained balance, which complements dynamic sparsity tuning. Experimental results demonstrate that SparseBalance achieves up to a 1.33$\times$ end-to-end speedup while still improving the long-context capability by 0.46\% on the LongBench benchmark.

---


### 154. [MCPThreatHive: Automated Threat Intelligence for Model Context Protocol Ecosystems](https://arxiv.org/abs/2604.13849)

**<font color=#1a73e8>作者：</font>** Yi Ting Shen, Kentaroh Toyoda, Alex Leung  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Model Context Protocol (MCP)-based agentic systems has introduced a new category of security threats that existing frameworks are inadequately equipped to address. We present MCPThreatHive, an open-source platform that automates the end-to-end lifecycle of MCP threat intelligence: from continuous, multi-source data collection through AI-driven threat extraction and classification, to structured knowledge graph storage and interactive visualization. The platform operationalizes the MCP-38 threat taxonomy, a curated set of 38 MCP-specific threat patterns mapped to STRIDE, OWASP Top 10 for LLM Applications, and OWASP Top 10 for Agentic Applications. A composite risk scoring model provides quantitative prioritization. Through a comparative analysis of representative existing MCP security tools, we identify three critical coverage gaps that MCPThreatHive addresses: incomplete compositional attack modeling, absence of continuous threat intelligence, and lack of unified multi-framework classification.

---


### 155. [Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image](https://arxiv.org/abs/2604.13856)

**<font color=#1a73e8>作者：</font>** Yujie Gao, Yao Xiao, Xiangnan Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing a complete 3D head from a single portrait remains challenging because existing methods still face a sharp quality-speed trade-off: high-fidelity pipelines often rely on multi-stage processing and per-subject optimization, while fast feed-forward models struggle with complete geometry and fine appearance details. To bridge this gap, we propose Any3DAvatar, a fast and high-quality method for single-image 3D Gaussian head avatar generation, whose fastest setting reconstructs a full head in under one second while preserving high-fidelity geometry and texture. First, we build AnyHead, a unified data suite that combines identity diversity, dense multi-view supervision, and realistic accessories, filling the main gaps of existing head data in coverage, full-head geometry, and complex appearance. Second, rather than sampling unstructured noise, we initialize from a Plücker-aware structured 3D Gaussian scaffold and perform one-step conditional denoising, formulating full-head reconstruction into a single forward pass while retaining high fidelity. Third, we introduce auxiliary view-conditioned appearance supervision on the same latent tokens alongside 3D Gaussian reconstruction, improving novel-view texture details at zero extra inference cost. Experiments show that Any3DAvatar outperforms prior single-image full-head reconstruction methods in rendering fidelity while remaining substantially faster.

---


### 156. [Simulation-Based Optimisation of Batting Order and Bowling Plans in T20 Cricket](https://arxiv.org/abs/2604.13861)

**<font color=#1a73e8>作者：</font>** Tinniam V Ganesh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops a unified Markov Decision Process (MDP) framework for optimising two recurring in-match decisions in T20 cricket namely batting order selection and bowling plan assignment, directly in terms of win and defend probability rather than expected runs. A three-phase player profile engine (Powerplay, Middle, Death) with James-Stein shrinkage is estimated from 1,161 IPL ball-by-ball records (2008-2025). Win/defend probabilities are evaluated by vectorised Monte Carlo simulation over N = 50,000 innings trajectories. Batting orders are searched by exhaustive enumeration. Bowling plans are computed by simulated annealing over the remaining quota with the constraint that the same bowler cannot bowl consecutive overs. Applied to two 2026 IPL matches, the optimal batting order improves Mumbai Indians' win probability by 4.1 percentage points (52.4% to 56.5%), and the optimal Gujarat Titans bowling plan improves defend probability by 5.2 percentage points (39.1% to 44.3%). In both cases the observed sub-optimality is consistent with phase-agnostic deployment in decisions that appear reasonable by aggregate metrics but are exposed as costly when phase-specific profiles are applied.

---


### 157. [PostureObjectstitch: Anomaly Image Generation Considering Assembly Relationships in Industrial Scenarios](https://arxiv.org/abs/2604.13863)

**<font color=#1a73e8>作者：</font>** Zebei Tong, Hongchang Chen, Yujie Lei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image generation technology can synthesize condition-specific images to supplement real-world industrial anomaly data and enhance anomaly detection model performance. Existing generation techniques rarely account for the pose and orientation of industrial components in assembly, making the generated images difficult to utilize for downstream application. To solve this, we propose a novel image synthesis approach, called PostureObjectStitch, that achieves accurate generation to meet the requirement of industrial assembly. A condition decoupling approach is introduced to separate input multi-view images into high-frequency, texture, and RGB features. The feature temporal modulation mechanism adapts these features across diffusion model time-steps, enabling progressive generation from coarse to fine details while maintaining consistency. To ensure semantic accuracy, we introduce a conditional loss that enhances critical industrial elements and a geometric prior that guides component positioning for correct assembly relationships. Comprehensive experimental results on the MureCom dataset, our newly contributed DreamAssembly dataset, and the downstream application validate the outstanding performance of our method.

---


### 158. [Hardware-Efficient Neuro-Symbolic Networks with the Exp-Minus-Log Operator](https://arxiv.org/abs/2604.13871)

**<font color=#1a73e8>作者：</font>** Eymen Ipek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) deliver state-of-the-art accuracy on regression and classification tasks, yet two structural deficits persistently obstruct their deployment in safety-critical, resource-constrained settings: (i) opacity of the learned function, which precludes formal verification, and (ii) reliance on heterogeneous, library-bound activation functions that inflate latency and silicon area on edge hardware. The recently introduced Exp-Minus-Log (EML) Sheffer operator, eml(x, y) = exp(x) - ln(y), was shown by Odrzywolek (2026) to be sufficient - together with the constant 1 - to express every standard elementary function as a binary tree of identical nodes. We propose to embed EML primitives inside conventional DNN architectures, yielding a hybrid DNN-EML model in which the trunk learns distributed representations and the head is a depth-bounded, weight-sparse EML tree whose snapped weights collapse to closed-form symbolic sub-expressions. We derive the forward equations, prove computational-cost bounds, analyse inference and training acceleration relative to multilayer perceptrons (MLPs) and physics-informed neural networks (PINNs), and quantify the trade-offs for FPGA/analog deployment. We argue that the DNN-EML pairing closes a literature gap: prior neuro-symbolic and equation-learner approaches (EQL, KAN, AI-Feynman) work with heterogeneous primitive sets and do not exploit a single hardware-realisable Sheffer element. A balanced assessment shows that EML is unlikely to accelerate training, and on commodity CPU/GPU it is also unlikely to accelerate inference; however, on a custom EML cell (FPGA logic block or analog circuit) the asymptotic latency advantage can reach an order of magnitude with simultaneous gain in interpretability and formal-verification tractability.

---


### 159. [Drowsiness-Aware Adaptive Autonomous Braking System based on Deep Reinforcement Learning for Enhanced Road Safety](https://arxiv.org/abs/2604.13878)

**<font color=#1a73e8>作者：</font>** Hossem Eddine Hafidi, Elisabetta De Giovanni, Teodoro Montanaro 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Driver drowsiness significantly impairs the ability to accurately judge safe braking distances and is estimated to contribute to 10%-20% of road accidents in Europe. Traditional driver-assistance systems lack adaptability to real-time physiological states such as drowsiness. This paper proposes a deep reinforcement learning-based autonomous braking system that integrates vehicle dynamics with driver physiological data. Drowsiness is detected from ECG signals using a Recurrent Neural Network (RNN), selected through an extensive benchmark analysis of 2-minute windows with varying segmentation and overlap configurations. The inferred drowsiness state is incorporated into the observable state space of a Double-Dueling Deep Q-Network (DQN) agent, where driver impairment is modeled as an action delay. The system is implemented and evaluated in a high-fidelity CARLA simulation environment. Experimental results show that the proposed agent achieves a 99.99% success rate in avoiding collisions under both drowsy and non-drowsy conditions. These findings demonstrate the effectiveness of physiology-aware control strategies for enhancing adaptive and intelligent driving safety systems.

---


### 160. [Evaluating Supervised Machine Learning Models: Principles, Pitfalls, and Metric Selection](https://arxiv.org/abs/2604.13882)

**<font color=#1a73e8>作者：</font>** Xuanyan Liu, Ignacio Cabrera Martin, Marcello Trovati 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The evaluation of supervised machine learning models is a critical stage in the development of reliable predictive systems. Despite the widespread availability of machine learning libraries and automated workflows, model assessment is often reduced to the reporting of a small set of aggregate metrics, which can lead to misleading conclusions about real-world performance. This paper examines the principles, challenges, and practical considerations involved in evaluating supervised learning algorithms across classification and regression tasks. In particular, it discusses how evaluation outcomes are influenced by dataset characteristics, validation design, class imbalance, asymmetric error costs, and the choice of performance metrics. Through a series of controlled experimental scenarios using diverse benchmark datasets, the study highlights common pitfalls such as the accuracy paradox, data leakage, inappropriate metric selection, and overreliance on scalar summary measures. The paper also compares alternative validation strategies and emphasizes the importance of aligning model evaluation with the intended operational objective of the task. By presenting evaluation as a decision-oriented and context-dependent process, this work provides a structured foundation for selecting metrics and validation protocols that support statistically sound, robust, and trustworthy supervised machine learning systems.

---


### 161. [MolCryst-MLIPs: A Machine-Learned Interatomic Potentials Database for Molecular Crystals](https://arxiv.org/abs/2604.13897)

**<font color=#1a73e8>作者：</font>** Adam Lahouari, Shen Ai, Jihye Han 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an open Molecular Crystal (MC) database of Machine-Learned Interatomic Potentials (MLIP) called MolCryst-MLIPs. The first release comprises fine-tuned MACE models for nine molecular crystal systems -- Benzamide, Benzoic acid, Coumarin, Durene, Isonicotinamide, Niacinamide, Nicotinamide, Pyrazinamide, and Resorcinol -- developed using the Automated Machine Learning Pipeline (AMLP), which streamlines the entire MLIP development workflow, from reference data generation to model training and validation, into a reproducible and user-friendly pipeline. Models are fine-tuned from the MACE-MH-1 foundation model (omol head), yielding a mean energy MAE of 0.141 kJ/mol/atom and a mean force MAE of 0.648 kJ/mol/Angstrom across all systems. Dynamical stability and structural integrity, as assessed through energy conservation, P2 orientational order parameters, and radial distribution functions, are evaluated using molecular dynamics simulations. The released models and datasets constitute a growing open database of validated MLIPs, ready for production MD simulations of molecular crystal polymorphism under different thermodynamic conditions.

---


### 162. [Rethinking Image-to-3D Generation with Sparse Queries: Efficiency, Capacity, and Input-View Bias](https://arxiv.org/abs/2604.13905)

**<font color=#1a73e8>作者：</font>** Zhiyuan Xu, Jiuming Liu, Yuxin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SparseGen, a novel framework for efficient image-to-3D generation, which exhibits low input-view bias while being significantly faster. Unlike traditional approaches that rely on dense volumetric grids, triplanes, or pixel-aligned primitives, we model scenes with a compact sparse set of learned 3D anchor queries and a learned expansion operator that decodes each transformed query into a small local set of 3D Gaussian primitives. Trained under a rectified-flow reconstruction objective without 3D supervision, our model learns to allocate representation capacity where geometry and appearance matter, achieving significant reductions in memory and inference time while preserving multi-view fidelity. We introduce quantitative measures of input-view bias and utilization to show that sparse queries reduce overfitting to conditioning views while being representationally efficient. Our results argue that sparse set-latent expansion is a principled, practical alternative for efficient 3D generative modeling.

---


### 163. [Blind Bitstream-corrupted Video Recovery via Metadata-guided Diffusion Model](https://arxiv.org/abs/2604.13906)

**<font color=#1a73e8>作者：</font>** Shuyun Wang, Hu Zhang, Xin Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bitstream-corrupted video recovery aims to restore realistic content degraded during video storage or transmission. Existing methods typically assume that predefined masks of corrupted regions are available, but manually annotating these masks is labor-intensive and impractical in real-world scenarios. To address this limitation, we introduce a new blind video recovery setting that removes the reliance on predefined masks. This setting presents two major challenges: accurately identifying corrupted regions and recovering content from extensive and irregular degradations. We propose a Metadata-Guided Diffusion Model (M-GDM) to tackle these challenges. Specifically, intrinsic video metadata are leveraged as corruption indicators through a dual-stream metadata encoder that separately embeds motion vectors and frame types before fusing them into a unified representation. This representation interacts with corrupted latent features via cross-attention at each diffusion step. To preserve intact regions, we design a prior-driven mask predictor that generates pseudo masks using both metadata and diffusion priors, enabling the separation and recombination of intact and recovered regions through hard masking. To mitigate boundary artifacts caused by imperfect masks, a post-refinement module enhances consistency between intact and recovered regions. Extensive experiments demonstrate the effectiveness of our method and its superiority in blind video recovery. Code is available at: this https URL.

---


### 164. [[COMP25] The Automated Negotiating Agents Competition (ANAC) 2025 Challenges and Results](https://arxiv.org/abs/2604.13914)

**<font color=#1a73e8>作者：</font>** Reyhan Aydoğan, Tim Baarslag, Tamara C.P. Florijn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper presents the primary research challenges and key findings from the 15th International Automated Negotiating Agents Competition (ANAC 2025), one of the official competitions of IJCAI 2025. We focus on two critical domains: multi-deal negotiations and the development of agents capable of concurrent negotiation within complex supply chain management environments. Furthermore, this work analyzes the results of the competition and outlines strategic directions for future iterations.

---


### 165. [PartNerFace: Part-based Neural Radiance Fields for Animatable Facial Avatar Reconstruction](https://arxiv.org/abs/2604.13918)

**<font color=#1a73e8>作者：</font>** Xianggang Yu, Lingteng Qiu, Xiaohang Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PartNerFace, a part-based neural radiance fields approach, for reconstructing animatable facial avatar from monocular RGB videos. Existing solutions either simply condition the implicit network with the morphable model parameters or learn an imaginary canonical radiance field, making them fail to generalize to unseen facial expressions and capture fine-scale motion details. To address these challenges, we first apply inverse skinning based on a parametric head model to map an observed point to the canonical space, and then model fine-scale motions with a part-based deformation field. Our key insight is that the deformation of different facial parts should be modeled differently. Specifically, our part-based deformation field consists of multiple local MLPs to adaptively partition the canonical space into different parts, where the deformation of a 3D point is computed by aggregating the prediction of all local MLPs by a soft-weighting mechanism. Extensive experiments demonstrate that our method generalizes well to unseen expressions and is capable of modeling fine-scale facial motions, outperforming state-of-the-art methods both quantitatively and qualitatively.

---


### 166. [ASTER: Latent Pseudo-Anomaly Generation for Unsupervised Time-Series Anomaly Detection](https://arxiv.org/abs/2604.13924)

**<font color=#1a73e8>作者：</font>** Romain Hermary, Samet Hicsonmez, Dan Pineau 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series anomaly detection (TSAD) is critical in domains such as industrial monitoring, healthcare, and cybersecurity, but it remains challenging due to rare and heterogeneous anomalies and the scarcity of labelled data. This scarcity makes unsupervised approaches predominant, yet existing methods often rely on reconstruction or forecasting, which struggle with complex data, or on embedding-based approaches that require domain-specific anomaly synthesis and fixed distance metrics. We propose ASTER, a framework that generates pseudo-anomalies directly in the latent space, avoiding handcrafted anomaly injections and the need for domain expertise. A latent-space decoder produces tailored pseudo-anomalies to train a Transformer-based anomaly classifier, while a pre-trained LLM enriches the temporal and contextual representations of this space. Experiments on three benchmark datasets show that ASTER achieves state-of-the-art performance and sets a new standard for LLM-based TSAD.

---


### 167. [Unsupervised Anomaly Detection in Process-Complex Industrial Time Series: A Real-World Case Study](https://arxiv.org/abs/2604.13928)

**<font color=#1a73e8>作者：</font>** Sergej Krasnikov, Lukas Meitz, Samineh Bagheri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial time-series data from real production environments exhibits substantially higher complexity than commonly used benchmark datasets, primarily due to heterogeneous, multi-stage operational processes. As a result, anomaly detection methods validated under simplified conditions often fail to generalize to industrial settings. This work presents an empirical study on a unique dataset collected from fully operational industrial machinery, explicitly capturing pronounced process-induced variability.
We evaluate which model classes are capable of capturing this complexity, starting with a classical Isolation Forest baseline and extending to multiple autoencoder architectures. Experimental results show that Isolation Forest is insufficient for modeling the non-periodic, multi-scale dynamics present in the data, whereas autoencoders consistently perform better. Among them, temporal convolutional autoencoders achieve the most robust performance, while recurrent and variational variants require more careful tuning.

---


### 168. [ASTRA: Enhancing Multi-Subject Generation with Retrieval-Augmented Pose Guidance and Disentangled Position Embedding](https://arxiv.org/abs/2604.13938)

**<font color=#1a73e8>作者：</font>** Tianze Xia, Zijian Ning, Zonglin Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subject-driven image generation has shown great success in creating personalized content, but its capabilities are largely confined to single subjects in common poses. Current approaches face a fundamental conflict when handling multiple subjects with complex, distinct actions: preserving individual identities while enforcing precise pose structures. This challenge often leads to identity fusion and pose distortion, as appearance and structure signals become entangled within the model's architecture. To resolve this conflict, we introduce ASTRA(Adaptive Synthesis through Targeted Retrieval Augmentation), a novel framework that architecturally disentangles subject appearance from pose structure within a unified Diffusion Transformer. ASTRA achieves this through a dual-pronged strategy. It first employs a Retrieval-Augmented Pose (RAG-Pose) pipeline to provide a clean, explicit structural prior from a curated database. Then, its core generative model learns to process these dual visual conditions using our Enhanced Universal Rotary Position Embedding (EURoPE), an asymmetric encoding mechanism that decouples identity tokens from spatial locations while binding pose tokens to the canvas. Concurrently, a Disentangled Semantic Modulation (DSM) adapter offloads the identity preservation task into the text conditioning stream. Extensive experiments demonstrate that our integrated approach achieves superior disentanglement. On our designed COCO-based complex pose benchmark, ASTRA achieves a new state-of-the-art in pose adherence, while maintaining high identity fidelity and text alignment in DreamBench.

---


### 169. [A Multi-Stage Optimization Pipeline for Bethesda Cell Detection in Pap Smear Cytology](https://arxiv.org/abs/2604.13939)

**<font color=#1a73e8>作者：</font>** Martin Amster, Camila María Polotto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer vision techniques have advanced significantly in recent years, finding diverse and impactful applications within the medical field. In this paper, we introduce a new framework for the detection of Bethesda cells in Pap smear images, developed for Track B of the Riva Cytology Challenge held in association with the International Symposium on Biomedical Imaging (ISBI). This work focuses on enhancing computer vision models for cell detection, with performance evaluated using the mAP50-95 metric. We propose a solution based on an ensemble of YOLO and U-Net architectures, followed by a refinement stage utilizing overlap removal techniques and a binary classifier. Our framework achieved second place with a mAP50-95 score of 0.5909 in the competition. The implementation and source code are available at the following repository: this http URL

---


### 170. [AI-Assisted Peer Review at Scale: The AAAI-26 AI Review Pilot](https://arxiv.org/abs/2604.13940)

**<font color=#1a73e8>作者：</font>** Joydeep Biswas, Sheila Schoepp, Gautham Vasan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific peer review faces mounting strain as submission volumes surge, making it increasingly difficult to sustain review quality, consistency, and timeliness. Recent advances in AI have led the community to consider its use in peer review, yet a key unresolved question is whether AI can generate technically sound reviews at real-world conference scale. Here we report the first large-scale field deployment of AI-assisted peer review: every main-track submission at AAAI-26 received one clearly identified AI review from a state-of-the-art system. The system combined frontier models, tool use, and safeguards in a multi-stage process to generate reviews for all 22,977 full-review papers in less than a day. A large-scale survey of AAAI-26 authors and program committee members showed that participants not only found AI reviews useful, but actually preferred them to human reviews on key dimensions such as technical accuracy and research suggestions. We also introduce a novel benchmark and find that our system substantially outperforms a simple LLM-generated review baseline at detecting a variety of scientific weaknesses. Together, these results show that state-of-the-art AI methods can already make meaningful contributions to scientific peer review at conference scale, opening a path toward the next generation of synergistic human-AI teaming for evaluating research.

---


### 171. [SceneGlue: Scene-Aware Transformer for Feature Matching without Scene-Level Annotation](https://arxiv.org/abs/2604.13941)

**<font color=#1a73e8>作者：</font>** Songlin Du, Xiaoyong Lu, Yaping Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Local feature matching plays a critical role in understanding the correspondence between cross-view images. However, traditional methods are constrained by the inherent local nature of feature descriptors, limiting their ability to capture non-local scene information that is essential for accurate cross-view correspondence. In this paper, we introduce SceneGlue, a scene-aware feature matching framework designed to overcome these limitations. SceneGlue leverages a hybridizable matching paradigm that integrates implicit parallel attention and explicit cross-view visibility estimation. The parallel attention mechanism simultaneously exchanges information among local descriptors within and across images, enhancing the scene's global context. To further enrich the scene awareness, we propose the Visibility Transformer, which explicitly categorizes features into visible and invisible regions, providing an understanding of cross-view scene visibility. By combining explicit and implicit scene-level awareness, SceneGlue effectively compensates for the local descriptor constraints. Notably, SceneGlue is trained using only local feature matches, without requiring scene-level groundtruth annotations. This scene-aware approach not only improves accuracy and robustness but also enhances interpretability compared to traditional methods. Extensive experiments on applications such as homography estimation, pose estimation, image matching, and visual localization validate SceneGlue's superior performance. The source code is available at this https URL.

---


### 172. [Heuristic Style Transfer for Real-Time, Efficient Weather Attribute Detection](https://arxiv.org/abs/2604.13947)

**<font color=#1a73e8>作者：</font>** Hamed Ouattara, Pierre Duthon, Pascal Houssam Salmane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present lightweight and efficient architectures to detect weather conditions from RGB images, predicting the weather type (sunny, rain, snow, fog) and 11 complementary attributes such as intensity, visibility, and ground condition, for a total of 53 classes across the tasks. This work examines to what extent weather conditions manifest as variations in visual style. We investigate style-inspired techniques, including Gram matrices, a truncated ResNet-50 targeting lower and intermediate layers, and PatchGAN-style architectures, within a multi-task framework with attention mechanisms. Two families are introduced: RTM (ResNet50-Truncated-MultiTasks) and PMG (PatchGAN-MultiTasks-Gram), together with their variants. Our contributions include automation of Gram-matrix computation, integration of PatchGAN into supervised multi-task learning, and local style capture through local Gram for improved spatial coherence. We also release a dataset of 503,875 images annotated with 12 weather attributes under a Creative Commons Attribution (CC-BY) license. The models achieve F1 scores above 96 percent on our internal test set and above 78 percent in zero-shot evaluation on several external datasets, confirming their generalization ability. The PMG architecture, with fewer than 5 million parameters, runs in real time with a small memory footprint, making it suitable for embedded systems. The modular design of the models also allows style-related or weather-related tasks to be added or removed as needed.

---


### 173. [Causal Drawbridges: Characterizing Gradient Blocking of Syntactic Islands in Transformer LMs](https://arxiv.org/abs/2604.13950)

**<font color=#1a73e8>作者：</font>** Sasha Boguraev, Kyle Mahowald  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We show how causal interventions in Transformer models provide insights into English syntax by focusing on a long-standing challenge for syntactic theory: syntactic islands. Extraction from coordinated verb phrases is often degraded, yet acceptability varies gradiently with lexical content (e.g., "I know what he hates art and loves" vs. "I know what he looked down and saw"). We show that modern Transformer language models replicate human judgments across this gradient. Using causal interventions that isolate functionally relevant subspaces in Transformer blocks, attention modules, and MLPs, we demonstrate that extraction from coordination islands engages the same filler-gap mechanisms as canonical wh-dependencies, but that these mechanisms are selectively blocked to varying degrees. By projecting a large corpus of unrelated text onto these causally identified subspaces, we derive a novel linguistic hypothesis: the conjunction "and" is represented differently in extractable versus non-extractable constructions, corresponding to expressions encoding relational dependencies versus purely conjunctive uses. These results illustrate how mechanistic interpretability can inform syntax, generating new hypotheses about linguistic representation and processing.

---


### 174. [Quantum Machine Learning for Colorectal Cancer Data: Anastomotic Leak Classification and Risk Factors](https://arxiv.org/abs/2604.13951)

**<font color=#1a73e8>作者：</font>** Vojtěch Novák, Ivan Zelinka, Lenka Přibylová 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study evaluates colorectal risk factors and compares classical models against Quantum Neural Networks (QNNs) for anastomotic leak prediction. Analyzing clinical data with 14\% leak prevalence, we tested ZZFeatureMap encodings with RealAmplitudes and EfficientSU2 ansatze under simulated noise. $F_\beta$-optimized quantum configurations yielded significantly higher sensitivity (83.3\%) than classical baselines (66.7\%). This demonstrates that quantum feature spaces better prioritize minority class identification, which is critical for low-prevalence clinical risk prediction. Our work explores various optimizers under noisy conditions, highlighting key trade-offs and future directions for hardware deployment.

---


### 175. [HINTBench: Horizon-agent Intrinsic Non-attack Trajectory Benchmark](https://arxiv.org/abs/2604.13954)

**<font color=#1a73e8>作者：</font>** Jiacheng Wang, Jinchang Hou, Fabian Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing agent-safety evaluation has focused mainly on externally induced risks. Yet agents may still enter unsafe trajectories under benign conditions. We study this complementary but underexplored setting through the lens of \emph{intrinsic} risk, where intrinsic failures remain latent, propagate across long-horizon execution, and eventually lead to high-consequence outcomes. To evaluate this setting, we introduce \emph{non-attack intrinsic risk auditing} and present \textbf{HINTBench}, a benchmark of 629 agent trajectories (523 risky, 106 safe; 33 steps on average) supporting three tasks: risk detection, risk-step localization, and intrinsic failure-type identification. Its annotations are organized under a unified five-constraint taxonomy. Experiments reveal a substantial capability gap: strong LLMs perform well on trajectory-level risk detection, but their performance drops to below 35 Strict-F1 on risk-step localization, while fine-grained failure diagnosis proves even harder. Existing guard models transfer poorly to this setting. These findings establish intrinsic risk auditing as an open challenge for agent safety.

---


### 176. [Creo: From One-Shot Image Generation to Progressive, Co-Creative Ideation](https://arxiv.org/abs/2604.13956)

**<font color=#1a73e8>作者：</font>** Zoe De Simone, Angie Boggust, Fredo Durand 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) systems enable rapid generation of high-fidelity imagery but are misaligned with how visual ideas develop. T2I systems generate outputs that make implicit visual decisions on behalf of the user, often introduce fine-grained details that can anchor users prematurely and limit their ability to keep options open early on, and cause unintended changes during editing that are difficult to correct and reduce users' sense of control. To address these concerns, we present Creo, a multi-stage T2I system that scaffolds image generation by progressing from rough sketches to high-resolution outputs, exposing intermediary abstractions where users can make incremental changes. Sketch-like abstractions invite user editing and allow users to keep design options open when ideas are still forming due to their provisional nature. Each stage in Creo can be modified with manual changes and AI-assisted operations, enabling fine-grained, step-wise control through a locking mechanism that preserves prior decisions so subsequent edits affect only specified regions or attributes. Users remain in the loop, making and verifying decisions across stages, while the system applies diffs instead of regenerating full images, reducing drift as fidelity increases. A comparative study with a one-shot baseline shows that participants felt stronger ownership over Creo outputs, as they were able to trace their decisions in building up the image. Furthermore, embedding-based analysis indicates that Creo outputs are less homogeneous than one-shot results. These findings suggest that multi-stage generation, combined with intermediate control and decision locking, is a key design principle for improving controllability, user agency, creativity, and output diversity in generative systems.

---


### 177. [Block-Based Pathfinding: A Minecraft System for Visualizing Graph Algorithms](https://arxiv.org/abs/2604.13957)

**<font color=#1a73e8>作者：</font>** Luca-Stefan Pirvu, Bogdan-Alexandru Maciuca, Andrei-Ciprian Rabu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Graph theory is a cornerstone of Computer Science education, yet entry-level students often struggle to map abstract node-edge relationships to practical applications. This paper presents the design and architecture of a Minecraft-based educational tool specifically built to visualize graph traversal and shortest-path algorithms. We propose a three-layer system: (1) a Grid Traversal module where terrain types (e.g., soul sand, ice) represent edge weights, allowing for the gamified study of shortest path algorithms; (2) a "Sky Graph" module for interactive 3D manipulation of both directed and undirected graphs; and (3) lessons and quizzes available through books. The system grounds its design in Constructionist learning theory, transitioning students from passive observers to active protagonists who physically manipulate algorithmic behavior. We additionally present a planned empirical evaluation using NASA-TLX and in-game telemetry to validate the system's pedagogical efficacy.

---


### 178. [[Emerging Ideas] Artificial Tripartite Intelligence: A Bio-Inspired, Sensor-First Architecture for Physical AI](https://arxiv.org/abs/2604.13959)

**<font color=#1a73e8>作者：</font>** You Rim Choi, Subeom Park, Hyung-Sin Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI moves from data centers to robots and wearables, scaling ever-larger models becomes insufficient. Physical AI operates under tight latency, energy, privacy, and reliability constraints, and its performance depends not only on model capacity but also on how signals are acquired through controllable sensors in dynamic environments. We present Artificial Tripartite Intelligence (ATI), a bio-inspired, sensor-first architectural contract for physical AI. ATI is tripartite at the systems level: a Brainstem (L1) provides reflexive safety and signal-integrity control, a Cerebellum (L2) performs continuous sensor calibration, and a Cerebral Inference Subsystem spanning L3/L4 supports routine skill selection and execution, coordination, and deep reasoning. This modular organization allows sensor control, adaptive sensing, edge-cloud execution, and foundation model reasoning to co-evolve within one closed-loop architecture, while keeping time-critical sensing and control on device and invoking higher-level inference only when needed. We instantiate ATI in a mobile camera prototype under dynamic lighting and motion. In our routed evaluation (L3-L4 split inference), compared to the default auto-exposure setting, ATI (L1/L2 adaptive sensing) improves end-to-end accuracy from 53.8% to 88% while reducing remote L4 invocations by 43.3%. These results show the value of co-designing sensing and inference for embodied AI.

---


### 179. [Provably Efficient Offline-to-Online Value Adaptation with General Function Approximation](https://arxiv.org/abs/2604.13966)

**<font color=#1a73e8>作者：</font>** Shangzhe Li, Weitong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study value adaptation in offline-to-online reinforcement learning under general function approximation. Starting from an imperfect offline pretrained $Q$-function, the learner aims to adapt it to the target environment using only a limited amount of online interaction. We first characterize the difficulty of this setting by establishing a minimax lower bound, showing that even when the pretrained $Q$-function is close to optimal $Q^\star$, online adaptation can be no more efficient than pure online RL on certain hard instances. On the positive side, under a novel structural condition on the offline-pretrained value functions, we propose O2O-LSVI, an adaptation algorithm with problem-dependent sample complexity that provably improves over pure online RL. Finally, we complement our theory with neural-network experiments that demonstrate the practical effectiveness of the proposed method.

---


### 180. [How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data](https://arxiv.org/abs/2604.13977)

**<font color=#1a73e8>作者：</font>** Joel Niklaus, Atsuki Yamaguchi, Michal Štefánik 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic data is a standard component in training large language models, yet systematic comparisons across design dimensions, including rephrasing strategy, generator model, and source data, remain absent. We conduct extensive controlled experiments, generating over one trillion tokens, to identify critical factors in rephrasing web text into synthetic pretraining data. Our results reveal that structured output formats, such as tables, math problems, FAQs, and tutorials, consistently outperform both curated web baselines and prior synthetic methods. Notably, increasing the size of the generator model beyond 1B parameters provides no additional benefit. Our analysis also demonstrates that the selection of the original data used for mixing substantially influences performance. By applying our findings, we develop \textbf{\textsc{FinePhrase}}, a 486-billion-token open dataset of rephrased web text. We show that \textsc{FinePhrase} outperforms all existing synthetic data baselines while reducing generation costs by up to 30 times. We provide the dataset, all prompts, and the generation framework to the research community.

---


### 181. [BOAT: Navigating the Sea of In Silico Predictors for Antibody Design via Multi-Objective Bayesian Optimization](https://arxiv.org/abs/2604.13980)

**<font color=#1a73e8>作者：</font>** Jackie Rao, Ferran Gonzalez Hernandez, Leon Gerard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Antibody lead optimization is inherently a multi-objective challenge in drug discovery. Achieving a balance between different drug-like properties is crucial for the development of viable candidates, and this search becomes exponentially challenging as desired properties grow. The ever-growing zoo of sophisticated in silico tools for predicting antibody properties calls for an efficient joint optimization procedure to overcome resource-intensive sequential filtering pipelines. We present BOAT, a versatile Bayesian optimization framework for multi-property antibody engineering. Our `plug-and-play' framework couples uncertainty-aware surrogate modeling with a genetic algorithm to jointly optimize various predicted antibody traits while enabling efficient exploration of sequence space. Through systematic benchmarking against genetic algorithms and newer generative learning approaches, we demonstrate competitive performance with state-of-the-art methods for multi-objective protein optimization. We identify clear regimes where surrogate-driven optimization outperforms expensive generative approaches and establish practical limits imposed by sequence dimensionality and oracle costs.

---


### 182. [HiProto: Hierarchical Prototype Learning for Interpretable Object Detection Under Low-quality Conditions](https://arxiv.org/abs/2604.13981)

**<font color=#1a73e8>作者：</font>** Jianlin Xiang, Linhui Dai, Xue Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpretability is essential for deploying object detection systems in critical applications, especially under low-quality imaging conditions that degrade visual information and increase prediction uncertainty. Existing methods either enhance image quality or design complex architectures, but often lack interpretability and fail to improve semantic discrimination. In contrast, prototype learning enables interpretable modeling by associating features with class-centered semantics, which can provide more stable and interpretable representations under degradation. Motivated by this, we propose HiProto, a new paradigm for interpretable object detection based on hierarchical prototype learning. By constructing structured prototype representations across multiple feature levels, HiProto effectively models class-specific semantics, thereby enhancing both semantic discrimination and interpretability. Building upon prototype modeling, we first propose a Region-to-Prototype Contrastive Loss (RPC-Loss) to enhance the semantic focus of prototypes on target regions. Then, we propose a Prototype Regularization Loss (PR-Loss) to improve the distinctiveness among class prototypes. Finally, we propose a Scale-aware Pseudo Label Generation Strategy (SPLGS) to suppress mismatched supervision for RPC-Loss, thereby preserving the robustness of low-level prototype representations. Experiments on ExDark, RTTS, and VOC2012-FOG demonstrate that HiProto achieves competitive results while offering clear interpretability through prototype responses, without relying on image enhancement or complex architectures. Our code will be available at this https URL.

---


### 183. [PRiMeFlow: Capturing Complex Expression Heterogeneity in Perturbation Response Modelling](https://arxiv.org/abs/2604.13986)

**<font color=#1a73e8>作者：</font>** Zichao Yan, Yan Wu, Mica Xu Ji 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the effects of perturbations in-silico on cell state can identify drivers of cell behavior at scale and accelerate drug discovery. However, modeling challenges remain due to the inherent heterogeneity of single cell gene expression and the complex, latent gene dependencies. Here, we present PRiMeFlow, an end-to-end flow matching based approach to directly model the effects of genetic and small molecule perturbations in the gene expression space. The distribution-fitting approach taken by PRiMeFlow enables it to accurately approximate the empirical distribution of single-cell gene expression, which we demonstrate through extensive benchmarking inside PerturBench. Through ablation studies, we also validate important model design choices such as operating in gene expression space and parameterizing the velocity field with a U-Net architecture. The PRiMeFlow architecture was used as the basis for the model that won the Generalist Prize in the first ARC Virtual Cell Challenge.

---


### 184. [Unsupervised domain transfer: Overcoming signal degradation in sleep monitoring by increasing scoring realism](https://arxiv.org/abs/2604.13988)

**<font color=#1a73e8>作者：</font>** Mohammad Ahangarkiasari, Andreas Tind Damgaard, Casper Haurum 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: Investigate whether hypnogram 'realism' can be used to guide an unsupervised method for handling arbitrary types of signal degradation in mobile sleep monitoring.
Approach: Combining a pretrained, state-of-the-art 'u-sleep' model with a 'discriminator' network, we align features from a target domain with a feature space learned during pretraining. To test the approach, we distort the source domain with realistic signal degradations, to see how well the method can adapt to different types of degradation. We compare the performance of the resulting model with best-case models designed in a supervised manner for each type of transfer.
Main Results: Depending on the type of distortion, we find that the unsupervised approach can increase Cohen's kappa with as little as 0.03 and up to 0.29, and that for all transfers, the method does not decrease performance. However, the approach never quite reaches the estimated theoretical optimal performance, and when tested on a real-life domain mismatch between two sleep studies, the benefit was insignificant.
Significance: 'Discriminator-guided fine tuning' is an interesting approach to handling signal degradation for 'in the wild' sleep monitoring, with some promise. In particular, what it says about sleep data in general is interesting. However, more development will be necessary before using it 'in production'.

---


### 185. [Physics-Informed Neural Networks for Methane Sorption: Cross-Gas Transfer Learning, Ensemble Collapse Under Physics Constraints, and Monte Carlo Dropout Uncertainty Quantification](https://arxiv.org/abs/2604.13992)

**<font color=#1a73e8>作者：</font>** Mohammad Nooraiepour, Zezhang Song, Wei Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate methane sorption prediction across heterogeneous coal ranks requires models that combine thermodynamic consistency, efficient knowledge transfer across data-scarce geological systems, and calibrated uncertainty estimates, capabilities that are rarely addressed together in existing frameworks. We present a physics-informed transfer learning framework that adapts a hydrogen sorption PINN to methane sorption prediction via Elastic Weight Consolidation, coal-specific feature engineering, and a three-phase curriculum that progressively balances transfer preservation with thermodynamic fine-tuning. Trained on 993 equilibrium measurements from 114 independent coal experiments spanning lignite to anthracite, the framework achieves R2 = 0.932 on held-out coal samples, a 227% improvement over pressure-only classical isotherms, while hydrogen pre-training delivers 18.9% lower RMSE and 19.4% faster convergence than random initialization. Five Bayesian uncertainty quantification approaches reveal a systematic divergence in performance across physics-constrained architectures. Monte Carlo Dropout achieves well-calibrated uncertainty at minimal overhead, while deep ensembles, regardless of architectural diversity or initialization strategy, exhibit performance degradation because shared physics constraints narrow the admissible solution manifold. SHAP and ALE analyses confirm that learned representations remain physically interpretable and aligned with established coal sorption mechanisms: moisture-volatile interactions are most influential, pressure-temperature coupling captures thermodynamic co-dependence, and features exhibit non-monotonic effects. These results identify Monte Carlo Dropout as the best-performing UQ method in this physics-constrained transfer learning framework, and demonstrate cross-gas transfer learning as a data-efficient strategy for geological material modeling.

---


### 186. [Remote Sensing Image Super-Resolution for Imbalanced Textures: A Texture-Aware Diffusion Framework](https://arxiv.org/abs/2604.13994)

**<font color=#1a73e8>作者：</font>** Enzhuo Zhang, Sijie Zhao, Dilxat Muhtar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative diffusion priors have recently achieved state-of-the-art performance in natural image super-resolution, demonstrating a powerful capability to synthesize photorealistic details. However, their direct application to remote sensing image super-resolution (RSISR) reveals significant shortcomings. Unlike natural images, remote sensing images exhibit a unique texture distribution where ground objects are globally stochastic yet locally clustered, leading to highly imbalanced textures. This imbalance severely hinders the model's spatial perception. To address this, we propose TexADiff, a novel framework that begins by estimating a Relative Texture Density Map (RTDM) to represent the texture distribution. TexADiff then leverages this RTDM in three synergistic ways: as an explicit spatial conditioning to guide the diffusion process, as a loss modulation term to prioritize texture-rich regions, and as a dynamic adapter for the sampling schedule. These modifications are designed to endow the model with explicit texture-aware capabilities. Experiments demonstrate that TexADiff achieves superior or competitive quantitative metrics. Furthermore, qualitative results show that our model generates faithful high-frequency details while effectively suppressing texture hallucinations. This improved reconstruction quality also results in significant gains in downstream task performance. The source code of our method can be found at this https URL.

---


### 187. [Depth-Aware Image and Video Orientation Estimation](https://arxiv.org/abs/2604.13995)

**<font color=#1a73e8>作者：</font>** Muhammad Z. Alam, Larry Stetsiuk, M. Umair Mukati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces a novel approach for image and video orientation estimation by leveraging depth distribution in natural images. The proposed method estimates the orientation based on the depth distribution across different quadrants of the image, providing a robust framework for orientation estimation suited for applications such as virtual reality (VR), augmented reality (AR), autonomous navigation, and interactive surveillance systems. To further enhance fine-scale perceptual alignment, we incorporate depth gradient consistency (DGC) and horizontal symmetry analysis (HSA), enabling precise orientation correction. This hybrid strategy effectively exploits depth cues to support spatial coherence and perceptual stability in immersive visual content. Qualitative and quantitative evaluations demonstrate the robustness and accuracy of the proposed approach, outperforming existing techniques across diverse scenarios.

---


### 188. [Acts of Configuration: Rethinking Provenance, Temporality and Legitimacy in Post-Mortem Agents](https://arxiv.org/abs/2604.13996)

**<font color=#1a73e8>作者：</font>** Kellie Yu Hui Sim, Pin Sym Foong, Darryl Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Work on persona-persistent post-mortem agents typically frames design around a life/death binary. This framing neglects a consequential yet under-theorised condition: when individuals remain alive but have impaired decisional capacity. Drawing on a multi-phase workshop in which participants trained and reflected on an AI agent for Advance Care Planning, we examined how people reason about agentic delegation post-capacity loss. Initially, participants favoured bounded agents grounded in first-party authorship and representational fidelity over autonomous or evolving stand-ins. However, temporality introduced novel ideas like adjacent use driven by persona persistence over functional expansion: agents should evolve while users retain capacity, remain static once capacity is lost, but somehow inform adjacent post-mortem uses. We discuss the implications of these findings and propose that the configuration of agents for post-capacity use reshapes our understanding of provenance, temporality, and legitimacy for post-mortem agents.

---


### 189. [Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents](https://arxiv.org/abs/2604.14004)

**<font color=#1a73e8>作者：</font>** Kangsan Kim, Minki Kang, Taeil Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory-based self-evolution has emerged as a promising paradigm for coding agents. However, existing approaches typically restrict memory utilization to homogeneous task domains, failing to leverage the shared infrastructural foundations, such as runtime environments and programming languages, that exist across diverse real-world coding problems. To address this limitation, we investigate \textbf{Memory Transfer Learning} (MTL) by harnessing a unified memory pool from heterogeneous domains. We evaluate performance across 6 coding benchmarks using four memory representations, ranging from concrete traces to abstract insights. Our experiments demonstrate that cross-domain memory improves average performance by 3.7\%, primarily by transferring meta-knowledge, such as validation routines, rather than task-specific code. Importantly, we find that abstraction dictates transferability; high-level insights generalize well, whereas low-level traces often induce negative transfer due to excessive specificity. Furthermore, we show that transfer effectiveness scales with the size of the memory pool, and memory can be transferred even between different models. Our work establishes empirical design principles for expanding memory utilization beyond single-domain silos. Project page: this https URL

---


### 190. ["I'm Not Able to Be There for You": Emotional Labour, Responsibility, and AI in Peer Support](https://arxiv.org/abs/2604.14007)

**<font color=#1a73e8>作者：</font>** Kellie Yu Hui Sim, Kenny Tsu Wei Choo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Peer support is increasingly positioned as a scalable response to gaps in mental health care, particularly in digitally mediated settings, yet what counts as peer support and how responsibility is distributed remain unevenly defined in practice. Drawing on interviews with peer supporters, we show how lived experience, moral commitment, and self-identification shape participation while blurring expectations around scope, authority, and accountability. Institutional ambiguity concentrates emotional labour, boundary-setting, and escalation of responsibility at the individual level, often without consistent organisational scaffolding. Participants evaluated AI not primarily through empathy or technical capability, but through how technologies redistribute risk, labour, and accountability within already fragile support roles. Building on these findings, we outline design futures for an AI-supported peer support ecosystem that foregrounds responsibility as a central design concern rather than treating AI as a mechanism of scale.

---


### 191. [Feed-Forward 3D Scene Modeling: A Problem-Driven Perspective](https://arxiv.org/abs/2604.14025)

**<font color=#1a73e8>作者：</font>** Weijie Wang, Qihang Cao, Sensen Gao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D representations from 2D inputs is a fundamental task in computer vision and graphics, serving as a cornerstone for understanding and interacting with the physical world. While traditional methods achieve high fidelity, they are limited by slow per-scene optimization or category-specific training, which hinders their practical deployment and scalability. Hence, generalizable feed-forward 3D reconstruction has witnessed rapid development in recent years. By learning a model that maps images directly to 3D representations in a single forward pass, these methods enable efficient reconstruction and robust cross-scene generalization. Our survey is motivated by a critical observation: despite the diverse geometric output representations, ranging from implicit fields to explicit primitives, existing feed-forward approaches share similar high-level architectural patterns, such as image feature extraction backbones, multi-view information fusion mechanisms, and geometry-aware design principles. Consequently, we abstract away from these representation differences and instead focus on model design, proposing a novel taxonomy centered on model design strategies that are agnostic to the output format. Our proposed taxonomy organizes the research directions into five key problems that drive recent research development: feature enhancement, geometry awareness, model efficiency, augmentation strategies and temporal-aware models. To support this taxonomy with empirical grounding and standardized evaluation, we further comprehensively review related benchmarks and datasets, and extensively discuss and categorize real-world applications based on feed-forward 3D models. Finally, we outline future directions to address open challenges such as scalability, evaluation standards, and world modeling.

---


### 192. [Hierarchical Reinforcement Learning with Runtime Safety Shielding for Power Grid Operation](https://arxiv.org/abs/2604.14032)

**<font color=#1a73e8>作者：</font>** Gitesh Malik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has shown promise for automating power-grid operation tasks such as topology control and congestion management. However, its deployment in real-world power systems remains limited by strict safety requirements, brittleness under rare disturbances, and poor generalization to unseen grid topologies. In safety-critical infrastructure, catastrophic failures cannot be tolerated, and learning-based controllers must operate within hard physical constraints.
This paper proposes a safety-constrained hierarchical control framework for power-grid operation that explicitly decouples long-horizon decision-making from real-time feasibility enforcement. A high-level reinforcement learning policy proposes abstract control actions, while a deterministic runtime safety shield filters unsafe actions using fast forward simulation. Safety is enforced as a runtime invariant, independent of policy quality or training distribution.
The proposed framework is evaluated on the Grid2Op benchmark suite under nominal conditions, forced line-outage stress tests, and zero-shot deployment on the ICAPS 2021 large-scale transmission grid without retraining. Results show that flat reinforcement learning policies are brittle under stress, while safety-only methods are overly conservative. In contrast, the proposed hierarchical and safety-aware approach achieves longer episode survival, lower peak line loading, and robust zero-shot generalization to unseen grids.
These results indicate that safety and generalization in power-grid control are best achieved through architectural design rather than increasingly complex reward engineering, providing a practical path toward deployable learning-based controllers for real-world energy systems.

---


### 193. [First-See-Then-Design: A Multi-Stakeholder View for Optimal Performance-Fairness Trade-Offs](https://arxiv.org/abs/2604.14035)

**<font color=#1a73e8>作者：</font>** Kavya Gupta, Nektarios Kalampalikis, Christoph Heitz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness in algorithmic decision-making is often defined in the predictive space, where predictive performance - used as a proxy for decision-maker (DM) utility - is traded off against prediction-based fairness notions, such as demographic parity or equality of opportunity. This perspective, however, ignores how predictions translate into decisions and ultimately into utilities and welfare for both DM and decision subjects (DS), as well as their allocation across social-salient groups.
In this paper, we propose a multi-stakeholder framework for fair algorithmic decision-making grounded in welfare economics and distributive justice, explicitly modeling the utilities of both the DM and DS, and defining fairness via a social planner's utility that captures inequalities in DS utilities across groups under different justice-based fairness notions (e.g., Egalitarian, Rawlsian). We formulate fair decision-making as a post-hoc multi-objective optimization problem, characterizing the achievable performance-fairness trade-offs in the two-dimensional utility space of DM utility and the social planner's utility, under different decision policy classes (deterministic vs. stochastic, shared vs. group-specific). Using the proposed framework, we then identify conditions (in terms of the stakeholders' utilities) under which stochastic policies are more optimal than deterministic ones, and empirically demonstrate that simple stochastic policies can yield superior performance-fairness trade-offs by leveraging outcome uncertainty. Overall, we advocate a shift from prediction-centric fairness to a transparent, justice-based, multi-stakeholder approach that supports the collaborative design of decision-making policies.

---


### 194. [A Complete Symmetry Classification of Shallow ReLU Networks](https://arxiv.org/abs/2604.14037)

**<font color=#1a73e8>作者：</font>** Pranavkrishnan Ramakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter space is not function space for neural network architectures. This fact, investigated as early as the 1990s under terms such as ``reverse engineering," or ``parameter identifiability", has led to the natural question of parameter space symmetries\textemdash the study of distinct parameters in neural architectures which realize the same function. Indeed, the quotient space obtained by identifying parameters giving rise to the same function, called the \textit{neuromanifold}, has been shown in some cases to have rich geometric properties, impacting optimization dynamics. Thus far, techniques towards complete classifications have required the analyticity of the activation function, notably excising the important case of ReLU. Here, in contrast, we exploit the non-differentiability of the ReLU activation to provide a complete classification of the symmetries in the shallow case.

---


### 195. [KindHML: formal verification of smart contracts based on Hennessy-Milner logic](https://arxiv.org/abs/2604.14038)

**<font color=#1a73e8>作者：</font>** Massimo Bartoletti, Angelo Ferrando, Enrico Lipparini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart contracts deployed on blockchains such as Ethereum routinely manage large amounts of assets, making their security critical. Empirical studies show that real-world attacks often exploit flaws in the business logic of contracts that unfold across multiple transactions, such as liquidity or front-running attacks. Detecting these attacks requires reasoning about expressive temporal properties beyond the capabilities of existing analysis tools. In this paper, we present an automated approach to the formal verification of smart contracts, enabling the specification and verification of complex temporal properties. Our approach provides a fully automated encoding into Lustre -- the specification language supported by the Kind 2 model checker -- of an expressive subset of Solidity contracts and temporal specifications based on first-order Hennessy-Milner Logic. This encoding allows us to leverage Kind 2 to determine whether the contract respects the specification or not. We implement our approach in a toolchain that integrates the translation and verification steps, and we evaluate its effectiveness and performance on a benchmark of smart contracts and temporal properties capturing complex attack scenarios. Our results show that the proposed approach can effectively verify non-trivial temporal properties of smart contracts and detect violations that are beyond the reach of existing analysis tools.

---


### 196. [Free Geometry: Refining 3D Reconstruction from Longer Versions of Itself](https://arxiv.org/abs/2604.14048)

**<font color=#1a73e8>作者：</font>** Yuhang Dai, Xingyi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction models are efficient but rigid: once trained, they perform inference in a zero-shot manner and cannot adapt to the test scene. As a result, visually plausible reconstructions often contain errors, particularly under occlusions, specularities, and ambiguous cues. To address this, we introduce Free Geometry, a framework that enables feed-forward 3D reconstruction models to self-evolve at test time without any 3D ground truth. Our key insight is that, when the model receives more views, it produces more reliable and view-consistent reconstructions. Leveraging this property, given a testing sequence, we mask a subset of frames to construct a self-supervised task. Free Geometry enforces cross-view feature consistency between representations from full and partial observations, while maintaining the pairwise relations implied by the held-out frames. This self-supervision allows for fast recalibration via lightweight LoRA updates, taking less than 2 minutes per dataset on a single GPU. Our approach consistently improves state-of-the-art foundation models, including Depth Anything 3 and VGGT, across 4 benchmark datasets, yielding an average improvement of 3.73% in camera pose accuracy and 2.88% in point map prediction. Code is available at this https URL .

---


### 197. [From Where Words Come: Efficient Regularization of Code Tokenizers Through Source Attribution](https://arxiv.org/abs/2604.14053)

**<font color=#1a73e8>作者：</font>** Pavel Chizhov, Egor Bogomolov, Ivan P. Yamshchikov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efficiency and safety of Large Language Models (LLMs), among other factors, rely on the quality of tokenization. A good tokenizer not only improves inference speed and language understanding but also provides extra defense against jailbreak attacks and lowers the risk of hallucinations. In this work, we investigate the efficiency of code tokenization, in particular from the perspective of data source diversity. We demonstrate that code tokenizers are prone to producing unused, and thus under-trained, tokens due to the imbalance in repository and language diversity in the training data, as well as the dominance of source-specific, repetitive tokens that are often unusable in future inference. By modifying the BPE objective and introducing merge skipping, we implement different techniques under the name Source-Attributed BPE (SA-BPE) to regularize BPE training and minimize overfitting, thereby substantially reducing the number of under-trained tokens while maintaining the same inference procedure as with regular BPE. This provides an effective tool suitable for production use.

---


### 198. [$π$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data](https://arxiv.org/abs/2604.14054)

**<font color=#1a73e8>作者：</font>** Yaocheng Zhang, Yuanheng Zhu, Wenyue Chong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep search agents have emerged as a promising paradigm for addressing complex information-seeking tasks, but their training remains challenging due to sparse rewards, weak credit assignment, and limited labeled data. Self-play offers a scalable route to reduce data dependence, but conventional self-play optimizes students only through sparse outcome rewards, leading to low learning efficiency. In this work, we observe that self-play naturally produces a question construction path (QCP) during task generation, an intermediate artifact that captures the reverse solution process. This reveals a new source of privileged information for self-distillation: self-play can itself provide high-quality privileged context for the teacher model in a low-cost and scalable manner, without relying on human feedback or curated privileged information. Leveraging this insight, we propose Privileged Information Self-Play ($\pi$-Play), a multi-agent self-evolution framework. In $\pi$-Play, an examiner generates tasks together with their QCPs, and a teacher model leverages QCP as privileged context to densely supervise a student via self-distillation. This design transforms conventional sparse-reward self-play into a dense-feedback self-evolution loop. Extensive experiments show that data-free $\pi$-Play surpasses fully supervised search agents and improves evolutionary efficiency by 2-3$\times$ over conventional self-play.

---


### 199. [OneHOI: Unifying Human-Object Interaction Generation and Editing](https://arxiv.org/abs/2604.14062)

**<font color=#1a73e8>作者：</font>** Jiun Tian Hoe, Weipeng Hu, Xudong Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-Object Interaction (HOI) modelling captures how humans act upon and relate to objects, typically expressed as <person, action, object> triplets. Existing approaches split into two disjoint families: HOI generation synthesises scenes from structured triplets and layout, but fails to integrate mixed conditions like HOI and object-only entities; and HOI editing modifies interactions via text, yet struggles to decouple pose from physical contact and scale to multiple interactions. We introduce OneHOI, a unified diffusion transformer framework that consolidates HOI generation and editing into a single conditional denoising process driven by shared structured interaction representations. At its core, the Relational Diffusion Transformer (R-DiT) models verb-mediated relations through role- and instance-aware HOI tokens, layout-based spatial Action Grounding, a Structured HOI Attention to enforce interaction topology, and HOI RoPE to disentangle multi-HOI scenes. Trained jointly with modality dropout on our HOI-Edit-44K, along with HOI and object-centric datasets, OneHOI supports layout-guided, layout-free, arbitrary-mask, and mixed-condition control, achieving state-of-the-art results across both HOI generation and editing. Code is available at this https URL.

---


### 200. [Neural architectures for resolving references in program code](https://arxiv.org/abs/2604.14073)

**<font color=#1a73e8>作者：</font>** Gergő Szalay, Gergely Zsolt Kovács, Sándor Teleki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Resolving and rewriting references is fundamental in programming languages. Motivated by a real-world decompilation task, we abstract reference rewriting into the problems of direct and indirect indexing by permutation. We create synthetic benchmarks for these tasks and show that well-known sequence-to-sequence machine learning architectures are struggling on these benchmarks. We introduce new sequence-to-sequence architectures for both problems. Our measurements show that our architectures outperform the baselines in both robustness and scalability: our models can handle examples that are ten times longer compared to the best baseline. We measure the impact of our architecture in the real-world task of decompiling switch statements, which has an indexing subtask. According to our measurements, the extended model decreases the error rate by 42%. Multiple ablation studies show that all components of our architectures are essential.

---


### 201. [TIP: Token Importance in On-Policy Distillation](https://arxiv.org/abs/2604.14084)

**<font color=#1a73e8>作者：</font>** Yuanda Xu, Hejian Sang, Zhengze Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy knowledge distillation (OPD) trains a student on its own rollouts under token-level supervision from a teacher. Not all token positions matter equally, but existing views of token importance are incomplete. We ask a direct question: which tokens carry the most useful learning signal in OPD? Our answer is that informative tokens come from two regions: positions with high student entropy, and positions with low student entropy plus high teacher--student divergence, where the student is overconfident and wrong.
Empirically, student entropy is a strong first-order proxy: retaining $50\%$ of tokens with entropy-based sampling matches or exceeds all-token training while reducing peak memory by up to $47\%$. But entropy alone misses a second important region. When we isolate low-entropy, high-divergence tokens, training on fewer than $10\%$ of all tokens nearly matches full-token baselines, showing that overconfident tokens carry dense corrective signal despite being nearly invisible to entropy-only rules.
We organize these findings with TIP (Token Importance in on-Policy distillation), a two-axis taxonomy over student entropy and teacher--student divergence, and give a theoretical explanation for why entropy is useful yet structurally incomplete. This view motivates type-aware token selection rules that combine uncertainty and disagreement. We validate this picture across three teacher--student pairs spanning Qwen3, Llama, and Qwen2.5 on MATH-500 and AIME 2024/2025, and on the DeepPlanning benchmark for long-horizon agentic planning, where Q3-only training on $<$$20\%$ of tokens surpasses full-token OPD. Our experiments are implemented by extending the OPD repository this https URL, which supports memory-efficient distillation of larger models under limited GPU budgets.

---


### 202. [From Weights to Activations: Is Steering the Next Frontier of Adaptation?](https://arxiv.org/abs/2604.14090)

**<font color=#1a73e8>作者：</font>** Simon Ostermann, Daniil Gurgurov, Tanja Baeumel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training adaptation of language models is commonly achieved through parameter updates or input-based methods such as fine-tuning, parameter-efficient adaptation, and prompting. In parallel, a growing body of work modifies internal activations at inference time to influence model behavior, an approach known as steering. Despite increasing use, steering is rarely analyzed within the same conceptual framework as established adaptation methods.
In this work, we argue that steering should be regarded as a form of model adaptation. We introduce a set of functional criteria for adaptation methods and use them to compare steering approaches with classical alternatives. This analysis positions steering as a distinct adaptation paradigm based on targeted interventions in activation space, enabling local and reversible behavioral change without parameter updates. The resulting framing clarifies how steering relates to existing methods, motivating a unified taxonomy for model adaptation.

---


### 203. [Momentum Further Constrains Sharpness at the Edge of Stochastic Stability](https://arxiv.org/abs/2604.14108)

**<font color=#1a73e8>作者：</font>** Arseniy Andreyev, Advikar Ananthkumar, Marc Walden 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work suggests that (stochastic) gradient descent self-organizes near an instability boundary, shaping both optimization and the solutions found. Momentum and mini-batch gradients are widely used in practical deep learning optimization, but it remains unclear whether they operate in a comparable regime of instability. We demonstrate that SGD with momentum exhibits an Edge of Stochastic Stability (EoSS)-like regime with batch-size-dependent behavior that cannot be explained by a single momentum-adjusted stability threshold. Batch Sharpness (the expected directional mini-batch curvature) stabilizes in two distinct regimes: at small batch sizes it converges to a lower plateau $2(1-\beta)/\eta$, reflecting amplification of stochastic fluctuations by momentum and favoring flatter regions than vanilla SGD; at large batch sizes it converges to a higher plateau $2(1+\beta)/\eta$, where momentum recovers its classical stabilizing effect and favors sharper regions consistent with full-batch dynamics. We further show that this aligns with linear stability thresholds and discuss the implications for hyperparameter tuning and coupling.

---


### 204. [UI-Zoomer: Uncertainty-Driven Adaptive Zoom-In for GUI Grounding](https://arxiv.org/abs/2604.14113)

**<font color=#1a73e8>作者：</font>** Fei Tang, Bofan Chen, Zhengxi Lu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI grounding, which localizes interface elements from screenshots given natural language queries, remains challenging for small icons and dense layouts. Test-time zoom-in methods improve localization by cropping and re-running inference at higher resolution, but apply cropping uniformly across all instances with fixed crop sizes, ignoring whether the model is actually uncertain on each case. We propose \textbf{UI-Zoomer}, a training-free adaptive zoom-in framework that treats both the trigger and scale of zoom-in as a prediction uncertainty quantification problem. A confidence-aware gate fuses spatial consensus among stochastic candidates with token-level generation confidence to selectively trigger zoom-in only when localization is uncertain. When triggered, an uncertainty-driven crop sizing module decomposes prediction variance into inter-sample positional spread and intra-sample box extent, deriving a per-instance crop radius via the law of total variance. Extensive experiments on ScreenSpot-Pro, UI-Vision, and ScreenSpot-v2 demonstrate consistent improvements over strong baselines across multiple model architectures, achieving gains of up to +13.4\%, +10.3\%, and +4.2\% respectively, with no additional training required.

---


### 205. [Complex Interpolation of Matrices with an application to Multi-Manifold Learning](https://arxiv.org/abs/2604.14118)

**<font color=#1a73e8>作者：</font>** Adi Arbel, Stefan Steinerberger, Ronen Talmon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given two symmetric positive-definite matrices $A, B \in \mathbb{R}^{n \times n}$, we study the spectral properties of the interpolation $A^{1-x} B^x$ for $0 \leq x \leq 1$. The presence of `common structures' in $A$ and $B$, eigenvectors pointing in a similar direction, can be investigated using this interpolation perspective. Generically, exact log-linearity of the operator norm $\|A^{1-x} B^x\|$ is equivalent to the existence of a shared eigenvector in the original matrices; stability bounds show that approximate log-linearity forces principal singular vectors to align with leading eigenvectors of both matrices. These results give rise to and provide theoretical justification for a multi-manifold learning framework that identifies common and distinct latent structures in multiview data.

---


### 206. [Correct Prediction, Wrong Steps? Consensus Reasoning Knowledge Graph for Robust Chain-of-Thought Synthesis](https://arxiv.org/abs/2604.14121)

**<font color=#1a73e8>作者：</font>** Zipeng Ling, Shuliang Liu, Shenghong Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM reasoning traces suffer from complex flaws -- *Step Internal Flaws* (logical errors, hallucinations, etc.) and *Step-wise Flaws* (overthinking, underthinking), which vary by sample. A natural approach would be to provide ground-truth labels to guide LLMs' reasoning. Contrary to intuition, we show that this yields no improvement in reasoning ability. We then propose CRAFT, a unified framework that mitigates both types of Step flaws, which builds a Reasoning Knowledge Graph (RKG) based on the consensus parts of multiple candidate traces, and synthesizes a high-quality trace through topological generation. Our approach improves label-prediction accuracy by 10+% on average, and consistently outperforms all baselines across both logical and mathematical reasoning benchmarks. Further, detailed benchmark evaluation proves that our method also improves the quality of LLMs' reasoning traces in multiple dimensions.

---


### 207. [HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System](https://arxiv.org/abs/2604.14125)

**<font color=#1a73e8>作者：</font>** Tianshuo Yang, Guanyu Chen, Yutian Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While end-to-end Vision-Language-Action (VLA) models offer a promising paradigm for robotic manipulation, fine-tuning them on narrow control data often compromises the profound reasoning capabilities inherited from their base Vision-Language Models (VLMs). To resolve this fundamental trade-off, we propose HiVLA, a visual-grounded-centric hierarchical framework that explicitly decouples high-level semantic planning from low-level motor control. In high-level part, a VLM planner first performs task decomposition and visual grounding to generate structured plans, comprising a subtask instruction and a precise target bounding box. Then, to translate this plan into physical actions, we introduce a flow-matching Diffusion Transformer (DiT) action expert in low-level part equipped with a novel cascaded cross-attention mechanism. This design sequentially fuses global context, high-resolution object-centric crops and skill semantics, enabling the DiT to focus purely on robust execution. Our decoupled architecture preserves the VLM's zero-shot reasoning while allowing independent improvement of both components. Extensive experiments in simulation and the real world demonstrate that HiVLA significantly outperforms state-of-the-art end-to-end baselines, particularly excelling in long-horizon skill composition and the fine-grained manipulation of small objects in cluttered scenes.

---


### 208. [Temporary Power Adjusting Withholding Attack](https://arxiv.org/abs/2604.14135)

**<font color=#1a73e8>作者：</font>** Mustafa Doger, Sennur Ulukus  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We consider the block withholding attacks on pools, more specifically the state-of-the-art Power Adjusting Withholding (PAW) attack. We propose a generalization called Temporary PAW (T-PAW) where the adversary withholds a fPoW from pool mining at most $T$-time even when no other block is mined. We show that PAW attack corresponds to $T\to\infty$ and is not optimal. In fact, the extra reward of T-PAW compared to PAW improves by an unbounded factor as adversarial hash fraction $\alpha$, pool size $\beta$ and adversarial network influence $\gamma$ decreases. For example, the extra reward of T-PAW is 22 times that of PAW when an adversary targets a pool with $(\alpha,\beta,\gamma)=(0.05,0.05,0)$. We show that honest mining is sub-optimal to T-PAW even when there is no difficulty adjustment and the adversarial revenue increase is non-trivial, e.g., for most $(\alpha,\beta)$ at least $1\%$ within $2$ weeks in Bitcoin even when $\gamma=0$ (for PAW it was at most $0.01\%$). Hence, T-PAW exposes a significant structural weakness in pooled mining-its primary participants, small miners, are not only contributors but can easily turn into potential adversaries with immediate non-trivial benefits.

---


### 209. [LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning](https://arxiv.org/abs/2604.14140)

**<font color=#1a73e8>作者：</font>** Sumeet Ramesh Motwani, Daniel Nichols, Charles London 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As language models are increasingly deployed for complex autonomous tasks, their ability to reason accurately over longer horizons becomes critical. An essential component of this ability is planning and managing a long, complex chain-of-thought (CoT). We introduce LongCoT, a scalable benchmark of 2,500 expert-designed problems spanning chemistry, mathematics, computer science, chess, and logic to isolate and directly measure the long-horizon CoT reasoning capabilities of frontier models. Problems consist of a short input with a verifiable answer; solving them requires navigating a graph of interdependent steps that span tens to hundreds of thousands of reasoning tokens. Each local step is individually tractable for frontier models, so failures reflect long-horizon reasoning limitations. At release, the best models achieve <10% accuracy (GPT 5.2: 9.8%; Gemini 3 Pro: 6.1%) on LongCoT, revealing a substantial gap in current capabilities. Overall, LongCoT provides a rigorous measure of long-horizon reasoning, tracking the ability of frontier models to reason reliably over extended periods.

---


### 210. [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141)

**<font color=#1a73e8>作者：</font>** Lin-Zhuo Chen, Jian Gao, Yihang Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D reconstruction aims to recover 3D information, such as camera poses and point clouds, from a video stream, which necessitates geometric accuracy, temporal
consistency, and computational efficiency. Motivated by the principles of Simultaneous Localization and Mapping (SLAM), we introduce LingBot-Map, a feed-forward 3D foundation
model for reconstructing scenes from streaming data, built upon a geometric context transformer (GCT) architecture. A defining aspect of LingBot-Map lies in its carefully
designed attention mechanism, which integrates an anchor context, a pose-reference window, and a trajectory memory to address coordinate grounding, dense geometric cues, and
long-range drift correction, respectively. This design keeps the streaming state compact while retaining rich geometric context, enabling stable efficient inference at around
20 FPS on 518 x 378 resolution inputs over long sequences exceeding 10,000 frames. Extensive evaluations across a variety of benchmarks demonstrate that our approach
achieves superior performance compared to both existing streaming and iterative optimization-based approaches.

---


### 211. [SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments](https://arxiv.org/abs/2604.14144)

**<font color=#1a73e8>作者：</font>** Dinging Li, Yingxiu Zhao, Xinrui Cheng 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning over three-dimensional scenes is a core capability for embodied intelligence, yet continuous model improvement remains bottlenecked by the cost of geometric annotation. The self-evolving paradigm offers a promising path, but its reliance on model consensus to construct pseudo-labels causes training to reinforce rather than correct the model's own geometric errors. We identify a property unique to 3D spatial reasoning that circumvents this limitation: ground truth is a deterministic consequence of the underlying geometry, computable exactly from point clouds and camera poses without any model involvement. Building on this insight, we present SpatialEvo, a self-evolving framework for 3D spatial reasoning, centered on the Deterministic Geometric Environment (DGE). The DGE formalizes 16 spatial reasoning task categories under explicit geometric validation rules and converts unannotated 3D scenes into zero-noise interactive oracles, replacing model consensus with objective physical feedback. A single shared-parameter policy co-evolves across questioner and solver roles under DGE constraints: the questioner generates physically valid spatial questions grounded in scene observations, while the solver derives precise answers against DGE-verified ground truth. A task-adaptive scheduler endogenously concentrates training on the model's weakest categories, producing a dynamic curriculum without manual design. Experiments across nine benchmarks demonstrate that SpatialEvo achieves the highest average score at both 3B and 7B scales, with consistent gains on spatial reasoning benchmarks and no degradation on general visual understanding.

---


### 212. [Seedance 2.0: Advancing Video Generation for World Complexity](https://arxiv.org/abs/2604.14148)

**<font color=#1a73e8>作者：</font>** Team Seedance, De Chen, Liyang Chen 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Seedance 2.0 is a new native multi-modal audio-video generation model, officially released in China in early February 2026. Compared with its predecessors, Seedance 1.0 and 1.5 Pro, Seedance 2.0 adopts a unified, highly efficient, and large-scale architecture for multi-modal audio-video joint generation. This allows it to support four input modalities: text, image, audio, and video, by integrating one of the most comprehensive suites of multi-modal content reference and editing capabilities available in the industry to date. It delivers substantial, well-rounded improvements across all key sub-dimensions of video and audio generation. In both expert evaluations and public user tests, the model has demonstrated performance on par with the leading levels in the field. Seedance 2.0 supports direct generation of audio-video content with durations ranging from 4 to 15 seconds, with native output resolutions of 480p and 720p. For multi-modal inputs as reference, its current open platform supports up to 3 video clips, 9 images, and 3 audio clips. In addition, we provide Seedance 2.0 Fast version, an accelerated variant of Seedance 2.0 designed to boost generation speed for low-latency scenarios. Seedance 2.0 has delivered significant improvements to its foundational generation capabilities and multi-modal generation performance, bringing an enhanced creative experience for end users.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
