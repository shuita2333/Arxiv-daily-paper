# 🧠 大模型相关研究 | 2026年09月23日

> 本类共 **379** 篇论文：已确认 **359** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-379](./part-08.md)

---

### 1. [Recognition, Simulation, and Refusal: A Contamination-Aware Study of Classic Psychological Effects in LLM Agents](https://arxiv.org/abs/2609.22090)

**<font color=#1a73e8>作者：</font>** Joy Bose  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An LLM producing the response pattern associated with a human psychological effect is not the same claim as the LLM possessing that bias. We present PsyAgentBench, a benchmark that re-runs classic psychology experiments on LLM agents under a factorial design built to separate these: each paradigm is run with the paradigm explicitly labeled in the prompt (named) or framed as a routine task (blind), and on the literal textbook version of the task (canonical) or a structurally matched variant written to reduce lexical and scenario overlap with likely training data (counterfactual), crossed with a persona manipulation. Across five completed paradigms, evaluated on up to three open-weight model families with 41,904 trials released, apparently human-like effects arise through qualitatively different routes rather than one susceptibility: paradigm-label gating with explicit override (Asch conformity, 0 percent blind to 83.3 percent named on gpt-oss-120B), knowledge-dependent signal reliance (anchoring, exactly zero on grounded facts versus near total on invented quantities, a pattern equally consistent with rational use of the only available signal), amplification on novel content under labeling (framing), robust absence (sunk cost), and safety-mediated selection where refusal itself is the primary finding (minimal-group allocation). A one-sentence persona change (agreeableness, framed as an instruction rather than a verified trait manipulation) eliminates, dampens, or reverses these effects depending on which effect it is, arguing against any single response-bias account. We further formalize, and in two cases document empirically, three ways a psychology paradigm can fail to port to LLM agents: persona dominance, population collapse, and safety selection. We argue scalar bias-susceptibility scores obscure this structure and report replication profiles instead.

---


### 2. [Token Signatures of Code: Comparing Coding Behaviors Across Large Language Models](https://arxiv.org/abs/2609.22097)

**<font color=#1a73e8>作者：</font>** Junpeng Wang, Yuzhong Chen, Menghai Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The evaluation of large language models (LLMs) on coding tasks has primarily focused on performance metrics such as pass@k. As LLMs continue to advance, many models now meet baseline performance requirements, reducing the discriminative power of performance-based evaluation alone. Yet a key question remains largely unexplored: how do LLMs differ in their coding behavior? We propose CLIC (Code Learning for Identification and Comparison), a visual analytics approach that characterizes LLM coding behavior through token-frequency analysis. CLIC represents each code sample as a feature vector of token frequencies and trains an interpretable decision tree to separate two LLMs' code sets. Beyond classification accuracy, we define two new metrics: robustness, which measures whether the two LLMs remain distinguishable as their most-discriminative tokens are progressively removed, and concentration, which measures whether the difference is driven by a few dominant tokens or spread across many. Interpreting numerous pairwise comparisons (across LLM pairs, tasks, and tokenization levels) and tracing the full analytical chain form an inherently multi-scale, hypothesis-driven exploration task. We therefore develop an interactive visual analytics system to navigate the comparison landscape, identify pairs of interest, and drill down into discriminative tokens and their code contexts. Case studies comparing 10 LLMs across 22 Kaggle ML tasks reveal actionable insights for LLM selection and prompt engineering.

---


### 3. [TreeSpark: Calibrated, Load-Adaptive Draft Trees for Semi-Autoregressive Speculative Decoding](https://arxiv.org/abs/2609.22098)

**<font color=#1a73e8>作者：</font>** Huapeng Zhou, Huayu Wang, Xinyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates language-model inference by letting a cheap drafter propose tokens that the target model verifies in parallel. Recent block drafters make drafting nearly free: a single backbone pass emits an entire block of draft tokens. Draft trees promise a further gain -- several alternative continuations verified in one target forward -- but existing constructions rank candidates by per-position marginals that ignore which parent a candidate extends, so on semi-autoregressive drafters wider trees mostly add mis-ranked nodes; and a tree of fixed size ignores how much speculation each decoding round, and each serving load, can support. We introduce TreeSpark, which reads a parent-conditioned distribution from the drafter's existing Markov head at negligible cost, calibrates it into an edge-acceptance estimate, and lets path survival govern everything else: best-first expansion, per-round stopping, and a load-adaptive serving policy. Sampling siblings without replacement, with matching residuals in recursive rejection, keeps decoding lossless at any temperature. Adaptive trees improve on matched fixed budgets at every temperature; against a tuned chain on the same drafter, TreeSpark accepts 15-25% more draft tokens per round and decodes 8-14% faster in single-request wall-clock, and under rising load it gracefully shrinks the tree back to the chain. Code and artifacts: this https URL

---


### 4. [AdaMem: Adaptive Memory Token Allocation for Soft Compression in Retrieval-Augmented Generation](https://arxiv.org/abs/2609.22100)

**<font color=#1a73e8>作者：</font>** Artem Sakhno, Grigorii Davydenko, Omar Zoloev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) improves language models with retrieved evidence, but processing many long passages is costly and can introduce distracting information. Soft compression addresses this challenge by encoding passages as compact sequences of continuous memory embeddings before generation. However, existing methods typically assign each retained passage an identical number of memory embeddings, irrespective of its query-specific relevance. To address this, we propose AdaMem, a relevance-guided soft-compression framework that maps learned passage-relevance estimates to a query-dependent allocation of a fixed memory-token budget. A shared query-conditioned compressor produces both continuous passage memories and relevance scores in a single pass; a deterministic allocation rule assigns more memory tokens to higher-scoring passages and can omit low-scoring ones. Across six open-domain QA benchmarks, AdaMem consistently outperforms OSCAR (the closely matched soft-compression baseline that uses uniform allocation) as well as other soft-compression methods at matched memory budgets. Under standard 16$\times$ compression, AdaMem improves sub-string match by up to 3.2 points (5.5%) over uniform allocation baseline, with an average relative gain of 3.4%; under aggressive 64$\times$ compression the average relative gain grows to 14.6%, with a maximum of 9.8 points (19.7%) on PopQA. AdaMem matches the answer quality of the uncompressed at up to 4$\times$ lower inference latency than full context baseline. AdaMem retains an efficiency profile comparable to the uniform-compression baseline, while achieving up to $4\times$ lower inference latency than full-context inference. Thus, relevance-guided memory allocation is particularly effective when retrieval pools are large and the available memory budget is tight.

---


### 5. [DeepInstructor: An Agentic AI Instructor for Experience-Driven Idea Evaluation](https://arxiv.org/abs/2609.22104)

**<font color=#1a73e8>作者：</font>** Rongcan Pei, Fang Guo, Qinglin Qi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As automated scientific discovery advances, Large Language Models (LLMs) can now generate research ideas at an unprecedented scale, shifting the bottleneck from idea generation to idea evaluation. Existing evaluators mainly rely on parametric LLM knowledge or unstructured retrieval, producing judgments that lack the experience-grounded reasoning used by human instructors. To address this, we propose DeepInstructor, an agentic framework that formulates idea evaluation as reasoning over structured scholarly experience. DeepInstructor constructs an Experience Graph from 58,607 peer reviews and employs a ReAct-based agent to retrieve dimension-specific evidence for traceable evaluation. We further introduce DeepInstruct, a dataset with controlled pairwise comparisons across novelty, significance, and feasibility. Experiments show that DeepInstructor substantially outperforms existing baselines, improving Hit@1 and Hit@2 alignment with human judgments by 24.4% and 29.7%, respectively. Our findings suggest that scientific idea evaluation can be grounded in explicit reasoning over structured scholarly experience

---


### 6. [PRQuant: Permutation Residual Quantization for Low-Overhead Inference](https://arxiv.org/abs/2609.22106)

**<font color=#1a73e8>作者：</font>** Peiran Wang, Anqi Wang, Jiaying Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accuracy of Low-bit quantization of linear layers is often dominated by a small number of outliers. Although existing methods, such as smoothing, rotation, or residual-based approaches, may mitigate this problem, they often introduce new accuracy bottlenecks to weights. Besides, most of these techniques are implemented as online approaches, which can result in heavy execution overheads. To address the afore-mentioned issues, We propose PRQuant (Permutation Residual Quantization), a training-free and low-overhead framework that combines channel reorganization with static weight-side residual compensation. After AWQ-style scaling, PRQuant identifies the input channels that contribute most to weight quantization error, permutes them into contiguous tail blocks, and constructs their residual weight sub-tensors offline. During inference, this contiguous structure enables the activation side to use tail blocks seamlessly without the expensive online gathering operation, and turns scattered residual compensation into a regular tail-augmented GEMM, substantially reducing latency. Experiments demonstrate that PRQuant effectively reduces down-projection reconstruction error. Ablation studies confirm that smoothing and residual compensation are the primary drivers of numerical improvement, while permutation provides a consistent marginal numerical benefit and, more importantly, enables a hardware-friendly contiguous layout that eliminates dynamic gathering overhead. Overall, PRQuant outperforms default MXFP4 and the evaluated PTQ baselines in average accuracy across five downstream benchmarks, improving over MXFP4 by 1.24 and 0.55 on Qwen3-4B-Instruct-2507 and Qwen3-30B-A3B-Instruct-2507, respectively.

