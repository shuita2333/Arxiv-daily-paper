# 🧠 大模型相关研究 | 2026年07月06日

> 本类共 **136** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-136](./part-03.md)

---

### 1. [TokenScope: Token-Level Explainability and Interpretability for Code-Oriented Tasks in Large Language Models](https://arxiv.org/abs/2607.01235)

**<font color=#1a73e8>作者：</font>** Amirreza Esmaeili, Fatemeh Fard  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding how Large Language Models (LLMs) make token-level decisions during code generation remains a major challenge for both researchers and practitioners. While recent tools provide insights into model internals or generation outcomes, they often lack decoding-time signals, fine-grained uncertainty measures, and interactive mechanisms for exploring alternative generation paths. We present TokenScope, an interactive interpretability and analysis tool for decoder-based LLMs that exposes token-level metrics, attention patterns, and structural information during generation. TokenScope supports interactive token replacement, counterfactual branching, and code-aware aggregation via abstract syntax trees. By unifying decoding-time signals with structural program analysis, TokenScope enables systematic investigation of LLM behaviour during code generation.

---


### 2. [Safeguarding LLM Agents from Misalignment through Provenance Analysis](https://arxiv.org/abs/2607.01236)

**<font color=#1a73e8>作者：</font>** Yining She, Yiliang Liang, Eunsuk Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM agents gain increasing access to powerful tools, ensuring that their actions are aligned with the user's intent becomes critical. When an agent's proposed tool invocation deviates from the user's intent -- a phenomenon called misalignment -- it may lead to harmful consequences that are difficult to undo. Existing runtime guardrails rely on an LLM-as-a-judge paradigm that lacks a systematic framework for reasoning about alignment, often producing judgments that are inconsistent or difficult to audit. Motivated by provenance analysis, we propose a provenance-based conceptual framework that formalizes misalignment detection as determining whether a proposed tool call is supported by traceable evidence in the agent's context. Building on this framework, we propose ProvenanceGuard, a multi-stage pipeline that analyzes the agent's action for three types of misalignment before the selected tool is executed and only allows the action to take place when it is considered aligned with the user's input query. We evaluated our proposed approach on two different benchmarks, Agent-SafetyBench and WorkBench, across 10 backbone LLMs. Compared to the LLM-as-a-judge baseline, ProvenanceGuard reduces error rate on misaligned traces from 42.9% to 1.8% on Agent-SafetyBench and from 32.1% to 17.3% on WorkBench, while reducing intervention burden on task-successful traces from 30.5% to 12.8% and introducing no statistically significant increase in unnecessary interventions on aligned traces. These results demonstrate that structured, provenance-based reasoning provides an effective and practical foundation for safeguarding LLM agents from misalignment.

---


### 3. [Kara: Efficient Reasoning LLM Serving via Sliding-Window KV Cache Compression](https://arxiv.org/abs/2607.01237)

**<font color=#1a73e8>作者：</font>** Shen Han, Yuyang Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning language models often generate long chain-of-thought (CoT), which accumulates a massive KV cache during the decoding phase and incurs high decoding latency and limited throughput. To address these issues, KV cache compression has emerged as a promising technique for reducing memory overhead by selectively removing unimportant KV pairs while preserving useful ones for subsequent decoding. Nevertheless, we identify two key limitations in existing KV cache compression methods: 1) their threshold-triggered compression policy may provide limited throughput improvement or even reduce throughput, and may fully eliminate KV pairs from certain blocks of the sequence, potentially worsening information loss. 2) they typically retain either isolated KV pairs or fixed-size chunks with rigid boundaries, failing to preserve important flexible-sized chunks at arbitrary token positions. To overcome these limitations, we propose Kara, a sliding-window KV cache compression method that performs decoding-time compression by operating only on the recently generated context. Kara leverages bidirectional attention to score and select informative KV pairs in the window. To enable flexible preservation of important semantic information, we design a Token2Chunk module to expand a subset of selected KV pairs into chunks. Furthermore, we adapt Kara to PagedAttention and develop KvLLM, an inference framework built upon vLLM, which reduces KV cache memory usage and effectively improves output throughput. Extensive experiments demonstrate consistent performance improvements of proposed Kara and KvLLM.

---


### 4. [Breaking Safety at the Token Boundary: How BPE Tokenization Creates Exploitable Gaps in LLM Alignment](https://arxiv.org/abs/2607.01239)

**<font color=#1a73e8>作者：</font>** Tung-Ling Li, Hongliang Liu, Yuhao Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Character-level perturbations bypass safety alignment in modern LLMs despite leaving prompts human-readable. We identify and test a central structural mechanism: BPE tokenization fragments safety-critical words into sub-word pieces, and the three public alignment datasets we surveyed contain no intentionally fragmented inputs. The mechanism is a chain, tested end-to-end on five model families (Qwen-3-4B, Qwen-2.5-7B, Gemma-3-4B, Llama-3.1-8B, Mistral-7B). An optimization targeting safety-token fragmentation flips the first-token refusal trigger on 80-100% of refused HarmBench prompts, with 48% of those flips producing genuinely harmful outputs (per-model 29-65%; gap-vs-behavior ROC-AUC 0.66-0.98, pooled 0.84). Activation patching localizes the disrupted signal to the last ${\sim}30\%$ of layers; an alignment-data scan finds zero fragmented prompts among 30,000 examples (positive-control recall $\geq 99\%$ at attack-relevant intensities); and targeted-mutation experiments isolate safety words as the disruption locus. On the defense side, a 68-cell grid (55 trained checkpoints) shows that no DPO configuration achieves seed- and pool-stable ASR closure on the three families with closed pool-size confounds. SFT trained on fragmented prompts closes ASR on 3/5 families but only via global collapse that raises refusal on benign prompts as well, indicating the missing distribution is necessary but not sufficient under the LoRA-16 recipe we tested. To distinguish selective repair from global collapse, we introduce Conv-Benign, a candidate paired diagnostic. All ASR claims are 3-judge-calibrated (cell rankings stable across judges; absolute levels $\pm$18pp; see App.~B.13).

---


### 5. [Prompt Framing Distorts Count-Based Evaluation of LLM Error Detection: Evidence from Numeric Anchoring](https://arxiv.org/abs/2607.01240)

**<font color=#1a73e8>作者：</font>** Dekun Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Count-based F1 is widely used as a proxy for LLM error-detection quality, but this paper shows that it can rise dramatically without a corresponding improvement in span localization, a gap termed F1 Inflation. The paper introduces ErrorBench, a controlled stress-test protocol for prompt-induced count distortion. ErrorBench evaluates six contemporary LLMs under five prompt conditions over 4,290 responses from 143 CoNLL-2014 passages. Under CoNLL-2014 M2-style scoring, anchored prompts produce up to 0.79 points of F1 Inflation, and up to 0.96 under strict matching. A 100-passage replication using the official ERRANT 3.0.0 pipeline and multi-reference scoring reproduces the pattern: averaged over six models, the Blind-to-Anchored prompt shift raises Count-F1 by +0.21 while raising multi-reference ERRANT F0.5 by only +0.04. The study finds larger count responses in highly instruction-compliant GPT/Claude systems and smaller responses in the Gemini family under this stress-test protocol. The findings suggest that LLM proofreading and document-review evaluations should avoid pre-populated error counts and should report span-aware metrics alongside count-based metrics.

---


### 6. [ExPerT: Personalizing LLM Responses to Users' Domain Expertise via Query-Wise Semantic and Keystroke Behavioral Cues](https://arxiv.org/abs/2607.01242)

**<font color=#1a73e8>作者：</font>** Yeji Park, Jiwon Tark, Taesik Gong  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used by end users, yet existing personalization methods relying on static profiles or text-only signals fail to capture query-specific expertise variation. We present ExPerT, a query-wise personalization framework that adapts LLM responses to users' query domain expertise by combining semantic and behavioral cues. ExPerT consists of two key components: (i) a semantic-behavioral expertise inference module that jointly interprets query text and keystroke dynamics via in-context LLM prompting, and (ii) an expertise-conditioned response generation that adapts the level of detail, terminology, and conceptual complexity. Our user study with 40 participants and 1270 queries demonstrated that ExPerT reduced expertise inference error by 65.7% compared to the strongest baseline (MAE = 0.398 vs. 1.162) and improved response satisfaction by 17.52% (from 3.71 to 4.36) on a 5-point Likert scale.

---


### 7. [RuleChef: Grounding LLM Task Knowledge in Human-Editable Rules](https://arxiv.org/abs/2607.01293)

