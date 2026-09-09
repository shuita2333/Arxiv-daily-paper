# 🧠 大模型相关研究 | 2026年09月10日

> 本类共 **483** 篇论文：已确认 **447** 篇，待复核 **36** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

---

### 51. [More Than Mimicking Reviewers: Evaluating LLMs for Pre-Submission Peer Review](https://arxiv.org/abs/2609.05788)

**<font color=#1a73e8>作者：</font>** Pouya Parsa, Amin Rezaei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Peer-review feedback often arrives too late for authors to make meaningful revisions. We study an author-facing LLM system that moves part of this stress test before submission: it generates a broad pool of atomic concerns and compresses them into a short report. We evaluate agreement with historical reviews and, separately, the possible validity of concerns they omit.
From 10,000 ICLR 2026 submissions, we use 3,398 manuscripts with accessible versions that predate review. On a ten-paper diagnostic, independent sampling covers 44.9% of historical issues; deduplication and refill reaches 78.7% strict and 84.9% seriousness-weighted coverage, at 3.6$\times$ more requests and 5.2$\times$ more tokens. A hidden Top-32 Oracle preserves the full 79.3% weighted coverage of a 256-candidate pool, but paper-only selectors retain only 40--44%. LLM review therefore provides broad coverage with a large candidate pool but compresses poorly; ablations identify representative selection and matcher sensitivity as the main sources of this gap.

---


### 52. [Recall Is Not Protection: Evaluating Safety Monitors Against Model Compliance](https://arxiv.org/abs/2609.05797)

**<font color=#1a73e8>作者：</font>** Sripad Karne  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety monitors screen prompts sent to deployed language models, flagging harmful requests so they are never answered. They are evaluated by recall against harmfulness labels, but a catch only prevents harm if the model would otherwise have complied. We measure the difference directly: we sample repeated responses from the target model, call a harmful prompt \emph{elicitable} if the model complies at least once, and report monitor recall separately on elicitable and non-elicitable prompts. Across six monitor configurations and three model families, spanning activation probes, fine-tuned text guards, and a 120B policy-conditioned reasoning classifier, recall on elicitable prompts falls 0.22 to 0.38 below recall on non-elicitable prompts at a fixed false positive rate. The prompts a monitor misses are 2.8 to 5.6 times more likely to be complied with than the prompts it catches. The gap replicates across three model families and appears also in text-only monitors entirely independent of the target model. This suggests that standard recall may overstate the protection monitors provide in practice, and that monitors should be evaluated against what their models will actually answer.

---


### 53. [Dynamic Lagging for Simultaneous Translation](https://arxiv.org/abs/2609.05799)

**<font color=#1a73e8>作者：</font>** Hieu Hoang, Amittai Axelrod  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In cascaded simultaneous speech translation, the machine translation (MT) system cannot control the read--write schedule of the upstream recognizer: it must decide, from a growing source prefix, how much target text to commit. We make a sentence-trained, decoder-only LLM prefix-aware by fine-tuning it on stable prefixes---the longest prefix that any translation up to the current partial source has shared with the model's own full-source output---mixed with full-sentence pairs, and prompt it through a single force-decode turn that carries the committed target forward as more source arrives, making the system flicker-free by construction. We fine-tune Qwen3-8B for EN to DE, JA, ZH, simulating the source stream with reference-transcript prefixes. Prefix finetuning preserves full-sentence quality while improving worst-position chunk quality, and it improves calibration of token-level commit confidence, reducing expected calibration error (ECE) on early source prefixes against a stable-prefix oracle. A single training-free threshold on that confidence is the most effective of the three latency controls we compare: it traces a continuous quality--latency frontier that outperforms the discrete wait-$k$ and target-suffix-deletion quality-latency tradeoff mechanisms. The effect holds well on FLEURS, WMT24++, and CoVoST~2 test sets, under both COMET and MetricX.

---


### 54. [Spillover-Aware Multi-Value Steering for Pluralistic LLM Alignment](https://arxiv.org/abs/2609.05800)

**<font color=#1a73e8>作者：</font>** Weici Pan, Xander Barron, Jiawei Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering controls LLM behavior at inference time by adding learned directions to hidden states, but existing methods handle one concept at a time. Pluralistic alignment, where different stakeholders need different value emphases, requires steering multiple dimensions simultaneously. We show that naive steering produces substantial spillover: the effect intended for one value leaks into others. This parallels the treatment-versus-spillover decomposition in causal inference. We trace spillover to geometric entanglement of steering directions, captured by their Gram matrix, and derive a zero-cost correction from an activation-norm-penalized objective that decouples each direction's contribution exactly. Our end-to-end pipeline requires no fine-tuning, no reward model, and no manual prompt engineering: given only domain questions, it automatically discovers value dimensions, extracts directions, diagnoses entanglement, and applies corrected steering. On climate discourse, the correction improves the net steering effect from +5.9% to +14.0%, validated over 100,000 pairwise judgments.

---


### 55. [AtomCite: Verification and Correction of Supplied Page-Level Citations in Multi-Page Documents](https://arxiv.org/abs/2609.05802)

**<font color=#1a73e8>作者：</font>** Chen Qian, Yimeng Wang, Yu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models answering questions over multi-page documents are expected to cite the supporting pages, yet supplied citations are sometimes inaccurate, and current evaluations score citations at generation time or against text passages: no existing benchmark evaluates whether a system can verify and correct a page-level citation already attached to an answer. We propose AtomCite, an agentic framework that parses an answer into claims, checks each claim against the image of its cited page, and applies a deterministic repair policy. To evaluate it, we introduce DocCite, to our knowledge the first benchmark for systems that verify and correct page-level citations in document images. Built on MP-DocVQA and DUDE, it combines 928 validated injected instances with 2,468 candidate natural errors harvested from frontier- and efficiency-tier models, of which a two-annotator audit confirms 1,909 as genuine errors. Primary labels are assigned deterministically, not by LLM judges, with the human audit as a separate validation layer. Across three model families (Gemini, Claude, and GPT), AtomCite reaches around 93% binary verification accuracy on the injected benchmark, significantly outperforming every OCR-only condition, including a compute-matched control, and exceeding every prior text-based baseline given the same OCR text. Its repair policy lifts citation precision on the injected mix from a constructed 34% to 87-90% while retaining over 90% of correct claims. AtomCite also transfers: with frozen prompts and zero training, it raises the hallucination-detection scores of two open 7-8B models on five public benchmarks above the same models prompted as direct judges. Finally, the audit shows that noise in automatic labels biases measured verifier accuracy and can reverse system rankings, so evaluations relying only on synthetic or automatic labels risk mismeasuring verification capability.

---


### 56. [Exposing Weaknesses in Emotion Recognition in Conversations](https://arxiv.org/abs/2609.05806)

**<font color=#1a73e8>作者：</font>** Amir Ben Khalifa, Fanny Bezancon, Amine Trabelsi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotion Recognition in Conversations (ERC) aims to identify speakers' emotions in multi-turn dialogue. Accurate emotion recognition can support a wide range of applications, including empathetic conversational agents, mental health support, and educational technologies. While many recent approaches rely on task-specific fine-tuning, such models may exploit dataset-specific cues. A central yet rarely questioned assumption in ERC is that each utterance can be assigned a single unambiguous emotion label. To investigate this assumption, we study ERC using Large Language Models (LLMs) in a zero-shot setting while incorporating preceding conversational turns as context. We show that aggregate metrics mask systematic failures. Errors concentrate around utterances containing negations, exclamations, and interjections. This pattern is consistent across all evaluated models, suggesting limitations in the benchmarks rather than model-specific weaknesses. A controlled re-annotation study involving four human annotators supports this finding: strong agreement is observed in only 35 percent of cases, with neutral utterances dominating high-agreement instances, while many emotional categories fall into low-agreement regimes. These findings suggest that many apparent model errors reflect genuine annotation ambiguity rather than poor emotion understanding. Standard single-label evaluation is therefore insufficient. To address this limitation, we introduce an LLM-as-Judge framework that evaluates each emotion independently according to its plausibility in the conversational context rather than enforcing a single-label decision.

---


### 57. [Agentic BAIM-LLM Evaluation (ABLE): Benchmarking LLM Use of Protein Design Tools](https://arxiv.org/abs/2609.05818)