---


### 7. [A Shared Learning Rate Is Not a Neutral Control in Selective On-Policy Distillation](https://arxiv.org/abs/2609.22109)

**<font color=#1a73e8>作者：</font>** Chencheng Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selective on-policy distillation trains a student only at the token positions a selector scores highest, and the literature compares selectors under a single shared learning rate--a control chosen to be neutral. We show it is not. Under LoRA on GSM8K (Qwen2.5-1.5B student, 7B teacher), across an 8x learning-rate grid, dense supervision is statistically flat (swing 1.8 pp, p=0.26) while every selective arm moves with the rate: 5.4 pp for a random 5% subset, 6.7 pp for a total-variation selector, up to 17.7 pp for a teachability selector. Consequently the dense-versus-selective verdict reads 10.1 pp at lr=1e-4 but 5.1 pp at 5e-5--a 2.0x difference decided by a parameter the protocol treats as scenery--and two of six pairwise significance calls between selectors flip between adjacent rates without any rank inversion. We call this selector-rate entanglement and trace it to selection itself rather than step size: AdamW update magnitudes track the rate to within 2.2% despite 15.5x gradient-norm differences across arms. A preregistered frozen-scoring ablation (selection scored by the initial student; criterion, budget, and on-policy rollouts unchanged; 12 seeds per cell) shows live scoring adds 3.79+/-1.69 pp of rate sensitivity (p=0.035) while the frozen arm remains significantly entangled (p=0.015): the feedback loop aggravates the phenomenon rather than causing it. Under full fine-tuning at the rates this literature actually uses (1e-6 to 1e-5) the pattern grows: dense itself swings 19.8 pp, the selective arm 49.5 pp, and the verdict ranges from a non-significant +3.6 pp at the published operating point to +34 pp (p=0.005) one notch hotter. On MATH-500 the rate dependence does not reproduce under LoRA, scoping that result, while the ~10 pp cost of selective training does. We prescribe reporting the arm x rate matrix, not a shared-rate column, as a precondition for selector comparisons.

---


### 8. [Evaluating Fine-Tuned and Base Language Models in Maternal and Vaccination Healthcare for African Settings](https://arxiv.org/abs/2609.22110)

**<font color=#1a73e8>作者：</font>** Abdulquddus Ajibade, Oluwaseun Odunsi, Iyinoluwa Animasaun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Large language models (LLMs) can improve healthcare information delivery in low-resource settings but may produce inaccurate or culturally inappropriate advice. This study evaluated domain-specific fine-tuning for maternal health and vaccination in Nigeria. Objective: To compare HelpMum's MamaBot-Llama and Vax-Llama with Meta's Llama-3.1-8B-Instruct for accuracy, safety, clarity, contextual appropriateness, and trustworthiness. Methods: We evaluated 200 healthcare questions, 100 each for maternal health and vaccination, across five subdomains per domain. MamaBot-Llama and Vax-Llama were fine-tuned using Low-Rank Adaptation on over 36,000 maternal health and 9,000 vaccination question-answer pairs, respectively. Two Nigerian licensed physicians independently rated responses using a 5-point Likert scale. Paired comparisons used Wilcoxon signed-rank tests. Results: Performance varied by domain. MamaBot-Llama significantly outperformed the base model across all criteria, with a 4.9% overall improvement (p < .001), including gains in clinical trustworthiness (+7%) and medical accuracy (+5%). Critical issues decreased by 50%, and clinicians preferred it in 78% of cases. In contrast, Vax-Llama showed a 5.2% overall decline (p < .001), with critical issues increasing by 192% and safety concerns by 400%. Conclusions: Domain-specific fine-tuning can improve healthcare LLM performance when based on high-quality, clinician-curated data, but may also degrade performance when dataset quality is inadequate. Rigorous domain-specific validation is essential before clinical deployment. Physician evaluators provided informed consent, and chatbot logs were anonymized. Keywords: Large language models; Fine-tuning; Maternal health; Vaccination; Healthcare AI; Low-resource settings; Nigeria; Model evaluation; LoRA; Medical accuracy

---


### 9. [Beyond the Text: Verifying That Agent-Written Papers Are Backed by Their Artifacts](https://arxiv.org/abs/2609.22111)

**<font color=#1a73e8>作者：</font>** Qiuhong Shen, Benlong Wu, Hanjin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly capable of conducting research autonomously, producing research documents alongside the code and experiments that ostensibly support them. Yet whether the reported findings are consistently supported by corresponding implementations and execution evidence remains largely unexplored: existing review practices primarily assess textual quality and cannot reliably identify inconsistencies such as hard-coded metrics, unimplemented methods, or unsupported experimental results. We present ReAgent, an automated auditing framework for assessing the consistency between agent-generated research documents and their associated repositories. ReAgent constructs structured representations of scientific claims from research documents and uses them to guide repository analysis and evidence collection. Static auditing examines whether claimed methodologies, implementations, and experimental configurations are consistently reflected in the repository, while dynamic auditing executes relevant experiments and collects execution evidence to assess empirical findings. By combining static analysis with dynamic evidence, ReAgent identifies inconsistencies that may remain hidden under either perspective alone, such as experiments that reproduce reported numbers while deviating from the claimed methodology. The collected evidence and audit decisions are organized into a structured repository-level audit report, enabling transparent evidence traceability. We evaluate ReAgent on a manually curated benchmark of agent-generated research document--repository pairs and compare it against representative static and reproduction-based baselines. Experimental results demonstrate that ReAgent effectively identifies inconsistencies between reported research findings and their supporting repository evidence.

---


### 10. [Privacy Personalization Trade offs in LLMs: The Impact of Stylometric Signal Reduction on User-Specific Text Generation](https://arxiv.org/abs/2609.22112)

**<font color=#1a73e8>作者：</font>** Muhammed Nazmul Arefin, Omar Jamal Hammad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated the ability to generate user-specific text with high stylistic fidelity. However, the personal data that enables such personalization frequently embeds demographic, cultural, and stylistic markers that raises concerns about stylometric re- identification. This paper investigates whether reducing identifiable stylistic signals affects personalization in text generation by LLMs. We introduce a controlled framework to isolate stylometric signals in LLM personalization using the LaMP-7 Twitter benchmark. Experiments on 250 sampled users compare two settings: paraphrasing conditioned on the original profile and paraphrasing conditioned on an anonymized converted profile in which demographic identifiers, cultural references, personal details, and informal linguistic cues have been systematically neutralized. Outputs are assessed by two independent LLM judges and a complementary human evaluation. Our pairwise evaluation shows that outputs conditioned on original profiles are nearly indistinguishable from human-authored ground truth, indicating that modern LLMs can closely reproduce an author's writing style with sufficient fidelity. In contrast, preference for model outputs with anonymized profiles drops to 13.0% on average, while semantic context preservation remains high at 94.8%. A study with human evaluators confirms the same pattern. These findings reveal a clear privacy-personalization trade-off and highlight the need for privacy-aware personalization methods that retain meaning while suppressing identifying stylistic signals.

---


### 11. [An Empirical Cost Attribution of Context-Compression Gateways in Multi-Turn Coding Agents](https://arxiv.org/abs/2609.22114)

**<font color=#1a73e8>作者：</font>** Luzhuo Chen, Jiayu Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context compression is widely proposed as a way to cut the token bill of LLM coding agents, and public benchmarks report that aggressive compression preserves task-solving quality. These two facts do not imply the third one commonly assumed: that compressing file reads saves money in a real multi-turn agent. We instrument a production compression gateway (Paritok) between coding agents (Claude Code, Codex) and frontier LLMs (Claude Sonnet, GPT-5), and decompose the token bill of real sessions into three independent levers: tool-schema filtering, content compression of file reads and tool output, and history summarization. Measured in isolation under controlled A/B runs, the three save at fundamentally different rates. Tool-schema filtering removes a fixed block every turn, roughly 21K-57K tokens on a typical turn; it is linear in the turn count N and the only unambiguously and reproducibly positive lever. Content compression saves only about 2% of the cache-priced prefix per turn, but compressed reads accumulate in history and are re-sent on every later turn, so its cumulative saving grows quadratically, about 3350*N^2 tokens (measured), overtaking the fixed tool-filter saving within roughly 6 turns until the context window caps it. A non-destructive gateway lets the agent pull original bytes back on demand; each recall re-sends exactly the one segment just compressed away, so its cost is fixed and bounded rather than a multiplicative blowup, and heavy recall spends the accumulated saving back one segment at a time. Finally, a strong single-shot compression benchmark - 86.5% of SWE-bench quality retained at a 25.7% compression rate, achieved by the model this gateway deploys (Paritok-4B, reported separately) - is orthogonal to multi-turn agent cost and must not be cited as a cost-saving argument. We distill the results into an actionable recipe for where token-saving effort pays off.