**<font color=#1a73e8>作者：</font>** Ádám Kovács, Nadia Verdha, Gábor Recski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present RuleChef, a framework that uses large language models (LLMs) to generate executable rules for NLP tasks such as text classification, Named Entity Recognition (NER), or relation extraction. Rules are generated based on a task description and a set of labeled examples, then they are iteratively improved based both on additional examples and on human feedback overexisting rules. RuleChef can also be used to bootstrap rules using the observed input-output pairs from any existing model for a given task. LLMs are used only at learning time, synthesizing rules and iteratively patching them based on failures measured on a held-out split. The result of this process is a fast, deterministic, and inspectable rule system. Preliminary evaluation is performed on both classification and NER tasks. We release RuleChef as open-source software under an Apache 2.0

---


### 8. [Black-Box Inference of LLM Architectural Properties with Restrictive API Access](https://arxiv.org/abs/2607.01313)

**<font color=#1a73e8>作者：</font>** Christopher Ellis, Shreyas Chaudhari, Mei-Yu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In practice, most commercial LLM providers do not publicly release details of underlying LLM architectures. However, prior work has shown that given limited API access to an LLM (namely, top-$k$ logits and/or a logit bias function), one can recover certain architectural details of an LLM, such as the hidden dimension of the feed-forward network. Perhaps in response to these results, most commercial LLM providers have restricted their APIs to expose only the single logit for each decoded token, and they no longer give users the ability to bias logits. We show that even under current restrictive APIs, several architectural parameters are still recoverable. We present NightVision, an attack that uses restrictive black-box API access to estimate the hidden dimension, depth, and parameter count of an LLM. Algorithmically, NightVision relies on a novel common set prompting technique in which multiple prompts expose log probabilities for the same set of output tokens; a spectral analysis of these results is used to infer hidden dimension. NightVision additionally uses end-to-end time to first token (TTFT) measurements and the estimated hidden dimension to estimate depth and parameter count. We empirically evaluate NightVision on 32 open-source LLMs, recovering hidden dimension to within 23% average relative error across all models (9% on MoE models), and depth and parameter count to within 53% for models exceeding three billion parameters. We run extensive ablations to demonstrate how these accuracies scale with token budget and model properties. Overall, our results suggest that current LLM APIs are not sufficiently restricted to fully obfuscate the architectural details of their underlying models.

---


### 9. [Auto-FL-Research: Agentic Search for Federated Learning Algorithms](https://arxiv.org/abs/2607.01366)

**<font color=#1a73e8>作者：</font>** Holger R. Roth, Ziyue Xu, Chester Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) research often depends on many small but consequential algorithmic choices: optimizer variants, server aggregation rules, local training schedules, normalization, regularization, and model architecture. These choices are expensive to explore manually and difficult to compare fairly when candidate changes can also alter the FL training or evaluation path. In this work, we present Auto-FL-Research (AFR), a constrained coding-agent workflow for FL algorithmic recipe search. Agents may propose and implement candidate training algorithms, including server aggregation rules, client update schedules, local objectives, and registered model variants, while task profiles fix the mutation surface, compute budget, communication contract, and final model evaluation. Each campaign records candidate scores, runtime, edited files, artifacts, and failure status. We evaluate AFR on five healthcare cross-silo FLamby tasks and on grouped-client profiles for the five fixed LEAF datasets plus the LEAF synthetic task. Five-seed repeat evaluations support gains on four FLamby tasks and five of six LEAF profiles, while also exposing seed-sensitive and search-selected failure cases. Same-budget controls show that several gains correspond to FL-recipe changes, whereas other improvements are recovered by fixed-surface scalar controls or fail under repeat or held-out evaluation. These mixed outcomes are part of the contribution: they show how agent-generated candidates can be separated into repeated FL mechanisms, fixed-surface tuning effects, and selected single-run artifacts.

---


### 10. [Multi-Objective Exploration and Preference Optimization via Mutual Information](https://arxiv.org/abs/2607.01392)

**<font color=#1a73e8>作者：</font>** Hongyan Xie, Yikun Ban, Ruiyu Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning large language models with diverse and heterogeneous human values requires multi-objective alignment methods to effectively trade off conflicting preference dimensions. Current methods achieve this trade-off by training policies conditioned on preference vectors and leveraging online direct preference optimization. However, exploration uncertainty can cause the reward distributions of responses generated under different preference vectors to overlap, and the generated responses may fail to effectively align with the corresponding preference vectors. In this paper, we propose Multi-Objective Exploration and Preference Optimization via Mutual Information (MI-EPO), an information-theoretic framework. It unifies multi-objective exploration and alignment by maximizing the joint conditional mutual information among generated responses, preference feedback, and preference vectors. By incorporating a probabilistic routing mechanism, MI-EPO naturally decomposes objective alignment and preference-aware exploration, encouraging the model to generate responses that are distinguishable and aligned with different preference conditions. Experiments on safe alignment and helpful assistant tasks show that MI-EPO significantly improves the alignment between generated responses and preference vectors, makes the outputs more controllable, and achieves stable trade-offs across multiple objectives.

---


### 11. [The Wiola Architecture for Efficient Small Language Models](https://arxiv.org/abs/2607.01394)

**<font color=#1a73e8>作者：</font>** Aryuemaan Kumar Chowdhury, Afreen Shaik, Yaparla Bhargavi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Wiola, a fully original Small Language Model (SLM) architecture built from first principles, sharing no structural lineage with any existing model family including GPT, LLaMA, Mistral, or Falcon. Wiola introduces five independently novel components: (i) Spiral Rotary Positional Encoding (SRPE), which embeds token positions on a three-dimensional helical manifold combining absolute, relative, and hierarchical positional signals; (ii) Gated Cross-Layer Attention (GCLA), providing each decoder layer with soft cross-attention access to compressed summaries of two preceding layers for inter-layer coherence; (iii) Adaptive Token Merging (ATM), which dynamically merges se mantically redundant adjacent tokens in middle network layers to reduce attention complexity without information loss; (iv) Dual Stream Feed-Forward (DSFF), replacing the conventional MLP with two parallel streams fused by a learned per-dimension gate; and (v) WiolaRMSNorm, a modified normalisation introducing a per-dimension learned offset vector that prevents representation collapse. We provide complete mathematical derivations, architectural block diagrams, complexity analyses, and systematic comparisons against GPT-2, LLaMA-2, and Mistral. Wiola is released in four sizes (120M, 360M, 700M, and 1.5B parameters) and is fully compatible with the HuggingFace Transformers ecosystem, with all 22 architectural unit tests passing.

---


### 12. [MultAttnAttrib: Training-Free Multimodal Attribution in Long Document Question Answering](https://arxiv.org/abs/2607.01420)

**<font color=#1a73e8>作者：</font>** Dang Quang Thien Tran, Quang V. Dang, Vinamra Tyagi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As grounded QA systems are increasingly deployed in AI assistants, accurately attributing generated answers to evidence is critical for user trust and model safety. While unimodal attributions have been explored in depth, the multimodal setting remains relatively under-researched. As a result, we introduce MultAttnAttrib, a training-free attribution-generation method that leverages a model's prefill pass, selected attention heads, and calibrated thresholds to locate source evidence within a document. To establish baseline results for the method, we introduce MultAttrEval, a complementary benchmark dataset annotated with fine-grained, ground-truth attributions for answer components grounded in multimodal source documents. To our knowledge, this is the first evaluation dataset designed specifically for multimodal attribution in long-form documents. Experimental results show that MultAttnAttrib consistently outperforms a variety of attribution-generation methods, including several strong prompting-based approaches and matches the latest frontier models such as GPT 5.4. Our method not only substantially improves attribution accuracy for both unimodal and multimodal attribution types, but also produces attributions at up to one-seventh of the direct inference latency compared to prompting on the same base model.

---


### 13. [IsoSci: A Benchmark of Isomorphic Cross-Domain Science Problems for Evaluating Reasoning versus Knowledge Retrieval in LLMs](https://arxiv.org/abs/2607.01431)

