# 📦 其他研究 | 2026年07月29日

> 本类共 **442** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-442](./part-09.md)

---

### 151. [IndicTalk: A Large-Scale Persona-Based Multilingual Conversational Corpus for Indic Languages](https://arxiv.org/abs/2607.23242)

**<font color=#1a73e8>作者：</font>** Sahil Deepak Gawande, Mayank Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have transformed conversational AI, yet high-quality multilingual code-mixed dialogue resources remain scarce, particularly for Indic languages where speakers naturally alternate between English and their native language in both native-script and Romanized forms. We present IndicTalk, one of the largest multilingual Indic code-mixed conversational corpora, comprising over 13,28,604 event-grounded multi-turn conversations across 18 language varieties covering 9 Indic languages. The corpus is generated through a fully automated pipeline that combines real-world news grounding, persona-conditioned dialogue generation using multilingual LLMs, and automatic quality validation. Extensive linguistic, automatic, and human evaluations demonstrate that IndicTalk produces fluent, coherent, and naturally code-mixed conversations across both script variants. We will release IndicTalk to support the development and evaluation of multilingual conversational AI for underrepresented Indic languages. The dataset is available at: this https URL .

---


### 152. [Characterisation of Density-based FM generation methods in the context of Information Fusion](https://arxiv.org/abs/2607.23243)

**<font color=#1a73e8>作者：</font>** Yanhao Huang, Christian Wagner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fuzzy Integral (FI) based aggregation provides a powerful mechanism for nuanced aggregation, for example, in ensemble approaches or decision-level fusion more generally. The main challenge of this approach is the appropriate parametrization of the Fuzzy Measure (FM), which captures the worths of the individual components--and their combinations--which are being fused. Here, widely used approaches including the Sugeno-$\lambda$ and Decomposable FMs, parametrize the FM by extrapolating from the densities, i.e. the weights associated with individual sources, while respecting the FM's monotonicity constraint. This paper articulates that this information is, in general, insufficient to uniquely identify a discrete FM; but shows how an interval-valued FM can indeed be determined uniquely. We proceed to show how the incorporation of additional information beyond the above, such as the choice of a specific FI and a dataset, then allows for obtaining even more specific interval-valued FMs. In practice, establishing the quality of an empirically determined FM is not trivial. To help address this, we show how the likelihood with which a resulting interval FM encompasses the `ideal', i.e. the commonly intangible, best, or ground-truth numeric FM, can be determined, producing a confidence interval at a given confidence level. Finally, based on a series of experiments, we demonstrate empirically that the Choquet FI output based on this FM can also be regarded as the confidence interval for the `ideal' information fusion result, providing a novel means to characterize FI fusion outcomes a priori and charting a pathway for future research.

---


### 153. [CAPT: A Multi-task Continuous Autoregressive Transformer enabling Cross-dataset and Cross-species Transfer for Calcium Population Dynamics](https://arxiv.org/abs/2607.23258)

**<font color=#1a73e8>作者：</font>** Xinhong Xu, Yimeng Zhang, Yuanlong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale calcium imaging has created an opportunity to build foundation-style models for neural population dynamics, but a central question remains unresolved: \textbf{whether a model pretrained on one collection of recordings can generalize to new datasets, experimental paradigms, and even species.} Existing approaches are often designed for specific tasks and evaluated on a single dataset, making it unclear whether their learned representations are reusable for new calcium trace datasets. To tackle this gap, we present \textbf{CAPT}, a \textbf{C}ontinuous \textbf{A}utoregressive \textbf{P}opulation \textbf{T}ransformer for calcium population dynamics. CAPT models continuous calcium traces directly through a continuous patch tokenization strategy and is trained autoregressively, enabling end-to-end pretraining and adaptation to diverse downstream tasks. We first pretrain CAPT on a large-scale mouse calcium imaging dataset and evaluate its transferability across independent mouse, larval zebrafish, and \textit{C. elegans} datasets collected by different laboratories. In these transfer settings, the pretrained backbone is frozen and only adaptation modules are updated. Across neural population forecasting and behavior decoding tasks, CAPT consistently outperforms specialized and general-purpose baselines. Alongside predictive performance, multimodal analyses using NeuroPAL annotations in \textit{C. elegans} datasets show that CAPT embeddings form a shared functional space across datasets and capture anatomical cell-identity-related structure. These results suggest that the continuous autoregressive modeling opens up possibilities for a simple route towards general-purpose neural foundation models for calcium imaging, which can generalize across datasets, experimental paradigms, and species.

---


### 154. [SeekJudge: A Practical Reward Framework for Reinforcement Learning in Computer-Use Agents](https://arxiv.org/abs/2607.23263)

**<font color=#1a73e8>作者：</font>** Yang Wan, Zhenhao Zhang, Jierui Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deciding whether a trajectory actually fulfills its instruction governs how we measure computer-use agents on long-horizon graphical-user-interface tasks and how we train them with reinforcement learning. This judgment has long relied on rule-based evaluation, which struggles to align with human intention and goes stale when an app updates or its online content drifts. Existing model-based judges attempt to address these problems but still leave a performance gap to the rule-based evaluation. We propose the \textbf{SeekJudge} framework, in which four role-specialized agents, a Condense, a Ground, a Seek and an Analyze agent, reach a verdict through a Seek--Analyze loop over the trajectory. A seed-calibrated distillation pipeline trains one specialized $9$B model to serve as the shared backbone for all four agents. Measured by downstream success rate on held-out RL test goals, SeekJudge is the first practical model-based reward to match or surpass native rule-based supervision in online RL. Beyond accuracy, SeekJudge provides step-level judgments, runs far cheaper than a closed-source large model, and keeps a small per-call context that scales to much longer trajectories. We further contribute a general architectural improvement to the reward server that speeds up judging in RL. Together these make model-based reward a practical drop-in for rule-based supervision in CUA reinforcement learning.

---


### 155. [From Signals to Behaviors: Evidence-Based Android Malware Detection](https://arxiv.org/abs/2607.23272)

**<font color=#1a73e8>作者：</font>** Shiwen Song, Yiheng Xiong, Sen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Android malware remains a persistent threat, and detecting it accurately is a long-standing open problem. Whether an app is malicious depends on what it actually does and the context in which it does it, not on the surface signals it happens to exhibit. Existing detectors instead reason about proxies for behavior, such as learned features or local code slices, and flag whatever deviates from these proxies as malicious. But deviation is not maliciousness: benign apps that merely look unusual are over-flagged, evolving malware that looks ordinary slips through. We argue that detection should be behavior-oriented: recover an app's potentially malicious behaviors and judge which are truly malicious. To realize this, we present Praxis, which structures detection as a hypothesize-confirm-judge pipeline: it hypothesizes candidate behaviors from coarse static signals, confirms each by grounding it in code evidence verified with program analysis, and judges the confirmed behaviors in context: the user's awareness, the app's functional context, and how they compose into an attack. For a malicious app, Praxis returns a verdict and the supported behaviors. We evaluate Praxis against seven baselines across three challenging settings. It achieves the best overall detection performance (87.4% F1), outperforming the baselines by 18.6-34.8 percentage points. On high-permission benign apps, it reduces the false-positive rate to 13.0%, a reduction of 41.1-67.0 percentage points compared with the baselines. Beyond binary detection, Praxis recovers fine-grained malicious behaviors at 87.3% F1, outperforming prior behavior-level approaches by 56.5-73.4 percentage points. Ablation studies show that each stage of the pipeline contributes to the final performance.

---


### 156. [Co-Evolving Graph and Text Memory for Training-Free Multi-Hop Question Answering](https://arxiv.org/abs/2607.23278)

**<font color=#1a73e8>作者：</font>** Hieu Man, Thien Huu Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering requires coordinating relational and textual evidence across reasoning steps, a combination neither a text corpus nor a knowledge graph can supply alone. Prior work often emphasizes only part of this loop: graph-augmented RAG retrieves from a pre-built or query-updated graph, KGQA systems search within topic-centered subgraphs, and memory-augmented agents maintain evolving memories without continuously reconciling graph memory with textual context. We propose Co-E, a training-free system built around synchronized bidirectional graph-text working memory. A synchronization cycle consolidates textual memory, extracts relational triples into graph memory, and injects graph facts back into the generation context. Because both memories are maintained, they shape subsequent retrieval and generation. Evaluated on six multi-hop QA benchmarks, Co-E improves over comparable training-free open-backbone baselines and is competitive with larger or trained systems.