**<font color=#1a73e8>作者：</font>** Bryce Cai, Geetha Jeyapragasan, Samira Nedungadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce ABLE, a benchmark for evaluating LLM agents' ability to use biological AI models (BAIMs), such as ProteinMPNN and AlphaFold3, in dual-use protein design workflows. ABLE assesses agent performance through a set of tasks spanning structure retrieval, sequence generation, and design validation. We evaluate 15 frontier models and find that seven refuse all tasks, while the remaining models exhibit substantial performance differences. Claude Sonnet 4 and Gemini 3 Pro achieve the highest scores across information retrieval, tool selection, and tool use. We further compare model performance on a subset of tasks against an expert human baseline. Our results suggest that current LLMs can substantially lower barriers to protein design, but remain inconsistent in planning, strategy generation, and integrating biological knowledge with tool use.

---


### 58. [Online Learning with LLM Experts from Limited Feedback](https://arxiv.org/abs/2609.05820)

**<font color=#1a73e8>作者：</font>** Wang Wei, Soumyabrata Pal, Koyel Mukherjee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adaptive routing of prompts to large language model (LLM) experts to maximize response quality in an online setting with limited feedback. We formulate it as a bandit problem with $K$ actions that represent experts and $d$ features that encode prompts, over a horizon of $T$ rounds. We propose algorithms that strategically select and observe rewards to minimize regret. In the full-information setting, we achieve a regret of $\tilde{O}(d T / \sqrt{m})$, while in the bandit setting we achieve $\tilde{O}(d T \sqrt{K / m})$, where $m \ll T$ is a budget on feedback. Our experiments show that we efficiently learn high-quality routing strategies across diverse LLMs from limited feedback.

---


### 59. [CONDUIT: A Unified Residual-Stream Restoration Framework for KV Cache Reuse in Vision-Language Models](https://arxiv.org/abs/2609.05821)

**<font color=#1a73e8>作者：</font>** Pengan Chen, Kaisheng Zheng, Liang Hong 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) often answer new questions about recurring visual content, where reusing the key-value (KV) cache can avoid re-encoding expensive visual prefixes. Exact-prefix reuse, however, fails when the same visual content appears under a changed prefix. Selective recomputation can recover quality under a small visual-token budget, but only when the right stale tokens are refreshed. Raw-attention selection can waste budget on high-attention tokens with small value-norm proxy scores and on query-irrelevant images. To address these failure modes, we propose CONDUIT, a training-free refresh policy that unifies single- and multi-image reuse as residual-stream restoration. Building on norm-weighted attention, CONDUIT ranks cached visual tokens using cached-key query attention and an accessible pre-output cached-value-norm proxy, then applies empirical image-level relevance amplification before one global selection. With one image, the coefficient is one and the rule reduces to intra-image token selection. The method preserves model architecture and weights, adding only a single query-conditioned scoring pass at inference. At a 10% refresh budget, CONDUIT achieves 97.0-99.5% of the corresponding full-prefill five-dataset average across three VLM backbones and leads budgeted methods on average; on the MMLongBench-Doc latency subset, it uses 13.5% of full-prefill FLOPs and achieves a 2.99x time-to-first-token speedup.

---


### 60. [Beyond Top-$k$ Skill Retrieval: Diversity-Aware Skill Routing for LLM Agents](https://arxiv.org/abs/2609.05824)

**<font color=#1a73e8>作者：</font>** Wang Wei, Tiankai Yang, Samyadeep Basu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on external skills, but routing user requests over large skill registries is difficult because many skills are functionally redundant while complex tasks often require complementary skill sets. Existing skill routers typically rank candidates independently by query relevance, which can waste context budget on redundant skills. We propose Diverse Skill Routing (DSR), a diversity-aware reranking framework that uses a Determinantal Point Process to balance relevance and non-redundancy. DSR introduces a query-residual diversity kernel that penalizes redundant skill overlap while reducing penalties caused only by shared query relevance. On the SkillRouter benchmark, DSR improves recall and full coverage over a strong pointwise reranking baseline, with larger gains on multi-skill queries. These results suggest that skill routing should be treated not only as relevance ranking, but also as complementary set selection.

---


### 61. [AgentBrew: Offline Tool-Use Agent Learning from Raw Real-World Trajectories](https://arxiv.org/abs/2609.05837)

**<font color=#1a73e8>作者：</font>** Zhiyi Lyu, Yewen Li, Longtao Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly deployed in real-world applications through tool-use APIs, yet training them for specific environments remains fundamentally difficult: real-world applications provide no pre-defined tasks or verifiers, no faithful simulators, and limited budget for large-scale environment interaction. In this paper, we propose \textbf{AgentBrew}, an offline training framework that learns effective tool-use policies from a single batch of raw interaction trajectories, without task verifiers or iterative on-policy rollouts. The agent first explores the target environment to collect a raw trajectory corpus without quality filtering. To extract training signal from this noisy corpus, \emph{retrospective task inference} reconstructs an aligned instruction for each trajectory based on its actual outcome, and \emph{PMI-Based credit assignment} decomposes the trajectory's total information about the inferred instruction into additive per-action credits via pointwise mutual information (PMI). These credits weight the policy training objective, amplifying informative actions while suppressing ineffective ones. On three real-world MCP applications (GitHub, Notion, PostgreSQL), AgentBrew improves Qwen3-32B by +8.7 Acc / +9.7 Score on average, surpassing Qwen3-235B (+2.3 / +4.4) and outperforming rejection sampling (+5.9 / +10.3). These results demonstrate that fine-grained offline learning can recover useful supervision from raw trajectories that filtering-based approaches would discard. The code is available at this https URL

---


### 62. [SinoGlyphBench: A Diagnostic Benchmark for Chinese Glyph-Level Obfuscation in Language-Model Moderation](https://arxiv.org/abs/2609.05843)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Zimu Wang, Suliu Qin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Glyph-level obfuscation can leave harmful Chinese content readable to humans while degrading automated moderation. We introduce SinoGlyphBench, a diagnostic benchmark that identifies label-critical semantic anchors and creates matched original and glyph-obfuscated inputs in text and image modalities. By perturbing anchors, background context, or both, this design distinguishes corruption of moderation-relevant evidence from general surface variation. Across 176,916 paired evaluations of 12 LLMs and MLLMs, obfuscation increases harmful false-negative and false-positive rates by 6.1 and 4.7 percentage points, respectively, and reduces four-way accuracy by 5.0 points. Models retain 75.7% of the decisions that were correct on the matched original inputs. Full-scope perturbations cause the largest degradation, anchor-only perturbations are more damaging than background-only perturbations, and cross-script substitution is particularly difficult in the text modality. Analysis of structured outputs identifies observable mismatches in visible-form reading, intended-message recovery, and final safety judgment. The evaluated models, therefore, remain brittle to Chinese content written with non-canonical glyphs. Resources are available at this https URL.

---


### 63. [Grounded and Faithful P&ID Reasoning: Constraining Vision-Language Models with Recovered Evidence Graphs](https://arxiv.org/abs/2609.05880)

**<font color=#1a73e8>作者：</font>** Prathamesh Gadekar, Sagar Srinivas Sakhinana, Venkataramana Runkana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Piping and Instrumentation Diagrams (P&IDs) are the authoritative maps of process plants: isolation, maintenance, and HAZOP decisions depend on what connects to what. Vision-language models describe these sheets fluently, yet they often invent or miss process connections---and an invented or missed link can reverse an isolation or reachability call, so a plant decision cannot trust a fluent answer that was never checked against the linework. We instead recover an explicit graph of the drawing---its symbols, the process connections between them, and the tags that name them---and then require the model to answer only by querying that graph through seven read-only operators, so a topology claim is returned only when it cites the query results that support it. On TopoPID-VQA, a new suite of 3000 topology questions over these sheets, Graph-Grounded Harness (Ours) raises exact match accuracy from 36.7--41.3% under image-only prompting to 74.3--76.0% for Qwen3-VL-4B, Qwen3-VL-8B, and Gemma-4-E4B. It does so on an imperfect substrate: on Digitize-PID dataset the recovered graph scores F1 0.742 on exact process connections, and 0.801 once symbols and tags are pooled in. The residual errors track that gap---grounding pays off where the recovered graph is right, and perception error still breaks topology questions where it is not.

---


### 64. [What if LLMs Ate Their Words: Causal History Effects in Multi-Turn Interaction](https://arxiv.org/abs/2609.05882)

