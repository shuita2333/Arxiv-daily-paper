# 🧠 大模型相关研究 | 2026年11月26日

> 本类共 **299** 篇论文：已确认 **280** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-299](./part-06.md)

---

### 1. [Validation Bias in Large Language Model Responses to Cancer Treatment Queries: A Factorial Cross-Sectional Study](https://arxiv.org/abs/2611.31251)

**<font color=#1a73e8>作者：</font>** Ramez Kouzy, Saketh Vinjamuri, Sarah Ghalayini 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) chatbots are increasingly used by patients seeking cancer information, but their safety when users present evidence-misaligned beliefs about treatment remains uncharacterized. We hypothesized that LLMs exhibit validation bias, affirming rather than correcting such beliefs, and evaluated this with a 2x2x2 factorial design crossing conversation format (single-turn vs multi-turn), treatment type (evidence-based vs alternative), and query valence (positive vs negative). Framing was evidence-aligned (supporting evidence-based treatments or questioning alternative therapies) or evidence-misaligned (promoting alternative treatments or questioning evidence-based therapies). We analyzed 1,272 conversations (6,360 interactions) across 14 LLMs from 6 vendors, scored by an LLM judge (GPT-5-mini) validated against human annotation on a 6-dimension safety rubric. The primary outcome was the unsafe response rate, defined as a Weak classification or any critical failure. Evidence-misaligned framing increased unsafe response rates compared with evidence-aligned framing (14.4% vs 5.1%; OR 3.14, 95% CI 2.07-4.78; P < .001), and the association persisted after accounting for clustering by LLM. Among 429 conversations classified as Strong under evidence-aligned framing, 22.6% were downgraded in their paired evidence-misaligned counterpart. Multi-turn conversations had lower unsafe response rates than single-turn conversations (5.2% vs 14.7%; P < .001). Unsafe response rates varied by vendor from 1.8% to 36.8%. LLMs exhibited significant validation bias in oncology, with unsafe responses nearly tripling under evidence-misaligned framing. Evaluations limited to neutral, fact-seeking queries may overestimate real-world safety, and safety testing of medical AI systems should include evidence-misaligned user framing.

---


### 2. [DAGGER: Deployment-Free Quality Estimation for Generative AI Workflows](https://arxiv.org/abs/2611.31252)

**<font color=#1a73e8>作者：</font>** Dimitrios Liakopoulos, Neeraja J. Yadwadkar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Estimating the quality of generative AI workflows is challenging because these workflows comprise multiple stages, and errors can propagate across them, making end-to-end performance depend not only on the accuracy of individual models but also on how their outputs affect downstream stages. Each stage can use one of many candidate models. Estimating end-to-end workflow quality by deploying and evaluating every resulting model configuration is therefore prohibitively expensive. As a result, existing approaches face a tradeoff between estimation cost and accuracy: inexpensive methods often produce unreliable quality estimates, while accurate methods require deploying and evaluating many workflow configurations. In this paper, we introduce DAGGER, a framework for estimating the quality of generative AI workflows without exhaustive deployment and profiling. DAGGER represents a workflow as a graph, in which nodes correspond to stages and edges capture how outputs from one stage affect subsequent stages. It then decomposes workflow quality into per-node accuracy terms and per-edge dependency terms. Using a novel analytical formulation and SVD-based matrix completion, DAGGER estimates workflow quality from sparse observations without executing every candidate workflow. We evaluate DAGGER on three generative AI workflows across three datasets. DAGGER estimates workflow quality with a median error of 6.8 percentage points while reducing profiling cost by 10.2$\times$ relative to BenchPress, a state-of-the-art baseline, and selects workflow configurations competitive with state-of-the-art frameworks such as LLMSelector.

---


### 3. [The Date You Didn't Set: The System-Prompt Date as a Hidden Variable in LLM Evaluation](https://arxiv.org/abs/2611.31254)

**<font color=#1a73e8>作者：</font>** Noureldin Zahran, Mohammed E. Fouda, Khaled N. Khasawneh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The system prompt of many instruction-tuned models carries a date, usually today's, filled in automatically for conversational and agentic requests alike, so an unchanged evaluation can send a different prompt each day. In this paper, we explore how much this hidden input changes evaluation outcomes. Across six instruction-tuned models and four benchmarks, with prompts, decoding, and configuration fixed, every model is affected: two plausible dates (2024--2026) switch a median $6.6\%$ of test items between correct and incorrect. Even rerunning the evaluation one day later flips about as many items as changing the batch size, although nothing in the setup was changed. In addition, using a grammar-constrained variant of Greedy Coordinate Gradient (GCG) to search dates of any year, we find dates that cost the Llama-3.x models up to $36.5$ points of held-out accuracy. Beyond accuracy, switching to another plausible date alters LLM-judge verdicts and undoes $15$--$32\%$ of reproduced jailbreak successes on Llama-3.2-3B. Yet none of the eleven evaluation stacks we audit pins the date. With the date and the rest of the setup fixed, reruns reproduce byte-for-byte; we therefore recommend pinning, logging, and reporting the date.

---


### 4. [INCLUDE-2.0: Disentangling Knowledge Gaps in Multilingual LLM Evaluation](https://arxiv.org/abs/2611.31255)

**<font color=#1a73e8>作者：</font>** Angelika Romanou, Maria Grandury, Clara Meister 等 41 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current multilingual benchmarks cover only a fraction of the languages represented in modern pretraining corpora and often conflate language proficiency with the ability to answer questions grounded in specific regions and communities. We introduce INCLUDE-2.0, a large-scale benchmark for region-aware multilingual factual evaluation, which covers 91 languages from 86 countries (127 total language--country pairs), comprising over 220K curated samples drawn from native regional sources. Unlike existing benchmarks that often treat language as a proxy for region, IINCLUDE-2.0 distinguishes between questions whose answers are independent of context, vary by country, concern widely documented facts about a place, or depend on knowledge primarily expressed through local linguistic and cultural sources. Each item is annotated with its regional knowledge type and domain, and paired with an English translation, enabling controlled analysis of the relationship between language proficiency and possession of regional knowledge.
Evaluating frontier and open-weight models on IINCLUDE-2.0, we find that aggregate multilingual accuracy masks substantial variation across regional knowledge types, languages, and regions. We find that frontier models perform worse on locally embedded knowledge than on widely documented facts about regions, with an average drop of ~14.5 points. We also show that for open-weight models, scale improves accuracy but does not reliably make performance invariant to whether a question is asked in English or its original language. INCLUDE-2.0 is available at this https URL

---


### 5. [Directly Maximizing On-policy Expected Accepted Length for Speculative Decoding](https://arxiv.org/abs/2611.31256)

**<font color=#1a73e8>作者：</font>** Ziying Zhang, Yaqing Wang, Yong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference by using a lightweight draft model to propose tokens for verification by a target model. Draft training commonly optimizes token-level distribution alignment, but this does not directly optimize the length of the accepted prefix: once a draft token is rejected, all subsequent draft tokens are discarded. We propose FreDraft, an on-policy training method that directly maximizes the expected accepted length of drafts sampled from the current draft model. This objective accounts for first-rejection truncation and induces prefix-aware credit assignment, weighting each token by its contribution to the acceptance of the current and subsequent tokens. To optimize the objective efficiently, we analytically marginalize token-level acceptance rate, using the target model's vocabulary distribution to reduce gradient variance. We further redistribute part of this distribution-level gradient into an explicit penalty for sampled tokens whose probabilities are overestimated by the draft model, while preserving the expected gradient. Experiments across multiple benchmarks and target models show that FreDraft improves accepted length and decoding speedup over strong baselines, achieving faster on-policy training convergence.

---


### 6. [scOPD: Routed On-Policy Self-Distillation for LLM-Based Single-Cell Annotation](https://arxiv.org/abs/2611.31257)

**<font color=#1a73e8>作者：</font>** Zhiyin Yu, Yuchen Mou, Songtao Huang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Motivation: Large language models (LLMs) have shown promise for single-cell annotation, but existing training methods mainly rely on scalar outcome rewards that provide limited supervision for intermediate biological reasoning. Batch-level annotation is particularly challenging because it requires jointly resolving local cell identities and a global one-to-one matching constraint, such that one local error can affect the entire assignment. Moreover, a single inference pass provides insufficient evidence for locating uncertain predictions. These limitations call for fine-grained reasoning supervision during training and uncertainty-aware refinement during inference.
Results: To address these challenges, we propose scOPD, an on-policy self-distillation framework for LLM-based single-cell annotation. After reasoning fine-tuning, scOPD adaptively routes qualified rollouts to reward-based optimization, while erroneous rollouts receive privileged token-level supervision from successful sibling trajectories. During inference, rollout disagreement triggers constraint-aware pairwise refinement of uncertain assignments. Across CellPuzzles and four out-of-domain disease datasets, scOPD consistently improves the performance of diverse LLM backbones, achieving average cell-level and batch-level accuracies of 81.71% and 44.49% with Qwen3-8B.
Availability and Implementation: Code and data are available at this https URL.