---


### 157. [StageGuard: Physiologically Constrained Sleep Staging](https://arxiv.org/abs/2607.23284)

**<font color=#1a73e8>作者：</font>** Juntang Wang, Yihan Wang, Hao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated sleep staging is increasingly used in large-scale studies to derive sleep-architecture endpoints: total sleep time, REM latency, sleep efficiency, and bout-duration statistics. Deep learning models achieve epoch-level accuracy approaching inter-rater agreement, yet often produce hypnograms that violate physiological invariants, such as rare transitions (e.g., direct Wake -> REM) or excessively fragmented sequences. Such violations can bias downstream sleep metrics, regardless of overall accuracy. We propose StageGuard, a plug-and-play, backbone-agnostic structured-inference framework that wraps any neural sleep-staging backbone with physiology-informed priors. StageGuard combines (1) a differentiable soft transition penalty that discourages physiologically rare transitions during training, and (2) a semi-Markov constrained decoder with a duration-augmented state space that jointly enforces transition penalties and minimum bout durations at inference. Unlike hard-prohibition methods, it admits rare transitions when emission evidence is overwhelming, leaving informative pathological events recoverable rather than blocked. StageGuard constrains staging outputs to satisfy known physiological priors rather than modeling sleep generatively. We quantify the validity gap using transition-violation rate (TVR) and fragmentation index (FI) and demonstrate that, across six backbones and four datasets, StageGuard reduces TVR to physiologically plausible levels and lowers FI by 56-62%, while maintaining or slightly improving classification accuracy. Crucially, improved constraint satisfaction translates into 59-79% lower error on derived sleep-architecture statistics not directly optimized by the method, and recovers the direction and effect size of expert-defined subgroup differences (OSA severity, age) more faithfully than the unconstrained baseline.

---


### 158. [Hiding in Plain Sight: An Effective Physical Adversarial Patch Attack against Visual-Infrared Fused Face Detection](https://arxiv.org/abs/2607.23292)

**<font color=#1a73e8>作者：</font>** Qiucheng Yu, Tao Ni, Yihe Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep learning-based visual-infrared fused face detection models are increasingly deployed across a wide range of applications, yet they remain susceptible to adversarial patch attacks. Most prior attacks target either the visual or the infrared image alone in the digital domain, which renders them ineffective against fused models in the physical world. Moreover, many of these methods are readily noticeable, as their patch patterns deviate substantially from those seen in the real world. In this paper, we introduce VIPatch (Visual-Infrared Patch), a novel physical adversarial patch attack that produces inconspicuous, realistic, and natural-looking patches for facial images. Specifically, VIPatch crafts a gradient-color mask together with a band-aid sticker across both the visual and infrared images, and jointly optimizes these two elements; the resulting digital patches further guide the fabrication of their physical counterparts. Experimental results show that VIPatch achieves competitive attack success rates (over 90%) in both the digital and physical domains, while keeping the patches unobtrusive to human observers.

---


### 159. [FILLER: Feature Imputation via Latent Location Exploration and Retrieval](https://arxiv.org/abs/2607.23295)

**<font color=#1a73e8>作者：</font>** Santu Mondal, Chayan Maitra, Rajat K. De  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In real-world machine learning applications, incomplete observations create a fundamental challenge. Researchers have come up with several ideas to address this crucial problem. However, current models still face challenges in balancing scalability and structural consistency. This study proposes a feature imputation method, called FILLER, that deliberately searches the two-dimensional latent space produced by a generative model and fills the missing values with appropriate entries. The generative model is trained on fully observed data to generate samples from the latent space, and FILLER uses this trained model to impute the values missing in the corrupted test samples. In this study, G-NeuroDAVIS serves the purpose of the generative model. This work also presents a mathematical proof on the convergence of the iterative search. Finally, FILLER has been evaluated on several image datasets under random and structured missingness patterns with varying levels of imputation complexities. In order to justify the efficacy of FILLER, it has been compared against existing state-of-the-art solution strategies in terms of RMSE, PSNR, and SSIM. In addition, Wilcoxon signed-rank test has been carried out to validate statistical significance. Moreover, downstream analyses (classification and clustering) have also established the quality of imputation in terms of standard metrics.

---


### 160. [Cross Sensory Co-Design Tools and Interaction Qualities](https://arxiv.org/abs/2607.23298)

**<font color=#1a73e8>作者：</font>** Albrecht Kurze, Klaus Stephan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> What is the temperature of a loud cry? What is the color of a hand-clap? Cross-sensory and multi-modal interactions offer interesting possibilities in terms of inputs and outputs that might be leveraged for affective and emotional purposes. However, it is hard to design such interactions without the right co-design tools. We developed such tools in the last 10 years: the Loaded Dice and the Wheel of Plush. Both devices incorporate a multitude of sensors and actuators to demonstrate interactions and aid in co-design workshops. The tools incorporate the principle of technical synesthesia: the ability to map any of the included sensors to any of the included actuators. With intuitive simple interaction schemes it is possible to easily and effortlessly create new combinations. We discuss the core principles of the tools and how we realized a meaningful mapping between sensors and actuators. We further discuss how we use the tools for exploration, sensory sketching or scenario driven ideation, and where we see additional potential.

---


### 161. [Explainable AI through the Lens of Material Agency: Enabling Musical Interface Design with Neural Audio Models](https://arxiv.org/abs/2607.23309)

**<font color=#1a73e8>作者：</font>** Shuoyang Jasper Zheng, Anna Xambó Sedó, Nick Bryan-Kinns  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent work in Human-Computer Interaction (HCI) increasingly treats AI models as design materials that have distinctive computational properties to shape design artifacts. Artists learn to work with the model "at play" to explore their emerging properties. The aim of explainability, in this view, is to make visible a crafting and hacking space to enable sustained creative practices with AI. In this chapter, we propose material explainability as a range of activities and artifacts that transform AI models into accessible and inclusive design materials in the workspace of artists, designers, and makers. We present a case study of building a repository of resources to enable artistic explorations of neural audio models in New Interfaces for Musical Expression (NIME) design. Reflecting on our community-building journey and the making of a collection of musical interface designs with a group of artists, we raise three recommendations on enabling the exploration of AI as materials in artistic practices to inspire future XAI design for artists.

---


### 162. [Emergent Behaviour in Financial Markets](https://arxiv.org/abs/2607.23311)

**<font color=#1a73e8>作者：</font>** Omar Inverso, Emilio Tuosto, Dragisa Zunic  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Some properties of so-called complex or collective systems can be observed to emerge from the interactions of elementary agents. This phenomenon, known as emergent behaviour, has long since been studied in the most diverse disciplines, with recent growing awareness from the formal methods community about the opportunity of opening up to seemingly distant disciplines with appropriate technology for computer-aided reasoning. Different peculiar elements of complexity make automated reasoning on these systems particularly challenging. We consider electronic financial markets to drive our discussion. We identify and structure the sources of complexity to tackle in order to provide computational support for the analysis of emergent phenomena. We refrain from evaluating the suitability of specific technical solutions or frameworks of preference, which would as usual require simplifying assumptions and divert from the actual phenomenon of interest. Rather, we elaborate on possible alternatives to handle some of the main technical aspects involved in automated analysis, while retaining a solid and concrete interpretation of the domain, and in doing so outline a more systematic research program for the formal specification and analysis of market mechanisms.

---


### 163. [A Structured Cyber Threat Intelligence Dataset Using STIX 2.1 Entities and MITRE ATT&CK Mappings](https://arxiv.org/abs/2607.23312)

**<font color=#1a73e8>作者：</font>** Dipshikha Das, Arnab Banik, Md. Shariful Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber threat intelligence (CTI) reports are typically written in unstructured formats, which complicates the extraction and analysis of important entities and adversarial behaviors. Although existing CTI research provides extraction tools, knowledge-graph frameworks, and MITRE ATT&CK mapped datasets, curated report-level datasets that preserve complex entity relationships and normalized adversarial behaviors remain limited. To address this limitation, this study presents a manually constructed dataset of 150 English-language CTI reports, each represented as STIX 2.1 based graphs, which includes 4,777 STIX entities, 5,817 STIX relationships in total, and 1,273 STIX attack-pattern entities (adversarial behaviors) mapped to 269 unique MITRE ATT&CK Enterprise techniques and sub-techniques. Twenty five randomly sampled reports were independently assessed by two cybersecurity researchers, which shows substantial inter-rater agreement. Disagreements were subsequently adjudicated to establish a gold-standard reference dataset. Four locally deployed open-source LLMs were evaluated as automated judges against this adjudicated reference sample. Qwen3.6:27B achieved the strongest overall performance, with a maximum kappa score of 0.803, micro-F1 scores exceeding 92%, and false-positive rates below 5%. The dataset provides a benchmark for CTI information extraction, knowledge-graph construction, incident analysis, and threat attribution. The findings further indicate that locally deployed LLMs can support human reviewers in identifying annotation inconsistencies, but expert validation remains essential.