---


### 12. [Evaluation Awareness Shifts from Format to Context with Model Scale](https://arxiv.org/abs/2609.22119)

**<font color=#1a73e8>作者：</font>** Navraj Singh, Maheep Chaudhary  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation awareness poses an unprecedented threat to model evaluation, but the mechanisms by which models detect it remain unknown. This study focuses on determining this and identifying contrasting mechanisms between smaller and larger models. While smaller models use the prompt's format sensitivity to detect evaluation, larger models often rely on higher-order reasoning to detect it. We evaluated Gemma 3 (1B, 4B, and 12B), Phi-3 (Mini and Medium), and Llama-3 8B using Chain-of-Thought analysis, representation probing, and Integrated Gradients attribution. Motivated by these findings, we propose a dual-pathway intervention that combines prompt sanitization with activation counter-steering to suppress both external evaluation triggers and their internal representations. Across 200 highly evaluation-aware prompts, our method achieves an average behavioral flip rate of 70.58\%, consistently outperforming either intervention alone. These results provide new insights into how evaluation awareness develops in compact language models and suggest that effective mitigation requires jointly addressing both prompt-level and representation-level this http URL and codebase can be found in this \href{this https URL}{Github Repository.}

---


### 13. [Success Leaves Detours: Learning Executable Walkthroughs for Long-Horizon Agents](https://arxiv.org/abs/2609.22120)

**<font color=#1a73e8>作者：</font>** Kaijie Chen, Chenyu Fang, Liang Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time self-evolving agents improve by reusing past experience, yet sparse-reward trajectories contain failures, loops, and detours, while summaries often omit the state conditions and action dependencies needed for execution. We study executable Walkthrough induction from sparse-reward trajectories: extracting compact, state-conditioned, and verifiable procedures. Our key observation is that delayed credit identifies actions associated with progress but cannot determine whether they produce facts required by later actions. We propose Trace, a credit-guided, dependency-grounded framework that compiles noisy trajectories into executable Walkthrough Memory. It detects progress anchors from rewards and persistent state changes, propagates credit to identify valuable transitions, and estimates action prerequisites from cross-episode success and failure evidence. Backward dependency slicing then traces required facts to their producers, extracting dependency-consistent action chains while removing irrelevant loops and detours. The resulting Walkthroughs encode entry conditions, ordered state--action--effect steps, and completion and failure predicates, supporting reuse, intermediate-state resumption, and programmatic verification. Experiments on J-TTL, WebShop, and ScienceWorld with three open-source LLMs show that Trace consistently outperforms eight test-time learning and memory baselines. Compared with the strongest baseline, it improves average AUC and Final-$3$ by $30.0%$ and $40.5%$, respectively, while using fewer inference tokens. These results show that long-horizon interaction benefits more from state-conditioned executable procedures than from complete trajectories or abstract summaries.

---


### 14. [Rank Portability Does Not Imply Feasibility Portability: Target-Specific Evaluation of Joint Hardware Constraints](https://arxiv.org/abs/2609.22122)

**<font color=#1a73e8>作者：</font>** Wesley Shu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-device hardware evaluation often assumes that if architecture rankings transfer across devices, a proxy device can support target-side model selection. We stress-test this assumption for joint latency-energy feasibility across two public architecture families. On NAS-Bench-201, cross-device rank correlations are moderate, while target-comparable feasible-set overlap remains incomplete. A faithful AdaProxy diagnostic substantially improves latency ranking, showing that the observed boundary failures are not simply due to weak adaptation. Exact finite-sample split-conformal analysis also exposes an evidence bottleneck: a finite one-sided 90% threshold requires at least nine calibration observations. We then replicate the phenomenon on 10,000 GPT architectures across 13 HW-GPT-Bench devices. Relative to an RTX3080 proxy, target latency SRCC ranges from 0.951 to 0.996, yet proxy-reuse violation risk ranges from 33.3% to 100% under matched joint constraints. These results show that rank portability, feasibility portability, and target-specific decision support are distinct evaluation objects. Cross-device evaluations should therefore report which target environments actually support the operating point being claimed.

---


### 15. [Balancing Reasoning and Hardware Constraints in RAG Pipelines for Ukrainian Multi-Domain Document Understanding](https://arxiv.org/abs/2609.22124)

**<font color=#1a73e8>作者：</font>** Illya Havrylov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the system submitted to the UNLP 2026 Shared Task on Multi-Domain Document Understanding. The challenge required extracting precise answers, document IDs, and page numbers from a diverse corpus of Ukrainian PDF documents within a strict 9-hour offline Kaggle execution limit. During evaluation on the hidden private test set, optical character recognition (OCR) of scanned documents emerged as a severe bottleneck, consuming 5-7 hours of the total time budget due to sequential single-threaded execution. This overhead strictly limited the remaining time for Large Language Model (LLM) inference to approximately two hours for 500 questions. To guarantee pipeline completion without timeouts, we developed a resource-efficient Hybrid Retrieval-Augmented Generation (RAG) pipeline utilizing BM25, BGE-M3, and Cross-Encoder reranking. Rather than deploying parameter-heavy reasoning models (e.g., DeepSeek R1) which consistently timed out, we utilized a 4-bit quantized LapaLLM 12B model via this http URL on dual NVIDIA T4 GPUs. Prioritizing pipeline stability over multi-step reasoning, our system achieved a Private Score of 0.8095, placing 10th out of 15 active teams.

---


### 16. [Type-Driven Tokenization for Brahmic Scripts](https://arxiv.org/abs/2609.22125)

**<font color=#1a73e8>作者：</font>** Sai Hemanth Kapila, Rakshika Bagavathy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard tokenizers used in large language models produce malformed text when applied to Brahmic scripts. They are a family of abugidas, writing systems whose consonants carry an inherent vowel that dependent marks can modify. They include Devanagari, Telugu, Tamil, Kannada, and others. The underlying issue is that these tokenizers violate orthographic constraints that do not arise in alphabetic scripts like English. We observe that while English orthography forms a \emph{semigroup} (any two valid tokens can be freely concatenated), Brahmic orthography forms a \emph{partial semigroup}: not every concatenation yields a valid string. We formalise this distinction in Agda, model valid Brahmic tokens as chains in a transition system, and derive a provably correct \texttt{fixToken} function that extends any candidate token to respect orthographic boundaries. We then show how this formal derivation translates into a practical patch for SentencePiece as well as a standalone Rust-based pre-tokenizer library, eliminating the observed errors across Indic scripts.

---


### 17. [Beyond Accuracy and Surface Fluency: Risk-Sensitive Evaluation of LLMs for Legal Clause Generation](https://arxiv.org/abs/2609.22127)

**<font color=#1a73e8>作者：</font>** Devansh Singh, Sundaraparipurnan Narayanan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to draft contractual language, yet conventional accuracy or preference-based evaluations are poorly matched to legal drafting. A clause may be fluent and stylistically polished while still omitting an essential carve-out, allocating risk in an unenforceable way, assuming an inapplicable jurisdiction, or exposing a party to regulatory liability. This paper presents a empirical study design and framework for evaluating LLM-generated contract clauses. The study evaluates four models - Claude Haiku 4.5, Gemini 2.5 Flash Lite, GPT 5.4 Nano, and Qwen 3.5 Flash, across 22 contract clause categories and 34 legally-motivated failure modes. We combine two evaluation frameworks: CLAUSE, which classifies prompts by legal function and failure target, and LENS-CRAFT, which scores outputs across nine legal-quality dimensions. Instead of averaging dimension scores, the study applies a Max Severity Principle so that a single legally decisive defect remains visible. The paper provides the evaluation protocol, taxonomy, analysis plan, and a results structure for reporting empirical findings. We argue that legal AI evaluation should move beyond aggregate accuracy toward clause-specific, failure-mode-driven, and risk-sensitive assessment.

---


### 18. [Correlation-Aware Structured Pruning for Large Language Models](https://arxiv.org/abs/2609.22131)