---


### 7. [RECAP: Training Long-horizon LLM Agents with Context Compaction](https://arxiv.org/abs/2611.31258)

**<font color=#1a73e8>作者：</font>** Yulun Jiang, Maria Brbic, Michael Moor  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context compaction enables large language model agents to tackle long-horizon tasks within limited context budgets by replacing interaction histories with compressed summaries. However, learning effective compaction jointly with the agent policy remains challenging, as summaries affect task success over many subsequent interactions. We introduce RECAP, a reinforcement learning (RL) framework based on the principle that a summary should preserve the behavior induced by the original interaction history. We formalize this principle with a behavior distortion objective that measures the divergence between the agent's subsequent behavior under compressed and original contexts. We show that the gradient of the distortion objective decomposes into two complementary learning signals: distortion-based reward for summary generation and self-distillation for subsequent actions. Experiments on Qwen3.5-4B show that RECAP consistently outperforms the task-reward-only RL baselines on both environments, leading to an absolute improvement of 4.6% and 4.3% on BrowseComp-plus and SWE-bench Verified, respectively. Ablations further highlight the value of jointly supervising summary generation and post-compaction behavior for RECAP.

---


### 8. [RecipeADQA: A User-aware Question-Answering Dataset for Multi-Constraint Recipe Recommendation](https://arxiv.org/abs/2611.31259)

**<font color=#1a73e8>作者：</font>** Haotian Li, Shuai Jiang, Sayaka Kamei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Question-answering recipe recommendation tasks lack datasets with ground-truth labels. Existing methods often generate datasets from simple combinations of ingredient or tag constraints, leading to unnatural expressions and unreasonable constraints that are hard to reflect users' real preferences. This paper proposes a construction method for a benchmark-style QA dataset for natural-language recipe recommendation. Driven by real user behavior, our method integrates external user query and review data to extract fine-grained preference signals by LLMs and maps them onto a knowledge-graph-based tag schema, thereby constructing QA data consisting of preference and ingredient constraints. Besides, a greedy strategy for constraint selection is also used to control the answer size, while tag-based re-ranking is applied to improve data quality. The generated dataset RecipeADQA contains natural-language questions, structured constraints, and answer sets, resulting in 128,465 instances. Experiments compare RecipeADQA with baseline datasets from two perspectives: data quality and retrieval-recommendation performance. The results show that ours outperforms existing methods on the same recipe knowledge graph in coverage, higher question quality in naturalness and constraint rationality, and better queryability. Moreover, we design a noise-augmented retrieve-and-rerank model, in which a lightweight parser first retrieves candidate recipes, and a small language model then selects and ranks relevant recipes from a noisy candidate pool. The model trained on RecipeADQA outperforms the same model trained on the baseline datasets. The relevant construction code and data have been open-sourced at a GitHub repository this https URL.

---


### 9. [Does Item Response Theory Generalize Across Languages? Evidence from Cross-Lingual LLM Benchmarks](https://arxiv.org/abs/2611.31261)

**<font color=#1a73e8>作者：</font>** Ruchira Dhar, Qiwei Peng, Anders Søgaard  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The application of Item Response Theory (IRT) for data selection in benchmarks has mostly been limited to monolingual settings. In this work, we ask: how does IRT generalize when the same benchmark is translated across languages? We conduct experiments on Multilingual GSM and Global MMLU, covering over 100 language models and 11 languages. Fitting 1PL, 2PL, and 3PL IRT models per language, we assess cross-lingual consistency of parameters and whether IRT-filtered subsets preserve model rankings across languages: item difficulty emerges as the most stable parameter followed by guessing and then discrimination. A differential item analysis also shows that lack of stability can be tracked to specific items shifting under translation across languages. Our findings suggest IRT-based selection in multilingual settings must be both parameter-aware and item-aware, validating model choice and screening individual items before assuming cross-lingual generalization.

---


### 10. [RegioZH: Unveiling Comprehension Disparities across Regional Chinese Varieties in LLMs](https://arxiv.org/abs/2611.31262)

**<font color=#1a73e8>作者：</font>** Weihua Zheng, Wu Kui, Thong T. Doan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current evaluations often treat Chinese varieties as monolithic, obscuring failures for regional users. We introduce RegioZH, a 2,607-item multiple-choice benchmark for regional lexical reasoning across Mainland China, Taiwan, Hong Kong, Singapore, and Malaysia. Built by region-specific annotators and expert-validated, it targets localized idioms, slang, code-mixing, politeness conventions, and sociocultural expressions. Zero-shot results on eleven LLMs show large disparities, including a 29.4-point average accuracy gap between Taiwan and Singapore. Persona and structured chain-of-thought prompts for five models yield selective gains, suggesting that some errors stem from retrieval or framing rather than only missing knowledge. Representation, attention, calibration, and surface-feature analyses show a dissociation between marker attention and semantic grounding, overconfident forced-choice errors, and localized lexical density as a consistent difficulty predictor. Qualitative analysis finds terminology misunderstandings, sociocultural inference gaps, and cross-regional semantic divergence. RegioZH demonstrates that apparent Chinese proficiency can mask uneven understanding across regional varieties, motivating intra-language robustness evaluation alongside multilingual generalization.

---


### 11. [Evaluating Large Language Models on Iranian Doctoral Entrance Exams in Electrical and Computer Engineering](https://arxiv.org/abs/2611.31263)

**<font color=#1a73e8>作者：</font>** Sima Akbari Neisiyani, Hossein Taghizad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We evaluate four large language models (LLMs) on multiple-choice questions from the 2024 and 2025 Iranian national Ph.D. entrance examinations in Electrical Engineering (EE) and Computer Engineering (CE). Of the 440 questions in the four official booklets, 7 were excluded because the question statement or its figure was ambiguous, leaving 433 questions (186 EE, 247 CE), of which 171 (39.5\%) depend on a figure. Each question was presented in the original Persian and in an English translation, giving 3,464 scored responses. GPT-5, Gemini 2.5 Pro, Claude Sonnet 4.5 and Grok 4 were queried zero-shot, with reasoning enabled, through a single commercial web interface (Perplexity) in October 2025, using an automated script. Because every model answers the same items, all inferences use paired tests or question-clustered models. Accuracy separates into two tiers: GPT-5 (79.9\%, 95\% CI 76.6--83.1) and Gemini 2.5 Pro (78.4\%, 74.8--81.9) are statistically indistinguishable, and both outperform Grok 4 (71.7\%) and Claude Sonnet 4.5 (71.3\%) by 6.7--8.7 percentage points (Holm-adjusted $p < 0.001$). The English--Persian accuracy difference is small for every model ($-0.2$ to $+2.5$ points; exact McNemar $p \ge 0.28$). For three models the 90\% confidence interval lies within $\pm 5$ points, so differences larger than this can be excluded. Questions with figures are much harder: the odds ratio is 0.30 (95\% CI 0.21--0.43) after adjusting for discipline. The apparent EE deficit of two models disappears once the larger share of figure-based EE items is accounted for. We describe the dataset, the protocol and its limitations, including the uncontrolled web-retrieval and decoding settings of the interface, and release item-level responses and analysis code.

---


### 12. [How Persona Conditioning Changes Open-Ended Task Execution: A Paired Evaluation of Behavioral Gains and Reliability Costs](https://arxiv.org/abs/2611.31264)

**<font color=#1a73e8>作者：</font>** Yugyeong Ji, Changho Lee, Yerin Hwang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are often prompted with role- or persona-based instructions, yet persona conditioning has mainly been evaluated through character fidelity or aggregate benchmark accuracy. We study persona conditioning as a task-execution steering signal that changes how models interpret, structure, and sustain responses. Using paired instances derived from real user role-play logs and expanded into simulated multi-turn continuations, we compare with-persona and no-persona conditions while fixing task content, constraints, user simulation, and evaluation criteria. Across eight models, persona conditioning improves expert content depth and procedural fidelity, and these gains survive length control. At the same time, it lowers strict instruction-following accuracy by 17 to 30 points in every model evaluated, and increases unsupported real-world specificity through persona-induced elaboration. These results suggest that persona prompting is not a general-purpose performance improvement technique, but a selective task-execution policy shift with both behavioral gains and reliability risks.

---


### 13. [SD-Cache: Learnable Memory Consolidation with State-Guided Dynamic Caching](https://arxiv.org/abs/2611.31265)

**<font color=#1a73e8>作者：</font>** Yuanhong Chen, Yiping Ji, Cameron Gordon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as persistent services that must reason over large volumes of external knowledge. Retrieval-augmented generation (RAG) grounds model responses in relevant documents, but the retrieved content must still be encoded and stored in the key-value (KV) cache. As this content accumulates, the cache grows linearly, increasing memory consumption and inference cost. Existing memory-compression methods address this problem either by retaining a subset of cached states or by learning context compressors that map documents to compact latent representations. Despite these advances, consolidating information under tight memory budgets while preserving its usefulness for future queries remains challenging. We investigate how the model's native KV states can be selectively consolidated into a fixed-size working memory without access to future queries. To this end, we introduce SD-Cache (State-guided and Dynamically updated Cache), a query-agnostic KV-memory consolidation framework that operates alongside a frozen generator LLM. SD-Cache learns to consolidate layer-wise KV states into fixed-size memory through selective anchor-based pooling and state-guided refinement, processing new contexts in a single forward pass without context-specific optimisation. Experiments on retrieval-augmented question answering and synthetic long-context benchmarks show that SD-Cache maintains competitive downstream performance under constrained memory budgets.