**<font color=#1a73e8>作者：</font>** Samir Abdaljalil, Erchin Serpedin, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce ISOSCI, a benchmark of isomorphic cross-domain science problem pairs that separates reasoning ability from domain knowledge retrieval in LLM evaluation. Each pair shares identical logical structure but requires different domain-specific knowledge, enabling controlled attribution of reasoning-mode gains. Across five model pairs spanning four model families, we find that 91.3% of reasoning-mode gains are knowledge-dependent rather than structure-invariant (63/69 gains; Wilson 95% CI [82.3%, 96.0%]), directly challenging the assumption that chain-of-thought reasoning improves short-horizon procedural scientific problem-solving. Reasoning toggles on highly capable models provide less than 5 percentage points accuracy gain across all domains, and a reasoning-specialized model (o3-mini) that outperforms its standard counterpart on GPQA Diamond (+19.2 percentage points) underperforms on ISOSCI (-24.7 percentage points), showing that benchmark choice determines conclusions about reasoning utility. We release ISOSCI at this https URL

---


### 14. [CreativityNeuro: Steering Language Model Weights to Improve Divergent Thinking and Reduce Mode Collapse](https://arxiv.org/abs/2607.01433)

**<font color=#1a73e8>作者：</font>** Samuel Schapiro, Core Francisco Park, Felix Sosa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Divergent thinking is a crucial aspect of creativity, yet large language models (LLMs) tend to consistently generate similar responses to open-ended questions, in what has been termed the artificial hivemind effect. Here, we introduce CreativityNeuro, a data-free method for enhancing divergent thinking in LLMs via contrastive weight steering. We evaluate our method across multiple creativity assessments and report several main findings. On the Divergent Association Task (DAT), a vocabulary-space creativity test, CreativityNeuro improves performance by up to 14 human percentile points. Next, in a large-scale human evaluation (N=720) on the Alternative Uses Test (AUT) and the Task Task, CreativityNeuro achieves significant improvements in originality, surprise, and creativity, transferring to longer-form and more open-ended tasks. Importantly, we find that across all three tasks, CreativityNeuro demonstrably reduces measures of mode collapse. Moreover, activation steering achieves comparable performance to CreativityNeuro on the DAT, but it does not transfer to the AUT and Task Task, demonstrating the effectiveness of weight-space steering in generalizing to unseen tasks. In conclusion, CreativityNeuro improves divergent thinking and reduces mode collapse without requiring behavioral data, re-training, or gradient-based fine-tuning, providing a straightforward way to enhance LLM performance in creative domains.

---


### 15. [Discrete Diffusion Language Models for Interactive Radiology Report Drafting](https://arxiv.org/abs/2607.01436)

**<font color=#1a73e8>作者：</font>** Max Van Puyvelde, Halil Ibrahim Gulluk, Wim Van Criekinge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models, which generate text by denoising a token canvas bidirectionally instead of emitting tokens left to right, have become competitive with autoregressive (AR) generation. Medical foundation models, however, remain almost entirely autoregressive. We adapt a mixture-of-experts diffusion language model, DiffusionGemma-26B, and benchmark it against its same-size AR sibling Gemma-4-26B under an identical LoRA recipe on medical visual question answering datasets, scored by a verbosity-robust LLM judge. Diffusion matches or exceeds AR on all of them, and the finetuned model (3.8B active) is competitive with frontier vision-language models; its decoding is also 3.5-4.4x faster. Beyond this parity, the diffusion model offers a drafting capability AR lacks: any-order infill. Because the canvas is denoised bidirectionally, a radiologist can fix report fragments and have the model fill the text between them, an operation inherent to diffusion but not to autoregression, which is subpar at it. This suits real reports, which are often terse or inconsistent across clinicians and institutions.

---


### 16. [FaithMed: Training LLMs For Faithful Evidence-Based Medical Reasoning](https://arxiv.org/abs/2607.01440)

**<font color=#1a73e8>作者：</font>** Zhiyun Zhang, Liwen Sun, Xiang Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Faithful reasoning is essential in medicine, where clinical decisions require transparent justification grounded in reliable evidence. Current medical LLMs either lack active access to evidence or use retrieved evidence without supervising how it should be appraised and applied during reasoning. To address this, we formalize evidence-based medicine principles as process-level criteria and introduce FaithMed, a framework that combines clinician-designed, automatically refined rubrics with reinforcement learning using step-level process reward assignment and advantage grouping. Across seven medical benchmarks, FaithMed improves over agentic-search baselines (+9% on average) and outcome-only RL (+5.8%), while raising average evidence-based medicine rubric scores over agentic-search Qwen3 baselines (+15.5%). This work demonstrates that explicit step-level supervision can improve both task success and the faithfulness of the reasoning process. Code is available at this https URL.

---


### 17. [Grounded Optimization: A Layered Engineering Framework for Reducing LLM Hallucination in Automated Personal Document Rewriting](https://arxiv.org/abs/2607.01457)

**<font color=#1a73e8>作者：</font>** Shashank Indukuri, Adarsh Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly applied to resume optimization for applicant tracking systems, introducing hallucination failures distinct from general text generation: anachronistic technology injection, cross-domain terminology contamination, structural mutation, and content fabrication. We present Grounded Optimization, a five-layer framework combining temporal context validation, deterministic contamination detection, structural invariant enforcement, prompt-level grounding, and an evaluator agent.
In ablation experiments across three LLMs, four temperature settings, and six layer configurations on 25 synthetic resumes spanning 14 industries, undefended baselines produce 2.48-5.36 detected hallucinations per resume. Among detectors independent of the active defenses, temporal hallucinations are reduced by 50-95% across all conditions; overall detected hallucination rate falls to 0.04-0.24. Prompt-level grounding alone achieves zero detected hallucinations at low temperature with a capable instruction-following model; higher temperatures and weaker models reveal the need for the deterministic layers as a complement. We release the contamination taxonomy, evaluation code, and raw data.

---


### 18. [Beyond Next-Token Prediction: An RLVR Proof of Concept for Tool-Use Agents on Atlassian Workflows](https://arxiv.org/abs/2607.01465)

**<font color=#1a73e8>作者：</font>** Karthikeya Aditya Vissa, Sankalp Mane, Ananya Mantravadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are trained to predict the next token, not to act inside a specific API. In niche enterprise SaaS workflows -- where success means hitting the right endpoint with the right nested arguments in the right order -- this objective mismatch shows up as silent failures: dropped required fields, hallucinated tools, or early stops after a single read. We ask whether Reinforcement Learning with Verifiable Rewards (RLVR), applied directly in the target environment, closes the gap. As a proof of concept we build a suite of five synthetic environments emulating the Jira REST v3 and Confluence v2 APIs at schema fidelity; rewards are computed entirely from the tool-call trace, with no live API, no learned judge, and no human label in the loop. Scoring prompted Qwen3-1.7B and Qwen3.5-4B on the same checkers that drive GRPO training, we find that on the four scenarios whose rewards are non-degenerate the RL-trained policy lifts average reward from a 4B-baseline range of 0.35--0.92 to 0.95--1.00, with the largest single gain on Confluence page creation ($0.35 \rightarrow 1.00$). We position this as a preliminary step toward outcome-optimised small models for niche enterprise APIs, and foreground two limitations a workshop reader should weigh: hand-crafting verifiable rewards does not scale beyond the handful of endpoints reported here, and one of our five scenarios (ticket-transition) has a saturating reward shape that the prompted 4B already maxes out.

---


### 19. [A Cost-Aware, Paired Protocol for Auditing Dynamic Tool Synthesis in Agentic Video Question Answering](https://arxiv.org/abs/2607.01469)

**<font color=#1a73e8>作者：</font>** Aseel Mohamed, Rama AlHamidi, Mohamed Rayan Barhdadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic Video Question Answering (VideoQA) systems invoke tools during inference, but their tool libraries are fixed, so recurring procedures are rebuilt from primitives on every question. Synthesizing composite tools could remove this overhead, but whether such expansion helps is hard to assess: final-answer accuracy, the standard metric, ignores inference effort, so it cannot reveal how a system shifts cost. We propose a cost-aware, paired protocol for auditing tool-augmented video agents. The protocol pairs two complete systems on the same input for each question and reports their net difference across accuracy and cost jointly. For each question, it sorts the paired outcome into one of six groups defined by joint correctness and by the change in visible tool calls, separating accuracy-preserving efficiency gains from harmful regressions. Significance is reported with McNemar's test and paired bootstrap confidence intervals. We instantiate the protocol on Dynamic-SAGE, an agentic VideoQA framework that synthesizes, validates, and persistently registers executable composite tools for reuse on unseen questions, and evaluate it against the SAGE baseline on SAGE-Bench. The audit reveals a multi-axis profile that a scalar accuracy comparison would miss: Dynamic-SAGE improves accuracy by 7.5 points (p < 0.001) and reduces reasoning turns and visible tool calls by roughly 28%, while shifting rather than reducing inference cost, as token usage rises 34% and cost 26%. Gains are largest on visual and open-ended questions and neutral on verbal and multimodal ones, and residual failures concentrate on hard, open-ended questions where the pipeline does the most work. By measuring accuracy and cost jointly, the protocol shows where the pipeline-level difference is reliable and where it is not. The code is available at this https URL.