**<font color=#1a73e8>作者：</font>** Sicheng Xu, Hao Shi, Wei Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured pruning is a promising approach for reducing the substantial inference costs of Large Language Models (LLMs) while maintaining hardware efficiency. Many existing methods assess the importance of prunable units (e.g., channels or heads) in isolation, implicitly assuming that pruning errors are additive. This independence assumption is often invalidated by the non-orthogonality of model weights and strong correlations between unit activations, potentially leading to performance degradation. To address this, we propose a Correlation-Aware Structured Pruning method. We formulate the pruning objective as a cardinality-constrained binary quadratic program that explicitly models cross-unit dependencies in the reconstruction error. Since this binary quadratic program is NP-hard and difficult to solve exactly, we develop a greedy interaction algorithm based on dependency-aware marginal costs to optimize unit selection. Furthermore, we incorporate a gradient-based strategy to achieve adaptive layer-wise sparsity allocation across the entire model. Extensive experiments on mainstream LLMs demonstrate that incorporating correlation information yields competitive accuracy-efficiency trade-offs compared to representative structured pruning baselines.

---


### 19. [Observational Equivalence of LLM and Human Annotation](https://arxiv.org/abs/2609.22133)

**<font color=#1a73e8>作者：</font>** Kentaro Nakamura, Jing Ling Tan, George Yean  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we show that LLM and human coding are observationally equivalent in terms of annotation quality: recent LLMs agree with expert coders at rates comparable to those observed among experts themselves. We demonstrate this through replications of text-classification tasks from 14 peer-reviewed political science studies, in which ten LLMs, three human experts, and 165 crowdsourced workers independently classify the same texts using identical codebooks. We find that this equivalence is driven by ambiguity in the texts and coding rules. When LLMs disagree with experts, experts are also more likely to disagree with one another, and clarifying coding rules reduces disagreement among both experts and sufficiently capable LLMs. Thus, there is little empirical basis for preferring human coding on the basis of annotation quality alone, while LLMs offer substantial advantages in speed and cost. We therefore argue that the central challenge of text annotation is no longer choosing between human and machine coders, but developing coding rules that minimize ambiguity and accounting for the ambiguity that remains. To this end, we propose using disagreement across LLMs to identify difficult cases and refine codebooks, and we develop ambiguity-aware bounds for downstream inference when a unique annotation cannot be defined for every text.

---


### 20. [Read-Best Is Not Steer-Best: A Probing--Steering Layer Dissociation in Omni-Modal Large Language Models](https://arxiv.org/abs/2609.22135)

**<font color=#1a73e8>作者：</font>** Yibo Wang, Jisheng Dang, Bimei Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models integrate text, audio, and image signals into a shared residual stream, where concepts such as emotion can be linearly decoded and causally modified by activation steering. A common but rarely tested assumption is that the layer with the highest probing accuracy is also the best layer for steering, so injection layers are often selected by probe performance. We provide the first causal test of this assumption across three independently developed omni-modal models and find that it fails. Reading and intervention rely on different layers, a phenomenon we call the probing-steering layer dissociation. Using emotion as a controlled testbed, we measure layer-wise readability and steerability across text, audio, and image inputs. Probe-best layers vary widely across architectures, while steering-effective layers consistently fall within a narrow mid-to-late range of normalized depth. Paired random-direction controls show an approximately 26-fold causal gap, ruling out random perturbation and direction quality as explanations. Logit-lens analysis reveals a staged forward process: causal handle, probing saturation, and vocabulary commitment, and motivates a two-factor account in which steering effectiveness depends on both representational readability and downstream plasticity. These results show that probing accuracy is a poor heuristic for selecting intervention layers and suggest a cross-architecture mid-to-late selection criterion. We also identify a cross-modal emotion subspace organized by valence and arousal, with joy acting as a stable anchor across models. Code and data: this https URL.

---


### 21. [Does the Truthfulness Signal Survive Code-Mixing? Probing Hidden States for Hallucination Detection in Hinglish](https://arxiv.org/abs/2609.22138)

**<font color=#1a73e8>作者：</font>** Tanveer Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hidden-state hallucination probing - training a linear classifier on an LLM's internal activations to detect whether a generated answer is faithful to the input - is an active area of 2026 research, with recent work reporting 0.90-1.00 AUROC across several benchmarks and languages. However, none of this work has tested probes on code-mixed input, despite the fact that a huge population of chatbot users write in Hindi-English code-mixed text ("Hinglish"). We address this gap directly: does a hallucination probe trained on clean-language hidden states transfer to Hinglish, or does the signal degrade under code-mixing? We construct a 5,674-item Hindi/English/Hinglish QA benchmark, generate and label 17,022 model responses across three open-weight 7-8B LLMs (Qwen2.5-7B, Mistral-7B, Llama-3.1-8B), extract per-layer hidden states at two token positions, and train linear and MLP probes for in-distribution detection and cross-lingual transfer. We find that the hallucination signal survives code-mixing well: transfer AUROC ranges from 0.88 to 0.99, with gaps of mostly under 0.05 AUROC relative to in-distribution performance, and that Hindi-trained probes transfer to Hinglish more reliably than English-trained probes. As an independent, practically motivated finding, all three models hallucinate substantially more on Hindi and Hinglish than on English for matched facts. We release our code and synthetic Hinglish QA dataset to support further work on code-mixed hallucination detection.

---


### 22. [Using Composition Operators to Linearize LLM Semantic Transformations](https://arxiv.org/abs/2609.22143)

**<font color=#1a73e8>作者：</font>** Afjal Chowdhury, James Chen, Alan Edelman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine learning learns functions: prompt to response, image to caption. What these functions are mathematically remains hard to say. We present a method to approximate these kinds of transformations using techniques from dynamical systems that fall under the umbrella of Koopmanism. We introduce the use of composition operators, which generalize the Koopman operator and, crucially, can map between distinct spaces, motivating the perspective that LLM transformations are rectangular infinite-dimensional operators. This formalism reveals useful structure: under natural assumptions on the prompt and response distributions, the LLM operator is an isometry, and misalignment between learned representations manifests as spectral pollution of its finite sections. We then outline a method of constructing finite-dimensional approximations of an LLM operator, and demonstrate how the singular value spectrum can be used to compare tasks and models.

---


### 23. [Multilingual Safety Signals Are Multi-Layered: Filtering Safety-Degrading Data for Safer LLMs](https://arxiv.org/abs/2609.22144)

**<font color=#1a73e8>作者：</font>** Jiakun Li, Guowei Song, Sijia Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preserving safety alignment during large language models fine-tuning is critical, however, recent studies have demonstrated that even benign fine-tuning data may contain safety-degrading samples that silently undermine safety alignment. Existing approaches typically identify such samples using representations from a single safety-sensitive layer. While this assumption has shown effectiveness in monolingual settings, its validity for multilingual models remains unclear due to potential cross-lingual differences in representation patterns. Through a cross-lingual analysis, we show that sensitive layers are only partially shared across languages, with safety-relevant signals often distributed across multiple layers. Motivated by these observations, we propose MMSAFE, a multi-layer framework for multilingual safety-degrading data identification that captures both shared and language-specific safety signals. Extensive experiments across multiple models, languages, and safety benchmarks demonstrate that MMSAFE reduces the average harmful-response ratio by 60% compared with random filtering and achieves stronger average performance than the strongest single-layer baseline, demonstrating the effectiveness of multi-layer modeling for robust multilingual safety alignment.

---


### 24. [Weak Ties, Strong Signals: Efficient Training Data Detection in Diffusion LLMs via Independent Token Sampling](https://arxiv.org/abs/2609.22145)

**<font color=#1a73e8>作者：</font>** Hongyao Yu, Tianqu Zhuang, Ziyuan Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) offer a compelling alternative to autoregressive models, yet they may expose sensitive training data during denoising. Detecting such usage is challenging because dLLMs lack the efficient one-pass probability decomposition of causal architectures. Existing methods rely on random masking to obtain tractable token-wise detection signals under limited query budgets, but fail to control dependencies among masked tokens. We demonstrate that this token-wise approximation introduces a non-negative structural estimation error, which is theoretically characterized by the cumulative conditional mutual information (CMI) among masked tokens and can obscure subtle memorization signals. This insight suggests that reliable detection requires masked token sets with weak internal dependency. To avoid the prohibitive cost of directly estimating CMI over token combinations, we propose \textit{Independent Token Sampling} (ITS), a query-efficient framework that uses an attention-derived pairwise dependency proxy to approximate the CMI-aware selection criterion. ITS further incorporates a diversity-promoting strategy to improve token coverage across sampling rounds, yielding aggregated token-wise signals that are less affected by dependency-induced approximation error. Experiments on multiple datasets show that ITS consistently outperforms state-of-the-art baselines across different models and datasets, achieving an AUC improvement of 0.18 on the ArXiv dataset while maintaining strong performance under limited query budgets. The code is available at this https URL .

---


### 25. [GRRR: The Geometry of Reshaping, Rotation, and Routing in Decoder LLM post-training](https://arxiv.org/abs/2609.22146)