---


### 14. [Agentic Systems Need Multi-Run Evaluation: A Study of Retrieval and Response Variability in a Deployed Enterprise RAG System](https://arxiv.org/abs/2611.31266)

**<font color=#1a73e8>作者：</font>** Karan Gupta, Sumit Bhatia, Yunyao Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Previous RAG systems have mostly been evaluated in a single-run setting, and with the advent of agentic RAG, systems are still often evaluated the same way. However, agentic RAG systems introduce a source of run-to-run variability, since several of their components make decisions non-deterministically. Such systems typically comprise a retrieval stage followed by a generation stage, and the retrieval stage in particular can behave differently across runs. For example, the agent might issue a different number of parallel searches from one run to the next, which alters the retrieved documents and therefore the final answer. In this paper we study this behavior in a deployed agentic RAG system for product-documentation questions, running each of 739 questions ten times and analyzing the execution traces to find where different runs first diverge. We find a substantial gap between success in any run and success in every run: the retrieval hit rate is 69.4% when the correct page is found in at least one run, but 50.9% when it must be found in all ten. Responses also stay similar in meaning while varying in wording, with an average BERTScore of 0.90 and a BLEU of 0.49. Trace-level analysis shows that retrieval is the largest source of divergence (43.9%), and the number of parallel searches at the first retrieval step alone accounts for 20.1% of divergent pairs. Taken together, these results show that single-run evaluation can hide reliability and consistency issues in agentic RAG systems, and that multi-run evaluation is necessary to reveal them.

---


### 15. [AhaPro: A Process-level Rebus benchmark for probing Aha moments in LLM reasoning](https://arxiv.org/abs/2611.31268)

**<font color=#1a73e8>作者：</font>** Wei Guo, Lang Qin, Yundi Gai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing research on Aha moments in large language models has largely focused on reflective expressions or final revision outcomes, leaving their role in the visible reasoning process insufficiently characterized. Rebus puzzles encode answers through character forms, spatial arrangements, and homophony. Reinterpreting key details may trigger Aha moments and shifts in the reasoning process and candidate answers. We introduce AhaPro, a process-level benchmark that uses rebus puzzles to examine how models reorganize evidence and revise answers through Aha moments. The framework represents CoT as sequences of candidate answers, evidence, and verification states, using hierarchical metrics to assess conflict detection, state improvement, and subsequent adoption. Across eleven models, we observe frequent failures to adopt better states discovered during Aha moments, alongside adopted revisions that leave state quality unchanged or reduce it. Models also detect conflicts without subsequently achieving an effective revision. Further paired interventions suggest that prior reasoning context may hinder effective revision after conflict detection, while multi-branch search highlights answer selection as a bottleneck between correct-answer discovery and successful correction.

---


### 16. [Reliability of Language-Model Judges for Quantitative Scientific Question Answering: Evidence from Perovskite Photovoltaics](https://arxiv.org/abs/2611.31269)

**<font color=#1a73e8>作者：</font>** Qiwei Han, Chi Zhou, Gaoxiang Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating retrieval-augmented language models increasingly relies on automated model judges, yet their reliability on quantitative scientific synthesis remains largely unmeasured. Here, we evaluate automated grading on a quantitative benchmark for perovskite photovoltaics, where all 755 ground-truth answers are deterministically computed from 45,441 experimental device records. We evaluate a frontier judge (Claude Opus 5.5) alongside two local open-weight judges (Qwen3-14B and Qwen3-8B) across 4,530 free-text answers from six retrieval architectures under three regimes: reference-augmented (with the computed key), evidence-augmented (with retrieved passages and query logs), and unassisted (question and answer alone). Equipped with the reference key, Claude Opus reproduces ground truth near-perfectly (Cohen's $\kappa = 0.982 \pm 0.003$) and preserves exact architectural rankings ($\tau = 1.00$). Withholding the reference causes evaluation fidelity to collapse: frontier agreement drops to $\kappa = 0.557 \pm 0.022$, and providing retrieved literature passages yields virtually no improvement ($\kappa = 0.576 \pm 0.024$). Without reference keys, local judges degrade to near-random agreement ($\kappa = 0.087$ and $0.112$), inverting the leaderboard to rank a hallucinating closed-book baseline first ($\tau \le 0.20$). Furthermore, SQL-augmented generations induce severe evaluative blind spots: absent a reference, the frontier judge accepts 46.6% of erroneous SQL answers, overestimating architecture accuracy as 66.4% against its true 52.6%. These findings demonstrate that model-based evaluation in the physical sciences cannot rely on unstructured text inspection; rigorous benchmarking requires reference ground truth precomputed from structured measurement records.

---


### 17. [Chain-of-Thought Is Not Explainability](https://arxiv.org/abs/2611.31271)

**<font color=#1a73e8>作者：</font>** Fazl Barez, Tung-Yu Wu, Iván Arcuschin 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) allows language models to verbalise multi-step rationales before producing their final answer. While this technique often boosts task performance and offers an impression of transparency into the model's reasoning, this position paper argues that rationales generated by current CoT techniques can be misleading and are neither necessary nor sufficient for trustworthy interpretability. We analyse faithfulness as whether CoTs are not only human-interpretable but also reflect the model's underlying reasoning well enough to support responsible use. By synthesising evidence from prior work, we systematically show that verbalised chains are frequently unfaithful, diverging from the critical hidden computations that drive a model's predictions. As CoT is increasingly relied upon in application domains, including high-stakes ones such as medicine, law, and autonomous systems, we further argue that this unfaithfulness is not taken seriously enough in these settings: our analysis of 1,000 recent CoT-centric papers finds that approximately 21.7% explicitly treat CoT as a load-bearing interpretability technique, building pipelines or safety arguments that would not hold if CoT is unfaithful to the model's actual reasoning. They include papers in high-stakes domains that heavily hinge on such interpretability claims. Building on prior work, we make three proposals: (i) avoid treating CoT as being sufficient for interpretability without additional verification, (ii) adopt rigorous methods that assess faithfulness for downstream decision-making, and (iii) report such assessments alongside any interpretability claims based on CoT, while continuing to use CoT for its communicative and monitoring benefits.

---


### 18. [PEACE-TEST-PROTOCOL: Polarization-Keyed Examination Papers and Mandatory Issued Eyewear that Displace AI Glasses and Extend Universal Design](https://arxiv.org/abs/2611.31299)

**<font color=#1a73e8>作者：</font>** Dohyeon Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-equipped AI glasses turn an examination page into a query for a remote vision-language model. Device detection targets possession, and our companion work SEOYUN targets the model. PEACE-TEST-PROTOCOL instead changes who owns the eyewear. Every candidate wears authority-issued glasses for the whole session, and the question paper is printed so that it can be read only through them. As in cinema stereoscopy, a patterned laminate encodes the text in the handedness of circular polarization rather than in brightness. The page looks uniformly grey to the naked eye and to unfiltered cameras, and the issued circular analyzer reveals the text. Compulsory issued eyewear turns the smart-glasses form factor against itself. The face position is occupied by a device the authority supplies and collects, and a camera anywhere else needs its own analyzer. Spectacle wearers receive prescription inserts in the issued frame, low-vision candidates may use an offline assistive mixed-reality tier, and blind candidates keep braille, audio, and screen-reader formats. We derive the luminance and contrast budget and show why circular keying tolerates head tilt. A simulation study supports the analysis. A spectral Mueller model confirms tilt invariance and invisibility to linear-polarization cameras, but a 1 degree axis misregistration leaks a few percent of contrast. A capture-and-OCR experiment on English and Korean text shows that video averaging can recover leakage too weak to read in a single frame, so leakage must be bounded against the adversary's total photon budget. Data from 151 observers and 28 cameras show that spectral (metameric) keys are visible to all of them. The key carries no secrecy, and filtered covert cameras remain possible. All results are simulations; no prototypes, physical measurements, or human-subject results are reported.

---


### 19. [MOZAIC: An Audio-Video Deepfake Benchmark for Telling What Is Fake](https://arxiv.org/abs/2611.31301)