---


### 20. [Procedural Memory Distillation: Online Reflection for Self-Improving Language Models](https://arxiv.org/abs/2607.01480)

**<font color=#1a73e8>作者：</font>** Ye Liu, Srijan Bansal, Bo Pang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR), along with recent selfdistillation variants such as SDPO, evaluates each rollout against a verifier and updates the policy from that episode-level signal. However, the richer procedural information in the rollout is rarely retained or reused. Across episodes and epochs, the model repeatedly encounters related problems under a changing policy, producing cross-episode signals that episode-local updates cannot capture: which strategies consistently pass verification, which failure modes persist, which patterns recur. We propose Procedural Memory Distillation (PMD), which converts these crossepisode signals into reusable procedural memory and distills it into the policy's weights during training. This memory functions as a training scaffold, absorbed into the policy itself, yielding a memory-free model at inference. PMD organizes the memory at three levels of abstraction: raw trajectories, self-reflected strategies and lessons, and higher-level behavioral patterns that recur across problems, all extracted online from the model's own trajectories. A memory-conditioned self-teacher draws on the accumulated experience to supervise the student on its own rollouts, enabling student to progressively internalize procedural knowledge within its parameters. The central design principle is co-evolution: the policy generates rollouts that update the memory, and memory shapes the supervision that updates the policy. Empirically, across Qwen3-8B and OLMo3-Instruct-7B, PMD improves over SDPO by 3.8-5.5% on SCIKNOWEVAL and 7.9-13.6% on LIVECODEBENCH. Co-evolution powers these gains: freezing either the memory or the policy trails PMD by more than 10% across SCIKNOWEVAL domains.

---


### 21. [Mind the Trust Gap: Identifying (Mis)alignments in Teacher-Student Views Toward Control and Agency in K-12 Classroom AI](https://arxiv.org/abs/2607.01506)

**<font color=#1a73e8>作者：</font>** Tomohiro Nagashima, Lisa Siegrist, Niklas Scholz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As Artificial Intelligence (AI)-based technologies have been integrated into school classrooms where multiple stakeholders (with different roles) interact with each other, it is critical to deeply understand stakeholder views in the classroom. In particular, prior work has not fully uncovered how teachers' and school students' views might or might not align well with each other, especially in K-12 classrooms. We conducted a speed-dating study using storyboards with 16 school students and 15 school teachers in Germany to investigate alignments and misalignments between their views on student-AI decision-making control in K-12 classroom. Through an explicit pair-matching analysis, we found that students and teachers had misaligned views on several key topics, including how much they trust AI and social and emotional aspects of student learning with AI. Findings also revealed the importance of teacher-student relationships outside of AI use that shape stakeholders' views and interactions. We discuss potential reasons for the observed misaligned views and strategies to fill the perspective gaps. This study illustrates the complexities of preferences in teacher-student-AI interactions that depend on the dynamic relations among the stakeholders.

---


### 22. [The Agentic Garden of Forking Paths](https://arxiv.org/abs/2607.01507)

**<font color=#1a73e8>作者：</font>** Jiacheng Miao, Jonathan K Pritchard, James Zou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Empirical research rarely admits a unique analysis. Different analytical choices can lead to different conclusions from the same data, yet these hidden forking paths are difficult to observe. We show that AI agents capture much of the analytical variation among human researchers while making these paths explicit. Across four high-stakes domains, assigning different personas is sufficient for AI agents to report divergent, often opposing, conclusions from the same data and question, with findings systematically aligned with those beliefs. In a study in which 42 human research teams analyzed the same immigration dataset, AI agents reproduced 72% of the human ideological gap in reported effect estimates. Despite reaching opposing conclusions, it is difficult to identify clear issues in each analysis based on the final AI reports: 86% passed independent AI review and 78% passed majority human expert review. These findings suggest that the central challenge is often not flawed analyses, but selective exploration and reporting from a large space of methodologically defensible analyses. AI agents may amplify this longstanding problem by making such exploration inexpensive and scalable. To address this, we introduce the m-value (multiverse value), the probability that an analysis path would produce a claim at least as extreme as the reported one. We further introduce Agentic Bootstrap, which estimates the m-value by using AI agents to sample plausible analysis paths. Applied to the human immigration study, 13.5% of reported human analyses fell in the most extreme 5% of the analysis space (m<0.05). Scientific evidence should therefore be evaluated not only by a single reported analysis but also by its position within the distribution of analyses that could reasonably have been reported. Agentic Bootstrap makes this distribution observable and turns it into a criterion for scientific credibility.

---


### 23. [Janus: a Playground for User-Involved Agentic Permission Management](https://arxiv.org/abs/2607.01510)

**<font color=#1a73e8>作者：</font>** Natalie Grace Brigham, Eugene Bagdasarian, Tadayoshi Kohno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents that autonomously execute tool calls on a user's behalf raise pressing questions about permission management: what role could users play, and what role should they play? Despite many proposed approaches, the user's role in agentic permission management remains under explored. We introduce Janus, a playground system for implementing and evaluating user-involved agentic permission management designs. Janus consists of two components: Janus-Core, a modular agentic system supporting a diverse spectrum of permission management designs, and Janus-Harness, an automated evaluation framework. Grounded in a conceptual model that identifies key design axes for user involvement, we implement six permission assistants spanning the design space and evaluate them across three scenarios and three synthetic responders. We demonstrate that user input is critical and can significantly strengthen privacy and security, that AI augmentation of user decisions can help reduce cognitive load, and that realistic user behavior including permission fatigue must be accounted for in system design. No single design performs optimally across all contexts, motivating a more principled and context-sensitive approach to deploying permission assistants in agentic systems. Janus is publicly available to support future investigation into this dimension of agentic system design.

---


### 24. [OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration](https://arxiv.org/abs/2607.01531)

**<font color=#1a73e8>作者：</font>** David Courtis, Wenhao Li, Scott Sanner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning how an environment behaves from interaction is central to building agents that adapt to unfamiliar tasks. World models learned with deep networks are flexible but data-hungry and transfer poorly beyond their training distribution. Program-synthesized world models, written as source code by LLMs and refined through counterexample-guided inductive synthesis (CEGIS), are instead data-efficient and reusable, yet they have been demonstrated mainly on structured-state worlds with a given object vocabulary, and a single program search does not scale to pixel-rendered environments whose object structure must be hypothesized flexibly. We introduce OPINE-World, an LLM agent that learns an object-centric programmatic world model online from interaction. OPINE-World couples two cooperating agents in a loop of hypothesis and test, one acting in the environment and one synthesizing the model in code with replay verification and model-based planning, and it steers exploration with a Bayesian measure of object-type adequacy we call ontology error. We evaluate OPINE-World on ARC-AGI-3, a benchmark for skill-acquisition efficiency in which the object vocabulary, the goal, and the action semantics are withheld. OPINE-World solves 20 of 25 games without per-game training and reaches an action-efficiency score of 78.4 against the human baseline.

---


### 25. [Certified World Models as Sensing Clocks: Drift-Aware Deadlines for Active Perception](https://arxiv.org/abs/2607.01537)

**<font color=#1a73e8>作者：</font>** Hongbo Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Certified world models estimate how long their predictions remain valid. We turn this validity horizon into an operational sensing clock: a rule for when an agent should stop coasting and re-sense. Starting from an audited equivariant world model, we derive a deadline for no-sensing intervals and show that deployable deadlines in learned world models must be drift-aware: on-manifold Lyapunov rates alone overestimate coasting validity, while calibrated native rollout-drift envelopes carry the deployed guarantee. On a frozen 3D VN-JEPA model, the resulting clock controls held-out interval-simultaneous certificate violation across seeds and data shards. In a cue-conditioned theorem-bed (a synthetic bench where all schedulers share the exact model, isolating the scheduling rule), the clock remains valid on the deployment distribution and substantially reduces eventful-tail violations relative to exact-mixture expected-belief scheduling at matched sensing budget. We also report limits: in the short-horizon frozen VN-JEPA regime, empirical conformal horizons match the deployed clock on validity and budget, and a partial-reset exploration finds no clean budget-matched advantage for the spectral term. Thus the contribution is a certified sensing-clock primitive and drift-aware deployment method, not a claim that spectral clocks empirically dominate all non-spectral schedulers.