---


### 164. [Ordered Network Analysis of Epistemic Emotions during Collaborative Problem Solving](https://arxiv.org/abs/2607.23317)

**<font color=#1a73e8>作者：</font>** Sifatul Anindho, Videep Venkatesha, Jaclyn Ocumpaugh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Investigating how affective states such as confusion and frustration persist and transition during co-situated collaborative problem solving (CPS) is important for understanding the dynamics of epistemic emotions. However, the accurate identification of affective states remain challenging as there is no gold-standard truth in this space. Here, we analyze affective states collected through retrospective cued-recall during an in-person CPS task. Using ordered network analysis (ONA), we examine (1) the overall ordered structure of affective states and how this structure differs across self-caught and probe-caught reporting methods, and (2) what aspects of this ordered structure are emphasized differently in slower and faster groups. We find that ONA reveals differences in persistence and transition patterns that are not apparent from descriptive summaries alone. In particular, we observe a stable epistemic core linking curiosity, optimism, and confusion, with different reporting methods emphasizing different connections among states. An analysis between faster and slower groups show that roles of confusion and disengagement also shift significantly during collaboration, particularly in their relationship to conflict. We interpret our findings in the context of collaboration and discuss their implications in developing AI systems that support CPS.

---


### 165. [BHARATI: Morphology-Aware Tokenizers for Classical Indian Languages with Subword Fertility Analysis](https://arxiv.org/abs/2607.23319)

**<font color=#1a73e8>作者：</font>** Poornima Kumaresan, Pavithra Muruganantham, Lakshmi Rajendran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard subword tokenization algorithms such as Byte-Pair Encoding (BPE) and SentencePiece are trained predominantly on modern language corpora and produce inefficient segmentations when applied to classical Indian languages. Sanskrit, Tamil, and other classical Indic languages exhibit agglutinative morphology, productive sandhi (phonological fusion at word boundaries), and domain-specific vocabularies absent from general-purpose training data. This paper presents BHARATI, a set of SentencePiece BPE tokenizers trained on a balanced 781 MB corpus spanning seven languages (English, Hindi, Sanskrit, Tamil, Telugu, Kannada, and Malayalam) with native script support for all languages. We describe three successive tokenizer versions: v1 (English and Sanskrit only, with broken byte-fallback for Tamil), v2 (four-language support with byte-level fallback for southern languages), and v3 (full seven-language native subword coverage). Subword fertility analysis demonstrates that v3 averages 2.6 tokens per Indian Knowledge System (IKS) technical term, compared to 5.25 tokens per term with GPT-2's tokenizer and 3.75 tokens with the multilingual SentencePiece baseline, with the largest gains on a set of reserved IKS terms that are represented as single tokens by construction. On a held-out test set of 490 IKS-domain sentences (70 per language across seven languages, released with the measurement script), v3 reduces sequence length by roughly 90% relative to GPT-2 and byte-level encoding (which lack native Indic subwords) and by approximately 25% relative to the mBART-50 multilingual baseline, averaged across the six Indic languages, directly translating to increased effective context length for downstream language models. The tokenizer models (32,000 vocabulary), training scripts, and evaluation benchmarks are released under open licenses.

---


### 166. [Training with (Swap) Regret Loss in a Single-Layer Self-Attention Model: A Case Study on the Probability Simplex](https://arxiv.org/abs/2607.23333)

**<font color=#1a73e8>作者：</font>** Chanwoo Park, Asuman Ozdaglar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit the regret loss framework introduced in Park et al. (2025), which uses decision-theoretic regret as a direct loss function for training models to make better decisions, through the lens of probability-simplex policies. Our first result shows that a single-layer self-attention model trained with regret loss admits a stationary point whose forward-pass exactly matches smoothed fictitious play with the appropriate stepsize that ensures no-regret behavior-i.e., for any given policy input, the model outputs the same update that smoothed fictitious play would produce. In parallel, we also newly introduce a swap-regret loss function, which extends the regret-loss framework beyond external regret and enables models to directly optimize for swap-deviation robustness. We further show that this swap-regret loss admits a stationary point whose forward pass implements the corresponding swap-regret update induced by classical Blum-Mansour no-pass implementation algorithm, with each head implementing an external-regret update via smoothed fictitious play. Together, these results show that regret-trained attention can realize differentiable mechanisms whose deployment induces equilibrium behavior in games: external-regret dynamics lead to coarse correlated equilibrium, while swap-regret dynamics lead to correlated equilibrium. Thus, regret-based objectives steer minimal attention architectures toward online-learning dynamics with game-theoretic guarantees, without supervised traces of those algorithms.

---


### 167. [Neural operator discovery from heterogeneous trajectories](https://arxiv.org/abs/2607.23337)

**<font color=#1a73e8>作者：</font>** Zituo Chen, Qiaofeng Li, Jiaxin Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators provide data-driven mappings for modeling dynamical systems. Extending them to families of systems typically requires explicit conditioning variables such as physical parameters, geometries, or boundary conditions. In many real-world settings, these quantities are unobserved. Here, we formulate neural operator discovery (NOD) as the problem of learning both shared solution operators and system-specific variation directly from heterogeneous trajectories without access to labeled governing factors. We introduce a factorized latent-conditioning formulation that jointly learns a neural operator and a low-dimensional latent representation through factorized prediction, trajectory-decoupled sampling, and dimension selection. Across diverse systems, the learned latent representation captures the intrinsic dimensionality of system variation and organizes system instances in a smooth and approximately invertible latent structure aligned with the underlying governing factors. This organization enables generalization to previously unseen system instances, including zero-shot extrapolation across regimes and stable long-horizon prediction. These results establish an interpretable paradigm for operator learning in the absence of explicit factor supervision.

---


### 168. [Does Graph Compression Preserve Signal Propagation?](https://arxiv.org/abs/2607.23338)

**<font color=#1a73e8>作者：</font>** Kawshik Banerjee, Khaled Mohammed Saifuddin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph compression reduces the computational cost of graph learning, but its effect on signal propagation remains largely underexplored. Existing work evaluates compression through downstream task performance or structural preservation, neither of which directly captures how propagation dynamics change after compression. We study two fundamental compression paradigms, coarsening and sparsification, and ask whether they preserve the propagation behavior of the original graph. Across five datasets, varying compression rates, and propagation depths, we measure signal behavior through three complementary metrics. Our results reveal a consistent tension between the two compression families. Sparsification retains higher signal diversity and mitigates oversmoothing, but its propagation trajectory progressively diverges from that of the original graph. Coarsening more faithfully preserves propagation behavior, but at the cost of stronger smoothing and rank collapse. These findings demonstrate that two propagation-centric objectives, preserving signal diversity and preserving propagation fidelity, are distinct and empirically at odds under graph compression, highlighting the need for evaluation protocols that jointly consider both dimensions. The code and results are available at: this https URL

---


### 169. [Exploring the OODA Loop as a Systematic Way of Thinking in Coping with Conflicts](https://arxiv.org/abs/2607.23342)

**<font color=#1a73e8>作者：</font>** Ethan Anderson, Shouhuai Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When conflicts emerge, we need systematic ways of thinking to deal with them. This paper revisits Boyd's Observe, Orient, Decide, Act (OODA) loop and explores its usefulness as a systematic way of thinking for reasoning about conflicts in dynamic environments characterized by uncertainty, adaptation, and adversarial interference. We explore the OODA loop beyond its origin in air warfare where it focuses attention on the relationship between information, understanding, choice, and action. Our exploration is conducted in two application domains: cyber conflicts and cognitive conflicts. Across both domains, we emphasize situational awareness as a critical mechanism of orientation, while noting that observations become useful only when they are perceived, comprehended, projected into possible futures, and integrated with mental models, objectives, doctrine, trust, and experience. Our exploration suggests that conflict is not merely a contest of actions or effects, but a contest over the ability to generate, protect, and leverage one's own superior observation, orientation, and decision, while degrading and exploiting adversary's observation, orientation, and decision.

