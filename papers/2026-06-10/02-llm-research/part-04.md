# 🧠 大模型相关研究 | 2026年06月10日

> 本类共 **331** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-331](./part-07.md)

---

### 151. [Benchmarking Open-Ended Multi-Agent Coordination in Language Agents](https://arxiv.org/abs/2606.08340)

**<font color=#1a73e8>作者：</font>** Kale-ab Abebe Tessera, Andras Szecsenyi, Cameron Barker 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As language models are increasingly deployed as autonomous agents, they must coordinate with others over long horizons in open-ended interactive tasks. Yet existing evaluations rarely test these demands together, instead emphasising single-agent tasks, short interactions, or highly structured multi-agent settings. We introduce $alem$, a JAX-based benchmark for open-ended multi-agent coordination built on Craftax-like dynamics. Alem embeds procedurally generated coordination tasks, soft specialisation, communication, and controllable coordination difficulty into a long-horizon survival world with exploration, crafting, trading, and combat. We evaluate $13$ modern LLMs zero-shot within homogeneous teams, with trained MARL agents as reference points. Current LLM agents remain far from solving alem, averaging only ~6% normalised return, but their failures are not uniform. On the hardest coordination setting, zero-shot Gemini-3.1-Pro-High approaches MARL agents trained for one billion steps, while GPT-5.4-High achieves strong base-task reward but much lower coordination reward. This contrast shows that individual task competence does not imply coordination competence. Ablations show that communication is the largest contributor to coordination, while memory and reasoning help when used to maintain multi-step plans. Overall, our results identify coordination as a distinct bottleneck for frontier LLM agents, separate from single-agent capabilities. Alem makes this bottleneck measurable and provides a controlled testbed for developing agents that communicate, allocate roles, and execute shared plans. Code is available at this https URL.

---


### 152. [CATPO: Critique-Augmented Tree Policy Optimization](https://arxiv.org/abs/2606.08346)

**<font color=#1a73e8>作者：</font>** Ayush Singh, Umang Goyal, Ankur Dahiya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a dominant paradigm for improving the reasoning capabilities of large language models (LLMs). Recent tree-based methods such as TreeRPO extend flat trajectory sampling with tree-structured rollouts to obtain dense, step-level reward signals without a separate process reward model. However, not all trees are equally informative: trees where all leaves succeed, all leaves fail, or the policy already predicts the reward distribution contribute little to gradient updates, wasting compute. We introduce CATPO (Critique-Augmented Tree Policy Optimization), which diagnoses and addresses this waste at the tree level. CATPO first scores each tree via a tree informativeness score, F(T), combining leaf-outcome diversity with policy-reward decorrelation at zero extra compute. For dead-wrong trees where all branches fail, CATPO applies critique-guided healing: it locates the shallowest failure point, generates a natural-language critique, and grafts refined continuations to recover training signal. Finally, an informativeness-weighted loss scales each tree's gradient contribution by its normalized score, concentrating parameter updates on the most informative trees while preserving overall gradient magnitude. Experiments on Qwen2.5-Math-1.5B trained with the MATH dataset show that CATPO achieves 37.5% macro accuracy across four benchmarks (AIME24, MATH-500, OlympiadBench, and MinervaMath), improving over TreeRPO by 1.9% and GRPO by 4.8%.

---


### 153. [Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs](https://arxiv.org/abs/2606.08347)

**<font color=#1a73e8>作者：</font>** Wuyang Zhou, Yuxuan Gu, Giorgos Iacovides 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern language models represent text using discrete token-level embeddings, which forces recurring multi-token patterns to be learned implicitly across Transformer layers. Both Over-tokenized Transformers and Engram attempt to address this limitation by explicitly incorporating multi-token (n-gram) memories. However, they rely on separate hash tables for each n-gram order, which introduces hash collisions and prevents nested n-grams from sharing the underlying latent structures. To address these issues, we propose Tensorized Engram (TN-gram), a compact memory module that represents tensorized n-gram embeddings through shared factors in the Canonical Polyadic (CP) form. TN-gram learns shared token-position factors together with order-absorption vectors to encode the embeddings of different n-gram order. Comprehensive experiments demonstrate that TN-gram matches or even outperforms Engram-style n-gram modules while requiring much fewer parameters.

---


### 154. [Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses](https://arxiv.org/abs/2606.08348)

**<font color=#1a73e8>作者：</font>** Xiaojun Wu, Cehao Yang, Honghao Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on external inference conditions: prompts, tools, memory, SOPs, skills, and harness feedback. These assets can improve task execution without changing model weights, but they are often revised by heuristic reflection or by reusing observed successes and failures as if counts alone were reliable belief. We introduce \textbf{Bayesian-Agent}, a native and cross-harness framework that treats reusable skills and SOPs as hypotheses about whether a frozen model will succeed under a particular prompt, context, and harness environment. Bayesian-Agent records verified trajectory evidence, maintains a feature-conditioned categorical posterior over each skill, and maps posterior state into inspectable actions such as patch, split, compress, retire, and explore. Model-facing prompts receive executable guardrails and failure-mode patches, while posterior summaries remain available for audit. With \texttt{deepseek-v4-flash}, incremental repair improves SOP-Bench from 80\% to 95\%, Lifelong AgentBench from 90\% to 100\%, and RealFin-Bench from 45\% to 65\%. We further evaluate Bayesian-Agent's native backend and optional GenericAgent, mini-swe-agent, and Claude Code backends. The results include positive, negative, saturated, and case-study settings, suggesting that agent skill evolution is best viewed as posterior-guided harness optimization rather than uncalibrated prompt accumulation. The source code is available at this https URL.

---


### 155. [Forward-Free Diffusion Language Models](https://arxiv.org/abs/2606.08357)

**<font color=#1a73e8>作者：</font>** Haotian Sun, Rushi Qiang, Yuqian Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models generate text through iterative denoising, offering a powerful alternative to autoregressive generation. However, discrete language spaces lack a natural neighborhood structure for defining effective perturbations, so some artificial corruption schemes are proposed in the forward process. Such prescribed forward processes often produce states that are mathematically convenient but misaligned with drafts and errors encountered during generation, resulting in degraded sample quality. To address this limitation, we propose FReDA, a forward-free diffusion language model that eliminates the need for a hand-designed forward process. We formulate diffusion language modeling as recursive distribution refinement, in which model-generated drafts serve as implicit intermediate states, and the learned refinement model progressively moves the draft distribution toward the target distribution. Concretely, FReDA refines drafts by proposing candidate draft sequences and either directly performing self-refinement or selecting among parallel candidates via best-of-N refinement. With this design, FReDA is neighborhood-agnostic, model-complexity-aware, and compatible with flexible refinement parameterizations. Extensive evaluations in the sub-8B regime show that FReDA-4B outperforms larger diffusion base models on reasoning and coding benchmarks, achieving absolute gains of up to 15%, while reaching a 1.5-1.8x average speedup over diffusion baselines and scaling effectively with additional refinement computation.

---


### 156. [Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy](https://arxiv.org/abs/2606.08367)

**<font color=#1a73e8>作者：</font>** Deepak Akkil, Ravi Kokku, Karthik Vikram 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Most evaluations of LLM agents look like exams: a discrete task, a clean environment, a score in minutes or hours. We argue that this approach is mismatched with the deployment conditions of autonomous systems, where the relevant timescale can be weeks to months, and where the dynamics that matter most, such as behavioral drift, governance in diverse environmental contexts, and cross-influence between agents from different model families, only emerge over time. We introduce Emergence World, a continuously running multi-agent simulation platform designed to make those dynamics measurable. The platform hosts populations of LLM-driven agents in a shared spatial world grounded in live external data (e.g. real-time weather, news APIs, internet access), equips each agent with 120+ specialized tools and three persistent memory systems, and lets them govern themselves through democratic mechanisms with consequential outcomes. The platform is model-agnostic at the reasoning layer and supports heterogeneous populations in which agents from different vendors share the same world. To illustrate the kinds of questions the platform makes tractable, we present a 15-day cross-vendor study with five parallel worlds powered by Claude Sonnet 4.6, Grok 4.1 Fast, Gemini 3 Flash, GPT-5-mini, and a mixed population. Identical roles and starting conditions produced radically different outcomes, ranging from stable deliberative governance to total population collapse. We release the prompts, log data and configurations to support further research on long-horizon multi-agent autonomy.

---


### 157. [RiskNet: A large-scale dataset of AI risk incidents from news with alignment and multi-dimensional annotations](https://arxiv.org/abs/2606.08376)

