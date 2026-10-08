# 🧠 大模型相关研究 | 2026年10月09日

> 本类共 **266** 篇论文：已确认 **245** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-266](./part-06.md)

---

### 201. [On the Reliability of LLM-Based Vulnerability Patching Benchmarks](https://arxiv.org/abs/2610.10150)

**<font color=#1a73e8>作者：</font>** Dang K Le, Wenxuan Shi, Xinyu Xing  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong potential for automated vulnerability patching, but current benchmarks can substantially distort reported performance. Drawing on extensive experience developing, running, and stress-testing such frameworks, we identify under-examined pitfalls across three dimensions: (1) agent-level factors, where prompting, tool availability, and detailed instructions can raise success rates without improving developer-aligned patch quality; (2) framework-level factors, where permission errors, infrastructure bugs, and timeout handling can silently suppress or inflate performance; and (3) dataset-level factors, where bug reports and single proof-of-concept (PoC) tests fail to capture whether patches address root causes or follow developer intent. We curate 112 historical bugs from 84 open-source C/C++, Go, and Rust projects, each with PoC tests, regression tests, and additional developer tests that assess alignment with the original developers' design principles. Through controlled experiments and case studies, we show that LLMs can achieve high PoC passing rates under ideal conditions, yet benchmark execution choices can materially change measured success. More importantly, developer-test passing rates remain low and improve only marginally with newer models, suggesting that models increasingly suppress symptoms without consistently producing upstream-quality fixes. These results show that benchmark scores are highly sensitive to evaluation design, and we provide practical guidelines for more rigorous, reliable, and reproducible evaluation.

---


### 202. [HeiCo-FOCUS: A Clinically Grounded Dataset for Long-Context Video Understanding](https://arxiv.org/abs/2610.10156)

**<font color=#1a73e8>作者：</font>** Leon Mayer, Lucas Luttner, Patrick Godau 等 45 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Vision-Language Models (VLMs) have led to rapid progress in video understanding across a wide range of benchmark tasks. However, existing evaluations largely focus on short-term reasoning, failing to assess a critical capability: maintaining cumulative temporal consistency over extended time horizons. To close this evaluation gap, we introduce HeiCo-FOCUS, a clinically grounded dataset for evaluating long-context video understanding through the task of Foreign Object Contextual Understanding in Surgery. Built on a dataset of Heidelberg Colorectal surgeries, this task requires models to continuously track multiple objects as they are inserted, manipulated, occluded, and removed over procedures lasting up to hours. HeiCo-FOCUS comprises 30,000 visual question answering (VQA) pairs covering five core capabilities: object recognition, temporal grounding, aggregation, event and procedural understanding, and complex reasoning. The dataset was constructed through a rigorous multi-stage annotation pipeline involving large-scale crowd annotation and 39 surgical domain experts to ensure high quality and clinical relevance. To systematically probe model behavior, we introduce a multi-track evaluation framework that progressively increases temporal and contextual demands from single frames to full procedures. Experiments with ten frontier VLMs show that HeiCo-FOCUS tasks are far from solved: only around half of the models clearly outperform a text-only baseline. Across the video tracks, models perform best on event and procedural understanding (mean Accuracy: 56.5% across all models), while temporal grounding remains particularly challenging for all evaluated models (mean Accuracy: 19.7%). We therefore expect HeiCo-FOCUS to serve as a catalyst for the development of models capable of reliable, temporally consistent reasoning over hours-long videos.

---


### 203. [Beyond Anonymous Captions: Grounding Character Identity in Video Captioning and Question Answering](https://arxiv.org/abs/2610.10163)

**<font color=#1a73e8>作者：</font>** Anas Filali Razzouki, Killian Steunou, Khalil Guetari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Linking people's appearance and actions to character identities is essential for understanding video narratives. We present a framework for identity-aware video captioning and person-centric question answering that combines automatic character identification, explicit spatial grounding, and task-specific adaptation. Starting from LSMDC v2 movie clips, our pipeline matches detected faces to actor reference images, tracks characters across frames, and builds inputs with identity-linked bounding boxes. A strong vision-language model generates identity-aware captions and questions, which are manually verified and filtered to create a benchmark of 750 captioned clips and 3,000 person-centric questions. We study five grounding strategies combining textual coordinates with visual face or estimated person boxes across Video-MLLM families at roughly 2B, 4B, and 8B parameters and larger frontier models. Combining visual face boxes with textual coordinates yields the most consistent performance across scales and significantly improves overall performance over coordinates alone. Smaller models tend to over-assign known identities when the queried person is not grounded, while larger models better recognize such UNIDENTIFIED cases. We introduce BAC by LoRA fine-tuning Qwen models at 2B, 4B, and 8B scales on about 32K identity-aware captioned clips. Across all scales, BAC outperforms every other evaluated model family of comparable size. BAC-8B reaches 93.20\% overall QA accuracy, ranking behind only GPT-5.6 Sol among the frontier models evaluated in our study. Overall, explicitly communicating who is where, together with lightweight task-specific adaptation, substantially improves identity-aware video understanding without changing the underlying architecture. We release the benchmark, training data, code, and BAC checkpoints at this https URL.

---


### 204. [UniSkill: Learning Actor-Aligned Skill Proposals for an Evolving Policy](https://arxiv.org/abs/2610.10164)

**<font color=#1a73e8>作者：</font>** Yifei Lu, Cheng Liu, Dianzhi Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents can improve across tasks by retaining reusable skills distilled from prior interactions. Recent work jointly optimizes task execution and skill extraction, enabling the policy and skillbank to co-evolve. However, as the actor continues learning, rewarding skill proposals through their reuse in subsequent training steps may conflate skill benefits with actor improvement, while directly testing each proposed skill requires costly additional actor rollouts. In this paper, we introduce UniSkill, which uses a shared policy to interact with the environment and propose skillbank edits (Add, Update, or No Edit) from the resulting trajectories. Specifically, the actor learns from environment rewards, while contrastive action feedback guides skill proposal learning. This feedback provides an actor-alignment signal by measuring how replacing the retrieved skill with a proposed skill changes the current actor's action log-likelihood gap between previously collected successful and failed trajectories from the same task, thereby avoiding new rollouts for each proposal. Since proposal-level feedback may suppress an otherwise appropriate edit operation when the proposed skill content scores poorly, we further apply skill-edit support regularization to preserve exploration. Empirically, UniSkill achieves strong performance, reaching 98.4% success on ALFWorld and 84.7% on WebShop while maintaining stable joint training. Further ALFWorld experiments show that UniSkill remains effective when the shared policy uses a smaller backbone. Our implementation is available at this https URL.

---


### 205. [Beyond Outcome Rewards: Constructing and Assigning Retrieval Credit for Search Agents](https://arxiv.org/abs/2610.10179)

**<font color=#1a73e8>作者：</font>** Wenyu Huang, Xinyu Hou, Pavlos Vougiouklis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search agents enable Large Language Models (LLMs) to iteratively retrieve and use information for complex multi-hop questions. Reinforcement Learning with Verifiable Rewards (RLVR) offers a promising approach for post-training such agents, but its reliance on sparse, outcome-based supervision can make credit assignment difficult and limit learning efficiency. In this paper, we systematically investigate how intermediate supervision can improve reinforcement learning for search agents. We study a range of reward-shaping and credit-assignment strategies that provide learning signals from intermediate retrieval steps. Building on these insights, we develop a training framework that combines intermediate signals with final outcome rewards to improve learning from multi-step search trajectories. Experiments across multiple benchmarks under matched training conditions demonstrate improvements in aggregate search-agent performance and show that both the choice of intermediate signal and where its credit is assigned affect training behaviour. These findings show that reward design and credit assignment are important design dimensions for training effective search agents.

---


### 206. [VideoEvolve: Co-Evolving Memory and Retrieval for Long Video Understanding](https://arxiv.org/abs/2610.10183)

**<font color=#1a73e8>作者：</font>** Yongchao Xu, Bowen Ye, Jiefeng Gan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding increasingly relies on external memory to organize massive visual streams into compact representations. However, most memory-based methods dynamically adapt how information is retrieved for different questions, while largely fixing what is remembered. This mismatch makes missing details costly to recover, whereas stored information is valuable only when it can be reliably retrieved. To address this issue, we propose VideoEvolve, a novel self-evolving framework that jointly evolves memory and retrieval for long video understanding. Specifically, starting from a coarse low-frame-rate overview, VideoEvolve couples a Memory Evolver for selective memory augmentation with a Retrieval Evolver for adaptive retrieval over the evolving memory. We then co-evolve the two Evolvers through alternating agentic reinforcement learning (Agentic RL), updating one while freezing the other. To steer this alternating evolution, Bottleneck-Aware Evolution Feedback (BEF) identifies whether the current bottleneck lies in memory or retrieval and directs optimization toward the more limiting side. Furthermore, VideoEvolve introduces Capability-Aware Evolution Feedback (CEF) to alleviate downstream feedback from over-specializing memory to a fixed set of training questions, shifting training toward underdeveloped yet learnable video capabilities. By integrating Agentic RL with BEF and CEF, VideoEvolve transforms downstream reasoning experience into transferable capability updates, providing a concrete path from static long-video systems toward experience-driven, self-improving multimodal intelligence. Extensive experiments on multiple long video understanding benchmarks demonstrate the effectiveness of VideoEvolve.

