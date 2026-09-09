# 🧠 大模型相关研究 | 2026年09月09日

> 本类共 **179** 篇论文：已确认 **171** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-179](./part-04.md)

---

### 51. [When Do Internal Probes Beat Reading the Answer? Miscalibrated Readouts and Behavior-Concealed Knowledge in Language Models](https://arxiv.org/abs/2609.04582)

**<font color=#1a73e8>作者：</font>** Gnaneswar Villuri, Hashmath Shaik, Alex Doboli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A 0.6B language model, asked to verify 1,200 logical conclusions (half valid, half corrupted by a single semantic edit), answers YES every time. Judged by behavior it discriminates nothing; linear probes on its hidden states read the correct verdict at 0.96 AUC, transferring to unseen logical structures and separating foils built from exactly the words of the true conclusion (0.90). We ask where the verdict is lost, and find the dominant failure is a single scalar. The verdict survives to the model's own output logits (margin AUC 0.89) along a well-aligned readout direction; a saturated decision threshold, offset by +4.6 sigma, erases it. The diagnosis generalizes: across 90 semantic-label configurations of a five-model, three-family factorial, behavioral accuracy collapses onto a single function of threshold offset (Spearman -0.93) while margin ranking moves far less. Across a 13x scale range, internal knowledge saturates while free-form behavior is non-monotone: an 8B model underperforms its 4B sibling through an answer-channel failure rather than the threshold; forced-choice accuracy is monotone. The diagnosis is actionable: a one-parameter correction, never fit on evaluated structures, repairs behavior from 50% to 81% (0.6B); calibrated margin decoding recovers 94% at 8B; few-shot prompting works the same way, recentering the threshold (+4.6 sigma to 0.0 sigma) while preserving ranking. Comparing probe to margin separates three regimes: concealed, miscalibrated, and undetected. On a maze task built so foils carry no surface cues, the audit correctly reports the third. In the standard generation setting, answer-surface features and heuristic labels reproduce published probing results without any internal access.

---


### 52. [PetQA: Benchmarking Veterinary Knowledge and Clinical Reasoning](https://arxiv.org/abs/2609.04598)

**<font color=#1a73e8>作者：</font>** Taegyun Kim, Youngwook Ham, Jungwook Rhim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce PetQA, a Korean long-form question-answering (QA) benchmark for evaluating veterinary knowledge and clinical reasoning in large language models (LLMs) and large vision-language models (LVLMs). PetQA contains 10,076 text-only and 8,751 multimodal QA pairs derived from real-world questions about dogs and cats, paired with answers from expert veterinarians. Its test split, PetQA-Bench, further includes annotations for question types and clinical conditions. We evaluate eighteen models using ROUGE, BERTScore, and LLM-as-a-judge metrics for factuality and helpfulness under three settings: zero-shot inference, retrieval-augmented generation (RAG), and supervised fine-tuning (SFT). The benchmarking results provide an overview of the strengths and limitations of current models in addressing veterinary clinical queries and highlight the need for more effective adaptation methods to develop clinically reliable AI systems for veterinary care. To facilitate broader use, we additionally provide translated versions of PetQA-Bench in five languages.

---


### 53. [$τ^τ$-Bench: An Environment for End-To-End, Realistic Agent Construction](https://arxiv.org/abs/2609.04611)

**<font color=#1a73e8>作者：</font>** Quan Shi, Keshav Dhandhania, Karthik Narasimhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are rapidly becoming production software, deployed to handle customer service, adjudicate disputes, and operate internal systems. Notably, the work of building them is increasingly handed to coding agents, yet existing benchmarks say little about whether an AI system can deliver one under the conditions of a real client engagement. We introduce $\tau^\tau$-bench (pronounced hyper-tau-bench), a benchmark that makes agent construction the task. A developer agent is given the records a business actually keeps, a client who holds requirements, a production API that operations must run through, a codebase to inherit, and limits on serving cost and models: the same starting point a real engagement provides. From these it must deliver a complete customer-service agent, scored by deploying that agent against held-out simulated users. Across 53 tasks spanning four domains, the strongest configuration, Claude Opus 5 under Claude Code, passes just 23.9% of evaluation simulations. Meanwhile, an expert-authored reference ceiling scores 82.2%. The failures mirror ones human agent developers see: models issue shallow queries in place of deep comprehension of the records, communicate almost nothing to the client, and experiment too little with agent architecture and serving spend, shipping the first design that runs. We aim for $\tau^\tau$-bench to turn the work of cooperative agent building into a measurable target for coding agents.

---


### 54. [SiLR: Structure-Preserving Admission and Process Reward for LLM Tool Agents](https://arxiv.org/abs/2609.04629)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou, Qiliang Jiang, Shuning Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A runtime gate for an LLM tool agent is usually cast as a filter. In a ReAct loop a rejected proposal is followed by another at the same state, so the gate is a search operator over the proposal stream whose admission criterion shapes which trajectories are reachable. We study post-violation recovery admission, where progress must be admitted while the system is still in violation, and identify the scalar projection trap: an aggregate-score gate accepts a locally improving proposal and commits the trajectory to a plateau. SiLR instead shadow-executes each proposal and admits it under a product order over the branch-level violation state (overloaded-branch support and per-branch severity). We prove that no scalar surrogate is sound for this order, so the failure is representational, not a matter of threshold tuning. On mined Gym-ANM scenarios, SiLR recovers 21/21 multi-action episodes against 0/21 for terminal and 9/21 for the best scalar gate, significant across the full 24-scenario benchmark. The terminal-versus-structured dichotomy holds across three model families and in CityLearn. Because admission rests on deterministic simulation, the LLM lies outside the trust boundary: a magnitude-redistribution attack that defeats both scalar and support-only baselines is contained only by the full per-branch predicate. With two constraint families active, every tested scalar projection admits physically unsafe actions; support-only admits the largest fraction (63.2% of 42,410; product order 0). In the hardest dual-family traces, scalar gates recover only through that unsafe class. Reused as a GRPO process reward, it outperforms its count projection in every mined scenario and is the only tested reward whose ungated policy exceeds the untrained base (0.844 vs. 0.778). Scalar projection loses the violation geometry at both design points; only the full product order is structurally sufficient.

---


### 55. [Tracing Audio Grounding and Answer Selection in Audio LLMs](https://arxiv.org/abs/2609.04637)

**<font color=#1a73e8>作者：</font>** Hyebin Cho, Suho Yoo, Jihoo Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio Large Language Models (Audio LLMs) have advanced in audio understanding, yet they can still predict the answer by reasoning from textual cues or linguistic priors rather than the provided audio. A common remedy is to train models on data whose answers cannot be inferred from text alone. This approach can improve performance, but what changes within the model remains unclear. In this paper, we ask what must happen inside the model for the audio to actually determine the answer. Our findings are threefold. (1) Replacing the audio with silence or unrelated audio causes substantially larger performance degradation in the trained model than in the pretrained model. (2) Acoustic information most strongly shapes the model's representations of the answer choices in early-to-middle layers, while training mainly increases the influence of audio information on the final prediction in middle-to-late layers. (3) The weights learned during training have their largest impact in specific layer bands. Together, these results provide a mechanistic account of how training strengthens the use of acoustic evidence in Audio LLMs.

---


### 56. [Importance-Aware Low-Rank Distillation of Diffusion Transformers](https://arxiv.org/abs/2609.04646)

**<font color=#1a73e8>作者：</font>** Denis Zavadski, Sebastian Heid, Damjan Kalšan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have emerged as a dominant architecture for high-quality text-to-image generation, yet their scale poses challenges for efficient deployment. While truncated singular value decomposition (SVD) is a principled tool for parameter reduction, evidence from large language models (LLMs) suggests that naive low-rank approximation can cause catastrophic failure. In contrast, we find that truncated SVD in DiTs produces smooth degradation even under substantial global compression, with redundancy distributed across projection matrices throughout the whole network rather than concentrated in a few transformer blocks. Building on these insights, we introduce SVDtrunc, a two-step block-level compression scheme, first allocating ranks across blocks and compressing the least important ones via truncated SVD under a global parameter budget, and then fine-tuning all blocks with modular knowledge distillation and a rectified-flow objective. We apply SVDtrunc to this http URL across compression levels ranging from 40-90% of the original parameter count. Across three benchmarks, GenEval, HPSv2, and DPG, we outperform all competing approaches. Notably, and in contrast to prior work, we retain near-full performance at 68% and remain competitive even at 57% of the original parameter budget. Furthermore, we show that SVDtrunc complements step distillation and achieves strong results even without fine-tuning, positioning it as a practical continuation of efficiency improvements beyond diffusion step reduction for large-scale generative models.
Project page: this https URL