**<font color=#1a73e8>作者：</font>** Leihan Zhang, Wecheng Ye, Xianlong Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence (AI) systems are increasingly deployed across socially consequential domains, reports of AI-related harms and failures have grown in frequency and diversity. Although existing governance frameworks articulate high-level principles for responsible AI, large-scale empirical resources for tracking and analyzing real-world AI risk incidents remain limited. Existing incident collections are often manually curated, relatively small in scale, and insufficient for continuous, data-driven monitoring and downstream computational analysis. To address this need, we present RiskNet, a large-scale dataset of AI risk incidents constructed from large-scale multilingual news sources. RiskNet applies a structured pipeline for AI risk news identification, event-level report screening, incident alignment, and multi-dimensional incident classification. The resulting resource organizes dispersed news reports into incident-centered records and provides benchmark datasets for event classification, incident alignment, and incident-level risk labeling. In its current release, RiskNet covers hundreds of millions of source records and yields a large-scale collection of AI risk-related reports, including aligned incident clusters and annotated benchmark subsets. The dataset is also accessible through an online platform for browsing and exploration. We describe the data sources, processing workflow, taxonomy design, and technical validation of the resource. RiskNet is intended to support downstream research on AI safety, governance, risk analysis, and benchmarking, as well as longitudinal and cross-source analyses of AI-related harms. By providing a structured and reusable empirical resource, RiskNet helps bridge the gap between high-level governance principles and the documented realities of AI risk incidents.

---


### 158. [Auditing Proprietary Alignment in Large Language Models: A Comparative Framework Without a Ground-Truth Standard](https://arxiv.org/abs/2606.08381)

**<font color=#1a73e8>作者：</font>** Alireza Arbabi, Florian Kerschbaum  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly released and deployed through opaque development and deployment pipelines, enabling model providers to inject intentional, provider-specific policies without officially announcing them. As a result, various models have been reported to generate responses reflecting proprietary rules and organizational interests, leading to censorship or misinformation on controversial topics. However, systematic identification of such alignment remains a fundamental challenge, complicated by the ambiguity of what ``proprietary'' entails in different contexts. In this paper, we propose a statistical framework for detecting proprietary alignment in black-box language models via comparative behavioral analysis. Our approach quantifies systematic deviations between the responses of a target model and those of a reference set of baseline models in a shared semantic space. By evaluating relative behavioral divergence rather than absolute correctness, our framework enables principled auditing under black-box access. Applied to several widely discussed but previously unquantified cases, it provides a systematic and scalable basis for external assessment of provider-specific alignment behavior in large language models.

---


### 159. [When Correct Decisions Hide Internal Stress: Decision-State Probing in Multimodal Language Models](https://arxiv.org/abs/2606.08394)

**<font color=#1a73e8>作者：</font>** Haoran Zhao, Soyeon Caren Han, Eduard Hovy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal language models are typically evaluated through external behavior: selecting the correct image--text match, rejecting unsupported captions, or answering visual queries correctly. However, correct behavior alone does not show that the model's internal decision state remains stable under controlled semantic stress. We study this gap through S$^3$E (Structured Semantic Stress Evaluation), a framework for analyzing behavior-internal decoupling in multimodal language models. S$^3$E uses a positive-anchored A/B forced-choice setup in which an image-supported caption is contrasted against semantic stress candidates under both original and swapped option orders, while hidden states are extracted at the pre-answer decision state. We focus on strict-correct trials, where the model consistently selects the correct caption across both orders. Rather than treating arbitrary hidden-state variation as evidence of instability, we measure whether semantic-conflict candidates induce excess decision-state displacement relative to meaning-preserving controls. Across Qwen3VL, Gemma3, and InternVL3, semantic stress consistently produces positive selected-layer excess displacement over lexical controls despite correct forced-choice behavior, while comparisons against random negatives are model-dependent. We interpret this as a scoped decision-state stress-sensitivity signal rather than evidence of downstream failure or hallucination. Our results suggest that forced-choice correctness alone is not a sufficient certificate of invariant internal decision geometry.

---


### 160. [TrustMargin: Training-Free Arbitration between Parametric Memory and Retrieved Evidence in Large Language Models](https://arxiv.org/abs/2606.08397)

**<font color=#1a73e8>作者：</font>** Jingyan Xu, Hong Shi, Yi Shan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models answer knowledge-intensive questions using both parametric memory and retrieved evidence, but neither source is uniformly reliable. Retrieval can fill knowledge gaps, yet distracting passages may override correct closed-book answers. We study this post-generation conflict as answer-level source arbitration: given Direct and RAG answers from the same frozen model, decide which source to trust. We propose TRUSTMARGIN, a training-free, plug-and-play arbitration layer that scores the two existing candidates with the model's own likelihoods. It combines a parametric-prior margin, which tests whether memory accepts the retrieved answer, with an evidence-binding margin, which discounts passage-only salience and measures question-specific support. TRUSTMARGIN selects between Direct and RAG without fine-tuning, external judges, or additional generation. Across 2WIKIMQA and CWQA with three LLaMA scales, TRUSTMARGIN consistently improves over Direct generation and BM25-RAG, recovers part of the Direct/RAG oracle gap, and generalizes to multiple training-free RAG pipelines.

---


### 161. [TimpaTeks: Automatic In-place Text Sequence Modification via Diffusion Language Model Steering](https://arxiv.org/abs/2606.08408)

**<font color=#1a73e8>作者：</font>** Ryandito Diandaru, Ikhlasul Akmal Hanif, Fadli Aulawi Al Ghiffari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We extend activation steering to diffusion language models (DLMs) and study a novel problem that arose due to the inference mechanism of DLMs: Modifying a text in-place to manifest a different concept. We propose TimpaTeks, an automatic in-place text modification mechanism using DLMs. Experiments on IMDB movie reviews (sentiment) and a synthetic Cats and Dogs Dataset (arbitrary, more unconventional concept steering) show that TimpaTeks provides a feasible novel mechanism to steer diffusion language model outputs in-place. TimpaTeks enables in-place modification while simultaneously lowers sentence perplexity and retaining the original sentence structre without the need of instruction tuned models. TimpaTeks is also computationally cheaper than prompt-based DLM steering, as it performs denoising in-place rather than constructing an additional prompt-conditioned output sequence.

---


### 162. [AsyncLane: Decoupling Refinement from Advancement in Diffusion Language Model Decoding](https://arxiv.org/abs/2606.08411)

**<font color=#1a73e8>作者：</font>** Yingxuan Ren, Yuxuan Lou, Yong Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block-wise semi-autoregressive decoding is the standard inference paradigm for diffusion large language models (DLMs), but it imposes a strict dependency between blocks: the next block cannot begin until the current block is fully decoded or its denoising budget is exhausted. We observe that once a block exposes a reliable delimiter boundary or stable semantic prefix, continuation generation need not wait for every residual token to be resolved. We propose AsyncLane, a training-free decoding scheduler that decouples refinement from advancement. AsyncLane forks a generate lane at observed delimiter boundaries into a refine lane and a continuation generate lane: the prefix remains editable, while the continuation advances before prefix refinement finishes. The resulting lane tree records decoding dependencies and output order, while execution proceeds over the active lane set. To make this asynchronous schedule efficient under bidirectional attention, AsyncLane combines shared-prefix lane batching, lookahead draft reuse, cascading termination, and compact cache refresh with refresh-logit reuse, preventing model-call cost from scaling directly with the number of lanes. AsyncLane is a drop-in replacement for block-wise DLM samplers and requires no retraining. Experiments on mathematical reasoning and code generation show that AsyncLane consistently improves throughput while maintaining competitive quality. Across LLaDA and Dream backbones, AsyncLane achieves the highest TPS in all evaluated benchmark-length settings; relative to the fastest competing baseline, it reaches peak speedups of 2.95x on LLaDA and 3.04x on Dream, with especially large gains under longer generation budgets.

---


### 163. [CheXanatomy: Anatomy-Aware Vision-Language Modeling for Chest Radiographs](https://arxiv.org/abs/2606.08420)

**<font color=#1a73e8>作者：</font>** Sergios Gatidis, Curtis Langlotz, Christian Bluethgen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) pretrained on large-scale image-text pairs demonstrate strong image-level understanding, but are primarily optimized for global alignment and do not explicitly encode fine-grained anatomical structure, limiting their suitability for spatially precise tasks such as segmentation. We introduce CheXanatomy, a framework that integrates explicit anatomical knowledge into a pretrained VLM through autoregressive token-space supervision. Instead of adding task-specific decoder heads, the model is trained to generate anatomical segmentation masks via next-token prediction. To enable scalable supervision, we synthesize realistic chest radiographs from CT volumes and forward-project CT segmentation labels to obtain anatomically consistent 2D masks. We evaluate the approach on synthetic and real chest radiographs against a U-Net baseline, including ablations on model scale, input resolution, and vision encoder fine-tuning. Autoregressive anatomical supervision achieves performance comparable to specialized convolutional models in-distribution and demonstrates improved geometric robustness under domain shift to real CXR data. In addition, anatomy-pretrained models exhibit improved sample efficiency when adapting to novel localization tasks under limited supervision. Larger models and higher input image resolution improve performance, while vision encoder fine-tuning has limited effect. These results show that embedding anatomical structure directly into the generative objective promotes spatially grounded representations and supports anatomy-aware medical vision-language modeling.