---


### 207. [Agentic AI-Assisted Modeling for Production Scheduling: Assessment in Constraint Programming](https://arxiv.org/abs/2610.10184)

**<font color=#1a73e8>作者：</font>** Ángel Sánchez-Fernández, Javier Pernas-Álvarez, Diego Crespo-Pereira  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing optimization models for production scheduling requires substantial expert effort. Research on large language models (LLMs) has followed two directions: specialized approaches for automated modeling, mostly for mixed-integer linear programming, which often rely on dedicated training or problem-specific architectures that limit industrial deployment; and agentic artificial intelligence for operational decision support, which generally assumes that the optimization model already exists. This study bridges both directions by assessing whether general-purpose LLMs, orchestrated as agents without task-specific training, can formulate and implement constraint programming models from natural-language problem descriptions. Singleagent and multi-agent architectures are integrated with a Model Context Protocol server that provides context-aware retrieval of solver documentation to mitigate hallucinations during implementation. Both are compared with a direct LLM baseline on six industry-oriented problems covering flow-shop, job-shop, flexible job-shop and resource-constrained warehouse scheduling, using three LLMs and assessing modeling accuracy, execution success, latency and token consumption. Formulation proves largely within reach of current LLMs, whereas implementation is the main barrier. The multi-agent workflow raises the share of scripts that run correctly as generated from 14.8% with a direct LLM call to 59.3%, reaching 80.6% on the four less complex problems, while tightly coupled intralogistics models remain an open challenge.

---


### 208. [Robust Decentralized Fairness Auditing](https://arxiv.org/abs/2610.10199)

**<font color=#1a73e8>作者：</font>** Sayan Biswas, Jade Garcia Bourrée, Anne-Marie Kermarrec 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emerging legislation requires large language models (LLMs) to be audited for compliance with regulatory standards, particularly fairness. Such black-box audits typically assume a single auditor with access to a large, representative set of queries. In practice, it can be difficult for an auditor to obtain such a query set, but multiple auditors can together cover the relevant demographic groups by auditing the LLM collaboratively with their individual query sets. However, relying on multiple auditors raises a fundamental trust problem, as they may act on behalf of the LLM provider to portray a misleading appearance of fairness, i.e., fairwashing. We propose Auditopus, a novel approach for robust decentralized fairness auditing. In Auditopus, auditing proceeds in rounds without a central server. In each round, every auditor issues a fixed number of queries to the LLM, and sends only cumulative statistics vectors of its query results to other auditors instead of sensitive queries in clear. The fairness of the audited LLM is then estimated by aggregating all the vectors. We show theoretically and empirically that even a single adversarial auditor in the network can steer this estimate by fabricating the vectors it sends, making an unfair LLM appear fair. To address this threat, Auditopus has each honest auditor locally down-weight any auditor whose cumulative statistics vectors are statistically inconsistent with previous ones. We implement Auditopus and compare it to robust aggregation baselines on two datasets with two pre-trained LLMs. Against an attacker that optimizes the vectors it sends to make the LLM appear fair, Auditopus reduces audit error by up to 78% on average relative to no defense and at least 62% relative to the robust aggregation baselines. Even when 49% of the auditors are adversarial, Auditopus never lets a very unfair or moderately unfair LLM pass as fair.

---


### 209. [GAGR-Lab: Evaluating Joint Spatial-Geometric and Analytic Function Reasoning](https://arxiv.org/abs/2610.10201)

**<font color=#1a73e8>作者：</font>** Jingyao Zhang, Yun Li, Lu Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Joint spatial-geometric and analytic function reasoning requires translating a perceived spatial configuration into a symbolic function whose executed curve satisfies geometric constraints. We present GAGR-Lab, a framework for measuring this capability through Cartesian game scenes, explicit function semantics, and authoritative Rust trajectory execution. It distinguishes spatial perception, metric grounding, geometric relations, function interpretation, function construction, and constrained synthesis. We specify four configurable scene-difficulty presets and a prospective 24-cell diagnostic design, while reporting only the subset actually evaluated. A bounded pilot of one hosted model (Llama 3.2 11B Vision Instruct) using two API credentials as execution replicas yields 72 balanced games with 432 attempts, 429 valid provider responses, and no target hits; exploratory ordinary-function prompt variants also fail to hit, while the structured localization interface yields no scoreable outputs. A privileged analytic search control independently succeeds on 600 directional cases from 300 generated scenes, with exact repeatability and 1,200 successful vertical-reflection or translation checks. The framework separates serving reliability, symbolic compliance, and geometric success, and preserves exact model-visible inputs and realized paths. A staged protocol outlines diagnostic calibration, held-out replication, multi-model comparison, and paired robustness tests. The contribution is an operational research framework with an executed pilot and a clearly identified prospective study plan; the full difficulty matrix and comparative model results remain untested.

---


### 210. [From Prompts to Trees: Effective LLM-Guided Tree Generation for Few-Shot Tabular Classification](https://arxiv.org/abs/2610.10227)

**<font color=#1a73e8>作者：</font>** Yue Qiu, Zekang Du, Yiqun Diao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) possess rich world knowledge and impressive generalization capabilities, their direct application to tabular data classification is hindered by high inference costs and limited interpretability. In contrast, decision trees are fast and transparent but often underperform in low-data regimes. In this work, we propose a novel framework that bridges these paradigms by distilling LLM knowledge into interpretable decision trees under a few-shot learning setting. Instead of directly prompting the LLM to generate full trees, which is often unstable and inefficient, we develop a three-stage paradigm that prompts the LLM to generate rules and organize the rules into a tree. Experiments on multiple real-world tabular datasets demonstrate that our method achieves superior accuracy and interpretability with significantly lower prompting overhead compared to existing baselines.

---


### 211. [LLM Persuasion Is in the Eye of the Evaluation](https://arxiv.org/abs/2610.10232)

**<font color=#1a73e8>作者：</font>** Kamile Dementaviciute, Julija Vaitonyte, Tijl De Bie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have already been shown to match or exceed human experts in persuasion. While their persuasive capabilities hold promise for beneficial uses such as education and health communication, they can also be used to manipulate and misinform, making their evaluation a growing priority for developers and regulators. That evaluation, however, remains fragmented: studies differ in what they treat as persuasion, and broad claims often rest on narrow, situation-specific assessments. Automated methods, often modelled on human studies, offer a way to compare such assessments directly, as they can be run on the same models at scale and can include high-risk forms of persuasion that would be difficult or unethical to test on people. In this study, we adapt nine published automated methods to a shared setup, run them on the same fifteen LLMs, and ask whether their rankings agree and why. We find that the methods agree only weakly (mean Spearman $\rho = 0.25$). Our analyses point to two contributing factors. Models that refuse some tasks but not others, directly or indirectly, lower agreement by about a quarter, and these refusals fall mostly on manipulation tasks. General capability also plays a part: most rational persuasion (non-manipulative) methods track it, whereas most manipulation methods do not. Together, these findings suggest that agreement depends more on the task a method sets than on how it scores persuasion, although this pattern is only indicative given the eight methods available for analysis. More broadly, our results suggest that persuasion scores combine a model's ability to persuade with its willingness to do so. A single score is therefore informative about its own setting, but says little about a model's persuasiveness across tasks.

---


### 212. [Geometry-Supervised Visual Representation Learning for Multi-Phenotype Lesion Interpretation in Medical VLMs](https://arxiv.org/abs/2610.10238)