**<font color=#1a73e8>作者：</font>** Jianing Qi, Hao Tang, Zhigang Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how post-training changes the weights of Large Language Models (LLMs) relative to their pretrained weights. Across 12 post-training chains with supervised fine-tuning (SFT) and reinforcement learning (RL), we express each weight update in the pretrained matrix's singular value decomposition (SVD) frame. This decomposition separates the changes of three geometrically distinct components: diagonal values, which reshapes singular values; off-diagonal values, which rotates the coupling between pretrained input and output directions; and null-space values, which routes outside the matrix's original nonzero SVD core. On a math evaluation suite, we find that removing the diagonal component usually preserves most of the gains from post-training. These results suggest that post-training gains are carried primarily by reconfiguring and extending pretrained pathways rather than by substantially changing singular values of pre-trained models.

---


### 26. [Beyond the Stitching Assumption: A Unified Framework for Multimodal Synthetic Data Evaluation via Semantic Quantization](https://arxiv.org/abs/2609.22149)

**<font color=#1a73e8>作者：</font>** Yefeng Yuan, Zhan Shi, Liang Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal synthetic datasets combine structured attributes with free text, but are often evaluated separately. Such metrics can remain high after tabular--text pairings are disrupted. We present a projection-based evaluator for tabular--text synthetic data. A fixed sentence encoder maps text to embeddings, \(k\)-means converts them to cluster states, and tabular variables are represented as categorical or quantile-binned states. Real and synthetic contingency tables are compared using Jensen--Shannon divergence (JSD), normalized mutual information (NMI), conditional JSD (cJSD), and joint-state entropy. We also report text-to-attribute (T2A) utility and a holdout-calibrated proximity flag rate (PFR) as a representation-level diagnostic. A text-permutation control preserves both marginal distributions while disrupting their pairing. Experiments on Amazon Reviews, Kiva Loans, and the Employment Scam Aegean Dataset show that modality-specific scores remain high under this control. The projection diagnostics detect disruption when real projected dependence exceeds a permutation baseline, but are less informative for weak or sparse projections. Some conditioned LLM baselines also exhibit stronger measured dependence than the corresponding real-data projections. These results support explicit cross-modal evaluation with permutation baselines and coverage reporting.

---


### 27. [Do Language Models Know Their Own Constraints?](https://arxiv.org/abs/2609.22151)

**<font color=#1a73e8>作者：</font>** Arin Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We ask whether behavioral constraints acquired through post training remain explicitly reportable. Using constrained recipe generation as a testbed, five banned ingredients enforced via LoRA fine tuning of Llama 3.1 8B Instruct we compare supervised fine tuning (SFT) and Group Relative Policy Optimization (GRPO) against an untrained baseline on a four tier Constraint Awareness Benchmark. Averaged over three seeds, both methods raise behavioral compliance from 4% to about 90% while reducing explicit constraint reporting below the untrained model (0.48/5 to 0.16/5 for SFT, 0.07/5 for GRPO) and eroding retained third person knowledge (93% to 36% for SFT, 14% for GRPO; p less than 0.01 between methods). Contrary to our initial hypothesis, the reward based signal is the more destructive of the two: a reward that penalizes banned ingredient tokens regardless of framing learns a context independent suppression rather than a self directed constraint. A context conditioned reward designed to teach the self to other distinction fails, collapsing toward inclusion in both framings. Probing prompt time hidden states recovers per ingredient avoidance at 83.8% (layer 24 MLP), but only 6.4 points above a per ingredient base rate predictor (77.4%), and the model's own verbal self report is more accurate still (87.8%). A positive control adding explicit self description examples does not restore reporting. The failure is therefore specific to enumerating constraints on request, not a general loss of access to them.

---


### 28. [Is Imagination Derived from Hallucination? A Cross-Taxonomy Evaluation of Imagination and Hallucination in Large Language Models](https://arxiv.org/abs/2609.22152)

**<font color=#1a73e8>作者：</font>** Zixuan Tang, Hongzong Li, Shuxin Zhuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Imagination performs as a high-level function of large language models (LLMs) which determines the potential of how an LLM creates unseen or creative content. While existing works have built a rich family of creativity benchmarks for this ability, they only measure how far an output departs from common answers and never check whether the departure is licensed by the prompt. Moreover, hallucination, the closest neighbor of imagination, is always measured in a separate pipeline on different generations, so the influential claim that imagination and hallucination stem from the same generative mechanism has never been directly testable. In this paper, we propose Whiteboard, the first LLM imagination evaluation benchmark. Its design follows the authoritative cognitive instruments developed to measure human imagination: seven mechanism-grounded imagination subtypes are adapted from classic paradigms, then crossed with ten support-boundary hallucination subtypes and scored jointly on the same generation. Different from previous creativity or hallucination benchmarks, Whiteboard gates every imagination score with an explicit support check and computes both axes deterministically through an auditable atom matrix, with no LLM judge on the primary path. The full Whiteboard item bank contains 1,660 prompts; on its shared 80-item anchor set, we evaluate 79 state-of-the-art LLMs and validate the instrument against 13,280 human judgments. Additionally, we further explore whether imagination derives from the same generative tendency as hallucination and what key factors shape it. Our analysis indicates a counterintuitive correlation between hallucination and imagination: Most of the subtype couplings are negative, every one of the anchor items reproduces the negative coupling on its own.

---


### 29. [SafeTune: A Unified Faithful Library for Auditing and Repairing Safety Drift in Fine-Tuned LLMs](https://arxiv.org/abs/2609.22153)

**<font color=#1a73e8>作者：</font>** Pratinav Seth, Saisab Sadhu, Anshul Kaushal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Methods for addressing safety drift in fine-tuned Large Language Models (LLMs) are scattered across incompatible implementations, lifecycle stages, and evaluation protocols, making them difficult to adopt and compare. We introduce SafeTune, a source-available library that unifies four intervention paradigms: post-hoc weight recovery, safety-constrained fine-tuning, gradient-based unlearning, and inference-time steering, alongside shared interpretability, evaluation, and deployment utilities. SafeTune provides a consistent configuration-driven workflow while preserving the distinct inputs and intervention points each paradigm requires. Its modular registry supports new methods, benchmarks, judges, models, and fine-tuning domains without redesigning the surrounding pipeline. We demonstrate SafeTune through controlled comparisons and finance and medical deployment case studies, showing how it characterizes safety drift, evaluates feasible interventions on common refusal-behavior and capability evaluations, and supports calibrated or layered mitigation.

---


### 30. [The Limits of Speculation: Bounding Speculative Decoding in Mixture-of-Experts](https://arxiv.org/abs/2609.22156)

**<font color=#1a73e8>作者：</font>** Aidar Amankulov, Denis Mamatin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding in Mixture-of-Experts (MoE) models faces the problem of unstable verification cost caused by input-dependent expert loading. To study the physics of this process, we formulate speculation-budget selection as an offline Stochastic Shortest Path (SSP) problem over reference sequences and build a diagnostic Oracle that uses counterfactual simulation to account for MoE verification cost. A detailed analysis of the Oracle's decisions on the Qwen3-Coder and EAGLE-3 pairing, in the space of marginal deltas (Delta Space), shows that rejected candidates form a strict linear boundary. This result demonstrates that a complex global optimization is locally governed by a necessary condition balancing marginal cost against expected progress ($\frac{\Delta \mathbb{E}[Cost]}{\Delta \mathbb{E}[a]}$), providing a rigorous mathematical reference point for designing future adaptive online heuristics.

---


### 31. [PAGE: Partition-Aware Gated KV-Cache Eviction](https://arxiv.org/abs/2609.22157)

**<font color=#1a73e8>作者：</font>** Pankaj Kumar, Subhankar Mishra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV-cache eviction methods decide which tokens to keep but not whether to evict at all, so a benchmark mean can hide a class of inputs on which compression drives accuracy from 99\% to 0\%. We reframe eviction as a per-input admission decision and show that inputs separate into a capacity-bound class, where eviction is catastrophic at every budget, and a dilution-prone class, where eviction is safe or beneficial. A single label-free scalar computed from prefill attention, the early-to-late drop in pairwise top-$k$ head agreement, predicts this class before any decoding. PAGE thresholds this drop: it applies any base evictor when the drop is large and retains the full cache otherwise, with no training and no accuracy labels. The drop orders inputs by eviction safety consistently across four architecture families, and a per-model unlabeled pilot of about 100 inputs recalibrates the threshold for a new family. Used as a safeguard, PAGE cuts the harm rate on the capacity-bound regime from 0.75 to 0.026, a 29 $\times$ reduction, across four evictors, four models, and two benchmarks, turning a 99\% to 0\% collapse into a flat 89\% without retraining the evictor. The gate is inert wherever eviction is already safe, and the capacity-bound class it protects is a small, identifiable minority of inputs, so the benefit is a targeted safety gain rather than an average one. PAGE is a per-input safeguard, not a compressor: realized compression is $1.8 - 3.4 \times$ (mean 2.9$\times$) against a nominal 16$\times$ budget and decays toward unity by batch 16 under static provisioning, and a trained evictor wins at matched memory.

---