**<font color=#1a73e8>作者：</font>** Shaina Raza, Mohamed Hafez, Ahmed Y. Radwan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audio-video (AV) deepfakes can fake the face, the voice, or both. Most benchmarks only ask whether a clip is real or fake, so they cannot show whether a detector relies on the picture, the voice, or encoding traces. We present MOZAIC, a paired benchmark with a 4-way label in which every source clip is released in all four combinations of real or fake video and real or fake audio so each modality contribution can be measured directly. Fakes cover inner-face swapping, whole-frame video diffusion and voice conversion. MOZAIC has 137,745 clips from 15,014 source pairs and four tasks: T1 AV authenticity, T2 manipulation type, T3 identity verification and T4 explanation. We evaluate 12 AV multimodal LLMs (MLLMs), train four detectors and fine-tune MLLMs with LoRA. Overall, the best MLLM reaches only 35.6% on the four-way T1 and catches far more video-only fakes than voice-only fakes (43.6% vs 7.5%). Trained detectors reach 98.4% on T1, and LoRA fine-tuning raises explanation scores (OmniVinci 4.17 to 7.40, Qwen2.5-Omni 4.42 to 6.98), but the best T1 detector falls to 78.3% when the face-swap generator is held out of training, so generalization and explanation remain open. We release the dataset, the compact MOZAIC-SMALL split, the code and the prompts. this https URL

---


### 20. [Per-Attack Blocking Hides Catalog Vulnerability: A Weakest-Link Analysis of Tool Manifests](https://arxiv.org/abs/2611.31338)

**<font color=#1a73e8>作者：</font>** Karthik Karunanithi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Runtime controls for tool-using agents depend on manifests that state what each tool may read and where its output may go. Evaluations of these controls, including ChainCaps, report per-attack blocking: the share of attacks a set of manifests stops. We show that this is the wrong unit. A catalog is only as safe as its weakest source policy: if $M$ independently authored policies are each wrong with probability $p$, the chance that the catalog contains an accepted exfiltration path is $1-(1-p)^M$, while per-attack blocking stays at $1-p$. Three lines of evidence agree. In synthetic catalogs run through two enforcement engines, ChainCaps and OpenAPPA, per-attack blocking holds at 92% while catalog vulnerability rises from 22% at 10 tools to 99% at 200, and composition provides no protective effect. A fifteen-model authoring pilot shows that real errors cluster by author, so a 200-tool catalog behaves like about 5 independent decisions rather than 60 (95% interval 3.4 to 9.2). On 114 real MCP tools with expert-written rules, the models' own manifests block 89% of attacks yet leave 9 of 15 catalogs open, as the author-effect model predicts and independence does not. Evaluations should report catalog vulnerability, the sink coverage of their tests, and an effective number of independent decisions alongside per-attack blocking.

---


### 21. [Beyond Static Charts: Benchmarking Interactive Chart-to-Code Generation for MLLMs](https://arxiv.org/abs/2611.31345)

**<font color=#1a73e8>作者：</font>** Yuhan Bian, Haoyu Liu, Siyu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, multimodal large language models (MLLMs) have achieved significant progress in chart-to-code generation. However, existing benchmarks mainly focus on static charts, overlooking interactive charts that enable richer and more expressive data exploration. Unlike static chart-to-code generation, which emphasizes visual consistency, interactive chart-to-code evaluation targets behavioral consistency, requiring chart states to evolve correctly under sequences of user interactions, thereby rendering traditional one-step evaluation paradigms ineffective. To address this gap, we introduce ChartInt, the first benchmark specifically designed for interactive chart-to-code generation. ChartInt consists of 2,779 carefully annotated examples covering common interaction patterns such as hover, highlight, and tooltips. Additionally, ChartInt incorporates editing tasks such as data updates, style adjustments, and cross-chart style transfer to expand real-world application scenarios. To enable reliable evaluation of interaction behavior, we propose a preset state snapshot protocol that predefines target interaction states and deterministically triggers interaction events, transforming dynamic behaviors into reproducible evaluation targets. Based on this protocol, we design a multi-dimensional evaluation framework measuring semantic and stylistic consistency. Experiments show that while current MLLMs perform well on static charts, their performance drops significantly on interactive tasks, highlighting the need for interaction-aware benchmarks.

---


### 22. [What People Choose Not to Say: A Multimodal Benchmark for Fine-Grained Information Manipulation in Conversations](https://arxiv.org/abs/2611.31346)

**<font color=#1a73e8>作者：</font>** Yuhan Bian, Zhaokai Liang, Jia Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in MLLMs have improved social understanding, enabling models to recognize emotions and distinguish truthful from deceptive behaviors. However, existing benchmarks largely focus on coarse-grained emotion recognition or binary truth-deception detection, overlooking the diverse ways people manipulate information in conversations, such as withholding, leakage, fabrication, evasion, and defensive counterclaim. Understanding these behaviors requires reasoning about underlying facts, participant knowledge, and conversational context, making them difficult to evaluate reliably. To address this gap, we introduce InfoCon, a multimodal benchmark for fine-grained information manipulation in conversations. InfoCon identifies six fine-grained strategies and derives a coarse consistency label from their factual and interactional relations. We develop an evidence-grounded multi-agent annotation framework to construct and verify reliable labels from rich contextual evidence. We benchmark representative multimodal models and systematically analyze their fine-grained information manipulation understanding, providing a testbed beyond binary truth-deception judgments.

---


### 23. [Antares-Smaug: Adversarial Names, Tokens and Attack Rewrites: Sanitisers Miss Unseen Generalisations](https://arxiv.org/abs/2611.31347)

**<font color=#1a73e8>作者：</font>** Mohammed Nayeem Khan, Akhil P  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Laya is an open decision model: given a text, a question and K named options with descriptions, it returns one probability per option in a single pass, and software may act on the answer unseen. We attack six Laya models with 81 programmatic edits of 566 synthetic items (injected sentences, label leaks, edited descriptions, decoy options, invisible and look-alike characters, floods) and report the share of correctly answered items hijacked or lost, with bootstrap intervals. Attack wordings that no defence was built from win the attacker's option on 59% of items for released Laya and 36% for fine-tune v1 (trained on 109 written injections). An injection works through the option name: a sentence naming an option steers the released model even when negated (32%), while an imperative naming no option does not (5%). Option descriptions barely matter (2%). Character edits alone cost v1 up to 72% of right answers. A sanitiser frozen before any held-out result cuts the attacks it was built from by 72% but held-out sentence attacks by 27%, and an attacker who picks the best of 34 held-out strings per item restores success to 84% (mean string 18%). The same oracle takes the model fine-tuned on the four build families of injected sentences from 5% (mean string) to 58%. Fine-tuning on build families only (against an unchanged-rows control) cuts held-out sentence attacks (three held-out families) from 33% to 3% but character edits only from 25% to 20%. A label-free check that deletes the option names and measures the shift flags held-out sentence attacks (AUROC 0.95) but not character edits (0.46), and thresholds set on dev schemas for 5% false alarms gave 8% to 18% on an unseen schema and other languages. All data are synthetic with LLM labels, on one backbone. Several planned runs (other checkpoints, a second seed, some fine-tunes) were not run.

---


### 24. [Detecting Harmful Short Videos in Toxic Diet Culture: A Governance-Ready Evidence Framework with Sparse Autoencoders](https://arxiv.org/abs/2611.31354)

**<font color=#1a73e8>作者：</font>** Wenli Zhang, Shuang Geng, Jiaheng Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithmic content moderation is increasingly important for governing short-form video content, yet harmful-content detection research focuses primarily on prediction or limited explanations. This leaves a governance challenge underexplored: producing decision-linked evidence that supports the review and justification of moderation decisions. Using toxic diet culture as an empirical case, we conceptualize governance-ready evidence as computational traceability, evidence localization, policy grounding, and evidence inspectability. We develop the Sparse Autoencoder-based Policy-Aligned Contrastive Evidence (SPACE) framework in a pretrained SAE feature space derived from a large multimodal model. A global relevance gate and decomposable linear evidence head identify decision-linked evidence; segment supervision and within-video ranking localize this evidence; policy alignment maps it to platform guidelines; and Pareto-efficient selection yields a compact, task-specific evidence vocabulary. On 3,711 labeled TikTok videos, SPACE achieves the highest harmful-category Macro F1 among benchmarks across four families, at 0.8507. Its highest-scoring observation overlaps a ground-truth harmful span for 88.0% of harmful test videos, while its evidence representation retrieves the corresponding policy category for 87.0%. Stakeholder evaluations indicate that the SPACE evidence report is perceived as useful for understanding, reviewing, documenting, and responding to moderation decisions. The study contributes computational design science knowledge for embedding governance-ready evidence within predictive content-moderation systems.

---


### 25. [Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation](https://arxiv.org/abs/2611.31358)

