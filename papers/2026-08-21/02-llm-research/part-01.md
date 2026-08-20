# 🧠 大模型相关研究 | 2026年08月21日

> 本类共 **166** 篇论文：已确认 **153** 篇，待复核 **13** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-166](./part-04.md)

---

### 1. [Position: Collusion Risks Among AI Reasoning Agents Justify Certification Requirements for Making Market Decisions](https://arxiv.org/abs/2608.18078)

**<font color=#1a73e8>作者：</font>** Matthew Riemer, Tommaso Tosato, Amin Memarian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper argues that AI agents with chain-of-thought reasoning capabilities are predisposed to exhibit collusive behavior and should be required to obtain behavioral certification before making decisions that affect economic markets. This is because integrating these agents into society could collapse the legal evidentiary distinction between competition and collusion among independent firms without eroding the economic harm distinction. Experiments with DeepSeek-R1 agents in the Bertrand oligopoly pricing domain reveal a tendency towards tacit collusion that persists even when humans prompt the agents not to collude. We further show that the chain-of-thought of these agents can be steered toward either extremely collusive or highly competitive behavior in a way that is not semantically detectable by another LLM analyzing the reasoning traces. As a result, deploying reasoning agents for market decisions leads to collusive economic outcomes without any evidence of conspiracy or intent. Thus, certification based on observed behavior in representative situations is necessary to prevent collusion. We provide preliminary evidence that such agents can be steered in a generalizable way toward efficient competitive equilibria. However, developing a comprehensive behavioral certification will be required before these models can be deployed in real-world markets while ensuring their stability and efficiency.

---


### 2. [Large Language Models in Mental Health: A Systematic Review of Applications, Innovations, and Ethical Challenges](https://arxiv.org/abs/2608.18080)

**<font color=#1a73e8>作者：</font>** Yisong Chen, Yifan Gao, Sijing Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a review on the applications of large language models (LLMs) in health, e.g., social media analysis, clinical conversational agents, therapy support tools, prompt engineering, multimodal learning, and ethical considerations. We integrate findings from interdisciplinary studies utilizing diverse data sources such as social media posts, electronic medical records, and multimodal inputs to enable early detection of depression, suicide risk assessment, personalized therapy support, and psychoeducational content generation. Our review highlights advancements in LLM models and annotation strategies that enhance interpretability and clinical relevance, while we also emphasize the critical role of prompt engineering for domain adaptation. We also discuss emerging multimodal fusion techniques integrating text, speech, and sensor data for improved mental health diagnosis and monitoring. Finally, we address ongoing ethical, sociotechnical, and regulatory challenges, and advocate frameworks to ensure safe, equitable, and accountable deployment of LLMs in real-world mental health care.

---


### 3. [Entity tracking emerges in sub-billion parameter language models and exceeds human performance in naturalistic narratives](https://arxiv.org/abs/2608.18083)

**<font color=#1a73e8>作者：</font>** Karolina Drożdż, Micha Heilbron  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding language requires tracking entities across discourse - i.e., knowing where things are and how they change, even when not explicitly stated. Whether language models perform such tracking in a human-like fashion remains unclear, in part because existing evaluations rely on artificial tasks, far removed from natural language comprehension, and lack comparisons to humans. Here, we evaluate entity tracking in both language models and humans (N = 48) using naturalistic narratives at multiple levels of complexity. In humans, we find that entity tracking degrades specifically with narrative complexity, not narrative length. In language models, we find that human-level entity tracking is already present at 410 million parameters - well below the multi-billion parameter, code-specialised models identified by prior work - and improves with scale, with contemporary models far exceeding human performance. Together, these results demonstrate that entity tracking, a core component of language understanding, emerges at model scales far smaller than previously thought.

---


### 4. [Compiler-Guided Adaptive Proof Search with Cross-Model Synergy on Context-Dependent Theorem Proving](https://arxiv.org/abs/2608.18084)

**<font color=#1a73e8>作者：</font>** Zhuo Liu, Ding Yu, Hangfeng He  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Theorem proving in real-world Lean 4 projects is challenging because proofs often depend on project-specific context. While iterative refinement can use compiler errors to repair failed proofs, reusing failed attempts requires careful search control: some proofs provide better starting points than others, and later revisions may degrade a partially correct proof. We propose a compiler-guided proof search framework that balances exploration and exploitation. It explores diverse starting points through dual-model generation and stagnation-triggered resampling, while exploiting promising proof states through current-best refinement guided by compiler-grounded pairwise comparison. Experiments on seven real-world Lean 4 projects from miniCTX-v2 show that our method achieves a better effectiveness--efficiency tradeoff than pass@k baselines. Within the pass@32 budget, our method improves average pass rate by 12.8 percentage points while reducing LLM calls by 21.9%.

---


### 5. [Persona-Guided LLM Agents for Task-Oriented Dialogue](https://arxiv.org/abs/2608.18085)

**<font color=#1a73e8>作者：</font>** Maryam Shoaeinaeini, Brent Harrison, A.B. Siddique  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work has shown that large language models (LLMs) can express diverse personality traits in open-ended text generation. However, it remains unclear whether they can do so in a goal-directed dialogue without compromising task completion, and whether adapting to the user's personality improves the interaction quality. We study these questions in task-oriented dialogue (TOD), where a system helps a user accomplish a goal via multi-turn interaction. We build a training-free framework that simulates a TOD interaction between two LLMs: a user agent that exhibits a target personality and a system agent that adapts to the user while completing the task. To isolate the effect of adaptation, we vary how much the system knows about the user's personality across three conditions. In Neutral, the system receives no personality information. In Try, it infers the personality from dialogue cues. In Oracle, it is given the personality explicitly. We evaluate GPT-4o, Qwen3-Next-80B, and Gemini 2.0 Flash on Hotel and Restaurant dialogues from the Schema-Guided Dialogue (SGD) dataset, across the Big Five traits and their opposite poles. We find that the user agent can express personality while the system maintains strong task performance, although some traits are realized far less reliably than others. Adapting to the user's personality improves constraint satisfaction, inform rate, and user satisfaction, but lowers truthfulness, revealing a trade-off between personalization and task-grounding. Oracle's gains grow when the target trait is strongly expressed, whereas Try's gains are largely insensitive to realization strength. Overall, cue-based adaptation in Try best resolves this trade-off and offers a more reliable route to personality-aware TOD without fine-tuning.

---


### 6. [Latent Space Refusal Anchoring for Low-Resource African Languages: Mechanistic Safety Recovery Without Retraining](https://arxiv.org/abs/2608.18089)

**<font color=#1a73e8>作者：</font>** Godwin Abuh Faruna  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned models often refuse harmful requests in English but comply with the same requests in Yoruba, Igbo, Igala, and Hausa. This suggests that the refusal mechanism is present in the residual stream but fails to activate for low-resource inputs. Recovering it normally requires labelled target-language data and retraining, neither of which is available at scale for most African languages. We introduce Latent Space Refusal Anchoring (LSR-Anchoring), a training-free method that extracts the refusal direction from English prompts and clamps it onto the residual stream at inference time. The primary variant, Mean-Activation Steering (MAS), operates across the four architectures we tested: Llama-3-8B, Llama-3.1-70B, Mistral-7B-Instruct, and Qwen2.5-7B. On Mistral and Qwen it recovers safety with benign degradation below 0.08. On Llama-3-8B it overcorrects, with Degraded Performance on Legitimate prompts (DPL) reaching 1.00. We address this with SAE-Derived Steering (SDS), which replaces the dense mean-difference direction with a single Sparse Autoencoder (SAE) feature and reduces Kullback-Leibler (KL) divergence by 3.5-7x without benign collapse. Four languages transfer positively, but Arabic fails on every architecture and at every steering magnitude, indicating a geometric mismatch rather than a baseline effect. Massive Multitask Language Understanding (MMLU) accuracy drops remain below 0.35 percentage points at every effective steering magnitude.

---


### 7. [Nine Emotion Centroids: A Label-Free Valence Axis That Transfers Across Four Modalities](https://arxiv.org/abs/2608.18090)

