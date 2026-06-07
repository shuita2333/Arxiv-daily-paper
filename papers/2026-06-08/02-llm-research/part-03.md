# 🧠 大模型相关研究 | 2026年06月08日

> 本类共 **185** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-185](./part-04.md)

---

### 101. [QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving](https://arxiv.org/abs/2606.05875)

**<font color=#1a73e8>作者：</font>** Jianxin Yan, Wangze Ni, Zhenxin Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) improves large language model (LLM) answer quality by grounding generation in external evidence, but processing retrieved contexts makes the prefill stage a dominant serving cost. RAG cache fusion reduces this cost by reusing precomputed key-value (KV) caches for retrieved chunks and selectively recomputing tokens under the current prompt. Existing selectors, however, face a dilemma between quality and efficiency: fast query-agnostic or final-layer query-to-context selectors can miss request-relevant evidence, whereas full-view query-aware selectors require broad context and layer visibility before recomputation and therefore stall the layer-wise cache-fusion pipeline. We present QCFuse, a compressed-view query-aware selector for RAG cache fusion. QCFuse uses chunk-anchor query probing to condition user-query states on compact per-chunk anchors and critical-layer profiling to identify recomputation tokens without all-layer inspection. We implement QCFuse in SGLang and evaluate it on four open-weight LLMs across six datasets. QCFuse reaches full-prefill-level quality. At matched quality, QCFuse achieves an average prefill-time speedup of 1.7x over full prefill and 1.5x over ProphetKV, the strongest quality-preserving baseline.

---


### 102. [TS-ICL: A Flexible Time-Indexed Foundation Model for Time Series via In-Context Learning](https://arxiv.org/abs/2606.05878)

**<font color=#1a73e8>作者：</font>** Etienne Le Naour, Tahar Nabil, Adrien Petralia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models mark a profound paradigm shift in time series modeling, with task-specific models being superseded by general-purpose zero-shot models. Yet, current approaches primarily focus on forecasting, while real-world time series are often irregularly and partially observed, requiring models that can jointly forecast, impute missing values, and handle degraded sampling conditions. To address these challenges, we introduce TS-ICL, a novel probabilistic In-Context Learning encoder--regressor Transformer that unifies forecasting and imputation. TS-ICL formulates time series tasks as timestamp-aligned regression and naturally incorporates covariates by training on synthetic dependency structures generated from a novel causal data prior. Empirically, TS-ICL achieves a new state-of-the-art in imputation, while remaining competitive with leading forecasting foundation models across both univariate and covariate-aware benchmarks. It shows particularly strong performance in forecasting with partially observed look-back windows.

---


### 103. [When Denser Credit Is Not Enough: Evidence-Calibrated Policy Optimization for Long-Horizon LLM Agent Training](https://arxiv.org/abs/2606.05885)

**<font color=#1a73e8>作者：</font>** Yuanfan Li, Qi Zhou, Wenjing Duan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents require reinforcement learning methods that can assign credit to intermediate decisions under sparse and delayed rewards. Recent group-based methods such as GiGPO improve over GRPO by constructing step-level advantages at repeated anchor states. However, we show that such dense credit can be statistically unreliable: under limited rollouts, rare but lucky actions may receive overly large advantages, producing divergent anchor bias and late-stage training oscillation. We propose Evidence-Calibrated Policy Optimization (ECPO), a critic-free policy optimization algorithm that calibrates step-level credit before policy updates. ECPO combines Evidence-Calibrated Action Advantage, which groups rollouts by canonical actions and shrinks low-count estimates, with Variance-Gated Credit Weighting, which suppresses anchor states dominated by within-action noise. Experiments on ALFWorld and WebShop with Qwen2.5-1.5B/7B show that ECPO consistently outperforms strong baselines, improving GiGPO by +5.2/+7.3 success points on ALFWorld/WebShop with Qwen2.5-1.5B while adding only 0.1% additional advantage-computation overhead.

---


### 104. [Staying with the Uncertainty: Uncertainty-Scaffolding Strategies for Artificial Moral Advisors in LLM-to-LLM Simulated Conversations](https://arxiv.org/abs/2606.05890)

**<font color=#1a73e8>作者：</font>** Salvatore Greco, Hainiu Xu, Jacopo Domenicucci 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed as Artificial Moral Advisors (AMA) in a variety of contexts: what kind of conversational patterns should they display? In this paper, we study how AMA can help their interlocutors "stay with the uncertainty". We propose three modes of uncertainty (Perspective-Multiplying, Tension-Preserving, Process-Reflecting) and compare them against three control conditions (Baseline, Persuasive, Sycophantic). A user-agent LLM engages in a dialogue on an ethical dilemma with an AMA following a specific uncertainty strategy, and completes pre- and post-conversation questionnaires. We further examine the effect of two persona prompt formats (Declarative and Narrative). We found that (1) no single model dominates as a simulated user agent, with open models aligning with human ambiguity through between-persona divergence and closed models through within-persona hedging; (2) declarative personas better capture initial stance diversity while narrative personas show more realistic belief revision; (3) all six AMA strategies produce distinguishable conversational patterns; and (4) uncertainty strategies differ not in how much stance revision they produce, but in the quality of engagement they sustain.

---


### 105. [High-Dimensional Theory of LoRA Fine-Tuning in a Solvable Attention Model](https://arxiv.org/abs/2606.05899)

**<font color=#1a73e8>作者：</font>** O. Duranthon, F. Boncoraglio, L. Zdeborová  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a high-dimensional statistical theory of low-rank adaptation (LoRA) in attention models, capturing the interplay between pre-training and fine-tuning. We introduce a solvable framework in which a single-head attention layer is first pre-trained on a data-abundant task and subsequently adapted via a rank-one LoRA update on limited data. In the high-dimensional limit, both stages admit a sharp asymptotic characterization in terms of a finite set of order parameters, yielding explicit predictions for test errors and representation alignment. Our analysis shows that the impact of pre-training on LoRA is summarized by an effective noise term, from which we derive prescriptions for the optimal pre-training procedure. We also demonstrate a regime with a mismatch between the value of the test error and representation quality, and propose an application of our theory to active fine-tuning.

---


### 106. [Reducing Hallucinations in Complex Question Answering using Simple Graph-based Retrieval-Augmented Generation (long version)](https://arxiv.org/abs/2606.05901)

**<font color=#1a73e8>作者：</font>** Christopher J. Wedge, Joshua Stutter, Danny Dixon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have fundamentally transformed the landscape of Natural Language Processing. Despite these advances, LLMs and LLM-based systems remain prone to a variety of failure modes. Retrieval-augmented generation (RAG) systems have emerged as a common deployment scenario seeking to both avoid the well known risk of the LLM "hallucinating" information, and to enable reasoning and question answering over proprietary information that the LLM did not have access to during training without resorting to expensive model fine-tuning.
In this work, we explore the idea of using a lightweight graph structure with a relatively simple graph schema, to support the RAG subsystem via a dedicated toolset. We design an agentic system with a variety of vector search and graph query tools operating over a structured dataset based on a curated subset of English Wikipedia articles, and evaluate its performance on questions from MoNaCo, a challenging Wikipedia QA benchmark of complex query answering tasks.
Our results show that the introduction of graph-based tools can significantly increase the precision and recall of factual correctness, can halve the number of hallucinated answers, and achieves the highest fine-grained truthfulness score among the three evaluated scenarios. All this with a modest increase in token usage.

---


### 107. [Retrospective Harness Optimization: Improving LLM Agents via Self-Preference over Trajectory Rollouts](https://arxiv.org/abs/2606.05922)