---


### 170. [SPRKD: Effective Knowledge Distillation for Deep Neural Networks via Saddle Region Approximation](https://arxiv.org/abs/2607.23346)

**<font color=#1a73e8>作者：</font>** Aditya Dewan, Arjun Yogeswaran, Benjamin Fedoruk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep neural networks are potent catalysts for scientific and industrial impact, yet excessive parameter counts impede deployment in low-compute settings such as hospital equipment and energy infrastructure. Predominant knowledge distillation (KD) methods favor replication: smaller students mimic teacher output logits, yet empirically yield low task performance, hamper convergence, and act merely as regularization rather than substantive knowledge transfer. We propose Saddle Point Recruitment for Knowledge Distillation (SPRKD), reframing distillation from replication to employing teachers as optimization-curvature and domain proxies, characterizing saddle points as regions of strong further-descent potential via embedding and basin-fractal properties. Using Hessian eigenvalue spectral density (ESD), SPRKD identifies low-loss saddle regions for student re-exploration; weak-teacher ensembles are aggregated into an Approximated Saddle Region (ASR), re-parameterized into the student via Transfer Learning by Injection, and approached with exponentially decaying Euclidean transformations, Negative Hessian Eigensteps, and Gaussian perturbations. On malaria blood smear classification with a 6,430-parameter CNN distilled from a weak 25,546-parameter teacher, SPRKD reaches 94.8% validation accuracy, outperforming Response KD by 24.70 percentage points (McNemar p = 6.3e-87) and matching scratch-trained baselines of the same architecture to statistical equivalence (p = 1.0). Across MNIST, CIFAR-100, and TinyImageNet, SPRKD exceeds scratch-trained baselines by up to 8 percentage points on preliminary benchmarks. Hessian ESD and 2-D loss landscape analysis show convergence to wider minima with substantially smaller Hessian trace and spectral radius than Response KD and control students, indicating smoother descent and greater noise robustness.

---


### 171. [Exploration of the generative capabilities of Boltzmann machines applied to social systems under the majority rule](https://arxiv.org/abs/2607.23349)

**<font color=#1a73e8>作者：</font>** Mauricio A. Valle, Gonzalo A. Ruz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the generative capabilities of Boltzmann machines to recover systems governed by the majority rule under critical conditions. To this end, we train deep belief networks (DBNs) with different configurations, where the first layer can use Gaussian visible units with more than two states (i.e., non-binary units). We then allow the DBN to "dream" samples conditioned on visible units that we keep fixed, and we measure the deviation of this dreamed system from the real one. We also corroborate, using a discrete thermometer based on a convolutional network, that the reconstructions remain in a critical state. Across several training sessions with different architectures, we show that, despite the complexity of the problem, the DBN can recover samples that remain critical even under input noise, with a gradual degradation of physical observables relative to the original sample.

---


### 172. [Joint Optimization for Greedy Longest-match Tokenization](https://arxiv.org/abs/2607.23362)

**<font color=#1a73e8>作者：</font>** Adhiraj Singh, Deepanshu Mody, Ghina Al Shdaifat 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that subword vocabularies can be trained to optimize compression for a specific inference rule rather than relying on greedy heuristics such as Byte Pair Encoding (BPE). We extend this approach to greedy left-to-right longest-match decoding, the fast and widely used inference rule underlying WordPiece. We introduce Joint Optimization for Greedy Longest-Match Tokenization (JOLT), which formulates vocabulary learning as an integer program over vocabulary-selection and segmentation-choice variables. Greedy-consistency constraints ensure that each optimized segmentation exactly matches the segmentation produced by longest-match decoding under the selected vocabulary, aligning the training objective with deployment-time tokenization. To scale the optimization, we solve a linear programming relaxation and selectively introduce higher-order segmentations only for unresolved pretokens. The resulting relaxation is nearly integral: rounded solutions fall within 0.008 - 0.176 % of the LP lower bound on the training scope. The bound also shows that BPE is already within 1 - 2 % of the best achievable compression under greedy longest-match decoding, while JOLT closes 89.6 - 99.4 % of the remaining gap. On held-out validation data across four training scopes and vocabulary sizes of 32,000 and 64,000, JOLT produces up to 0.78 % fewer tokens than BPE, with improvements generally increasing as the training scope grows. These results demonstrate that inference-aligned vocabulary optimization can recover most of the limited compression headroom left by BPE while providing a certificate of near-optimality.

---


### 173. [On the Impossibility of Unbiased and Length-Invariant Policy Optimization with Outcome Rewards](https://arxiv.org/abs/2607.23364)

**<font color=#1a73e8>作者：</font>** Fei Ding, Yongkang Zhang, Yuhao Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) is the dominant reinforcement learning algorithm for training reasoning capabilities in large language models, notably adopted by DeepSeek-R1. The recent improvement Dr. GRPO (COLM 2025) identifies the response-level length bias caused by per-trajectory length normalization in GRPO and proposes removing this normalization, claiming the resulting optimizer is "unbiased." We show that this claim is incomplete. Specifically, we establish an impossibility theorem: under the standard outcome reward + GRPO setting, no length-based weighting scheme can simultaneously achieve the following two properties. (P1) Gradient unbiasedness: the gradient estimator is an unbiased estimate of the true policy gradient. (P2) Length invariance: each trajectory's effective contribution to the gradient is independent of its token length. GRPO approximately satisfies P2 but violates P1; Dr. GRPO satisfies P1 but violates P2. We characterize the complete tradeoff spectrum via the parametric family f_alpha(L) = L^{alpha - 1}, where alpha = 0 recovers GRPO, alpha = 1 recovers Dr. GRPO, and provide quantitative analysis showing that Dr. GRPO's length bias can cause longer trajectories to dominate gradient updates by a factor proportional to the length ratio. Our results reveal that neither algorithm is universally "done right"; they occupy opposite ends of a fundamental and unavoidable tradeoff.

---


### 174. [Explaining BiomedCLIP with Weighted Banzhaf Interactions Supported by Tree-Gram Parsing](https://arxiv.org/abs/2607.23368)

**<font color=#1a73e8>作者：</font>** Jakub Rymarski, Adam Rempała, Bartłomiej Sobieski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are demonstrating significant capabilities in medical tasks like radiology analysis, yet providing faithful and interpretable explanations remains a key consideration for their responsible deployment in clinical settings. However, existing explanation methods, such as the widely used FIxLIP framework, often struggle with the fine-grained nature of modern tokenizers. The tokenization problem fragments clinical concepts---splitting terms like "saddle embolus" into scattered, meaningless subwords---which leads to noisy, semantically incoherent cross-modal attributions. Such fragmentation also results in a combinatorial explosion of interaction possibilities, obscuring the model's true reasoning. To address this, we introduce ParseFIxLIP, an extension that incorporates the Tree-Gram Parsing into the Banzhaf interaction game used by FIxLIP. This semantically informed strategy utilizes dependency parsing trees to define explanation players by grouping related text tokens into semantically coherent units. Our smart_depth grouping strategy, merging tokens according to spaCy token dependency tree, successfully mitigates concept fragmentation, yielding substantially more interpretable cross-modal interactions by unifying complex medical concepts. Quantitatively, while baselines struggled with the high dimensionality of long captions, our parsing approach maintained statistical robustness and semantic parsimony. Qualitative analysis on BiomedCLIP, validated on medical imagery (ROCOv2) and general examples, confirms that the approach accurately captures the synergistic influence of grouped words on model predictions. In conclusion, our work offers intuitive and clinically relevant insights into VLM decision-making, fulfilling the critical need for coherent explanations in the medical domain.

---


### 175. [Visualizing in the Mind's Eye: Icon Design Shapes Mental Imagery of Fire Risks](https://arxiv.org/abs/2607.23369)

**<font color=#1a73e8>作者：</font>** Wen Xu, Anjana Arunkumar, Lace M. Padilla  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce mental imagery, or seeing images in the "mind's eye," as a cognitive process that can be shaped by data visualization design and in turn impact decisions. We found in a preregistered study (n = 400) that abstract geometric icons visualizing fire risk data evoked more mental images than concrete house-on-fire icons, and also produced more diverse and personalized mental images. Mediation analysis showed that increased mental imagery subsequently led to risk-averse decisions through evoking negative affect. These findings reveal a nuanced mechanism through which visualization concreteness influences decisions: concrete designs may actually suppress affect-driven behavior by restricting mental imagery.

---