**<font color=#1a73e8>作者：</font>** Yousef Radwan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Inside a modern language model sits a single internal direction that tracks how positive or negative a sentence feels. We show how to find this valence axis (V-axis) from just 9 emotion category names plus 50 short narrative paragraphs per emotion -- about 1,500 fewer labels than the usual supervised approach -- and that the same direction appears in vision, audio, and human-brain encoders never jointly trained. The recipe: embed nine emotion-anchored story sets in a frozen encoder, take the top principal direction of the nine averaged embeddings. Projecting new inputs onto it captures 93% of supervised performance on SST-2 (Llama-3-8B-Instruct, AUC 0.772 vs. 0.828), correlates with human valence ratings on 11,811 EmoSet images at r=0.636, reaches AUC 0.906 on ESC-50 audio (p<2.2e-15), and AUC 0.720+/-0.055 on EEG from 123 subjects (p<3.65e-8). The direction is mechanistically active: ablating it collapses sentiment accuracy by 5.5-37.2 pp across three LLMs vs. at most 0.88 pp for matched random directions (z>12). A 2-parameter classifier trained on text labels transfers to images (AUC 0.961), audio (0.764), and brain recordings (0.828) without target-modality labels; a generic 16-D subspace stays at chance (0.525). The recipe is bounded to continuous attributes -- seven tests on categorical concepts return near-chance -- and steering is family-specific (Llama/Mistral yes, Qwen/Gemma no).

---


### 8. [Self- and Other-Labels Induce Bidirectional Bias in LLM Judges](https://arxiv.org/abs/2608.18091)

**<font color=#1a73e8>作者：</font>** Songeun Chae, Min Kim, Donghoon Jung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM-as-a-judge systems become increasingly widespread, self-preference in LLMs -- the tendency to favor one's own outputs -- raises growing concerns about evaluation reliability. However, it has been studied predominantly on generated text, where stylistic features and response quality are inevitably conflated. As a result, existing measurements cannot separate genuine self-preference from these confounds. We address this by changing the object of evaluation: instead of judging generated text, ten LLMs assess narrative constraint selections, which carry no model-specific stylistic fingerprint yet retain a recoverable model-specific signature. We run two experiments that yield distinct findings. Under blind evaluation, self-preference largely disappears once selection quality and evaluator severity are controlled. It vanishes on three of four rubric dimensions and reverses on the fourth, where judges rate their own selections as less original. Under matched quality, however, self- and other-labels alone -- without naming any model -- shift scores bidirectionally: LLM judges inflate scores for self-labeled selections and deflate those for other-labeled ones regardless of the selection's actual source. We make two contributions: 1) authorship attribution is a distinct driver of evaluation bias, and 2) open-ended, ground-truth-free tasks can serve as controlled instruments for studying LLM judge behavior.

---


### 9. [Position: Multi-Agent Systems Should Prioritize Concurrency Control](https://arxiv.org/abs/2608.18092)

**<font color=#1a73e8>作者：</font>** Xin Yang, Letian Li, Zimo Ji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MAS) promise scalable collaboration, yet adding agents often reduces reliability. This position paper argues that many MAS failures are fundamentally concurrency control problems: agents concurrently read and write shared state, and long LLM inference windows amplify the risk of stale reads, lost updates, and inconsistent outcomes. Failure modes commonly attributed to coordination or communication breakdowns can be mapped directly onto classical concurrency anomalies. We contend that MAS frameworks should address these failures through explicit concurrency control mechanisms: conflict detection, isolation guarantees, and structured access to shared resources. Concurrency control should be a first-class design concern, not an afterthought.

---


### 10. [Abliteration Mitigation via Refusal Aliases](https://arxiv.org/abs/2608.18093)

**<font color=#1a73e8>作者：</font>** Nathan Truong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Abliteration, the removal of refusal capabilities from large language models by projecting weight matrices orthogonal to an extracted refusal direction, has emerged as a prominent safety concern through its ability to bypass post-training alignment using only a small set of contrastive prompts. We find that existing defenses commonly overlook the cause of abliteration; that is, how easily the refusal direction can be extracted. To hinder this process, we introduce a weight-editing method that obscures the refusal signal by applying rank-$k$ updates to residual stream writer matrices while replacing refusal-inducing activations with random aliases and correcting downstream reader matrices to preserve the model's original behavior. On Llama-3-8B, AMRA improves post-abliteration refusal scores by $2.16$ points over the undefended baseline with less than $0.5$ percentage points of MMLU degradation. On Gemma-2-9B, it improves the post-abliteration refusal by $14.70$ points over the baseline while keeping harmful output rates similar to the baseline, albeit at a greater utility cost.

---


### 11. [NE-BERT: A Multilingual Language Model for Nine Northeast Indian Languages](https://arxiv.org/abs/2608.18094)

**<font color=#1a73e8>作者：</font>** Badal Nyalang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large pretrained language models have demonstrated remarkable capabilities across diverse languages, yet critically underrepresented low-resource languages remain marginalized. We present NE-BERT, a domain-specific multilingual encoder model trained on approximately 8.3 million sentences spanning 9 Northeast Indian languages and 2 anchor languages (Hindi, English), a linguistically diverse region with minimal representation in existing multilingual models. By employing weighted data sampling and a custom SentencePiece Unigram tokenizer, NE-BERT outperforms IndicBERT-V2 and MuRIL across all 9 Northeast Indian languages, achieving 15.97X and 7.64X lower average perplexity respectively, with 1.50X better tokenization fertility than mBERT. We address critical vocabulary fragmentation issues in extremely low-resource languages such as Pnar (1,002 sentences) and Kokborok (2,463 sentences) through aggressive upsampling strategies. Downstream evaluation on part-of-speech tagging validates practical utility on three Northeast Indian languages. We release NE-BERT, test sets, and training corpus under CC-BY-4.0 to support NLP research and digital inclusion for Northeast Indian communities.

---


### 12. [MAVEN: A Macro-Societal Value Evaluation Framework of Multimodal Content with Compact Aligned Evaluators](https://arxiv.org/abs/2608.18096)

**<font color=#1a73e8>作者：</font>** Zijuan Zhao, Zheren Fu, Hou Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Assessing whether multimodal content aligns with macro-societal values, such as peace, justice, and freedom, has become an increasingly urgent challenge. Existing frameworks are largely confined to safety-oriented taxonomies, text-only psychometric probes, or single-label classification. Therefore, we propose MAVEN, a hierarchical framework for macro-societal value evaluation of multimodal content, grounded in international human-rights instruments and cultural value theory. MAVEN organizes values into 6 primary dimensions and 72 secondary indicators, supporting multi-level quantitative scoring. Building on MAVEN, we construct a human-verified multimodal benchmark and a soft-match metric to evaluate VLMs' assessments across value dimensions. For evaluator optimization, we propose a span-adaptive variant of multi-level preference optimization for evaluator distillation, together with a training-free multi-role consensus strategy at inference time. We evaluate existing open- and closed-source VLMs on our benchmark, revealing shared tendencies and clear differences in macro-societal value judgments. Experiments show that our compact 2B evaluator matches its 8B counterpart in the same family and approaches frontier closed-source VLMs, offering a practical path toward scalable macro-societal value evaluation. Our SA-MDPO implementation and MacroValue-Bench are available at this https URL.

---


### 13. [FrenchNews-7: Benchmarking Cross-Publisher French News Editorial Desk Classification](https://arxiv.org/abs/2608.18097)

**<font color=#1a73e8>作者：</font>** Amr Sobhy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present FrenchNews-7, a cross-publisher France-based French-language news editorial desk classification benchmark combining a large multi-outlet corpus, a URL-derived seven-class taxonomy, and a fine-tuned CamemBERT classifier. Labels are assigned via a hybrid pipeline combining publisher URL slugs with LLM annotation for structurally ambiguous cases, audited through an inter-rater study (2 humans + 2 LLMs; pairwise $\kappa \geq 0.766$, human--human $\kappa = 0.806$). We evaluate lexical, multilingual, and French-specific trained classifiers under both in-distribution and held-out-publisher settings, with additional comparison against zero-shot LLM baselines (GPT-OSS-120B, Mistral Small 3.2, Llama-3.3-70B) on the held-out pool. The strongest model, CamemBERT-base on full article text, outperforms headline-only input, generalizes to unseen outlets, and exceeds all three zero-shot LLM baselines on overall recall (0.799), with the gap concentrated in the ambiguous editorial-boundary categories Economie and Societe. Cross-publisher evaluation reveals uneven boundary stability: Sport, Culture & Loisirs, and International transfer cleanly, while Economie (recall = 0.517) is close to blinded human agreement (0.55), and Societe (precision = 0.577) absorbs boundary ambiguity, both suggesting editorial conventions rather than recoverable classifier headroom. The fine-tuned CamemBERT-base model, labeled manifest, reference collection scripts, and a reliability-tier guidance table are available at this https URL (model) and this https URL (dataset).

---


### 14. [Fractional Decay KV-Cache: Ownership-Aware Memory Management for Improved Inference Relevancy in Dialog Systems](https://arxiv.org/abs/2608.18098)