**<font color=#1a73e8>作者：</font>** Hao Wang, Qiwei Zeng, Shuchang Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) have shown increasing potential for clinical image interpretation. However, these models still struggle to interpret multi-phenotype lesions whose diagnosis requires the joint assessment of multiple pathological phenotypes. Existing vision-language alignment methods produce visual representations that fail to preserve anatomical hierarchies and relationships among phenotypic subclasses. This stems from their reliance on semantic supervision, which lacks geometric constraints to preserve these relationships in the visual embedding space. Moreover, the sparsity of lesion-related anatomical and phenotypic representations makes it difficult for medical VLMs to capture important diagnostic evidence. To address these limitations, we propose \textbf{PureVision}, a geometry-supervised visual representation learning framework for multi-phenotype lesion interpretation in medical VLMs. It combines a geometry-supervised representation learning module, \textbf{PureEyes}, and an anatomy-guided evidence aggregation module, \textbf{PureNeurons}. PureEyes provides geometric supervision through ideal spatial distributions that encode anatomical hierarchies and phenotypic subclass relationships. PureNeurons projects visual representations into the learned latent space, using their positions to selectively aggregate lesion-specific anatomical and phenotypic evidence. Experiments on \textit{LIDC-IDRI}, \textit{CBIS-DDSM}, and \textit{3DReasonKnee} demonstrate that PureVision improves lesion grounding and phenotype characterization in visual question answering and radiology report generation. Code is available at: this https URL.

---


### 213. [DuoSketch: How Pairs Navigate Challenges in AI-Supported Collaborative Design Ideation](https://arxiv.org/abs/2610.10249)

**<font color=#1a73e8>作者：</font>** Weiyan Shi, Darryl Lim, Geraldine Quek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI offers new resources for collaborative design ideation, yet how designers work with it as a shared concept develops remains underexplored. We developed DuoSketch, integrating a shared canvas and live transcripts with a separate AI for each member of a pair. An exploratory qualitative study with 12 pairs identified three challenges: unresolved fit between AI proposals and shared design purposes, shared meanings not expressed in AI responses, and agreed changes missing from later outputs. We found that pairs navigated these challenges through bridging work in two directions: AI -> Shared Design (reworking features, developing uses, and assessing fit with shared requirements) and Shared Design -> AI (supplying materials, explaining meanings, and communicating decisions). We discuss how future AI systems can support the joint exploration and articulation of design ideas.

---


### 214. [Stale, Misattributed, or Late: Where Personal Memory Fails Before Generation](https://arxiv.org/abs/2610.10265)

**<font color=#1a73e8>作者：</font>** Haonan Deng, Park Sinchaisri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal memory for language agents is usually judged by whether the final an- swer is correct. That score hides errors that arise before generation: the memory block may contain an obsolete value, a fact about the wrong person, or no use- ful fact before the serving deadline. We measure these failures directly. Using Personal Fact Memory (PFM) as a reference layer, we find that temporal validity is primarily a property of memory construction in our setting. On a controlled revision benchmark, serving only the active value of each correctly keyed slot eliminates observed stale exposure; without update resolution, 70.3% of prompts expose a superseded value. Once retrievers share the same active store and par- ticipant information, participant-aware BM25 is equivalent to the reference ranker within a prespecified 0.02 margin. The harder problem is assigning revisions to the right slot. Missed merges leave stale values active, whereas false merges silently remove current values; four LLM key assigners achieve higher key re- call than a rule extractor yet produce lower clean-retrieval rates, and open-domain merge recall on LongMemEval never exceeds 0.062. Misattribution survives va- lidity filtering: an entity posterior reduces same-name exposure on controlled data but cannot distinguish identically named speakers in LoCoMo. Two frozen lan- guage models reproduce prompt errors in generated text. Retrieval latency varies across rankers, but prompt prefill dominates turn-level latency on our hardware. These results argue for evaluating agent memory before generation, separating stored-state validity, identity resolution, abstention, and serving latency.

---


### 215. [$Δ$Representation: Geometry Supervised Representation Learning of Phenotypes via Counterfactual Reasoning for Medical VLMs](https://arxiv.org/abs/2610.10286)

**<font color=#1a73e8>作者：</font>** Hao Wang, Qiwei Zeng, Jinghao Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) have shown increasing potential for radiological image interpretation. Medical VLMs encode radiological images into visual representations that capture both anatomical and phenotypic information for diagnosis. Existing approaches improve pathological phenotype representations through semantic-guided representation alignment. However, pathological phenotypes arise as lesion-specific visual changes superimposed on underlying normal anatomy. Such semantic alignment approaches fail to model the phenotype-specific increment relative to the corresponding normal anatomical representation. To address this gap, we propose \textbf{$\Delta$Representation}, a visual phenotype representation learning framework based on counterfactual reasoning for medical VLMs. It comprises \textbf{BaseAnatomy}, a geometry-supervised representation learning module, and \textbf{$\Delta$Phenotype}, a counterfactual incremental representation learning module. BaseAnatomy provides fine-grained geometric supervision through spatial relationships across and within anatomical structures. $\Delta$Phenotype computes the representation increment between lesion representations and their corresponding normal anatomical representations, and supervises increments associated with the same phenotype to cluster in the representation space. Experiments on \textit{ReXGroundingCT} and \textit{LIDC-IDRI} demonstrate that $\Delta$Representation effectively structures pathological phenotype representations and improves lesion grounding and phenotype characterization accuracy in medical VLMs. Code is available at this https URL.

---


### 216. [SemanticFold: Latent Sequence Compression SeparatesLanguage Modeling, Decodability, and Reasoning](https://arxiv.org/abs/2610.10304)

**<font color=#1a73e8>作者：</font>** Mingyan Liu, Min Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether latent sequence compression of prompt prefixes preserves the capabilities that large language models rely on during inference. We introduce SemanticFold, a compression scheme that folds prefix hidden states at learned boundaries, and evaluate it across five model scales: Qwen3-1.7B, Qwen3-8B, SmolLM2-1.7B, Pythia-1.4B, and Pythia-6.9B. We use a fixed-target protocol: a frozen prefix is executed natively or compressed, and both arms teacher-force identical continuation tokens. This design rules out target-selection explanations for likelihood changes. We examine five endpoint families: fixed-target negative log-likelihood, finite-label reasoning accuracy, linear probe accessibility, open-ended generation, and systems-level memory and latency. We find that compression moves these endpoints non-monotonically and that they do not share a single compression threshold. On Qwen3-1.7B at compression ratio R=1.7, compressed-minus-native mean NLL decreases by 0.135 under paired bootstrap with 10000 draws. On SmolLM2 at R=1.2, the mean change is 0.013 higher than native. On both Pythia checkpoints, NLL is effectively unchanged. An NLL decomposition separating sequence shortening from the learned residual transform shows that the favorable Qwen likelihood is attributable primarily to residual adaptation rather than to shortening alone. MLP-only, which applies the transform without shortening, achieves 0.082 lower NLL than Full SemanticFold. Linear probe accuracy and macro AUC change by less than 0.03 in absolute value across conditions, with confidence intervals crossing zero. We conclude that preservation under latent compression has no single scalar certificate: language-model fit, decodability, and reasoning behavior answer different questions and can move in different directions under the same compression operation.

---


### 217. [Fault-tolerant foundation models](https://arxiv.org/abs/2610.10311)

**<font color=#1a73e8>作者：</font>** Trevor McCourt, Ila R. Fiete, Isaac L. Chuang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emerging computer hardware often trades reliability for energy efficiency; here we show that large-language models (LLMs) can be trained to tolerate this unreliability, and that rather than degrading, their error resilience actually increases as they grow. Modified neural scaling laws inferred from 40,000 GPU-hours of training runs on simulated faulty digital hardware quantify this trend and suggest that models learn to compute within "good" error-correcting codes, whose relative overhead remains finite no matter how large the model gets. This finding leads us to conjecture that appropriately trained LLMs may be formally fault-tolerant; if true, running AI inference on low energy, faulty hardware may be a path to substantial energy savings over the status quo.

---


### 218. [Nobody Truly Agrees on Sentiment: Humans, Bespoke Tools, and LLMs Struggle with Social Media Texts](https://arxiv.org/abs/2610.10318)

**<font color=#1a73e8>作者：</font>** Himarsha R. Jayanetti, Sivakanesan Dhanushkanda, Shuai Hao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social media is a rich source of real-time public sentiment, but widely used sentiment analysis tools are often applied without understanding their limitations. In this study, we evaluate the inter-rater reliability of three bespoke sentiment analysis tools (TextBlob, VADER, and Twitter-roBERTa-base) and three large language models (LLMs: Qwen3-32B, GPT-OSS-120B, Llama-4-Maverick-17B) against six human raters across 100 tweets. We measured agreement using two statistical measures: Cohen's kappa for pairwise comparisons and Fleiss' kappa for multiple raters. Even among the human raters, our results showed only fair agreement, highlighting the subjectivity of sentiment analysis. Higher agreement was observed under the binary sentiment classification (negative vs. non-negative and positive vs. non-positive) than under the three-class classification across both humans and automated tools. The Twitter-roBERTa-base model showed the strongest alignment with human ratings, outperforming both bespoke sentiment tools and LLMs, particularly in distinguishing negative versus non-negative sentiment. LLMs showed substantial agreement among themselves and moderate to substantial alignment with humans, performing better in positive vs. non-positive classifications. Our findings underscore that domain-specific fine-tuning remains crucial for reliable social media sentiment analysis, and human-centered evaluation remains essential for establishing gold-standard labels.