**<font color=#1a73e8>作者：</font>** Jinnan Li, Zheren Fu, Yue Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn interaction creates a feedback process in which an LLM's previous responses become context for later behavior. Prior work shows substantial multi-turn degradation and that assistant-generated history can affect later behavior. However, it remains unclear how these effects manifest across models, tasks, turns, and inside a model. We study these gaps across six task families and five models. Degradation from fully specified single-turn input (FULL) to progressively revealed multi-turn interaction (SHARDED) is clearly task- and model-dependent, and stronger one-shot performance does not imply greater interaction robustness. We then retrospectively analyze completed SHARDED conversations by replaying the user messages already observed in each trajectory while editing only assistant-generated history. Replacing prior assistant responses with neutral content (termed neutralization) changes downstream min-max normalized performance by +.027 across 2,973 trajectories. On a prespecified length-controlled subset, short and length-matched neutralization yield nearly identical effects (+.069 versus +.068), showing that simple context shortening is insufficient to explain the effect of history editing. Turn Surgery further intervenes on one assistant turn at a time. Among 237 selected degraded trajectories, 63.7% contain at least one beneficial intervention, while most tested positions remain unchanged; for binary tasks, 48.4% admit a fail-to-success reversal. An open-weight case study links behaviorally consequential history changes to measurable downstream state differences, but finds task-dependent rather than universal internal signatures. Overall, assistant-generated history has active but selective effects on multi-turn performance, motivating selective rather than uniform history management.

---


### 65. [One Rate Is Not Enough: Adaptive Anisotropic Learning Rates for LoRA Fine-Tuning](https://arxiv.org/abs/2609.05885)

**<font color=#1a73e8>作者：</font>** Huiyi Wang, Daijiao Liu, Lina Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) has become the standard for parameter-efficient fine-tuning of large language models. Most LoRA variants follow a uniform-LR convention, applying a single global learning rate across every rank-one component of every adapter. We show that this convention overlooks substantial within-module heterogeneity, where the rank-one components of a LoRA adapter update at highly uneven rates and low-velocity modules converge to concentrated singular spectra that underutilize the nominal rank budget. To address this, we propose an adaptive anisotropic learning-rate model that assigns each rank-one component its own effective learning rate, computed online from training-time signals and mean-normalized per module to preserve the global LR budget. AnLR-LoRA instantiates this model with two signals available during AdamW optimization, namely function-space velocity and Adam SNR, as a lightweight scheme with no extra trainable parameters. Across commonsense reasoning, natural language generation and visual instruction-tuning benchmarks, AnLR-LoRA consistently improves over LoRA while encouraging broader use of rank capacity, with gains that remain robust across a wide range of global learning rates and transfer cleanly to other LoRA variants.

---


### 66. [Multimodal Resource-Exhaustion Attacks on Vision-Language Models via Joint Pixel-Prompt Optimization](https://arxiv.org/abs/2609.05889)

**<font color=#1a73e8>作者：</font>** Zhaoxiong Ni, Yatie Xiao, Chi-Man Pun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Resource-exhaustion attacks against autoregressive vision-language models (VLMs) typically assume unimodal threat models, treating the image branch as the primary optimization surface while holding user-visible prompts fixed. Even recent loop-centric variants remain confined to this single-channel paradigm, leaving the exploitation of availability unexplored as a cross-modal optimization problem over jointly controllable input surfaces.
We introduce Joint Pixel-Prompt Optimization (JPPO), the first compound adversarial framework elevating the visible prompt to a first-class adversarial variable alongside image perturbations. Under a restricted joint-input threat model, JPPO performs coupled, stagewise optimization over both the pixel and prompt surfaces. This produces synergistic cost amplification, mechanistically distinct from loop-dependent failures, exhibiting negligible loop incidence in our experiments.
Evaluating five open-source VLM families on MS COCO and ImageNet under an 8/255 infinity-norm budget, JPPO achieves over 4.6x latency and 5.3x energy amplification on Qwen2.5-VL-7B, and over 36.6x latency with 32.7x energy amplification on BLIP-2. This represents the strongest cost amplification among directly compared baselines while requiring substantially fewer optimization iterations. Ablations confirm this amplification arises from multimodal coordination rather than prompt length or isolated modalities. These findings reveal structural blind spots in current VLM serving defenses, motivating cost-aware robustness evaluation as a first-class security requirement for multimodal deployments.

---


### 67. [The End of AI Exponentiation: Fluttering Inside and Outside AI Bubble](https://arxiv.org/abs/2609.05894)

**<font color=#1a73e8>作者：</font>** Victor Kebande  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The exponentiation of Artificial intelligence (AI) in the recent past has entered a transformative era that has been driven by the growth in large language models (LLMs), large-scale compute infrastructures, and autonomous reasoning systems. However, the rapid acceleration of AI has increasingly shown technological, societal, economic, ethical and infrastructural challenges associated with peak data limitations, rising computational demands, synthetic data recursion, valuation inflation, and societal instability. The traditional scaling paradigms that have powered the modern AI systems are gradually encountering friction in sustaining continuous exponential growth. This paper views ``the end of AI exponentiation,'' thus exploring how it flutters inside and outside the bubble, where instability emerges within the AI ecosystem through compute and data-center races, speculative investments, and the rat-race toward superintelligence, and outside the ecosystem through labor disruption, governance concerns, public uncertainty, and geopolitical acceleration surrounding future intelligent systems and infrastructures globally.

---


### 68. [AlignDiff: Exploiting Model-Intrinsic Information for Better Preference Data Selection](https://arxiv.org/abs/2609.05899)

**<font color=#1a73e8>作者：</font>** Peng Lai, He Zhu, Zhiwen Ruan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning large language models with human preferences remains a challenge, primarily due to the critical role of preference data quality in effective alignment. Existing datasets are frequently plagued by inherent noise and distribution shifts, which inherently limit model performance. To bridge this gap, we propose AlignDiff, a preference data filtering framework driven by intrinsic model signals. AlignDiff first identifies samples with clear preferences using both positive and inverse signals, then prioritizes the more challenging samples based on the average negative log-likelihood gap, encouraging the model to learn richer information from them. AlignDiff is evaluated on two widely used model families (LLaMA and Qwen) and three benchmarks widely adopted in the alignment community (AlpacaEval 2.0, Arena-Hard, and MT-Bench). Across all settings, it consistently outperforms seven strong baselines. We conduct comprehensive ablation studies to validate the effectiveness of AlignDiff, and further show that difficulty-based curriculum learning improves model performance.

---


### 69. [From Review to Authorization: Key-Isolated Threshold Signing for LLM Agents](https://arxiv.org/abs/2609.05901)

**<font color=#1a73e8>作者：</font>** Yu Zheng, Qizhi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents can turn untrusted content into effectful actions such as payments and permission changes. If the same process interprets this content and controls a reusable signing credential, prompt injection can cross the judgment boundary and reach execution authority. We present KITA, a review-to-authorization architecture that keeps the user's personal secret signing key and every threshold signing-key share outside all LLM processes. Under threshold signature unforgeability and our system assumptions, compromising the proposer and fewer than t reviewer-signer domains cannot produce a valid authorization for a new action without signing contributions from t distinct domains. Thus, any such authorization includes a share from an uncompromised domain, bound to the canonical action and released only after authenticated reviewer approval. This establishes execution-bound authorization integrity. We implement the complete reviewer-to-executor path with a structured-output LLM adapter and threshold BLS. Six system tests validate quorum gating and message binding at this interface, while cryptographic microbenchmarks measure the online signing path and its scaling behavior.

---


### 70. [GenPuzzle: Benchmarking Visual Reasoning in Image Generation Models](https://arxiv.org/abs/2609.05902)

**<font color=#1a73e8>作者：</font>** Changpeng Zhao, Yiren Song, Jinpeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image generation systems increasingly combine multimodal understanding, reasoning, and synthesis, suggesting that they may do more than render plausible scenes. Yet existing evaluations emphasize aesthetics, prompt alignment, compositionality, or text-based answers, leaving unclear whether these systems can solve visual problems and faithfully express solutions in pixels. We introduce GenPuzzle, a benchmark for reasoning-centric image generation. GenPuzzle contains 2,005 problems across 12 tracks, spanning pattern completion, spatial construction, mazes, Sudoku, nonograms, tangrams, board games, matchstick puzzles, orthographic projection, and mathematical visual proof. Each task provides a visual puzzle and requires an image output that preserves the input state while executing a logically valid solution. GenPuzzle uses task-specific evaluation protocols: discrete grid outputs are transcribed and verified programmatically, while visually complex outputs are assessed with tiered, multidimensional, or binary multimodal large language model (MLLM) rubrics. We further select the automatic judge by measuring agreement with human reference scores. Across three frontier generators, the strongest model reaches only 40.57 Macro Overall, revealing frequent failures in logic, geometry, state preservation, and instruction execution. GenPuzzle provides a testbed for measuring progress from image rendering toward visual problem solving.