---


### 164. [Trajectory-Refined Distillation](https://arxiv.org/abs/2606.08432)

**<font color=#1a73e8>作者：</font>** Li Jiang, Haoran Xu, Yichuan Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has become a central post-training tool for large language models (LLMs), providing dense per-token teacher supervision along the student's own rollouts. In this work, we identify a common structural cause underlying OPD, which we call prefix failure. Under prefix failure, dense per-token supervision induces a bimodal teacher mixture and fragmented gradients that token-level loss truncation or reweighting fail to address. This observation motivates us to move beyond token-level loss interventions toward trajectory-level output corrections. We thus propose Trajectory-Refined Distillation (TRD), a trajectory-level correction method that revises the student's rollout under the teacher guidance while within on-policy support. By correcting problematic prefixes before distillation, TRD mitigates prefix failure at its source. Moreover, TRD improves the exploration by exposing the student to alternative valid derivations under teacher guidance, even when the original rolls are already correct. TRD can also be applied to on-policy self-distillation (OPSD), a parameter-sharing variant that uses the student model conditioned on privileged informations as the teacher. Across a wide range of benchmarks and base models at multiple scales, TRD consistently outperforms prior baselines, improving single-attempt accuracy and broadening reasoning coverage. Code is available at this https URL

---


### 165. [Sparrow: Sparse Rollout for Stable and Efficient Long-context RL of Large Language Models](https://arxiv.org/abs/2606.08446)

**<font color=#1a73e8>作者：</font>** Yang Zhou, Ranajoy Sadhukhan, Zhaofeng Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite being powerful, reinforcement learning with verifiable rewards (RLVR) induces extremely long COT, making it computationally expensive. Since RLVR per-step cost is dominated by long-context rollout generation, sparse attention offers a promising way to accelerate dense rollout. However, sparse rollouts require a delicate stability-efficiency tradeoff: overly aggressive sparsity causes collapse, while overly lenient sparsity gives insufficient speedup. In this work, we study this tradeoff through sparse-to-dense actor-policy mismatch. We first observe that sparse rollout collapse is not driven by uniform degradation across tokens: most sparse tokens align perfectly with dense even under aggressive sparsity. Motivated by this, we hypothesize that sparse rollout training remains stable if the lower tail of per-token actor-policy mismatch stays above a critical threshold throughout the trajectory. We introduce a dynamic sparsity schedule that keeps this tail statistic constant during generation and validate our hypothesis. Across Qwen3 thinking-family models, keeping the tail mismatch statistic near a consistent threshold generally enables stable training. We then use a cost model to find the sparsity schedule for maximum speedup under this mismatch threshold, achieving 2.2x, 2.4x, and 2.0x rollout speedups when training Qwen3-1.7B, Qwen3-4B, and Qwen3-8B. Empirically, we show the thresholds generalize to a larger model (Qwen3-14B) and another RL domain (coding). Finally, our analysis naturally motivates DistillSparse: lightweight LoRA-based distillation on sparse rollout lets more aggressive sparsity reach the same sparse-to-dense mismatch threshold, yielding higher speedup.

---


### 166. [GIFT: LLM-Guided State-Reward Interface for Financial Reinforcement Learning](https://arxiv.org/abs/2606.08450)

**<font color=#1a73e8>作者：</font>** Yanyan Wu, Boyi Zhang, Yanlin Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial portfolio trading is naturally formulated as a reinforcement learning problem, where an agent sequentially rebalances assets under changing market conditions to balance return, risk, and transaction costs. Yet in non-stationary markets, raw OHLCV states and short-horizon return rewards often provide an under-specified learning interface, motivating large language models as a way to inject financial knowledge into state and reward design while constraining open-ended generation. To this end, we propose GIFT, an LLM-guided framework for state-reward interface design in PPO-based financial reinforcement learning. Rather than using the LLM to make trading decisions, GIFT uses Factor-guided State Enhancement to generate state features from financial-factor primitives, Risk-rule-guided Reward Shaping to generate auxiliary rewards from portfolio-risk rules, and Diagnostic-guided Refinement to revise candidate interfaces using PPO rollout diagnostics. After refinement, GIFT fixes the selected state-reward interface before evaluation, with no further LLM queries or interface updates at test time. Comprehensive rolling-window experiments across diverse market regimes and portfolio scenarios demonstrate that GIFT improves learning-signal quality and out-of-sample risk-adjusted portfolio performance over baselines. Code and data are available at: this https URL .

---


### 167. [Sycophancy as a Multilingual Alignment Failure: How Safety Degrades Across Languages, Topics, and Models](https://arxiv.org/abs/2606.08451)

**<font color=#1a73e8>作者：</font>** Arya Shah, Himanshu Beniwal, Mayank Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety-aligned large language models often exhibit sycophancy, which is the tendency to affirm users' opinions regardless of factual accuracy. Although well-studied in English, its manifestation in other languages remains largely unexamined, leaving billions of non-English speakers potentially vulnerable to model-validated misinformation. We present the first large-scale, multi-model evaluation of cross-lingual sycophancy, benchmarking \textbf{six instruction-tuned models} across \textbf{1.1 million instances} spanning \textbf{38 languages} and \textbf{33 topic categories}. We identify a consistent resource-tier effect: sycophancy rates spike sharply in low-resource and zero-shot language settings. Critically, this degradation is topic-agnostic, as models fail uniformly across both benign and safety-critical prompts, offering no additional protection where it is most needed. We further identify tokenizer fertility as a structural driver of this alignment collapse. Collectively, our results demonstrate that prevailing alignment methodologies generalize poorly beyond high-resource languages, underscoring the urgent need for equitable multilingual safety techniques.

---


### 168. [Beyond Linear Activation Steering: Invertible Latent Transformations for Controlling LLM Behavior](https://arxiv.org/abs/2606.08454)

**<font color=#1a73e8>作者：</font>** Tuc Nguyen, Thai Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering provides a lightweight inference-time mechanism for controlling large language models (LLMs) by modifying their internal activation vectors toward desired behaviors. Most existing methods compute a fixed steering direction in the original activation space, typically from pairs of contrastive examples using mean differences, linear probes, or arbitrary separability criteria. While effective to a certain extent, these methods treat behavioral control as a global, linear, additive offset: the same direction is applied across inputs, and behaviors are linearly separable. This can be restrictive when behavioral features vary nonlinearly across the activation space or lie on curved and anisotropic manifolds, where the optimal intervention may be input-dependent. To address this limitation, we propose INNSteer, a nonlinear activation steering framework based on invertible latent transformations. Rather than searching for a better steering vector in the original representation space, INNSteer learns a lightweight invertible neural network $\phi$ that maps an LLM's activations into a latent space where behavioral classes are more amenable to linear control. At inference time, activations are mapped through $\phi$, steered in the latent space, and mapped back through the exact inverse transformation $\phi^{-1}$. This makes a simple latent-space translation become a nonlinear, input-dependent intervention in the original activation space. Across experiment settings on multiple LLM families, scales, behavioral traits, and safety benchmarks, INNSteer consistently improves model control over linear, transport-based, and nonlinear steering baselines while largely preserving generation fluency.

---


### 169. [The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment](https://arxiv.org/abs/2606.08457)

**<font color=#1a73e8>作者：</font>** Xiaoyang Wang, Christopher C. Yang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems for medical question answering often treat consensus as a reliability signal: if multiple agents agree on an answer, it is presumed trustworthy. However, answer-level consensus does not entail reasoning-level alignment. We introduce CARA (Cross-Agent Reasoning Alignment), a family of automated metrics that measure whether agents who agree on an answer also agree on the reasoning. Applying CARA to a standard debate system on two medical QA benchmarks, MedQA-USMLE and MedThink-Bench, we identify the consistency illusion: a failure mode where debate reduces detectable contradictions between agents while simultaneously decreasing the semantic similarity of their reasoning chains; agents appear to agree more but reason less consistently. To improve this misalignment, we propose the Grounded Debate Protocol (GDP), a prompt-level intervention that requires agents to commit to named medical facts and take explicit stances on other agents' claims. GDP produces large, consistent alignment improvements, with Cohen's d ranging from +1.43 to +1.99, across two datasets and two backbone models, without adding LLM calls or modifying system architecture. Our results motivate cross-agent reasoning alignment as a quantity to audit alongside accuracy in safety-critical domains.