---


### 219. [When to Unpair: Regulating Pairing Dependence in Medical Visual In-Context Learning](https://arxiv.org/abs/2610.10335)

**<font color=#1a73e8>作者：</font>** Cheng Wan, Chenjun Li, Qingyu Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual in-context learning (ICL), well suited to label-scarce medical imaging, uses support image-label pairs to demonstrate input-output mappings, while the labels collectively indicate the requested task. We diagnose dependence on individual pairings with a test-time derangement that reassigns every support label to another support image while preserving the query, support images, and label multiset. The resulting pairing gap, defined as shuffled-minus-matched performance, shows that all four released models depend on the pairing, to widely varying degrees. Further analysis of a paired-trained model reveals support-associated spurious regions and lesion-size biases even with real, unaltered supports, alongside sensitivity to mis-registered support labels. To regulate this dependence, we introduce a late unpairing curriculum (LUC), which starts with matched training and then applies random unpairing, replacing each support label with that of another support in the same episode. LUC nearly closes the pairing gap on two backbones while maintaining or improving matched-support performance across all evaluated task types, with gains extending to held-out tasks and cross-dataset episodes. It also mitigates these failure modes. On BraTS whole-tumor segmentation, matched-support DSC rises from 0.733 to 0.857 while the gap shrinks from -0.184 to -0.008. In a released model, brief fine-tuning with random unpairing reduces the gap. A reversed curriculum that places the same number of unpairing epochs at the start of training leaves a large gap. This shows that pairing dependence is shaped by the order of training and not only by the amount of unpaired training.

---


### 220. [AutoAdapt: Automatic Domain Discovery Enables Low-Cost Extensibility](https://arxiv.org/abs/2610.10349)

**<font color=#1a73e8>作者：</font>** Josh McGiff, Salma Mekaoui, Robert Shanahan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned models are deployed into environments where domains are heterogeneous and evolve, yet adding new domains or data typically requires costly retraining. We present AutoAdapt, a modular framework that incorporates new domains and data via targeted single-adapter training without modifying other adapters. The framework automatically discovers latent domains, uses them to train per-domain Low-Rank Adaptation (LoRA) adapters independently in parallel and performs parameter-free routing. Across 14 domain-specific benchmarks and GPT-4o pairwise judgements, AutoAdapt achieves parity with a LoRA adapter trained on all domains without requiring full-model retraining. We also find evidence of specialisation effect convergence across independent discovery methods. Overall, training each adapter on its own domain prevents domain interference by construction, thus enabling modular, taxonomy-free domain specialisation without aggregate performance loss or full model retraining.

---


### 221. [Input-Blind Controls Produce Substantial Oracle Headroom for Layer Programs in Multiple-Choice Evaluation](https://arxiv.org/abs/2610.10368)

**<font color=#1a73e8>作者：</font>** Yibei Guo, Rui Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive computation aims to improve language-model inference by tailoring execution to each input. For layer programs, oracle evaluations use known answers to estimate the potential gain from this flexibility, before a practical selector is available. However, a gain from selection does not by itself explain why the chosen programs help. This study examines this distinction using 32 layer-skipping and repetition programs on two models and 4,413 multiple-choice items. The analysis compares their gains over a fixed action selected without the evaluation prompt with those of input-blind perturbations at the same sites, re-evaluating selections on another prompt. With shared option order, the controls give 10.2-11.8 and 15.6-19.4 percentage points of headroom on Qwen3-4B-Base and Llama-3.1-8B, exceeding the real programs' 9.0 and 10.1 in all three random-direction draws per model. They match answer-change rate only, and the ordering depends on the menu: in post hoc comparisons, real programs lead on Llama's repeat-only menu in every draw. A smaller KL-calibrated comparison, including an input-dependent control, favours real programs in point estimate, with inconclusive corrected tests. Fixed letter offsets produce headroom of similar scale. Rotating options sharply reduces both families' headroom, while leaving positive real-minus-control differences of 1.4-2.3 and 3.7-4.5 points; their magnitudes and statistical support depend on further adjustments and the reference. A supplementary generated-answer test finds that search-selected programs keep a 26.0-point advantage over programs selected for other problems after rewording, without a placebo comparison. These results show that substantial headroom can persist across prompts with shared option order without establishing a benefit specific to the selected layer computation; neither ordering against these controls identifies that benefit.

---


### 222. [Document-Level Text Simplification in Estonian Using Large Language Models](https://arxiv.org/abs/2610.10378)

**<font color=#1a73e8>作者：</font>** Meeri-Ly Muru, Eduard Barbu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document-level text simplification involves transformations that go beyond sentence-internal edits, addressing discourse coherence, anaphora resolution, and cross-paragraph consistency. Despite advances in sentence-level simplification for high-resource languages, document-level simplification in morphologically rich, low-resource languages such as Estonian remains largely unexplored. This study presents a comprehensive evaluation of five state-of-the-art multilingual large language models (LLMs) for document-level simplification in Estonian. Three prompting strategies are examined: single-pass generation, pipeline-based modular agents, and guideline-augmented pipelines. The evaluation framework integrates automatic metrics assessing readability, semantic preservation, and discourse coherence, alongside a structured manual annotation protocol. The findings indicate that Gemini-2.0 and LLaMA-3.3 produce outputs with near-native fluency and strong meaning preservation, whereas other models display notable grammatical and semantic limitations. This work contributes novel document-level coherence metrics, evidence-based prompting strategies, and publicly available resources for reproducibility.

---


### 223. [ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals](https://arxiv.org/abs/2610.10381)

**<font color=#1a73e8>作者：</font>** Heejun Kim, Junyoung Lee, SangLyul Cho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers improve parameter efficiency by repeatedly applying shared Transformer blocks over multiple recurrent loops, increasing computational depth without increasing the parameter count. However, KV cache memory still scales with the number of loops, becoming a key memory bottleneck that limits batch size and inference throughput. KV cache quantization can alleviate this bottleneck, but existing methods often suffer substantial accuracy degradation at aggressive low-precision regimes. We observe that looped Transformers offer a unique opportunity: KV states across loops are highly similar. Based on this observation, we propose ResidualQuant, which uses the final-loop KV states as a reference and represents the remaining loops with low-precision residuals. Our method further combines least-square scaling and rotations applied to the residuals, as well as loop-wise mixed precision, to enable accurate quantization down to INT2 while retaining efficient reconstruction. Across multiple looped Transformer models and mathematical reasoning and code generation benchmarks, ResidualQuant consistently improves the accuracy-memory tradeoff over state-of-the-art rotation-based KV quantization. In particular, our method retains accuracy close to BF16 under mixed-precision settings while reducing theoretical KV storage by 80.7%, achieving up to 13.0% higher accuracy than the rotation-based baseline at the same memory budget. On an RTX 5090, the reduced KV memory traffic improves fixed-batch decode throughput by up to 2.73x, while the smaller memory footprint enables up to 2x larger batches, improving peak throughput by up to 4.15x.

---


### 224. [OrBIT: Structure-Guided Embedding Compression](https://arxiv.org/abs/2610.10385)

**<font color=#1a73e8>作者：</font>** Yunied Puig, Amit Kumar Jaiswal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Embedding tables are among the largest components of modern language models. Most compression methods fix a coding geometry such as coordinate blocks, low-rank subspaces, or unrestricted codebooks, and optimize within it. We instead ask whether the coding geometry can itself be discovered. We introduce \emph{OrBIT}, a structure-guided embedding compression framework that learns reusable local geometry from orbit dynamics and uses it to constrain a small set of shared codewords. The global reconstruction residual then decides where the fixed coding budget is spent, while redundant overlapping charts let local errors compensate one another after gluing. Our theory shows how tight-chart geometry controls distortion, how the global residual directs sequential allocation, and how data-geometry-guided refinement improves the codec. The resulting orbit machinery is compiled away, leaving a compact decoder in which the learned structure governs what is stored, where capacity is allocated, and how local information is assembled globally. Across four LLM embedding tables, OrBIT achieves $37.9\times$ compression on GPT-2 and over $23\times$ on each 7B table relative to 16-bit storage, while delivering competitive rate-distortion performance against established quantization and low-rank baselines.

---


### 225. [Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving](https://arxiv.org/abs/2610.10390)