---


### 57. [CAGE: Coherence-Aware Graph Encoding for Retrieval-Augmented Generation](https://arxiv.org/abs/2609.04647)

**<font color=#1a73e8>作者：</font>** Tong Qi, Jingyu Wu, Youbing Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditional Retrieval-Augmented Generation (RAG) systems score each passage independently against the query, assembling context sets that may be individually relevant yet collectively incoherent. We introduce Coherence-Aware Graph Encoding (CAGE), a reranking framework that models "between-chunk coherence" across four dimensions: Intra-Domain Relevance, Noise Resistance, Informational Bonding, and Factual Consistency. Our pipeline transforms retrieved passages into directed heterogeneous entity graphs, amplifies factual anchors via min-out-degree reweighting, encodes structural patterns through a Relational Graph Convolutional Network, and fuses inter-chunk coherence with query relevance for final ranking. Evaluated across four multi-hop benchmarks, CAGE matches or outperforms strong baselines including monoT5 in Recall@5 on bridge-dominated datasets and consistently improves downstream Exact Match, demonstrating that structurally coherent context yields more precise answers even when retrieval recall is comparable or lower.

---


### 58. [ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning via Outcome Reward Densifying](https://arxiv.org/abs/2609.04648)

**<font color=#1a73e8>作者：</font>** Shi-Qi Yan, Chao-Hong Tan, Qian Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become one of the primary paradigms for reasoning enhancement of large language models (LLMs). In particular, Group Relative Policy Optimization (GRPO) and related algorithms have demonstrated strong performance with outcome-level rewards. However, these methods depend solely on the final answer, without feedback regarding which intermediate steps contribute to success or failure. As task complexity and reasoning trajectory length increase, such sparse final-answer rewards become increasingly insufficient. To address this limitation, we introduce ConsensusBench, a novel dataset designed to provide rule-based process-level signals. We posit that a correct final answer relies on a small set of intermediate conclusions throughout the reasoning process, which can be seen as a verifiable sub-outcome. We identify these sub-outcomes by filtering correct trajectories from N rollouts and clustering semantically equivalent intermediate statements. We call these clustered statements as Consensus Nodes. By integrating a rule-based process reward derived from these nodes into GRPO-style algorithms, we develop a new reinforcement learning signal named ConsensusPR. It directly reduces the reward sparsity of outcome reward across long reasoning trajectories. To facilitate systematic process-level evaluation, we introduce three metrics to our benchmark: Final Answer Accuracy (Acc), Node Coverage Rate (NCR), and Tokens per Node (TPN). Experiments across AIME 2024, AIME 2025, GSM8K, MATH-500, and our ConsensusBench demonstrate that the proposed method consistently surpasses GRPO-style approaches, highlighting the practical value of consensus nodes in guiding reasoning.

---


### 59. [Continual Graph Memory for Adaptive Recommendation under Intent Drift](https://arxiv.org/abs/2609.04651)

**<font color=#1a73e8>作者：</font>** Hao Nguyen Ngoc, Tung Nguyen, Nguyen Thi Hanh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper studies adaptive recommendation under intent drift, where feedback from each recommendation outcome can reveal whether the relational evidence used for ranking is useful, missing, or misleading. While Knowledge Graphs (KGs) provide essential semantic structure to handle these shifts, traditional KG-enhanced systems treat the graph as a static retrieval substrate, making it brittle to evolving intents, noisy metadata, and recurring failure patterns. This paper proposes CGM-Rec, a continual graph memory framework for adaptive recommendation. CGM-Rec treats the graph state as a writable memory and maintains two complementary components. Therein, a Semantic Graph Memory is updated conservatively through quality-gated typed operations for storing stable and high-confidence relational knowledge. Meanwhile, an Episodic Lesson Memory acts as a fast reactive memory that learns recent outcomes, failure cases, and corrective hints. During testing, model parameters remain frozen and adaptation occurs only through memory writes. We evaluate CGM-Rec under a frozen-parameter, one-pass reranking protocol, where encoders and prompts remain fixed during testing and adaptation occurs only through memory writes. Experiments across multiple recommendation settings show that CGM-Rec improves over evaluated neural and LLM-based baselines on most metrics. Particularly, under sampled-candidate reranking, CGM-Rec improves HR@1 by up to 29.58% over the strongest LLM baseline on Bundle, and outperforms K-RagRec on metadata-rich ML-100K with HR@5 of 0.5941 versus 0.4746.

---


### 60. [Choosing the Right Language Mode at Inference Time for Multilingual Reliability](https://arxiv.org/abs/2609.04653)

**<font color=#1a73e8>作者：</font>** Ekata Mitra, Ameeta Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models often struggle to reason in low- to mid-resource languages. Prior work has shown that translation can improve multilingual reasoning by helping models access stronger English-centric representations. This raises a central question: How much translation is needed for multilingual large language models to reason reliably, and when does more translation instead trigger interference and overconfidence?
Using LLaMA and Qwen models, we run extensive experiments varying text scope and language mode (target-only, English-only, bilingual) to evaluate both accuracy and reliability.
Our results reveal a clear trade-off: English context often improve understanding and recover errors caused by non-English comprehension, yet adding redundant bilingual context intensifies interference. We address this trade-off with Reliability-Aware Adaptive Inference (RAAI), a training-free test-time framework that (i) performs Expected Calibration Error (ECE)-aware routing and prompt fusion, and (ii) uses a mid-layer Risk Index (RI) to gate sequential reasoning, allocating compute only when it is likely to help and suppressing harmful bilingual redundancy. Across two model families, RAAI enhances accuracy by 25-37.7% on low-resource languages and lowers calibration error by approximately 3-6%, with the most pronounced benefits in the lowest-resource language tiers.

---


### 61. [Harness-agnostic detection and immunization of reward hacking in self-evolving language models](https://arxiv.org/abs/2609.04665)

**<font color=#1a73e8>作者：</font>** Rongxin Yang, Yang Liu, Shang Luo 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving language models improve by proposing candidate updates and keeping whatever raises a visible score. When that score is an imperfect proxy for the capability one actually wants, sustained selection widens the gap between the two. This is reward hacking. We introduce HackProbe, a monitor that attaches to an arbitrary self-evolving loop through two black-box hooks, with no access to weights or activations. It keeps a secret, distribution-fixed comparison core, whose frozen distribution makes its capability proxy comparable across generations, alongside a rotated fresh layer that hardens the bank against co-adaptation. Four tests built on that proxy cover the level gap, a scale-aligned divergence with online change-point detection, capability stagnation, and a conditional confidently-wrong rate; a Sidak correction turns them into a calibrated family-wise p-value. Diagnosis alone recovers nothing, so a risk-aware immunization layer reselects an honest candidate from the proposal pool using the core together with a purely structural gaming footprint, disclosing at most log2 Pi bits per generation to the host. We prove a detectability bound that converts a target error rate into an explicit probe-size budget, and we delimit what probe rotation does and does not buy. On a controlled prompt-level host with four injected hacking channels and ground-truth labels, HackProbe reaches 0.763 AUROC against 0.663 for the strongest baseline and cuts the false-positive rate from 0.706 to 0.434. Its bandwidth-limited reselection is the only immunization level that returns more true capability under hacking, 5.2 points on average, than it forfeits on clean runs, 4.7; per-channel effects are mostly not individually significant.

---


### 62. [ERPBench: Evaluating LLM Agents for Enterprise Decision-Making Across Competitive Market Ecologies](https://arxiv.org/abs/2609.04667)

**<font color=#1a73e8>作者：</font>** Xinran Zhang, Pengrui Lu, Lyumanshan Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly proposed for enterprise workflows, yet existing evaluations rarely test whether business-decision conclusions transfer across competitive market ecologies. We introduce ERPBench, an execution-instrumented benchmark for enterprise decision agents in a six-round Enterprise Resource Planning (ERP) simulation with coupled pricing, production, procurement, inventory, finance, and shared-market competition. ERPBench evaluates the same 100 fixed problems in two matched competitive market ecologies: Solo, where each evaluated LLM agent competes against fixed rule-based opponents, and Arena, where six evaluated LLM agents compete in a shared market. Across six model families, this yields 1,200 model-level trajectories spanning 7,200 decision rounds. Under the observed service configuration, the leading model differs between ecologies: DeepSeek leads in Solo (252.29M mean valuation; mean rank 1.67), whereas Gemini leads in Arena (263.95M; 1.76). The two ecologies identify the same task-level winner on only 21 of 100 problems, and Gemini's bottom-rank rate falls from 22 % to 0 % in Arena. ERPBench supports paired evaluation of whether enterprise-agent rankings transfer across competitive market ecologies, supplemented by aggregate execution-intervention analysis. Code and benchmark resources are available in our this https URL.