**<font color=#1a73e8>作者：</font>** Sukanta Ganguly  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) caching is essential for efficient autoregressive inference in transformer based dialog systems, yet existing strategies treat all cached entries uniformly or apply coarse eviction heuristics that fail to adapt as dialog topics evolve. We propose Fractional Decay KV-Cache (FD-KVC), a novel algorithm that maintains a dual-channel scoring mechanism for each cached KV pair: a cumulative attention channel that tracks aggregate importance (akin to H2O), and a recency-weighted relevance channel governed by temporal decay and reinforcement-inspired updates. The combination enables FD-KVC to both preserve historically important tokens and rapidly adapt when dialog topics shift. An adaptive learning rate driven by an ownership loss function ensures convergence without oscillation. FD-KVC operates entirely on CPU with negligible overhead. Across five diverse multi-turn dialog scenarios with 600 dialogs each, FD-KVC outperforms H2O, the state-of-the-art heavy-hitter baseline, by +6.7% on composite late-turn alignment, with improvements of +127% on topic-shift, +87% on gradual evolution, and +30% on mixed-topic dialogs. FD-KVC adapts to new topics 3.6X faster than H2O and achieves the highest topic diversity (80.6%) across all methods. Ablation studies confirm the contribution of each component.

---


### 15. [FinSkillBench: Evaluating AI Agents and Domain Skills for Investment Management](https://arxiv.org/abs/2608.18099)

**<font color=#1a73e8>作者：</font>** Jermyn Zhen Yong Bek, Zhuang Qiang Bok, Zhongtian Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Investment management is a high-stakes domain in which agentic AI systems must do more than generate plausible text. They must retrieve point-in-time data, assemble correct computational inputs, invoke specialized methods, and produce auditable structured outputs. We introduce FinSkillBench, an evaluation suite designed to measure whether language model agents can effectively use financial domain skills to solve investment management tasks. The benchmark spans three domains, portfolio construction, risk management, and fundamental analysis, and includes 12 subtasks with 2,603 task episodes.
Each episode provides point-in-time inputs, hidden ground truth, and a task-specific this http URL compare three conditions: no skill, curated skill packages consisting of procedural documents and executable components, and self-generated skills in which the agent writes and reuses its own procedures within an episode. Across 9 models and a large-scale evaluation, curated skills consistently improve performance, raising mean scores from 0.366 to 0.528, with the largest gains in portfolio construction and risk management.
In contrast, self-generated skills provide little benefit despite higher computational cost. An independent evaluation using a separate agent framework (Hermes Agent, 8 models, 5,280 episodes total) reproduces the directional pattern across all three domains, with the magnitude of skill effects varying by subtask and harness.
These results showthat in investment management agents, access to reliable procedural skills can be as important as model choice, while naive self-generation of skills is often ineffective. We release the benchmark, evaluation tools, curated skill packages, and full trajectories to support further research.

---


### 16. [Computational Orientalism: Measuring Structural Discourse Bias in Large Language Models Using the Middle East Cultural Sensitivity Score (MECSS)](https://arxiv.org/abs/2608.18100)

**<font color=#1a73e8>作者：</font>** Maha Shahid  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI systems now shape how hundreds of millions of people learn about cultures other than their own. When someone asks one of these systems about the Middle East, they do not receive neutral facts. They receive a representation shaped by the frameworks embedded in training data, and that data is overwhelmingly Western and English-language. This paper asks whether that representation is Orientalist in Said's sense: whether it denies agency to Middle Eastern actors, treats Western frameworks as neutral while marking non-Western knowledge as particular, and explains the region through categories it did not produce. Standard fairness metrics cannot answer this, because they detect explicit prejudice rather than structural framing. This paper introduces the Middle East Cultural Sensitivity Score (MECSS), a framework that turns Said's seven Orientalist operations into measurable dimensions, and the term "Said-washing" for a specific failure: a model that disclaims generalization, then reproduces the structure it disclaimed. Across 280 conversations (1,120 exchanges), GPT-4 and Falcon3-7B-Instruct both reproduce Orientalist patterns systematically, through structural positioning rather than open stereotyping. GPT-4 scores moderately (mean MECSS 1.73); Falcon3-7B-Instruct scores higher (2.18), even though it was built in Abu Dhabi and trained with Arabic content. This is evidence against the assumption that building a model regionally makes it less Orientalist, though the models differ in size as well as origin, so geography cannot be isolated as the cause. Epistemic Center, the treatment of Western frameworks as unmarked universals, scores near the top of the scale for both models. Said-washing appears in 87.9% of GPT-4 conversations, a pattern existing metrics cannot see. Reducing this bias requires changing what models learn from, not only adding languages or relocating institutions.

---


### 17. [Stability-Aware Feature Design for Robust Watermark Detection in Machine-Generated Text](https://arxiv.org/abs/2608.18102)

**<font color=#1a73e8>作者：</font>** Sina Mansouri, Mohit Marvania, Abolfazl Safikhani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of large language models (LLMs) has intensified the demand for principled methods to distinguish human from machine-generated text. Watermarking provides a promising avenue, yet existing detectors exhibit sharp performance deterioration under multiple paraphrasing and when applied to shorter texts. We introduce Pattern Stability Score (PSS), a novel detection framework that leverages local statistical features and stability dynamics across paraphrased variants. Specifically, the proposed method combines global and local z-score features with higher-order statistics of run-length patterns, enriched by autocorrelation signals and stability scores computed over paraphrase depth. Numerical evaluations are performed on three benchmark datasets (PG-19, CNN/DailyMail, and WikiText) using multiple LLMs (Llama-3-8B, Qwen2-7B) and paraphrasers (Mistral-7B, Qwen2-7B, Gemma-7B), systematically stress-testing robustness under up to eight rounds of paraphrasing. Compared to prior z-score thresholding baselines and some state-of-the-art deep learning methods, our approach improves detection AUC (area under the receiver operating characteristic curve) by over 10-15 percentage points across different token lengths. Additionally, extensive cross-domain experiments demonstrate that a single universal classifier generalizes across different LLMs, paraphrasers, and text domains without retraining, maintaining above 87.8% AUC even when all components differ from training.

---


### 18. [DeepTCM1.0: A Multi-Expert AI Agent for Deciphering Mechanisms of Chinese Herbal Formulae Based on General Large Language Models](https://arxiv.org/abs/2608.18103)

**<font color=#1a73e8>作者：</font>** Wenxin Duan, Hanwei Wang, Zhongying Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Mechanistic elucidation of traditional Chinese medicine (TCM) compound formulas remains a central challenge in the modernization of TCM. Conventional approaches, including data mining and network pharmacology, are insufficient for achieving deep integration between classical TCM theory and modern scientific research. In addition, direct question-answering using general-purpose artificial intelligence large language models is limited by inadequate adaptation to TCM theoretical frameworks and susceptibility to reasoning hallucinations. Consequently, there is an urgent need to develop intelligent analytical methods aligned with the holistic principles of TCM. Objective: To establish a multi-expert intelligent agent framework integrating classical TCM theory with modern life sciences, thereby enabling systematic and interpretable mechanistic analysis of TCM compound formulas, with Guizhi Decoction serving as a representative validation case. Methods: The DeepTCM1.0 framework was constructed based on the general-purpose large language model DeepSeek V3.2. It adopts a three-tier collaborative architecture and a three-round iterative quality-control workflow, simulating the collaborative analytical process of 11 interdisciplinary intelligent agents. The framework was applied to the mechanistic interpretation of Guizhi Decoction from the dual perspectives of classical traditional Chinese medicine theory and modern scientific research. Framework performance was comprehensively evaluated through double-blind five-dimensional scoring, intraclass correlation coefficient (ICC) reliability testing, Mann-Whitney U tests, and effect size analysis. The evaluation employed four independent large language models as evaluators, each conducting five rounds of repeated scoring on five anonymized reports, resulting in a total of 100 independent scoring assessments.

---


### 19. [Self-Evolving Agents as Dynamic Graph Transformation: A Survey and New Perspective](https://arxiv.org/abs/2608.18104)