### 32. [StepKV: Step-Aware KV Cache Compression for LLM Agents](https://arxiv.org/abs/2609.22158)

**<font color=#1a73e8>作者：</font>** Boyu Feng, Jiahong Liu, Yifan Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) caching is essential for efficient autoregressive large language model (LLM) inference, but the cache grows linearly with context length, increasing storage and decoding costs. KV cache compression mitigates this cost by retaining only a subset of cached tokens. This challenge is particularly important for multi-step LLM agents, where a query expands into trajectories of reasoning, tool interactions, and retrieved observations. Existing pruning methods typically treat the cache as a flat token stream and rank tokens by recency or attention saliency. This creates a mismatch between the unit of compression and the unit of reasoning: token-level pruning removes individual entries, whereas useful information in multi-step agents is often organized into reasoning steps with uneven and delayed importance. Consequently, an early observation or intermediate decision may receive little recent attention yet remain essential for later evidence synthesis. We term this failure mode Reasoning Continuity this http URL observations motivate KV cache compression that jointly considers token- and reasoning-step-level information. StepKV addresses this goal by treating reasoning steps as first-class retention units. It associates cache entries with their generating steps, estimates step utility from trajectory-derived signals, and combines this utility with token-level saliency. The resulting scores globally rank prunable tokens, from which StepKV retains the top-scoring entries under a target budget. StepKV thus provides a step-centric perspective for agent KV cache compression. Across multi-hop QA and long-horizon web reasoning tasks, StepKV sustains accuracy under low KV budgets where token-level baselines degrade sharply, offering a more robust efficiency-accuracy trade-off for multi-step agent inference.

---


### 33. [Didactic knowledge or Clinical Cases? How Data Types Shape Medical Large Language Models](https://arxiv.org/abs/2609.22161)

**<font color=#1a73e8>作者：</font>** Yuzheng Fan, Haochun Wang, Sendong Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical large language models are commonly trained on mixtures of didactic data (e.g., textbooks) and clinical data (e.g., patient records), yet how these data types differentially shape model capabilities remains unclear. We address this issue with token-matched experiments that vary the didactic-to-clinical ratio and analyze how data composition affects performance, capability profiles, and error patterns across knowledge-intensive and clinic-oriented tasks. We uncover an asymmetric transfer across task types: clinical data improves clinic-oriented tasks while remaining competitive on knowledge-intensive ones, whereas didactic data mainly improves knowledge-intensive tasks. Error analysis suggests a knowing-doing gap, where improvements in knowledge recall do not reliably generalize to clinical reasoning. We further observe that modest amounts of clinical data yield most of the gains on EHR-grounded tasks, while the optimal mixture ratio varies with the knowledge and clinical reasoning demands of downstream tasks. These findings suggest that medical LLM data curation should be application-driven, with higher proportions of clinical data preferred for reasoning-intensive use cases.

---


### 34. [Beyond Raw Context Transfer: Representation-based Federated Retrieval-Augmented Generation](https://arxiv.org/abs/2609.22162)

**<font color=#1a73e8>作者：</font>** Can Peng, Yu Liu, Yingyu Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) improves the factuality of large language models (LLMs) and vision-language models (VLMs) by grounding generation in external knowledge. However, most existing RAG frameworks assume a centralized retrieval corpus, which is often impractical in sensitive domains such as healthcare, where data are inherently distributed and raw content cannot be directly shared across institutions. Recent efforts on decentralized RAG primarily follow prompt-based paradigms that exchange raw, human-readable retrieved content, leading to substantial inference-time computational overhead and direct exposure of retrieved information. To address these limitations, we propose Representation-based Federated RAG (FedRepRAG), a decentralized RAG framework that keeps raw documents at their owning clients and exchanges only compact latent representations during cross-client retrieval. To integrate retrieved knowledge, we introduce a collaboratively trained projector that converts retrieval embeddings into generator-compatible representation tokens for a frozen LLM/VLM backbone. Experiments across decentralized visual question answering (VQA) and question answering (QA) benchmarks show that FedRepRAG consistently outperforms direct inference and local retrieval baselines while substantially reducing retrieval-context length and inference-time computational overhead compared with raw-context transfer. Further analyses confirm the importance of query-relevant retrieved representations and characterize the residual representation-level leakage associated with representation exchange. Overall, FedRepRAG provides an effective and efficient framework for federated RAG without transferring raw retrieved content.

---


### 35. [MechaTerp-TRACE: A Novel Approach for Component Ablation Analysis in Language Models](https://arxiv.org/abs/2609.22163)

**<font color=#1a73e8>作者：</font>** Brandon Colelough, Davis Bartels, Madeline Bittner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpretability research on large language models has produced accounts of factual recall in feed-forward layers and of token relationships in self-attention, but little work offers a unified way to compare the causal contribution of different architecture components to a model's output. We introduce MechaTerp (the Mechanistic Interpretability suite) -TRACE (subset for Teacher-forced Registry of Ablated Component Effects), an architecture and study that measures how much each registered component of a language model supports the production of a named entity. TRACE ablates one component at a time and measures the resulting change in the output distribution at a fixed answer token, so component types from whole transformer blocks down to individual neurons and output logits can be compared on a common scale. We apply it to thirteen instruction-tuned dense decoder models spanning five families and one to thirty billion parameters, ablating 49,656 components across 48 medical and 42 general-knowledge prompts. We find that the components carrying the most effect are the same few, positionally fixed components in every model, regardless of which entity a prompt asks about, and that once these are removed, the remaining support is close to evenly spread in eleven of the thirteen models. Apparent localisation of entity knowledge is therefore largely attributable to generic generation machinery, which has direct consequences for methods that assume entity knowledge sits in a findable place, including targeted knowledge editing.

---


### 36. [Monocultural Biases: Correlated biases in large language models lead to unequal systemic exclusion rates in hiring](https://arxiv.org/abs/2609.22169)

**<font color=#1a73e8>作者：</font>** Matthew Bone, Fabian Stephany, Maria del Rio-Chanona  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Employers are increasingly using large language models (LLMs) to automate their hiring process. This paper investigates the risk of monocultural biases, in which the widespread deployment of large language models homogenizes biases across the labor market, leading to greater systemic exclusion for certain demographic groups. For ten LLMs, we measure hiring biases across their base and post-trained versions to identify which stage, pre-training or post-training, lead to monocultural biases. We find that, compared to their base models, post-trained models are 3.6% less likely to callback older applicants. This negative shift occurs in eight of the ten models that we evaluate. Post-trained models have much more correlated decisions than base models which is likely driven by human capital traits like skills or college major. However, greater consensus among models increases global systemic exclusion rates from 5.6% to 17.3% and exacerbates demographic inequalities, with intersectional systemic exclusion rates ranging from 12.2% to 21.7% for post-trained models. We find that this inequality is primarily driven by age-based discrimination that is exacerbated in post-training. These results indicate that while post-training techniques may improve models' abilities to select the best applicants, they may raise systemic inequality risks for those at the margin by uniformly introducing new biases.

---


### 37. [Multiple latent orderings better predict language model preferences](https://arxiv.org/abs/2609.22170)

**<font color=#1a73e8>作者：</font>** Aviral Chawla, William H.W. Thompson, Jean-Gabriel Young  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are frequently employed in settings where they are asked to make value judgments and choices. These observed choices often exhibit intransitivity: A model may prefer item $A$ to $B$ and $B$ to $C$, while also preferring $C$ to $A$. Existing work that models LLM preferences treats such inconsistencies as sampling noise around a single latent ordering. We instead propose that intransitivity reflects the aggregation of multiple latent, internally consistent orderings. We first show that observed inconsistencies cannot be explained by a single ordering under any monotone link function. We then introduce a noise-augmented mixture Bradley-Terry (MBT) model that infers latent preference components from repeated pairwise comparisons. Across seven models and four tasks, a mixture of orderings often explains structural inconsistencies better than single-utility models. We find that aggregate preferences often hide underlying preference heterogeneity. A case study on Moral Machine dilemmas shows that models which disagree on aggregate orderings can still share latent components. Together, these results suggest that LLMs reflect plural preferences. Alignment and evaluation pipelines that treat LLM preferences as a single function, therefore, risk averaging over coherent orderings that different users may endorse differently.

---


### 38. [Quantifying Hidden Salt for Precision Healthcare: Sodium Assessment via Joint-Factor Retrieval and Chain-of-Thought Inference](https://arxiv.org/abs/2609.22171)