---


### 71. [EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing Agents](https://arxiv.org/abs/2609.05903)

**<font color=#1a73e8>作者：</font>** Nanxi Li, Yingzi Ma, Yulong Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are turning language into real-world effects, making safety necessary against both indirect prompt injections and direct harmful requests. System-level safety harnesses add an enforcement layer beyond model-level defenses, but existing harnesses are usually designed once by experts and applied across heterogeneous models and domains. Effective protection is deployment-dependent: models differ in how much enforcement they need before utility declines, while domains differ in the effects, state, and action sequences that must be governed. A harness that is strict enough for one model may over-block another, and a policy that transfers across domains may miss application-specific safety relations.
We present EvoSafeHarness, a safety-specific optimization framework that synthesizes a deployable harness for a frozen model in a target domain. It jointly searches a natural-language policy and executable code logic, guided by model behavior, domain specifications, and fresh-context adversarial review to reject benchmark-specific rules. Across four agent benchmark families, EvoSafeHarness achieves a stronger safety-utility frontier than fixed expert-designed defenses. On DecodingTrust-Agent, it reduces average attack success rate from 45.6% to 10.0% at a 3.3-point utility cost and achieves the best score in 14 of 15 cells. On AgentDojo, it reaches 82.8% utility at 0.0% ASR, twice CaMeL's utility at the same operating point, and transfers unchanged to unseen AgentDyn suites. It also achieves the best score on Agent-SafetyBench for every victim and keeps mean ASR below 20% under adaptive PAIR attacks with a refinement budget of 16. Analysis shows that domain semantics determine which safety relations and trajectory state are needed, while model and runtime behavior determine how and where those relations should be enforced.

---


### 72. [From Narrative to Auditable Forecasts: A Structured Scaffold for Agentic Forecasting](https://arxiv.org/abs/2609.05905)

**<font color=#1a73e8>作者：</font>** Yuanpu Cao, Yongkang Du, Yurui Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly used for live forecasting, where they retrieve up-to-date information and produce estimates for unresolved future events. However, current agentic forecasting often relies on implicit narrative aggregation: agents collect evidence, discuss it in prose, and often assign a probability without an explicit update path from evidence to forecast. This limits both forecasting accuracy and auditability. We propose AuditForecast, an agentic scaffold for structured probabilistic forecasting. AuditForecast first anchors the forecast with a suitable quantitative baseline model, uses model-guided data retrieval to derive a base probability, and then applies situational factor updates outside the model's scope through mechanical aggregation in odds space. This turns forecasting from a prose-based judgment into a structured process with explicit intermediate objects. Across multiple live forecasting benchmarks, AuditForecast improves forecasting accuracy and calibration relative to strong agentic baselines, surpasses market-implied references in several settings, and outperforms substantially more expensive deep-research agents while remaining Pareto-dominant in the cost--accuracy tradeoff. Beyond performance gains, AuditForecast produces an auditable forecasting report that makes forecast construction explicit and supports systematic post hoc analysis.

---


### 73. [UniRRM: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms](https://arxiv.org/abs/2609.05910)

**<font color=#1a73e8>作者：</font>** Peng Lai, Yichao Du, Junchao Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) excels on tasks with verifiable rewards, but in open-ended tasks, the reliability of reward models remains a key challenge. Existing solutions either depend on costly proprietary LLM-as-a-Judge systems or opaque scalar reward models that lack interpretability. Recent works on generative reward models offer a promising alternative, but they remain constrained by static evaluation criteria, fragmented evaluation paradigms, and limited multilingual support. To address these challenges, we introduce \textbf{MixReward}, a large-scale multilingual dataset spanning six domains and 103 languages, containing both pairwise and listwise data, and propose \textbf{UniRRM}, a unified reasoning reward model supporting multiple languages and evaluation paradigms. UniRRM uses a staged reasoning chain to dynamically generate task-generic and instruction-specific criteria, enabling fine-grained, input-adaptive judgments while maintaining consistency across languages. Experiments demonstrate that UniRRM-8B and UniRRM-14B achieve performance close to the state-of-the-art for models of comparable size across multiple benchmarks, and are effective for unseen evaluation paradigms. In addition, ablation studies validate the reliability and effectiveness of UniRRM.

---


### 74. [Structurally Close, Temporally Distant: Measuring Security Exposure in Long-Horizon LLM Agents](https://arxiv.org/abs/2609.05911)

**<font color=#1a73e8>作者：</font>** Md Jafrin Hossain, Nur Al Hasan Haldar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents interact with untrusted content, persistent memory, external state, and sensitive tools. Existing analyses often characterize attacks by the number of execution steps between malicious input and a downstream action. We show that temporal remoteness can overstate security separation in stateful agents. We introduce a provenance-aware execution graph linking agent events through deterministic state, identifier, and tool provenance, and define \emph{influence distance} $\DI$ as the shortest structural path from an untrusted source to a sensitive action. We compare it with \emph{sequence distance} $\DT$, the shortest injection--sink path in the ordered trajectory. Since the influence graph contains every sequence edge, $\DI \leq \DT$; $\Gap=\DT-\DI$ measures the separation hidden by step count. Across 454 injection--sink pairs from 360 long-horizon AgentDojo trajectories over OpenAI's \texttt{gpt-4o-mini} and \texttt{gpt-4o} and Claude's Haiku 4.5 and Sonnet 4.6, $\Gap>0$ for 96.9% of pairs, with a median gap of 9 hops; 91.0% remain decoupled after removing the largest provenance-only edge class. On AgentDojo's banking suite, 33.8% of 231 pairs from 377 trajectories decouple through different provenance mechanisms. Among 274 OpenAI pairs, $\Gap$ does not independently predict attack success after controlling for $\DT$, attack family, and backend ($\beta_{\Gap}=0.066$, $p=.088$). At matched thresholds $k=2,3$, a deterministic $\DI$-based pre-execution gate blocks five attack sinks missed by a sequence-only gate with no additional benign blocking, although the paired gain is not significant ($p=.0625$). Execution structure therefore reveals proximity hidden by step count and can support targeted runtime intervention. We measure candidate influence pathways rather than causal attribution.

---


### 75. [Neuron-Guided Fine-Tuning: Unlocking Efficient Alignment Mechanisms for Large Language Models](https://arxiv.org/abs/2609.05913)

**<font color=#1a73e8>作者：</font>** Zeyu Wu, Junchao Wu, Shudong Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing Supervised Fine-Tuning paradigms, particularly Full Parameter Fine-Tuning are often plagued by parameter redundancy, inconsistent data quality, and catastrophic forgetting, which current methods typically address in isolation and lack a unified optimization signal to bridge data selection, parameter updates, and knowledge preservation. To address this, we propose Neuron-Guided Fine-Tuning (NGFT), a holistic framework that leverages neuron activation patterns as a universal proxy to unify the fine-tuning lifecycle. NGFT operates via three synergistic mechanisms: (1) Adaptive Task-Specific Neuron Selection, which identifies essential neurons in a single forward pass to concentrate updates and reduce redundancy; (2) Activation-Based Data Selection, which prioritizes information-dense samples that maximize contribution to key neurons; and (3) Neuron Activation Alignment, a novel loss function that anchors activations to pre-trained states, deepening representation learning and preserving general knowledge. Experimental results across three models across both domain-specific and general benchmarks demonstrate that NGFT significantly outperforms existing mainstream fine-tuning methods in both efficiency and performance, while effectively mitigating catastrophic forgetting.

---


### 76. [STAR-Pro: Stage-Wise Token Adaptive Reduction with Progressive Refinement for Efficient Large Vision-Language Models](https://arxiv.org/abs/2609.05916)