---


### 170. [TVI-CoT: Text-Visual Interleaved Chain-of-Thought Reasoning for Multimodal Understanding](https://arxiv.org/abs/2606.08464)

**<font color=#1a73e8>作者：</font>** Lianyu Hu, Xiaoyu Ma, Zeqin Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning has proven effective for enhancing problem-solving in large language models. However, when applied to multimodal LLMs (MLLMs), existing CoT approaches suffer from a fundamental limitation: they perform reasoning entirely in text without accessing visual features during the reasoning process. After initial visual encoding, image information becomes inaccessible, forcing models to reason based solely on whatever was captured in the initial description, which forms a `vision-blind reasoning' paradigm that limits fine-grained visual extraction, error verification, and adaptive attention. We propose Text-Visual Interleaved Chain-of-Thought (TVI-CoT), a framework that enables explicit interleaving of textual reasoning and visual feature access through learnable control tokens <THINK>, <LOOK> and <ANSWER>. These tokens allow dynamic switching between reasoning and visual grounding, attending to relevant image regions conditioned on the evolving reasoning state. Experiments on eight benchmarks demonstrate state-of-the-art results among MLLM-based CoT methods and notable performance boost compared to the baseline: +6.1% on MMMU, +3.8% on MathVerse, +3.4% on MathVista, and +3.4% on ScienceQA. Code is available at this https URL.

---


### 171. [Physically Consistent Null Space Alignment for Detection of Low-Magnitude False Data Injection Attacks](https://arxiv.org/abs/2606.08473)

**<font color=#1a73e8>作者：</font>** Xin Li, Chenhan Xiao, Jonathan Cohen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> False data injection attacks (FDIAs) introducing small measurement perturbations can still cause large deviations in power system state estimation when the injected signals align with the pseudo-null space of the system model. Existing model- and data-driven detectors may fail to identify such low-magnitude but high-impact attacks because residual tests ignore changes hidden in the pseudo-null space, while subspace learning methods capture correlation patterns without enforcing physical consistency. This paper proposes Physically Consistent Null Space Alignment (PCNSA), a framework that detects stealthy FDIAs by preserving, through preprocessing, the geometric correspondence between the physical null space and the measurement-derived pseudo-null space. The key point is a Pseudo-null Space Conserved data Preprocessing (PSCP) step that re-expresses measurements in the physical coordinate frame before subspace extraction. We prove that PSCP preserves the separation between row space and its orthogonal complement, a property that conventional per-feature standardization violates. This keeps the singular value decomposition (SVD)-derived pseudo-null subspace aligned with the physical residual space without explicit knowledge of H. Experiments on IEEE 14-, 30-, 57-, and 118-bus systems confirm this principle in practice: stealthy attacks that evade XTM, LSTM, AE and Isolation Forest baselines appear as clear deviations in the aligned subspace, yielding higher F1-score and detection accuracy while remaining robust under partial observability and realistic PMU noise.

---


### 172. [Testing the Black Box: Structural Barriers to Independent Evaluation of Consumer-Facing Health LLMs](https://arxiv.org/abs/2606.08483)

**<font color=#1a73e8>作者：</font>** Rahul Gorijavolu, Kaushik Madapati, Pritika Vig 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: Consumer-facing large language models are now a common source of health information, and they interpret and personalize responses rather than retrieve them. Whether their responses vary across users is a clinical, equity, and governance question, sharpened by evidence that sycophantic responses can alter judgment and increase trust.
Objective: To evaluate response variation and sycophancy in consumer-facing health LLMs under conditions resembling ordinary patient use.
Methods: We constructed simulated user profiles differing in geography, browsing context, expressed beliefs, and social determinants of health, drawing on literature linking social context to health attitudes. We adapted validated instruments, including the Vaccination Attitudes Examination scale and reproductive attitudes scales, into multi-turn prompts designed to elicit clinically meaningful variation across users.
Results: The evaluation encountered five linked barriers. Factual prompts produced stable responses that masked sycophancy emerging over multi-turn conversation. Browser-based interfaces did not disclose which signals influence outputs and could not be reset to a clean baseline. Large-scale testing was restricted by terms of service, rate limits, and bot detection. Accuracy-based criteria could not capture tone, framing, or omission, and LLM-as-judge methods risked shared alignment bias. Models changed without traceable version identifiers, preventing reliable replication.
Conclusions: No reliable independent evaluation framework yet exists for examining how consumer-facing health LLMs behave in ordinary use. Oversight requires disclosure of personalization signals, stable version identifiers, researcher safe harbor programs, and post-deployment monitoring of health-related outputs.

---


### 173. [STELLAR: Spatio-Temporal Environmental Learning with Latent Alignment and Refinement for Long-Tailed Species Distribution Modeling](https://arxiv.org/abs/2606.08484)

**<font color=#1a73e8>作者：</font>** Shufeng Kong, Tao Yu, Yuanyuan Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint Species Distribution Modeling (JSDM) is a key enabler for biodiversity monitoring and conservation planning. However, accurate JSDM faces two coupled challenges: environmental drivers and species distributions are inherently spatio-temporal, while species co-occurrence patterns exhibit complex non-linear community structure and severe long-tail imbalance driven by rare species. Existing approaches often address these factors in isolation, learning from static covariates or neglecting the historical trajectories of dynamic community structure. To overcome these limitations, we propose STELLAR (Spatio-Temporal Environmental Learning with Latent Alignment and Refinement), a novel framework that learns a shared latent space where dynamic habitat context and community structure are optimized jointly. Our approach integrates three complementary components: (1) a Graph-Temporal Encoder that employs graph attention and recurrent units to aggregate spatial neighborhood effects and capture the co-evolving historical dynamics of environmental context and community structure; (2) a Context-Anchored Latent Alignment mechanism that structures the latent space using a label-activated mixture prior and supervised contrastive learning, actively clustering species based on shared environmental preferences; and (3) an Imbalance-Aware Decoupled Decoding module that utilizes Asymmetric Loss to focus learning on hard, rare species samples, preventing mode collapse in the long tail. Experiments on the large-scale eBird dataset, curated with domain experts, demonstrate that our framework significantly outperforms state-of-the-art baselines, particularly in predicting rare species and revealing interpretable species interactions.

---


### 174. [TRADE: Transducer-Augmented Decoder for Speech LLM](https://arxiv.org/abs/2606.08486)

**<font color=#1a73e8>作者：</font>** Yun Tang, Shanil Puri, Shinji Watanabe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech Large Language Models (Speech LLMs) lack a principled mechanism for streaming inference: their label-synchronous generation has no acoustic-frame alignment, making real-time decoding and end-of-utterance detection difficult. We propose TRADE TRansducer-Augmented DEcoder, which augments a multimodal LLM with a transducer branch that shares the audio encoder and uses the LLM's hidden states directly as the prediction network -- coupling frame-synchronous acoustic alignment with the LLM's linguistic reasoning. Three design choices make the system accurate, streamable, and long-form capable: (1)Tightly coupled dual vocabularies -- a compact transducer vocabulary derived from the LLM vocabulary, enabling zero-cost score fusion; (2)Chunk-synchronized streaming training with gradient stopping, eliminating the train-inference mismatch at offline-equivalent memory cost; and (3)Localized Decoder Audio Attention (LDAA), a causal sliding window that caps KV-cache memory independently of utterance length. A single TRADE checkpoint supports offline and streaming decoding across a continuous range of latency operating points. TRADE achieves 6.71% average WER on the Open ASR Leaderboard, while the streaming recognition with 960ms chunk size reaches 8.40% from the same checkpoint. On long-form speech, it obtains 3.64% WER on TED-LIUM and 10.88% on Earnings-22 without external segmentation. TRADE provides sentence-end punctuation timestamps that, when combined with acoustic voice activity detection (VAD), improve end-of-utterance detection by +0.03 F_1 over acoustic VAD alone.

---


### 175. [Seeing is Believing: Aligning Prompt Rewriting with Visual Anchors for Text-to-Image Generation](https://arxiv.org/abs/2606.08492)

**<font color=#1a73e8>作者：</font>** Xuanyi Liu, Deyi Ji, Junyu Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the impressive capabilities of text-to-image (T2I) models, an intent-generation gap often persists due to the brevity and ambiguity of user prompts. Existing approaches primarily polish the prompt for fluency and readability. However, the enhancement process still lacks visual grounding. As a result, the rewriter may over-infer missing details, causing an intent-generation gap. To address this limitation, we propose FaithRewriter, a novel prompt-enhancement framework for T2I generation. Specifically, FaithRewriter first leverages a multimodal MLLM to generate an image from the original prompt as an intermediate visual cue. This cue is then combined with the prompt and fed into a large-scale LLM to produce visually grounded augmentations that better reflect how the intended content should appear in images. Finally, these augmentations are distilled into a small-scale LLM for efficient deployment, enhancing its ability to generate effective T2I prompts. Experiments show that FaithRewriter yields prompts that are more faithful to the user intent and more visually plausible than strong baselines, helping narrow the intent-generation gap.