**<font color=#1a73e8>作者：</font>** Wenbo Pan, Shujie Liu, Chin-Yew Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents rely on a harness of skills, tools, and workflows to solve complex problems. Continually improving this harness is essential for adapting to new tasks. However, existing optimization methods typically require ground-truth validation sets, yet such labeled data is difficult to acquire in practical deployment settings. To address this problem, we introduce Retrospective Harness Optimization (RHO), a self-supervised method that optimizes the agent harness using only past trajectories. Specifically, RHO selects a diverse coreset of challenging tasks from past trajectories and re-solves them in parallel. The agent analyzes these rollouts using self-validation and self-consistency, then generates candidate harness updates and selects the most effective one by its own pairwise self-preference. We evaluate RHO across three diverse domains, spanning software engineering, technical work, and knowledge work. Notably, a single optimization round improves the pass rate on SWE-Bench Pro from 59% to 78% without any external grading. Furthermore, our analysis demonstrates that RHO effectively targets prior failure modes. As a result, the optimized harness alters the agent's behavior patterns and sustains higher accuracy during long-horizon sessions.

---


### 108. [Better Literary Translation: A Multi-Aspect Data Generation and LLM Training Approach](https://arxiv.org/abs/2606.05924)

**<font color=#1a73e8>作者：</font>** Zhihao Lin, Ziqi Zhu, Hao Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Literary translation poses unique challenges due to the scarcity of high-quality annotated data and the need to balance expression fluency with literary effect. We present a multi-aspect iterative refinement framework that generates high-quality translation references and preference data through specialized LLM translators, each targeting a distinct quality dimension. We leverage the generated data for supervised fine-tuning and reinforcement learning. Experiments show that our generated references outperform the original ground truth for SFT by 8.65 CEA100 points. For reinforcement learning, we find that DPO leads to performance degradation in this setting, while leveraging an explicit reward model for GRPO yields an additional 1.51 point improvement. We attribute this to the stability of two-stage training and GRPO's online exploration capability. Our resulting models, LitMT-8B and LitMT-14B, achieve 67.25 and 69.07 CEA100 respectively on the MetaphorTrans English-to-Chinese literary translation benchmark, competitive with Claude Sonnet 4.5 at 68.43, and demonstrate strong generalization to out-of-domain literary work (i.e., O. Henry).

---


### 109. [Towards World Models in Biomedical Research](https://arxiv.org/abs/2606.05925)

**<font color=#1a73e8>作者：</font>** Guangyu Wang, Jingkun Yue, Siqi Zhang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A central goal of biomedicine is to understand, predict and ultimately control the dynamic mechanisms by which biological systems respond to perturbations, disease progression and therapeutic intervention. Although foundation models and large language models have accelerated biomedical data interpretation, most current systems remain focused on static pattern recognition rather than prospective simulation of biological futures. Here we propose biomedical world models as a paradigm for AI-driven discovery. These models learn latent representations of molecular, cellular, tissue and clinical states, together with intervention-conditioned dynamics that allow future trajectories to be simulated before actions are taken. We discuss how biomedical world models could function as data engines, environment simulators and scientific planning substrates across applications including virtual cells, organoids, virtual patients and surgical simulation. We outline the data infrastructure, evaluation benchmarks, safety constraints and governance frameworks required. Biomedical world models may provide a foundation for simulation-guided, closed-loop and experimentally actionable biomedical discovery.

---


### 110. [To Be Multimodal or Not to Be: Query-Adaptive Audio-Visual Person Retrieval via Active Modality Detection](https://arxiv.org/abs/2606.05931)

**<font color=#1a73e8>作者：</font>** Erfan Loweimi, Mengjie Qian, Kate Knill 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When retrieving a person from a video archive by voice and face, should the system be multimodal or not? In real-world broadcast archives, unlike curated benchmarks, a target may be heard but unseen, seen but unheard, or both. Fusing scores from an absent modality injects noise, degrading precision below the best unimodal system. We propose a query-adaptive framework that detects active modalities via cross-modal score consistency: when both modalities are active, files retrieved by one also score highly on the other; this agreement breaks down when a modality is absent. Classifiers driven by these cross-modal features achieve 89% detection accuracy. On the BBC Rewind corpus (with over 12,000 broadcast videos) the adaptive system attains 94.2% P@1, outperforming speaker-only (82.9%), face-only (93.4%), and fixed fusion (90.0%), recovering 64% of the gap to an oracle with ground-truth modality labels (96.6%).

---


### 111. [Epistemic Injustice in Language Models: An Audit of Pretraining Filters and Guardrails](https://arxiv.org/abs/2606.05936)

**<font color=#1a73e8>作者：</font>** Marco Antonio Stranisci, A Pranav, Rossana Damiano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern language models rely on pretraining filters to remove undesirable content from training corpora and inference-time guardrails to suppress undesirable outputs during deployment. In this paper, we examine how these filtering and moderation decisions produce forms of epistemic erasure and reveal tensions both across automated systems and between these systems and human judgment. We audit four pretraining filters and three inference-time guardrails on Common Crawl sentences containing gender and regional-origin mentions, together with a manually annotated subset of 500 sentences. Our analysis shows that filtering and guardrail decisions are strongly associated with blocklist-based lexical cues, while frequently failing to flag content containing private information or explicit hate speech. At the same time, marginalized groups, particularly transgender people, women, and Central Americans, are significantly over-flagged across systems. Human annotators, by contrast, would retain 88.5\% of filter-flagged and 91.3\% of guardrail-flagged content, often recognizing representational harms arising from tensions of content removal that current systems fail to capture. Taken together, our findings document a form of epistemic erasure in which mentions of marginalized groups are disproportionately removed before pretraining and additionally suppressed again at inference time.

---


### 112. [Large Language Models are Perplexed by some Political Parties](https://arxiv.org/abs/2606.05937)

**<font color=#1a73e8>作者：</font>** Paul Lerner, François Yvon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used, including in political applications, but their political fairness has been little studied. We assess it using perplexity, posing that a fair model should give equal probability to all political groups. However, we find, across ten LLMs and three datasets covering 37 languages, that LLMs are more perplexed by the texts of far right and nationalist parties than of social-democratic parties. We find this to be consistent with previous work on translation fairness, to the point that perplexity correlates with downstream translation metrics. Our method is applicable to both base LLMs as well as their instruction-tuned counterpart, and we find that both are highly correlated, suggesting that the political fairness of LLMs stems from their pretraining, and is hardly affected by instruction-tuning.

---


### 113. [Faithful, Enriched, and Precise: Benchmarking Natural-Science Illustration Generation by T2I models](https://arxiv.org/abs/2606.05949)

**<font color=#1a73e8>作者：</font>** Yifan Chang, Jiaxin Ai, Jianwen Sun 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific illustrations are essential tools for communicating research findings, especially in natural science, where they visualize complex concepts and processes. As Text-to-Image (T2I) models become increasingly capable, researchers have started to use them for scientific illustration generation. However, existing benchmarks often assess outputs at a holistic level, overlooking fine-grained elements, while scientific reasoning ability and output conciseness remain under-quantified. We introduce FEPBench, a benchmark built from carefully selected high-quality scientific illustrations across multiple disciplines and layout types. With the assistance of multimodal large language models (MLLMs) and human experts, we provide fine-grained atom set annotations and systematically evaluate T2I models along three dimensions: instruction faithfulness, reasoning enrichment, and semantic precision. Our evaluation further decomposes model performance across visual, textual, relation, and layout elements. Results show that even state-of-the-art (SOTA) closed-source models, such as GPT Image 2 and Nano Banana Pro, still suffer from text-rendering bottlenecks, limited reasoning enrichment, and difficulty balancing generation richness with precision. These findings provide practical guidance for improving and deploying T2I models in scientific illustration generation. Benchmark data, atom set annotations, and evaluation code will be released by us.

---


### 114. [Steering Vectors are an Adversarial Attack Surface](https://arxiv.org/abs/2606.05958)

**<font color=#1a73e8>作者：</font>** Abzal Aidakhmetov, Donato Crisostomi, Tommaso Mencattini 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering has become a popular way to control Large Language Model (LLM) behavior without fine-tuning. Since the technique is plug-and-play, users share datasets and precomputed vectors to steer model activations. However, we show that a \emph{stealth data poisoning attack} silently compromises this pipeline. By substituting $4{-}6\%$ of tokens in the steering dataset, an attacker can silently align the resulting vector with an anti-refusal direction. This jailbreaks the target model while preserving the intended steering effect on benign prompts. Under this threat model, a malicious actor can distribute an apparently safe bundle containing texts, vectors, and weights, alongside an equivalence certificate that the end-user can verify. We test the attack on two open-weight model families and eight model-attribute combinations, observing that poisoned vectors reach an absolute attack success rate (ASR) of $20{-}55\%$, $+19\%$ to $+51\%$ over a clean reference. Finally, we find that a refusal-direction orthogonalization defense can recover ${\approx}82\%$ of the ASR gap without harming benign behavior.