---


### 26. [Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale](https://arxiv.org/abs/2607.01538)

**<font color=#1a73e8>作者：</font>** Siddharth Gollapudi, Nilesh Gupta, Prasann Singhal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) raise an intriguing alternative to vector-based retrieval: conditioning on an in-context corpus and directly generating a relevant answer. However, prior work has largely focused on proprietary systems or the smaller-scale reranking task, leaving corpus-scale in-context retrieval largely unexplored. In this work, we present the first systematic study of in-context retrieval on two scales practical retrievers demand: million-token corpora and length-generalization far beyond training-time sizes. We first introduce BlockSearch, a 0.6B LM retriever whose architectural and training modifications improve over prior LM baselines and length-generalize up to 10 times beyond its training regime. Nevertheless, retrieval still collapses under more extreme extrapolation. We trace this failure to an attention dilution effect: as the corpus grows, irrelevant documents dominate the softmax denominator, reducing the normalized mass on the gold document even when its pre-softmax score stays high. Motivated by this analysis, we introduce length-aware adjustments to the attention softmax and document-level sparse attention. With these modifications, at the million-token scale, our model matches dense retrieval on widely studied benchmarks (e.g, MS MARCO and NQ), while outperforming the concurrent model MSA despite being 7 times smaller. Furthermore, it significantly outperforms dense retrieval on tasks requiring entirely different notions of similarity, such as LIMIT, achieving a 3 times higher score. Together, our results position in-context retrieval a promising alternative to classical retrieval while emphasizing attention control under extreme context growth as a new challenge.

---


### 27. [Evolutionary Feature Engineering for Structured Data](https://arxiv.org/abs/2607.01548)

**<font color=#1a73e8>作者：</font>** Ege Onur Taga, Yilin Zhuang, M. Emrullah Ildiz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as open-ended search operators in evolutionary optimization. We introduce Evolutionary Feature Engineering (EFE), a framework for using LLM-based evolution to discover preprocessing transformations for structured data. EFE represents transformations as Python programs with a standardized fit/transform interface, allowing them to be inserted directly into existing machine learning pipelines. During evolution, candidate programs are refined using dataset context, summary statistics, and downstream performance feedback on validation set. We instantiate EFE in two settings. For time-series forecasting, EFE-Time learns invertible, dataset-specific normalizations that improve off-the-shelf time-series foundation models. It reduces forecasting errors (MASE, WQL, MAE) 3% or more when averaged across datasets and improvements are as much as 19% on the COVID-Deaths dataset. Notably, these improvements occur with recent TSFMs such as Chronos-2. For tabular prediction, EFE-Tab evolves compact feature programs that add useful interpretable features and remove redundant ones, improving or matching existing LLM-based feature-engineering methods. We found EFE-Tab to be particularly effective on classical decision trees, where small sets of evolved features yield competitive accuracy while preserving interpretability. Overall, EFE demonstrates that LLM-based evolution can improve both accuracy and interpretability when automatically tackling structured data.

---


### 28. [DiPS: Dialogue Policy Selection for High-Stakes Persuasion Agents](https://arxiv.org/abs/2607.01557)

**<font color=#1a73e8>作者：</font>** Tianyi Zhang, Mousumi Das, Abrar Anwar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often struggle with persuasion in high-stakes scenarios. People's individual personalities and concerns require tailored strategies rather than a one-size-fits-all approach. To address this challenge, we focus on a fire-rescue scenario in which an operator must persuade a resident to evacuate as a high-stakes persuasion domain and propose Dialogue Policy Selection (DiPS), a Q-learning framework to dynamically select persuasion strategies adapted to the evolving conversational context. Specifically, we train a critic, trained to maximize the chance of evacuation success, to select a persuasion policy at each turn based on the resident's recent this http URL then evaluate DiPS against multiple baselines in both simulated and real human interactions. We find that DiPS achieves higher evacuation success than a zero-shot LLM and generic RAG-augmented approach.

---


### 29. [Beyond Skepticism: Evaluating LLMs Pedagogical Intent Reasoning with the Adaptive Pedagogical Vigilance Framework](https://arxiv.org/abs/2607.01581)

**<font color=#1a73e8>作者：</font>** Minghao Chen, Ruihan Zhou, Jiayi Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The capacity of Large Language Models (LLMs) to reason about pedagogical intent within instructional communication remains underexplored, particularly in educational domains such as translation pedagogy. To address this, we propose the \textbf{Adaptive Pedagogical Vigilance (APV)} framework, a novel computational formalism that reframes communicative vigilance as an adaptive mechanism for optimizing learning through intent inference. APV formalizes the problem via a Bayesian Pedagogical Intent Inference Engine (PIIE), which models how instructors select content to maximize pedagogical utility and how vigilant learners should inversely reason about latent instructional configurations -- encompassing genre, stance, and incentives. We evaluate APV through a three-tier hierarchy: distinguishing instructional genre, reasoning about structured pedagogical setups, and generalizing to authentic educational discourse. Experiments on leading LLMs (e.g., GPT-4o, Claude 3.5) show that APV substantially improves model vigilance. It achieves the strongest discrimination between pedagogical and exposure-based content, correlates highly with human judgments ($r=0.958$), and maintains robust performance on naturalistic data where baseline methods degrade. This work establishes a unified framework for assessing and enhancing LLMs' understanding of pedagogical motives, advancing the development of more reliable AI-assisted learning systems.

---


### 30. [EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation](https://arxiv.org/abs/2607.01584)

**<font color=#1a73e8>作者：</font>** Mahyar Ghazanfari, Amin Tabrizian, Armin Mehrabian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have recently been explored for scientific hypothesis generation, but most prior work relies on unstructured literature and free-form textual claims. We present a pipeline for Earth observation that grounds hypothesis generation directly in the NASA Earth Observation Knowledge Graph. A heterogeneous graph neural network trained on historical co-usage relations ranks candidate dataset pairings, and a three-agent LLM pipeline filters, generates, and evaluates structured research hypotheses. Applied to 1,475 NASA datasets, the system produces 160 hypotheses spanning multiple Earth-science domains, including ecohydrology, glaciology, aerosol--cloud interactions, vegetation phenology, and stratospheric chemistry. Model-predicted novel dataset pairings are rated nearly as plausible as held-out real co-usages from the literature, indicating that the pipeline surfaces scientifically coherent yet unexplored combinations. A 2*2*2 factorial experiment across GPT-5.2 and Claude Sonnet 4.6 shows that hypothesis rankings remain stable, while absolute scores depend strongly on judge identity, highlighting limitations of single-judge LLM evaluation.

---


### 31. [VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment](https://arxiv.org/abs/2607.01586)

**<font color=#1a73e8>作者：</font>** Guoyang Xia, Fengfa Li, Hongjin Ji 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action models (VLAs) have recently advanced robotic manipulation, yet the effects of different robot-data pre-training paradigms remain difficult to compare because existing models often differ in architecture, data, action space, and evaluation protocol. We present VLAFlow (Vision-Language-Action Flow), a unified flow-matching framework for controlled comparison of VLA training objectives. Using a heterogeneous robot corpus, OXEMix, containing approximately 5,000 hours of data from DROID, OpenX-Embodiment, OpenX-Augmented, and RoboCOIN, we evaluate four paradigms under the same pi0-style architecture, shared VLM backbone, action expert, and 14-dimensional action space: action-only modeling (MindPI), language-supervised co-training (MindLPI), future latent alignment (MindWPI), and their combination (MindLWPI). Experiments on LIBERO, LIBERO-Plus, and SimplerEnv show that action-only pre-training is sensitive to heterogeneous data. In contrast, language supervision helps preserve vision-language generalization, while future latent alignment improves state-transition and action-outcome modeling. By combining both signals, MindLWPI achieves the most stable overall transfer performance across benchmarks. These results suggest a meta-action space view: language and future latent representations provide complementary intermediate constraints that make heterogeneous action supervision smoother and more transferable.

---


### 32. [Hawk: Harnessing Hardware-Aware Knowledge for High-Performance NPU Kernel Generation](https://arxiv.org/abs/2607.01590)