**<font color=#1a73e8>作者：</font>** Guo Chen, Fuxiao Liu, Haoqin Tu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual creation demands expressive imagery together with precise control over text, layout, and structure. We introduce Nemotron-Labs-VisualCreation, an agentic framework that connects these capabilities through Pixel as Code. Raster images are represented by learned discrete visual tokens, while structured artifacts use explicit programs. A shared generation-and-rendering interface connects these representations to visual feedback across images, vector graphics, webpages, and documents. A Nemotron-native harness coordinates planning and raster candidate selection, with targeted repair for editable structured and hybrid artifacts. To support this interface, we develop Nemotron-Labs-Image-Tokenizer, the autoregressive raster generator Nemotron-Labs-Image-30B-A3B, and the structured-code model family Nemotron-Labs-VisionCode. On approximately 178K images spanning six visual domains, our tokenizer improves reconstruction PSNR from 26.08 to 29.57 dB over Emu3.5 IBQ. It also provides 7.13x faster encoding and 10.93x faster decoding at batch size one on A100. In standalone evaluation, one Nemotron-Labs-VisionCode variant surpasses Kimi K3.1 Pro on the aggregate across Chart2Code, MMSVG, Design2Code, and Image2Struct. At the system level, the Nemotron-native configuration raises GenEval2 Soft-TIFA GM from 31.71 to 52.56 using the same raster generator. With our best setting, Nemotron-Labs-VisualCreation achieves performance competitive with GPT Image 2 and Nano Banana Pro across most benchmarks with available comparisons.

---


### 26. [CoRe: Jointly Learning Contextual Representations for Understanding and Generation](https://arxiv.org/abs/2611.31397)

**<font color=#1a73e8>作者：</font>** Hangke Sui, Chang Li, Yuyan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce CoRe, in which understanding and generation jointly shape one contextual representation for images and one for text, trained from scratch. Each representation is read for understanding, conditions the other modality, and is the space in which that modality is generated by a continuous flow from Gaussian noise. With 383M parameters trained on CC12M and no pretrained language model, text encoder, or VAE at inference, CoRe matches a same-data contrastive-only baseline in global understanding and reaches COCO-30K FID 10.10, comparable to much larger generators built on pretrained components. In controlled comparisons at equal data and architecture, CoRe generates better in both directions (text to image and image to text) than a representation shaped by understanding alone and then frozen, and follows prompts better than generating in a space that understanding does not shape. In the other direction, with an attentive segmentation probe, on monocular depth, and when read by a frozen language model, CoRe surpasses the contrastive-only baseline: generation adds information that stronger readouts reach. Because generation runs inside the understanding representation, frozen real-image probes read and steer intermediate states and the model ranks its own samples without extra training. Because both modalities use continuous flows, both also distill to a few steps. Our controls indicate why one representation suffices: understanding organizes the representation semantically, while generation makes it retain more information.

---


### 27. [Learning What vs. Learning How: Decomposing Task and Interface Competence in Agentic Training](https://arxiv.org/abs/2611.31427)

**<font color=#1a73e8>作者：</font>** Chaeeun Lee, Hossein A. Rahmani, Aryo Pradipta Gema 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents operate through harnesses that define system prompts, action formats, feedback loops, and resource constraints. A model may possess the knowledge needed to solve a task yet fail to express that knowledge through a particular harness. This raises a basic question: when a policy fails under a given harness, is it missing task knowledge or the competence to operate the interface? We distinguish two components of agentic competence: task competence, the knowledge and reasoning needed to solve a task, and interface competence, the ability to act on that knowledge through a given harness. Across four reasoning and agentic benchmarks, we show that harness-conditioned training yields vastly different outcomes depending on how these interact. Multi-harness distillation aggregates task knowledge from trajectories collected through different harnesses into a shared policy, but this knowledge is realised only when training preserves or improves competence on the inference-time interface. Otherwise, single-harness training can induce interference in interface competence, sometimes catastrophically collapsing performance on a held-out harness despite improvements in underlying task knowledge. To disentangle task and interface supervision, we introduce harness rehearsal: distillation on traces that carry minimal task knowledge while exercising the target interface. Cross-harness task supervision or rehearsal alone yields little gain, but their combination yields gains far larger than either: on BFCL V3 multi-turn with Qwen3-4B, they achieve 8.5% and 32.5% respectively, versus 58.8% together. Finally, on-policy reinforcement learning (RL) is more robust than distillation to single-harness training: it does not substantially degrade performance on other harnesses, and interface competence acquired through multi-harness distillation persists through subsequent RL.

---


### 28. [Leaks by Installments: Cross-Session Answer Disclosure in LLM Tutors and a Ledger-Based Defense](https://arxiv.org/abs/2611.31429)

**<font color=#1a73e8>作者：</font>** Venkata Muttineni, Karthik Narayan, Christopher David  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tutors built on large language models (LLMs) are told not to give away answers, but a learner does not have to ask for the answer all at once. Existing safeguards judge each reply within the current conversation, so a learner can open a new session, reword the problem, or request a worked solution to the same problem with different numbers. We call this cross-session disclosure and propose a defense: a persistent, per-learner disclosure ledger. For every problem a learner brings, the system builds a typed solution graph. Before a reply is released, a gate matches the reply's own content, not the learner's wording, against the ledger by result values and by type-labeled solution structure, then computes which steps the learner could now derive. The reply is withheld if that set reaches the final answer or exceeds a budget. In a simulation of 3,000 problems, the ledger reduced leakage through renumbered practice variants from 100% to 10.6% while honest learners completed 94-99.5% of problems. With two real LLM tutors (Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct) on 60 problems, leakage through renumbered variants fell from 0.58 to 0.08 and from 1.00 to 0.18, with 98% honest completion. The ledger did not reduce split requests beyond a per-session gate in the live runs. All acceptance criteria were fixed before each run.

---


### 29. [Transformers with Signatures: Towards Universal In-Context Learning in Path Space](https://arxiv.org/abs/2611.31439)

**<font color=#1a73e8>作者：</font>** Ziheng Cheng, Xin Guo, Ben Hambly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) enables transformers to adapt to new tasks from demonstrations without updating their parameters. However, theoretical guarantees for transformers remain limited in general, and elusive in particular when target responses depend nonlinearly on the evolution of observed paths. We establish an ICL framework for path space, using path signature features. Building on the universal linear approximation property of signatures, we construct explicitly a causal softmax transformer with two attention heads per layer that emulates in-context Lasso. Under sparse signature approximation and suitable moment and concentration conditions, we establish finite-sample prediction error bounds. Our analysis goes beyond the IID data setting in the existing ICL theory, allowing dependence among demonstrations and the query.
Experiments on in-context sparse recovery, nonlinear path regression, execution-cost prediction, and financial payoff inference demonstrate robustness to changes in observation grids and adaptation to unseen market environments. Across these prediction tasks, transformers with signatures match or outperform vanilla transformer baselines with substantially fewer trainable parameters, highlighting the effectiveness and efficiency of signature-based ICL.

---


### 30. [Ground, Guide, Act: Improving VLA Spatial Generalization with Multimodal Foundation Models](https://arxiv.org/abs/2611.31452)

**<font color=#1a73e8>作者：</font>** Guangting Zheng, Shaoxuan Wang, Yu Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models effectively learn action policies from robot demonstrations, but struggle to generalize to changes in object positions and task goals. General multimodal foundation models (MFMs) offer complementary scene understanding and spatial reasoning, but remain slow and unreliable for direct fine-grained control. To understand how MFMs can improve VLA spatial generalization, we conduct a systematic capability analysis across multiple VLA architectures using atomic-stage interventions, revealing that many failures stem from poor target grounding and global spatial routing, while local manipulation skills remain largely usable. Based on these findings, we propose MFM-VLA, a selective collaboration framework in which an MFM provides target grounding and spatial guidance, controllers execute free-space motion, and the VLA retains control over fine-grained manipulation. We fine-tune the VLA with action-chunk-level dense geometric captions and perturbed-state recovery data to improve local guidance following and recovery from unfamiliar handoff states. A development-calibrated capability router selects between direct VLA execution and MFM-assisted execution to avoid unnecessary intervention. Across LIBERO-PRO, ALOHA-Sim-PRO, RoboCasa365, and real-world chemistry tasks, MFM-VLA improves success rates by 14.9, 74.0, 3.6, and 30.9 percentage points, respectively, over the corresponding base VLA. The project page is available at this https URL

---


### 31. [Taxi: Analyzing Agents at (Real) Scale](https://arxiv.org/abs/2611.31457)

**<font color=#1a73e8>作者：</font>** Guy Dar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this technical report, we present Taxi -- a system for debugging, clustering, and monitoring agents at scale. Taxi scales to millions of steps efficiently. This is made possible by a combination of scalable analysis methods. Taxi relies primarily on clustering to generate a taxonomy over steps for a structured overview of the data, and provides full SQL access for engineers and automated agents to ask complex questions. Clustering and querying are best used together in a hybrid pipeline guided by a coding agent. Taxi also includes an experimental integration of Jev-style decision models: models that map state and bounded questions directly to typed, probabilistic decisions. They add low-cost semantic routing and evaluation where embeddings or literal queries alone are insufficient. In addition, Taxi provides an extensible ecosystem, including built-in evaluators and daily reports. To accommodate growth, Taxi is designed to be modular, hackable, and easy to plug-and-play for individuals and teams.

---


### 32. [A dataset of clinically similar image pairs from citation-linked case reports for medical image retrieval](https://arxiv.org/abs/2611.31465)