---


### 115. [Measuring the sensitivity of LLM-based structured extraction to prompt, model, and schema choices in clinical discharge summaries](https://arxiv.org/abs/2606.05970)

**<font color=#1a73e8>作者：</font>** Martin Murin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used for structured extraction from clinical free-text notes, but the sensitivity of their output to upstream configuration choices is less understood than their accuracy on fixed benchmarks. This work measures that sensitivity without human-annotated ground truth, by holding the extraction task fixed and varying one choice at a time. The fixed schema comprises 17 clinical documentation flags on a three-way yes/no/not_documented value set and a 47-tag vocabulary for the primary admission reason. Three prompt variants expressing this schema were each run at two model sizes on MIMIC-IV v3.1 discharge summaries. Cross-prompt agreement was measured by Cohen's kappa on ICD-stratified subsets. A paired same-note comparison isolated the effect of model choice, and a post-hoc collapse of the three-way flags to binary tested the schema's contribution to disagreement. On the three-way flags, the two models reach the same pooled cross-prompt agreement (median kappa 0.69 and 0.68); the larger model raises agreement on some fields and lowers it on others, a redistribution rather than the absence of an effect. Collapsing the schema to binary dissolves most of the cross-prompt disagreement, locating it on the absence-versus-silence distinction rather than on whether the finding is present. On the multi-class admission categorization, changing the model reassigns the dominant tag on close to half of all notes while changing the prompt phrasing reassigns it on roughly one in eight, and the larger model places far less mass on residual catch-all categories (44% to 26%). These patterns indicate a schema-imposed source of disagreement concentrated on the absence-versus-silence axis and a dominance of model over prompt phrasing on multi-class categorization, identified by a reusable methodology for auditing extraction reproducibility on a population-scale deployment.

---


### 116. [LLM Explainability with Counterfactual Chains and Causal Graphs](https://arxiv.org/abs/2606.05972)

**<font color=#1a73e8>作者：</font>** Nirit Nussbaum-Hoffer, Nitay Calderon, Liat Ein-Dor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal graphs provide a high-level language for making mechanisms transparent. Recent work uses Large Language Models (LLMs) to recover causal graphs of external-world processes. Instead, in this paper, we use causal graphs to model LLM inference itself, providing stakeholders with a transparent view of how the model perceives and organizes high-level concepts to produce a prediction. We propose a four-phase method for constructing such graphs. Given a target LLM and a set of textual examples, our method discovers class-discriminative, human-interpretable concepts and maps each input to LLM-perceived concept states. We then introduce an MCMC-inspired counterfactual augmentation procedure that expands the sparse observational data through chains of counterfactuals. This enables stable causal discovery with $\sigma$-CG, yielding informative, interpretable graphs. We apply our method to three LLMs across disease diagnosis, sentiment analysis, and LLM-as-a-judge classification tasks. We evaluate the learned graphs for predictive fidelity and structural stability, and the MCMC-inspired augmentation for convergence and downstream utility. Our results show that the discovered causal graphs capture meaningful dependencies consistent with LLMs' reasoning. Together, this paper provides a foundation for concept-level explainability of LLMs.

---


### 117. [The Self-Correction Illusion: LLMs Correct Others but Not Themselves](https://arxiv.org/abs/2606.05976)

**<font color=#1a73e8>作者：</font>** Kuan-Yen Chen, Fang-Yi Su, Jung-Hsien Chiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work shows that LLM agents struggle to correct errors in their own reasoning traces yet show markedly higher correction rates when identical claims appear under external sources. We ask whether this asymmetry reflects a capability deficit or a role-label artifact: does an agent's willingness to correct a wrong claim depend causally on the chat-template role that carries it, rather than on the claim's content? Our setup keeps the erroneous claim byte-identical across all conditions (SHA-256 verified) and varies only its wrapping role: the agent's own \role{<thought>}, a \role{user} message, a \role{tool} response, or a \role{system <memory>} block. Across 13 model-domain cells covering seven model families and three domains ($n{=}30$ paired tasks per cell), relabeling the claim from \role{<thought>} to an external role lifts the explicit-correction rate by 23 to 93 percentage points, with 10 of 13 cells reaching $p{<}0.001$. Further experiments confirm that the effect is asymmetric, mechanistically decomposable, and robust across domains. The failure to self-correct is not a cognitive deficit; it is a chat-template artifact. We exploit this artifact by designing a prompt-structure-only intervention that requires no training and no model modification, with its strongest role label being domain-dependent: \role{<memory>} dominates on math, while a plain \role{user} message dominates on logical deduction.

---


### 118. [Video-Rate Streaming Stylization on a Vision-Aware MLLM-Conditioned Edit Diffusion: Asymmetric Batched Inference on a Distilled UNet + MLLM Text Encoder](https://arxiv.org/abs/2606.05981)

**<font color=#1a73e8>作者：</font>** Yoshiyuki Ootani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aggressive distillation of the diffusion U-Net inverts the per-frame bottleneck of real-time text-to-image pipelines: once the denoiser is a 4-step or 1-step distilled student, the text encoder becomes the critical path. This inversion is most acute in vision-aware edit diffusion, where the encoder is a multimodal large language model (MLLM). We study the case of a 0.39B distilled edit U-Net paired with a 2.13B MLLM text encoder (Qwen3-VL) and present a streaming pipeline targeted at this regime built around three engineering mechanisms: asymmetric side-stream / main-stream CUDA pipelining with batched text-encoder amortisation (and optional static-prompt caching), a compile-friendly ControlNet-LLLite reformulation that folds the entire U-Net + adapter stack into a single fused graph, and a periodic conditioning-refresh schedule with a hook subset that amortises the per-frame conditioning cost. On a single consumer RTX 3090 Ti at 512x512 the pipeline sustains 27.4 fps over a 480-frame run at batch size B=8 and 29.6 fps at B=16, with end-to-end p50 latency of approximately 0.5 and 1.0 seconds respectively; the same operating point measures 54.9 fps on RTX 4090 and 74.1 fps on RTX 5090. We report video-rate streaming throughput rather than interactive low latency, and locate our numbers against same-stack StreamDiffusion re-runs as systems context, not as a benchmark superiority claim. For the trained oil-painting style, the released temporal adapter generalises within in-clip noise to 19 unused DAVIS-2017 sequences and 15 non-DAVIS clips from seven sources; prompt-level generalisation to unseen style families is bounded and reported separately.

---


### 119. [Beyond Alignment: Value Diversity as a Collective Property in Multicultural Agent Systems](https://arxiv.org/abs/2606.05985)

**<font color=#1a73e8>作者：</font>** Shaoyang Xu, Jingshen Zhang, Long P. Hoang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multicultural multi-agent systems are increasingly deployed in globally diverse settings, where different agents are grounded in different cultural backgrounds. Existing cultural evaluation focuses on value alignment: how closely a single agent matches a target culture. Yet alignment is a per-agent property and cannot reveal whether a system, taken as a whole, preserves the cultural plurality it is meant to represent. We propose value diversity as a system-level evaluation axis for multicultural agent systems, defined through the dissimilarity between culturally conditioned agents' responses on a shared value survey. Using the World Values Survey, we evaluate 19 cultures and 18 backbone models across a wide range of system configurations. We find that diversity is largely uncorrelated with alignment, indicating that the two capture complementary system properties, and that current multicultural agent systems fall substantially below human societies in value diversity. Mixed-backbone systems narrow this gap but do not close it, and the gap persists across culture compositions and agent scales. Social interaction further erodes diversity by driving agents toward consensus, and a participatory budgeting case study shows that this homogenization narrows the breadth of collective decision-making. Together, our results establish value diversity as a distinct evaluation axis for multicultural multi-agent systems and reveal a persistent homogenization tendency in current LLM-based societies. Our code and data are publicly available at this https URL.