### 176. [Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social Sentiment and Technical Features](https://arxiv.org/abs/2607.23370)

**<font color=#1a73e8>作者：</font>** Muhammad Abdullah Haroon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bitcoin price prediction on sub-daily timescales is a hard open problem in computational finance. Bitcoin exhibits fat-tailed returns, non-stationary dynamics, and a price discovery process influenced by social discourse on Reddit and Twitter. Conventional approaches fuse OHLCV technical features with sentiment via static concatenation, applying identical fusion weights regardless of market state. This is inconsistent with the behavioural finance literature, which shows that retail sentiment is most predictive during volatile periods and noisy during calm ones. This paper proposes Regime-Aware Multi-Modal Learning (RAML), which conditions fusion of sentiment and price features on a dynamically detected binary market regime. Rolling 24-hour volatility partitions observations into stable and volatile regimes; a learnable sigmoid gate adjusts the weight of the sentiment embedding relative to the price embedding, trusting sentiment more during volatility and price dynamics more during stable phases. The system is evaluated on 3,491 hourly observations (July 2024-September 2025), combining Bitcoin OHLCV data with Reddit /r/Bitcoin FinBERT sentiment. Four models are compared - price-only BiLSTM, sentiment-only classifier, static-concatenation BiLSTM, and RAML - across 3-hour and 6-hour horizons, with an ablation study isolating the sentiment branch, regime detection, and adaptive fusion. RAML achieves macro-F1 of 0.5474 (3h) and 0.5513 (6h), with the highest AUC at 3 hours (0.5084), indicating better calibration. Ablation confirms every component is necessary, and replacing adaptive weighting with concatenation causes recall collapse at 6 hours (F1: 0.14). These results establish regime-conditioned adaptive fusion as a necessary design principle for multi-modal financial forecasting.

---


### 177. [When Activation Oracles Learn Not to Read: Concept-Specific Blind Spots in Fine-Tuned Oracles](https://arxiv.org/abs/2607.23379)

**<font color=#1a73e8>作者：</font>** Tobias Bersia, Tatiana Gaintseva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation Oracles (AOs) are language models trained to answer natural-language questions about another model's internal activations. They offer a flexible interface for reading hidden information from model states, especially when relevant information is internally represented but absent or incomplete in visible behavior. However, AOs are themselves learned systems: their answers are shaped by training data, objectives, and learned reporting behavior, rather than being neutral readouts of represented information. We study this in a controlled Taboo Word Guessing setting, where subject models are fine-tuned to internally use a hidden concept while avoiding direct disclosure. Contrary to the expectation that an AO trained on such a subject becomes a specialist reader, we find that fine-tuned AOs can become concept-specific anti-readers: they selectively fail to recover the concept persistently present during their own training. This failure is not simply explained by absence of the concept from the subject or oracle representations: the target remains decodable inside the oracle, while LogitLens and layer-ablation analyses indicate that the failure arises in the AO readout pathway. Our results show that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising a reliability concern for learned interpretability interfaces.

---


### 178. [Directional Influence Function: Estimating Training Data Influence in Constrained Learning](https://arxiv.org/abs/2607.23388)

**<font color=#1a73e8>作者：</font>** Xin Wang, R. Tyrrell Rockafellar, Xuegang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As constrained learning becomes increasingly common, models are trained under explicit feasibility requirements to enforce fairness, safety, robustness, regulariza- tion, and physics or logic constraints. Understanding how training samples in- fluence the model solution (e.g., learned parameters) is crucial for interpretability and robustness. The classical influence function (IF) estimates sample contribu- tions via local sensitivity analysis, measuring how the solution changes when a specific training sample is perturbed or removed. However, IF becomes unreli- able in constrained settings: data perturbations can reshape both the objective and the feasible region, leading to estimates that violate feasibility. In response, we propose the Directional Influence Function (DIF), a novel estimator that explicitly incorporates these constraints into influence estimation. DIF formulates the opti- mality conditions of constrained learning as a variational inequality (VI) and ana- lyzes how perturbing training data affects this VI. We validate DIF on constrained linear regression and demonstrate that it recovers leave-one-out retraining results, whereas IF and penalty-based IF exhibit significant bias. We further apply DIF to fairness-constrained CNNs, where DIF accurately predicts test loss changes under data removal and aligns closely with actual retraining. Our results establish DIF as an efficient and reliable tool for data attribution in constrained learning.

---


### 179. [Rendering on Real Silicon: GPU Render-Timing as a Passive, AI-Resistant CAPTCHA Signal](https://arxiv.org/abs/2607.23389)

**<font color=#1a73e8>作者：</font>** David Noever, Forrest McKee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Conventional CAPTCHAs pose puzzles that modern AI systems increasingly solve, while behavioral and cryptographic-attestation defenses carry privacy or enrollment costs. We investigate an orthogonal signal: the physical timing behavior of a client's GPU under a controlled WebGL rendering workload. Unlike WebGL fingerprinting, which hashes pixel output into a static device identifier, we measure render-timing dynamics to classify rather than identify, leaking no persistent identifier. We characterize the in-the-wild adversary with a 12-hour passive deployment (207 unsolicited requests; 86% automated; 85% of browser-claiming clients failed HTTP header-consistency checks). We then collect labeled GPU-timing samples through a single public endpoint exercised by real browsers (positive class, 13 distinct GPUs) and by keyed headless automation across a render-backend matrix (negative class). Software-rendered automation -- empirically the dominant real-world adversary -- separates from genuine GPUs by roughly 5x in mean render time. On a confound-controlled comparison (identical GPU family and browser engine, differing only in headless vs. interactive execution), headless automation on real hardware still exhibits a distinct timing signature, separating from human samples by 75-106% on frame jitter, timer-quantization ratio, and coefficient of variation. We report these as pilot-scale findings on a single GPU architecture and outline the cross-architecture collection required to establish generalization.

---


### 180. [When Can Depth Replace Precision? A Resource Theory of Quantized Neural Computation](https://arxiv.org/abs/2607.23390)

**<font color=#1a73e8>作者：</font>** Mojtaba Soltanalian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When can additional low-bit residual computation replace missing numerical precision for a fixed input-output map? We model a quantized residual system over a fixed horizon as a pure schedule selecting fields from a declared low-bit operation library, and use relaxed controls to characterize its infinite-depth limit. The distance from the target to the closed relaxed reachable set is the exact structural floor: no increase in depth can remove it for that library. Pure schedules approach the relaxed class at rate $O(D^{-1})$ under bounded-variation time dependence and $O(D^{-\vartheta}+D^{-1})$ under Holder dependence of exponent $\vartheta$. Execution arithmetic can reverse this conclusion: full-state write-back introduces a $D\rho_z$ penalty and can freeze residual updates, whereas increment error feedback replaces this growth by a bounded carry term and obeys an exact common-lattice conservation law. A fixed-teacher converse makes this rate sharp: for coherent depth-$L$ first-order high-precision comparators, accuracy matching requires $D=\Theta(L)$. Learned codebooks add a metadata resource, while state-dependent routing introduces hybrid event conditions. Verified primal and dual bounds yield feasible, impossible, or unresolved decisions before training. Companion software implements the workflow, and Lean 4 machine-checks the exact discrete core. Depth replaces precision only relative to a declared library, horizon, execution semantics, and routing model.

---


### 181. [Key-Interval A*: Accelerating Grid Pathfinding via Structural Abstraction](https://arxiv.org/abs/2607.23393)

**<font color=#1a73e8>作者：</font>** Taiquan Sui  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing exact methods for 4-connected grid pathfinding reduce online search, but often either retain fine-grained search states or require substantial preprocessing. This paper presents Key-Interval A* (KIA*), an optimal pathfinding algorithm that uses lightweight preprocessing to construct and search over a compact interval-level abstraction of free space. KIA* represents free space using intervals: maximal contiguous runs of traversable cells. It extracts key intervals that capture structural boundary changes and connects them through contiguous non-key regions. KIA* then performs A*-style search on the resulting key-interval graph and constructively reconstructs grid paths from interval chains, without cell-level local search. We prove the completeness and optimality of KIA* on 4-connected grids. Experiments on standard benchmarks show that KIA* preserves exact shortest-path lengths and achieves the fastest runtime on seven of eight benchmark groups, with the largest gains on structured and game maps.

---


### 182. [A Statistical Difference between Single-Layer Learning and Hierarchical Learning in Wide Neural Networks](https://arxiv.org/abs/2607.23397)