**<font color=#1a73e8>作者：</font>** Yuanyuan Xu, Wenjie Zhang, Yin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents are increasingly becoming self-evolving systems that persist across interactions, maintain memories, use tools, acquire skills, refine workflows, and coordinate with other agents. These capabilities make agent states structural and dynamic: entities, relations, attributes, dependencies, and execution structures change with new evidence, feedback, and environmental conditions. Existing graph-agent surveys typically treat graphs as support structures for agent functions rather than as evolving substrates, while self-evolving-agent surveys focus on agent-level mechanisms and rarely discuss graph topology evolution. Thus, the coupling between evolving agent state and dynamic graph topology remains underexplored. This survey connects these two research lines by framing \textit{agent evolution as dynamic graph transformation}. We model agent state as a dynamic graph, where memories, tools, skills, workflows, and inter-agent relations are represented as typed nodes, edges, and subgraphs updated through schema-constrained rewrites. Based on this formulation, we organize existing dynamic-graph-based methods for self-evolving agents into four taxonomies: node/feature evolution, edge/topology evolution, subgraph activation, and cross-component co-evolution. Building on this taxonomy, we propose dynamic graph learning as reusable infrastructure for self-evolving agents and map nine dynamic-graph-learning subfields to agent-evolution capabilities, discussing their adaptations and possible failure modes. Finally, we discuss five types of graph-aware evaluation and governance protocols from a dynamic-graph perspective, which complement end-task evaluation. The goal is to provide a compact structural lens for designing and governing self-evolving agents.

---


### 20. [StocksTalk: A Voice-Enabled Conversational Agent for Structured Query Generation over Web Data](https://arxiv.org/abs/2608.18105)

**<font color=#1a73e8>作者：</font>** Akshat Parmar, Vikranth Udandarao, Abhay Shakya 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> StocksTalk is a voice-enabled conversational system for transforming spoken financial screening requests into executable and validated structured queries over real-world market data. The system combines streaming speech recognition, retrieval-augmented constraint extraction, schema-grounded LLM-based SQL generation, rule-based validation, and human-in-the-loop verification within an interactive dashboard. Unlike traditional template-driven financial assistants, StocksTalk exposes intermediate reasoning artifacts, including extracted constraints, normalized financial metrics, operator grounding, and generated queries, allowing users to inspect and refine each stage before execution. To evaluate the system, we curate a benchmark of 150 spoken financial prompts spanning multiple investment strategies and input noise conditions. Experimental results show that retrieval grounding, constrained query generation, and interactive verification substantially improve constraint extraction accuracy, SQL executability, logical consistency, and multi-turn stability compared to baseline LLM-based approaches. StocksTalk demonstrates how transparent, voice-driven interfaces can bridge natural language interaction and structured financial analysis, providing an effective framework for conversational stock screening and decision support.

---


### 21. [Different Facets of Verbalised Overconfidence: an Interpretability Study](https://arxiv.org/abs/2608.18106)

**<font color=#1a73e8>作者：</font>** Davide Mazzaccara, Leonardo Bertolazzi, Raffaella Bernardi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models tend to overconfidence, giving assertive answers when the evidence suggests hedging or abstention. Using controlled reasoning scenarios that manipulate logical necessity and possibility, we study this behavior in Qwen3-4B, across three ways to express uncertainty: verbal epistemic markers, abstention, and numeric confidence scores. Our results confirm this tendency toward overconfidence, particularly when the model is prompted to output a numeric confidence score. At the interpretability level, we propose a method that differentially identifies transcoder features responsible for uncertainty and certainty. Our analysis reveals Qwen3-4B's default mechanism favors certainty generation through a broad coalition of shared features, while uncertainty is implemented as a sparse override mediated by a small set of dedicated features. Intervening on these uncertainty features both causally proves this imbalance underlying overconfidence and also mitigate overconfident errors. The same set of features generalise across the three uncertainty-expression settings, languages, and an out-of-distribution modality task.

---


### 22. [Institutional Prestige as Geographic Bias in Large Language Models: Evidence from Three Factorial Experiments with Bootstrap Confidence Intervals](https://arxiv.org/abs/2608.18107)

**<font color=#1a73e8>作者：</font>** Maikel Leyva-Vazquez, Florentin Smarandache  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate whether large language models (LLMs) systematically discriminate in candidate evaluations based on applicant name ethnicity and/or institutional prestige and geographic location. Three factorial experiments are reported (4,320 API calls, four LLMs, five professional domains). Study 1 (3x4 design) finds a statistically robust institution-tier gradient of +0.297 points on a 10-point scale (95% bootstrap CI: +0.175 to +0.422), while name-origin effects are negligible and non-significant (95% CI crosses zero). Study 2 (2x2 Prestige x Country design) breaks the prestige-geography confound: the prestige effect (+0.185; 95% CI: +0.093 to +0.275) exceeds the country-of-origin effect (+0.126; 95% CI: +0.037 to +0.218) by 1.5x. Study 3 (2x2 Journal x Institution design) reveals that journal prestige (Nature vs. a peripheral open-access journal) dominates institutional prestige by 5.7x: journal effect +1.937 (95% CI: +1.811 to +2.062) vs. institution effect +0.341 (95% CI: +0.184 to +0.504). A "rescue effect" is confirmed: publishing in Nature compensates for low institutional prestige more strongly for candidates from the University of Guayaquil (+2.127) than from MIT (+1.745). Results are quantified using the Neutrosophic Bias Index NBI<T,I,F>; the I component reveals elevated evaluation inconsistency for low-prestige profiles, an epistemic disadvantage not captured by mean-only metrics. Code and data: this https URL

---


### 23. [Same Facts, Different Updates: Inference Setup Shapes LLM Behavior in Medical Allocation](https://arxiv.org/abs/2608.18108)

**<font color=#1a73e8>作者：</font>** Spencer Gibson, Tyler Crosse, Magnus Saebo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are being incorporated into sensitive and important decision-making processes across nearly all fields. While prior work studies model bias around inputs and scenario framing, models can also behave in unexpected and undesirable ways due to context accumulated over their deployment. In this work, we study a medical example in which a model is asked to assign resource-allocation probabilities to two people given brief clinical context, and then sees the same scenario with a single extra sentence containing contrasting patient information, either with or without its previous response in context. Across three of four tested models, the paired-context and independent-inference experiments have different probability shifts, often in opposite directions (in favor of Person B vs. in favor of Person A) when new information is provided. We include additional paired-context experiments to show the effect of varying attributes across scenario axes. Our findings show the context-dependent effect of patient information in a sensitive medical use case. More broadly, our work shows the importance of carefully incorporating LLM-based systems into decision-making processes, context engineering, and further model behavioral studies.

---


### 24. [Solving Is Not Drawing: A Benchmark for Diagrammatic Reasoning in Olympiad Geometry](https://arxiv.org/abs/2608.18111)

**<font color=#1a73e8>作者：</font>** Hsien Xin Peng, Anthony Kim, Alvin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models such as GPT and Claude now solve olympiad-level mathematics with remarkable proficiency, so much so that geometry problem solving has become a standard proxy for their mathematical reasoning. Yet solving a geometry problem and drawing the figure it depends on are not the same skill: progress often hinges on a faithful diagram with the right auxiliary constructions and incidences, and it is unclear that a model which reasons its way to the answer can also produce one. A growing collection of benchmarks, including MathVista, and MathVerse, measures whether models reach the correct answer, but to our knowledge, none isolate the distinct ability to construct the diagram itself, leaving this capability unmeasured. We introduce an open-source benchmark that targets this gap: 954 self-contained olympiad geometry problems, with a 297-problem hard subset, each paired with its solution and a human-authored, high-fidelity diagram in renderable Asymptote code, together with a suite of text-, code-, image-, VLM-, and constraint-based metrics for what we term diagrammatic reasoning. Evaluating current foundation models reveals a pronounced gap between solving and drawing: their diagrams are markedly less faithful, with an average compile success rate of only 36.14\%. Strong mathematical reasoning, we find, does not imply the ability to construct accurate geometric diagrams. Our benchmark and dataset can be accessed at this https URL.

---


### 25. [Accurate Decoding of Natural Sentences from Non-Invasive Brain Recordings](https://arxiv.org/abs/2608.18114)

**<font color=#1a73e8>作者：</font>** Mingfang Zhang, Jarod Lévy, Cedric Rommel 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Restoring communication for people who have lost the ability to speak or move after a brain injury is a major challenge. While intracranial implants now enable high-performing brain-computer-interfaces, non-invasive alternatives are still lagging behind. Here, we present Brain2Qwerty v2, a model that can decode the production of natural sentences solely from real-time magnetoencephalography (MEG) recordings. By collecting 22,000 sentences typed by nine subjects, each recorded for 10 hours, our model leverages character, word and sentence-level representations to achieve an average word error rate (WER) of 39%. For our best participant, the model accurately decodes half of the sentences with one word error or less. Critically, decoding accuracy log-linearly improves with data volume, suggesting that the performance gap with intracranial approaches could be partially bridged through data scaling. We show that AI enables this performance in three main ways: the substitution of hand-crafted pipelines for event detection with deep learning, the finetuning of large language models to extract semantic representations, and the deployment of AI agents to iteratively refine our decoding pipeline via automated code development. Together, these results show that non-invasive brain-to-text decoding starts to operate at a level of accuracy previously thought exclusive to surgical implants, opening a path toward safe and efficient brain-computer-interfaces.