**<font color=#1a73e8>作者：</font>** Yichen Guo, Tinghao Wang, Qizhe Zhang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) achieve strong multimodal understanding, but the hundreds to thousands of visual tokens they process impose substantial computational overhead, motivating training-free visual token pruning. In this work, we conduct two complementary analyses of visual token pruning. First, we measure the feature-space coverage of tokens retained before cross-modal fusion and find that aggressive pruning discards substantial visual information. Second, we track text-to-visual attention across decoder layers and find that the visual tokens considered important change substantially with depth, making one-shot pruning decisions unreliable. Together, these findings show that effective pruning should preserve broad visual coverage before fusion and progressively refine the retained tokens as cross-modal evidence evolves during fusion. We therefore propose STAR-Pro (STage-Wise Adaptive Token Reduction with Progressive Refinement), a training-free two-stage framework. Its Adaptive Stage applies pivoted QR to construct an over-budget feature-coverage candidate pool, while its Progressive Stage uses evolving text-to-visual attention at selected decoder layers to prune a nested survivor set under a target layer-average token budget. Extensive experiments across seven LVLMs spanning multiple architectures and 18 image and video benchmarks demonstrate the effectiveness of STAR-Pro under aggressive pruning. On LLaVA-Video-7B, STAR-Pro reduces visual tokens by 90.5%, retains 92.7% of baseline performance, and achieves a $2.24\times$ measured inference speedup. Code is available at this https URL.

---


### 77. [Versioned Transitive Dependency-Closure Binding and Operation-Time Effect Governance for Agent Skills: ClosureBound](https://arxiv.org/abs/2609.05920)

**<font color=#1a73e8>作者：</font>** Genliang Zhu, Chu Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent Skills combine instructions with files, packages, tools, models, and services, so operational identity can exceed a signed directory. Recursive or lazy dependencies may change while root-level evidence remains valid, and different surfaces may reach the same durable effect. We present ClosureBound, a reference monitor that prevents authorization transfer across material changes to this heterogeneous closure. Its resolver commits typed graph nodes and topology. Each grant binds an exact closure root, effect ceiling, purpose/provenance, validity, and epochs. At durability, it re-resolves closure and state, normalizes the operation into an external-effect IR, and admits it only if a joint witness satisfies every bound. Supported equivalent paths share one ceiling. Assuming complete mediation and discovery, authenticated freshness, sound normalization, cryptographic binding, and authoritative linearization, we establish metadata non-authority, closure determinism, version non-inheritance, effect non-amplification, bound-value freshness, and path invariance. We do not establish program equivalence or remote-service honesty. A provider-free implementation matches 40 frozen lifecycle fixtures; 18 kernel contracts and six mutants cover binding and downgrade cases. Full-profile exploration reaches 84,608 states and 530,752 transitions without a declared invariant violation; six weakened profiles yield witnesses. A lexical audit of 549 public Skills (4,872 unique files) finds that 21 of 526 roots with bundled files name every non-manifest path verbatim, 67 contain links resolving outside their roots, and no root declares a frontmatter dependencies field. These observations motivate conservative closure discovery and define concrete targets for broader runtime, interoperability, efficacy, and production validation.

---


### 78. [Solving versus Verifying: Catching Contradictions in Tax Reasoning Systems](https://arxiv.org/abs/2609.05928)

**<font color=#1a73e8>作者：</font>** Albert Sadowski, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models now compute correct tax liabilities on over 90% of well-formed cases in statutory benchmarks, which makes them candidates for the tax-advisory and compliance systems that consume such an answer directly. Real legal inputs, however, are frequently defective: required facts are missing, or stated facts contradict one another. Accuracy on clean benchmarks says nothing about how a model behaves then, and a system that computes straight through a defective input returns a confident number with no sign that anything is wrong. This raises two questions: does a model asked to solve a case abstain when the input is defective, and when it does not, can the same model catch the defect when asked instead to verify the input? We study six recent models on SARA-derived tax cases under missing-fact and contradictory-fact perturbations. The strongest models abstain when a fact is missing but compute through injected contradictions, returning the clean-input answer 63-76% of the time with no signal of the conflict; asked instead to verify the same input, they flag most of those contradictions. We wire that verification call into a simple contradiction gate: one extra call that abstains when the model reports a conflict. Across all six models it recovers most of the missed contradiction abstention at a clean-accuracy cost of at most about 5 percentage points, with no training and no external tooling. High accuracy on well-formed inputs is therefore an incomplete measure of reliability, and the detection the solver misses is cheaply recoverable with a single self-check.

---


### 79. [Rethinking the Evaluation of Efficiency Methods for Multi-Agent Systems](https://arxiv.org/abs/2609.05933)

**<font color=#1a73e8>作者：</font>** Jiamu Zhang, Lingxi Zhang, Pengjun Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficiency is increasingly important for Large Language Model (LLM)-based multi-agent systems (MAS), as larger models and more agents introduce substantial execution costs. Recent methods aim to make MAS cheaper by pruning agents, removing communication edges, or searching for compact structures. However, we argue that existing evaluations may overestimate their true ability to improve MAS efficiency. Reported gains are often measured under method-specific prompts and starting topologies, making them difficult to attribute to the proposed structural changes. Moreover, many reported successes appear in non-MAS-demanding settings, where a single agent or a randomly pruned system can already preserve strong performance. To study these issues, we introduce a controlled and MAS-demanding diagnostic benchmark for representative MAS efficiency methods. We evaluate methods under a shared backbone model, agent registry, and runtime, across controlled variations in topology, scale, depth, and tool use. Our analysis shows that many reported gains are setup-dependent and may arise from structural collapse, disabled tool pathways, or starting systems where random pruning already preserves accuracy, rather than robust improvements in MAS efficiency.

---


### 80. [SurveyAgent-HKA: A multi-agent framework for scientific survey generation with LLMs and human knowledge augmentation](https://arxiv.org/abs/2609.05938)

**<font color=#1a73e8>作者：</font>** Tong Bao, Mir Tafseer Nayeem, Yi Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic scientific survey generation has become an important task in scientific document processing. The common approach of retrieving literature from a single source (e.g., arXiv) and generating surveys through a one-pass large language model (LLM) call often leads to limited reference coverage and, more importantly, fails to replicate the expert-driven revision process that is crucial for writing high-quality surveys. In this paper, we introduce SurveyAgent-HKA, a multi-agent framework that improves end-to-end scientific survey generation by incorporating knowledge derived from published surveys and peer-review comments. The framework decomposes survey generation into well-defined sub-tasks handled by LLM-powered agent. It first retrieves relevant papers from multiple sources and identifies key topics through clustering to construct an initial outline, which is then refined using outlines from related human-written surveys. Based on the refined outline, topic-focused papers are retrieved and re-ranked to select for drafting a well-grounded survey. Then, we identify common issues raised by experts in peer-review comments from published surveys to guide the revisions and finalize the survey. Experiments on two domains show that our approach outperforms mainstream baselines in citation quality, structural consistency, and content quality. Furthermore, our framework is efficient in both time and cost, making it a practical solution for broader AI-assisted scientific writing applications.

---


### 81. [ProtoRAG: Prototype-Based Retrieval Augmentation for Few-Shot Fine-Grained Remote Sensing Object Detection](https://arxiv.org/abs/2609.05953)

**<font color=#1a73e8>作者：</font>** Jian Wang, Yuxiang Hong, Chufeng Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot fine-grained object detection (FGOD) in remote sensing imagery is challenging because limited annotations must support both object localization and discrimination among visually similar subcategories. Although multimodal large language models (MLLMs) provide strong coarse object localization, they lack explicit visual evidence for reliable fine-grained recognition. To address this limitation, we propose ProtoRAG, a prototype-based retrieval-augmented framework that decouples coarse localization from fine-grained recognition by equipping MLLMs with an external object-level visual memory. To construct a reliable visual memory from limited support samples, we introduce Discriminative Prototype Space Learning (DPSL), which encourages discriminative and prototype-stable representations through supervised contrastive learning and prototype-consistency regularization. We further develop an uncertainty-guided candidate-constrained reasoning strategy that augments MLLMs with retrieved candidate-specific visual references and invokes multimodal reasoning only for ambiguous instances. Extensive experiments show that ProtoRAG consistently surpasses representative baselines in nine few-shot settings, outperforming the strongest baselines by 14.80, 2.27, and 4.04 mAP$_{50}$ on MAR20, HRSC2016, and FAIR1M-2.0, respectively.

---


### 82. [LoGIC: Budgeted Context Construction for Node-Level Graph In-Context Learning with Tabular Foundation Models](https://arxiv.org/abs/2609.05955)