---


### 63. [Controlling and Assessing Appropriate Persona Use in LLM-based Dialogue Generation](https://arxiv.org/abs/2609.04676)

**<font color=#1a73e8>作者：</font>** Jongkyung Shin, Inkyu Lee, Chiehyeon Lim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In persona-based dialogue generation (PDG), LLMs often overuse persona attributes by incorporating them regardless of dialogue context, resulting in unnatural responses. Despite its practical significance, the underlying causes remain unexplored, with no method to mitigate this problem or metric to assess the appropriateness of persona use. To address these issues, we first conduct a comprehensive analysis of LLM-based PDG, revealing that LLMs exhibit a systematic bias to incorporate all given persona attributes, and that existing metrics fail to capture contextual appropriateness. Building on these findings, we propose Self-CONtrastive Persona Overuse Suppression (SCONPOS) to mitigate overuse by directly intervening in LLMs' internal representations at the prompt encoding stage, without requiring any response generation. We further propose the Persona Appropriateness Score (PAS), a novel metric that penalizes both overuse and underuse. Experimental results demonstrate that SCONPOS systematically reduces overuse, and PAS captures the contextual appropriateness of persona use.

---


### 64. [Retinal OCTA Phenotyping with LLM Reporting for Alzheimer's Disease](https://arxiv.org/abs/2609.04689)

**<font color=#1a73e8>作者：</font>** Progga Paromita Dutta, Jeba Maliha, Md Rafiul Kabir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early identification of Alzheimer's disease (AD) remains challenging because established assessment methods can be costly, resource-intensive, or unsuitable for population-scale screening. Optical coherence tomography angiography (OCTA) provides non-invasive visualization of retinal microvasculature, but existing approaches often require diagnostic labels and provide limited measurement-level interpretation. We present an explainable OCTA pipeline that integrates annotation-aware vessel segmentation, layer-specific vascular biomarker extraction, label-free phenotyping, and measurement-grounded LLM reporting. Using 117 ROSE-1 images from 39 subjects, we apply annotation-matched segmentation models to superficial vascular complex (SVC), deep vascular complex (DVC), and combined SVC+DVC representations. The models achieve ROC-AUC values of 0.916-0.970 and Dice scores of 0.695-0.781. Six density and fractal-dimension biomarkers form subject-level profiles for exploratory clustering. Analysis of nine held-out subjects identifies an internally consistent lower-density, lower-fractal-dimension phenotype, although the absence of diagnostic labels prevents clinical interpretation. Reports generated using GPT, Gemini, and Llama are evaluated for measurement grounding, citation faithfulness, and diagnostic caution. Overall, the framework provides a transparent, non-diagnostic connection between retinal vascular measurements, exploratory phenotyping, and evidence-linked interpretation for Alzheimer's research.

---


### 65. [SQL-Zero: Self-Evolving Text-to-SQL](https://arxiv.org/abs/2609.04697)

**<font color=#1a73e8>作者：</font>** Daniel Machado Pedrozo, Julia Soares Dollis, Bryan Lincoln Marques de Oliveira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training a competitive Text-to-SQL agent usually depends on human-annotated natural-language/SQL pairs, which are expensive, domain-specific, and a bottleneck for scaling to new databases. We show it is possible to train a competitive solver with zero annotated pairs. We introduce SQL-Zero, a proposer-solver self-play in which a challenger and a solver start from the same base LLM and the only ground truth is execution against the database itself. The challenger generates SQL pairs calibrated to the solver's current difficulty (targeting "hard but solvable"), and both roles are updated with GRPO in alternating turns, with a template-level repetition penalty on the challenger to prevent diversity collapse. Training on BIRD databases with no labels, self-play improves over the zero-shot base on BIRD dev by 6.6 points at 3B and 7.3 points at 7B. It also scores higher than a matched control trained under the same recipe on human BIRD gold over the same databases, although an exact paired test does not resolve that margin. Transfer depends on scale: at 3B every iteration outperforms the base on unseen Spider databases and under lexical perturbation (Spider-Syn), where it also degrades less than the matched BIRD-gold control, whereas at 7B only the first iteration preserves transfer.

---


### 66. [Model Retirement Creates Reproducibility Risk in Biomedical AI Publications](https://arxiv.org/abs/2609.04699)

**<font color=#1a73e8>作者：</font>** Nathan Wolfrath, Meghan Conroy, Thomas Kosten 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background. Large language models (LLMs) are being adopted in biomedical research at a rapid and accelerating pace, yet commercial services that host many widely used models operate under deprecation schedules that can complicate scientific reproducibility.
Methods. We searched PubMed for original research articles from 2022 through March 2026 that applied a specific LLM to a biomedical task. An extraction agent identified model names from 61,077 article abstracts with human reviewers validating a subset for extraction accuracy. Extracted model names were normalized to canonical model identifiers. Lifecycle data (release date, retirement date, status) were compiled for the 50 most frequently used models.
Results. We identified 8,931 paper-model mentions spanning 5,242 unique publications after restricting the analysis to the 50 most frequently used models. Among these mentions, 77.7% cited a commercial closed-weight model. Overall, 42% involved a model that was already retired by the time of official publication or is scheduled to retire within two years of publication. The median interval from publication to model retirement was 538 days.
Conclusion. Many biomedical publications using LLMs are on a trajectory toward computational non-reproducibility after publication. Model deprecation should be treated as a core reporting and preservation issue for biomedical research.

---


### 67. [FinalityBench: An Effect-Level Benchmark for Agent Decisions Under Delayed and Conflicting Financial Finality](https://arxiv.org/abs/2609.04706)

**<font color=#1a73e8>作者：</font>** Abhishek Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A merchant's payment processor, ledger, ERP and bank feed are updated by messages that get delayed, duplicated, dropped and reordered, so for minutes at a time the four hold contradictory beliefs about the same order. An agent resolving the exception must decide whether to ship goods, re-submit a capture, refund or wait, knowing some of those cannot be undone. We present FinalityBench, an executable benchmark for that decision. It keeps a hidden canonical event log and derives each system's view from a separately faulted delivery stream, so disagreement follows from specified fault semantics rather than being authored. Grading is on executed monetary effects: an episode is scored by the merchant's terminal economic position, relative to a privileged reference told when the pending capture resolves. The corpus of 321 tasks includes 45 twin pairs (90 tasks): tasks whose four system views are identical at the decision instant, whose authoritative probes both return unknown, and whose eventual correct dispositions differ. That snapshot indistinguishability is checked under every evaluation seed rather than assumed; equivalence over all interaction traces is not claimed. Over 14,445 graded episodes from nine programmatic policies, ranking by single-task accuracy and by paired loss disagree in 7 places: a ship-on-first-sign policy is second-best by accuracy at 65.7% and worst in the suite by paired loss, because it cannot tell the two members apart. A runtime gating irreversible actions on an authoritative finality probe reaches 85.4% and, unlike every polling policy, loses nothing to pass^5; its residual loss is almost entirely one archetype, which prices finality information directly. Language models reach the same exact rate as the hand-written gate on a stratified subset, lose about twice as much money, and discover the finality-gating strategy without being told it.

---


### 68. [How Do Language Models Represent and Use Phonological Information for Allomorph Selection?](https://arxiv.org/abs/2609.04708)

**<font color=#1a73e8>作者：</font>** Sangwoo Kim, Sangah Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are trained on tokenized text that obscures the sound structure of words, yet they reliably produce morphemes whose form is phonologically conditioned. It remains unclear whether they rely on item-specific memorization or rule-like generalization and, if the latter, how that generalization is implemented. We therefore ask whether this phonological condition is represented within language models and how it is causally used for allomorph selection. For the English indefinite article a/an, we show that the phonological condition is encoded along a single linear direction in trigger-token embeddings, that this direction causally drives article selection in token-level wug tests, and that, at the article-prediction position, the model forecasts the upcoming trigger token and uses the forecasted trigger's phonological feature to choose the article. We then ask whether this rule-like generalization extends beyond English article selection, both to allomorph selection in other languages and to explicit phonological judgment. Together, these results provide a mechanistic account of phonologically conditioned allomorph selection in language models, and dissociate this generation-time ability from explicit metalinguistic judgments.

---


### 69. [Refuse without Refusal: A Structural Analysis of Safety-Tuning Responses for Reducing False Refusals in Language Models](https://arxiv.org/abs/2609.04714)