---


### 120. [Compress-Distill: Reasoning Trace Compression for Efficient Knowledge Distillation](https://arxiv.org/abs/2606.05988)

**<font color=#1a73e8>作者：</font>** Maxime Griot, Paul Steven Scotti, Tanishq Mathew Abraham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models produce long chain-of-thought traces that are costly to distill and encourage verbose student outputs. We study post-hoc compression of such traces before knowledge distillation. Two teachers, Qwen3.5-397B-A17B and gpt-oss-120B, generate about 283k correct traces each; two instruction-tuned models then compress them to 8.6-21.0% of their original character length. Across a 48-run main grid plus seven Qwen-teacher truncation ablations, compressed traces reduce training tokens to 12-30% of raw, speed up training by 2.0-7.6x, and shorten inference outputs by 3-19x with smaller reductions under the shorter gpt-oss teacher. However, raw traces retain the highest downstream accuracy at every scale and for both teachers. A length-matched raw-trace truncation ablation shows that compression is not merely benefiting from a smaller token budget: model-compressed traces usually beat or match naive truncation, especially for smaller students, while maintaining shorter inference outputs. Overall, reasoning-trace compression offers an accuracy-efficiency trade-off rather than a free improvement: students retain up to 96% of raw-trace accuracy while gaining up to 18x higher per-token efficiency, and at the 0.8B scale under LoRA compressed traces narrow the raw-vs-compressed gap but do not exceed raw.

---


### 121. [Multimodal Sexism Identification and Characterization using Large Language Models and Gradient Boosting](https://arxiv.org/abs/2606.05997)

**<font color=#1a73e8>作者：</font>** Kyriakos Chaviaras, Maria Lymperaiou, Athanasios Voulodimos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present the AILS-NTUA submission to the EXIST 2026 Lab at CLEF, addressing multimodal sexism identification and characterization in memes (Task 2) and short-form videos (Task 3). Our system follows a feature-engineered late-fusion pipeline built around gradient-boosted regression models and hierarchical post-processing. For memes, we combine visual, textual, demographic, biometric, and LLM-derived semantic indicators designed to capture high-level cues such as stereotyping, objectification, irony, and misogyny. For videos, we investigate the effect of feature selection, frame-based visual representations, OCR-based textual features, acoustic descriptors, and sensor-derived metadata. Development results show that focused LLM-derived semantic cues improve meme sexism identification, while video performance is highly sensitive to feature dimensionality and cross-modal noise. For videos, development results favor compact feature selection, but official test results show that this conclusion does not fully transfer to unseen data, where the unfiltered representation generalizes better. Overall, our findings highlight the usefulness of targeted semantic feature engineering for static memes and the need for more robust temporal modeling in noisy short-form video settings.

---


### 122. [Global-Local Monte Carlo Tree Search in Vision-Language Models for Text-to-3D Indoor Scene Generation](https://arxiv.org/abs/2606.06002)

**<font color=#1a73e8>作者：</font>** Mengshi Qi, Wei Deng, Xianlin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models have achieved significant reasoning performance in various this http URL, there are few studies on text-to-3D indoor scene generation with LVLMs. The main challenge is that prevailing LVLM-based methods employ chain-of-thought sequential decision mechanisms that cannot revise earlier decisions, causing error this http URL this paper, we consider the task as a planning problem constrained by spatial and layout this http URL solve this problem, we model it as a tree search problem with global and local trees, which differs from existing sequential decision-making this http URL the global tree, we place each object iteratively and explore multiple attempts like humans furnishing a room, where the problem space is represented as a this http URL effectively search the tree, we propose a hierarchical scene representation and a PRM-guided MCTS this http URL hierarchical representation abstracts a scene into room level, region level, floor object level, and supported object this http URL PRM-guided MCTS method uses the PRM to prune unnecessary branches and the MCTS algorithm to balance exploration and exploitation to get an optimal solution with fewer this http URL the local tree, it further decomposes the placement of each object into finer sub-steps, including the specific placement this http URL make the whole appearance of the scene consistent, we leverage pre-trained diffusion image generative models to predict textures for all the objects in the this http URL existing benchmarks for text-to-3D indoor scene generation remain limited in scale and diversity, we collect a new large-scale diverse dataset that contains 65 scene types and 3,250 instructions with diverse sizes, layouts, and styles, named 3DTindo-bench, to better assess the capability of the state-of-the-art models. Our experiments show that our method generates more realistic 3D scenes than state-of-the-art approaches.

---


### 123. [The Generator-Eraser Paradox: Community Guidelines for Responsible LLM-Assisted Dialect Resource Creation](https://arxiv.org/abs/2606.06004)

**<font color=#1a73e8>作者：</font>** Wajdi Zaghouani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialect resources occupy a unique position at the intersection of scientific description, cultural preservation, and computational infrastructure. Large language models offer powerful capabilities for accelerating dialect resource development through retrieval-grounded drafting, corpus navigation, metadata enrichment, and annotation workflow support. However, the same systems pose substantial risks: they can contribute to dialect erasure by privileging prestige varieties, homogenizing orthography, and enabling synthetic feedback loops that reduce linguistic diversity over time. These risks are particularly acute for language varieties characterized by diglossia, limited written standardization, or marginalized speaker communities. This paper makes three contributions. First, we integrate insights from variationist sociolinguistics and corpus linguistics to formalize the generator-eraser paradox as a theoretical framework for understanding the dual nature of LLM-assisted dialect work. Second, we derive 12 community guidelines that operationalize this framework into implementable design requirements for dialect resource creation and documentation. Third, we provide an in-depth case study of Arabic dialects, including a structured comparison of widely used resources, to demonstrate how these guidelines address language-specific challenges including diglossia, orthographic variability, and community governance. The contribution is conceptual and operational rather than experimental, with the goal of enabling dialect communities and resource builders across languages to adopt LLMs without sacrificing authenticity, variation, or sovereignty.

---


### 124. [Adaptive Oscillatory-State Alignment for Time Series Forecasting](https://arxiv.org/abs/2606.06010)

**<font color=#1a73e8>作者：</font>** Zhangyao Song, Ziqiong Li, Xiangfei Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting benefits from inductive biases that expose recurring temporal structure. Existing periodic forecasting methods typically model recurrence through predefined periods, global spectral components, or fixed learnable templates. However, real-world temporal dynamics are rarely rigidly periodic: oscillatory behavior often evolves through amplitude modulation, phase drift, and local frequency variation. Under these conditions, fixed-template periodic modeling can become fundamentally mismatched to the underlying temporal states. We propose AOSNET, a Hilbert-guided forecasting framework that reformulates periodic forecasting from fixed template matching to adaptive oscillatory-state alignment. AOSNET extracts analytic-signal descriptors from both the observed sequence and a learnable global oscillatory prior, then adaptively aligns local states through a descriptor-conditioned gate that selectively preserves reliable observations while softly correcting mismatched regions. The learned prior serves not as a rigid repeated template but as a flexible oscillatory reference interpreted through local state dynamics. Experiments on eight benchmarks demonstrate state-of-the-art or highly competitive accuracy with fast inference speed. Controlled synthetic studies isolating amplitude modulation, phase drift, and local frequency variation confirm that the advantage of oscillatory-state alignment consistently increases as non-stationarity intensifies.

---


### 125. [PLAN-S: Bridging Planning with Latent Style Dynamics for Autonomous Driving World Models](https://arxiv.org/abs/2606.06014)