**<font color=#1a73e8>作者：</font>** Sumio Watanabe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical neural networks are widely used in artificial intelligence, yet their mathematical properties remain incompletely understood. In the infinite-width limit, two different theoretical frameworks have been proposed. One reduces deep learning to kernel regression with a fixed kernel by assuming that the parameters remain close to their initialization, whereas the other allows the parameters to move away from their initialization, requiring the kernel itself to be optimized.
In this paper, we study a three-layer neural network with a finite but large number of hidden units. We show that training the input-to-hidden weights yields a smaller generalization error than keeping them fixed. Furthermore, the latter setting exhibits singularities in the parameter space, whereas the former does not. These findings indicate that singularities play an essential role even in wide neural networks.

---


### 183. [Transfer Learning Architectures for Scalable Multi-Fidelity Bayesian Optimization](https://arxiv.org/abs/2607.23404)

**<font color=#1a73e8>作者：</font>** Jaewook Lee, Ethan Errington, Christian D. Lorenz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-driving laboratories increasingly rely on multi-fidelity Bayesian optimization (MFBO) to balance cheap, approximate evaluations against scarce, expensive ones, with a predictive surrogate at its core. Gaussian processes (GPs) are the default choice, but they scale poorly as data accumulate and assume a smooth landscape that molecular and materials search spaces routinely violate. Transfer learning offers an alternative suited to this regime: it learns a representation from abundant cheap data and adapts it to sparse expensive data. Despite its use in property prediction, transfer learning has not been tested as the engine of a closed-loop optimization. Here we benchmark eleven transfer-learning surrogates against four GP methods under an identical selection rule, fidelity budget, and model size, across nine tasks spanning synthetic functions to real chemistry and materials problems. GPs win on smooth, low-dimensional functions but perform worst on molecular and materials problems, where transfer-learning surrogates reach substantially better solutions using far less computation. Because acquisition policy is held fixed across surrogates, this advantage is attributable to the surrogate itself. Uncertainty-driven exploration is not reliably beneficial, and calibration does not predict optimization performance, so greedy exploitation of the transfer-learned mean is the more robust default. Transfer learning is therefore the surrogate of choice for molecular and materials MFBO.

---


### 184. [Blood Pressure Estimation from PPG: A Comparative Study of Direct and ECG-Mediated Deep Learning Pipelines](https://arxiv.org/abs/2607.23406)

**<font color=#1a73e8>作者：</font>** Bo Wu, Haoling Wang, Zhuodiao Kuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous cuffless blood pressure (BP) monitoring is essential for connected health systems and wearable devices, enabling early detection, longitudinal tracking, and personalized management of cardiovascular disease. Many prior approaches attempt to estimate BP indirectly by reconstructing electrocardiography (ECG) from photoplethysmography (PPG), assuming ECG provides a stronger physiological link to BP. However, ECG sensing is less accessible in wearable settings and may introduce unnecessary complexity.
In this work, we first perform a large-scale physiological correlation analysis on the MIMIC-III waveform database, revealing that PPG exhibits substantially stronger coupling with arterial blood pressure (ABP) ($|r|=0.247$, $p<0.001$) than ECG does ($r=0.018$, $p=0.187$), challenging the assumption that ECG provides a superior intermediate representation. Motivated by this insight, we conduct a systematic comparison between direct PPG-to-BP prediction and ECG-mediated pipelines using multiple state-of-the-art deep learning models.
Across 1.74M segments from 3,127 patients, direct PPG-to-BP prediction achieves British Hypertension Society Grade A performance ($\mathrm{MAE}_{\mathrm{SBP}} = 4.82 mmHg$, $\mathrm{MAE}_{\mathrm{DBP}} = 4.31 mmHg$), outperforming all ECG-mediated approaches, which achieve only Grade B accuracy.
Our findings suggest that accurate continuous BP monitoring can be achieved directly from wearable PPG signals, enabling simpler, more efficient pipelines for real-world connected health systems.

---


### 185. [NeurGO: Learning to Generate Elite Candidates for Meta-Black-Box Expensive Optimization](https://arxiv.org/abs/2607.23408)

**<font color=#1a73e8>作者：</font>** Jintao He, Huixiang Zhen, Wenyin Gong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Expensive black-box optimization is ubiquitous in science and engineering, where function evaluations are costly and the evaluation budget is limited. Traditional evolutionary algorithms and Meta-BlackBox Optimization (MetaBBO) approaches typically consume most evaluations on candidate selection, often wasting precious budget on inferior solutions. Although surrogate-assisted evolution and Bayesian optimization aim to reduce evaluations through surrogate models, constructing an accurate global model from limited data remains challenging, and model bias can easily trap the search in local optima. To overcome these limitations, we propose NeurGO, a generative MetaBBO framework that directly synthesizes elite candidates from historical population states. Specifically, we employ an attention-based encoder to capture the population-level search trend and condition a decoder on this representation to generate high-quality candidates, avoiding the expensive evaluation of large offspring pools. We then design a quality-diversity loss to maintain solution quality and population diversity throughout the search. Through extensive benchmarking on CEC 2008 and the COCO BBOB test suites, our method achieves better optimization performance under the same evaluation budget and exhibits faster convergence.

---


### 186. [Harmonized Interpretable ECG Waveform Features for Robust Cross-Dataset Clinical Prediction](https://arxiv.org/abs/2607.23412)

**<font color=#1a73e8>作者：</font>** Jie Lin, Weijie Sun, Sunil V. Kalmady 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiograms (ECGs) are widely used for cardiovascular risk prediction, yet models often fail to transfer across hospitals because of protocol, population, and measurement differences. We benchmark cross-dataset generalization on three tasks - heart failure classification, 30-day all-cause mortality, and 30-day mortality among sinus-rhythm ECGs - using two large cohorts (MIMIC-IV and the Alberta Cohort). To reduce vendor-specific measurement mismatch, we build a harmonized, interpretable feature representation computed directly from raw waveforms: FeatureDB morphology/heart-rate-variability summaries plus compact time-frequency descriptors (autoregressive and wavelet features). We train XGBoost models on this unified feature space and evaluate with patient-disjoint internal and bidirectional external testing. We pre-specify two hypotheses: (H1) external AUROC retains at least 90% of source-site internal AUROC under transfer, and (H2) internal AUROC of the harmonized feature set stays within 10% of dataset-native machine-measurement models. Across tasks, internal AUROC is 0.79-0.82 and cross-dataset AUROC is 0.74-0.78, with larger and direction-dependent AUPRC shifts under transfer. As an exploratory benchmark, an end-to-end ConvNeXt model trained directly on raw ECG waveforms with age and sex achieves higher internal AUROC, while the harmonized representation remains competitive in relative cross-dataset transfer stability. These findings show that a consistent waveform-derived feature interface preserves performance, supports realistic external validation, and provides a transparent alternative for cross-site clinical prediction.

---


### 187. [Early Detection of Hardware Trojans Using Neural Controlled Differential Equations and Analysis of Power Traces](https://arxiv.org/abs/2607.23417)

**<font color=#1a73e8>作者：</font>** Hasala Senevirathne, Rahul Vishwakarma, Amin Rezaei  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Evolving Hardware Trojans pose a serious threat to modern digital systems by evading traditional detection through stealthy, adaptive behavior. Even recent methods that leverage advances in machine learning can only detect them after activation, leaving a critical window for potential security breaches. To address this gap, we propose a novel approach for hardware Trojan detection and prediction using Neural Controlled Differential Equations (NCDEs) and analysis of power traces. Our method leverages an NCDE model trained exclusively on Trojan-free data to learn nominal power behavior, combined with a Linear Discriminant Analysis (LDA) classifier calibrated on labeled data, to distinguish between three scenarios: no Trojan, dormant Trojan, and active Trojan. Our method uses a sliding window to process side-channel measurements, enabling detection of subtle power consumption deviations that indicate Trojan presence, even when dormant. Experimental results demonstrate that the proposed NCDE-based method achieves superior accuracy compared to traditional machine learning approaches, with the additional advantage of handling dormant Trojans above a sensitivity threshold. We validate our approach on standard hardware Trojan benchmarks, showing robust detection and prediction performance.

---


### 188. [TroPUF: Evaluating Hardware Trojan Insertion in Delay-Based Physical Unclonable Functions](https://arxiv.org/abs/2607.23418)