**<font color=#1a73e8>作者：</font>** Guy Shmueli, Keno K. Bressem, Tom Hope  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieving images of patients clinically similar to a given patient can support diagnosis, teaching and research. Training and evaluating retrieval systems requires knowing which images of different patients show the same finding, and existing datasets are small or narrow in scope. We construct PMC-PaIR, a dataset of 86,144 pairs of clinically similar images from 56,013 open-access PubMed Central case reports, which often document rare or challenging presentations. We develop an approach that follows citations, which often link case reports of similar patients. To determine what two linked cases share clinically, it prompts large language models to generate and answer hierarchical questions, from modality to diagnosis and findings, and to match images by caption using the answers. Experts find the pairs highly accurate, and this question-guided approach finds twice as many correct pairs as direct matching. Fine-tuning BiomedCLIP on PMC-PaIR improves retrieval in all modality, anatomy and diagnosis categories tested, for image-only queries and image queries with a short text naming the finding. We release the dataset and the automated pipeline, which can extend PMC-PaIR as new case reports are published.

---


### 33. [PromptSMC: Enabling Particle Exploration in Flow Matching via LLM-Based Prompt Rejuvenation](https://arxiv.org/abs/2611.31471)

**<font color=#1a73e8>作者：</font>** Wenyi Lian, Zheng Zhao, Thomas B. Schön  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper is concerned with prompt-image alignment at inference time through exploration of generative trajectories and dynamical prompt rejuvenation. We leverage sequential Monte Carlo (SMC), to offer a gradient-free and principled framework for this purpose through reward-guided trajectory selection. More specifically, we introduce LLM-based prompt rejuvenation, allowing for efficient particle exploration in SMC samplers along the diffusion time in flow matching models. The proposed method, PromptSMC, retains the selected latent states and uses a pretrained LLM to dynamically revise the prompts of duplicated particles under semantic-preservation constraints. These revised prompts induce alternative conditional velocity fields, allowing particles to explore different continuations from a shared intermediate state. The method further uses a reward model to evaluate each particle's alignment with the original prompt, and the resulting scores guide particles through resampling. PromptSMC thus integrates prompt-based exploration with reward-guided sampling, achieving faithful prompt-image alignment without additional noise injection, model training, or reward gradients. Our experiments and ablation studies across multiple benchmarks and backbones demonstrate the effectiveness of the method for text-to-image flow matching. Code is available at this https URL.

---


### 34. [SpatialCraft: Evolving Procedural Intelligence from Experience and Skills for Spatial Reasoning Agents](https://arxiv.org/abs/2611.31475)

**<font color=#1a73e8>作者：</font>** Xiwei Liu, Yulong Li, Xuhui Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning agents increasingly rely on external tools, such as 3D reconstruction, segmentation, and geometric computation, to answer questions that a multimodal large language model (MLLM) cannot resolve from pixels alone. Tool access, however, shifts the bottleneck to orchestration: the agent must decide which tools to call, in what order, and how to interpret their outputs, yet a stateless agent repeats the same mistakes across tasks. We ask whether a frozen tool-using agent can improve its orchestration from its own interaction history, without parameter updates. We present SpatialCraft, a self-evolving framework that maintains two forms of external knowledge: Experiences, condition-action tactics distilled by contrasting rollouts of the same task, and Skills, multi-step procedures with explicit activation and termination conditions. Three designs couple the two streams. Experiences can be anchored to a Skill, appearing only while it is active rather than once per task. A Contrastive Utility Score estimates each Experience's effect by randomly withholding it across rollouts of the same task, separating its contribution from task difficulty, and Experiences with consistently positive utility are consolidated into the Skills they support. Across five spatial benchmarks and four backbones, SpatialCraft achieves the best accuracy in all 20 settings, showing that a frozen agent can learn to orchestrate spatial tools from its own experience.

---


### 35. [Evaluating Frontier-Model Agent Skills with Open-Weight Models in a Science Gateway](https://arxiv.org/abs/2611.31480)

**<font color=#1a73e8>作者：</font>** Komal Thareja, Mats Rynge, Anirban Mandal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific analyses that span many jobs and computing sites depend on workflow management systems to run reliably, but writing a production workflow requires expertise in such a system, which many domain scientists do not have. Coding agents can supply this expertise when they are guided by skills and packaged procedures for recurring tasks. We wrote skills and specialist agents for the Pegasus workflow management system with a frontier model, and the PegasusAI Studio science gateway offers them to scientists through a chat interface. New users without frontier-model credits need an open-weight model, served at no cost on research cyberinfrastructure, but skills written for a frontier model may not work with an open-weight solution. This paper presents a method for adapting such skills. An evaluation harness drives the real gateway as a user would, scores the workflows the agent builds, and feeds recurring failures back to the frontier model that maintains the skills. We evaluated 21 open-weight models on 17 tasks. The five highest-scoring models are close in quality after one trial per task, and their median response times differ twelvefold. In repeated trials with the best of the three open-weight models, we repeated scores of 0.76 on workflow building against 0.82 for Claude. The harness led to five changes to the initial skills. We also identify challenges in evaluating agents within operational systems: evaluation failures can be mistaken for model failures, and agents can circumvent experimental controls within their privilege domain. In a controlled ablation, an initially significant effect disappeared when the restrictions were properly enforced.

---


### 36. [GDD: A Remote Sensing Image Deepfake Detection and Manipulation Localization Dataset](https://arxiv.org/abs/2611.31487)

**<font color=#1a73e8>作者：</font>** Jacob Arndt, Philipe Dias, Debvrat Varshney 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Verifying image authenticity is a critical need for a variety of applications and decision-making in the remote sensing (RS) domain, yet it is becoming more challenging as advancements in generative AI enable producing increasingly realistic synthetic overhead data. However, existing RS deepfake benchmarks prioritize sheer volume at the expense of visual realism and diversity, while also lacking rigorous out-of-distribution (OOD) testing protocols to evaluate real-world robustness. To address this, we introduce the Geospatial Deepfakes Dataset (GDD), a benchmark for RS deepfake detection and manipulation localization. Rather than relying on uncurated, redundant synthetic generation, GDD comprises images across diverse modern generative models and real image sources, alongside manipulations from diffusion inpainting, splicing, and copy-move operations. Crucially, GDD establishes an OOD evaluation protocol for deepfake detection comprising unseen real image sources and generative models. We benchmark five deepfake detectors and two localization models across intra- and cross-dataset regimes and reveal that detectors trained on high-volume, uncurated benchmarks overfit to dataset-specific artifacts, whereas training on GDD yields superior cross-dataset generalization despite its compact scale. This benchmarking also exposes critical failure modes in current state-of-the-art methods. Combined, GDD and its evaluation protocol establish a high-quality standard for developing and stress-testing detection and localization models in this safety-critical RS domain. The dataset is publicly available.

---


### 37. [Near-Zero Forgetting Is Not Enough: Out-of-Distribution Robustness in Continual Learning of Pretrained VLAs](https://arxiv.org/abs/2611.31511)

**<font color=#1a73e8>作者：</font>** Adrià Ruiz, Bartłomiej Twardowski, Tinne Tuytelaars 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work shows that pretrained Vision-Language-Action (VLA) models exhibit near-zero forgetting in specific continual learning settings with experience replay. However, robustness to domain shift of learned tasks remains unexplored. In this work, we study the robustness of Pi0 fine-tuned with experience replay under out-of-distribution (OOD) data using the LIBERO and LIBERO-Plus benchmarks. While the in-domain (ID) setup achieves near-zero catastrophic forgetting, OOD performance on previous tasks quickly collapses. Specifically, we show that during the continual learning process, the OOD capabilities of the model degrade, following a shared representational pattern across domain shifts, which is also visible behaviorally in the two simpler suites. Representational analysis shows that drift concentrates in the multimodal and action features. Linear probes indicate that OOD features still retain task-relevant information, but appear unreadable, consistent with representation misalignment. These findings suggest that even when ID stability remains intact, severe OOD forgetting can still occur, accompanied by representational drift during continual learning.

---


### 38. [PatientFlowSynth: Evaluating FHIR Agents with Matched Patient Charts](https://arxiv.org/abs/2611.31521)

**<font color=#1a73e8>作者：</font>** Anthony Cuturrufo, Ratul Ghosh, Devashish Khatwani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents that search patient charts must classify claims from retrieved records, including cases with missing or conflicting evidence. In Fast Healthcare Interoperability Resources (FHIR), status fields can change how those records should be interpreted. PatientFlowSynth provides 18,000 tasks from 225 synthetic patients and 18 templates that hold the patient, question, and retrieval program fixed across chart variants representing four evidence states. Re-executing the program verifies each variant's reference answer, evidence sets, and search requirements. Strict success requires a completed response with correct labels and citations exactly matching an accepted evidence set retrieved during the episode. Where required, a tool response must also show a complete search at the specified scope. In a study using GPT-5.6 Luna and 225 synthetic patients (3,600 matched pairs), explicit Encounter-status guidance increased strict success from 40.7% to 51.3% (+10.6 percentage points; 95% patient-bootstrap confidence interval, 8.4 to 12.8). Among cases whose primary reference label was insufficient evidence, label agreement fell from 49.2% to 29.3%. A prespecified two-model replication reproduced both changes. Failed retrieval can mask interpretation errors by producing a correct insufficient-evidence label without examining the relevant records. Additional model comparisons showed that the benefit of guidance was model-dependent. Retrieval, citation, and classification should be evaluated separately.