---


### 26. [Temporal Multi-Signal Fusion for Token-Level Hallucination Detection](https://arxiv.org/abs/2608.18115)

**<font color=#1a73e8>作者：</font>** Igor Itkin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Token-level hallucination detectors score each token independently from a single signal, and fail exactly when the generating model is confidently wrong. This paper instead treats hallucination as a temporally extended span and detects it by sequence labeling: each token is scored from a 33-dimensional feature stream that fuses text statistics, Natural Language Inference (NLI) entailment, and language model surprisal, with no access to model internals. A Bidirectional Gated Recurrent Unit (BiGRU) over these features reaches an AUC of 0.840 on RAGTruth (10 seeds), an 11-point gain over an independent logistic-regression baseline (p = 0.002, Wilcoxon signed-rank). A controlled decomposition attributes most of the gain to temporal order rather than model capacity: evidence propagates from confident positions to ambiguous neighbors within a span. The same 0.845 ceiling recurs across recurrent, state-space (Mamba), and attention architectures, locating the bottleneck in the feature set rather than the model. Because it reads only the generated text and external signals, the detector works on closed-source models, and it keeps working on text produced by language models it never saw during training, losing under 4% AUC.

---


### 27. [You Are What You Prompt: Prompt Quality, Domain Shift, and Uncertainty in Agrifood Vision-Language Models](https://arxiv.org/abs/2608.18116)

**<font color=#1a73e8>作者：</font>** Andrea Morales-Garzón, Salvador López-Joya, Miguel López-Pérez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models enable zero-shot classification through natural language prompts, but performance is sensitive to prompt formulation, especially in specialized domains. Zero-shot Prompt Ensembling (ZPE) addresses this by weighting prompts by discriminative signal, yet its behavior under domain shift remains unexplored. We evaluate ZPE in the agrifood domain using CLIP and SigLIP across four datasets and four prompt pools, spanning in-distribution (ID) food and out-of-distribution agricultural benchmarks. ZPE provides limited benefit under ID conditions but substantially improves performance and calibration under domain shift, where domain-specific pools of 51-52 prompts consistently outperform generic pools of 247-426. Lexical analysis shows that ZPE acts as an unsupervised domain-alignment detector without label access. We further introduce PID (Prompt-based Inconsistency Detection), which repurposes prompt disagreement as epistemic uncertainty, improving failure detection under severe domain shift where standard confidence measures collapse.

---


### 28. [Alignment Is All You Need: Instruction-Free Training for General Audio-Language Models](https://arxiv.org/abs/2608.18132)

**<font color=#1a73e8>作者：</font>** Xuanru Zhou, Yiwen Shao, Jiahong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are typically built through a multi-stage pipeline consisting of cross-modal alignment, supervised fine-tuning (SFT), and preference optimization. This pipeline assumes that adapting an LLM to a new modality requires extensive task-specific supervision. However, pretrained LLMs already possess strong reasoning and instruction-following abilities. As LLMs evolve rapidly, an important question remains: can we efficiently transfer these capabilities to a new modality with minimal intervention, and is alignment alone sufficient for building a multimodal model? We introduce an Instruction-Free Alignment-Only large audio-language model (LALM) that keeps both the audio encoder and the LLM fully frozen, learning only a lightweight projector. Borrowing insights from AzeroS [1], we train on (audio, response) pairs from Self-Generated Data Construction, where an LLM expands captions into free-form responses without explicit task instructions. Across MMAU, MMAR, MMSU, and MMAU-Pro, our approach matches or surpasses heavily post-trained baselines using substantially less data. By keeping the LLM frozen, our model preserves its native instruction-following competence and can port seamlessly across model generations. Our results suggest that competitive MLLM can emerge from alignment alone, reducing multimodal extension to a lightweight projector-training problem that generalizes across modalities and adapts rapidly to each new LLM release.

---


### 29. [Language Models for Portuguese: A Systematic Mapping Study](https://arxiv.org/abs/2608.18138)

**<font color=#1a73e8>作者：</font>** Jhessica Silva, Carlos Caetano, Helena Maia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, the rapid development of language models has transformed the field of Natural Language Processing through a wide range of applications. However, the development of language models has not progressed uniformly across all languages. In the case of the Portuguese language, there has recently been a growing effort by academia and companies to develop language models and create data resources for Portuguese. These efforts have resulted in the rise of an increasingly diverse ecosystem of language models for Portuguese. However, information on these models remains dispersed in scientific publications, technical reports, model repositories, and project documentation. This survey presents a systematic mapping study of language models developed for Portuguese, providing a comprehensive overview of the current state of the field. We map a total of 46 models, characterizing them by various aspects, including base model, architecture, computational resources, training datasets, licensing, code availability, data, and model weights. Furthermore, we analyzed the evolution and relationships among these models through a phylogenetic perspective, identified current research gaps and opportunities, and discussed future directions for the development of language models for Portuguese.

---


### 30. [Efficient Adaptation of LLMs for Hate Speech Detection in Low-Resource Languages: A Comparative Study on Roman Urdu](https://arxiv.org/abs/2608.18142)

**<font color=#1a73e8>作者：</font>** Toneema Zubair, Muhammad Junaid Asif, Faisal Kamiran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> It is challenging to detect hate speech in Low Resource Languages (LRLs) because of the absence of annotated data, the informality of its language structure, and the lack of standardized grammar. A good example of such a challenge is Roman Urdu which is broadly used by South Asians on social media and has a high variation while lacking contextually consistent spellings. The objective of this paper is to conduct a comprehensive assessment of Large Language Models (LLMs) for Hate Speech Detection (HSD) in Roman Urdu script and fine-tune these models using the Parameter-Efficient Fine-Tuning (PEFT) method called Low-Rank Adaptation (LoRA). To evaluate zero-shot inference, we benchmarked it against PEFT on different transformer models, including Mistral, LLaMA, Falcon, and multilingual BERT. Experiments are conducted on the PURUTT (Parallel Urdu and Roman Urdu Corpus for Toxic Comments and Transliteration) dataset with over 72,000 annotated comments. The results suggest that zero shot models perform moderately (F1 = 0.56), but updating a small fraction of the model trainable parameters improves the classification performance significantly (F1 > 0.93). Our results have shown that PEFT delivers outstanding performance alongside excellent computational efficiency, making it highly suitable for low-resource language processing tasks.

---


### 31. [The Deontic Gap: Large Language Models and the Modal Language of Obligation](https://arxiv.org/abs/2608.18144)

**<font color=#1a73e8>作者：</font>** Daniel Hart, Sarah Allred, Joseph Abbas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modal auxiliaries such as must, should, and have to mark necessity and obligation within the contexts of speaker authority and interpersonal stance. We examine whether large language models (LLMs) reproduce contemporary human patterns of deontic modal usage. Across three primary corpora, an external benchmark, two controlled replications, and a naturalistic eleven-model replication, AI-generated text consistently underuses positive deontic modals (must, should, have to, had to) relative to contemporary humans. Historical comparison with the Google Books Ngram corpus (1920-2022), used as a heuristic calibration against the published-prose record, shows that AI modal frequencies fall within the range of formal published English, whereas contemporary human modal rates in informal digital contexts often exceed twentieth-century book baselines. Phrase-level decomposition shows that the AI-human modal gap is concentrated in constructions central to interpersonal stance (should, have to, had to), while AI matches or exceeds humans on need to in instructional and question-answering contexts but not in persuasive student writing, indicating that the modal profile is genre-conditional. The findings suggest that LLM modal usage reflects the formal written resources on which these models were trained, while underusing the modal constructions through which contemporary human writers mark immediate, interpersonal obligation.

---


### 32. [When Do LLMs Actually Help? Evaluating LLMs as Data Quality Annotators](https://arxiv.org/abs/2608.18158)