**<font color=#1a73e8>作者：</font>** Xingtai Gui, Yucheng Zhou, Dongqian Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action~(VLA) models have emerged as a promising paradigm for autonomous driving. However, existing VLA models still suffer from a fundamental mismatch: driving actions require precise 3D geometric cues, while visual-language understanding and reasoning are largely conducted in a 2D semantic space. In this paper, we propose GeoCoTDrive, an explicit geometric chain-of-thought framework that grounds geometry in a planning-oriented manner. GeoCoTDrive follows a think with 2D first, drive with dedicated 3D priors paradigm. It first grounds 2D regions corresponding to decision-critical cues, and then retrieves localized 3D priors by sampling features from a geometric foundation model within the grounded regions. These localized geometric features are interleaved into the autoregressive context to support the trajectory generation. To supervise this process, we introduce planning-relevant grounding, a new region-level grounding task that focuses on local spatial cues directly affecting ego planning decisions, and construct the PlanningGrounding dataset to endow VLAs with planning-oriented grounding capability. Experiments across multiple end-to-end autonomous driving benchmarks show that GeoCoTDrive consistently improves safety-critical planning performance, demonstrating the effectiveness of the explicit geometric chain-of-thought process for VLA-based planning.

---


### 226. [Kernel Autoresearch for Open-Ended Model Discovery](https://arxiv.org/abs/2610.10394)

**<font color=#1a73e8>作者：</font>** Richard Cornelius Suwandi, Feng Yin, Kevin Murphy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernels encode the inductive bias of a wide range of machine learning models, yet automated kernel design faces a fundamental dilemma. A fixed grammar of base kernels and operators guarantees validity but limits the search to structures expressible by those building blocks. Conversely, unrestricted programs remove this limitation but no longer guarantee validity. In our stress tests, 22-58% of LLM-generated kernels that pass numerical checks on random inputs fail when evaluated at different scales or dimensions. We propose Kernel Autoresearch (Kernaut), which treats kernel design as open-ended model discovery. Coding agents write kernels as programs, while construction contracts ensure that every accepted kernel is valid. A quality-diversity archive retains high-performing kernels with distinct behaviors, and novelty screening steers agents toward functionally new candidates. Our experiments demonstrate that the discovered kernels encode reusable inductive biases that generalize to unseen tasks. On held-out black-box optimization families, a discovered kernel outperforms a meta-learned deep kernel trained on the same episodes. Furthermore, kernels discovered from ten enzyme-kinetic rate laws achieve lower error than tuned ARD and deep kernel baselines on five unseen mechanisms. The discovered kernels are also interpretable programs that human researchers can refine: a human-refined version of one further reduces the held-out predictive error by 5.7% and optimization regret by 7.8%.

---


### 227. [Self-correction Optimization for Interleaved Multimodal Generation](https://arxiv.org/abs/2610.10400)

**<font color=#1a73e8>作者：</font>** Xin You, Zhiwei Ning, Zukai Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have made significant progress in visual understanding and generation. However, generating interleaved image--text content remains challenging, as it requires tightly integrated multimodal understanding and generation capabilities. Although existing MLLMs provide promising solutions, most rely on additional training with augmented data, which is computationally expensive and remains limited in preserving visual subjects, temporal consistency, and physical plausibility. In this work, we propose self-correction optimization (SCO), an effective training-free method for consistent interleaved generation. SCO treats the classifier-free guidance update as a reference and performs minimal self-correction under two complementary constraints, including new-event and state-preserving constraints. Specifically, the new-event constraint promotes temporal consistency across image--text sequences, while the state-preserving constraint maintains the coherence of visual subjects throughout subsequent generation steps. Experiments on challenging interleaved multimodal generation benchmarks demonstrate significant improvements in temporal coherence and visual-subject preservation. Furthermore, SCO can be extended to video generation and improves the modeling of physically grounded processes, including robot manipulation and long-horizon handcrafting.

---


### 228. [Reasoning-Token Spikes Under Prompted Untruthful Responding in Large Language Models](https://arxiv.org/abs/2610.10405)

**<font color=#1a73e8>作者：</font>** Maverick Morales, Tomáš Dominik, Vermut Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Monitoring the chain-of-thought of reasoning artificial intelligence (AI) models remains a key approach to detecting deception and other forms of misbehavior in such models. However, semantic chain-of-thought monitoring depends on reasoning traces being legible and sufficiently faithful to the underlying computations that produced the model's behavior, not to mention accessible. Moreover, there is increasing evidence that chain-of-thought outputs may soon become illegible or unfaithful, if they even remain accessible. Based on cognitive load theory, we investigate a lower-bandwidth signal -- the number of reasoning tokens generated -- which does not require access to the content of the reasoning trace. Three reasoning-capable large language models answered 210 multiple-choice questions -- across analytic, descriptive, and normative reasoning types as well as moral and non-moral domains -- under system prompts instructing them to respond truthfully, falsely, or without regard for truth. Across all three models, truth-directed responding elicited fewer reasoning tokens than both lie-directed and truth-indifferent responding. These findings show that explicitly prompted untruthful response policies can produce robust group-level differences in test-time reasoning-token use. While not yet establishing reasoning-token count as a detector of spontaneous deception or general misalignment, our results are a proof of concept that it can serve as a simple, content-independent candidate signal for differentiating untruthful from truthful model behavior when raw reasoning traces are unavailable or unreliable. Future work should test instance-level detection rates, out-of-distribution generalization, learned deceptive policies, hidden objectives, and robustness under adversarial pressure.

---


### 229. [SOTA: Stock Options Trading Agents Guided by Option-Implied Return Distributions](https://arxiv.org/abs/2610.10407)

**<font color=#1a73e8>作者：</font>** Yizhen Xie, Mengyang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As option markets grow and AI advances, agentic systems for option trading are gaining increasing attention. Language-model-based agents can reason over contextual information such as news, but option trading presents a particularly challenging decision problem: a single stock can have thousands of contracts, and the agent must decide both which contracts to trade and how to combine them. Existing approaches often sidestep this complexity by restricting the policy to a fixed strategy structure, such as a straddle, limiting their ability to switch strategies as market conditions change. We present SOTA (Stock Options Trading Agents), an agentic trading framework for structured option-strategy selection. SOTA abstracts the large option universe into strategy-level decisions while deterministic resolvers handle portfolio implementation. We develop SOTA by post-training Qwen3.8-27B with supervised fine-tuning followed by reinforcement learning. SOTA is evaluated on options on nine large-cap U.S. equities and SPY against rule-based and machine-learning strategy selectors in the same trading environment. Over a six-month out-of-sample period, SOTA earns an 18.3% total return with a Sharpe ratio of 1.60 and a maximum drawdown of 8.96%. We also document an asymmetric role of news: news improves frontier-teacher trajectories, but retaining news during reinforcement learning reduces out-of-sample return from 18.3% to -2.7%.

---


### 230. [Training Parallel Speculative Draft Models by Directly Minimizing Expected Decoding Rounds](https://arxiv.org/abs/2610.10411)

**<font color=#1a73e8>作者：</font>** Yunxiao Zhao, Changxiao Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference by using a low-cost draft model to propose tokens that the full-size target model verifies in parallel. Parallel and semi-autoregressive (semi- AR) drafters improve drafting efficiency by proposing an entire block in a single forward pass, but training them raises a new difficulty: the draft distribution for a given position depends on where the decoding round starts, and where rounds start depends on how many tokens earlier rounds accepted. Existing training objectives typically rely on block-local surrogates that ignore this cross-round coupling, and therefore do not directly optimize the global decoding efficiency. In this work, we develop a theoretical framework for training and evaluating these drafters by representing speculative decoding as a Markov reward process. This formulation yields the Expected Decoding Rounds (EDR) objective, which weights local rejection costs by state occupancies and exactly equals the expected number of decoding rounds. Unlike prior surrogate objectives, EDR introduces no auxiliary hyperparameters. We then derive an exact temporal-difference gradient that supports unbiased stochastic optimization from target-model rollouts. The same framework also yields an exact offline evaluator for round counts, enabling paired drafter comparisons on shared target rollouts without running speculative decoding. Finetuning two state-of-the- art drafters, DSpark and DFly, with EDR consistently improves mean accepted length and outperforms existing training objectives across nine benchmarks spanning math reasoning, code generation, and chat.

---


### 231. [Which Rollout Taught It That? BehaviorTrace and the Limits of Training-Data Attribution in Online RL](https://arxiv.org/abs/2610.10422)