**<font color=#1a73e8>作者：</font>** Mingyu Huang, Weiqing Min, Yuehui Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Precision healthcare, particularly for conditions like hypertension and cardiovascular disease, necessitates monitoring of dietary sodium intake. However, tracking this is hindered by the prevalence of hidden salt in cooking, such as sodium in soy sauce and ketchup. While recipes offer a valuable data source for dietary analysis, sodium-rich seasonings are frequently omitted or described ambiguously in instructions. To solve this issue, we propose SALT, a Sodium Assessing & Level Tracking framework adopting an RAG framework to assess sodium content in recipes. Our framework first introduces a Joint-Factor Embedding Retrieval module to locate similar recipes with specified sodium content for addressing the lack of contextual references. These retrieved samples provide contexts for subsequent inference. Then we design a structured 4-hop Chain-of-Thought inference module to refine the vague estimation from language models through a multi-step sodium estimation. To facilitate our study, we further construct a recipe dataset SALT54k with $54,151$ entries labeled with sodium quantities across $11$ common seasonings. Results on SALT54k demonstrate that our method achieves state-of-the-art performance in sodium estimation. Additional real-world validations confirm the effectiveness of our method, demonstrating its potential as a practical solution for AI-assisted precision healthcare.

---


### 39. [Beyond Task Completion: Training Capable and Safe Computer-Use Agents](https://arxiv.org/abs/2609.22178)

**<font color=#1a73e8>作者：</font>** Zeyu Kang, Zhenyun Yin, Yang Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) have made rapid progress in completing complex tasks through graphical user interfaces, yet post-training centered on task success alone does not induce reliable safety behavior. A reliable CUA must condition its execution on risk: it should complete ordinary benign tasks, avoid environmental hazards and continue when a safe completion path remains, and refuse when the goal is harmful or no safe path exists. To learn this conditional policy, we develop Safety and Capability Optimization for Policy Execution (SCOPE), which jointly post-trains a CUA for task-execution capability and safety-aware decision making. To provide aligned training data for this joint objective, we further introduce SCOPE-Gen, an automated pipeline that synthesizes verifiable capability tasks and converts them into paired environment-risk variants while preserving their original goals. Using the resulting tasks, we construct SATraj-OS, a trajectory dataset comprising capability demonstrations, safe continuations, and explicit refusals. SCOPE first learns from all three trajectory types through supervised fine-tuning and then further improves task completion through online reinforcement learning. Starting from Qwen3.5-9B, SCOPE-RL achieves a 54.17% task success rate on OSWorld and a 64.30% attack-avoidance rate on OS-BLIND, yielding the best aggregate capability--safety score of 58.80% among the evaluated agents. Ablations reveal asymmetric but complementary roles for the two forms of safety supervision: refusal trajectories account for most of the attack-avoidance gain, whereas risk-handling trajectories preserve greater task utility at comparable attack-avoidance levels.

---


### 40. [DPTM-DT: Dual-Pretrained Transformer Multitask Representation Learning for Drug-Target Prediction](https://arxiv.org/abs/2609.22184)

**<font color=#1a73e8>作者：</font>** Ge Kong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug-target relation prediction supports candidate screening, drug repositioning, and mechanism analysis. Existing models often use incomplete drug or protein representations, model cross-modal interactions shallowly, or train affinity regression and interaction classification separately, although these tasks describe closely related views of the same drug-target pair. This paper presents DPTM-DT, a dual-pretrained Transformer framework for multitask drug-target prediction. DPTM-DT combines GROVER molecular graph embeddings, ESM protein language-model embeddings, and CTD physicochemical descriptors, then exchanges drug-target information through bidirectional cross-modal attention. A shared pair representation is used for continuous affinity regression, high-affinity binary classification, and six-level affinity classification. Experiments on Davis and KIBA cover random 80/20 and DeepDTA-style standard splits. On the random 80/20 split, DPTM-DT achieves MSE/CI values of 0.193/0.917 on Davis and 0.120/0.918 on KIBA. It also reports binary AUPR/MCC values of 0.727/0.654 and 0.798/0.689, and six-class Macro-F1/Top-2 values of 0.800/0.932 and 0.815/0.962 on Davis and KIBA, respectively. Across the reported regression, binary classification, and multiclass classification settings, DPTM-DT achieves the best overall performance among the compared methods. Results under the standard split show the same relative trend. Ablations indicate that dual target representation, gated fusion, and cross-modal attention each contribute to the final performance. Code and supplementary materials are available at: this http URL.

---


### 41. [Fairness Beyond Anonymization? Demographic Leakage in German LLM-Generated Resumes](https://arxiv.org/abs/2609.22188)

**<font color=#1a73e8>作者：</font>** Charlotte Leininger, Helena Veit, Matthias Aßenmacher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into AI-assisted hiring pipelines, including automated resume generation and screening. Under the EU AI Act, the hiring domain is classified as high-risk, making fairness and transparency critical requirements. Existing work has primarily focused on explicit hiring decisions, while less attention has been paid to whether generated resumes themselves encode recoverable demographic information. In this work, we conduct a two-stage audit of demographic leakage in German-language LLM-generated resumes. First, we use ChatGPT (GPT-4o-mini), Gemini 2.5 Flash-Lite, and multiple scales of the open-weight Qwen 3 model family (4B, 8B, and 14B) to generate resumes from real anonymized job-matching profiles, systematically varying gender- and ethnicity-associated names while holding qualifications constant. Second, we simulate a downstream resume screening scenario, where the generated resumes are first anonymized and gender-neutralized, before demographic leakage classifiers are trained on the resulting texts. We find that, despite these interventions, classifiers reliably distinguish between resumes generated with male and female names. This leakage is not driven by overtly gendered wording, but by subtle differences in the usage of semantically equivalent, formally gender-neutral terms in German. In contrast, ethnicity-related leakage remains comparatively weak across models. Our findings demonstrate that apparently neutral resume generation can still preserve highly predictive demographic signals, raising concerns about anonymization-based fairness interventions in multilingual AI hiring pipelines.

---


### 42. [A Pinch of SFT, A Dash of RL: When Reinforcement Learning Helps Long-Horizon Advertising Agents](https://arxiv.org/abs/2609.22194)

**<font color=#1a73e8>作者：</font>** Aakash Kolekar, Sahika Genc, Bunyamin Sisman 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enterprise analytics agents solve long-horizon tool-use problems over distributed business data, requiring retrieval, reasoning, API calls, code execution, and adaptation to intermediate observations. Supervised fine-tuning (SFT) calibrates tool syntax and teacher-supported behavior, whereas reinforcement learning (RL) can explore reward-supported behaviors beyond demonstrations; applied uniformly, however, RL can perturb already-calibrated skills. We study how to balance SFT and RL under production-mirroring beta APIs. We observe that, in our controlled experiment, checkpoint trajectories retrospectively separated into three regimes: Imitation, where SFT captured reliable teacher behavior; Lift, where both stages helped; and Discovery, where useful reward-observable behavior lay outside reliable teacher support. We leverage this prospectively, using teacher support and reward-observable headroom to route features to SFT only, SFT then RL, increased RL allocation, or further environment development. Across 18 subsequent feature-specific experiments, the diagnostic predicted 15/18 observed trajectories. On GPT-OSS 120B, targeted SFT then RL produced positive point estimates on 7/8 advertiser skills relative to a frontier Control; five positive gains had paired 95% confidence intervals excluding zero, while one skill had a confidence-supported regression. The largest gain was non-disclosure (+11.27 points; 95% CI [+9.72, +12.82]). A separate SME audit surfaced that targeted RL reduces standard leakage from 11.8% to 2.9% and adversarial leakage from 22.9% to 6.8% relative to SFT while preserving actionability (86.2% to 85.7%). In a matched uniform-versus-targeted comparison with shared rewards and optimization, targeted RL improved the seven-skill mean delta from +1.62 to +3.57 while using 43% less incremental RL compute.

---


### 43. [The Situated Identity Test: Distinguishing Persistent Cognitive Identity from Persona Imitation](https://arxiv.org/abs/2609.22195)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can convincingly adopt personas, recall past dialogues, and weave rich autobiographies. Yet this conversational eloquence conceals a fundamental attribution problem: looking the part does not mean having lived the life. Two individuals can share identical public profiles--the same age, hometown, occupation, and personality traits--while possessing entirely distinct private histories, relationships, and acquired skills. When conditioned solely on that shared profile, an agent lacks the information required to determine which lineage is correct. We introduce the Situated Identity Test (SIT), an architecture-independent framework that evaluates whether an agent's behavior is functionally attributable to a specific developmental lineage. Grounded identity requires both appropriate knowledge of recorded experiences and appropriate ignorance of ungrounded ones, bounded by what the identity has actually acquired rather than what its underlying foundation model knows. We prove that any policy conditioned solely on a compressed profile is bounded by an average situated validity of at most 1/m across m colliding life histories on lineage-discriminative queries (at most 50% for paired lineages). We instantiate this framework in SITBench, an evaluation suite designed for 25 profile-collision pairs (50 distinct lineages) across 10,000 planned probes and nine architectural configurations. Supported by an open-source reference implementation, deterministic test fixtures, and empirical pilot evaluations on frontier foundation models (GPT-5.6 Sol and Claude Opus 5), we formalize the failure modes of persona prompting under profile collision and provide an assurance harness for evaluating episodic continuity, structured state, and epistemic boundaries.