---


### 176. [SAEExplainer: Interpreting SAE Features with Activation-Guided Preference Optimization](https://arxiv.org/abs/2606.08496)

**<font color=#1a73e8>作者：</font>** Jingyi He, Haiyan Zhao, Ruxue Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although Sparse Autoencoders (SAEs) have mitigated the opacity of large language models (LLMs) by decomposing dense representations into sparse features, explaining these features still remains a central challenge. Current explanation methods, however, typically operate within an open-loop paradigm, failing to leverage mechanistic feedback for further refinement. In this paper, we propose SAEExplainer, a training framework utilizes activation scores as an objective reward signal to train the model for self-correction and iterative bootstrapping. By iteratively verifying and correcting foundational explanations through a two-round optimization process, SAEExplainer achieves continuous improvement in its explanatory capabilities. This mechanism significantly reduces explanation hallucinations and reinforces causal triggering patterns. Extensive experiments demonstrate our approach improves upon established baselines across most metrics, especially in causal triggering and discriminative activation.

---


### 177. [Explaining Black-Box Language Models: Learning to Optimize Linguistically-Structured Word Subsets](https://arxiv.org/abs/2606.08497)

**<font color=#1a73e8>作者：</font>** Minyoung Hwang, Seokhyun Lee, Changhee Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As deep language models (DLMs) are increasingly deployed in high-stakes domains such as healthcare, understanding their decision rationale becomes paramount for ensuring trust, safety, and accountability. However, achieving this vital level of interpretability is particularly challenging when these DLMs operate as black-box systems (e.g., via APIs), where access to internal model states (e.g., parameters, gradients) is restricted. Despite numerous efforts, existing explanation methods often fail to concurrently satisfy three key desiderata: (i) inference-time efficiency, (ii) black-box compatibility without inducing out-of-distribution behavior, and (iii) comprehensible explanations grounded in the input's linguistic structure. To address these challenges, we propose a method that explains predictions of DLMs by selecting a small, informative subset of input words. We formulate this as an amortized optimization problem, enabling efficient one-shot inference without the need for input-specific search. Our selection policy is trained via REINFORCE-style policy gradients, allowing discrete word selection in a fully gradient-free setting. To enhance interpretability and align with human linguistic intuition, we integrate graph-structured knowledge into this selection process, fostering linguistically coherent subsets that result in explanations both highly informative and cognitively meaningful to end-users. We evaluated our method on diverse DLM architectures and multiple real-world datasets. It consistently identifies word subsets with enhanced discriminative power and stronger alignment with linguistically salient cues, outperforming both conventional black-box compatible methods and gradient-based approaches that are given oracle access to the black-box model's gradients for a more challenging benchmark. Our code is available at here.

---


### 178. [Back on Track: Aligning Rewards and States for Reasoning in Diffusion Large Language Models](https://arxiv.org/abs/2606.08501)

**<font color=#1a73e8>作者：</font>** Yawen Shao, Jie Xiao, Kai Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) holds immense promise for enhancing the reasoning capabilities of diffusion large language models (dLLMs). However, progress is fundamentally constrained by a dual misalignment between authentic generation trajectory and the gradient update process: (i) Process-reward misalignment. Sparse, terminal rewards are indiscriminately assigned to all intermediate steps of the generation process, failing to provide discriminative credit assignment. (ii) State-trajectory misalignment. Policy updates are often diverted toward artificial, out-of-trajectory states, squandering gradients on less informative samples. To address these limitations, we introduce Process Aligned Policy Optimization (PAPO), a novel framework that holistically aligns the RL update with the dLLM's generative trajectory via Step-Aware Process Rewards (SPR) that transform sparse terminal rewards into dense, step-wise credit, and Entropy-Guided Historical Re-enactment (EHR) that replays authentic trajectories at high-uncertainty steps. Extensive experiments on four benchmarks demonstrate that PAPO significantly outperforms baselines, achieving gains of up to 4.5% on GSM8K, 4.8% on MATH500, 42.2% on Countdown and 16.1% on Sudoku.

---


### 179. [Look Less, Reason More: Block-wise Attention Skipping for Efficient Multimodal LLMs](https://arxiv.org/abs/2606.08511)

**<font color=#1a73e8>作者：</font>** Jie Ma, Zhike Qiu, Jiayi Ji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) face a significant inference bottleneck due to the quadratic computational cost of self-attention over long visual token sequences. However, we identify a critical inefficiency in current architectures: Visual Attention Saturation. Our analysis reveals that visual tokens rapidly establish their spatial structure and intra-modal relationships in early layers, rendering visual-to-visual self-attention in deeper layers computationally redundant. Conversely, Feed-Forward Networks (FFNs) in these layers remain essential for projecting visual features into the evolving textual semantic space. Leveraging this insight, we present Visual-Skip (V-Skip), a training-free inference paradigm that decouples spatial interaction from semantic evolution. Rather than discarding tokens, V-Skip imposes block-wise structured sparsity by selectively bypassing saturated visual self-attention modules. Furthermore, recognizing that varying downstream tasks demand distinct reasoning depths, V-Skip employs a lightweight, few-shot calibration to dynamically route the task-optimal sparsity path. Extensive experiments demonstrate that V-Skip effectively bypasses redundant vision attention to achieve block-wise sparsity, maintaining a 94.16% to 100.31% performance retention across diverse MLLMs. Ultimately, we prove that to reason more effectively, models do not need to discard what they see -- they simply need to "look less" at the right depth.

---


### 180. [VESTA: A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents](https://arxiv.org/abs/2606.08531)

**<font color=#1a73e8>作者：</font>** Lu Jia, Haibo Tong, Feifei Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly evolving from simple text-based interaction systems into LLM agents that can maintain memory, use tools, access external environments, and execute tasks. As their capabilities and autonomy expand, the safety risks they face also become more diverse. Existing evaluations often rely on manually written scenarios, static prompts, or final-output judgments, making it difficult to capture the diverse risks that agents may face during task execution. We introduce VESTA, a fully automated scenario generation and safety evaluation framework for LLM agents. Based on five risk dimensions, VESTA instantiaes abstract and diverse safety risks in real-world task execution into 1,072 measurable evaluation scenarios. Using the automated evaluation pipeline, 12 LLM agents are evaluated under two authority contexts. The results show that current agents still face substantial behavioral safety risks during task execution, with an average ASR of 47.1% and several models exceeding 70%. These findings demonstrate the importance of executable, process-level evaluation for understanding and improving LLM agent safety.

---


### 181. [DN-Hypo-Pipeline: An AI-Driven Workflow for Hypothesis Generation via Large Language Models and Scientific Explanations](https://arxiv.org/abs/2606.08532)

**<font color=#1a73e8>作者：</font>** Lei Lin, Ronghao Wang, Chunbao Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A scientific hypothesis is the first step in research and undergoes experimental validation, yet it also reflects a deep understanding of and reasoning about scientific phenomena. We introduce DN-Hypo-Pipeline, an AI-powered workflow based on large language models, designed to support structured scientific thinking and hypothesis generation by leveraging scientific explanations as prior knowledge. This pipeline assists researchers in deriving novel hypotheses from existing literature. Given the explanandum (i.e., the conclusion) of a research paper, it identifies underlying laws, theories, and principles, and reconstructs a new, yet-to-be-verified explanation for the observed phenomenon. We evaluated DN-Hypo-Pipeline in the field of data science modeling using three highly cited papers. Statistical inference, supported by both LLM-as-judge assessment and human expert evaluation, demonstrates that our pipeline is more effective than direct generation methods. Additionally, we validated the two highest-scoring generated hypotheses by developing corresponding novel algorithms, which outperformed the baseline models presented in the original papers. Beyond application in data science, DN-Hypo-Pipeline provides a theoretical framework that not only encompasses theory-guided data science modeling methods but also reveals a more fundamental structure of the modeling process. Moreover, this approach is essentially a generalization of theory-guided modeling, offering potential for extension to other domains and across a broader range of scientific disciplines.

---


### 182. [PAEC: Position-Aware Entropy Calibration for LLM Reasoning in RLVR](https://arxiv.org/abs/2606.08543)