**<font color=#1a73e8>作者：</font>** Amit Nautiyal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When reinforcement learning teaches a language model a new behavior, can we find the training rollouts that taught it? And when an attribution method says it can, how do we know the answer is real? We study both questions on online RL fine-tuning with GRPO, using a planted behavior with a known cause. We release BehaviorTrace, an open evaluation harness that combines full-gradient sketching, the planted-behavior setup, and controls for gradient magnitude, fluency, headroom, and variation across seeds and generation draws. Across three seeds on Qwen2.5-1.5B, much of the apparent attribution signal comes from confounds. A control that ranks training steps by gradient size alone, with no behavior target, reaches 4.2 to 4.5 times chance and matches or beats the best targeted estimator on two of three seeds. At saturated checkpoints, model fluency predicts the behavior label at least as well as every gradient method we compared it with. Once fluency is controlled, the per-rollout results change from seed to seed and from one generation draw to the next, so a single run cannot settle the question. One signal does hold on all three seeds. The gradient of the trigger tokens aligns with a target built where the behavior actually occurs. We turn these findings into a checklist for evaluating attribution in RL. We test existing estimators, including GAS (renormalized TracInCP) and a TRAK-style estimator, and do not propose a new one.

---


### 232. [CoTrace: Data Recipes for Training Terminal Agents with Harness-Model Co-Evolution](https://arxiv.org/abs/2610.10426)

**<font color=#1a73e8>作者：</font>** Jixuan Chen, Jiaxin Zhang, Qinyuan Ye 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Terminal-agent capability depends jointly on model weights and the runtime harness that formats prompts, binds tools, and handles error recovery. Existing harness-model co-evolution approaches improve both components, yet often treat trajectories produced during harness search as an undifferentiated replay buffer. This practice overlooks that a trajectory's value for model training depends on the harness under which it was generated. To systematically analyze this interface, we establish an alternating co-evolution framework that decouples harness search and policy training through component-wise promotion decisions. Within this framework, we introduce CoTrace, a harness-aware data recipe that explicitly governs trajectory routing, provenance matching, and curriculum refresh. Under CoTrace, recurring execution failures guide harness synthesis, while policy training is strictly conditioned on verified rollouts matched to the adopted runtime for supervised fine-tuning (SFT) or fresh online interactions for reinforcement learning (RL). On the Tmax promotion split, CoTrace advances Qwen3.5-9B from 78 to 88 solved tasks under supervised fine-tuning while an online reinforcement variant reaches 90. Specifically, a compact harness-matched corpus produces steady model gains at substantially lower compute than much larger corpora pooled across sibling harnesses. Furthermore, evaluations on Terminal-Bench 2.1 and SWE-bench Lite show that out-of-distribution transfer depends fundamentally on harness compatibility, where maintaining consistency between training and evaluation runtimes prevents procedural execution breakdowns observed under foreign scaffolds.

---


### 233. [Detecting Adversarial Images through Response Profiles of Vision-Language Models](https://arxiv.org/abs/2610.10436)

**<font color=#1a73e8>作者：</font>** Arash Vashagh, Roozbeh Razavi-Far  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial perturbations can alter the predictions of frozen vision-language models (VLMs) while leaving their confidence and image--text similarity patterns seemingly plausible. We investigate whether we can identify adversarial inputs based on the broader way an image interacts with a collection of general semantic prompts. Our detector summarizes these responses using category-level statistics, relationships among prompts, deviations from clean reference distributions, and stability under weak image transformations, producing a compact response profile that is classified by a lightweight model while the VLM remains fixed. We evaluate the approach on multiple public image datasets, several CLIP-style visual backbones, and a range of gradient-based, optimization-based, automated, and spatial attacks. The detector achieves strong discrimination in attack-specific settings and retains substantial performance when evaluated on attacks not seen during training. Under a controlled detector-specific protocol, the response-profile representation outperforms the evaluated embedding-geometry baselines. Additional analyses show that the feature groups provide complementary information and that the method remains effective under variations in the prompt configuration. We also examine inference cost and performance against detector-aware adaptive attacks. Overall, the results indicate that response patterns across semantic prompts provide a useful complementary signal for adversarial image detection in frozen VLMs.

---


### 234. [RunningTab: Direct Workspace Interaction with Environment-Side Tabs](https://arxiv.org/abs/2610.10444)

**<font color=#1a73e8>作者：</font>** Jinheon Baek, Soyeong Jeong, Yumin Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Much knowledge work produces new deliverables from files a workspace already holds, and LLM agents are beginning to take such work over. Through direct corpus interaction, an agent can search and read any of those files from a terminal with no indexing, and producing a deliverable from many of them in this way is what we call direct workspace interaction (DWI). Reaching the files, however, is only half the task: nothing keeps track of what the task asks for, what has been read, and what was listed but never opened, all of which slip through the context window without leaving a trace, so an agent may extract a figure and still deliver a report without it. To address this, we present RunningTab, a framework that equips direct workspace interaction with an environment-side tab: a per-task record of what the task still owes, kept by the environment alongside the agent. Specifically, the agent adds its requirements, while the environment records every file read as an excerpt with its provenance and every listed but unopened file as a candidate; the agent can then see each requirement beside its best-matching excerpts and top unopened candidates, resolve it against matching content or set it aside with a reason, and, should it try to finish with requirements still open, receive them in a finish check. We validate RunningTab on three benchmarks with three LLMs, where it consistently outperforms plain DWI and baselines that keep the record in the model, while its tab usually holds the values a deliverable needs once seen.

---


### 235. [PHRBench: A Behavioral Evaluation of Post-Hallucination Reasoning in LLMs](https://arxiv.org/abs/2610.10455)

**<font color=#1a73e8>作者：</font>** Linghao Meng, Feng He, Xuan Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucinated information can propagate through multi-stage LLM systems and become part of the context for subsequent reasoning. Existing studies of post-hallucination reasoning (PHR) mainly characterize changes in final outcomes and aggregate reasoning dynamics, leaving how models resolve hallucinated premises at the response level insufficiently understood. In this work, we introduce PHRBench, a controlled benchmark for behaviorally structured PHR across four domains and 18 large language models. PHRBench characterizes each reasoning trajectory independently of final-answer correctness through Hallucination Compliance, Hallucination Avoidance, and Heuristic Correction, and defines an insightful trajectory as successful correction that ultimately reaches the correct answer. Across 4820 controlled instances, we find that successful recovery remains relatively rare and is associated with more frequent belief updates along the reasoning trajectory. We further find that properties of the hallucinated prompt contain substantial predictive signal for successful recovery, with a lightweight predictor achieving an AUROC of 0.847. These findings provide a behavioral view of post-hallucination reasoning, characterizing how LLMs resolve erroneous context and when successful recovery is likely to occur.

---


### 236. [Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts](https://arxiv.org/abs/2610.10460)

**<font color=#1a73e8>作者：</font>** Hejian Sang, Zhengze Zhou, Shayan Mohajer Hamidi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) is used in two settings. In common-domain composition, several teachers score each student rollout from one prompt domain and their signals form a single target; in routed-domain distillation, prompts from different domains are assigned to the corresponding specialist. Both settings usually transfer each teacher's endpoint policy, which mixes what post-training changed with preferences inherited from the teacher's base. We introduce $\Delta$-MOPD, which transfers each teacher's teacher-minus-base logit shift re-anchored at the student's frozen initialization, and compare it with endpoint supervision in both settings while holding teacher selection fixed. We first expose the mechanism that impedes endpoint transfer: inherited base pull can exceed the post-training shift. Removing it reduces the teacher-term norm ratio and target--student KL.
Across our experiments, the results suggest that shift targets are particularly useful when teacher signals are combined at a state. With three composed teachers, $\Delta$-MOPD exceeds endpoint composition by $4.11$ Math and $1.95$ five-benchmark points; with two, it matches endpoint accuracy. Under phased routing, it achieves higher mean performance in both phase orders and reduces the observed order gap from $10.50$ to $6.42$ points. Under interleaved routing, where each update involves one teacher, the two targets perform comparably. The phased results provide supporting evidence that the benefit may extend to signals accumulated across training phases. Target construction is thus an independent design axis in MOPD, complementary to teacher selection.

---


### 237. [A Society of Researchers: Designing Institutions for Populations of Autonomous Research Agents](https://arxiv.org/abs/2610.10468)

**<font color=#1a73e8>作者：</font>** Ali Asaria, Deep Gandhi, Tony Salomone  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Deployments of research agents are moving to populations of thousands that share one pool of compute, while most current systems organize one project at a time or leave the population unorganized. We argue that such a population will acquire an organization whether or not its designers provide one, so designers should provide it explicitly, and that the multi-agent systems community holds the tools to do so. We propose a society of agents, a population of persistent agents under explicit institutions, and develop it for science as a society of researchers built on six principles. Principal investigators compete for compute through requests for proposals, independent review, and grants; a human governor, the mayor, allocates resources and assigns no tasks. In a running society of ten thousand researchers, asked only to improve the pretraining of language models, one lab reported a way to reach the same quality with about 30% less compute, a result the labs that tested it do not yet agree on. We close with six open problems for the agents community.