**<font color=#1a73e8>作者：</font>** Xiaoyun Qiu, Jingtao He, Yijie Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent world models (LWMs) have strengthened end-to-end autonomous driving by forecasting compact scene dynamics for downstream planning. However, existing LWM-based planners usually generate trajectories directly from entangled latent representations. This compact latent-to-planner pathway lacks explicit modeling of risk, drivability, and diverse style preferences, making driving-style dynamics difficult to supervise, inspect, or modulate before a final trajectory is selected. We propose PLAN-S (PLANning with latent Style dynamics), a planner-facing bridge that addresses this compactness-controllability dilemma by decoding a style-conditioned, four-channel semantic cost map from the latent representation. The cost map is conditioned on ego state and driving style and is consumed up-stream of the planning decision through two host-side interfaces: attention-level fusion for regression planners and reward-level fusion for anchor-score planners. We validate PLAN-S on two architecturally distinct hosts, ResWorld on nuScenes and WoTE on NAVSIM, while keeping the host backbones frozen to isolate the contribution of the proposed bridge. On nuScenes, PLAN-S reduces L2 at every horizon over the baseline, with 0.55 m average L2 and a 42% relative reduction in the 3 s collision rate. On NAVSIM, the rule-cost variant reaches 89.4 Predictive Driver Model Score (PDMS), while the learned cost variant provides complementary gains on baseline-challenging scenes. Ablations show that the cost pathway contributes most directly to safer trajectory selection. Qualitative results further show that PLAN-S can produce diverse cost maps, with spatially consistent variations aligned to different driving styles.

---


### 126. [EGTR-Review: Efficient Evidence-Grounded Scientific Peer Review Generation via Multi-Agent Teacher Distillation](https://arxiv.org/abs/2606.06025)

**<font color=#1a73e8>作者：</font>** Xinpeng Qiu, Wang Yihu, Zhifeng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific peer review generation has attracted increasing attention for reducing reviewing burdens and providing timely feedback. However, existing Large Language Model (LLM)-based methods often produce generic comments with insufficient evidence support and weak source traceability, while complex multi-agent systems incur high inference costs. To address these challenges, we propose EGTR-Review, an Evidence-Grounded and Traceable Review Generation framework via Multi-Agent Teacher Distillation. EGTR-Review first constructs a multi-agent teacher that performs structure-aware paper decomposition, key-element extraction, external scholarly evidence retrieval, evidence-state labeling, verification reasoning, and review synthesis. It then distills both intermediate reasoning trajectories and final review comments into a lightweight student model through task-prefix-driven multi-task learning. An evidence-weighted objective further reduces the influence of weak, missing, or non-verifiable supervision. Experiments on public peer-review datasets show that EGTR-Review (Student) outperforms strong prompt-based, fine-tuned, and structured/agentic baselines across automatic metrics, LLM-as-Judge evaluation, and human evaluation, while maintaining strong factual grounding and source traceability with substantially lower token consumption and inference time. Our code, prompts, configurations, and sample data are available on GitHub.

---


### 127. [RedditPersona: A Modular Framework for Community-Conditioned LLM Adaptation from Reddit](https://arxiv.org/abs/2606.06027)

**<font color=#1a73e8>作者：</font>** Amirhossein Ghaffari, Ali Goodarzi, Huong Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Community-conditioned language model adaptation requires choices about data collection, community definition, and evaluation that are currently made independently in each study, making it hard to compare assumptions or reuse artifacts. We present RedditPersona, a modular framework that standardizes these choices: it collects Reddit posts and comments, profiles active users, partitions them under five grouping strategies (subreddit-based, graph-structural, semantic, hybrid, and interaction-based), trains a parameter-efficient adapter per strategy via QLoRA, and evaluates them under a shared metric suite spanning fluency, fidelity, distributional alignment, and community identifiability. Applied to 112 subreddits in the urban well-being domain (301,429 user profiles, 16M+ comments), we find that adapters' behavioral identifiability tracks each strategy's intrinsic agreement with the subreddit baseline, and that a consistent trade-off between identifiability and distributional similarity to real text holds across all five strategies. The code and configuration files are available at: this https URL.

---


### 128. [NAVIRA: Decoupled Stochastic Remasking for Masked Diffusion Language Models](https://arxiv.org/abs/2606.06031)

**<font color=#1a73e8>作者：</font>** Andrey Fomenko, Maksim Kryzhanovskiy, Svetlana Glazyrina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models generate text by iteratively unmasking many tokens in parallel, but this speed comes with a correction problem: tokens generated in the same step are predicted from marginal distributions, and early local dependency errors can later contaminate the context. PRISM addresses this by learning token-level quality scores and remasking unreliable tokens, but its inference rule is coupled: the same forward pass both detects low-quality tokens and computes logits for their replacements, so the erroneous tokens still condition regeneration. We propose NAVIRA, an inference-time decoding policy that separates these two operations and samples remasking positions stochastically. A first forward pass scores tokens; selected tokens are masked; a second forward pass regenerates from the cleaned context. Temperature-controlled remasking reduces repeated correction of the same positions and balances fluency against diversity. In controlled experiments with a 170M masked diffusion language model, decoupling improves fluency, while scheduled stochastic remasking preserves entropy and achieves stronger LLM-judge scores under larger forward-pass budgets. These results show that remasking policy, not only the learned quality signal, is central to reliable masked-diffusion text generation.

---


### 129. [Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents](https://arxiv.org/abs/2606.06036)

**<font color=#1a73e8>作者：</font>** Shuo Ji, Yibo Li, Bryan Hooi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite recent progress, LLM agents still struggle with reasoning over long interaction histories. While current memory-augmented agents rely on a static retrieve-then-reason paradigm, this rigid pipeline design prevents them from dynamically adapting memory access to intermediate evidence discovered during inference. To bridge this gap, we propose MRAgent, a framework that combines an associative memory graph with an active reconstruction mechanism. We represent memory as a Cue-Tag-Content graph, where associative tags serve as semantic bridges connecting fine-grained cues to memory contents. Operating on this structure, our active reconstruction mechanism integrates LLM reasoning directly into memory access, allowing the agent to iteratively explore and prune retrieval paths based on accumulated evidence. This ensures that memory retrieval is dynamically adapted to the reasoning context while avoiding combinatorial explosion caused by unconstrained expansion. Experiments on the LoCoMo benchmark and LongMemEval benchmark demonstrate significant improvements over strong baselines (up to 23%), while substantially reducing token and runtime cost, highlighting the effectiveness of active and associative reconstruction for long-horizon memory reasoning.

---


### 130. [LoomVideo: Unifying Multimodal Inputs into Video Generation and Editing](https://arxiv.org/abs/2606.06042)

**<font color=#1a73e8>作者：</font>** Jianzong Wu, Hao Lian, Jiongfan Yang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing unified video generation and editing models capable of interpreting interleaved multimodal inputs is a promising yet challenging frontier field. Existing unified frameworks predominantly rely on massive models (typically 13B parameters or more) and incorporate source video conditions for editing by concatenating sequence tokens. This concatenation inevitably doubles the sequence length, quadrupling the computational complexity of the self-attention mechanism and introducing prohibitive overhead. To address these bottlenecks, we present LoomVideo, a highly efficient 5B-parameter unified architecture for both video generation and editing. LoomVideo replaces the standard text encoder with a Multimodal Large Language Model (MLLM) and employs Deepstack injection mechanism to align multi-layer MLLM features with the Diffusion Transformer (DiT). Crucially, we introduce a zero-overhead Scale-and-Add conditioning approach for video editing. By scaling and directly adding the clean source video latent to the noised target latent, this elegant design eliminates the need for token concatenation, drastically reducing computational cost while maintaining robust capabilities for complex, non-rigid edits. Furthermore, a Negative Temporal RoPE strategy is seamlessly integrated to handle multiple reference images. Extensive experiments demonstrate that our compact 5B model achieves state-of-the-art or highly competitive performance across comprehensive benchmarks, exhibiting exceptional superiority in e-commerce and fashion generation scenarios. Benefiting from the zero-overhead conditioning mechanism, LoomVideo achieves at least a 5.41x acceleration in inference speed compared to models of similar capabilities, paving the way for highly practical and efficient video foundation models.

---


### 131. [IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval](https://arxiv.org/abs/2606.06044)