**<font color=#1a73e8>作者：</font>** Junyi Wen, Ruiyan Zhuang, Yongjia Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing high-performance kernels for Neural Processing Units (NPUs) is a critical industry bottleneck, requiring developers to manually navigate implicit hardware constraints and strict memory hierarchies. While large language models offer immense automation potential, they fail catastrophically on NPUs due to a fundamental lack of hardware-specific priors. Naively transplanting code snippets from similar NPU kernels may pass the compiler, but it consistently triggers runtime crashes and performance degradation by blindly violating underlying hardware constraints. To overcome this, we introduce Hawk, a training-free framework that harnesses hardware-aware knowledge through three core modules: (1) Run-Time Knowledge Synthesis Module, which employs a Triple-Part Executable Knowledge Representation to inherently couple the error context with executable semantics; (2) Bottleneck-Aware Knowledge Retrieval Module, which implements a 2D-Retrieval paradigm to project queries into orthogonal syntactic and hardware-aligned semantic spaces; and (3) Effect-Driven Knowledge Distillation Module, which leverages LLM-driven semantic arbitration to continuously distill the knowledge by pruning errors and consolidating redundancies based on the empirical execution feedback. Extensive evaluations on real-world NPU workloads demonstrate that Hawk elevates generation accuracy from 49.4% to 80.0%, while achieving up to a 2.2x execution speedup over state-of-the-art baselines.

---


### 33. [Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model](https://arxiv.org/abs/2607.01595)

**<font color=#1a73e8>作者：</font>** Junyan Tan, Haoran Lin, Siyuan Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the scale and complexity of cloud-based AI systems continue to escalate, ensuring service reliability through rapid fault detection and adaptive recovery has become a critical challenge. While existing approaches integrate Large Language Models (LLMs) for semantic understanding and Deep Reinforcement Learning (DRL) for policy optimization, they often rely on sequential, loosely coupled architectures that underutilize the generative and reasoning capabilities of LLMs. In this paper, we propose a paradigm shift with PASE, a Planning-Aware Semantic self-healing engine, a novel fault self-healing framework that reconceptualizes recovery as a neuro-symbolic program synthesis task. PASE employs an LLM as a core Plan Synthesis Engine to generate structured recovery plans from a library of semantic primitives. A Neural-Symbolic World Model verifies plan feasibility through simulation, while a Meta-Prompt Optimizer, trained via DRL, learns to generate optimal prompts that guide the LLM's planning process. This tight reason-plan-verify-adapt loop enables dynamic, context-aware recovery strategy generation beyond predefined action spaces. Experiments on a real-world cloud fault injection dataset demonstrate that PASE significantly outperforms state-of-the-art methods, reducing average system recovery time by over 40% and improving fault detection accuracy in unknown fault scenarios. Our framework advances autonomous system management by unifying LLM-based reasoning with model-assisted verification and meta-learned guidance.

---


### 34. [BOUNDARY_SYNC: Measuring Communication-Induced Representational Coupling in Multi-Agent LLM Systems](https://arxiv.org/abs/2607.01600)

**<font color=#1a73e8>作者：</font>** Zewen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are deployed as communicating agents, does inter-agent communication cause outputs to converge? We introduce BOUNDARY_SYNC, a protocol measuring representational coupling via the Coupling Amplification Factor (CAF = JSD_cond / JSD_baseline), where CAF < 1 indicates homogenization and CAF > 1 indicates diversification. In controlled GPT-4o experiments (N=30, ~9,900 API calls), we measure coupling in text and image communication. Key findings: (1) text communication causes significant homogenization (CAF=0.803 [0.740, 0.873], d=1.30, p<0.001), confirmed by no-communication ablation and prompt-perturbation controls; (2) image communication also homogenizes under within-modality baselines (CAF=0.834 [0.811, 0.858]), with comparable proportional effect; (3) group size moderates coupling direction -- K=5 produces homogenization while K=3 yields CAF > 1.0 (point estimates 1.14 and 1.06, CI pending), suggesting a directional shift toward diversification; (4) cross-model replication shows extreme variation (CAF 0.034-0.803), with DeepSeek dominated by format artifacts; (5) coupling is stateless -- driven by prompt context rather than cumulative updating, with continuous consensus producing monotonic convergence. These results establish LLM agent coupling as real, measurable, and controllable at the prompt level, with direct implications for multi-agent system design.

---


### 35. [SemHash-LLM: A Multi-Granularity Semantic Hashing Framework for Document Deduplication](https://arxiv.org/abs/2607.01601)

**<font color=#1a73e8>作者：</font>** Xinyi Fang, Kejian Tong, Jiabei Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large scale document deduplication must preserve semantic equivalence while remaining efficient over massive corpora. We present SemHash LLM, a multi granularity framework that unifies semantic projection hashing, attention weighted MinHash, contrastive boundary learning, and selective LLM based adjudication. The method combines character, token, and document level signals through gated fusion, then applies a cascaded filtering pipeline for efficient candidate reduction. Semantic projection hashing learns compact binary codes in distilled LLM embedding space, while attention weighted Min- Hash suppresses boilerplate and emphasizes informative content. Adaptive decision boundaries and uncertainty estimation further improve robustness across template pollution, short text perturbation, containment, and viral fragments. Experiments show that SemHash LLM achieves strong duplicate detection quality with less than one percent neural verification cost.

---


### 36. [SINA: A Fully Automated Circuit Schematic Image to Netlist Generator Using Artificial Intelligence](https://arxiv.org/abs/2607.01609)

**<font color=#1a73e8>作者：</font>** Saoud Aldowaish, Yashwanth Karumanchi, Kai-Chen Chiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Artificial Intelligence (AI) have revolutionized Electronic Design Automation (EDA), particularly through Large Language Models (LLMs) for circuit design tasks. However, their application to analog and mixed-signal domains remains limited by the lack of machine-readable representations of existing circuit design knowledge. Circuit schematic images found in research manuscripts, textbooks, and websites constitute a vast repository of validated designs; however, these visual representations cannot be directly processed by EDA tools. Converting them into machine-readable netlists is essential for enabling simulation, verification, and building comprehensive databases for AI-based models. Current conversion methods lack generalization across both Integrated Circuit (IC) and Printed Circuit Board (PCB) level schematics. Moreover, they struggle with component recognition and connectivity inference, and fail to distinguish between connected junctions and crossing wires. In this paper, we propose SINA, an open-source circuit schematic image-to-netlist generator. SINA is a fully automated pipeline that integrates deep learning for robust component detection, connected-component labeling for accurate connectivity inference, Optical Character Recognition (OCR) for component reference designator extraction, and a Vision-Language Model (VLM) for reliable reference designator assignment. SINA handles both IC- and PCB-level schematics and incorporates dedicated crossing-wires detection to differentiate wire intersections from connections. We validate the correctness of the generated netlists using graph isomorphism techniques. Our experiments demonstrate an overall netlist generation accuracy of 96.67%, which is 2.72x higher compared to state-of-the-art approaches.

---


### 37. [Scaling with Confidence: Calibrating Confidence of LLMs for Adaptive Test Time Scaling](https://arxiv.org/abs/2607.01612)

**<font color=#1a73e8>作者：</font>** Xuqing Yang, Yi Yuan, Shanzhe Lei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) with reinforcement learning (RL) has significantly advanced their performance on reasoning and question-answering tasks. However, prevailing RL reward designs typically prioritize response correctness, neglecting to incentivize models to express their confidence accurately. This leads to a critical problem: performance gains are often accompanied by poor calibration between confidence and accuracy, misleading models to overconfidently hallucinate when uncertain. To address this limitation, we propose $\textbf{C}$orrectness and $\textbf{C}$onfidence $\textbf{C}$alibration $\textbf{R}$einforcement $\textbf{L}$earning ($\textbf{C3RL}$), a novel RL algorithm integrating correctness, calibration and dataset-informed reference accuracy rewards together. Comprehensive evaluation across 8 text and multimodal datasets demonstrates that C3RL enhances calibration without sacrificing accuracy, outperforming the current state-of-the-art method in both performance and calibration metrics. Utilizing the well-calibrated verbalized confidence from C3RL, we further introduce $\textbf{C}$onfidence-based $\textbf{A}$daptive Test Time $\textbf{S}$caling ($\textbf{CAS}$), an adjustable inference-time strategy that allocates computational resources based on response confidence. Experiments show that CAS surpasses majority voting on both in-domain and out-of-domain datasets while reducing the inference budget by up to 12.33 times. We believe the synergy of C3RL and CAS paves the way for deploying more reliable and resource-efficient LLMs. The code, data and models will be released.

---


### 38. [MKGR: Multimodal Knowledge-Graph Representation Learning for Cold-Start Protein-Protein Interaction Prediction](https://arxiv.org/abs/2607.01627)