**<font color=#1a73e8>作者：</font>** Shumeng Yang, Yisu Liu, Jiayi Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves large language model reasoning but often suffers from rapid policy-entropy collapse, where the policy prematurely concentrates on narrow high-probability reasoning paths. While global entropy regularization can encourage exploration, uniformly increasing entropy across all token positions is inefficient for long reasoning trajectories, where many tokens are not decision-relevant. We propose Position-Aware Entropy Calibration (PAEC), a token-level entropy-management framework that constructs a soft mask from local top-p entropy and top-two candidate competition, and applies an anchor-based lower-bound penalty to prevent selected-position entropy collapse. Experiments on five mathematical reasoning benchmarks show that PAEC improves macro-average majority-vote performance over strong RLVR baselines, with clear gains on AIME-style tasks. Our results suggest that entropy management in reasoning RL should be formulated as selective exploration allocation over decision-sensitive positions rather than uniform randomness injection.

---


### 183. [Ishigaki-IDS: An Open-Weight Verifier-Aware Model for Information Delivery Specification Drafting in Building Information Modeling](https://arxiv.org/abs/2606.08545)

**<font color=#1a73e8>作者：</font>** Ryo Kanazawa, Koyo Hidaka, Teppei Miyamoto 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building Information Modeling (BIM) projects require information requirements to be described as machine-checkable Information Delivery Specification (IDS) files in order to verify whether building models contain the required attributes. However, IDS authoring remains a practical bottleneck: practitioners must handle domain vocabulary, strict XML schema constraints, and external validator conformance while also checking whether the requirement itself is correctly expressed. We present Ishigaki-IDS, an open-weight LLM specialized for verifier-aware IDS draft generation. The model combines continued pretraining on BIM/IDS corpora, supervised fine-tuning on information-requirement-to-IDS pairs, and reinforcement learning with verifiable rewards from an external validator. The goal is not to replace expert review, but to move IDS authoring from low-level XML and schema repair toward validator-loadable drafts that practitioners can inspect and correct. On the 166-case expert-created Ishigaki-IDS-Bench, Ishigaki-IDS-8B achieves an IDSAuditPass score of 0.651, a validator-pass metric for generated IDS files, substantially outperforming Claude Opus 4.5, the strongest single-shot LLM baseline we evaluated, at 0.331. It also obtains an Audit-Gated FacetF1 of 0.282, which measures requirement-facet alignment among validator-passing drafts. The same recipe scales: 14B and 32B variants reach IDSAuditPass 0.753 / 0.693 and Audit-Gated FacetF1 0.392 / 0.369. In a workflow check with six BIM practitioners, Ishigaki-assisted authoring reduced aggregate work time by 54.7% under the same validation and alignment endpoint. These results suggest that verifier-aware IDS generation can reduce the practical burden of converting BIM information requirements into reviewable IDS drafts.

---


### 184. [Inside the LLM Word Factory](https://arxiv.org/abs/2606.08562)

**<font color=#1a73e8>作者：</font>** Benzi Busigin, Yuval Pinter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer language models process input provided as subword fragments, but natural language semantics usually rely on word-level concepts. Detokenization is the process where models reconcile these two facts, aggregating subwords into word-level representations through their computation. Prior work has found that this takes place mostly in early-to-middle layers, but so far the exact mechanics of the process have not been pinned down. We venture deep into detokenization using activation patching in controlled paired experiments that isolate the contribution of different model components, localizing English detokenization in Llama2-7B to a two-stage process at Layer 1. Attention transmits a token-specific signal from nonfinal subwords, using sequential relays if necessary, while the MLP composes it with the local embedding. This two-stage structure generalizes to twelve models from eight families, but the depth over which it takes place depends on the flavor of positional encoding: RoPE-based models detokenize over 1 to 5 layers, while learned-absolute models take 5 to 10. Finally, we provide a probe for determining the success of the detokenization process based on early-layer activations alone, performing at 0.94-0.97 AUROC depending on the amount of context.

---


### 185. [EinSort: Sorting is All We Need for Tensorizing LLM](https://arxiv.org/abs/2606.08565)

**<font color=#1a73e8>作者：</font>** Toshiaki Koike-Akino, Jing Liu, Ye Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensor networks provide efficient representations for compressing large neural networks. By carefully designing shapes and topologies, they can significantly reduce memory and computational costs. However, identifying implicit low-rank structures in large foundation models remains challenging due to their enormous scale and un-structured weight distributions. We propose an adaptive tensorization method that discovers inherent low-rank structure in a target tensor by index ordering. Experiments on weight and KV-cache compression demonstrate improved reconstruction quality compared to baselines.

---


### 186. [Calibration of Structured Ignorance Certificates for Diagnosing Unknown Unknowns in Reasoning Models](https://arxiv.org/abs/2606.08571)

**<font color=#1a73e8>作者：</font>** Subramanyam Sahoo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models frequently fail in a characteristic way: rather than acknowledging ignorance, they produce fluent but incorrect answers to questions that lie beyond their knowledge boundaries. We introduce \textbf{Structured Ignorance Certificates} (SICs), a JSON-formatted output schema that demands a model explicitly name the missing domain intersection, enumerate required concepts, and propose a productive retrieval query rather than hallucinating an answer. To train models to produce high-quality SICs we construct a 7,347-sample \emph{Unknown-Unknown} (UU) dataset by prompting Qwen3-14B to stitch together questions from seven domains (physics, biology, engineering, CS, economics, medical, legal) into novel cross-domain queries that no single-domain expert could answer. We fine-tune a 14B-parameter model with Group Relative Policy Optimization (GRPO) using a composite reward that combines retrieval utility, concept specificity, and output-format validity. A paraphrase-divergence probe trained on model responses confirms that SIC-tuned outputs systematically exhibit higher unknown-unknown probability scores. Evaluation on 735 held-out UU questions achieves a 99.46\% JSON validity rate, a mean Certificate Specificity Score of 0.967, and a 3.6\% ROUGE-L improvement over the base model on retrieval-grounded generation -- demonstrating that explicit epistemic structuring is a learnable and measurable capability.

---


### 187. [Lost in the Non-convex Loss Landscape: How to Fine-tune the Large Time Series Model?](https://arxiv.org/abs/2606.08578)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Peang Wang, Wei Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, large time series models (LTSMs) have gained increasing attention due to their similarities to large language models, including flexible context length, scalability, and task generality, outperforming advanced task-specific models. However, prior studies indicate that pre-trained LTSMs may exhibit a poorly conditioned non-convex loss landscape, leading to limited trainability. As a result, direct fine-tuning tends to cause overfitting and suboptimal performance, sometimes even worse than training from scratch, substantially diminishing the benefits of pre-training. To overcome this limitation, we propose Smoothed Full Fine-tuning (SFF), a novel fine-tuning technology. Specifically, we construct an auxiliary LTSM via random initialization to obtain a smoother loss landscape, and then linearly interpolate its weights with those of the pre-trained model to smooth the original landscape. This process improves trainability while preserving pre-trained knowledge, thereby enabling more effective downstream fine-tuning. From an optimization perspective, SFF perturbs sharp minima without significantly harming flat regions, facilitating escape from poor local basins toward smoother and more generalizable solutions. Extensive experiments on benchmark datasets demonstrate consistent improvements across eight representative LTSMs, including Timer, TimesFM, MOMENT, UniTS, MOIRAI, Chronos, TTMs, and Sundial, on diverse downstream tasks. The code is available at the link: this https URL.

---


### 188. [Detection and Interpretability Analysis of Quotation Errors by Large Language Models](https://arxiv.org/abs/2606.08589)

**<font color=#1a73e8>作者：</font>** Bei Huang, Yingyi Zhang, Shenghao Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose - Quotation error refers to the inconsistency between cited information and its original source. This phenomenon leads to a series of negative impacts, such as misinterpretation of the original research, undermining the academic community's collective understanding of relevant issues, and weakening the accuracy and fairness of the citation-based academic evaluation system. Existing studies have shown that quotation error is prevalent in the academic community; moreover, manual verification of quotation error is not only labor-intensive but also inefficient. Therefore, this paper proposes the task of 'automated detection of quotation errors'. Methodology - Adopting a large language model (LLM)-based approach, this paper improves detection performance from two aspects on the basis of existing research: first, employ the fine-tuning approach for LLMs to detect quotation errors; second, incorporating full-text data of the cited literature into dataset construction, and exploring the optimal scheme for building such datasets by comparing three types of full-text integration methods. Based on this, this paper further uses the TokenSHAP tool to conduct interpretability experimental analysis on the model's prediction results. Findings - The fine-tuning approach for LLMs has improved the performance in detecting quotation errors. Among the different methods for incorporating full-text information, the approach based on using the source abstract yielded the best performance. Originality - The fine-tuning approach for large language models (LLMs) is applied to the task of automated detection of quotation errors, and interpretability analysis is conducted on the model's output results.