**<font color=#1a73e8>作者：</font>** Marissa Marcarelli, Amin Rezaei  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Delay-based Physical Unclonable Functions (PUFs) are commonly used for device authentication and key generation due to the fact that they rely on manufacturing induced delay variations. However, these same variations make PUFs inherently non-deterministic, which can allow malicious logic to blend in with normal circuit behavior. As a result, the act of embedding hardware Trojans directly inside the PUF primitive presents a unique security risk that is not yet well understood. This work presents a unified simulation framework for evaluating stealthy hardware Trojan insertion across multiple delay-based PUF architectures and Trojan types. Functional metrics, hardware overhead, and resistance to machine learning modeling are assessed in parallel. Results show that dormant Trojans preserve expected PUF behavior, structural characteristics, and modeling resistance. Detectable degradation appears only after activation, indicating that conventional validation techniques fail to identify embedded Trojans prior to payload execution. These findings expose a gap in current PUF security assumptions, and highlight the need to evaluate PUFs and hardware Trojans as a coupled security problem.

---


### 189. [PATCH-FFT: Unmasking Dormant Hardware Trojans with Patch-Based Frequency-Domain Transformers](https://arxiv.org/abs/2607.23421)

**<font color=#1a73e8>作者：</font>** Hasala Senevirathne, Amin Rezaei  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware Trojans embedded by malicious entities in integrated circuits can covertly leak sensitive information through power side channels, often remaining undetected in their dormant state until specific trigger conditions activate their malicious behavior. For information-leaking Trojans, detection in the dormant state is critical, as once triggered, the secret data is already exfiltrated. This paper introduces a patch-based Transformer architecture for detecting dormant hardware Trojans through frequency-domain analysis of power traces. Our approach converts time-domain power measurements into frequency-domain representations using real Fast Fourier Transform (rFFT), revealing spectral signatures hidden in conventional time-series analysis. Experimental results demonstrate that our method achieves 90.94% average detection accuracy across dormant and active Trojan scenarios, outperforming state-of-the-art approaches particularly in detecting dormant Trojans that prior time-domain methods do not address.

---


### 190. [Short-Term Pain for Long-Term Gain: Adaptive Experiment with Post-Commitment Reward Shift](https://arxiv.org/abs/2607.23432)

**<font color=#1a73e8>作者：</font>** Puping Jiang, Wei Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-makers in learning environments face a dilemma when their short-term optimal actions may not favor their long-term benefits the most. To understand the fundamental tradeoff behind the dilemma, we study adaptive experimentation with post-commitment reward shifts. During an experiment phase, the decision-maker may adaptively test multiple options; during a subsequent commitment phase, the decision-maker must commit to a single option, whose reward may differ from its pre-commitment reward. We propose the Reserved Arm Eliminations for Commitment (RAEC) algorithm, which reserves a predetermined portion of the experiment phase to identify the best post-shift option while using the remaining rounds to minimize short-run regret. We establish regret upper bounds for RAEC across all parameter regimes and matching minimax lower bounds, providing a tight characterization of the cost of balancing short-term performance and long-term commitment.
We also study two extensions. With prior structural knowledge linking pre- and post-shift rewards, we show that correctly identifying the ranking-changing component of the shift is more important than estimating its absolute magnitude. For settings with concave commitment rewards and portfolio choice, we develop the Reserved Online Stochastic Convex Optimization for Commitment (ROSCOC) algorithm, which directly converts its reserved exploration history into a commitment portfolio and achieves tight regret bound. Finally, we also conduct numerical experiments which confirm that our proposed algorithms achieve the desired regret predicted by our theory, and also outperform other baseline algorithms.

---


### 191. [Renting the Cracking Machine with a Cost-and-Time Analysis of Exhaustive DES-56 Key Search in the Cloud](https://arxiv.org/abs/2607.23443)

**<font color=#1a73e8>作者：</font>** Gonzalo Sharif Curi Martínez, Rodrigo Ramele  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Data Encryption Standard (DES), with its 56-bit key, has been considered cryptographically broken since 1998. However, a concrete, reproducible measurement of the cost and time required to perform an exhaustive key search using today's commodity cloud infrastructure has not been widely reported in recent literature. In this paper we present a distributed brute-force system built on AWS EC2 that partitions the $2^{56}$ keyspace across 37 \texttt{c6i.2xlarge} instances running a C/OpenMP worker, achieving a measured throughput of $2.91$\,M\,keys/s per instance (${\sim}108 \times 10^6$ keys/s aggregate). We conduct 15 independent trials covering keyspace offsets from $10^6$ to $1.5 \times 10^{10}$ keys, measuring wall-clock time and monetary cost per trial. For small offsets ($\leq 10^8$), total time is dominated by AWS instance boot latency (${\approx}\;90$\,s), yielding a mean of $116.8\pm20.1$\,s at \$0.41 per attack. For larger offsets the search time dominates and grows linearly: a key at offset $1.5{\times}10^{10}$ requires ~${\approx} \; 87$ minutes and \$18. At the measured aggregate throughput of 108\,M\,keys/s, exhausting the full $2^{56}$ keyspace with these 37 instances would take ${\approx} \; 21$ years; however, because the workload is embarrassingly parallel and cloud capacity is elastic, the same search can be traded for money almost linearly. Extrapolating our measured cost, a complete exhaustive search would cost ${\approx} \; \$1.2$M and, with a sufficiently large fleet, could be completed in about one day. The system is thus practical for bounded-subspace attacks at negligible cost, and full DES exhaustion, while expensive, is firmly within reach of a well-funded attacker using only commodity cloud resources.

---


### 192. [PerturbPFN: Probing the Limits of Synthetic Priors in Drug Perturbation Modelling](https://arxiv.org/abs/2607.23447)

**<font color=#1a73e8>作者：</font>** Yuche Gao, José Miguel Hernández-Lobato, Siyuan Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting cellular responses to unseen chemical perturbations is challenging due to unknown targets and mechanisms, high-dimensional expression responses, and limited experimental coverage of the large small-molecule design space. We propose PerturbPFN, a PFN-style amortized model for unknown-target perturbation prediction under a hierarchical synthetic structural prior. Instead of directly regressing high-dimensional expression responses, PerturbPFN infers a latent system graph, sparse atomic intervention targets, and intervention strengths, then propagates their effects through an SCM decoder. The model is trained entirely on prior-predictive synthetic episodes generated from biologically motivated graph and expression simulators, enabling structured in-context learning without test-time gradient updates. We evaluate PerturbPFN on both real single-cell perturbation data and synthetic benchmarks, covering effect prediction, target identification, and regulatory structure discovery. Our results show that PerturbPFN offers a complementary trade-off to specialized baselines, achieving competitive perturbation prediction with low inference cost while exposing interpretable intermediate estimates of targets, strengths, and system structure.

---


### 193. [Local Regularization Does Not Characterize Multiclass PAC Learnability](https://arxiv.org/abs/2607.23449)

**<font color=#1a73e8>作者：</font>** Eric Hou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local regularization assigns each hypothesis a test-point-dependent score and predicts with a minimum-score hypothesis consistent with the sample. Asilis et al. asked whether this principle characterizes multiclass PAC learnability. We give a negative answer. There is a countable class of Daniely--Shalev-Shwartz dimension at most two with realizable PAC sample complexity \[ O\!\left(\frac{1}{\varepsilon}\log\frac{1}{\delta}\right), \] that no local regularizer learns. Hypotheses are edges of complete graphs and instances are tournaments. At a test tournament, the scores fix an edge ranking while the training sample independently removes competitors. Cyclic triangles force enough inversions that surviving competitors produce constant population error at arbitrarily large sample sizes.

---


### 194. [Multi-Modal Object Re-Identification with Prompt-S6 and Semantic-Aware Knowledge Guidance](https://arxiv.org/abs/2607.23451)

**<font color=#1a73e8>作者：</font>** Weixiang Zhou, Jiabei Zuo, Yuhao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal object Re-Identification (ReID) aims to retrieve specific objects by integrating complementary information from multiple modalities. However, existing multi-modal ReID methods do not effectively address background interference suppression or achieve tri-modal alignment, instead focusing on pairwise feature fusion. Moreover, many current aggregation approaches suffer from high computational complexity. To address these limitations, we propose PRISM, a novel multi-modal ReID framework built upon Prompt-S6 (PS6) and semantic-aware knowledge guidance. PS6 maintains the linear complexity and strong sequence modeling capability of Mamba while enabling efficient cross-modal interaction. Leveraging these advantages, we design two key components: Semantic-Driven Token Pruning (SDTP) and Progressive Fusion Network (PFN). Parsing semantic priors from the segmentation foundation models, the SDTP then leverages these priors and applies dynamic token pruning to suppress background noise and refine feature representations. The PFN progressively aggregates multi-modal features to achieve tri-modal alignment and fully exploit modality complementarity. With the proposed modules, PRISM generates more robust multi-modal representations under complex scenarios. Extensive experiments on four multi-modal object ReID benchmarks demonstrate the effectiveness and efficiency of our approach. The source code is available at this https URL.