**<font color=#1a73e8>作者：</font>** Mingqi Yang, Zidong Guo, Jihui Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models have become powerful graph learners. Systems such as G2T-FM and GraphPFN encode each node as a feature row and make predictions through in-context learning (ICL), with labeled rows serving as the prompt. Current protocols employ the complete training table as context, causing attention to scale quadratically with the labeled pool and introducing preprocessing and memory bottlenecks. We investigate context construction for node-level graph ICL: which labeled nodes and auxiliary unlabeled nodes should constitute the prompt for specified queries. We formulate this allocation in terms of two resources: a labeled-context budget for predictive evidence and an unlabeled-halo budget for adapter message passing without using label capacity. We present LoGIC, which retrieves labeled nodes via structural, feature-based, and coverage channels, shares each context across the queries in a graph-local cluster, incorporates an unlabeled halo for adapter backbones, and chooses the channel and context budget without test labels. Across three backbone configurations drawn from two model families on GraphLand, budgeted contexts maintain locally runnable full-context performance, stay competitive with published large-dataset results, and markedly lower peak memory requirements compared with full-context and whole-graph inference. They further permit frozen graph ICL on million-node graphs without retraining. Our analysis identifies when retrieval channels work best and connects their behavior with graph properties.

---


### 83. [FineHOI: Part-Aware Dense Representations for Zero-Shot Human-Object Interaction Detection](https://arxiv.org/abs/2609.05959)

**<font color=#1a73e8>作者：</font>** Francesco Tonini, Lorenzo Vaquero, Mohammad Mahdi Derakhshani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-Object Interaction (HOI) detection aims to localize humans and objects in images and classify their interactions. Zero-shot HOI focuses on recognizing interactions that are not observed during training, requiring models to generalize beyond seen verb-object compositions. Recent approaches leverage Vision-Language Models (VLMs), benefiting from rich semantic representations. However, they often rely on global or detector-centric features that compress interaction cues and hinder fine-grained spatial reasoning. To overcome this limitation, we propose FineHOI, a zero-shot HOI framework that explicitly models interactions from dense patch-level features. Our approach is motivated by the observation that human-object interactions are defined by localized spatial relationships, which are not preserved by global and detector-centric representations. To this end, we introduce an Adaptive Part-Level Attention module that decomposes humans and objects into semantically coherent parts via unsupervised clustering, and re-weights them based on their interaction relevance. These representations are then integrated through a Region-Aware Interaction Transformer that integrates part-aware and global features and produces the final HOI embedding. Extensive experiments demonstrate that FineHOI consistently outperforms existing zero-shot HOI methods, achieving particularly strong gains on unseen interactions. Code is available at this https URL.

---


### 84. [Beyond Cross-Lingual Transfer: Benchmarking Propagation Boundaries in Multilingual LLM Unlearning](https://arxiv.org/abs/2609.05976)

**<font color=#1a73e8>作者：</font>** Pengyang Shao, Chuanpeng Lu, Wei Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) unlearning aims to suppress target knowledge while preserving general capabilities. In multilingual settings, unlearning must additionally propagate within its intended linguistic scope. However, existing evaluations mainly measure cross-lingual transfer and cannot distinguish insufficient from excessive propagation. We introduce CLLPU (Cross-Lingual and Language-Bound Protocol for LLM Unlearning), a multilingual benchmark that formulates this problem through two settings: common-goal forgetting, where target knowledge should be suppressed across all languages, and language-conditioned forgetting, where suppression should remain confined to a designated language. CLLPU combines goal-guided topic pairing, schema-aware relation matching, and dual-anchor multilingual translation to construct 800 matched knowledge-unit pairs and 72,000 QA instances across ten languages. Experiments with six representative methods on Llama-3.1-8B-Instruct reveal opposite failure modes: forgetting remains incomplete when universal suppression is required, yet spreads beyond the intended boundary when language-conditioned confinement is required. We further find that general multilingual utility can conceal damage to neighbor knowledge. These findings establish propagation control as a central challenge for multilingual LLM unlearning. We publicly release CLLPU together with its construction pipeline.

---


### 85. [Accelerating Diffusion Transformers with Gaussian Process Rectified Feature Cache](https://arxiv.org/abs/2609.05981)

**<font color=#1a73e8>作者：</font>** Zhirong Shen, Rui Huang, Chang Zou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers have become the dominant paradigm in generative AI, but their high computational costs severely hinder real-time applications. Prediction-based feature caching is widely used to accelerate diffusion transformers; however, as the number of steps increases, the deviation between its predictions and the reference full-compute trajectory gradually grows. An intuitive idea is to use an online regression model to dynamically correct this deviation, but it faces the issue of label data being unavailable during the acceleration process. This paper presents a statistical observation that the residuals between the features of full computation steps using caching methods and reference full-compute trajectory locally exhibit a zero-mean Gaussian distribution. By treating the features of full computation steps as noisy observations of reference features, the data acquisition problem is resolved. Based on this observation, a plug-and-play GP-Refiner correction framework is proposed. This method utilizes Gaussian Process Regression for correction and, leveraging the properties of GPR, introduces an uncertainty-adaptive computation strategy that triggers necessary full-computation calibration by monitoring the posterior variance in real time. Experiments demonstrate significant improvements across different models when combined with various state-of-the-art methods. Integrating the proposed framework with TaylorSeer reduces the computational load by 19.3% while improving PSNR by 0.9 dB and reducing LPIPS from 0.46 to 0.29. Code is available in this https URL.

---


### 86. [MOAE: Multi-Objective Agent Evolution with Pareto-Preserving Search](https://arxiv.org/abs/2609.05992)

**<font color=#1a73e8>作者：</font>** Hengle Jiang, Qijun Cai, Ziying Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM-based agents continue to advance, their evaluation has become increasingly multifaceted: a capable agent must not only achieve high task completion accuracy but also perform well in interaction quality, safety, and efficiency, raising a central question: can these objectives be optimized simultaneously? Existing methods have considered multiple objectives, but many collapse heterogeneous measurements into a fixed scalar score. Such scalarization depends on metric normalization and preference weights and may discard candidates that represent useful deployment trade-offs. We introduce Multi-Objective Agent Evolution (MOAE), which organizes iterative in-context refinement as a Pareto-preserving evolutionary search over complete agent rollouts. Given a limited rollout budget, MOAE maintains an empirical archive of non-dominated candidates, uses objective-specific diagnostics to guide offspring generation, and applies constraint-aware selection only at deployment. This separates candidate preservation during search from the preference used to return a final solution. The procedure requires no parameter updates and allows each objective to be replaced by any measurable property, which we instantiate as task performance, trajectory quality, and safety. Experiments on TravelPlanner and AgentDojo show that MOAE consistently improves task performance and trajectory quality while maintaining strong safety under matched rollout budgets. Search-behavior analysis further shows that Pareto preservation expands the attainable objective region and increases the frequency of joint improvement. These results demonstrate the potential of Pareto-preserving in-context evolution for optimizing multiple agent properties without committing to a fixed scalarization during search.

---


### 87. [Alignment by Stereotyping: How LLMs Sacrifice Individual Distinctiveness for Cultural Adaptation](https://arxiv.org/abs/2609.05993)

**<font color=#1a73e8>作者：</font>** Qishuai Zhong, Zongmin Li, Siqi Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed for personalized interaction, and demographic conditioning via user profiles is a widely adopted strategy for cultural adaptation. We ask whether this approach genuinely serves individual users or achieves accuracy by erasing individual distinctiveness. Studying seven models including frontier GPT-5.1 on the World Values Survey, we find that demographic profiles improve value alignment accuracy for most models, but at a systematic cost to individuality. That is, models pull responses toward demographic group centroids rather than preserving individual differences, a behavioral pattern we term alignment by stereotyping. Permutation tests (10,000 permutations, six demographic attributes, seven models) certify that top-performing models compress individuals far above the human baseline; within-family scaling amplifies this tradeoff while degrading intrinsic cultural understanding. Using a synthetic dialogue dataset validated on real human-chatbot conversations from PRISM (Kirk et al., 2024), we further show that distributing demographic signals across conversational turns partially suppresses prototype retrieval compared to compact demographic labels, a finding validated on real conversations via PRISM but requiring replication at larger scale.

---


### 88. [Geometry-Aware Test-Time Learning for Quantitative Spatial Reasoning](https://arxiv.org/abs/2609.06004)