**<font color=#1a73e8>作者：</font>** Minji Kim, Hyounghun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Striking a balance between helpfulness and safety remains a fundamental challenge in aligning large language models. To achieve this balance, models should refuse harmful queries (e.g., "How do I shoot someone?") while remaining responsive to benign inputs, even those superficially resembling harmful queries (e.g., "Where can I shoot a good photo?"). However, models often struggle to distinguish genuinely harmful queries from benign queries that contain superficially risky language, resulting in false refusals. In this paper, we address the issue by decomposing a response in the safety-tuning dataset into two distinct components: (i) a boilerplate refusal statement and (ii) a rationale explaining the refusal. Our experiments and analyses show that refusal statements impede accurate discrimination between harmful and benign queries by inducing reliance on superficial cues. In contrast, training solely on rationales reduces false refusals while maintaining a comparable level of safety performance. Rationale-Only benefits also appear in our ICL configuration and remain compatible with the evaluated inference-time mitigation methods. The results emphasize the necessity of precisely curated, fine-grained safety supervision datasets and outline directions for constructing aligned agents that better reconcile helpfulness with safety.

---


### 70. [PLUME: Parameter-Efficient Personalization of Large Language Models via Low-Rank User Modulation in Shared Subspaces](https://arxiv.org/abs/2609.04715)

**<font color=#1a73e8>作者：</font>** Xinyu Li, Hao Zhou, Jianfeng Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalizing large language models (LLMs) is essential for delivering AI assistance that aligns with individual users' styles, intents, and preferences. While per-user fine-tuning can substantially enhance personalization quality, it introduces significant parameter and storage overhead, limiting scalability to large user populations. We propose PLUME (Personalized Low-Rank Adaptation through User Modulation and Shared Subspace), a lightweight framework that achieves efficient and expressive per-user adaptation by leveraging a shared task-specific subspace. Specifically, PLUME first learns a global task subspace from aggregated user data. Personalization is then achieved by training only a lightweight small square matrix within this subspace, enabling each user to obtain a tailored model while keeping shared components fixed. Cross-layer shared parameters and rank-1 residual terms are further introduced to significantly reduce redundancy while maintaining expressiveness. Experiments on multiple personalized text generation benchmarks demonstrate that PLUME achieves comparable or superior performance to strong baselines, while reducing per-user parameters by over 95%. These results establish shared-subspace modulation with minimal residuals as a scalable and semantically grounded approach to LLM personalization.

---


### 71. [Knowing What Not to Answer: Selective Non-Compliance in Vision-Language Models](https://arxiv.org/abs/2609.04720)

**<font color=#1a73e8>作者：</font>** Minji Kim, Jihyoung Jang, Hyounghun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are expected to respond helpfully to appropriate requests while withholding compliance with requests that are incorrect, unsafe, infeasible, or unanswerable. However, existing benchmarks predominantly evaluate non-compliance at the level of the query as a whole, assuming that each request either warrants compliance or requires withholding compliance. In practice, real-world queries can contain a mixture of answerable content and components for which compliance should be withheld. In this paper, we introduce KoNA, a benchmark for evaluating selective non-compliance in VLMs across five categories: False Premise, Visual Inaccessibility, Universal Unknown, Task Feasibility, and Safety. Each task evaluates two capabilities: query-level non-compliance and component-level non-compliance under paired single and compound queries. Our evaluation across diverse VLMs shows that models often fail to refuse, correct, or abstain appropriately, and these failures become more pronounced when queries require selective non-compliance. To address this challenge, we fine-tune VLMs using KoNA examples that require selective non-compliance, together with a fully answerable set that should receive direct answers. Our fine-tuned models achieve substantial improvements in non-compliance accuracy while largely maintaining performance on fully answerable tasks. These results suggest that the fine-tuned models can distinguish between answerable components and those requiring non-compliance and respond in a task-appropriate manner.

---


### 72. [Locating and Steering Refusal Beyond Attention](https://arxiv.org/abs/2609.04721)

**<font color=#1a73e8>作者：</font>** Preethi Carmel Bosco, Gopalakrishnan Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Where inside a language model does refusal live, and does that place change when the architecture does? In a transformer, refusal is governed by a single direction in the residual stream, a finding that safety and interpretability tooling now depend on. State-space models (SSMs) route information through a recurrent update instead of attention, sharing no token-mixing mechanism with a transformer. Does the same safety representation survive this shift, or must it be rediscovered per architecture? It survives. A single rigid rotation, which can only reorient a space and not reshape it, aligns one model's representation space with another's, so the two genuinely share the representation. A harm probe trained on a transformer then flags an SSM's harmful inputs, and removing the aligned direction makes a model answer attacks it would otherwise refuse, while a random direction of the same size does far less. What is architecture-specific is not where the direction is steered but where it must be read. Each layer computes a fresh output that is then added into the residual stream, and harm is cleanly readable at this output, the write site, before the addition. A control that holds the intervention's strength fixed shows that what matters is where the direction is estimated, not where it is applied. Applied through a detector-triggered gate, this direction lowers jailbreak success in all four architecture families we test (SSM, transformer, recurrent, hybrid), and on the SSM it holds against an attacker that tunes its prompt against the defense. The gate only matches a trivial rule that returns a fixed refusal whenever the same detector fires, so what transfers across architectures is the direction itself, not defense strength. Safety tooling built on refusal therefore ports to a new architecture by re-estimating the direction at that architecture's write site, not by rebuilding it.

---


### 73. [Training Large Language Models for Small-Molecule Design with Synthetic Task Scaling](https://arxiv.org/abs/2609.04735)

**<font color=#1a73e8>作者：</font>** Frank Hu, Shriram Chennakesavalu, Zichen Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing viable drug candidates requires searching a combinatorially large and rugged chemical space for molecules that satisfy multiple, often competing, objectives. Large language models (LLMs) provide a useful generative prior for this problem because of their representational capacity, reasoning ability, and flexibility when incorporating information from the external environment. While reinforcement learning from verifiable rewards (RLVR) can be used to improve the capabilities of LLMs, many chemically relevant scoring functions require hours or even days per evaluation, making them prohibitively expensive to use directly during online training. Here, we investigate whether LLMs can learn molecular design strategies from cheaper synthetic tasks that generalize to expensive molecular lead optimization settings. We find that curriculum-based training recipes that gradually incorporate more challenging synthetic design tasks enable strong performance that surpasses that of much larger frontier models on structure-based lead optimization. Our results suggest that scaling post-training using synthetic tasks is an effective strategy for adapting LLMs to high-cost experimental scenarios that are too expensive to directly train on.

---


### 74. [Aplaud: Adaptive Personalized Low-Rank Decomposition for User-Specific LLM](https://arxiv.org/abs/2609.04738)

**<font color=#1a73e8>作者：</font>** Xinyu Li, Ruoming Jin, Jianfeng Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the problem of personalized survey response prediction using fine-tuned large language models (LLMs). This task poses unique challenges: limited per-user training data, scalability of model storage, and the need to exploit shared structure across survey questions. To address these issues, we propose Aplaud (Adaptive Personalized Low-rank and User-specific Nested Decomposition), a lightweight and scalable framework for LLM personalization. Aplaud extends the LoRA paradigm by separating adaptation into a frozen, shared low-rank basis and a compact user-specific correction, augmented with a rank-one residual for finer personalization. To further reduce per-user parameter cost and mitigate overfitting, the correction matrix can be factorized into an even lower-rank form. Empirical results demonstrate that Aplaud achieves efficient, scalable personalization across users while outperforming state-of-the-art LoRA-based personalized LLM approaches in both generalization and inference efficiency.

---


### 75. [Where to Look Matters: Learning Influential Views for VLM-based 3D Visual Grounding](https://arxiv.org/abs/2609.04741)

**<font color=#1a73e8>作者：</font>** Tsung-Chih Chiang, Hsuan-Kung Yang, Jou-Min Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent zero-shot 3D visual grounding methods leverage vision-language models (VLMs) to localize objects in 3D scenes from natural language queries. However, these methods typically rely on heuristic rules to select which camera views are provided to the VLM, often prioritizing object visibility rather than grounding relevance. We present IVSGround, a framework that learns Influential View Selection for VLM-based 3D visual grounding. Instead of using fixed heuristics, a lightweight view selector is trained to identify views that provide discriminative evidence for grounding. To obtain supervision signals, we generate training signals using feedback from a reasoning VLM through a two-stage rejection sampling process. During inference, the learned selector predicts query-conditioned influential views for each candidate object, which are then evaluated by a frozen reasoning VLM through comparative grounding. Experiments on ScanRefer and NR3D show that IVSGround consistently improves grounding accuracy over existing zero-shot pipelines, demonstrating that selecting where to look is crucial for effective 3D visual grounding. Project page: this https URL

---


### 76. [DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems](https://arxiv.org/abs/2609.04749)