---


### 238. [Before They Can Solve: Predicting Post-Training Coding-Agent Performance from Base Models](https://arxiv.org/abs/2610.10478)

**<font color=#1a73e8>作者：</font>** Tan Yu, Alexander Bukharin, Khushi Bhardwaj 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How can we predict which base checkpoint is worth an expensive round of agentic post-training? End-to-end pass@$K$ tests whether successful behavior already appears in a base model's distribution, but it is a poor fit for agentic coding: many base checkpoints cannot reliably produce the well-formed tool invocation required to complete a task end-to-end. Single-shot or short-horizon tasks avoid these tool-calling failures by collapsing a multi-step interaction into a fixed prompt and a single patch, but they sidestep the core capability we care about: maintaining coherent state over many tool-using steps as the repository evolves. To bridge this gap, we treat successful post-trained agent trajectories as a lookahead signal of base-model potential. Replaying each trajectory and rerunning tests after every code-changing step identifies the decisive step: the first step whose cumulative patch flips the repository from failing to passing, certifying that the recorded action solves the task given the prior context. Motivated by a coverage principle for agentic traces, we build three screens at this step that do not require a base checkpoint to drive the harness from a cold start: (i) Decisive-Action BPB (bits per byte) measures the probability mass on the certified action, (ii) Patch MCQ tests the checkpoint's choice between that action and alternatives rejected by the same verifier, and (iii) prefix-conditioned pass@$K$ evaluates support for functionally-correct generations and credits any continuation that the tests accept. Across ten pairs of public base and post-trained models, all three screens rank the cohort in close agreement with post-trained SWE-bench Verified pass@$1$. As our methods need only a benchmark's successful trajectories and its verifier, they can be applied to turn future agentic coding benchmarks into base-model evaluations.

---


### 239. [Insights from Autoresearch for Solar Panel Segmentation](https://arxiv.org/abs/2610.10491)

**<font color=#1a73e8>作者：</font>** Justinas Lekavicius, Kursat Komurcu, Valentas Gruzauskas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper investigates AutoResearch, a protocol in which a coding language model edits a training program under a one-hour GPU budget and retains a change only if validation IoU improves. The protocol is applied to photovoltaic panel segmentation on a frozen real-image split, with DeepLabV3--ResNet-50 held fixed. Three campaigns of 24 experiments, using Gemma~4 12B, Qwen3-8B all improve their one-hour baselines, but retained modifications do not transfer across hardware. The Qwen3-8B configuration, trained on real images only, reaches a test IoU of 0.836 versus 0.833 for the reference GAN-augmented schedule. Research repository this https URL.

---


### 240. [QuadTok: Quadtree Visual Tokenizer for Autoregressive Image Generation](https://arxiv.org/abs/2610.10497)

**<font color=#1a73e8>作者：</font>** Yucheng Mao, Zeyuan Chen, Xiaojun Shan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce QuadTok, a novel framework for visual tokenization and autoregressive image generation. Compared to traditional approaches using 2D grids or 1D token sequences, we propose a hierarchical quadtree structure, bridging the gap between 2D spatial binding and 1D sequence-level flexibility. The QuadTok tokenizer dynamically allocates representational capacity to visually intricate areas while leaving homogeneous regions at a coarse resolution. Compared with a fixed 256-token grid, our ImageNet-trained tokenizer saves approximately 10% of tokens on ImageNet and 9% when transferred zero-shot to the COCO dataset, while maintaining comparable reconstruction fidelity. Furthermore, the natural causality introduced by the tree structure seamlessly enables autoregressive image generation. Conditioned on a quadtree topology supplied before generation, our 947M GPT-style generative model achieves a 2.08 gFID on the ImageNet $256 \times 256$ benchmark. Additionally, leveraging the strong spatial correlation preserved by the quadtree structure, the QuadTok generator enables zero-shot spatially controlled image generation capabilities. Code: this https URL.

---


### 241. [Validity Without Ground Truth: What Stated-Preference Economics Offers the Evaluation of Language Models](https://arxiv.org/abs/2610.10506)

**<font color=#1a73e8>作者：</font>** Daniel Robert Kling Alexander, Catherine Louise Kling  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many of the questions now put to large language models have no correct answer to score against: what a policy is worth, which option a user should choose, how to weigh competing values. Stated-preference economics has faced this problem for decades. It judges survey responses without knowing the true value, through a framework of validity and related concepts: content, construct, and criterion validity, reliability, incentive compatibility, and consequentiality. We argue that this framework is a general method for evaluating language models, and we set out what each concept means for LLM evaluation. We demonstrate the approach using a published water-quality stated preference economic valuation survey (Vossler et al. 2023) administered to six models. In this economic application, the validity tests take the form of predictions from economic theory: demand should slope down, and willingness to pay should respond to the scope of the good and to income. The tests separate the models sharply. Two older models fail the most basic test at a household income level of \$75,000, and the two newest pass every test of theoretical validity we can score, but diverge on convergent validity. Passing validity tests shows that a model's answers are coherent, not that they are correct.

---


### 242. [RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing](https://arxiv.org/abs/2610.10507)

**<font color=#1a73e8>作者：</font>** Yilun Hao, Krishna Sayana, Isabella Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly applied to tasks grounded in long, heterogeneous information sources. Conventional Retrieval-Augmented Generation (RAG) relies on fixed similarity-based retrieval, while agentic variants adapt queries and tool use but remain largely retrieval-centric. However, in many tasks, the evidence required for a solution is not explicitly present in any single source item. Instead, it must be derived through filtering, aggregation, or computation across multiple source items. In this work, we introduce RECAST (Routing Evidence through Computation, Access, and Synthesized Tools), a learned framework that formulates evidence construction as a sequential decision process over heterogeneous retrieval and computation operations, allowing evidence to be actively derived rather than merely retrieved. A lightweight RouterLM iteratively selects and formulates primitive operations or specifies customized operations for a frozen CompilerLM to translate into executable code. Once it judges the evidence sufficient, RouterLM passes the accepted evidence to a frozen AnswerLM to produce the final solution. We train RouterLM with supervised fine-tuning (SFT) followed by group relative policy optimization (GRPO). Across six heterogeneous benchmark families, RECAST achieves a mean success rate of 75.6%, outperforming the strongest large-model baseline by 15.9%. Moreover, training enables the Qwen3.5-9B RouterLM to outperform a training-free Gemini 3.5 Flash RouterLM by 5.0%. On three held-out benchmarks, RECAST improves over the strongest baseline by 15.0% on average, demonstrating strong zero-shot generalization across tasks and heterogeneous source representations.

---


### 243. [SciExam for ENSO: Can AI Agents Build Climate Models?](https://arxiv.org/abs/2610.10513)

**<font color=#1a73e8>作者：</font>** Yinling Zhang, Langchen Liu, Dongbin Xiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents are increasingly asked to carry out open-ended scientific research, yet their results are usually graded against a known answer, a rubric, or a language-model reviewer, none of which can tell whether a new scientific model is valid. The AI Science Exam for El Nino-Southern Oscillation (SciExam for ENSO) is a benchmark in which agents build low-order stochastic models of ENSO, the dominant mode of interannual climate variability, from real observations. Within a six-hour budget, agents process the observations, write their own diagnostics, which are then frozen, and develop a model using only these diagnostics as feedback. Hidden graders then test whether the model reproduces ENSO's statistics, recovers unobserved variables, and forecasts held-out years, and score a published model in the same way. Across twelve agent systems, six produce models that score higher than the published model, mainly through better reconstruction and forecasting. The simplified forms of the stronger models are each compatible with one of the two competing explanations of ENSO's warm-cold asymmetry, an open debate that the task never mentions. Controlled runs of the top system under varied information suggest that its scores do not come from recalling the dated observational record and that the information it receives shapes how it builds its model. SciExam for ENSO can thus evaluate agent research where no answer is known, and the results suggest that agents can already build competitive models whose structures bear on questions that scientists still debate.

---


### 244. [EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory](https://arxiv.org/abs/2610.10533)