---


### 39. [Can LLM-Simulated Respondents Pre-Test Survey Questions? Evidence From Preregistered Prospective Validation](https://arxiv.org/abs/2611.31532)

**<font color=#1a73e8>作者：</font>** Sristi Bafna, Mac MacComas, Michael Bader 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can be conditioned to simulate behavioral responses, including survey responses, but it remains unclear whether and how these simulations can support downstream research tasks. Here, we evaluate whether simulated respondents can support pre-testing new candidate survey questions before fielding them, operationalized as prioritizing candidate survey items. Specifically, we rank candidate questions by their mean responses, which can reveal ceiling or floor effects; their variance, which indicates whether responses contain meaningful variation; and differences between subpopulations, which indicate whether questions capture distinctions between relevant groups within a population. We introduce a preregistered, prospective evaluation that commits model predictions before target human responses exist, ruling out memorization of those responses by design. Using two waves of a local survey (2025: N = 1,271; 2026: N = 1,161), we built simulated respondents from 2025 participants and preregistered GPT-4.1 predictions for 22 questions introduced in 2026. Simulations accurately ranked questions by mean responses (Spearman \r{ho} = 0.71) and anticipated which questions distinguished city from county residents (\r{ho} = 0.88), Black from White residents (\r{ho} = 0.68), and employed from unemployed residents (\r{ho} = 0.57), suggesting simulations can help prioritize questions before fielding. More broadly, our prospective, preregistered design provides a general framework for evaluating AI simulations without contamination from memorized target outcomes.

---


### 40. [Agent Evaluation Without Ground Truth: A Null Proportion Perspective](https://arxiv.org/abs/2611.31539)

**<font color=#1a73e8>作者：</font>** Brian M. Cho, Michael Lindon, Nathan Kallus  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The correctness of actions taken by agents is typically evaluated against known, externally verified ground truth labels, such as whether a proof is correct or whether code compiles and passes unit tests. However, as coding and science agents are entrusted with more end-to-end autonomy -- proposing interventions, running experiments, and deciding what to deploy and investigate next -- whether an agent's actions genuinely improve an outcome must be inferred from noisy, often inconclusive experiments. To evaluate agents in this setting, we define agent quality as a weighted sum of correct decisions along its trajectory, using sequences of $e$-values as statistical evidence regarding correctness in place of ground-truth labels. Our framework accommodates arbitrarily dependent decisions, data-dependent trajectory termination, dynamically generated hypotheses, and quality measures defined after the trajectory concludes. We construct upper and lower bound estimators and confidence sets for agent quality with statistical guarantees that hold uniformly over agent trajectory distributions and establish instance-wise sharpness of our estimator class. We demonstrate our methods with a case study comparing the success of Claude Opus and Claude Haiku in improving the runtime of an open-source Python package.

---


### 41. [Where Agent Defenses Fail: A Case Study of Policy Compositions and Measurement Limits](https://arxiv.org/abs/2611.31541)

**<font color=#1a73e8>作者：</font>** Kunwar Sangram Singh, Krishna Mohan Guda Nagavenkata Srinivasa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A coding agent may need to upload a report while its sandbox blocks network access. A host mediator can restore delivery, but an injected instruction may add a secret to the approved request. We study this interaction using files and HTTP receipts to measure effects independently of control logs. Two prospective frozen-input cohorts comprise 110 and 300 runs on previously explored authored tasks. Restrictive sandboxing produces no observed attack harm but reduces benign utility to 6/8 and 12/24. Mediation restores uploads and admits disclosure; complete-line matching retains full benign utility but misses two value-only disclosures in the expanded cohort. A separate 72-run boundary study identifies encoded disclosure, observer misses, and formatting checks that obscure benign refusals. An 80-run SafeAgents/OpenShell follow-up shows that containment stops the tested guard misses among valid observations, while mediation restores benign uploads and delivers both encoded-attestation attacks. Twelve judge-error rows remain unscored. A separate response-capture diagnostic reproduces their failures at the native token budget. A 12-run exact-publication-contract experiment blocks both attacks but also rejects both benign formatting variants; a 4-run normalized follow-up restores both benign uploads while still rejecting both attacks. These small, single-model studies identify delivery-path and measurement limits; they do not establish general attack resistance.

---


### 42. [Reproducible Social Structure Emerges From Free-Form Interaction Among LLM Agents](https://arxiv.org/abs/2611.31543)

**<font color=#1a73e8>作者：</font>** Tom Alisch, Sonia Murthy, Robert Hawkins 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM simulations are increasingly used as models of social systems, but most published findings are anecdotal, i.e., drawn from a single run. It is therefore unclear which observed phenomena are robust findings of the simulated system itself, and which were random events in one particular run. Here, we introduce a repeatable, goal-free, proactive multi-agent framework in which fifty persona-conditioned agents with persistent memory choose whether, with whom, and how to communicate across three social platforms. The framework supports non-perturbative measurements across temporal snapshots and repetitions. Running the same world ten times from identical initial conditions for a total of 700 hours, we find that most measured network- and agent-level parameters are stable across repetitions. Throughout a run, initially broad communication contracts into sparse sustained dyads in all ten worlds. Importantly, we find that many identical dyads re-form across worlds significantly more often than expected by chance or from agent-specific sociability alone. Static personality similarity largely fails to predict these dyads. Instead, alignment and extremity in the emotions and traits expressed during first contact predict whether a pair later forms a sustained dyad. Additionally, individual agents' emotion and trait expression in their chain-of-thought predicts their future behavior. Finally, swapping either persona prompts or accumulated memories between agents causes recipients to exhibit behavior more similar to donors. Both kinds of transplant move the recipients about 60% of the way toward its donor personality, and state-transplanted agents start behaving similar to their donor agent from their next turn on. Overall, we show that repeated worlds enable robust, statistically-grounded conclusions about emergent within-configuration behavior in agent societies.

---


### 43. [Aftershock: Yesterday's Linux Kernel Bugs, Tomorrow's Android Exploits](https://arxiv.org/abs/2611.31547)

**<font color=#1a73e8>作者：</font>** Kareem Shehada, Zhiyun Qian  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Android kernels have long suffered from slow patch propagation from Linux upstream, with fixes often reaching devices far later than conventional Linux distributions. Until recently, this lag was largely a patch-management problem. With rapidly improving LLM agents, it is becoming an exploitation problem: public upstream patches can now serve as blueprints for building working n-day exploits before downstream devices are fixed. We test this threat end to end by building an automated pipeline that screens upstream Linux patches, reproduces memory-safety vulnerabilities on Android targets, and drives an LLM agent to construct local privilege escalation exploits from an untrusted application. Across 152 candidate CVEs reported over 33 months, we reproduce 38 vulnerabilities and generate 17 independently verified exploits under production defenses. Exploitation takes a median of 14.3 agent-hours and $321 in API cost, with 90% median reliability; 12 of 14 trials succeed on Pixel 9 and Pixel 10 devices. Notably, the pipeline relies only on publicly available, off-the-shelf models. Surprisingly, only 3 of the 17 exploited CVEs appear in Android Security Bulletins, suggesting limited visibility into which upstream fixes address vulnerabilities that affect Android kernels. For these 17 CVEs, the corresponding upstream patches reach Pixel devices with a median delay of 181 days. Together, these results reveal a stark asymmetry: attackers can increasingly automate exploitation in hours, while defenders still identify and deploy fixes on the timescale of months.

---


### 44. [Agent Recovery Gone Wrong: Measuring Harm Beyond Duplicate Calls](https://arxiv.org/abs/2611.31554)

**<font color=#1a73e8>作者：</font>** Artem Trofimov, Boris Novikov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Code-executing LLM agents submit blocks of code that issue several API writes. If a block fails after some of its writes have taken effect, the agent rewrites the block and continues. It is unknown how often such a recovery harms the external state when the failure occurs naturally in the code written by the agent. In this paper, we measure it on recorded trajectories of AppWorld agents. In a stratified random sample of 200 candidate episodes across ten models, 145 are partial executions confirmed by the database state. In the sample, 30 of 143 confirmed partial executions with a determinable outcome are followed by a harmful recovery, and its violation remains at the end of the run, which gives a stratification-weighted estimate of 24.6%. Two thirds of the harmful recoveries duplicate an effect, and the rest delete user data or make a wrong first-time write, e.g., an order of a wrong product. A rule that searches for repeated calls finds 75% of duplications but only 41% of all harm. We also examine two sources of operation identity for an idempotency contract. In a small pilot (17 episodes, one local model), identifiers supplied by the model do not detectably reduce harm, because the model issues a new identifier for the same operation. Identity derived from the call content, evaluated counterfactually on the sample, would have matched every harmful write in 14 to 18 of the 30 harmful recoveries, but in none of those with a wrong first-time write, and it would also have matched writes required by the task in 30 episodes. Based on these results, we outline design requirements for safer agent recovery.