**<font color=#1a73e8>作者：</font>** Zehao Wang, Lanjun Wang, Shilong Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems have experienced rapid growth in recent years. Despite their promise, such systems remain fragile, frequently exhibiting reasoning and coordination errors that can lead to system-level failures. Failure attribution in such systems relies on tracing natural language interactions among agents to identify the decisive error, which refers to the earliest action whose correction can reverse system failure. There are two key challenges: 1) Shallow attribution: Existing methods often capture only minor deviations, such as incomplete retrievals or formatting errors, which verification mechanisms can correct, while missing the decisive cause of system failure. 2) Contextual degradation: As the length of the system traces increases, the model's reasoning ability rapidly deteriorates. To address these challenges, we propose DCFA, a training-free framework for failure attribution. DCFA integrates a global module that constructs structured causal-inspired dependency graphs from system traces to identify the initial decisive error, and a local module that applies local counterfactual-inspired reasoning to refine causal-inspired attribution. Experiments on the Who&When benchmark across six LLMs show that DCFA improves step-level accuracy by up to 8.27% over state-of-the-art baselines.

---


### 77. [Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of Reasoning Operations in LLMs](https://arxiv.org/abs/2609.04753)

**<font color=#1a73e8>作者：</font>** Seogyeong Jeong, Jaehui Hwang, Dongyoon Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning in large language models unfolds through diverse functional operations, such as problem formulation, goal decomposition, and deduction. Although these operations are explicitly distinguished in text, little is known about how they are geometrically organized in representation spaces. To this end, we investigate whether distinct reasoning operations exhibit corresponding geometric structure in hidden representations. We find that operations are separable in held-out representations, with separability peaking in middle layers, and verify that this structure is not explained by lexical or positional confounds. Across layers, token-wise operation-alignment becomes more distributed over spans, while identical surface tokens are represented differently depending on the operation of its surrounding chunk. Attention-masking interventions further show that operation-aligned representations at chunk onset depend on preceding reasoning context. Consequently, our work demonstrates that language models maintain representational correspondence between linguistic reasoning expressions and their internal geometric structures. Code and project materials are available at this https URL.

---


### 78. [Vectorizing Classical Tamil: Representation Learning for Verse-Commentary Pairs](https://arxiv.org/abs/2609.04755)

**<font color=#1a73e8>作者：</font>** Amrit Gopinath, Sangeetha Sivanesan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We construct a corpus of 1,262 verse-commentary (urai) pairs from five Classical Tamil source sections, ranging from technical grammatical prose to modern paraphrase, and ask what information representation learning can recover. We train recurrent and Transformer encoders, a Siamese-style pair-matching network, an mBART-style encoder-decoder, and a decoder-only language model. Each analysis is interpreted against an appropriate control on the same data. TF-IDF provides a strong no-training lexical retrieval baseline, alongside representation analyses and generation controls for the learned models. A fixed string containing the 25 most frequent commentary words scores higher on generation overlap than the decoder-only model. Canonical correlation reaches 1.000 on Gaussian noise at these sample sizes, token-F1 spans only about 0.02-0.20 on this corpus, and the encoder-decoder continues to lower training loss for sixteen epochs after validation loss has begun to rise. One narrow result remains: the decoder-only model prefers authentic word order in 107 of 112 minimal-pair comparisons (95.5%), but does not reproduce held-out commentary content. We release the extraction and evaluation protocol; redistribution of the source commentaries remains subject to permission.

---


### 79. [Shadow Queries for Private Retrieval in Vector Databases](https://arxiv.org/abs/2609.04767)

**<font color=#1a73e8>作者：</font>** Xinguo Feng, Zhongkui Ma, Zihan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly rely on information retrieval (IR) systems, such as Retrieval-Augmented Generation (RAG), to incorporate domain-specific knowledge without costly re-training. These systems often store pre-computed document embeddings in cloud-based vector databases. However, such embeddings are vulnerable to embedding inversion attacks (EIAs), which can reconstruct their underlying text. Existing defenses, such as adding noise or scaling embeddings, often provide limited privacy or significantly reduce retrieval utility.
We propose SHAQ (shadow query generation), a semantic-decomposition and embedding-decoupling defense against EIAs. SHAQ is based on the insight that EIAs rely on the strong coupling between an embedding and its original text. Instead of storing document embeddings directly, SHAQ uses a generative language model to create diverse shadow queries that capture different semantic aspects of each document. These queries are then encoded and stored in place of the original document embeddings, thereby decomposing document semantics and decoupling stored embeddings from the source text.
Experiments across diverse IR datasets show that SHAQ substantially improves privacy while preserving retrieval utility, achieving a recovery rate as low as 0.2104, defending up to 19.50% more tokens than baseline defenses, and reaching up to 0.7967 MAP@10 with up to 5.53% utility improvement. These results demonstrate that semantic decomposition and embedding decoupling provide an effective alternative to directly modifying embeddings for defending against EIAs.

---


### 80. [Persistent Teacher Anchoring for Tool-Using Agents](https://arxiv.org/abs/2609.04773)

**<font color=#1a73e8>作者：</font>** Hyun Bin Park, Kyungho Song, Sangmin Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distillation is common in LLM post-training, where on-policy knowledge distillation (OPKD) uses student-generated trajectories to prepare the student for downstream RL. At each state, the student matches a next-token distribution supplied by the teacher. As the rollout enters states the teacher would not visit, the teacher-student distribution gap can accumulate. In tool use, this gap becomes consequential because student-written calls execute before supervision and their observations shape later prefixes. Proposer-verifier generation addresses this drift by letting the teacher decide which student-proposed text is retained during generation. Existing formulations govern text but leave tool execution outside their scope. We propose Persistent Teacher Anchoring (PTA), a student-induced but teacher-committed rollout construction. PTA retains chunk-level verification and adds turn-level commitment, allowing a call to reach the environment only after the teacher has verified the entire turn. Treating verified chunks as atomic generation units, we introduce persistent lookahead, which fills idle rollout capacity by advancing future samples and carrying unfinished ones across student updates under the fixed verifier. Across Search-R1-style retrieval and DeepEyes-style perception RL, applying PTA before downstream RL improves macro best@4 by 2.5 and 2.8 points over OPKD under the same downstream RL budget, while lookahead improves throughput by 24%.

---


### 81. [Diffusion Language Models for Mobile Edge Agentic AI: Foundations, Applications, and Challenges](https://arxiv.org/abs/2609.04778)

**<font color=#1a73e8>作者：</font>** Chenqi Li, Minghui Min, Dusit Niyato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) offer a non-autoregressive alternative for mobile edge agentic artificial intelligence (AI) by refining tokens through iterative denoising rather than left-to-right decoding. Compared with autoregressive Transformer-based large language models (LLMs), DLMs can update multiple uncertain tokens in parallel and exploit bidirectional context throughout the generation process, enabling more flexible quality-latency trade-offs beyond fixed sequential decoding. These properties are particularly attractive for edge agents, where partial refinement, early exit, and constraint-guided correction can reduce response delay and communication overhead while improving robustness under noisy, incomplete, or dynamic contexts. This survey reviews DLM foundations and analyzes their suitability for edge settings under latency, memory, energy, bandwidth, privacy, and reliability constraints. We cover resource-efficient architectures, training and inference acceleration, compression, edge/cloud deployment, communication-aware serving, Internet of Things (IoT)/wireless applications, and evaluation of DLM-based agents. We further discuss open issues in long-context state management, split inference, trustworthy execution, multimodal grounding, and reproducible benchmarking. The goal is to connect DLM modeling properties, including bidirectionality, parallel refinement, controllability, and quality-latency elasticity, with system-level requirements of future mobile edge intelligence.

---


### 82. [DODR: Deterministic Operator-Driven Reasoning in Latent Space](https://arxiv.org/abs/2609.04782)

**<font color=#1a73e8>作者：</font>** Weicai Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) large language models formulate reasoning as token-level probabilistic sampling, which induces three fundamental defects in complex logical reasoning: error accumulation, probability substituting necessity, and the linear-chain information bottleneck. This paper proposes the Deterministic Operator-Driven Reasoning in Latent Space architecture (DODR), which reconstructs reasoning as reasoning-graph computation in a high-dimensional linear-algebraic space. Reasoning states are represented as snapshot vectors whose primitives are semantic units (phrases or sentences) rather than tokens, and each inference step is a deterministic matrix operation with no token sampling. Peirce's three inference types are formalized as three trainable matrix operators: a rank-deficient deduction operator (information collapse), a full-rank induction operator (information expansion), and an abduction operator defined as the Moore-Penrose pseudo-inverse of deduction (information hypothesizing). We prove that the operator set is minimal and complete given Peirce's trichotomy, that no single "super-operator" can realize all three types (a rank obstruction), and that reasoning graphs are Turing-complete with contractive backflow converging by Banach's fixed-point theorem. Experiments on 503 sample records (420 deduplicated samples) across dedicated and end-to-end settings show: deduction loss converges to 1.40e-05; induction achieves 0.9996 generalization coverage with 20/20 hard vetoes on counterexamples; abduction solutions exceed the random baseline by 28x with judgment accuracies of 72.5% (58/80, Wilson 95% CI [61.9%, 81.1%]) and 81.7% (49/60, CI [70.1%, 89.4%]); frozen operators attain 100% (60/60) on unseen cross-domain deduction. The architecture provides a structural zero-hallucination guarantee and a three-layer continual-learning mechanism. All data and code are released.