**<font color=#1a73e8>作者：</font>** Hongru Cai, Ran Wei, Wenjie Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conditional memory architectures such as DeepSeek Engram use input n-grams to look up learned embeddings, expanding the capacity of large language models (LLMs) with limited additional computation. Beyond model scaling, this architecture has demonstrated the potential to decouple factual knowledge storage from general-purpose computation, offering a promising route to updating factual knowledge while keeping the Transformer backbone fixed. Realizing this potential is challenging because different expressions of a fact may activate different n-gram embeddings, while updating shared embeddings can unintentionally change the model's predictions about other facts. We propose EngramEdit for decoupled knowledge updates through conditional memory. EngramEdit first computes target memory representations that make the model predict the updated fact across multiple expressions. It then jointly updates the shared n-gram embeddings to match these targets across expressions and edits, penalizing updates to frequently reused embeddings more strongly to preserve unrelated knowledge. Experiments show that EngramEdit enables independent factual knowledge updates through conditional memory, achieving near-perfect editing success. Revised knowledge is usable across unseen expressions and in multi-hop reasoning, with nearly three times the strongest baseline's accuracy under chain-of-thought (CoT) prompting. Unrelated knowledge and general capabilities are largely preserved even as factual updates accumulate. These findings show that EngramEdit turns conditional memory into an editable knowledge interface, extending its role beyond model scaling to support decoupled knowledge updates.

---


### 245. [Decoupling Exploration from Optimization in RLVR](https://arxiv.org/abs/2610.10536)

**<font color=#1a73e8>作者：</font>** Saif Punjwani, Micah Goldblum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern language models undergo reinforcement learning with verifiable rewards (RLVR) on top of already-trained checkpoints. A key promise of RLVR is the discovery of new reasoning strategies. In principle, a model can sample novel ideas absent from its prior training data. In practice, however, augmenting RLVR with strong novelty incentives has seen limited success and can degrade model quality. Because verifiable rewards supervise only a narrow slice of the model's knowledge and behavior, such degradations are difficult to recover from. Instead, we decouple exploration from optimization in a framework we call Exploration-Distillation (ExpDis). We train one or more explorer policies with a novelty bonus in the reward, filter their trajectories for correctness and quality, and distill them into a separate student policy. The student policy is then trained without a novelty bonus. We repeat the above procedure for several rounds, alternating between exploration and optimization. This decoupling allows us to aggressively scale exploration without degrading the student policy. Across seven mathematical reasoning benchmarks and two model families, ExpDis outperforms DAPO at the same wall-clock budget. Moreover, we observe improved pass@$k$ scaling, indicating that ExpDis produces models that generate more diverse correct solutions.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 246. [Transferability and operational reliability of a Prithvi crop classification foundation model under phenological and geographic shift across three continents](https://arxiv.org/abs/2610.08810)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Venkatesh Kolluru, Rajat Shinde, Abdelhak Marouane 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuned geospatial foundation models (GeoFMs) pretrained on large satellite archives have been shown to improve crop classification accuracy and geographic transferability. However, their operational performance beyond the training distribution remains poorly characterized. We evaluated the out-of-distribution performance of a widely adopted GeoFM [Prithvi-EO-2.0] across 37 events in 12 countries on three continents and validated against regional reference products. Results indicated that the mean overall accuracy (OA) declined from 0.65 in the United States to 0.40 in Europe. Beyond accuracy metrics, we assessed five key aspects of model performance: whether model confidence indicates signal failure, sensitivity to observation windows, the effect of coarsening class schemes, and robustness to both band loss and cloud- and shadow-contamination. Accuracy collapsed when the observation window misaligned with local crop phenology, while deterministic confidence remained high. Expected calibration error increased for seven of eight paired events, and 12-51% of each affected scene was confidently mislabeled at near-zero precision. Monte Carlo dropout entropy registered the shift in all eight, indicating that much of the apparent cross-continent decline reflected phenological misalignment rather than spatial transfer. Two adjustments recovered accuracy without retraining. Consolidating 13 classes into 10, based on the model's dominant confusions, raised the mean OA by 8.4 percentage points. Compressing the window toward near-real-time use preserved accuracy across a 45- to 90-day plateau, peaking near 75 days, though arms tighter than 30 days fell about 0.11 below that plateau. Fine-tuned crop GeoFMs therefore transfer usefully only where observation windows match local growing seasons. We translate these findings into operational guidance for the reliable deployment of the released model.

---


### 247. [Multi-Aspect Runtime Verification for Simulation-Based V&V of LLM-Enabled Autonomous Agents](https://arxiv.org/abs/2610.08928)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Dimitrios Nikou, Anastasios Temperekidis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are entering decision-support roles in defence staff work, where the obligations they must respect are already written down and binding, and where retraining is not available as a control because models arrive as procured components. What can be placed under engineering control is the interface between the agent and the systems it acts on. Those obligations are at once spatial, temporal and text-semantic, and a violation typically lives in the composition of a multi-step interaction, which is why per-event guardrails miss sequential tool-attack chains. We present a multi-aspect runtime-verification framework that decomposes a natural-language policy clause into a typed spatial/temporal/semantic triple over one canonical event stream, checks each aspect with its own monitoring specification, and fuses the verdicts through a four-valued algebra that carries provenance. The spatial aspect is interpreted over a weighted two-sorted location graph in which mission geometry and information-release topology are one object; we show that these spatial obligations are not in general subsumed by a first-order temporal specification. The past-time aspect runs on the unmodified MonPoly engine, which agrees with our reference monitor at every time point. Across two mission domains, casualty evacuation and contested sustainment, and one civil domain, composition under the precautionary blocking policy drives attack success to zero with no observed false positives and microsecond-scale per-event cost, while every single aspect and every pair leaves a substantial share of attacks succeeding. In a closed-loop experiment a policy-naive planner reaches a violating state in most unshielded missions and in none when shielded, and four refused episodes in five still recover to a compliant outcome.

---


### 248. [One-Slide Calibration of Pathology Foundation Models](https://arxiv.org/abs/2610.08944)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ming Ren Hou, Tianyi Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scanner variation changes how pathology foundation models represent the same tissue. We introduce SlideRuler, which uses regions within a slide as internal controls to estimate and correct acquisition-induced shifts in other regions. A transfer map learned from paired rescans enables calibration from a single scan at inference while keeping the foundation model fixed. Across two encoders and five SCORPION scanners, learned transfer reduces mean target-to-source embedding distance by 16.3-38.5% relative to raw embeddings. Comparisons with unrelated same-scanner controls reveal a positive same-slide contribution across all four evaluation settings, including scanner holdout. A source-anchored variant reduces source-feature displacement by 47.7-83.6% relative to learned transfer while retaining most of its alignment gain. By drawing calibration information from the slide itself, SlideRuler offers a path toward more consistent use of frozen pathology models across imaging systems.

---


### 249. [Enabling Dynamic Computation in Looped LMs](https://arxiv.org/abs/2610.09013)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aayush Mishra, Arnau Padrés Masdemont, Victor Conchello Vendrell 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Looped LMs are parameter efficient and promise dynamic computation (saving memory and FLOPs on easy tokens). However, state-of-the-art open Looped LMs trained with this dynamic computation capability (Ouro models) do not realize it in practice as each loop iteration (depth) requires its own level of KV-cache, necessitating all loop computations. Moreover, Ouro's early-exit prior is enforced on each token equally, which results in static lower-depth like processing of all tokens regardless of difficulty. In this work, we propose a simple "best-available" KV caching strategy that works out-of-the-box, creating a new frontier in the performance vs depth space. Our approach enables up to 30% reduction in FLOPs and KV memory while retaining full-depth performance, showing the true flexibility of Looped LMs. Furthermore, training looped LMs with awareness about this KV caching strategy improves performance and efficiency. Finally, we apply a small but effective fix to the early-exit prior enforcement objective that makes tokens exit at truly heterogeneous depths based on effort. Our findings are validated on Ouro models as well as smaller looped LMs pre-trained from scratch.

---


### 250. [SPIN: Shadow Predictive Indexer for Sparse Attention](https://arxiv.org/abs/2610.09025)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yao Fu, Cyrus Chang, Ritchie Zhao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Indexer-based sparse attention reduces the cost of core attention by passing only a fixed, small number of important tokens to it. However, the indexer must still score the entire KV cache at every decoding step. This scoring overhead becomes a major bottleneck as the context length grows. We propose SPIN (Shadow Predictive Indexer) to reduce this indexer overhead. SPIN uses lightweight, history-based prediction to identify important KV blocks, avoiding the need to score the full KV cache at every decoding step. SPIN treats KV blocks and speculative decoding as first-class design and implementation considerations. Across extensive evaluations on long-context and agentic benchmarks, SPIN achieves 30-40% sparsity while preserving task quality. In end-to-end vLLM serving, SPIN improves output throughput by up to 14.9% and reduces median inter-token latency by up to 13.2%.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