---


### 44. [EvoRank: LLM-Guided Evolution of Multi-Objective Learning-to-Rank Pipelines](https://arxiv.org/abs/2609.22196)

**<font color=#1a73e8>作者：</font>** Rayhan Patel, Shabaz Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present EvoRank, an open autonomous ranking engineer: an LLM-guided evolutionary loop that discovers complete Learning-to-Rank pipelines (features, models, losses, ensembles) for multi-objective e-commerce search. On the Expedia ICDM 2013 dataset, with relevance, conversion, and revenue as competing objectives, three independent runs each converge within 50 iterations (about ten dollars) on interpretable pipelines that beat an Optuna-tuned LambdaMART on 60k held-out queries, an advantage that persists at full data scale and places in the top 6 percent of the original competition. A first campaign, evolving only training objectives, builds the central design rule: it appeared to work on its selection fold (the small dataset it uses to pick winners) while a transfer audit, re-scoring winners on held-out data, showed the gains were almost entirely fitness noise (the randomness of its own scoring), and neither seeded domain knowledge nor richer diagnostic feedback changed what transferred. The deciding quantity is measurable in advance: search-space headroom relative to fitness noise. We package this as a headroom gate that predicts, before any LLM spend, whether the loop will pay off, and we release the system, the auditing tools, and a catalog of failure modes with their guardrails, so teams can apply the procedure to their own ranking stacks.

---


### 45. [Dissecting Hierarchical Reasoning Models: A Mechanistic Study](https://arxiv.org/abs/2609.22197)

**<font color=#1a73e8>作者：</font>** Leo Raphael Rodrigues, Jian Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study Hierarchical Reasoning Model (HRM), a representative hierarchical Transformer-based latent reasoning model with many variants, on Sudoku, Maze, and ARC-AGI-2. We mechanistically understand how HRM reasons and what information it encodes. Our analyses compare HRM against Transformer baselines with and without recurrent modules, apply causal interventions on recurrent states, and utilize linear probes against random-direction ablations, as well as sparse autoencoders with feature ablations. Our results reveal several key findings: recurrent models outperform one-pass baselines, while single-state recurrent Transformers are comparable to HRM. State interventions further show that the causal contributions of the high- and low-level states vary across task-specific checkpoints and inference stages. Selected task variables are linearly decodable from the recurrent states in HRM, yet ablating probe directions produce effects comparable to random controls. SAE ablations yield larger behavioral changes than probe-direction ablations. However, top-ranked SAE features show no stable advantage over size-matched random subsets at larger ablation sizes or across tasks; the same pattern persists in a Sudoku control with within-step BPTT. Together, we characterize that HRM is essentially implementing constraint-aware iterative refinement on a puzzle-specific solution state, in which the functional contributions of components at different levels vary without relying on a compact, causally important feature set. These results highlight the necessity of studying the different working mechanisms and the importance of developing mechanistic interpretability techniques better suited for latent-space, recursive reasoning models.

---


### 46. [The Role of AI in Online Reviews](https://arxiv.org/abs/2609.22198)

**<font color=#1a73e8>作者：</font>** Valeria Lerman, Oren Rigbi, Yaniv Dover  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of large language models (LLMs) creates new opportunities for strategic content generation on online platforms, including potentially harmful forms of manipulation that may undermine platform effectiveness and reshape platform dynamics. However, measuring such activity is difficult because AI-generated content is rarely directly observable. We introduce an empirical approach that leverages discrete LLM supply shocks - abrupt changes in model prices and capabilities, and contrasts verified with non-verified reviews to identify changes in platform activity associated with generative AI supply improvements. We apply this approach to more than 13 million reviews from Trustpilot, one of the leading online platforms for business reviews. A robust finding is that following LLM supply shocks, unverified reviews shift toward greater negativity: more 1-stars, fewer 5-stars, and lower ratings, with effects driven primarily by new model releases and concentrated among firms with the lowest and highest review volumes, suggesting that strategic AI use may reshape platform competition dynamics. We further find that LLM supply shocks trigger short, concentrated bursts of review activity. Together, these findings suggest that generative AI is already reshaping how reputation and competition operate on online platforms.

---


### 47. [Improving Parameter Utilization by Sharing Neural Experts Across Layers in Transformers](https://arxiv.org/abs/2609.22199)

**<font color=#1a73e8>作者：</font>** Dian Jiao, Jiaxin Duan, Shuai Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based large language models often suffer from inter-layer parameter redundancy, where functional transformations are redundantly learned across network depths. We propose CS-MoE, a novel Transformer architecture featuring cross-layer expert sharing to address this inefficiency. Deviating from the widely used Mixture-of-Experts (MoE) architecture that terminates each Transformer block with layer-isolated experts, CS-MoE combines layer-independent experts with concurrent access to a centralized, globally shared expert pool. This \textit{Global Experts Sharing} mechanism enables elastic control over token-level parameter activation and computational consumption (FLOPs). Experiments demonstrate that CS-MoE achieves lower perplexity than equal-scale dense Transformers while activating only 55\% of parameters. Furthermore, its performance scales monotonically with an increased number of activated experts and approaches MoE counterparts that consume more FLOPs by expanding the shared pool with a fixed FLOPs budget. CS-MoE also establishes a flexible Pareto frontier between computational cost and model capacity, offering an efficient alternative for computation-constrained environments.

---


### 48. [PII-TRACE: A Benchmark for Context-Aware PII Detection in Multi-Turn LLM Conversations](https://arxiv.org/abs/2609.22200)

**<font color=#1a73e8>作者：</font>** Kaiyuan Zhang, Chuan Wang, Joey Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM assistants and agentic systems log long multi-turn conversations. AI providers often scan these conversations for Personally Identifiable Information (PII) and mask the PII before storing or processing conversation data. Yet most PII detectors and benchmarks target self-contained records rather than cross-turn evaluation. To evaluate PII detection across turns in multi-turn conversations, we introduce PII-TRACE (Tracing Recurring PII Across Conversational Exchanges), to our knowledge the first PII benchmark to assess whether detectors identify PII in conversational contexts and cover every mention of a recurring identifier across turns. PII-TRACE contains 13,148 synthetic multi-turn dialogues in 13 languages with character-level spans and identifier clusters. Across eleven baselines, including frontier LLMs, no detector achieves full entity-level coverage without substantial false positives on PII-free conversations, and single-pass reading loses a third of the gold characters on long dialogues. To close this gap, we introduce PII-Tracer, a compact 0.6B-parameter detector trained with conversation-level supervision. PII-Tracer attains the highest entity-level coverage of any system we evaluate and also performs strongly on standard single-record benchmarks.

---


### 49. [Evaluating Personal Information Output from Conversational Interactions in Generative AI Systems](https://arxiv.org/abs/2609.22204)

**<font color=#1a73e8>作者：</font>** Yosuke Seki, Hirotaka Tahara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This exploratory pilot study evaluates the scope and perceived accuracy of personal information output from ongoing conversational interactions in generative AI systems using GPT-5.2 Instant and GPT-5.2 Thinking, categorized into three output types: Fact, Inference, and Confidence. Based on the evaluation results obtained from 15 Japanese participants, differences in model design have limited impact on personal information output tendencies. Compared with the Inference type, the Fact type shows a more conservative output pattern. Regarding attribute categories, the findings indicate that Core Personal attributes associated with identification are treated relatively conservatively, whereas Behavioral and Linguistic attributes show higher accuracy across both Fact and Inference outputs. Furthermore, Holistic Profile, Psychological and Cognitive, and Residual attributes are more readily inferred, even when not supported by explicit factual outputs. Notably, the lack of null outputs for these attributes in the Inference type suggests that such inferred profiles may be constructed from indirectly available contextual information. The findings may contribute to future discussions regarding privacy awareness and personal information inference in generative AI systems.

---


### 50. [Dissecting Training-Free Uncertainty Estimation in Multimodal Large Language Models](https://arxiv.org/abs/2609.22206)

**<font color=#1a73e8>作者：</font>** Soroush Seifi, Vaggelis Dorovatas, Lin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable performance across a wide range of multimodal tasks, yet understanding and quantifying their predictive uncertainty remains underexplored despite being central for safety critical applications. In this work, we present a systematic study of training-free uncertainty quantification strategies for MLLMs, categorizing existing approaches into three conceptual families: token-level methods, which operate directly in the text output space; verbalized methods, which elicit uncertainty estimates or abstention signals via natural language prompts; and semantic methods, which measure uncertainty in a semantic meaning space. We benchmark these strategies across multiple datasets, model families, generations, and scales, and find that no single family dominates: token-level entropy (at sampling temperature 1.0) wins on short answers, verbalized abstention on sentence-length responses, and semantic methods on long-form generation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-379](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