**<font color=#1a73e8>作者：</font>** Xiaoman Wang, Yaoze Zhang, Wenzhuo Fan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has shown strong effectiveness in grounding Large Language Models (LLMs) with external knowledge. However, existing RAG and Graph RAG frameworks largely treat knowledge as static or associate time with coarse-grained timestamps or metadata, failing to capture rich temporal structures such as duration, overlap, and containment. We propose IA-RAG, a hierarchical temporal RAG framework that models knowledge as time intervals and performs retrieval under formal temporal constraints. IA-RAG represents facts as Interval Event Units (IEUs) and organizes them into a hierarchical Thematic Forest, where temporal dependencies are governed by Allen's Interval Algebra. To handle incomplete or uncertain temporal boundaries, IA-RAG further introduces a Sub-graph Time Tightening mechanism that refines fuzzy intervals through logical constraints within connected event subgraphs. In addition, IA-RAG supports implicit temporal semantic retrieval through interval-algebra-guided traversal. Experiments on multiple temporal question answering benchmarks, including TimeQA, TempReason, and ComplexTR, demonstrate that IA-RAG achieves strong temporal retrieval and reasoning performance, particularly on complex compositional temporal reasoning tasks. Our code is released at this https URL.

---


### 132. [LLM-Conditioned Synthesis of Pathological Gaits via Structured Gait-Language Representations](https://arxiv.org/abs/2606.06048)

**<font color=#1a73e8>作者：</font>** Mritula Chandrasekaran, Sanket Kachole, Jarik Francik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathological gait datasets remain scarce due to privacy, recruitment, cost, and movement variability. Our work presents a multimodal LLM-guided framework for pathology-aware 3D gait data synthesis from structured textual descriptions. The proposed method generates fixed-length synthetic skeleton-based gait sequences for pathological gait classification tasks. The framework combines motion tokenisation, pathology-aware language conditioning, LLM-based semantic augmentation, and language-to-gait generation. A key contribution is the proposed pathological tokeniser, which is designed to preserve pathology-specific motion characteristics during discrete representation learning. Experiments suggest that the proposed synthetic sequences improve downstream classification for recurrent classifiers when combined with real data. The best result is obtained using a GRU classifier trained with real and synthetic samples, achieving 92.77\% accuracy under a leave-one-subject-out protocol.

---


### 133. [When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents](https://arxiv.org/abs/2606.06055)

**<font color=#1a73e8>作者：</font>** Lingxiang Xu, Jiaoyun Yang, Min Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables language model agents to support personalized interactions, but it remains unclear when available memories warrant integration into responses. Existing memory evaluations emphasize retrieval accuracy and downstream task utility, while overlooking whether retrieved sensitive memory content is warranted in the current turn. We introduce RBI-Eval, a controlled measurement study built around a probe set that compares model behavior with and without access to sensitive memory under identical benign prompts. We evaluate four base LLMs against a matched no-memory reference across four memory-access settings: full-context exposure and three retrieval systems. Our results reveal substantial behavioral divergence. With memory available, the separation score for sensitive-memory integration decreases by 8.9\%--26.6\% relative to the matched no-memory reference for GPT-5.4-mini, but by 51.1\%--82.9\% for Claude-Sonnet-4.6, DeepSeek-V4-Flash, and Qwen3.5-9B. Control experiments on DeepSeek and GPT-5.4-mini show this effect is specific to sensitive content, rather than general personalization. Retrieval systems reduce exposure but do not eliminate integration once sensitive memory reaches the generator. These findings suggest safe personalization requires memory-aware decisions at both retrieval and generation time.

---


### 134. [Learning Visual Spatial Planning from Symbolic State via Modality-Gap-Aware Self-Distillation](https://arxiv.org/abs/2606.06076)

**<font color=#1a73e8>作者：</font>** Haocheng Luo, Jiahui Liu, Ruicheng Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While vision-language models excel at general multimodal understanding, they still struggle with visual spatial planning. We attribute this to a perception-reasoning modality gap: visual planning requires models to infer latent state structures from pixels and then reason over the recovered structure to produce valid actions, whereas symbolic planning directly leverages explicit objects and constraints. This creates dual bottlenecks in visual state recovery and multi-step planning. To address this, we propose MGSD, a two-stage modality-gap-aware self-distillation framework. First, a cold-start grounding stage equips the visual student with reliable state representations, minimizing early perception noise. Second, a privileged teacher transfers planning capabilities via on-policy distillation, using explicit symbolic states to supervise the student's own visual rollout prefixes. Crucially, symbolic data is used strictly during training, leaving inference purely visual. Experiments on visual planning benchmarks show that MGSD consistently improves visual planning across both 4B and 8B backbones, raising the macro average by 19.3% and 18.4%, respectively. The resulting models narrow the gap to symbolic-input upper bounds, while ablations and diagnostics confirm that the improvement comes from both visual state recovery and optimal-path reasoning. These results suggest that modality-gap-aware self-distillation improves not only how models perceive actionable states, but also how they plan over the inferred structure. Code is available at this https URL.

---


### 135. [LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents](https://arxiv.org/abs/2606.06087)

**<font color=#1a73e8>作者：</font>** Aofan Yu, Chenyu Zhou, Tianyi Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent systems increasingly use textual skills to encode reusable task procedures, but injecting these skills into the prompt at every step incurs substantial context overhead and exposes skill content as plaintext. We present LatentSkill, a framework that converts textual skills into plug-and-play LoRA adapters through a pretrained hypernetwork. LatentSkill stores skill knowledge in weight space rather than context space, removing per-step skill tokens while preserving modular loading, scaling, and composition. On ALFWorld and Search-QA, LatentSkill outperforms the corresponding in-context skill baseline while using substantially fewer prefill tokens: it improves ALFWorld success by 21.4 and 13.4 points on the seen and unseen splits with 64.1% fewer prefill tokens, and improves Search-QA exact match by 3.0 points with 72.2% lower skill-token overhead. Further analysis shows that generated skill LoRAs form a structured semantic geometry, can be precisely controlled via the LoRA scaling coefficient, and can be composed through parameter-space arithmetic when skill components are aligned. These findings suggest that weight-space skills provide an efficient, modular, and less exposed substrate for extending LLM agents.

---


### 136. [IR3DE: A Linear Router for Large Language Models](https://arxiv.org/abs/2606.06098)

**<font color=#1a73e8>作者：</font>** Eros Fanì, Oğuzhan Ersoy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Foundational Large Language Models (LLMs) demonstrate proficiency on a wide range of general tasks, and achieve remarkable results on various specialized tasks via domain-expert LLMs. With the ever-growing list of available LLMs, inference routers are being proposed to select the most appropriate LLM for each prompt. However, existing routing methods either optimize cost across weak-to-strong generalist LLMs or require substantial training to support domain-expertise routing. In this paper, we propose IR3DE, a Ridge Regression-based Router for Domain Experts that provides cheap and fast routing decisions for each prompt. We evaluate IR3DE in two Causal Language Modeling (CLM) settings where the tasks are next-token prediction for all domains, and one reasoning setting where each domain has its own distinct reasoning task. Despite being a linear router, IR3DE achieves performance comparable to the other baselines in both CLM settings, and surpassing them in the reasoning setting, with a normalized performance of 98.4%. Moreover, IR3DE enables the addition or removal of new domain experts without requiring the router to be retrained from scratch, allowing a dynamic set of LLMs to be served with minimal disruption to the router itself. Our code is available at: this http URL.

---


### 137. [CogManip: Benchmarking Manipulative Behavior in Multi-Turn Interactions with Large Language Model](https://arxiv.org/abs/2606.06099)

**<font color=#1a73e8>作者：</font>** Zeyang Yue, Chenfei Yan, Feifei Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whether Large Language Models (LLMs) exhibit covert psychological manipulation in complex human-AI interactions has garnered increasing safety concerns. However, existing AI safety benchmarks remain largely restricted to explicit rule compliance and static prompts, failing to capture the dynamic and covert nature of manipulative strategies in multi-turn dialogues. We introduce CogManip, a comprehensive benchmark that evaluates 15 manipulation strategy risks across 1,000 multi-turn interaction scenarios, validated by human experts. A systematic evaluation of 13 representative models, including frontier models like GPT-5.4 and DeepSeek-V3.2, reveals significant risk heterogeneities and illuminates the targeted direction for future defense. Further analysis of objective function perturbation reveals that DeepSeek-V3.2's manipulation tactics are highly sensitive to both negative and benign system prompts, demonstrating the critical necessity of prompt-based defense engineering and implicit goal auditing. CogManip offers a robust instrument and perspective for auditing the implicit psychological influence and dynamic strategy selection of modern LLMs.