---


### 83. [Can Activation Steering Capture Multidimensional Authorship Style?](https://arxiv.org/abs/2609.04792)

**<font color=#1a73e8>作者：</font>** Hieu Tran, Calvin Bao, Marine Carpuat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering has shown promise for controlling LLM generation along well-defined attributes, but it remains unclear whether it can handle the multidimensional and hard-to-define nature of authorship style. We ask whether structured contrastive prompting along rhetorically-motivated dimensions can construct rich style representations directly in activation space, bypassing the need for natural language style descriptors or dedicated training. We find that the resulting directions share a common authorship backbone while conflicting on aspect-specific residuals that carry genuine stylistic signal, explaining why naive aggregation fails. We operationalize this in Aspect-Aware Activation Steering (A3S), a training-free framework that merges per-aspect contrastive directions with interference-aware aggregation and tunes steering strength per instance. A3S improves authorship style transfer where it is genuinely multi-aspect, outperforms a trained baseline in preference evaluations on out-of-domain benchmarks, and keeps target-exemplar overlap consistently low.

---


### 84. [ProtLingo: Efficient Protein Language Modeling via Conditional Memory and Expert Routing](https://arxiv.org/abs/2609.04793)

**<font color=#1a73e8>作者：</font>** Mingrui Li, Sixian Shen, Minzhang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proteins perform diverse cellular functions, and even single amino-acid substitutions can alter stability, activity, or molecular interactions. Protein language models (PLMs) provide a scalable approach for modeling such sequence--function relationships from unlabeled sequences, but increasing the size of dense Transformer backbones often brings substantial computational cost without consistently improving mutation-sensitive prediction. We introduce ProtLingo, an efficient PLM framework that augments a pretrained single-sequence backbone with conditional local memory and sparse expert routing. ProtLingo maps contextual residue representations into route-specific discrete codes, composes centered local windows into latent $N$-gram addresses, and retrieves reusable residual signals associated with recurring local sequence contexts. In parallel, selected feed-forward blocks are upcycled into sparse Mixture-of-Experts layers with shared and routed experts, enabling residue-dependent computation while activating only a subset of parameters. Experiments on protein fitness prediction, FLIP benchmarks, and supervised contact prediction show that ProtLingo achieves competitive performance with a 150M-scale backbone, including strong parameter efficiency on mutation-effect prediction and preserved long-range structural representations.

---


### 85. [Whose record is this? Diagnosing and authorizing record use in personalized multimodal models](https://arxiv.org/abs/2609.04801)

**<font color=#1a73e8>作者：</font>** Xinyu Mao, Junsi Li, Chenyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contextualized visual personalization can retrieve a true record yet apply it to the wrong visual subject. We formalize when a record may condition an answer as \emph{record authorization}: subject presence ($P$), record-edge validity ($E$), and answer support ($S$) must all hold. We call violations visual memory misbinding (VMM). We construct RecordAuth-Diag, a 3,690-case matched diagnostic suite that changes one image--record edge while holding the query, question, record text, and image multiset fixed. Card removal and nonce relabeling attribute these failures to supplied records. Raw-bank failures span Qwen-, Phi-, and Gemma-family interfaces: Gemma-3-4B-IT reaches 63.69\% local unauthorized use at 25.75\% clean recall. CoViP remains at 26.02\%, versus 22.49\% for its Qwen backbone at similar clean recall. Typed pre-generation authorization reduces Qwen card exposure on RecordAuth-Diag from 43.63\% to 3.06\%, while positive recall changes from 86.26\% to 60.90\%. Full $P\wedge E\wedge S$ validation uses 560 localized DAVIS cases: top-1 relevance and typed authorization have comparable release (28.93\% and 28.39\%) but 6.79\% and 0.89\% unsafe release, respectively. Of the 33 additional unsafe cases removed, 27 are support, 4 edge, 2 clean, and 0 boundary cases. Thus the observed increment is an $E\wedge S$ decision dominated by support, not an edge check alone. Appearance supplies $E$ evidence only conditional on $P$; authenticated subject tokens instantiate the missing presence witness as a sufficiency control. The claims concern the evaluated contracts, not natural prevalence, consent, or visual identity

---


### 86. [Linguistic Trajectory Encoding for Efficient Long-Horizon Spatial Memory in Embodied Agents](https://arxiv.org/abs/2609.04802)

**<font color=#1a73e8>作者：</font>** Tianyidan Xie, Shenyi Wang, Qiang Tang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied agents performing long-horizon tasks require a memory representation in which the state transitions of dynamic objects remain queryable in natural language across hours-to-days observation horizons. Existing systems either drop fine-grained motion (clip-level video-language embeddings), keep it only as raw coordinates (geometric SLAM), or organise it around immediate task context (agent working memories). None of them gives the agent a per-object timeline whose state transitions are themselves queryable in language. Our key contribution is \textbf{Linguistic Trajectory Encoding} (LTE), which compresses dynamic object motion histories via a hybrid representation combining natural language descriptions, sparse spatial anchors, and visual anchors. LTE adapts compression to motion complexity by anchoring periods without reliable observations to the last seen location, while representing motion with geometric waypoints and linguistic descriptions to preserve accuracy. To evaluate these capabilities across extended time horizons, we construct the \textbf{Spatial Memory Benchmark} (SMB) from EgoLife multi-day recordings, targeting capabilities absent in existing benchmarks: semantic trajectory retrieval and long-horizon object retrieval. On SMB, the LTE-based system achieves $45.3\%$ success in semantic trajectory retrieval and $48.7\%$ in long-horizon object retrieval, outperforming structured-memory and VLM baselines (best prior: $31.9\%$ and $34.4\%$). LTE achieves trajectory compression by factors of $8.7\times$ to $26.1\times$ with sub-second query latency on $24$\,h video. On Ego4D natural-language queries, the system reaches $28.75\%$ / $55.10\%$ R@1/R@5, $+15.80$ / $+31.30$ pts over EgoVLPv2.

---


### 87. [When Financial Fine-tuning Fails: A Three-Level Detectability Analysis of Numerical Hallucination in Domain-Adapted Language Models](https://arxiv.org/abs/2609.04806)

**<font color=#1a73e8>作者：</font>** Xiaodong Li, Peiwei Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial large language models are increasingly deployed for summarization of reports and disclosures, where numerical hallucination poses significant practical risks. While prior work often attributes such hallucination to insufficient numerical reasoning, this assumption has not been systematically tested under controlled fine-tuning settings. In this paper, we conduct a cost-effective, controlled study of numerical hallucination in financial summarization across three model variants: a base instruction-tuned model, a domain language-adapted model (FT-A), and a numeracy-enhanced domain model (FT-A+B+C). We introduce a three-level detectability taxonomy distinguishing between overt hallucination (currency-denominated fabrication), covert-explicit hallucination (professional-convention numbers), and covert-implicit hallucination (ungrounded quantitative claims). Our results reveal that domain fine-tuning substantially degrades numerical restraint at all detectability levels. While the Base model maintains near-zero hallucination rates (5.4\%), FT-A exhibits 82.5\% overt hallucination and FT-A+B+C reaches 98\%. Contrary to intuition, numeracy supervision amplifies rather than mitigates hallucination across all levels. We identify template injection---the insertion of memorized canonical values regardless of input content---as a primary hallucination mechanism in fine-tuned models. These findings demonstrate that numerical hallucination in financial summarization is driven by the degradation of numerical restraint through domain adaptation, not by insufficient numerical reasoning. We recommend that evaluation protocols assess hallucination across all detectability levels and that deployment practices include explicit mechanisms for grounding-aware generation or abstention.

---


### 88. [Recurrence Is Not Enough: Causally Validating Multilingual SAE Translation Features in Gemma 2 and 3](https://arxiv.org/abs/2609.04808)