**<font color=#1a73e8>作者：</font>** Praphulla Lal Shrestha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs have been increasingly used to catch data quality issues automatically, but we know very little about how consistent these judgments actually are. This study tests an LLM on two e-commerce data quality tasks, entity matching and brand mislabeling, against rule based baselines and human verified ground truth, under both zero-shot and few-shot prompting. On entity matching while using the Abt Buy benchmark (2,194 labeled pairs), a simple rule based baseline (F1=0.950) performed about as well as LLM zero shot prompting (F1=0.948). Moreover, a few-shot prompt revision that looked effective on a small validation sample reduced full-scale performance to F1=0.914. This showed that small sample prompt evaluation can be misleading. On brand mislabeling detection, using 500 Amazon product listings with synthetically injected labeling errors, the LLM clearly outperformed a naive rule based baseline (F1=0.833 vs 0.721), because it could draw on background knowledge of brand product relationships that a simple rule could not access. Testing consistency across repeated runs (200 pairs, 5 runs at temperature 0.7) showed the model agreeing with itself 99.7% of the time on average, with 99% of pairs giving identical answers across all 5 runs. Using majority voting across these runs only improved F1 by 0.005, at 5 times the inference cost. These results suggest that the value of using an LLM over traditional methods depends heavily on the task. LLMs offer little advantage when strong lexical signals already exist, but a clear advantage when the task requires background knowledge, all while remaining highly consistent across repeated queries.

---


### 33. [Are LLMs Safe Beyond Text: Do Emojis Expose Gaps in Safety Evaluation](https://arxiv.org/abs/2608.18164)

**<font color=#1a73e8>作者：</font>** M P V S Gopinadh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety evaluations of large language models (LLMs) predominantly rely on text-based adversarial prompts, potentially overlooking vulnerabilities arising from alternative input representations. This work examines emoji-augmented prompts as a test case for this gap, evaluating 50 prompts across four open-source LLMs (Mistral 7B, Qwen 2 7B, Gemma 2 9B, Llama 3 8B). Results show substantial variation in robustness: Gemma 2 9B and Mistral 7B exhibit non-zero success rates (10%), Llama 3 8B 6%, while Qwen 2 7B shows complete resistance (0% success rate). A chi-square test ($\chi^2 = 32.94, p < 0.001$) confirms significant differences in outcome distributions. These findings indicate that robustness is sensitive to input representation, and that evaluations restricted to standard text prompts may underrepresent model vulnerabilities.

---


### 34. [Adversarial Review: Structured Disagreement for Grounded Agentic Code Review](https://arxiv.org/abs/2608.18167)

**<font color=#1a73e8>作者：</font>** Eric S. Qiu, Joyce Gill  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early multi-agent LLM systems often used role-separated teams, yet scaling agent count yields diminishing returns on repository-level coding tasks. Recent alternatives treat agents as passive tools (subagents), yet this removes the benefits of agent interaction entirely. We study whether a subagent paradigm can support a middle ground: minimal agentic cooperation without the overhead of large multi-agent teams. We introduce Adversarial Review (AR), a minimal cooperative code-review protocol in which a main coding agent works with a reviewer and a critic agent. The reviewer evaluates code, while the critic audits the review through structured disagreement before the main agent edits. On LiveCodeBench, AR achieves the highest pass rate among tested methods, outperforming a five-agent baseline while using only three agents. On SWE-PRBench, naive AR exposes a false-consensus failure mode, where agents converge on agreement without sufficient evidence, but a single prompt iteration that adds disagreement explicitly achieves the highest F1 among tested methods. On SWE-bench Verified, AR also shows improvements over the baselines on repository-level coding tasks. Together, AR demonstrates that cooperative code review does not require many agents or complex communication structures: it requires that disagreement be minimal, structured, and evidence-grounded.

---


### 35. [Looped Language Models Improve Compositional Tool Calling](https://arxiv.org/abs/2608.18171)

**<font color=#1a73e8>作者：</font>** Andrei Cristian Popescu, Haitz Sáez de Ocáriz Borde, Pietro Liò  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Looped language models have shown promising results on reasoning benchmarks, yet their potential for agentic tool use remains largely unexplored. We study this question in compositional tool-calling settings, where models must coordinate multiple API calls, maintain intermediate state, and preserve dependencies across tool interactions. We evaluate native and retrofitted looped language models on API-Bank, BFCL, and NESTful, comparing looped and non-looped models trained under matched supervised fine-tuning recipes and varying recurrent depth at inference time. In controlled experiments, recurrent computation generally benefits compositional and dependency-aware tool use, while providing smaller and more model-dependent gains on isolated API invocation. Accuracy on multi-step tool use generally increases with recurrent depth; adaptive inference, however, achieves a more favorable compute-performance trade-off by allocating additional computation only when needed. Our results suggest that looped language models are a promising architecture for agentic systems that require reliable planning, coordination, and execution of compositional tool use workflows.

---


### 36. [Efficient INT8 Inference of Small NLP Models on Server CPUs with PyTorch Native Stack](https://arxiv.org/abs/2608.18182)

**<font color=#1a73e8>作者：</font>** Weiwen Xia, Yuxin Cui, E Cao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small NLP models, especially BERT-family encoders, remain important in industrial workloads such as classification, ranking, and retrieval even in the era of large language models. On server CPUs, INT8 quantization offers an attractive latency-throughput-cost trade-off, but users increasingly expect such acceleration to be available directly in the native PyTorch stack. We integrate SmoothQuant into TorchAO and optimize the resulting inference path for Intel Xeon CPUs through graph-level fusion in TorchInductor and efficient INT8 GEMM kernel selection across oneDNN-, AVX512_VNNI-, and AMX-based implementations. Across BERT, DistilBERT, and XLM-RoBERTa benchmarks, the approach delivers up to 5.8x end-to-end throughput speedup with negligible---and in some cases no measurable---accuracy loss relative to the FP32 baseline. We also validated our work by detailed performance analysis with roofline models. The implementation has been upstreamed to PyTorch and TorchAO, enabling out-of-the-box deployment with native PyTorch tooling

---


### 37. [Accelerating Visual On-Policy Distillation with Batched Speculative Jacobi Rollouts](https://arxiv.org/abs/2608.18183)

**<font color=#1a73e8>作者：</font>** Bingqi Shan, Zhehao Yu, Kenhong Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual on-policy distillation (OPD) improves the training of compact visual autoregressive models by learning from trajectories generated by the current student. However, these online rollouts are still produced token by token with autoregressive decoding, which adds substantial cost to every on-policy training step. Speculative Jacobi Decoding (SJD) provides an alternative because it can process multiple tokens in parallel without an auxiliary draft model, but the original method is designed for single-sequence inference. We introduce HB-SJD, a batched SJD rollout backend for visual OPD. HB-SJD allows each image to advance independently according to its own decoding progress, while images at different sequence positions are still verified in batched model forwards. As images finish, HB-SJD switches between Full and Compact execution to reduce the cost of later rollout rounds. HB-SJD only replaces the student rollout backend and leaves the teacher, distillation objective, and optimization procedure unchanged. Experiments with LlamaGen show that HB-SJD substantially reduces rollout and end-to-end training time while preserving the generation quality of the distilled student.

---


### 38. [Allocating Recurrent Compute in Looped Language Models](https://arxiv.org/abs/2608.18230)

**<font color=#1a73e8>作者：</font>** Ruhai Lin, Yiyang Guo, Rui-Jie Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models improve reasoning and knowledge manipulation by applying shared computation repeatedly. Existing systems usually repeat an entire layer stack, although a mixer and a dense feed-forward network (FFN) perform different operations and have different costs. We ask a narrower question: what should loop? We view recurrence as repeated composition of a state update and argue that an application is valuable when it exposes a new cross-position influence direction that remains observable at the task readout. Iterative Transport Rank (ITR) describes the cumulative influence trajectory; marginal ITR describes the nonredundant influence contributed by successive applications. This view motivates MixerLoop, which repeats each Gated DeltaNet mixer while applying its dense FFN once. We compare MixerLoop with no recurrence and full-block recurrence at 15M and 110M parameters under the same data, initialization, and architecture. A finite context-off intervention tests whether later mixer applications produce distinct, non-negligible, and beneficial changes at the final language-model readout. MixerLoop surpasses FullLoop on aggregate CORE at 15M and retains 41.5% of its CORE improvement at 110M while reducing recurrent-backbone projection FLOPs by 45.9%. These results show that the benefits of recurrent depth can be retained without repeatedly executing the dense FFN.

---


### 39. [Contracting for LLM Delegation: Moral Hazard in Technology and Effort Choice](https://arxiv.org/abs/2608.18232)