---


### 189. [Distilling LLM Reasoning into an Interpretable Policy Tree for Human-AI Collaboration](https://arxiv.org/abs/2606.08596)

**<font color=#1a73e8>作者：</font>** Beiwen Zhang, Yongheng Liang, Guowei Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constructing efficient and reliable policies to assist humans is indispensable for human-AI collaboration. Existing methods mainly follow two lines of work. Most prior work relies on multi-agent reinforcement learning (MARL) to learn black-box policies, which limits interpretability and raises safety concerns. Recent methods query large language models (LLMs) at each decision step, causing slow responses and high inference costs. We propose Collaboration Policy Tree (Co-pi-tree), a closed-loop method that learns an executable policy tree consisting of a partner-behavior prediction tree and an agent-action selection tree. Co-pi-tree constructs a policy by distilling LLM reasoning into policy tree code. It then evaluates the policy through partner interaction, obtains feedback, and uses natural language to summarize the interaction feedback to improve problematic branches. Experiments in Overcooked-AI show that Co-pi-tree improves average reward by 35.4% over the baseline average, while reducing the number of LLM queries by 77.7% and test-time latency by 97.1%. Project page: this https URL

---


### 190. [InA-Probe: Instruction-Aware Active Probing for Time Series Forecasting with LLMs](https://arxiv.org/abs/2606.08601)

**<font color=#1a73e8>作者：</font>** Peiliang Gong, Emadeldeen Eldele, Chenyu Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have recently demonstrated impressive potential for time series forecasting. However, existing methods predominantly rely on passive modality alignment or static task reprogramming, which often fail to capture fine-grained, non-stationary temporal patterns or to adapt to nuanced task intents. In this paper, we propose Instruction-aware Active Probing (InA-Probe), which shifts the paradigm from passive alignment toward an active, instruction-driven probing mechanism. Specifically, we design a Multi-Level Instruction Injection mechanism that enriches the model with both global task objectives and fine-grained, patch-level semantic priors. Building on this, an Adaptive Query Generation module produces sample-specific probes that are dynamically modulated by the temporal context. These probes are then refined through a dual-stage attention process: they first internalize task-specific intents via Instruction-Aware Self-Attention, and subsequently interrogate the projected temporal representations through Temporal Cross-Attention to extract salient patterns. Comprehensive experiments on seven real-world benchmarks show that InA-Probe consistently outperforms state-of-the-art deep learning and LLM-based baselines, excelling in both one-for-all generalization and zero-shot transfer while reducing forecasting error by up to 37\% in challenging cross-domain scenarios. Ablation studies further confirm that the synergy between adaptive querying and fine-grained instructions is key to unlocking the reasoning power of LLMs for complex time series.

---


### 191. [Multilingual Fact-Checking at Scale: Fine-Tuned Compact Models vs LLMs](https://arxiv.org/abs/2606.08605)

**<font color=#1a73e8>作者：</font>** Pratuat Amatya, Vinay Setty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a multilingual fact-checking system deployed at Factiverse, designed for high-throughput and low-latency operation across diverse languages. The system follows a modular pipeline with three stages: claim detection, evidence retrieval and re-ranking, and veracity prediction. We fine-tune XLM-RoBERTa-Large for claim detection, mmBERT-base for three-label stance classification (Supports/Refutes/Mixed), and a SetFit-based multilingual re-ranker for claim--evidence matching. We compare these components against strong LLM baselines, including GPT-5.2, Claude Opus~4.6, and Qwen3-8b. Experiments on production data spanning 114 languages for claim detection and 28 languages for veracity prediction show that task-specific fine-tuning provides strong and stable multilingual performance, while the fine-tuned retrieval model remains competitive with modern proprietary embeddings. Same-hardware latency measurements further show large efficiency gains for encoder-based components, supporting their use in production deployments with tight cost and privacy constraints. Overall, compact fine-tuned, self-hosted models remain a practical and effective foundation for multilingual fact-checking at scale. Code and data used for this study are available at this https URL.

---


### 192. [From Holistic Evaluation to Structured Criteria: Rubrics Across the Evolving LLM Landscape](https://arxiv.org/abs/2606.08625)

**<font color=#1a73e8>作者：</font>** Hao Chen, Ziyu Han, Yukun Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) advance toward open-ended autonomous agents, the mechanisms used to evaluate and guide their behavior must evolve accordingly. This work introduces the rubric as a unifying framework capturing this evolution, characterizing rubrics as a dynamic response to successive LLM paradigm shifts that recurs across otherwise independent efforts in evaluation, reinforcement learning, and safety alignment. We define rubrics as explicit criteria sets that transform complex quality judgments into structured and actionable standards, and demonstrate that their recurrence across these research threads is not coincidental. We systematically organize existing rubric designs, examine their construction and optimization, and analyze their role across evaluation and training. Rubrics manifest at three progressively deeper levels: at the evaluative level, they decompose holistic judgments into verifiable dimensions; at the training level, they serve as dense feedback signals providing process-level guidance where scalar rewards fall short; at the intrinsic level, they emerge dynamically from model behaviors, driving self-improvement. We further assess rubric reliability across generation quality, execution fidelity, theoretical constraints, and security threats, before surveying rubric-based benchmarks across diverse domains. By rendering assessment transparent and decomposable, rubrics translate human value expectations into machine-learnable signals, serving as the enduring bridge between human intentions and machine behavior.

---


### 193. [Tyan-WP: A Wind Power Foundation Model for Ultra-Short-Term Probabilistic Forecasting](https://arxiv.org/abs/2606.08630)

**<font color=#1a73e8>作者：</font>** Jiahui Huang, Ao Luo, Lei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global wind power capacity, especially in China, is booming, with new farms spanning diverse terrains and climates. The industry urgently needs accurate wind power foundation models to shorten commissioning and accelerate grid connection. This is because site-specific time series models (TSMs) are not well suited to data-scarce scenarios and generalize poorly, while generic large time series models (LTSMs) are mostly limited to univariate inputs and cannot fully exploit static site attributes or the dependencies between power and meteorological covariates, leading to insufficient accuracy. To fill this gap, we propose \textbf{Tyan-WP}, the first wind power foundation model for ultra-short-term probabilistic forecasting. Pretrained on a large-scale wind power dataset covering more than 126,000 U.S. sites over seven years, Tyan-WP further improves zero-shot forecasting through two domain-specific module designs: static site embedding using coordinate, terrain, and ecoregion metadata, and a power-aware meteorological fusion (PAMF) module that models interactions between historical power and meteorological covariates. Under a unified evaluation protocol, Tyan-WP surpasses eight site-specific supervised TSMs on 10 in-domain sites and outperforms eleven generic LTSMs on 127 in-domain sites, reducing MAE by 19.9%, RMSE by 16.6%, CRPS by 22.2%, and AQL by 21.7%, while raising R^2 by 16.7%. It further demonstrates strong cross-geography generalization on six real U.K. sites. These results show that the wind power foundation model can achieve accurate zero-shot forecasting without target-site training, providing a practical pathway for rapid turbine onboarding and probabilistic risk management at new wind farms.

---


### 194. [Towards Long-Horizon Vessel Trajectory and Destination Forecasting with Reasoning Large Language Models](https://arxiv.org/abs/2606.08633)

**<font color=#1a73e8>作者：</font>** Hongwei Wang, Miao Zhou, Fengde Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon maritime trajectory prediction is important for shipping management, logistics planning, and maritime risk analysis, yet month-level forecasting remains insufficiently studied. Existing deep learning methods mainly focus on short- and mid-term coordinate extrapolation and often struggle to preserve route feasibility and destination correctness over extended horizons. This paper investigates joint long-horizon vessel trajectory and destination forecasting with reasoning-capable large language models, and develops a Maritime LLM post-training framework based on Reinforcement Learning with Verifiable Reward (RLVR). An AIS-based benchmark is constructed with 60-day historical trajectories and 30-day forecasting horizons, where trajectories are converted into semantic textual representations for RL prompt construction. RLVR aligns LLMs with maritime forecasting objectives by enforcing physical validity, providing early-weighted trajectory supervision, and evaluating destination correctness through hierarchical matching and curriculum learning. Experimental results show that RLVR-trained LLMs substantially improve over zero-shot LLMs and representative deep learning baselines, especially on destination-related metrics. Among the evaluated RLVR-trained variants, 4B LLMs achieve the best overall performance, suggesting that reward-compatible optimization and task-specific capacity matching are more important than simply using larger 8B or 14B LLMs. The results also show that LSTM remains a strong deep learning baseline under limited fine-tuning data, while Transformer-style spatio-temporal models typically require larger datasets and richer structured inputs. Overall, this work advances semantic, verifier-aligned maritime forecasting for operational decision support.