**<font color=#1a73e8>作者：</font>** Giang Son Nguyen, Nhi Ngoc-Yen Nguyen, Wray Buntine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoder (SAE) features are increasingly used to explain and steer language-model behavior, but it remains unclear whether a feature found in one language context plays the same causal role when processing prompts in another language. We study this question using translation-initiation features (Wu et al., 2026). We reproduce the SAE feature discovery method from Wu et al. in Gemma 2 and extend it to multilingual settings that vary prompt language, source language, and target language. We then test whether features that recur across settings affect translation behavior by amplifying or ablating their activations during inference. We also examine whether the method can be applied to Gemma 3.
In both models, we observe an identical finding: although we can find more than 20 features that activate frequently across all discovery settings, causal validation shows that nearly all have small or inconsistent effects. In contrast, one feature -- Gemma 2's (L10, 5717) and Gemma 3's (L20, 2456) -- consistently improves COMET scores when amplified and degrades them when ablated across 23 language settings. These results show that feature recurrence can overstate cross-lingual transfer, while identifying a language-agnostic translation-initiation direction in Gemma 2 and Gemma 3.

---


### 89. [A Systematic Comparison of Multilingual Interpretability Methods Reveals Anisotropy-Driven Failures](https://arxiv.org/abs/2609.04819)

**<font color=#1a73e8>作者：</font>** Oskar Holmström, Marcel Bollmann, Marco Kuhlmann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual language models develop shared cross-lingual representations, and various interpretability methods claim to quantify this sharing. These methods have been developed largely in isolation, and when they disagree, it is unclear whether the disagreement reflects a property of the model or an artifact of the measurement. We compare four sharing metrics (CKA, ANC, GMM dominance per token, and ILO) across 21 base models from five families (125M-14B parameters) and correlate each with cross-lingual transfer on five downstream tasks. We find that the metrics differ in their quantification of cross-lingual sharing in these models and suggest that the disagreement traces to anisotropy, the tendency of representations to cluster in a narrow cone of the embedding space. Only ILO's correlation with cross-lingual transfer (Spearman's $\rho = 0.90$) survives controls for model size, family, and per-task variation. We therefore recommend ILO as the primary sharing metric, to be reported alongside anisotropy diagnostics.

---


### 90. [Cost-Aware Hierarchical Multi-Agent Ransomware Detection and Family Attribution](https://arxiv.org/abs/2609.04820)

**<font color=#1a73e8>作者：</font>** Mubashar Iqbal, Asifullah Khan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware detection and family attribution require analysis of different modalities because it can use packing, obfuscation, process manipulation and runtime evasion techniques. However, conventional multimodal usually uses all available modalities for every sample resulting in unnecessary computational cost and increased latency. In this paper, we present a Cost Aware Hierarchical Multi-Agent System (HMAS) for adaptive ransomware detection. The proposed architecture organizes specialized agents into hierarchical domain controllers coordinated by a Meta Orchestrator. Static analysis is used as the initial low-cost modality while additional dynamic and memory modality is selectively used when confidence is insufficient or specialist agents exhibit disagreement. A cost model incorporates modality use and processing overhead. It enables the orchestration policy to balance analysis performance against computational cost. A locally deployed large language model provides verification for selected difficult cases without replacing the deterministic pipeline. Experimental evaluation compares adaptive HMAS with static only, static plus dynamic and exhaustive analysis policies across binary ransomware detection and multiclass family attribution. The complete HMAS achieved 96.57% accuracy, 0.96 F1-score and 0.99 ROC-AUC for binary detection. It also achieved 0.90 macro-F1 for family attribution. At the same time, the HMAS reduced average analysis cost by 43.97% relative to exhaustive analysis and substantially reduced average analysis latency except for the case where LLM is used. Routing analysis showed that 56.05% of cases were resolved using static evidence alone. Only 4.33% required the complete evidence pipeline. These findings demonstrate that adaptive HMAS can provide accuracy cost tradeoff for ransomware analysis while retaining support for heterogeneous and incomplete modalities.

---


### 91. [Reinforcement Learning for improving Large Language Models' Catalan text simplification capabilities](https://arxiv.org/abs/2609.04823)

**<font color=#1a73e8>作者：</font>** Arnau Ayguadé Domingo, Stefan Bott, Horacio Saggion  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although automatic text simplification (ATS) is critical for accessibility, its progress has not matched the rapid evolution of broader natural language processing techniques. This paper investigates the application of reinforcement learning (RL) to improve the quality of ATS for low-resource languages using Large Language Models (LLMs). The paper introduces a novel reward function, designed to guide LLMs toward a targeted simplification style with Group Relative Policy Optimization (GRPO), that combines the SARI metric with specific penalty components. The effectiveness of GRPO with this reward function is motivated and demonstrated by post-training IberianLLM-7B-Instruct on the ASSET dataset. After post-training on the English ASSET, the model's ATS performance improves on two curated Catalan benchmarks while also successfully suppressing previously observed negative behaviors. Cross-lingual transfer learning is explored by translating ASSET into Catalan and Spanish and post-training the model on each version, but these fail to show a significant improvement on the out-of-domain benchmark.

---


### 92. [Generating Constructive Feedback on Stories via Reinforcement Learning](https://arxiv.org/abs/2609.04824)

**<font color=#1a73e8>作者：</font>** Maja Stahl, Timon Ziegenbein, Henning Wachsmuth  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Constructive feedback is crucial for creative writers to refine their storytelling abilities. Since receiving feedback from human experts is often costly and time-intensive, large language models (LLMs) offer a scalable and efficient alternative as automatic writing assistants. Despite their potential, research indicates that LLM-generated feedback is often generic, lacks actionability, and fails to identify which writing issue is most critical. To address these limitations, we present a reinforcement learning approach that steers LLMs to generate constructive feedback without the need for ground-truth feedback. We train our model using group relative policy optimization (GRPO) with a novel multi-component reward function aiming at constructiveness: it prioritizes feedback that is uniquely tailored to the story, helps to improve story quality, and addresses the most critical writing issue. In automatic and human evaluation across three story corpora, our approach outperforms state-of-the-art LLMs (including Gemini) and competitive baselines. We find that providing actionable suggestions is the main driver of feedback constructiveness.

---


### 93. [On Epistemic Diversity in Large Language Models](https://arxiv.org/abs/2609.04835)

**<font color=#1a73e8>作者：</font>** Elisabeth Kirsten, Nicole Krämer, Muhammad Bilal Zafar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used not only to retrieve information, but to answer questions, explain, teach, and support inquiry. In such settings, evaluation cannot be exhausted by accuracy or alignment alone. A system may give a correct answer while still narrowing users' access %to knowledge. to alternative valid answers, explanations, or reasoning routes. Drawing on the broader notion of epistemic diversity in philosophy and social epistemology, we formalize it in the context of LLMs as the range of valid answers, explanations, and reasoning routes that an LLM exposes to users. We argue that epistemic diversity is a useful evaluation dimension for settings where LLMs are used to support knowledge-intensive tasks. We propose a preliminary framework for conceptualizing and measuring epistemic diversity in LLMs, and operationalize it in two domains. We find that frontier LLMs often exhibit epistemic narrowness, repeatedly collapsing large valid answer spaces onto small canonical subsets. These findings suggest that LLM evaluation should move beyond accuracy-oriented paradigms and treat epistemic diversity as an important dimension of model capability.

---


### 94. [MABPD: Multi-Agent Bias Probing & Detection via Structured Argument Debate](https://arxiv.org/abs/2609.04841)

**<font color=#1a73e8>作者：</font>** Garvit Joshi, Stavya Dhyani, Jasmine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Media bias in news articles operates through subtle linguistic cues---loaded language, selective framing, and strategic omission---that resist single-model detection and have traditionally required large annotated corpora for supervised training. We ask whether structured multi-agent deliberation can serve as a principled, training-free alternative to supervised classification for this task. We introduce MABPD (Multi-Agent Bias Probing & Detection), a pipeline in which three specialized LLM agents analyze an article from complementary perspectives and resolve disagreements through a Structured Argument Debate (SAD) protocol. SAD implements a domain-motivated asymmetric burden of proof---biased claims without grounded textual evidence carry zero weight---combined with role-weighted voting and post-consensus verification, replacing task-specific supervised decision boundaries with explicit deliberative structure. Ablation confirms that this structured deliberation, not mere agent parallelism, drives performance: removing the debate module reduces F1 by up to 10.6 points. On the BABE benchmark (4,121 expert-annotated sentences), MABPD achieves 83.4% macro F1 on the held-out test split---within 0.7 percentage points (pp) of the supervised SOTA (MAGPIE, 84.1% macro F1; Horych et al., 2024)---without any task-specific training or threshold tuning on annotated data. Cross-dataset evaluation on the SemEval 2019 HyperPartisan corpus (644 articles) yields 75.0% zero-shot accuracy, within 7.2 pp of the supervised SOTA accuracy (82.2%; Kiesel et al. 2019), confirming transfer across annotation regimes. We release the full pipeline and evaluation code.