**<font color=#1a73e8>作者：</font>** Wenbo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate protein-protein interaction (PPI) prediction is central to functional genomics, disease mechanism discovery, and drug development. A difficult setting arises when candidate interactions include proteins that have no observed PPI edges during training, where models relying on network topology alone often lose useful context. This paper presents \method, a multimodal representation framework for cold-start PPI prediction. \method\ combines region-aware protein sequence encoding with four protein-centered biomedical knowledge graphs, including protein-drug, protein-disease, protein-miRNA, and protein-lncRNA associations. The sequence branch extracts contextual representations from structurally informed sequence regions, while graph attention encoders learn modality-specific protein embeddings from sparse biomedical associations. A bridge reconstruction objective regularizes graph learning by recovering shared protein-entity associations, and a pair-level gating module adaptively integrates sequence and graph evidence for each candidate protein pair. Experiments on two benchmark datasets under novel-old and novel-novel cold-start settings show that \method\ consistently outperforms competitive sequence, network, and knowledge-graph baselines across ACC, F1, AUC, AUPR, and MCC.

---


### 39. [DeadPool: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint](https://arxiv.org/abs/2607.01646)

**<font color=#1a73e8>作者：</font>** Haotian Xie, Junlin Chen, Mingkai Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-art large language model (LLM) training takes tens of thousands of graphics processing units (GPUs) for months and encounters failures across the software and hardware stack. Existing fault-tolerance mechanisms either impose non-trivial overhead during failure-free execution or suffer from prolonged recovery latency, particularly under scenarios where a small subset of compute nodes experience permanent failures. %The tradeoff between failure-free overhead and recovery latency forms a space forms a Pareto frontier We present DeadPool to simultaneously address both optimization objectives. DeadPool incorporates a fault-tolerance mechanism that restores LLM training via hot-swapping, namely by replacing failed nodes with spare nodes without terminating the complete job. The hot-swapping of DeadPool is enabled by two ideas: First, it exploits an off-critical-path in-memory checkpointing mechanism for spatial redundancy. Second, it introduces a communicator reconstruction protocol that replaces failed nodes with spare nodes at runtime. DeadPool efficiently overlaps the in-memory checkpointing with computation, thus introducing zero overhead during error-free execution. Upon permanent node failures, DeadPool can rebuild memory states with minimal recomputation by leveraging in-memory checkpoints. We evaluate DeadPool across scales (up to 512 NVIDIA A100 GPUs) and LLMs (up to 65B parameters), and observe zero checkpoint overhead with hot-swapping recovery completing in under 40 seconds. These results show that DeadPool simultaneously achieves both zero-overhead error-free execution and extremely low recovery cost.

---


### 40. [CALM: Interpretable Cross-Modal Alignment for Biomarker Discovery from Unpaired Data](https://arxiv.org/abs/2607.01656)

**<font color=#1a73e8>作者：</font>** Jueqi Wang, Zachary Jacokes, John Darrell Van Horn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The interaction between brain structure and genetic influences is key to understanding neuropsychiatric disorders. However, most large-scale datasets are unimodal, providing either neuroimaging or genetics data. We propose CALM, a framework that learns interpretable associations between brain ROIs and genetic pathways from completely disjoint populations. CALM aligns the two modalities in a shared latent space via linear projections that simultaneously match the class-conditional latent distributions and ensure group separability. These projections provide interpretable pathway--ROI associations. When trained on unimodal imaging and genetics datasets, CALM generalizes to an unseen paired dataset, outperforming several state-of-the-art methods and ablation baselines. We also demonstrate stability of the learned associations against a paired baseline. Our experiments on autism spectrum disorder reveal immune and metabolic pathways linked to specific cortical regions and are consistent with established literature. Thus, CALM opens the door to leveraging large unimodal repositories for studying cross-modal interactions in brain disorders across disparate datasets.

---


### 41. [Temporal and Cross-Modal Alignment for Enhanced Audiovisual Video Captioning](https://arxiv.org/abs/2607.01667)

**<font color=#1a73e8>作者：</font>** Chen Zhao, Jiajun Ma, Qilong Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) have advanced video understanding, achieving precise temporal and cross-modal alignment in audiovisual video captioning remains a formidable challenge. Most existing approaches suffer from modality detachment and temporal incoherence, failing to accurately bind auditory events to visual entities or capture complex causal dynamics. To address these deficiencies, we propose TCA-Captioner, a framework specifically engineered to enhance Temporal and Cross-Modal Alignment for audiovisual video captioning. We first introduce the Observer-Checker-Corrector (OCC) framework, an iterative refinement strategy that generates high-fidelity, meticulously grounded training data. Leveraging a curated high-density human interaction dataset, TCA-Captioner is optimized to model sophisticated audiovisual interactions. Furthermore, we present TCA-Bench, a diagnostic benchmark utilizing a Decoupled Evaluation Protocol to isolate and quantify model proficiency in audiovisual binding and temporal relational reasoning. Extensive experiments demonstrate that TCA-Captioner sets a new standard for temporally-coherent and synchronized audiovisual narratives.

---


### 42. [SCAPE: Accurate and Efficient LLM Training with Extreme Sparse Communication](https://arxiv.org/abs/2607.01678)

**<font color=#1a73e8>作者：</font>** Mingkai Zheng, Junlin Chen, Haotian Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Communication increasingly dominates the cost of Large Language Model (LLM) pre-training, especially under data-parallel and sharded training schemes, where gradient synchronization and parameter reconstruction overhead increase with model size and system scale. Existing communication-reduction methods either sparsify raw gradients, which can be unstable for modern Adam-style optimizers at high sparsity, or quantize communication, whose savings are fundamentally bounded by bit width and often incur additional runtime overhead. We present SCAPE, a communication-efficient distributed optimizer for LLM training that exploits the stability of AdamS's first-moment to enable aggressive sparsification without loss of LLM quality. Instead of constructing masks from raw gradients, SCAPE derives them from first-moment-based statistics, partitions mask generation across workers to align with optimizer sharding, and delays mask usage by one step so that mask synchronization can overlap with computation. SCAPE also reconstructs the quantities required for second-moment updates from a single synchronized sparse buffer, avoiding an additional collective. We implement SCAPE in Megatron-LM and evaluate its convergence by pre-training GPT-345M on OpenWebText and Llama-500M on SlimPajama-6B using 32 NVIDIA GH200 GPUs on TACC Vista. In both models, SCAPE preserves training stability, validation loss, and downstream task accuracy under 90\% and 99\% sparsity. For Llama-500M, SCAPE reduces end-to-end pre-training wall-clock time by up to 43.3\% while maintaining model quality comparable to dense AdamW and AdamS. For Llama-1.8B, SCAPE achieves up to 3.26$\times$ speedup per step compared to dense AdamS.

---


### 43. [Model Merging as Probabilistic Inference in Fine-Tuning Parameter Space](https://arxiv.org/abs/2607.01689)

**<font color=#1a73e8>作者：</font>** Long Minh Bui, Tuan Anh Le Van, Tung Phi Duc 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging aims to combine existing single-task solutions into a multi-task solution without additional data-driven fine-tuning.~Most existing approaches achieve this using geometric properties of local solution spaces. However, such geometric views provide limited guidance for scoring how statistically useful each task-specific update direction is across tasks during merging. To address this, we formulate model merging from a new perspective of probabilistic inference under a product-of-experts (PoE) scenario where each single-task solution defines an energy-based expert model (EBM) over the merged parameters. We show that several existing model merging methods arise as special cases of our framework under energy designs that impose implicit Gaussian assumptions on directional residuals between merged and task-specific models. Empirically, we find that these residuals are often heavy-tailed which exposes a mismatch with the imposed light-tailed Gaussian structures. We address this with a heavy-tailed PoE design based on Cauchy experts, which better captures the observed residual behavior while admitting a provably convergent inference procedure. Experiments across multiple tasks and architectures show significant improvements over state-of-the-arts baselines. Our code is available at this https URL.

---


### 44. [LASER: A Corrective Lens for LVLMs via Visual Attention Preservation and Sink Suppression](https://arxiv.org/abs/2607.01707)