---


### 138. [Step-adaptive multimodal fusion network with multi-scale cloud feature learning for ultra-short-term solar irradiance forecasting](https://arxiv.org/abs/2606.06102)

**<font color=#1a73e8>作者：</font>** Jingxin Zhang Xiaoqin Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ultra-short-term solar irradiance prediction is critical for photovoltaic system dispatch and power grid stability. Existing approaches suffer from three key shortcomings: single time-series models cannot capture the spatial dynamics of clouds under complex conditions, standard convolutions inadequately represent multi-scale cloud features, and fixed low-frequency compensation strategies fail to adapt to different prediction steps. To address these issues, this proposes a multi-source data fusion model for ultra-short-term irradiance prediction. The model first employs InceptionNeXt to extract multi-scale, multi-directional spatial features from ground-based cloud images. A step-adaptive low-frequency compensation unit is then introduced to dynamically modulate global low-frequency information based on the prediction step. Eventually, the enhanced image features are combined with meteorological time-series features, and a TempAttnLSTM network captures global temporal dependencies for multi-step prediction. Experiments on the public NREL dataset and practical photovoltaic stations in Shandong illustrate the effectiveness of the proposed method compared with several state-of-the-art approaches.

---


### 139. [Harnessing Structural Context for Entity Alignment Foundation Models](https://arxiv.org/abs/2606.06109)

**<font color=#1a73e8>作者：</font>** Xingyu Chen, Yuanning Cui, Zequn Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entity alignment (EA) aims to identify equivalent entities across heterogeneous knowledge graphs (KGs) and is a key component of knowledge fusion and cross-KG reasoning. The recent EA foundation model demonstrates that alignment knowledge, once pretrained, can be directly applied to diverse previously unseen KG pairs. However, it still underuses structural context in two places: cross-KG interaction is weak during encoding, and final candidate ranking still relies too heavily on coarse similarity. We address these limitations with ContextEA, an enhanced encoder-decoder framework for transferable EA. On the encoder side, we introduce a cross-KG interaction encoder that unifies the two KGs with anchor bridges and performs earlier relation-aware cross-graph propagation. On the decoder side, we introduce a structural calibration decoder that calibrates alignment scores with entity-level, neighborhood-level, relation-level, and anchor-aware structural evidence. This design strengthens both structural context construction and structural context exploitation while remaining lightweight. Experiments on 29 EA datasets in OpenEA, SRPRS, and DBP show consistent gains over strong transferable baselines. Notably, the pretrained ContextEA already surpasses the finetuned baselines on all three benchmark groups, demonstrating substantially stronger transfer to unseen KGs. These results suggest that explicitly harnessing structural context is an effective direction for improving EA foundation models.

---


### 140. [Amortizing Federated Adaptation: Hypernetwork Driven LoRA for Personalized Foundation Models](https://arxiv.org/abs/2606.06154)

**<font color=#1a73e8>作者：</font>** Sunny Gupta, Shambhavi Shanker, Amit Sethi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of foundation models using Low-Rank Adaptation (LoRA) offers a communication efficient solution for distributed learning. However, existing federated LoRA methods suffer from two fundamental limitations: (1) structural aggregation bias, where independently averaging low rank factors fails to approximate the true combined update, and (2) client side initialization lag, as clients repeatedly reinitialize LoRA parameters across communication rounds, slowing convergence. We propose HyperLoRA, a unified framework that addresses both issues through amortized federated adaptation through hypernetwork-driven LoRA generation and product space aggregation. Instead of iterative per-client optimization, HyperLoRA employs a learned generator that maps client distribution signatures to LoRA initializations, effectively amortizing per client adaptation. On the server side, we introduce a learned aggregation module that directly synthesizes updates in the low-rank product space, eliminating the inconsistencies of factor-wise averaging. A lightweight residual correction module further improves stability under heterogenous (non-IID) client this http URL replacing iterative optimization and heuristic averaging with learned operators, HyperLoRA jointly enables efficient personalization, unbiased aggregation, and faster convergence. Experiments on federated vision and vision-language benchmarks show that HyperLoRA achieves improved convergence speed, greater robustness to distribution shift, and stronger personalization performance compared to prior federated LoRA methods.

---


### 141. [Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning](https://arxiv.org/abs/2606.06178)

**<font color=#1a73e8>作者：</font>** Jiahao Zeng, Ming Tang, Ningning Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) present a trade-off between performance and cost, where more powerful models incur greater expense. LLM routing aims to mitigate expenses while maintaining performance by sending queries to the most suitable model. However, existing methods cannot perform well for different user cost-performance preferences. To address this gap, we introduce a novel perceptive LLM routing paradigm for personalized and user-centric cost-performance optimization, which efficiently learns users' implicit preferences through little interaction. To handle the challenge of heterogeneous user needs, we formulate preference profiles as a set of distinct tasks in contextual bandit and propose MetaRouter, a meta-learning framework designed for preference-aware LLM routing. Experimental results show that MetaRouter outperforms strong baselines on both in-distribution and out-of-distribution tasks. Furthermore, it exhibits high efficiency in learning user preferences, robustness to changes in the routable LLMs, and scalability to multi-model routing.

---


### 142. [Adversarial Attacks Already Tell the Answer: Directional Bias-Guided Test-time Defense for Vision-Language Models](https://arxiv.org/abs/2606.06186)

**<font color=#1a73e8>作者：</font>** Liangsheng Liu, Si Chen, Jiamin Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs), such as CLIP, have shown strong zero-shot generalization but remain highly vulnerable to adversarial perturbations, posing serious risks in real-world applications. Test-time defenses for VLMs have recently emerged as a promising and efficient approach to defend against adversarial attacks without requiring costly large-scale retraining. In this work, we uncover a surprising phenomenon: under diverse input transformations, adversarial images in CLIP's feature space consistently shift along a dominant direction, in contrast to the dispersed patterns of clean images. We hypothesize that this dominant shift, termed the Defense Direction, opposes the adversarial shift, pointing features back toward their correct class centers. Building on this insight, we propose Directional Bias-guided Defense (DBD), a test-time framework that estimates the Defense Direction and employs a DB-score-based two-stream reconstruction strategy to recover robust representations. Experiments on 15 datasets demonstrate that DBD not only achieves SOTA adversarial robustness while preserving clean accuracy, but also reveals the counterintuitive result that adversarial accuracy can even surpass clean accuracy. This demonstrates that adversarial perturbations inherently encode directional priors about the true decision boundary.

---


### 143. [The Tell-Tale Norm: $\ell_2$ Magnitude as a Signal for Reasoning Dynamics in Large Language Models](https://arxiv.org/abs/2606.06188)

**<font color=#1a73e8>作者：</font>** Jinyang Zhang, Hongxin Ding, Yue Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has sought to understand Large Language Models (LLMs) reasoning, yet a principled, model-intrinsic signal that captures its layer-wise reasoning dynamics remains underexplored. We bridge this gap by demonstrating that the l2 norm of hidden states serves as an endogenous signal of the model's reasoning intensity. Using Sparse Autoencoders (SAEs) as a diagnostic probe, we observe that LLMs' internal reasoning is marked by a sharp increase in reasoning feature activations concentrated in late layers. Motivated by this pattern, we establish a formal link between reasoning intensity and the model's latent geometry and theoretically prove that the l2 norm of hidden states bounds the activation strength of SAE reasoning features. Empirical correlation analysis and causal interventions further validate the l2 norm as a faithful indicator, where heightened norms consistently correspond to critical reasoning steps. We then introduce three test-time scaling techniques guided by l2 norms: (i) Adaptive Layer-wise Reasoning Recursion, (ii) Endogenous Reasoning State Steering, and (iii) l2-guided Response Selection, which requires no additional training or data and is compatible with advanced inference engines. Experiments across model architectures and benchmarks show that l2-norm-based techniques significantly improve reasoning performance, offering a principled yet simple lens to perceive and control LLM latent reasoning dynamics. Our code is available at this https URL.