---


### 45. [COGENT: A Modular Cognitive Architecture for Agentic User Simulation](https://arxiv.org/abs/2611.31559)

**<font color=#1a73e8>作者：</font>** Yikun Chi, Adam Davies, Debarati Das 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based user simulation can support interface design, accessibility research, and interactive-agent evaluation, but standard computer-use agents are optimized for task completion rather than reproducing how people perceive, reason, and act. We introduce COGENT (COGnitive agENT), a modular cognitive architecture for simulating user interaction with desktop interfaces. COGENT draws on established cognitive theories, such as Norman's action cycle and ACT-R, to enable explainable, intervenable, and modular user simulation by decomposing the simulation process into cognitive modules with explicit representations of perception, memory, user state, intentions, and action selection. We begin by presenting six intervenability demonstrations, each tracing how a single edit to memory, a user attribute, or a processing module propagates through the cognitive pipeline to produce a behavioral change. We evaluate COGENT's behavioral and attributional fidelity across three benchmarks -- AgentNetBench, A11y-CUA, and SENSE-42 -- finding that it achieves statistically significant fidelity gains over computer-use baselines in reproducing recorded human behavior and recovers the relational structure among human self-reported psychological states. Together, these demos and evaluations demonstrate COGENT's utility toward more faithful, explainable, intervenable, and modular LLM-based cognitive simulations.

---


### 46. [CLAIMGATE: Cautious On-Device Checking of Spoken Legal and Clinical Claims](https://arxiv.org/abs/2611.31569)

**<font color=#1a73e8>作者：</font>** Peter Forcha, Harshitha Kaje Kusumadhara, Audrey Moguem Souop 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In law and medicine, a misstated rule can shape a decision before anyone has time to check it. Checking such claims in real time helps only if the checker keeps pace with conversation, keeps sensitive audio on the device, and stays silent rather than mislead. We present CLAIMGATE, an on- device assistant that listens to a conversation, detects checkable claims, retrieves the relevant official rule, and labels each claim as supported, contradicted or not covered, with a citation. CLAIMGATE is designed to fail towards silence: its 4-bit 7B- parameter language model may cite only retrieved rules, and the verdict is derived in code from the claim and rule the model quotes. We evaluate it on traffic stops and medical visits using real official rule text (5,742 Florida and Texas statute subsections; CDC, FDA and MedlinePlus guidance), real transcripts, live speech and author-written gold-labelled claims. On 141 held-out traffic-stop claims, CLAIMGATE reaches 80.1% accuracy and cuts serious errors (a true claim called false, or the reverse) from 20 to 5 compared with the same model without retrieval; deriving the verdict in code alone reduces them from 13 to 5 at no cost to accuracy. The claim gate passes 95.7% of held-out claims and rejects all 30 everyday sentences, and feedback arrives a median 1.86 s after a speech window closes on an 8 GB consumer GPU. On 148 allergy claims, with only the claim gate to rebuild, CLAIMGATE reaches 87.8% accuracy with 5 serious errors, against 20 without retrieval.

---


### 47. [Off-the-Shelf Autonomous Agents for Game Playtesting](https://arxiv.org/abs/2611.31570)

**<font color=#1a73e8>作者：</font>** Ayush Maniar, Eryk Banatt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In playtesting games, a human operator is typically required to test most gameplay elements. In this work we present Buddy, an autonomous game solving agent which can solve long time horizon objectives in an unseen 3D role-playing game using off-the-shelf language model systems. Buddy will take actions, receive feedback on those actions, and pursue a goal across many turns. No written walkthrough or model training of any kind is required, and we show that this paradigm holds in a novel environment where the agent must discover solutions via exploration rather than recalling them from pretraining. We demonstrate three downstream capabilities: game solving with no provided walkthrough, logging bug tickets for encountered difficulties, and conversion of successful agent traces into scripted hierarchical task networks for regression testing. Unlike existing playtesting solutions, our framework is fully modular: language models and harnesses can be easily swapped out as capabilities improve over time.

---


### 48. [Safe Autoformalization: Sufficiency and Necessity with Entailment Graphs](https://arxiv.org/abs/2611.31571)

**<font color=#1a73e8>作者：</font>** Umut A. Acar, Eli Goldweber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoformalization translates a natural-language statement into a formula that captures its intent, which depends on the statement's context: the background that disambiguates it. LLMs make autoformalization practical, but their probabilistic output carries no formal guarantees. We propose techniques for safe autoformalization that certify one-sided logical adequacy: a formula sufficient for the intent is safe to enforce, and a formula necessary for it is safe to rely on. We use LLMs to generate candidate formulas and order them by logical strength in an Entailment Graph (EG), an ordering a solver decides. Each edge carries a residual and a co-residual, the two adjoints of the entailment order, all fixed by the candidate pool alone. In a context, two searches return the sufficient frontier, the weakest candidates that entail the statement, and the necessary frontier, the strongest candidates the statement entails; each step is one local check against an edge's residual or co-residual. The frontiers bracket the statement and yield the ambiguity residue, which holds exactly of the situations the candidates certify neither as satisfying nor as violating it; the statement is ambiguous precisely when the residue is satisfiable. For natural-language statements and contexts, an LLM entailment oracle decides the checks; it is sound if it accepts only checks that hold, and complete if it accepts every check that holds. We prove that a sound oracle makes the search safe regardless of pool quality, and that a complete one makes the frontiers tight. On security-critical AWS properties, EGs are safe in all 20 cases of an expert-adjudicated study, where majority vote over equivalence clusters and Universal Self-Consistency are unsafe in 25% and 10%. An ablation with the same oracle but no graph is unsafe in 25% and rejects every candidate in another 30%. We machine-checked our proofs in Lean.

---


### 49. [The Paradox of Agency-Preserving AI: Negotiating Learner Agency in Layered Human-AI Interactions](https://arxiv.org/abs/2611.31573)

**<font color=#1a73e8>作者：</font>** Yueling Fan, Jacqueline Wong, Olov Engwall 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is increasingly used by learners in cognitively demanding tasks, but its capacity to provide immediate solutions raises concerns about decreased learner agency. Meta-level AI systems that provide reflective and metacognitive scaffolding have emerged as a promising approach to supporting learners' self-regulation. However, these systems introduce a fundamental paradox: AI intended to preserve learner agency can itself constrain that agency by regulating when, how, and why learners should reflect. To investigate this challenge, we conducted a co-design workshop with 18 students engaged in programming and academic writing tasks using ChatGPT extended with ChatWise, a meta-level AI system providing self-regulated learning-aligned feedback. Drawing on 185 prompt-feedback entries, 174 written reflections, and participants' design artifacts (17 storyboards and 5 group design proposals), we identified four interconnected design tensions: assistance vs reflection, immediate intervention vs space for self-regulation, visibility vs attention competition, and system adaptation vs user control. The study contributes a multidimensional account of learner agency that includes task, cognitive, and interaction agency, along with empirically grounded interaction-design mechanisms to negotiate these tensions.

---


### 50. [Lit Up but Not Needed: Scoped Lesions Show Where Multimodal Mixture-of-Experts Depend on Their Experts](https://arxiv.org/abs/2611.31576)

**<font color=#1a73e8>作者：</font>** Zhixuan Ge, Anqi Li, Kexin Geng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cognitive neuroscience learned that an activation map is not a map of necessity. Regions that light up during a task are not always needed for it, and only lesions reveal which ones are. Mixture-of-experts (MoE) vision-language models come with an activation map for free, since the router records which experts respond to image and text tokens, and recent work reads modality-specialized experts off this map. We bring the lesion. In Qwen3-VL-30B-A3B, Kimi-VL-A3B and Gemma-4-26B-A4B, 3 to 12% of the experts are vision-exclusive: image tokens route to them at up to five times the uniform rate and text tokens almost never. In Qwen3-VL they receive a quarter of all image-token routing, and lesioning all of them costs less than one percentage point on average over eight perception benchmarks and free-form OCR, no more than lesioning a random set of the same size. In Kimi-VL and Gemma-4 the lesion also costs no more than a random set. Scoped lesions, which remove an expert set only at image positions or only at text positions, then show where the models do depend on their experts. In Qwen3-VL, silencing every expert at every image position costs 3 points, against 45 at text positions, where the dependence sits in dual-use experts that text-only tasks need as well. Across models the image-side dependence is 2 to 3 points in Qwen3-VL and Kimi-VL and 26 in Gemma-4. Reading text in images is the one ability that needs image-position experts in every model. The exclusive experts receive informative patches, produce outputs of ordinary size, and stay inert under sensory deprivation: text-only training recruits them only when load balancing forces it. In Kimi-VL the balancing bias itself manufactures most of them. Load balancing draws the modality map in the part of the computation the models depend on least. Expert selection, pruning and skipping should follow the lesion, not the map.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-299](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