**<font color=#1a73e8>作者：</font>** Gege Zhang, Shuaicheng Niu, Gang Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative spatial reasoning in visual-language models (VLMs) aims to infer spatial distances and directional relationships among objects in 3D space from a 2D image and a natural language query. Despite recent progress, VLM spatial reasoning remains brittle under distribution shifts, largely due to the high cost of 3D supervision. As a result, models often produce inconsistent or contradictory predictions when faced with novel object configurations or rephrased spatial queries, revealing a misalignment between learned representations and underlying geometry. To address this, we propose TTL-SR, a geometry-aware Test-Time Learning framework for quantitative Spatial Reasoning that leverages geometric consistency constraints and unlabeled test data to adapt models to target domains. Specifically, TTL-SR augments the input query with geometrically coupled auxiliary queries, filters unreliable predictions via adaptive geometric triggering to construct structured token-level pseudo-labels, and updates model parameters under a geometry-aware multi-objective loss using only test data. Experimental results demonstrate that TTL-SR significantly boosts spatial reasoning performance, yielding 6.47% and 9.41% accuracy gains for Qwen3-VL-4B-Instruct and SpatialRGPT-VILA-1.5-8B on Q-Spatial-ScanNet dataset, respectively.

---


### 89. [Memory in Deep Time-Series Models](https://arxiv.org/abs/2609.06006)

**<font color=#1a73e8>作者：</font>** Minh Hoang Nguyen, Huu Hiep Nguyen, Manh Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning for time series has progressed through successive architectural paradigms, from recurrent networks and transformers to structured state-space models, retrieval-augmented predictors, foundation models, and tool-using agents. These developments are typically studied in isolation, organized by architecture or modeling era. We argue that they can instead be viewed through a common question of \emph{how does a time-series model retain and access information beyond its immediate input?} This question is motivated by a fundamental limitation of conventional time-series modeling: information relevant to a prediction may lie far beyond a feasible input window, while compressing history into a fixed-size state can discard information that may become useful later. We formulate this challenge as a \emph{memory} problem and organize existing time-series methods along a spectrum from internal memory, encoded in parameters and fixed-size states, to external memory that is addressable, retrievable, and increasingly maintained by agents. We then develop a unified taxonomy of memory mechanisms and review three classes of external memory, including explicit modules, retrieval augmentation, and agentic stores, under a common framework for what is retained, how it is written and accessed, and how it persists. A cross-cutting analysis maps these mechanisms to time-series tasks and identifies gaps in both methods and evaluation. We conclude by outlining open problems in building memory systems that can selectively retain, retrieve, revise, and forget information as temporal environments evolve. The result is a framework for studying memory as a first-class dimension of time series modeling, independent of the underlying backbone.

---


### 90. [Tri-PvP: Exposing Modality Bias in Omni-Modal Large Language Models through Perceptual-Propositional Evidence Conflicts](https://arxiv.org/abs/2609.06011)

**<font color=#1a73e8>作者：</font>** Yen-Ting Piao, Shu-Yun Chen, Chin-Hui Chu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models (OLLMs) jointly process vision, audio, and text, yet their modality bias under cross-modal conflict remains underexplored. Existing benchmarks conflate two distinct forms of evidence within a single modality: perceptual signals (e.g., a photograph or recording of a dog) and propositional signals (e.g., the declarative claim "this is a dog"), such that any measured modality bias is inherently confounded with evidence-form bias, precluding clean attribution to either source. To address this, we introduce Tri-PvP, an 8,000-sample tri-modal conflict benchmark crossing vision, audio, and text, where vision and audio each take perceptual or propositional form. Evaluating five OLLMs, we find robust visual bias across most models and evidence-type conditions. Crucially, we reveal a systematic asymmetry in evidence-form bias: models exhibit a stronger bias toward perceptual signal in vision but propositional in audio. Further analyses via layer-wise linear probing and contrastive decoding reveal that modality bias is already linearly decodable from early representation layers and can only be partially mitigated, calling for mitigation strategies beyond surface-level interventions.

---


### 91. [Generator-Independent Runtime Assurance under Partial Observation](https://arxiv.org/abs/2609.06036)

**<font color=#1a73e8>作者：</font>** Guangxi Wan, Yongbo Xie, Yuqi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proposal-based controllers---learned policies, language-model planners, and other black-box \emph{generators}---are increasingly deployed behind runtime verification gates. We ask when the closed-loop safety guarantee decouples from the generator. The prevailing per-candidate certification pattern does not compose: under retry or best-of-$k$ selection a per-candidate false-admission level $\alpha$ can inflate to $1-(1-\alpha)^{k}$. Our main theorem shows that \emph{simultaneous setwise soundness}---certifying a set of admissible proposals containing no nonviable action---is necessary and sufficient for generator-independent \emph{admission soundness}, the worst case over all generators of executing a nonviable proposal equalling the probability of setwise failure; together with a design-time certificate and a no-bypass rule it is sufficient for \emph{contract safety}, with violation bound $\Gamma+\sum_t\varepsilon_t+\eta$ invariant under arbitrary, even adversarial, replacement of the generator. A second theorem bounds every admission mechanism under partial observation: for a fixed probing and admission policy, if two state hypotheses whose information laws lie within total-variation distance $\delta$ require different safe decisions, then $\abar+\beta+\delta\ge1$. A sequential risk ledger makes the guarantee implementable with time-uniform confidence tubes, and shows that deterministic admission computations concentrate all statistical risk in state estimation. Simplex-style runtime assurance and control-barrier-function filtering are recovered as degenerate cases.

---


### 92. [Generating Adversarial Texts for Machine Translation via GRPO](https://arxiv.org/abs/2609.06048)

**<font color=#1a73e8>作者：</font>** Florian Zogaj, Jakob Hütteneder, Giovanni De Muri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As machine translation (MT) systems continue to improve, standard benchmarks become less informative for exposing remaining weaknesses. Traditional methods for creating challenging test sets rely on expensive manual creation or curation, while automated approaches struggle to produce sets with the necessary translation difficulty and linguistic diversity. We propose a scalable reinforcement-learning-based approach for rewriting existing source texts into instances that are more difficult to translate for MT systems. We fine-tune a large language model with Group Relative Policy Optimization (GRPO), using reward signals based on translation difficulty together with constraints for semantic similarity, grammaticality, and approximate length preservation. On WMT25, our approach substantially reduces average COMET translation quality from 0.63 to 0.48, while preserving grammaticality and readability, whereas the base model remains at 0.64. Evaluations on the unseen WMT19-WMT24 benchmarks confirm that this behavior generalizes beyond the training data, and human evaluation further shows that the rewrites substantially lower translation quality while incurring a moderate drop in naturalness and only a small change in grammaticality. We release our code to support reproducibility.

---


### 93. [Data Quality Rule Generation with LLMs](https://arxiv.org/abs/2609.06053)

**<font color=#1a73e8>作者：</font>** Anna-Christina Glock, Thomas Hütter, Johannes Fürnkranz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The validation of data, such as customer and employee data, is an important task in many organizations. Errors in data can have severe consequences. For example, a wrong drug unit in a patient record can lead to life-threatening medication errors, and a missing street number in an address to failed deliveries. Companies often employ rule-based enterprise data quality (DQ) tools, which allow domain experts to specify rules to validate the data over time. While rule-based DQ tools are computationally efficient and provide explainable reports, maintaining a comprehensive rule set manually is challenging, as domain experts often overlook essential rules, especially in complex domains and large data volumes. Hence, closing these gaps remains an open problem in practice. In this paper, we address the challenge of automated DQ rule generation. For this, we formalize a generalizable generate-filter framework and introduce LeDQeR, an LLM-based DQ rule generation approach. First, a large language model (LLM) generates candidates rules from an observed dirty data tuple for a given rule-based DQ tool syntax. Second, we apply four filter techniques that ensure the (i) executability, (ii) correctness, and (iii) generalizability, and avoid (iv) redundancy of the generated rules. An extensive experimental evaluation suggests that LeDQeR is able to produce effective and compact rule sets for various datasets and error types.

---


### 94. [GradeTrap: Authority Cues in Images Shift VLM Judgments Despite Explicit Instructions to Ignore Them](https://arxiv.org/abs/2609.06058)