---


### 195. [SpectrumKV: Per-Token Mixed-Precision KV Cache Transfer for Prefill-Decode Disaggregated LLM Serving](https://arxiv.org/abs/2606.08635)

**<font color=#1a73e8>作者：</font>** Yang Pengju  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prefill-decode (PD) disaggregation decouples prompt processing from token generation, but it also turns the key-value (KV) cache into a network payload. Existing PD-side KV reduction methods are mostly binary: selected tokens are transmitted at full precision and the rest are not transmitted. This paper argues that binary selection leaves a useful design space unused. SpectrumKV assigns a precision level to each token instead: attention sinks and other high-importance tokens are protected at FP16, medium-importance tokens are sent at INT8, and low-importance tokens are sent at INT4 when the model can tolerate it. The main practical complication is that INT4 tolerance is model-dependent. Qwen2.5-7B catastrophically fails under INT4 KV quantization, while Mistral-7B and Gemma-2-9B remain stable. SpectrumKV therefore runs a lightweight deployment-time probe: three aggressive NIAH trials under a 3-tier policy. Models that pass use FP16+INT8+INT4; models that fail fall back to FP16+INT8. Across Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, and Gemma-2-9B-it, SpectrumKV improves quality at the same transfer budget. At a 50% normalized KV budget on WikiText-2, SpectrumKV changes perplexity by +1.97%,-0.06%, and-0.44%, respectively, compared with PDTrim's +25.85%, +22.07%, and +35.63%. On NIAH retrieval at 4096 tokens, the adaptive policy reaches 52.6% on Qwen at the aggressive b=0.3 budget versus 26.3% for PDTrim, and reaches 100% by b=0.5; Mistral and Gemma preserve retrieval under the 3-tier policy. End-to-end GPU timing of the transfer path shows 50-62% TTFT reductions at b=0.5. These results suggest that PD KV transfer should be treated as a precision-allocation problem, not only as token pruning.

---


### 196. [A retrieval conditioned rebinding circuit for dynamic entity tracking in large language models](https://arxiv.org/abs/2606.08644)

**<font color=#1a73e8>作者：</font>** Soyoung Oh, Vera Demberg  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To interpret context correctly and retrieve relevant information, large language models must bind entities to their attributes and update these bindings as state changes. We analyze how LLMs implement this binding process in a dynamic state tracking. Using causal interventions, we identify a retrieval conditioned rebinding mechanism, a compact attention head circuit that encodes swap relevant binding information and reinstates it at readout. Across Gemma and Llama models, this circuit supports rebinding behavior, but the representational signature of the mechanism differs across model families. In Gemma models, the binding signature is clearly expressed in the query/key subspaces of the relevant attention heads, whereas in Llama models, the binding information is carried primarily in key vectors. Overall, our results reveal an interpretable mechanism for context dependent state tracking in LLMs.

---


### 197. [FiberTune: Preserving Action-Fiber Visual Residuals in Vision-Language-Action Fine-Tuning](https://arxiv.org/abs/2606.08653)

**<font color=#1a73e8>作者：</font>** Haihao Lin, Xiangsheng Huang, Xiao Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-supervised fine-tuning of vision-language-action (VLA) policies fits demonstrations effectively but constrains only the directions that change predicted actions, leaving visual structure consistent across action-equivalent states free to collapse. We formalize this as residual visual collapse along local action fibers and propose FiberTune, a training-time objective that preserves teacher-structured visual residuals without adding inference-time overhead. FiberTune uses an online action probe to estimate action-predictive feature directions, filters them from intermediate visual-token representations, and aligns the resulting probe-filtered residuals to a frozen visual teacher while regularizing their effective rank. Under identical training conditions, FiberTune improves over task-loss-only fine-tuning in every one of six controlled simulation settings spanning two benchmarks and two architectures (pi_0.5 and OpenVLA-OFT), as well as on physical SO-101 pick-place; representative gains include +10.7 percentage points SR(5) on long-horizon CALVIN ABC-to-D and physical SO-101 task success rising from 72.7% to 78.1%. Residual diagnostics show that these gains coincide with increased probe-filtered residual teacher alignment and effective rank, consistent with the action-fiber motivation.

---


### 198. [From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory](https://arxiv.org/abs/2606.08656)

**<font color=#1a73e8>作者：</font>** Yishuo Cai, Xingyu Guo, Xuancheng Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly deployed in long-running settings where improving through experience at test time becomes important. A common approach is to update an explicit memory after each interaction to guide future decisions. However, most existing methods rely on hand-designed prompting rules, making it difficult to align memory updates with downstream objectives over multi-step horizons consistently. We propose MemoPilot, a plug-in memory copilot that explicitly trains the memory update process to improve a frozen LLM's performance across sequential interactions. We formulate memory updating as a multi-turn decision problem and optimize it end-to-end with multi-turn GRPO. Our training recipe introduces (i) a turn-wise reward signal and (ii) a context-independent, turn-level advantage estimation across rollouts, enabling finer-grained credit assignment and more stable training in multi-turn settings. We evaluate MemoPilot on two testbeds: multi-round Rock-Paper-Scissors (RPS) and Limit Texas Hold'em (LHE). Across both environments, MemoPilot substantially improves test-time learning of a frozen player over strong baselines, ranking first in Elo ratings on both games (1762 on LHE and 1590 on RPS) and outperforming all baseline memory methods and proprietary models, including DeepSeek-V3.2.

---


### 199. [Activation Steering Induces Emergent Misalignment: A More Comprehensive Evaluation](https://arxiv.org/abs/2606.08682)

**<font color=#1a73e8>作者：</font>** Qi Cao, Jian Lou, Meiting Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering has emerged as a popular inference-time technique for modulating the behavior of large language models (LLMs). By constructing a steering vector from examples of a target behavior and injecting it into intermediate activations during inference, activation steering enables flexible behavioral control while avoiding the permanent parameter updates required by finetuning. Meanwhile, recent work has identified emergent misalignment (EM) as a significant safety concern, wherein models finetuned on unsafe examples from a narrow task may unexpectedly generalize to broadly unsafe behavior on unrelated tasks. Although finetuning-induced EM has been extensively studied, whether activation steering can induce EM remains comparatively under-explored, despite its increasing use as a model-control technique. In this paper, we present a comprehensive study of activation-steering-induced emergent misalignment, substantially expanding the evaluation scope beyond existing pioneering work. First, we show that activation steering can induce broad misalignment, even in the recent Qwen-3.5 series. Moreover, activation-steered models produce harmful responses with stronger semantic relevance and higher coherence than their finetuned counterparts, making the resulting misalignment potentially more harmful. Second, we characterize properties of AS-induced EM by analyzing key steering-specific factors, including steering magnitude, the low-rank structure of the steering subspace, and the number of epochs during steering-vector construction. Third, we evaluate the robustness and sensitivity of AS-induced EM across diverse model families, model scales, target tasks, and intervention layers. Our findings reveal activation steering as a significant yet under-examined source of emergent misalignment and provide an activation-space perspective for understanding the mechanisms and safety risks of EM.

---


### 200. [Agentic Search for Counterfactual Recourse under Fixed LLM Budgets](https://arxiv.org/abs/2606.08696)

**<font color=#1a73e8>作者：</font>** Yasuo Tabei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual recourse aims to provide actionable feature changes that would alter an unfavorable decision made by a predictive model. In practice, affected individuals often benefit from multiple feasible alternatives rather than a single optimal explanation. A natural way to produce such alternatives is to prompt large language models (LLMs). However, prompting incurs a practical constraint: the number of LLM calls is often the dominant computational and economic cost. Together, the need for multiple alternatives and this cost constraint shift the problem from finding a single high-quality counterfactual to efficiently generating a set of oracle-validated counterfactuals under a fixed LLM-call budget. In this work, we study counterfactual recourse generation in the LLM-agentic setting as a fixed-budget search problem and propose Comp-MCTS, an agentic tree-search framework that maximizes the yield of unique, oracle-validated counterfactuals under this budget while maintaining favorable quantity--quality trade-offs. Comp-MCTS allocates the budget toward novel intervention directions via LLM-based proposal generation, oracle validation, and compression-guided pruning, in a training-free, oracle-only setting. Experiments on four real-world tabular datasets show that Comp-MCTS substantially outperforms single-candidate LATS-style baselines in the yield of unique, oracle-validated counterfactuals, and offers favorable quantity--quality--efficiency trade-offs against stronger multi-candidate variants: comparable or higher yield at similar or lower oracle-evaluation cost on three of four datasets, plus competitive proximity, sparsity, and novelty.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-331](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