---


### 195. [Generalization bounds and sample complexity for remaining useful life prediction from complete degradation trajectories](https://arxiv.org/abs/2607.23454)

**<font color=#1a73e8>作者：</font>** Huy Hoang Le, Kim-Anh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven remaining useful life (RUL) prediction requires complete degradation trajectories for training, yet such run-to-failure data are scarce and expensive. Practitioners currently lack principled guidance on how many failure examples suffice for a given model and accuracy target. This paper develops a sample complexity framework for RUL prediction comprising seven main results organised around three themes. First, we establish fundamental learning rates: a distribution-free generalization bound shows that the uniform deviation of the mean squared error decreases as $O(B^{2}\sqrt{p/n})$, where $p$ is the model complexity and $n$ the number of trajectories, and a minimax lower bound proves that the $\Theta(p/n)$ rate is unimprovable.} \rev{Second, we quantify how domain knowledge accelerates learning: incorporating degradation physics reduces data requirements by up to two orders of magnitude for deep networks, a Bernstein-type analysis achieves the minimax-optimal $O(p/n)$ rate under high signal-to-noise conditions, and closed-form penalties reveal when an incorrectly assumed physics model hurts rather than helps. Third, we characterise the impact of data quality: fleet variability induces an irreducible bias$-$variance tradeoff, while right-censored observations suffer an efficiency loss that depends critically on the degradation class.} Closed-form expressions are provided for exponential, power-law, and stretched-exponential degradation. \rev{Cross-domain validation against published turbofan, battery, and bearing benchmarks confirms the theoretical predictions within a factor of 2$-$3 on average. The results yield practical guidelines for planning data collection, selecting model complexity, and evaluating physics model assumptions in prognostics applications.

---


### 196. [Two Regimes of Chain-of-Thought Unfaithfulness: Behavioral Detection Fails Where Models Are Wrong](https://arxiv.org/abs/2607.23458)

**<font color=#1a73e8>作者：</font>** Suramya R. Angdembay, Dikshant Aryal, Nick Rahimi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) explanations support oversight only if they are faithful: the stated reasoning must actually produce the answer. Auditing black-box (behavioral) detection of unfaithful CoT against FaithCoT-Bench's human annotations, we find answer correctness structures the problem at every level. Answer incorrectness alone (an oracle diagnostic, not a deployable detector) outperforms every purpose-built signal (AUROC 0.696), because 69% of annotated unfaithfulness occurs on incorrect answers. Stratifying by correctness splits detection into two regimes: on correct answers, behavioral signals moderately separate faithful from post-hoc reasoning (0.63-0.67); on incorrect answers, where most unfaithfulness lives, no tested signal is detectably above chance (replicated on all four models for benchmark-wide signals). The standard step-removal metric anti-correlates with human labels; this inversion reproduces on the benchmark's released scores and on hint-dependent counterfactually labeled traces. Linear probes decode the behaviorally blind regime in Llama-3.1-8B and the correct-answer regime in Qwen-2.5-7B, with no shared, positively aligned direction detected across regimes; instructed answer-first traces (7 models) transfer to neither annotated regime, while hint-induced unverbalized answer flips do, in model- and source-dependent settings. We also independently verify and resolve a documentation-data mismatch in the benchmark's label semantics.

---


### 197. [Extending Fourier Neural Operators for Modeling Parameterized and Coupled PDEs](https://arxiv.org/abs/2607.23466)

**<font color=#1a73e8>作者：</font>** Cheng Jing, Uvini Balasuriya Mudiyanselage, Abhishek Verma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameterized and coupled partial differential equations (PDEs) are central to modeling phenomena in science and engineering, yet neural operator methods that address both aspects remain limited. We extend Fourier neural operators (FNOs) with minimal architectural modifications along two directions. For parameterized dynamics, we propose a hypernetwork-based modulation that conditions the operator on physical parameters. For coupled systems, we conduct a systematic exploration of architectural choices, examining how operator components can be adapted to balance shared structure with cross-variable interactions while retaining the efficiency of standard FNOs. Evaluations on benchmark PDEs, including the one-dimensional capacitively coupled plasma equations and the Gray-Scott system, show that our methods achieve up to 55-72% lower errors than strong baselines, demonstrating the effectiveness of principled modulation and systematic design exploration.

---


### 198. [Learning to Optimize: Joint Routing and Flow Allocation on Sparse Non-Euclidean Networks](https://arxiv.org/abs/2607.23467)

**<font color=#1a73e8>作者：</font>** Haomiao Sun, Fang He, Congyuan Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study an integrated pickup-and-delivery problem on sparse, non-Euclidean networks that jointly optimizes cyclic routing, cargo flow allocation, and cross-cycle service. The tight coupling of these operational constraints creates a complex discrete-continuous decision space with highly restricted feasible regions. To overcome these computational challenges, we propose Double-Channel Graph Attention (DCGA), an end-to-end reinforcement learning framework. DCGA isolates network reachability and demand-service logic into separate graph channels and constructs valid routes using a simulator-coupled, constraint-informed decoder. Experiments on LinerLib benchmarks demonstrate that DCGA achieves seconds-level inference and delivers state-of-the-art solution quality on instances beyond a specific scale, with its advantage over existing baselines widening significantly as problem size increases. Supported by extensive stability and ablation analyses, our results demonstrate that this structure-aware learning approach provides an effective, low-latency engine for realistic routing-and-flow optimization.

---


### 199. [Robust 6-DoF Object Pose Tracking with Built-In Recovery under Occlusions and Rapid Object Motions](https://arxiv.org/abs/2607.23468)

**<font color=#1a73e8>作者：</font>** Balázs Opra, Léo Ghafari, Thomas Stewart 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time 6-DoF object pose tracking is essential for many robotics applications, and several approaches exist. Yet even today's approaches remain unreliable under temporary full occlusions and rapid object motions. Once tracking is lost, most methods struggle to detect the failure and recover automatically, often requiring manual re-initialization. In this paper, we address the problem of robust model-based 6-DoF tracking of unseen objects from RGB-D data, especially in scenarios with occlusion and fast motion. We propose a novel method that combines efficient learning-based keypoint matching with optimization-based alignment and introduces a novel failure detection and recovery module. Our system monitors pose reliability, detects tracking divergence or occlusions, and performs a global re-detection and pose estimation step that robustly verifies recovery candidates before resuming tracking. Our evaluation on standard tracking benchmarks and on a new dataset of occluded and fast-moving scenes shows that our method matches state-of-the-art accuracy on easy tracking sequences, maintains high tracking speed at 57.6 frames per second, and provides the most robust tracking performance under challenging conditions. Thus, we believe that our approach is a relevant step forward in robust 6-DoF object tracking from RGB-D data.

---


### 200. [Sparse Gaussian-Mixture-Model Q-Functions via Hadamard Overparametrization for Online Reinforcement Learning](https://arxiv.org/abs/2607.23474)

**<font color=#1a73e8>作者：</font>** Minh Vu, Konstantinos Slavakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops an online, off-policy policy-iteration framework for reinforcement learning (RL), based on sparse Gaussian-mixture-model Q-functions (S-GMM-QFs). The framework reconciles streaming, non-stationary data with the Riemannian structure of the parameter space while handling distributional mismatch through experience replay. S-GMM-QFs are introduced via Hadamard overparametrization, enabling interpretable sparsification through smooth regularization that facilitates Riemannian-based optimization. Overparametrization allows the framework to adaptively identify meaningful components from a large initial pool, yielding sparse models where interpretability emerges naturally from geometry: each component's parameters (means and covariances) explicitly encode its geometric role in the ambient state-action space. These geometric roles are learned through online gradient descent on a smooth objective over a (Cartesian-product) Riemannian manifold. Numerical tests demonstrate that S-GMM-QFs match or exceed deep RL methods while using substantially fewer parameters and achieving faster improvement per observed transition. Notably, parameter efficiency and interpretability combine to maintain strong generalization in low-parameter regimes where sparsified deep RL approaches degrade.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-442](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