**<font color=#1a73e8>作者：</font>** Nanda Kishore Sreenivas, Kate Larson  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We extend the standard Principal-Agent framework to scenarios where the Agent selects from a suite of technologies, each characterized by a distinct cost-capability profile. This framework is increasingly critical in the era of Large Language Models (LLMs), where Agents choose both a model and an associated effort level (e.g., token budget). We model the relationship between output quality and effort as a concave, saturating function, which depends on the Agent's hidden two-dimensional action choice balancing technology selection and effort allocation. We derive the optimal linear contract for the Principal, demonstrating that the Agent's best response is characterized by a threshold reward share that triggers technology switching. Finally, we calibrate our model using open-weight LLM pairings across the MATH and MMLUPro benchmarks. We show that both Principal and Agent, when employing bandit algorithms to navigate this environment, converge to strategies that closely align with our theoretical equilibrium. These results suggest that simple linear contracts can effectively incentivize complex, technology-aware delegation in agentic workflows.

---


### 40. [ClosureBench: A Constructive Benchmark for Compositional Graph Reasoning](https://arxiv.org/abs/2608.18242)

**<font color=#1a73e8>作者：</font>** Stefano Goria  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce ClosureBench, a constructive benchmark for compositional graph-relational reasoning with programmatically verified ground truth. Unlike fixed-test-set benchmarks vulnerable to data contamination, ClosureBench generates instances on demand: each task's reference answer is computed by executing a program in the Ein tensor-logic language, ensuring machine-verified correctness. The benchmark spans 26 task categories at three compositional levels (L1-L3), with difficulty controlled along three independent axes: graph size, edge density, and query depth.
We evaluate models from 1.5B open weights to frontier systems (o3, GPT-4.1, Gemini 2.5, Claude Sonnet 4) and report three findings. First, because the benchmark can always supply fresh instances, it measures memorisation directly: a model fine-tuned on a fixed test set shows a 19.3 percentage-point gap between its accuracy on seen and on fresh instances, which a static test set cannot reveal. We scope this to supervised fine-tuning on answer pairs, not pretraining contamination. Second, accuracy falls as graph size and query depth increase, and the two interact: models misread the graph from its natural-language description and then reason correctly over the wrong graph, so even the strongest frontier model degrades from atomic to compositional queries. This bottleneck is a property of the reasoning rather than the input format: it persists when the graph is given as a JSON edge list or an adjacency matrix instead of prose. Third, a 4B model fine-tuned to emit executable programs rather than answers stays nearly flat across compositional levels and approaches frontier accuracy (94.3% on held-out instances) at a fraction of the token cost. This holds for two program targets, Ein and Python+NetworkX, so it is a property of verified program synthesis rather than of one language.

---


### 41. [Redakto - The Incognito Tab for LLMs](https://arxiv.org/abs/2608.18260)

**<font color=#1a73e8>作者：</font>** Saurav Kumar Saha, Tom Röhr, Felix Bießmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are being increasingly used in everyday applications. A major challenge in the context of LLMs or Artificial Intelligence (AI) in general is to ensure privacy when using them, meaning that personally identifiable information (PII) is removed from any text that enters an LLM. These challenges have become more urgent with novel EU legislation. Uncertainty around LLM usage with respect to privacy concerns in EU countries can be a major blocker for the speed of innovation and transfer from research to applications. Here we present \textbf{Redakto}, a tool that can be used for anonymizing text prior to feeding it to an LLM or other downstream text processing. We provide state-of-the-art functionalities for both redaction of PII but also when used for pseudonymization. These functionalities are exposed such that they can easily be used by end-users, through the Redakto web application, and by developers and researchers, via REST APIs and model context protocol (MCP) hooks. The implementation is fully open source, requires modest compute resources, and can be readily deployed on local hardware. In contrast to prior work and in order to better assess the quality of the anonymized texts, we conduct extensive empirical evaluations on textual data from legal and medical domain with respect to both privacy and utility of the redacted texts. Our empirical results demonstrate that the texts anonymized with different redaction strategies achieve utility scores on par with the original texts, suggesting that anonymization with Redakto can be used for LLM tasks without substantial negative impact for the tasks we explored.

---


### 42. [Cacheable by Design? Training Mixture-of-Experts Routers for Locality Against the Edge Memory-Bandwidth Wall: A Pre-Registered Negative Result with a Systems Measurement Study](https://arxiv.org/abs/2608.18261)

**<font color=#1a73e8>作者：</font>** Shriniwas Ramesh Suram  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Serving a 235B-parameter Mixture-of-Experts (MoE) model on a single 8 GB GPU is bottlenecked not by compute but by memory bandwidth: decode must stream each token's active experts from whichever tier holds them, and on consumer hardware most experts sit on an SSD far slower than RAM. We quantify this bandwidth wall on Qwen3-235B (Q4_K_M, 134 GB): measured decode is 0.44 tok/s warm, matching a bytes-per-token / bandwidth model, while a batching scheme that should amortize one disk sweep instead collapses at batch 32 from paging thrash. We build llama-moe-trace, a zero-surgery router-telemetry tool, and measure routing on Qwen3-30B: adjacent-token expert reuse is 2.0x chance, 95% of traffic uses 52.5% of experts, and an LRU cache of 13.4% of experts serves 66% of requests. We then ask whether cacheability is trainable: we pre-register training of 137M MoE language models with auxiliary locality and domain router losses, under joint criteria on cache-miss reduction and perplexity. The mechanism works (misses down up to 60%; a 99% static-pin hit rate) but every configuration fails the pre-registered <=1% perplexity gate -- miss reduction and quality are tightly coupled. Concurrent StickyMoE reports the same loss as near-free on single-domain sub-25M models; on multi-domain 137M we find the tax real. Our contribution is this pre-registered, stricter-criterion, multi-domain evaluation plus edge-serving measurements. A 340M rung shows the tax does not shrink with scale (it rises slightly). We further show training-free cache-aware rerouting stacks with trained locality -- together ~80% miss reduction at <=3.4% perplexity at both sizes, far cheaper than either alone -- while domain-primed prefetching does not help. All code, traces, and the pre-registration are released.

---


### 43. [SIGMA: Symmetry-aware, Intelligent, Geometric, Multi-objective Adaptive Control for Robust, Dependable Traffic Management](https://arxiv.org/abs/2608.18263)

**<font color=#1a73e8>作者：</font>** Pratham Payra, Jagadish B, Tanmay Sen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic signal control is a complex sequential decision-making problem requiring real-time adaptation and trade-offs among throughput, delay fairness, signal stability, and emergency vehicle priority. Existing RL methods often fix objectives, ignore dynamic priority changes, and fail to generalize across geometrically similar this http URL propose SIGMA (Symmetry-aware, Intelligent, Geometric, Multi-objective Adaptive traffic control), an RL framework enhanced with a large language model (LLM) for adaptive objective tuning and orientation-invariant learning. SIGMA converts natural-language emergency commands into priority vectors for a multi-objective actor-critic controller, avoiding manual reward engineering. Rotational augmentation improves transferability across four-way intersections, while offline-to-online learning ensures stable initialization and gradual adaptation to changing this http URL define reliability properties covering emergency service levels, graceful degradation under LLM failures, and demand sensitivity, validated via bootstrap statistics. Evaluated in SUMO on four Kolkata-based urban intersections against fixed-time, actuated, and DQN controllers, SIGMA reduces average/emergency waiting times and queue lengths, and boosts throughput. Ablation studies confirm robustness to component failures and geometric rotations. Overall, SIGMA offers a reliable, language-guided, multi-objective traffic control system with statistical reliability assurance.

---


### 44. [Rethinking Privileged Information in On-Policy Self-Distillation](https://arxiv.org/abs/2608.18271)

**<font color=#1a73e8>作者：</font>** Samyak Shrestha, Alexander Tessier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) trains a student on its own responses using token-level supervision from the same model conditioned on privileged reference information. We investigate whether performance gains from OPSD show that the student learned the information in the reference or instead reflect recovery of reasoning behavior already present in the base model. We perform OPSD experiments on science and mathematics datasets using Qwen3 models ranging from 1.7B to 8B. Our analysis framework separates the supervision induced by the reference from the supervision provided by the teacher without the reference and measures how each aligns with changes in the student's predictions. The correct reference does not provide a consistent performance benefit across teacher generation modes, model sizes, and training datasets. Students can improve without the correct reference, and a solution from another problem can outperform the correct solution on several mathematical reasoning benchmarks. The student's predictions align more strongly with the base model's thinking behavior than with the supervision induced by the reference, but controls constructed from other problems reproduce much of both alignments. Moreover, stronger alignment attributable to the correct reference does not reliably coincide with a greater performance benefit from the reference. Performance gains and distributional alignment alone therefore cannot determine how privileged reference information contributes to student learning in OPSD.

---


### 45. [Evaluating Structured Information Extraction with Open Models in a High Risk Public Sector Application](https://arxiv.org/abs/2608.18289)