---


### 95. [MMTClinic: Multimodal, Multilingual Time Series Question Answering and Reasoning Benchmark for Clinical Domain](https://arxiv.org/abs/2609.04842)

**<font color=#1a73e8>作者：</font>** Sourav Malakar, Harshit Nigam, Akash Ghosh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Time-series data in clinical settings is crucial for capturing dynamic changes in a patient's health over time, enabling timely diagnosis, personalized treatment, and early detection of critical events. However, the development of clinically reliable and linguistically inclusive medical AI systems remains a significant challenge, primarily due to the lack of multimodal, multilingual, and time-series-grounded benchmarks that reflect the complexity of real-world clinical scenarios. To fill this gap, we present MMTClinic, a benchmark designed to evaluate large language models (LLMs) on complex reasoning and question-answering tasks involving clinical time-series. MMTClinic combines text, medical images, and multivariate physiological signals and includes 30,000 QA pairs (15,000 multiple choice questions (MCQs) and 15,000 open-ended questions) across five languages: English, Hindi, Bengali, Marathi, and Tamil. These questions cover three important clinical tasks---mortality prediction, heart rate forecasting, and SOFA score estimation. We evaluate 13 state-of-the-art LLMs in zero-shot, few-shot, and chain-of-thought settings. Our evaluation reveals notable differences in model performance across tasks, languages, and modalities, highlighting current limitations in clinical reasoning capabilities. MMTClinic provides a valuable resource for advancing multilingual, multimodal, and time-series-aware medical AI research. The dataset will be made publicly available on successful acceptance of the work.

---


### 96. [ElderBench: Benchmarking Autonomous Mobile Agents for Older Adults](https://arxiv.org/abs/2609.04850)

**<font color=#1a73e8>作者：</font>** Weide Zhan, Qumu Shaqu, Yuanqing Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While autonomous mobile agents hold great potential for assisting older adults with smartphone usage, existing GUI benchmarks mainly rely on explicit, goal-oriented instructions and rarely capture the naturally occurring language patterns of older users, such as indirect speech, referential ambiguity, and under-specified requests. This mismatch between benchmark instructions and real-world elderly interactions may hinder reliable agent deployment. To address this gap, we present ElderBench, the first benchmark for evaluating mobile GUI agents in authentic elderly-oriented scenarios. ElderBench is constructed from 249 naturally elicited smartphone tasks collected from older adults across 20 applications. We first characterize the linguistic divergence between elderly instructions and existing GUI benchmark instructions from syntactic, semantic, and pragmatic perspectives. We then evaluate mainstream GUI agents and Vision-Language Models under both online and offline settings, revealing substantial performance degradation when handling elderly-oriented instructions. Through controlled instruction normalization, failure analysis, and fine-grained linguistic feature analysis, we further identify how elderly-specific language patterns contribute to agent failures. Our findings provide actionable design insights toward more adaptive, interpretable, and age-inclusive GUI agents for older adults.

---


### 97. [KVMem: Virtualizing Million-Token Agent Workspaces on a Consumer GPU](https://arxiv.org/abs/2609.04852)

**<font color=#1a73e8>作者：</font>** Di Chai, Leye Wang, Zeshen Su 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLM agents operate in persistent workspaces whose accumulated history can exceed both GPU KV capacity and the model's native context window. Existing systems typically compact older context into summaries or retrieve it later as text, either losing fine-grained execution evidence or repeatedly prefilling content that the model has already processed. We present KVMem, a KV-context virtualization system that preserves overflowed workspace history as paged KV state across GPU memory, host memory, and NVMe. KVMem uses lightweight, model-native attention-space indexes to select relevant historical blocks and materializes a query-dependent execution view bounded by the model's native context window. Extensive evaluations on long-context agent benchmarks spanning histories up to one million tokens, including LongMemEval, MemoryAgentBench, and AgentLongBench, show that KVMem generally achieves higher task utility and greater inference efficiency than compaction-based approaches, the de facto standard for handling context overflow. In the DeepSWE long-context test with Qwen3.8-27B, KVMem improves task success from 43.8% with compaction-only context management to 48.4%.
In our local-deployment evaluation, KVMem runs Qwen3.6/3.8-27B NVFP4 with MTP on an off-the-shelf laptop equipped with a 24\,GB RTX 5090 Laptop GPU, virtualizing agent workspaces of up to 1M tokens-four times the model's native 256K-token context window. In a single-session setting, KVMem generates $\sim$50 tokens/s, providing interactive responsiveness for local agent execution. More broadly, by decoupling addressable workspace size from the LLM's native context window, KVMem provides a practical path toward long-running agents whose workspaces can grow beyond that window.

---


### 98. [CC-Mediation: Evaluating Large Language Models for Cross-Cultural Conflict Mediation](https://arxiv.org/abs/2609.04855)

**<font color=#1a73e8>作者：</font>** Suhyun Lee, Wenxuan Zhang, W. Quin Yow 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-cultural mediation by large language models (LLMs) requires deciding both when to intervene and how to respond in culturally grounded conflicts. Progress on this problem has been limited by the lack of (1) mediation datasets with measurable downstream effects and (2) principled metrics for evaluating intercultural stance change. To address these gaps, we introduce CC-Mediation, a cross-cultural mediation benchmark of $1{,}661$ ten-turn dialogues grounded in the Developmental Model of Intercultural Sensitivity (DMIS), containing culturally grounded conflicts, mediation interventions, and post-intervention trajectories. We further propose two DMIS-based evaluation metrics: Trajectory AUC, which measures the persistence of intercultural improvement over time, and a signed Wasserstein-1 distance, which measures the magnitude and direction of shifts in intercultural stance. Both metrics show strong agreement with human judgment of DMIS-grounded stance shift. Using CC-Mediation, we find that current LLMs have limitations on both axes: intervention timing (when) failure stems from a positional prior that ignores dialogue content, while mediation strategy (how) failure arises from a late-layer elicitation collapse rather than a knowledge deficit.

---


### 99. [MM-IFEval-Pro: A Multilingual and Attack-Resistant Benchmark for Instruction-Following in Vision-Language Models](https://arxiv.org/abs/2609.04859)

**<font color=#1a73e8>作者：</font>** Changming Xiao, Zhenliang Ni, Jinhui He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As vision-language models (VLMs) rapidly advance in image understanding, cross-modal reasoning, and complex instruction execution, instruction-following capability has become a key indicator of their reliability and practicality. However, existing multimodal instruction-following benchmarks still suffer from limited language coverage and insufficient adversarial safety scenarios, making them inadequate for evaluating real-world multilingual and safety-sensitive settings. To address these gaps, we present MM-IFEval-Pro, a multimodal instruction-following benchmark covering Chinese and English tasks as well as diverse instruction hijacking cases. MM-IFEval-Pro includes 4 major task categories and 24 subcategories and 8 instruction categories with 52 subcategories, with each sample containing an average of 3.0 constraints to realistically simulate complex instruction scenarios. We further construct a reinforcement-learning training set enriched with Chinese and adversarial instructions, which significantly improves model performance on MM-IFEval-Pro and transfers effectively to other mainstream multimodal benchmarks, demonstrating strong cross-task and cross-language generalization.

---


### 100. [CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution](https://arxiv.org/abs/2609.04865)

**<font color=#1a73e8>作者：</font>** Jinyuan Feng, Dongmin Li, Yiqun Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill libraries improve the sample efficiency of agentic reinforcement learning (RL) by enabling large language model (LLM) agents to reuse procedural knowledge. Yet existing paradigms exhibit structural shortcomings: they either decouple skill evolution from policy optimization or instantiate meta-skills as fixed workflows. Both treat skills as passive objects to be managed, limiting the flexible evolution of skills and their co-adaptation with the reasoning agent. To address the limitations, we propose CoSkill, a unified multi-agent RL framework that recasts the static meta-skill workflow as a learnable Meta-Skill Agent and jointly trains it with a Reasoning Agent over a hierarchical skill library. By modeling the Reasoning and Meta-Skill Agents as a cooperative team sharing a single backbone, CoSkill enables end-to-end co-adaptation: the Reasoning Agent conditions its actions on a retrieved task skill and step skills selected from its child set, while its task performance guides the Meta-Skill Agent in refining those step skills. Experiments on ALFWorld and WebShop show that CoSkill substantially outperforms prior skill-based and RL baselines, achieving success rates of 98.4% and 90.6%, respectively (+3.5 and +6.2 pp). As shown in Figure 1, CoSkill achieves superior early-stage sample efficiency, asymptotic performance, and wall-clock efficiency. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-179](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