**<font color=#1a73e8>作者：</font>** Bowen Yuan, Zijian Wang, Yadan Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) exhibit strong reasoning ability but suffer from visual forgetting during long-horizon decoding, where attention progressively drifts away from visual evidence. Existing methods largely treat this issue as a late-stage attention decay problem or attempt to mitigate it through heuristic reminders or post-hoc attention lifting. Through systematic empirical analysis, we find that performance degradation under visual forgetting is largely driven by two overlooked factors: early-stage attention decay disrupts evidence acquisition, and attention concentration on a subset of task-irrelevant visual sink tokens. Motivated by these insights, we propose LASER, a post-training framework that regulates both the visual attention trajectory and intra-visual token attention distribution during reasoning. Technically, LASER introduces two complementary rewards: a Visual Grounding Reward, which encourages the model to maintain attention on semantically salient visual tokens throughout decoding, and a Sink Suppression Reward, which penalizes excessive attention concentration on visual sink tokens. Together, these rewards preserve early-stage grounding while preventing attention collapse onto uninformative regions. Extensive experiments on eight benchmark datasets demonstrate that LASER consistently outperforms strong baselines, validating attention-aware training as an effective remedy for visual forgetting.

---


### 45. [COMFYCLAW: Self-Evolving Skill Harnesses for Image Generation Workflows](https://arxiv.org/abs/2607.01709)

**<font color=#1a73e8>作者：</font>** Zongxia Li, Dawei Liu, Fuxiao Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents are increasingly used to construct workflows and assist humans in completing recurring tasks more efficiently. As these workflows become repeated and domain-specific, agent memory and reusable skills become increasingly important: agents should be able to recall workflow patterns, execution constraints, and user preferences from previous runs. We study this problem in workflow-based image generation and introduce COMFYCLAW, an agentic skill evolution harness for controlling ComfyUI workflows. COMFYCLAW formulates workflow construction as typed graph editing, exposes tools organized by construction stage, automatically reverts invalid edits, and uses a region-level vision-language model (VLM) verifier to translate visual failures into actionable repair suggestions. The framework further evolves a progressively disclosed skill library, where trajectories, execution errors, and verifier feedback from previous runs are distilled into reusable Agent Skills. Across four benchmark splits, three agent models, and two image backbones, COMFYCLAW achieves the best average image-generation evaluation score across all six agent configurations, outperforming a verifier-only baseline without skill evolution. Human annotations further show that annotators prefer COMFYCLAW over variants without skill evolution. Our results suggest that skill evolution is an effective mechanism for improving agent reliability and performance in recurring visual workflow construction.

---


### 46. [Generic Expert Coverage for Pruning SparseMixture-of-Experts Language Models](https://arxiv.org/abs/2607.01710)

**<font color=#1a73e8>作者：</font>** Yongqin Zeng, Sicheng Pan, Jiale Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparsely activated Mixture-of-Experts (MoE) language models contain substantial structured redundancy among routed experts, but pruning them without downstream calibration data remains challenging. Existing expert-pruning methods typically rely on a single aggregated importance score, which can bias the retained set toward experts favored by dominant calibration patterns. We propose \textbf{Generic TB-Coverage}, a coverage-aware expert pruning method that uses only generic text corpora (WikiText2 and C4) for calibration. Instead of collapsing expert utility into one score, our method profiles per-expert utility separately on each corpus and enforces a fixed-budget coverage rule that preserves high-utility experts from each corpus before constructing the final pruning mask. Across Qwen1.5-MoE-A2.7B and DeepSeek-MoE-16B-Base at 25\%, 50\%, and 75\% retention budgets, our method improves average accuracy on six common zero-shot benchmarks over random pruning, REAP, and ExpertSparsity, while also reducing perplexity degradation on WikiText2 and C4. The gains are largest under aggressive pruning (25\% and 50\% retain), suggesting that preserving cross-corpus expert coverage is an effective generic-data prior for MoE pruning. Our improvements hold with fixed pruning budgets and no downstream calibration data.

---


### 47. [Rethinking Speech-LLM Integration for ASR: Effective Joint Speech-Text Training by Interleaving](https://arxiv.org/abs/2607.01733)

**<font color=#1a73e8>作者：</font>** Ruchao Fan, Yiming Wang, Rui Zhao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-LLM integration has shown promising results by leveraging extensive textual pretraining, yet its specific benefits for automatic speech recognition (ASR) remain unclear. We observe that as supervised ASR training data increases, the contribution of LLM priors becomes less evident, and simple speech-text joint training under-utilizes textual knowledge. We therefore propose Joint Speech-Text Interleaved Pretraining (JSTIP), an ASR-oriented pretraining strategy that constructs word-level and segment-level interleaved speech-text sequences within aligned pairs for speech-LLM architectures that accept continuous inputs. Experiments on 38k hours of ASR data show consistent entity accuracy improvement compared to ASR-only and joint speech-text training baselines. JSTIP achieves on-par entity recognition performance using domain transcription text compared to synthetic speech-text pairs, simplifying domain adaptation. Benefiting from textual pretraining and domain text data, JSTIP is competitive with open-source ASR and Speech-LLM systems in medical entity recognition. The zero-shot speech question answering behaviors further suggest that interleaving reduces the speech-text modality gap and preserves the LLM generative prior, which is likely the reason for the entity improvements on the ASR task.

---


### 48. [Predicting Closed-Loop Performance of Latent World Models: Offline Checkpoint Selection for MPC and Model-Based RL Under Non-Markovian Rewards in LunarLander](https://arxiv.org/abs/2607.01736)

**<font color=#1a73e8>作者：</font>** Nikolai Smolyanskiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how to predict the downstream closed-loop performance of a learned latent world model from validation-time diagnostics alone. Choosing the right checkpoint from a world-model training run is difficult: validation loss and multi-step prediction RMSE keep improving long after closed-loop performance has collapsed. We present a suite of structural validation-time diagnostics drawn from optimal-control theory and apply them to Gymnasium's LunarLander v3, which features shaped rewards. We train an RSSM [5, 4] world model on it and treat per checkpoint CEM-MPC return as the oracle for closed-loop quality. By evaluating 40 metrics against this oracle, we find that the strongest single predictor is the Reward Observability Fraction (ROF), which measures the reward predictor's dependence on the observable subspace. We combine ROF with three structural regularizers into a single-number offline checkpoint selection score, the Composite Reward Observability Fraction (CROF). The CROF-selected world model trains a model-based A2C policy that beats a fairly evaluated model-free A2C baseline by ~24.5 return points while using ~65x fewer real-environment interactions, and the same world model also drives a strong zero-shot CEM-MPC policy. Code and data: this https URL.

---


### 49. [ReQuest: Rethinking-based Question-Aware Frame Selection for Long-Form Video QA](https://arxiv.org/abs/2607.01737)

**<font color=#1a73e8>作者：</font>** Minkuk Kim, Suyong Yun, Young Tae Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) have substantially advanced video understanding, yet long-form video QA remains challenging under fixed input token budgets, where uniform sampling can be inefficient for evidence localization. We propose ReQuest , an uncertainty-driven, question-adaptive keyframe selection pipeline that aligns question intent with relevant video content through selective computation. ReQuest integrates (i) a lightweight question-aware selector distilled from MLLM-generated supervision, (ii) Re-thinking Routing that triggers additional inference only when the model is uncertain with a length-adaptive criterion, and (iii) uncertainty-guided adaptive non-maximum suppression that selects temporally diverse frames while adjusting spacing based on question difficulty. As a plug-andplay method, ReQuest improves long-video QA without modifying or fine-tuning the underlying MLLM. Experiments on Video-MME, MLVU, and LongVideoBench demonstrate consistent accuracy gains with competitive computational cost, with particularly strong improvements in medium and long video regimes.

---


### 50. [Meta-Benchmarks for Financial-Services LLM Evaluation](https://arxiv.org/abs/2607.01740)

**<font color=#1a73e8>作者：</font>** Blair Hudson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public LLM leaderboards optimise for global average performance and do not capture the specific cognitive demands of financial-services work: a model that leads on MMLU-Pro may underperform on document-grounded compliance reasoning, and a coding leader may handle multi-turn customer interactions poorly. We present a meta-benchmarking framework that organises 452 publicly reported benchmarks into 41 O*NET Generalized Work Activities and aggregates those into 38 BIAN banking business domains spanning sales, operations, risk, and support work. A multiplicative weighting scheme (discrimination x coverage x recency), computed over a rolling model window, rewards benchmarks that still separate the best models, are widely reported, and remain in active use, suppressing saturated legacy tests automatically. These weights scale the K-factor in a pairwise Elo tournament, producing cross-benchmark-comparable work-activity scores without raw score normalisation; business-domain scores are weighted averages of the constituent work-activity Elos. We demonstrate the framework on a point-in-time public snapshot covering 288 models across 25 organisations as of June 2026, and describe the methodology, full taxonomy, design decisions, and limitations with the aim of making the approach reproducible for institutions facing similar selection and governance challenges.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-136](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