**<font color=#1a73e8>作者：</font>** Elias Schubert, Felix Bießmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The extraction of structured information from unstructured documents represents a critical component of digital transformations in all sectors. While proprietary solutions dominate commercial applications, a rapidly growing ecosystem of open-source Optical Character Recognition (OCR) engines, Large Language Models (LLMs), and Vision-Language Models (VLMs) offers accessible alternatives. However, systematic evaluations on realistic, multi-step extraction pipelines remain scarce. Responsible usage of such extraction tools require comprehensive evaluations on realistic tasks, especially as these solutions will be key components of applications in the public sector that the EU AI act categorizes as high risk. To address this gap we present a comprehensive benchmark assessing the end-to-end performance of open-source systems on a complex real-world document processing task classified as high risk: Student applications for an international study program. We conduct a comprehensive empirical evaluation with state-of-the-art OCR engines, LLMs and VLMs. Our results reveal that while VLMs generally outperform OCR+LLM pipelines, even state-of-the-art open-source models struggle to handle such tasks reliably in zero-shot settings. Only 4 of 35 configurations achieved F1 scores above 0.5, with the best OCR+LLM pipeline matching top VLM performance, though most OCR+LLM combinations performed substantially worse. Roughly 75\% of all configurations scored below 0.25. Model scale influences performance, yet the relationship is non-linear: substantially larger models do not guarantee proportionally better results. Input quality, particularly the structural preservation of OCR output, emerges as a critical factor independent of downstream model capability.

---


### 46. [The Lifecycle of LLM-as-a-Judge for Large-Scale Recommendation Explanations](https://arxiv.org/abs/2608.18300)

**<font color=#1a73e8>作者：</font>** Emma Yanyang Kong, JJ Tan, Ishan Gupta 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge, which leverages a large language model to evaluate natural language generated by another AI application or model, has become a standard, scalable approach for accelerating and extending costly human evaluation. However, most work treats a judge as a static artifact, evaluating it once at construction or against a fixed benchmark. In contrast, we argue that an LLM judge running in a production system is better understood as having a lifecycle: it must be built, trained, deployed, and continuously maintained as the surrounding data evolves, and each phase poses distinct technical and operational challenges.
We present such a lifecycle for the LLM judges that evaluate user-facing recommendation explanations at Netflix, where our pipeline generates and the judges assess hundreds of thousands of distinct show-level explanations per week, served across the mobile experience to millions of members. Our framework has four phases: (I) Birth, defining multiple evaluation criteria and building curated benchmark datasets with human labels and rationales; (II) Training, refining the judges' rubrics via Reasoning-Aligned Rubric Tuning (RART), a rubric-tuning procedure that uses a meta-judge over reasoning output as the learning signal; (III) Deployment, in which one judge serves two production roles: quality gating and reflective generation; and (IV) Monitoring, a continuous Human-in-the-Loop alignment process that detects drift and triggers re-tuning behind a human review gate. We report post-launch results from a five-week A/B test over tens of millions of members, in which the judge-aligned explanations shifted member viewing toward novel content (previously unwatched) and increased successful browse-to-play sessions relative to a no-explanation control, with no quality-related takedowns.

---


### 47. [SESSE: Sketch, Expand, Sort, Summarize, Evaluate -- LLM-as-Judge Evaluation via Structured Decomposition](https://arxiv.org/abs/2608.18303)

**<font color=#1a73e8>作者：</font>** Dae Lee, Mihai Delgeanu, Adel Youssef  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-judge evaluation reduces response quality assessment to a single holistic A/B preference choice, providing no mechanism to isolate which quality dimensions drove the preference or distinguish model errors from genuine label ambiguity. We propose SESSE (Sketch, Expand, Sort, Summarize, Evaluate), a training-free framework that decomposes holistic judgment into structured sub-questions mined directly from the judge's own error cases; requiring no oracle responses, task-specific rubrics, or fine-tuning. On RewardBench (n=1,000), SESSE achieves near-parity with the chain-of-thought baseline and is competitive with RISE-Judge-32B (92.7%), a fine-tuned specialist, while remaining fully training-free. Per-criterion vote evidence provides an interpretable audit trail for diagnosing label ambiguity and judge failure modes unavailable from a single holistic output token.

---


### 48. [ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents](https://arxiv.org/abs/2608.18307)

**<font color=#1a73e8>作者：</font>** Tianchen Guan, Xinlei Lin, Royce Cheng-Yue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current evaluation of computer-use agents is split between long-horizon workflow benchmarks and atomic GUI-grounding tests. This leaves an under-instrumented middle layer: realistic component-centered interactions (e.g., toggle a button set) that are short enough to diagnose and rich enough to capture the burdens of modern interfaces. We present ComponentBench, a benchmark and diagnostic pipeline for component-level evaluation of computer-use agents on modern web UIs. ComponentBench is organized around a library-agnostic ontology of 97 canonical UI components instantiated as 2,910 programmatically verified tasks across widely used component libraries, paired with cleaned human reference trajectories that enable evaluation of both task success and interaction efficiency. Beyond task collection, we introduce a scalable pipeline for auditing realized structural difficulty after implementation and synthesizing structured failure analyses across tasks and component families. Evaluating seven models -- GPT-5.4, Gemini 3 Flash, GPT-5.4 mini, GPT-5 mini, Gemini 3.1 Flash-Lite, Qwen3-VL-235B, and UI-TARS-1.5-7B -- across four observation and action spaces, we show that these design choices critically impact performance. Within a single shared harness, changing only the observation and action space shifts task success by more than 30% for the same model: GPT-5 mini falls from 83.1% with accessibility-tree observations to 48.9% with coordinate-only Pixel control. Moreover, even the fastest configuration takes 3.7x as long as the matched human reference, and spatial manipulations that are trivial for humans continue to challenge current agents.

---


### 49. [XRF-to-Optical Field-of-View Localization with Vision Language Models](https://arxiv.org/abs/2608.18309)

**<font color=#1a73e8>作者：</font>** Xiangyu Yin, Tatjana Paunesku, Letonia Copeland-Hardin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Registering images acquired with different microscopy modalities is essential for relating complementary measurements of the same specimen. In correlative X-ray fluorescence (XRF) and optical microscopy, the XRF map often covers only a small region of an optical image acquired from the same or an adjacent tissue section. Field-of-view (FOV) localization is necessary but can be difficult when appearance and structure differ across modalities. Here we evaluate training-free vision language model (VLM) localization on two datasets representing same-section high-correspondence and adjacent-section low-correspondence imaging. We test unconstrained and metadata-constrained search and compare VLMs with geometric controls, classical template matching, and two alternative training-free approaches (DINOv2 and multiGradICON). Direct VLM prompting produced content-dependent spatial signals but was not reliable alone. Classical matching was most accurate when cross-modal structure was preserved but failed in the low-correspondence collection. A proposal-and-verify workflow used repeated VLM predictions as candidates and image-based similarity to select the final location. This workflow recovered useful localization in the low-correspondence regime.

---


### 50. [Governance Records as Supervision: Verifier-Selected Self-Training for Structured Workflow Repair](https://arxiv.org/abs/2608.18324)

**<font color=#1a73e8>作者：</font>** Jesus Salas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine-verifiable workflows produce governance records linking a task contract, model attempt, verifier decision, accepted output, and target origin. We test whether these records can supervise bounded models, consolidating occasional or expensive capability into reliable one-shot execution.
On fresh, structure-disjoint PlanBench replanning cases, Qwen3-14B thinking generated 24 plans admitted by the independently authored VAL verifier. Those plans trained the same checkpoint for non-thinking execution, without oracle targets or a stronger teacher. On 80 unopened cases, VAL-accepted plans increased from 1 to 57, with 56 paired gains and zero regressions; thinking reached 30. The adapter was schema-valid on all cases and used approximately 1/56 of thinking's mean latency. The separate paired interface-cure gate did not pass.
A matched ablation fixed the source cases, 52-candidate pool, 24-target count, model, recipe, and seed while changing target selection. On 160 new cases, base, schema-selected, model-self-selected, and VAL-selected execution reached 1, 55, 69, and 102 accepted plans. VAL exceeded self-selection by paired net +33 (p=0.0000019647), with gains in both difficulty strata. Independent semantic selection is therefore load-bearing relative to matched alternatives within this band.
A complementary Phi stronger-teacher arm raised base Phi-4 from 2 to 51 accepted plans and from 35 to 80 schema-valid outputs. Earlier synthetic experiments establish teachability, cumulative learning, construction robustness, and stopping boundaries. The results support verifier-selected supervision for bounded, machine-checkable capabilities, not arbitrary planning, enterprise validity, or unrestricted self-improvement.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-166](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