**<font color=#1a73e8>作者：</font>** Deep Dessai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As vision-language models (VLMs) become increasingly capable and are deployed in consequential real-world settings, they must evaluate evidence independently rather than defer uncritically to human authority. We introduce GradeTrap, a controlled evaluation that places two social cues in direct conflict: a student answer, which should attract sycophantic agreement, and a conflicting answer attributed to a peer, teacher, or official answer key, which should attract authority-based deference. Models produce free-form answers while being explicitly instructed to solve independently and ignore all student answers, feedback, and grading marks. We test the models on 60 synthetic real-world trade-off scenarios. Five neutral trials establish a stable model-relative preference, followed by three repetitions of six experimental cues including controls. On the 45-item common intersection across Gemini 3.5 Flash-Lite, GPT-5.6 Luna, and Claude Haiku 4.5, a generic second-answer control yields 5.4% conflicting-answer selection. Relative to that control, pooled within-item changes show no reliable peer-review effect, a 6.9-point teacher-review effect, and a 19.5-point official-key effect. In contrast, a displayed conflicting student answer alone compared to a displayed student reference answer alone only raises selection from 2.2% to 5.2%. Official-key provenance therefore redirects judgements more than a student answer or the generic second-answer control, despite an explicit ignore instruction and an opposing student answer given along with the official key. Effects vary in magnitude across the three models.

---


### 95. [DAREBench: Deployment-Aware and Reliable Evaluation of Models as Agents](https://arxiv.org/abs/2609.06059)

**<font color=#1a73e8>作者：</font>** Yu Liu, Zhilin Liu, Zhiwei Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models evolve from question-answering systems into general-purpose agents, evaluation must move beyond static answer correctness to assess multimodal perception, multi-step execution, tool use, and artifact delivery. However, existing benchmarks are often tied to specific task types, execution environments, or scoring protocols, limiting their comparability, interpretability, and reliability for deployment decisions. We introduce DAREBench (Deployment-Aware and Reliable Evaluation of Models as Agents), a benchmark designed to capture workload variation and support reliable agent evaluation. Built on a shared OpenClaw execution environment, DAREBench organizes 233 tasks selected and adapted from 22 source benchmarks into a $2\times3$ workload matrix defined by input modality and execution form, and evaluates them under a unified contract-based protocol with evidence-based score auditing. We evaluate 23 commercial API models and 12 locally deployed open-weight models over 7,587 model--task runs, reporting accuracy and token consumption alongside reference costs for API models. Results show that no single model dominates all workload groups, text and multimodal tasks exhibit distinct accuracy--cost trade-offs, and local open-weight models are competitive in several groups but still trail frontier commercial models overall. These findings suggest that agent deployment and model selection should consider workload profiles, deployment mode, and accuracy--cost trade-offs rather than rely on a single aggregate score.

---


### 96. [Explaining AI Agents Through Execution Traces](https://arxiv.org/abs/2609.06063)

**<font color=#1a73e8>作者：</font>** Vittoria Vineis, Fabiano Veglianti, Lorenzo Antonelli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI Agents are increasingly deployed in real-world settings, where they interact with external tools and make sequential decisions with limited human oversight. This creates a pressing need for reliable and auditable explanations of what an agent did and why. However, traditional Explainable AI (XAI) methods fall short of providing the process-level transparency required for such interactive, multi-step systems, motivating a paradigm shift toward approaches specifically designed for AI Agents. To address this gap, we present a post-hoc XAI framework that transforms a lengthy agent's execution trace into a structured report and a faithful natural-language explanation explicitly grounded in its observable behavior. Because it relies solely on execution traces, the framework applies across different agent architectures, environments, and tasks. Human and automated evaluations across multiple benchmarks and architectures show that our framework produces high-quality, trace-faithful explanations while reliably identifying unsupported claims, unjustified actions, and evidence gaps, outperforming naive LLM-generated explanations.

---


### 97. [Don't Lose Entities from Retrieval to Generation: Dual Entity Recovery RAG for multi-hop QA](https://arxiv.org/abs/2609.06065)

**<font color=#1a73e8>作者：</font>** Heechang Lee, Dong-Young Lim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented multi-hop question answering (QA) decomposes a query into sub-questions and decomposes the corpus into smaller retrieval units such as sentences. Both forms of decomposition improve the pipeline, but we show that both share the same vulnerability, the loss of entity information, and that this loss breaks the pipeline at two separate points. The first point is retrieval, where a sub-question loses the entity resolved at the previous hop, leaving the retriever with nothing to match against. The second point is harder to see, because retrieval still appears to succeed. Once a passage is split into sentences, an isolated sentence loses the context that grounds its pronouns, so even with the correct sentence in hand the LLM cannot tell which entity the sentence is about. We isolate this second point as a distinct failure mode that we call lost-in-generation, and a retrieval-controlled experiment shows that it degrades answers even when the gold evidence is fixed in the context. We then propose Dual Entity Recovery RAG (DER-RAG), which keeps the grounding entity explicit from retrieval through to generation with two lightweight components, a two-way query decomposition that carries the resolved entity across sub-questions and a subject entity prefix attached to each sentence at generation time. DER-RAG needs no graph construction, no corpus modification, and no fine-tuning, yet on three multi-hop QA benchmarks it matches or exceeds strong baselines, including graph-based methods that depend on costly offline structures.

---


### 98. [Generating Instance Generators in PDDL Planning](https://arxiv.org/abs/2609.06071)

**<font color=#1a73e8>作者：</font>** Nicola J. Müller, Naya Rudolph, Katharina Stein 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> PDDL, the de-facto standard language in the AI Planning community, is designed to specify planning domains: sets of instances that share the same predicates and action schemas. Yet it does not provide any means to specify the actual instance set, i.e., legality constraints on initial states and goal conditions, as well as possibly domain subset constraints specifying an instance subset we are interested in. One consequence of this is that instance generation has always been ad-hoc, with manually written domain- and subset-specific instance generators. Recent work has started to address this, through reasoning and learning methods that however suffer from scalability limitations. Here we introduce an alternative approach, leveraging LLMs to generate instance-generation programs, with built-in soundness guarantees through prescribed checks. We show that these automatically generated instance generators return large numbers of sound and diverse instances efficiently.

---


### 99. [ACE: Adapter Consolidation across Experts for Parameter-Efficient Fine-Tuning of MoE LLMs](https://arxiv.org/abs/2609.06072)

**<font color=#1a73e8>作者：</font>** Ahin Lee, Sehyun Yun, Joonha Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) of mixture-of-experts (MoE) models commonly attaches a separate low-rank adapter to each expert. This expert-wise design fragments adaptation in three ways: capacity is split across narrow low-rank updates, gradient supervision becomes sparse and imbalanced under sparse routing, and execution is decomposed into many small GEMMs. We find that such expert-wise separation is often unnecessary, as subsets of LoRA adapters become functionally similar during fine-tuning, revealing redundancy among expert-specific adapters. Based on this redundancy, we propose ACE (Adapter Consolidation across Experts), which groups redundant experts and replaces their expert-specific adapters with group-shared higher-rank LoRA modules under the same PEFT budget. ACE further introduces grouped adapter execution, which consolidates fragmented expert-wise adapter computations into fewer, larger group-level GEMMs. Across evaluations covering 12 datasets and four MoE backbones, ACE achieves the highest observed mean accuracy among the parameter-matched PEFT methods on the three backbones with complete baseline coverage, while providing $1.31\times$ to $1.48\times$ wall-clock training speedup over expert-wise LoRA without increasing peak memory. Our code is available at this https URL.

---


### 100. [FedSubMuon: Communication-Efficient Federated LLM Fine-Tuning via Structured Subspace Muon](https://arxiv.org/abs/2609.06073)

**<font color=#1a73e8>作者：</font>** Shaolong Chen, Youming Tao, Shuzhen Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning adapts large language models (LLMs) to decentralized client data, but its scalability in cross-device training is often limited by the high communication cost. Muon is an optimizer that improves optimization performance by orthogonalizing momentum for matrix-valued parameters. Existing federated Muon methods demonstrate the benefit of matrix-aware optimization in federated learning, but still require transmitting full layer-size updates and optimizer state. A natural way to reduce communication is to directly apply Muon to LoRA factors, but this changes the optimized object and weakens Muon's matrix-aware update geometry. We propose FedSubMuon, a communication-efficient federated Muon fine-tuning method that optimizes compact coefficient matrices within shared structured subspaces. This design keeps Muon on a single matrix-valued trainable object, while reducing the client upload to compact coefficient matrices. We further introduce FedSubMuon-GT, an accuracy-oriented extension that uses projected gradients to adapt tracked subspace bases toward task-relevant gradient directions. Experiments on instruction tuning and mathematical reasoning show that FedSubMuon-GT achieves the best overall accuracy on four of five dataset-model pairs, while FedSubMuon performs best under all matched communication budgets. On Dolly-15K, the closest communication baseline requires 5.5 times and 1.4 times more total communication on Llama-1B and Qwen-4B, respectively.

---


> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