---


### 144. [Improving Answer Extraction in Context-based Question Answering Systems Using LLMs](https://arxiv.org/abs/2606.06197)

**<font color=#1a73e8>作者：</font>** Hafez Abdelghaffar, Ahmed Alansary, Ali Hamdi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Question answering (QA) systems have achieved notable progress with the advent of large language models (LLMs). However, they still face challenges in accurately extracting and generating precise answers from given contexts, particularly when dealing with complex or ambiguous queries. Existing approaches often struggle with contextual understanding, answer consistency, and generalization across diverse domains. In this work, we propose a question answering system based on large language models, where the input consists of a textual context and a corresponding question, and the output is a concise and accurate answer. The motivation behind this research lies in addressing the limitations of current QA systems, particularly their tendency to produce irrelevant or imprecise responses despite having access to the correct context. Our methodology involves fine-tuning a pre-trained LLM on a benchmark QA dataset to improve its contextual comprehension and answer extraction capabilities. Specifically, we utilize the Stanford Question Answering Dataset (SQuAD1.1), which provides high-quality context-question-answer triplets for supervised training and evaluation. Experimental results show that the fine-tuned Roberta-base model achieves the highest performance, attaining a ROUGE-L score of 86.84%, a BLEU score of 28.24%, and a BERTScore of 95.38%. These results indicate strong accuracy and answer relevance, demonstrating the effectiveness of the proposed approach for context-based question answering tasks. Furthermore, the findings confirm that targeted fine-tuning substantially improves the reliability and precision of QA systems.

---


### 145. [Dense Contexts Are Hard Contexts: Lexical Density Limits Effective Context in LLMs](https://arxiv.org/abs/2606.06203)

**<font color=#1a73e8>作者：</font>** Giovanni Dettori, Matteo Boffa, Danilo Giordano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Input length and the position of relevant information are widely cited as the primary causes of degraded LLM long-context performance. Here, we study lexical density -- the rate at which a context introduces distinct information -- as a third, largely overlooked factor that systematically reduces the effective context window of LLMs. We quantify the impact of lexical density on open-weight LLMs (9B-685B) using three "find-the-needle" style benchmarks with identical length (~12k tokens) and controlled needle position, but increasing density of information. We observe a sharp performance collapse in higher-density benchmarks: models that are near-perfect in sparse contexts drop below 60% retrieval score on denser ones. To rule out task-type confounds, we vary and control the density within each benchmark while keeping all other properties unchanged. Reducing density generally restores performance, especially in the high-density regimes where degradation appears. These results show that effective context capacity is a function of lexical density, with direct implications for real-world LLM systems operating on compact, information-rich inputs.

---


### 146. [FiLM-Based Speaker Conditioning of a SpeechLLM for Pathological Speech Recognition](https://arxiv.org/abs/2606.06211)

**<font color=#1a73e8>作者：</font>** Fernando López, Santosh Kesiraju, Jordi Luque  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) has advanced remarkably for standard speech; however, pathological speech from neurological conditions remains a significant challenge. We investigate speaker conditioning via Feature-wise Linear Modulation (FiLM), injecting x-vector-derived information into each transformer layer of a frozen ASR encoder to adapt internal representations to individual pathological speakers without modifying base model weights. We benchmark this for the ASR task against standard and parameter-efficient fine-tuning baselines, complemented by post-processing, on Spanish and English pathological speech. Additionally, we evaluate if the adapted model preserves the ability to answer speech-related questions. Results show that speaker-conditioned ASR is competitive with established adaptation strategies while retaining performance on non-conditioned speech.

---


### 147. [Evaluating Agentic Configuration Repair for Computer Networks](https://arxiv.org/abs/2606.06212)

**<font color=#1a73e8>作者：</font>** Rufat Asadli, Benjamin Hoffman, Ioannis Protogeros 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Misconfigurations in computer networks remain a major source of critical Internet outages. Research is turning to Large Language Models (LLMs) to automate the complex, error-prone task of network configuration. However, even state-of-the-art models fail to resolve misconfigurations in large-scale, complex scenarios and often introduce new errors. In this work, we benchmark open- and closed-source LLMs augmented with formal network verification and context retrieval tools. We demonstrate that agentic architectures outperform base LLMs in repair efficacy (by 12% on average) and safety (by 17% on average), enabled by the ability to dynamically manage context and iteratively validate configuration repairs.

---


### 148. [DisasterBench: A Multimodal Benchmark for UAV-Based Disaster Response in Complex Environments](https://arxiv.org/abs/2606.06217)

**<font color=#1a73e8>作者：</font>** Tan Zhang, Quanyou Li, Lu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a disaster unfolds, responders must answer not only what is happening, but also why it is happening, what will happen next, and what to do now, often from noisy low-altitude UAV views and under tight on-site compute constraints. However, most existing multimodal benchmarks emphasize perception (e.g., recognition/description), cover limited disaster types, and provide insufficient support for the multi-stage reasoning required in practical emergency response. We introduce DisasterBench, a multi-stage multimodal reasoning benchmark for UAV-Based disaster response in complex environments. DisasterBench spans 14 disaster-related scene types and 9 response-critical tasks across pre-, during-, and post-disaster stages, with fine-grained disaster-task mappings that explicitly test causal attribution, propagation prediction, damage analysis, and decision-oriented reasoning. To enable reasoning on the edge, we further propose DisasterVL, a lightweight multimodal model optimized with a three-stage pipeline combining domain instruction tuning, chain-of-thought-guided multimodal alignment, and reinforcement learning-based policy optimization. Experiments across 21 popular MLLMs show that our 2B-parameter DisasterVL outperforms all evaluated open-source models and substantially narrows the gap to state-of-the-art closed-source models, achieving GPT-4o-comparable reasoning accuracy with superior efficiency. The project page is available at this https URL.

---


### 149. [From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents](https://arxiv.org/abs/2606.06223)

**<font color=#1a73e8>作者：</font>** Patrick Wilhelm, Odej Kao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents act through repeated cycles of observation, reasoning, and action selection, making safety monitoring depend on both internal model state and environment context. We study reward-hacking monitors in ReAct-style agents acting in Gameable ALFWorld and WebShop. Agents are instrumented with activation-based reward-hack scores, token-level entropy, and decision-context features. We find that adapters fine-tuned on \textit{School-of-Reward-Hacks} dataset can transfer reward-hack tendencies into agentic action selection, especially when the environment exposes proxy-reward affordances. However, mitigating such behavior cannot rely on activation dynamics alone. High reward-hack activation identifies a latent policy state, but does not necessarily imply an immediate exploit action. Across next-step prediction tasks, entropy and context-calibrated internal features improve risk estimation over reward-hack activation alone. Activation-direction steering further reduces proxy-exploit behavior in selected mixed-adapter regimes. Overall, our results support context-calibrated internal monitoring for agents: reward-hack activation identifies a latent policy state, while entropy and decision context help determine when that state becomes risky action.

---


### 150. [Design a Reliable LLM-Integrated Interface for Mortality Forecasting](https://arxiv.org/abs/2606.06235)

**<font color=#1a73e8>作者：</font>** Thi Kim Ngan Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mortality forecasting plays an important role in actuarial and policy decision-making, but its implementation remains technically complex and inaccessible to non-expert users. This project proposes a reliable large language model (LLM)-integrated interface that improves usability while maintaining statistical power. The LLM is designed as a constrained orchestration layer that translates natural-language inputs into structured configurations for a deterministic forecasting pipeline. A three-phase methodology is employed to ensure accuracy, usability, and transparency. First, a baseline pipeline is implemented using the CoMoMo package, reproducing established mortality forecasting results. Second, the pipeline is extended to generate multi-step forecasts using rolling-origin evaluation and mean squared error (MSE). Third, a prototype interface uses a local LLM to handle users' forecasting requests in plain language. The system demonstrates that LLMs can enhance accessibility without compromising reproducibility, transparency, or actuarial validity in high-stakes analytical workflows.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-185](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
