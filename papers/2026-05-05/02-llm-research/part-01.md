# 🧠 大模型相关研究 | 2026年05月05日

> 本类共 **79** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-79](./part-02.md)

---

### 1. [AirFM-DDA: Air-Interface Foundation Model in the Delay-Doppler-Angle Domain for AI-Native 6G](https://arxiv.org/abs/2605.00020)

**<font color=#1a73e8>作者：</font>** Kejia Bian, Meixia Tao, Jianhua Mo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of large foundation models is catalyzing a new paradigm for AI-native 6G network design: wireless foundation models for physical layer design. However, existing models often operate on channel state information (CSI) in the space-time-frequency (STF) domain, where distinct multipath components are inherently superimposed and structurally entangled. This hinders the learning of universal channel representation. Meanwhile, their reliance on global attention mechanisms incurs prohibitive computational overhead. In this paper, we propose AirFM-DDA, an Air-interface Foundation Model operating in the Delay-Doppler-Angle (DDA) domain for physicallayer tasks. Specifically, AirFM-DDA reparameterizes CSI from the STF domain into the DDA domain to explicitly resolve multipath components along physically meaningful axes. It employs a window-based attention module augmented with framestructure-aware positional encoding (FS-PE). This window-based attention aligns with locally clustered multipath dependencies while avoiding quadratic-complexity global attention, and FS-PE injects frame-structure priors into network. Extensive experiments demonstrate that AirFM-DDA achieves superior zero-shot generalization across unseen scenarios and datasets, consistently outperforming the baselines on channel prediction and estimation tasks. Compared to the global attention, its window-based attention reduces training and inference costs by nearly an order of magnitude. Moreover, AirFM-DDA maintains robustness under high mobility, large delay spreads, severe noise, and extreme aliasing conditions.

---


### 2. [TADI: Tool-Augmented Drilling Intelligence via Agentic LLM Orchestration over Heterogeneous Wellsite Data](https://arxiv.org/abs/2605.00060)

**<font color=#1a73e8>作者：</font>** Rong Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present TADI (Tool-Augmented Drilling Intelligence), an agentic AI system that transforms drilling operational data into evidence-based analytical intelligence. Applied to the Equinor Volve Field dataset, TADI integrates 1,759 daily drilling reports, selected WITSML real-time objects, 15,634 production records, formation tops, and perforations into a dual-store architecture: DuckDB for structured queries over 12 tables with 65,447 rows, and ChromaDB for semantic search over 36,709 embedded documents. Twelve domain-specialized tools, orchestrated by a large language model via iterative function calling, support multi-step evidence gathering that cross-references structured drilling measurements with daily report narratives. The system parses all 1,759 DDR XML files with zero errors, handles three incompatible well naming conventions, and is backed by 95 automated tests plus a 130-question stress-question taxonomy spanning six operational categories. We formalize the agent's behavior as a sequential tool-selection problem and propose the Evidence Grounding Score (EGS) as a simple grounding-compliance proxy based on measurements, attributed DDR quotations, and required answer sections. The complete 6,084-line, framework-free implementation is reproducible given the public Volve download and an API key, and the case studies and qualitative ablation analysis suggest that domain-specialized tool design, rather than model scale alone, is the primary driver of analytical quality in technical operations.

---


### 3. [Soft-MSM: Differentiable Context-Aware Elastic Alignment for Time Series](https://arxiv.org/abs/2605.00069)

**<font color=#1a73e8>作者：</font>** Christopher Holder, Anthony Bagnall  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Elastic distances like dynamic time warping (DTW) are central to time series machine learning because they compare sequences under local temporal misalignment. Soft-DTW is an adaptation of DTW that can be used as a gradient-based loss by replacing the hard minimum in its dynamic-programming recursion with a smooth relaxation. However, this approach does not directly extend to elastic distances whose transition costs depend on the local alignment context. Move-Split-Merge (MSM) is one such distance: it uses context-aware split and merge penalties and has often outperformed DTW in supervised and unsupervised time series machine learning tasks such as classification and clustering.
We introduce Soft-MSM, a smooth relaxation of MSM and an elastic alignment loss with context-aware transition costs. Central to the formulation is a smooth gated surrogate for MSM's piecewise split/merge cost, which enables gradients through both the dynamic-programming recursion and the local transition structure. We derive the forward recursion, backward recursion, soft alignment matrix, closed-form gradient, limiting behaviour, and divergence-corrected formulation. Experiments on 112 UCR datasets show that Soft-MSM gives lower MSM barycentre loss than existing MSM barycentre methods, and yields significantly better clustering and nearest-centroid classification performance than Soft-DTW-based alternatives. An implementation is available in the open-source \texttt{aeon} toolkit.

---


### 4. [AgentReputation: A Decentralized Agentic AI Reputation Framework](https://arxiv.org/abs/2605.00073)

**<font color=#1a73e8>作者：</font>** Mohd Sameen Chishti, Damilare Peter Oyinloye, Jingyue Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decentralized, agentic AI marketplaces are rapidly emerging to support software engineering tasks such as debugging, patch generation, and security auditing, often operating without centralized oversight. However, existing reputation mechanisms fail in this setting for three fundamental reasons: agents can strategically optimize against evaluation procedures; demonstrated competence does not reliably transfer across heterogeneous task contexts; and verification rigor varies widely, from lightweight automated checks to costly expert review. Current approaches to reputation drawing on federated learning, blockchain-based AI platforms, and large language model safety research are unable to address these challenges in combination. We therefore propose \textbf{AgentReputation}, a decentralized, three-layer reputation framework for agentic AI systems. The framework separates task execution, reputation services, and tamper-proof persistence to both leverage their respective strengths and enable independent evolution. The framework introduces explicit verification regimes linked to agent reputation metadata, as well as context-conditioned reputation cards that prevent reputation conflation across domains and task types. In addition, AgentReputation provides a decision-facing policy engine that supports resource allocation, access control, and adaptive verification escalation based on risk and uncertainty. Building on this framework, we outline several future research directions, including the development of verification ontologies, methods for quantifying verification strength, privacy-preserving evidence mechanisms, cold-start reputation bootstrapping, and defenses against adversarial manipulation.

---


### 5. [How Frontier LLMs Adapt to Neurodivergence Context: A Measurement Framework for Surface vs. Structural Change in System-Prompted Responses](https://arxiv.org/abs/2605.00113)

**<font color=#1a73e8>作者：</font>** Ishan Gupta, Pavlo Buryi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We examine if frontier chat-based large language models (LLMs) adjust their outputs based on neurodivergence (ND) context in system prompts and describe the nature of these adjustments. Specifically, we propose NDBench, a 576-output benchmark involving two frontier models, three system prompt types (baseline, ND-profile assertion, and ND-profile assertion with explicit instructions for adjustments), four canonical ND profiles, and 24 prompts across four categories, one of which involves an adversarial masking strategy.
Four trends emerge consistently from our findings. First, LLMs show significant adaptation under ND context, where fully instructed conditions yield lengthier and more structured outputs, characterized by higher token counts, more headings, and more granular steps (p < 10^-8, Holm-corrected). Second, such adaptation is largely structural in nature: although list density does not change much, there is a marked rise in the frequency of headings and per-step detail. Third, ND persona assertion alone fails to suppress potentially harmful tendencies, as masking-reinforcement decreases only in explicitly instructed cases (36-44% reduction); the reduction rate barely changes in persona assertion conditions.
Moreover, reliability analysis of LLM-based harm assessment reveals that only two out of the six dimensions (masking and reinforcement, validation quality) exceed the pre-defined inter-judge agreement criterion (alpha >= 0.67) and thus can be considered primary results.
NDBench is made publicly available along with its prompts, outputs, code, and other resources, forming a reproducible framework for auditing future LLMs' adaptation to ND awareness.

---


### 6. [Cultural Benchmarking of LLMs in Standard and Dialectal Arabic Dialogues](https://arxiv.org/abs/2605.00119)

**<font color=#1a73e8>作者：</font>** Muhammad Dehan Al Kautsar, Saeed Almheiri, Momina Ahsan 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There is a significant gap in evaluating cultural reasoning in LLMs using conversational datasets that capture culturally rich and dialectal contexts. Most Arabic benchmarks focus on short text snippets in Modern Standard Arabic (MSA), overlooking the cultural nuances that naturally arise in dialogues. To address this gap, we introduce ArabCulture-Dialogue, a culturally grounded conversational dataset covering 13 Arabic-speaking countries, in both MSA and each country's respective dialect, spanning 12 daily-life topics and 54 fine-grained subtopics. We utilize the dataset to form three benchmarking tasks: (i) multiple-choice cultural reasoning, (ii) machine translation between MSA and dialects, and (iii) dialect-steering generation. Our experiments indicate that the performance gap between MSA and Arabic dialects still exists, whereby the models perform worse on all three tasks in the dialectal setup, compared to the MSA one.

---


### 7. [Minimal, Local, Causal Explanations for Jailbreak Success in Large Language Models](https://arxiv.org/abs/2605.00123)

**<font color=#1a73e8>作者：</font>** Shubham Kumar, Narendra Ahuja  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety trained large language models (LLMs) can often be induced to answer harmful requests through jailbreak prompts. Because we lack a robust understanding of why LLMs are susceptible to jailbreaks, future frontier models operating more autonomously in higher-stakes settings may similarly be vulnerable to such attacks. Prior work has studied jailbreak success by examining the model's intermediate representations, identifying directions in this space that causally encode concepts like harmfulness and refusal. Then, they globally explain all jailbreak attacks as attempting to reduce or strengthen these concepts (e.g., reduce harmfulness). However, different jailbreak strategies may succeed by strengthening or suppressing different intermediate concepts, and the same jailbreak strategy may not work for different harmful request categories (e.g., violence vs. cyberattack); thus, we seek to give a local explanation -- i.e., why did this specific jailbreak succeed? To address this gap, we introduce LOCA, a method that gives Local, CAusal explanations of jailbreak success by identifying a minimal set of interpretable, intermediate representation changes that causally induce model refusal on an otherwise successful jailbreak request. We evaluate LOCA on harmful original-jailbreak pairs from a large jailbreak benchmark across Gemma and Llama chat models, comparing against prior methods adapted to this setting. LOCA can successfully induce refusal by making, on average, six interpretable changes; prior work routinely fails to achieve refusal even after 20 changes. LOCA is a step toward mechanistic, local explanations of jailbreak success in LLMs. Code to be released.

---


### 8. [Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents](https://arxiv.org/abs/2605.00136)

**<font color=#1a73e8>作者：</font>** Kaituo Zhang, Zhen Xiong, Mingyu Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented reasoning has become a popular direction for LLM-based agents, and it is widely assumed to improve reasoning and reliability. However, we demonstrate that this consensus does not always hold: in the presence of semantic distractors, tool-augmented reasoning does not necessarily outperform native CoT. To explain this performance gap, we propose a Factorized Intervention Framework that isolates the cost of prompt formatting, the overhead of the tool-calling protocol, and the actual gain from executing tools. Our analysis reveals a critical tradeoff: under semantic noise, the gains from tools often fail to offset the "tool-use tax", which is the performance degradation introduced by the tool-calling protocol itself. To address this, we introduce G-STEP, a lightweight inference-time gate to mitigate protocol-induced errors. While this yields partial recovery, our findings suggest that more substantial improvements still require strengthening the model's intrinsic reasoning and tool-interaction capabilities.

---


### 9. [Technical Report: Activation Residual Hessian Quantization (ARHQ) for Low-Bit LLM Quantization](https://arxiv.org/abs/2605.00140)

**<font color=#1a73e8>作者：</font>** YiFeng Wang, Zhun Sun, Keisuke Sakaguchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Activation Residual Hessian Quantization (ARHQ), a post-training weight splitting method designed to mitigate error propagation in low-bit activation-weight quantization. By constructing an input-side residual Hessian from activation quantization residuals (G_x), ARHQ analytically identifies and isolates error-sensitive weight directions into a high-precision low-rank branch. This is achieved via a closed-form truncated SVD on the scaled weight matrix W G^{1/2}_x . Experimental results on Qwen3-4B-Thinking-2507 demonstrate that ARHQ significantly improves layer-wise SNR and preserves downstream reasoning performance on ZebraLogic even under aggressive quantization. The code is available at this https URL.

---


### 10. [Wasserstein Distributionally Robust Regret Optimization for Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2605.00155)

**<font color=#1a73e8>作者：</font>** Yikai Wang, Shang Liu, Jose Blanchet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) has become a core post-training step for aligning large language models, yet the reward signal used in RLHF is only a learned proxy for true human utility. From an operations research perspective, this creates a decision problem under objective misspecification: the policy is optimized against an estimated reward, while deployment performance is determined by an unobserved objective. The resulting gap leads to reward over-optimization, or Goodharting, where proxy reward continues to improve even after true quality deteriorates. Existing mitigations address this problem through uncertainty penalties, pessimistic rewards, or conservative constraints, but they can be computationally burdensome and overly pessimistic. We propose Wasserstein distributionally robust regret optimization (DRRO) for RLHF. Instead of pessimizing worst-case value as in standard DRO, DRRO pessimizes worst-case regret relative to the best policy under the same plausible reward perturbation. We study the promptwise problem through a simplex allocation model and show that, under an $\ell_1$ ambiguity set, the inner worst-case regret admits an exact solution and the optimal policy has a water-filling structure. These results lead to a practical policy-gradient algorithm with a simple sampled-bonus interpretation and only minor changes to PPO/GRPO-style RLHF training. The framework also clarifies theoretically why DRRO is less pessimistic than DRO, and our experiments show that DRRO mitigates over-optimization more effectively than existing baselines while standard DRO is systematically over-pessimistic.

---


### 11. [Consistent Diffusion Language Models](https://arxiv.org/abs/2605.00161)

**<font color=#1a73e8>作者：</font>** Hasan Amin, Yuan Gao, Yaser Souri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) are an attractive alternative to autoregressive models because they promise sublinear-time, parallel generation, yet practical gains remain elusive as high-quality samples still demand hundreds of refinement steps. In continuous domains, consistency training along the probability-flow ODE is a popular recipe to accelerate diffusion. For discrete diffusion, no analogous sample-space ODE exists, making direct adaptation ill-defined. We argue that the natural discrete substitute is not a deterministic trajectory but its stochastic counterpart: the exact posterior bridge, available in closed form for broad corruption families including masked and uniform diffusion. Building on this observation, we introduce Multi-Path Discrete Consistency (MPDC), a new principle that trains a denoiser to be path-invariant in expectation across these stochastic bridges, and instantiate it as the Consistent Diffusion Language Model (CDLM), a single-stage, teacher-free training framework. A single CDLM objective unifies masked diffusion, continuous consistency models, and progressive/discrete distillation as analytic limits or empirical approximations of one common view. Empirically, CDLM establishes a new state of the art on both conditional and unconditional text-generation, consistently outperforming strong base discrete diffusion models and often even multi-stage distilled baselines across sampling budgets, with the largest gains in the few-step regime. Together, these results position CDLM as a principled and scalable foundation for the next generation of fast, high-fidelity discrete generative modeling.

---


### 12. [Introducing WARM-VR: Benchmark Dataset for Multimodal Wearable Affect Recognition in Virtual Reality](https://arxiv.org/abs/2605.00184)

**<font color=#1a73e8>作者：</font>** Karim Alghoul, Faisal Mohd, Fedwa Laamarti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the growing integration of human-computer interaction into everyday life, advances in machine learning have enabled systems to better perceive and respond to users' emotional states. Most existing affect recognition datasets focus on static environments, limiting their applicability to immersive multimedia contexts such as Virtual Reality (VR). In this paper, we introduce WARM-VR, a novel publicly available multimodal dataset designed to support affect recognition in immersive, multisensory environments using wearable sensing instrumentation. Data were collected from 31 participants aged 19-37 using wearable sensors: a wristband measuring Blood Volume Pulse (BVP), EDA, skin Temperature, three-axis Acceleration, and a chest strap recording ECG signals. Participants engaged in immersive VR experiences designed to elicit relaxation through a calming beach environment following stress induction via an arithmetic task. These sessions incorporated synchronized multimedia stimuli: visual, auditory, and olfactory. Affective states were assessed subjectively through validated self-report questionnaires and objectively through the analysis of physiological measurements. Statistical analysis of the questionnaires confirmed that VR relaxation significantly reduced negative affect, particularly with olfactory enhancement. Furthermore, we established a benchmark on the dataset using widely recognized machine learning algorithms. The best performance for binary classification from BVP data of valence, was obtained with a CNN and a CNN-Bi-GRU model, both achieving an average F1-score of 0.63 and an AUC of 0.69. For arousal, a lightweight Transformer architecture provided the most balanced results (F1-0 0.54 and F1-1 0.63), outperforming recurrent hybrids. In the relaxation task, a CNN-Bi-GRU model reached the highest overall performance (average F1-score 0.64, AUC 0.69).

---


### 13. [Diversity in Large Language Models under Supervised Fine-Tuning](https://arxiv.org/abs/2605.00195)

**<font color=#1a73e8>作者：</font>** Roman Klypa, Oleksandr Cherednichenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised Fine-Tuning (SFT) is essential for aligning Large Language Models (LLMs) with user intent, yet it is believed to suppress generative diversity. Although this reduction is frequently referenced, formal empirical testing of the phenomenon remains limited. The expressiveness of LLMs by itself was addressed by multiple prior methods. Their varying perspectives suggest that deeper analysis could yield further improvements. In this study, we attribute the decline to two primary drivers: the neglect of low-frequency patterns within fine-tuning datasets and the forgetting of preexisting knowledge. Motivated by our theoretical analysis, we develop Tempered Focal (TOFU) loss, a novel objective that addresses both stated challenges simultaneously. Our extensive evaluation confirms at scale that generation breadth narrows after SFT and strengthens the hypothesis explaining this effect. Across multiple models and benchmarks, we demonstrate that TOFU enhances output diversity while preserving high response quality, offering a principled approach to SFT.

---


### 14. [The $\textit{Silicon Society}$ Cookbook: Design Space of LLM-based Social Simulations](https://arxiv.org/abs/2605.00197)

**<font color=#1a73e8>作者：</font>** Aurélien Bück-Kaeffer, Sneheel Sarangi, Maximilian Puelma Touzel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Studies attempting to simulate human behavior with $\textit{Silicon Societies}$ grow in numbers while LLM-only social networks have started appearing outside of controlled settings. However, the design space of these networks remains under-studied, which contributes to a gap in validating model realism. To enable future works to make more informed design decisions, we perform a systematic analysis of the consequences and interactions of key design choices in simulated social networks, including the choice of base model used to model individual agents, and how they are connected to each other. Using surveys as a proxy for agent opinions, our findings suggest that the geometry of the design space is non-trivial, with some parameters behaving in additive ways while others display more complex interactions. In particular, the choice of the base LLM is the most important variable impacting the simulation outcomes.

---


### 15. [RSAT: Structured Attribution Makes Small Language Models Faithful Table Reasoners](https://arxiv.org/abs/2605.00199)

**<font color=#1a73e8>作者：</font>** Jugal Gajjar, Kamalasankari Subramaniakuppusamy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model answers a table question, users have no way to verify which cells informed which reasoning steps. We introduce RSAT, a method that trains small language models (SLMs, 1-8B) to produce step-by-step reasoning with cell-level citations grounded in table evidence. Phase 1 (SFT) teaches a structured JSON output format from verified reasoning traces. Phase 2 (GRPO) optimizes a composite reward centered on NLI-based faithfulness, alongside citation validity and parsimony. Across six models from two families-Qwen 2.5 (1.5B/3B/7B) and Llama 3 (1B/3B/8B)-RSAT improves faithfulness 3.7$\times$ over SFT alone (0.224$\rightarrow$0.826), with near-perfect citation validity (0.992). Post-hoc attribution collapses below 13% format success, confirming that attribution must be integrated into reasoning, not retrofitted. Ablations show the faithfulness reward is essential: removing it drops faithfulness from 0.97 to 0.03.

---


### 16. [Confidence Estimation in Automatic Short Answer Grading with LLMs](https://arxiv.org/abs/2605.00200)

**<font color=#1a73e8>作者：</font>** Longwei Cong, Sonja Hahn, Sebastian Gombert 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Short Answer Grading (ASAG) with generative large language models (LLMs) has recently demonstrated strong performance without task-specific fine-tuning, while also enabling the generation of synthetic feedback for educational assessment. Despite these advances, LLM-based grading remains imperfect, making reliable confidence estimates essential for safe and effective human-AI collaboration in educational decision-making. In this work, we investigate confidence estimation for ASAG with LLMs by jointly considering model-based confidence signals and dataset-derived uncertainty. We systematically compare three model-based confidence estimation strategies, namely verbalizing, latent, and consistency-based confidence estimation, and show that model-based confidence alone is insufficient to reliably capture uncertainty in ASAG. To address this limitation, we propose a hybrid confidence framework that integrates model-based confidence signals with an explicit estimate of dataset-derived aleatoric uncertainty. Aleatoric uncertainty is operationalized by clustering semantically embedded student responses and quantifying within-cluster heterogeneity. Our results demonstrate that the proposed hybrid confidence measure yields more reliable confidence estimates and improves selective grading performance compared to single-source approaches. Overall, this work advances confidence-aware LLM-based grading for human-in-the-loop assessment, supporting more trustworthy AI-assisted educational assessment systems.

---


### 17. [TUR-DPO: Topology- and Uncertainty-Aware Direct Preference Optimization](https://arxiv.org/abs/2605.00224)

**<font color=#1a73e8>作者：</font>** Abdulhady Abas Abdullah, Fatemeh Daneshfar, Seyedali Mirjalili 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) with human preferences is commonly done via reinforcement learning from human feedback (RLHF) with Proximal Policy Optimization (PPO) or, more simply, via Direct Preference Optimization (DPO). While DPO is stable and RL-free, it treats preferences as flat winner vs. loser signals and is sensitive to noisy or brittle preferences arising from fragile chains of thought. We propose TUR-DPO, a topology- and uncertainty-aware variant of DPO that rewards how answers are derived, not only what they say, by eliciting lightweight reasoning topologies and combining semantic faithfulness, utility, and topology quality into a calibrated uncertainty signal. A small learnable reward is factorized over these signals and incorporated into an uncertainty-weighted DPO objective that remains RL-free and relies only on a fixed or moving reference policy. Empirically, across open 7-8B models and benchmarks spanning mathematical reasoning, factual question answering, summarization, and helpful/harmless dialogue, TUR-DPO improves judge win-rates, faithfulness, and calibration relative to DPO while preserving training simplicity and avoiding online rollouts. We further observe consistent gains in multimodal and long-context settings, and show that TUR-DPO matches or exceeds PPO on reasoning-centric tasks while maintaining operational simplicity.

---


### 18. [Why Do LLMs Struggle in Strategic Play? Broken Links Between Observations, Beliefs, and Actions](https://arxiv.org/abs/2605.00226)

**<font color=#1a73e8>作者：</font>** Jan Sobotka, Mustafa O. Karabag, Ufuk Topcu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly tasked with strategic decision-making under incomplete information, such as in negotiation and policymaking. While LLMs can excel at many such tasks, they also fail in ways that are poorly understood. We shed light on these failures by uncovering two fundamental gaps in the internal mechanisms underlying the decision-making of LLMs in incomplete-information games, supported by experiments with open-weight models Llama 3.1, Qwen3, and gpt-oss. First, an observation-belief gap: LLMs encode internal beliefs about latent game states that are substantially more accurate than their own verbal reports, yet these beliefs are brittle. In particular, the belief accuracy degrades with multi-hop reasoning, exhibits primacy and recency biases, and drifts away from Bayesian coherence over extended interactions. Second, a belief-action gap: The implicit conversion of internal beliefs into actions is weaker than that of the beliefs externalized in the prompt, yet neither belief-conditioning consistently achieves higher game payoffs. These results show how analyzing LLMs' internal processes can expose systematic vulnerabilities that warrant caution before deploying LLMs in strategic domains without robust guardrails.

---


### 19. [Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory](https://arxiv.org/abs/2605.00238)

**<font color=#1a73e8>作者：</font>** Longwei Cong, Sonja Hahn, Sebastian Gombert 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated short answer grading (ASAG) with large language models (LLMs) is commonly evaluated with aggregate metrics such as macro-F1 and Cohen's kappa. However, these metrics provide limited insight into how grading performance varies across student responses of differing grading difficulty. We introduce an evaluation framework for LLM-based ASAG based on item response theory (IRT), which models grading correctness as a function of latent grader ability and response grading difficulty. This formulation enables response-level analysis of where LLM graders succeed or fail and reveals robustness differences that are not visible from aggregate scores alone. We apply the framework to 17 open-weight LLMs on the SciEntsBank and Beetle benchmarks. The results show that even models with similar overall performance differ substantially in how sharply their grading accuracy declines as response difficulty increases. In addition, confusion patterns show that errors on difficult responses concentrate disproportionately on the \texttt{partially\_correct\_incomplete} label, indicating a tendency toward intermediate-label collapse under ambiguity. To characterize difficult responses, we further analyze semantic and linguistic correlates of estimated difficulty. Across both datasets, higher difficulty is associated with weaker semantic alignment to the reference answer, stronger contradiction signals, and greater semantic isolation in embedding space. Overall, these results show that item response theory offers a useful framework for evaluating LLM-based ASAG beyond aggregate performance measures.

---


### 20. [ARMOR 2025: A Military-Aligned Benchmark for Evaluating Large Language Model Safety Beyond Civilian Contexts](https://arxiv.org/abs/2605.00245)

**<font color=#1a73e8>作者：</font>** Sydney Johns, Heng Jin, Chaoyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are now being explored for defense applications that require reliable and legally compliant decision support. They also hold significant potential to enhance decision making, coordination, and operational efficiency in military contexts. These uses demand evaluation methods that reflect the doctrinal standards that guide real military operations. Existing safety benchmarks focus on general social risks and do not test whether models follow the legal and ethical rules that govern real military operations. To address this gap, we introduce ARMOR 2025, a military aligned safety benchmark grounded in three core military doctrines the Law of War, the Rules of Engagement, and the Joint Ethics Regulation. We extract doctrinal text from these sources and generate multiple choice questions that preserve the intended meaning of each rule. The benchmark is organized through a taxonomy informed by the Observe Orient Decide Act (OODA) decision making framework. This structure enables systematic testing of accuracy and refusal across military relevant decision types. This benchmark features a structured 12-category taxonomy, 519 doctrinally grounded prompts, and rigorous evaluation procedures applied to 21 commercial LLMs. Evaluation results reveal critical gaps in safety alignment for military applications.

---


### 21. [Retrieval-Augmented Reasoning for Chartered Accountancy](https://arxiv.org/abs/2605.00257)

**<font color=#1a73e8>作者：</font>** Jatin Gupta, Akhil Sharma, Saransh Singhania 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The inception of Large Language Models (LLMs) has catalyzed AI adoption in the finance sector, yet their reliability in complex, jurisdiction-specific tasks like Indian Chartered Accountancy (CA) remains limited. The models display difficulty in executing numerical tasks which require multiple steps while also needing advanced knowledge about legal regulations and the method of scaling their operations is not feasible in settings which have limited access to resources. We present CA-ThinkFlow as a parameter-efficient Retrieval-Augmented Generation (RAG) framework which operates with a 14B, 4-bit-quantized reasoning model, 14B-DeepSeek-R1, and a layout-aware Docling extraction system which maintains document structure during extraction. CA-ThinkFlow uses a basic RAG method which automatically adds retrieved information into the prompt, while it depends on the model's built-in Chain-of-Thought (CoT) functions to create context and produce correct answers. The system we developed system operates at performance levels which match large proprietary models when we tested it on the multi-level CA-Ben benchmark, achieving Scholastic Reliability Coefficient (SRC) results which equal 68.75\% of GPT-4o and Claude 3.5 Sonnet. The framework shows high efficiency and strength in handling parameters, but essential reasoning abilities fail to process complex regulatory texts which exist in fields such as Taxation.

---


### 22. [How Language Models Process Out-of-Distribution Inputs: A Two-Pathway Framework](https://arxiv.org/abs/2605.00269)

**<font color=#1a73e8>作者：</font>** Hamidreza Saghir  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent white-box OOD detection methods for LLMs -- including CED, RAUQ, and WildGuard confidence scores -- appear effective, but we show they are structurally confounded by sequence length (|r| >= 0.61) and collapse to near-chance under length-matched evaluation. Even raw attention entropy (mean H(alpha) across heads and layers), a natural baseline we include for completeness, shows the same confound. The confound stems from attention's Theta(log T) dependence on input length. To identify genuine OOD signals after deconfounding, we propose a two-pathway framework: embeddings capture what text is about (effective for topic shifts), while the processing trajectory -- hidden-state evolution across layers -- captures how the model processes input. The relative power of each pathway varies along a vocabulary-transparency spectrum: embedding methods excel on vocabulary-distinctive OOD, while trajectory features detect covert-intent inputs that share vocabulary with normal text (0.721 avg AUROC; Jailbreak: 0.850). Three evidence lines support this framework: (1) a crossover between k-NN and trajectory scoring across 6 tasks, where each pathway wins on different OOD types; (2) a per-layer analysis showing that layer-0 k-NN signal is almost entirely a length artifact (Jailbreak: 0.759 raw -> 0.389 matched) -- processing constructs genuine OOD signal from near-chance embeddings; and (3) circuit attribution showing adversarial tasks engage attention circuits more than semantic tasks (p = 0.022; Jailbreak patching p < 0.001), with partial cross-model replication. Code release upon publication.

---


### 23. [Agentic AI for Trip Planning Optimization Application](https://arxiv.org/abs/2605.00276)

**<font color=#1a73e8>作者：</font>** Tiejin Chen, Ahmadreza Moradipari, Kyungtae Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trip planning for intelligent vehicles increasingly requires selecting optimal routes rather than merely producing feasible itineraries, as interacting factors such as travel time, energy consumption, and traffic conditions directly affect plan quality. Yet existing systems are largely designed for feasibility-oriented planning, and current benchmarks provide only reference answers without ground truth, preventing objective evaluation of optimization performance. In our paper, we address these limitations with an agentic AI framework that enables dynamic refinement through an orchestration agent coordinating specialized agents for traffic, charging, and points of interest, and with the Trip-planning Optimization Problems Dataset, which supplies definitive optimal solutions and category-level task structure for fine-grained analysis. Experiments show that our system achieves 77.4\% accuracy on the TOP Benchmark, significantly outperforming single-agent and workflow-based multi-agent baselines, demonstrating the importance of orchestrated agentic reasoning for robust trip planning optimization.

---


### 24. [What Don't You Understand? Using Large Language Models to Identify and Characterize Student Misconceptions About Challenging Topics](https://arxiv.org/abs/2605.00294)

**<font color=#1a73e8>作者：</font>** Michael J. Parker, Maria G. Zavala-Cerna  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study presents a systematic approach to identifying and characterizing student misconceptions in online learning environments through a novel combination of quantitative performance analysis and large language model (LLM) assessment. We analyzed data from 9 course periods across 5 online biomedical science courses, encompassing 3,802 medical student enrollments. Using data from 40-50 topic-focused quizzes per course, we developed a two-stage methodology. First, we identified challenging central topics using quiz-level performance metrics. Second, we employed LLMs to characterize the underlying misconceptions in these high-priority areas. By examining student performance on first attempts across primarily multiple-choice questions (MCQs), we identified consistently challenging topics that were also central to course objectives. We then leveraged recent advances in generative AI to analyze three distinct data sources in combination: quiz question content, student response patterns, and lecture transcripts. This approach revealed actionable insights about student misconceptions that were not apparent from performance data alone. The quality of the LLM-identified misconceptions was rated as excellent by subject matter experts. We also conducted teacher interviews to assess the perceived utility of our topic identification method. Faculty found that data-driven identification of challenging topics was valuable and corroborated their own classroom observations. This methodology provides a scalable approach to characterizing student difficulties in learning environments where quizzes are used. Our findings demonstrate the potential for targeted and potentially personalized interventions in future course iterations, with clear pathways for measuring intervention effectiveness through follow-up quiz performance.

---


### 25. [Online Self-Calibration Against Hallucination in Vision-Language Models](https://arxiv.org/abs/2605.00323)

**<font color=#1a73e8>作者：</font>** Minghui Chen, Chenxu Yang, Hengjie Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) often suffer from hallucinations, generating descriptions that include visual details absent from the input image. Recent preference alignment methods typically rely on supervision distilled from stronger models such as GPT. However, this offline paradigm introduces a Supervision-Perception Mismatch: the student model is forced to align with fine-grained details beyond its perceptual capacity, learning to guess rather than to see. To obtain reliable self-supervision for online learning, we identify a Generative-Discriminative Gap within LVLMs, where models exhibit higher accuracy on discriminative verification than open-ended generation. Leveraging this capability, we propose \textbf{O}nline \textbf{S}elf-\textbf{CA}lib\textbf{R}ation (OSCAR), a framework that integrates Monte Carlo Tree Search with a Dual-Granularity Reward Mechanism to construct preference data and iteratively refines the model via Direct Preference Optimization. Extensive experiments demonstrate that OSCAR achieves state-of-the-art performance on hallucination benchmarks while improving general multimodal capabilities.

---


### 26. [Prompt-Induced Score Variance in Zero-Shot Binary Vision-Language Safety Classification](https://arxiv.org/abs/2605.00326)

**<font color=#1a73e8>作者：</font>** Charles Weng, Dingwen Li, Alexander Martin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Single-prompt first-token probabilities from zero-shot vision-language model (VLM) safety classifiers are treated as decision scores, but we show they are unreliable under semantically equivalent prompt reformulation: even when the binary label is constrained to a fixed output position, equivalent prompts can induce materially different unsafe probabilities for the same sample. Across multimodal safety benchmarks and multiple VLM families, cross-prompt variance is strongly associated with prompt-level disagreement and higher error, making it a useful fragility diagnostic. A training-free mean ensemble improves NLL on all 14 dataset-model evaluation pairs and ECE on 12/14 relative to a train-selected single-prompt baseline, and wins more head-to-head NLL comparisons than labeled temperature scaling, Platt scaling, and isotonic regression applied to the same prompt. Ranking gains are consistent against the train-selected baseline on both AUROC and AUPRC, and against the full 15-prompt distribution remain consistent on AUPRC while softening on AUROC. Labeled calibration on top of the mean provides further gains when labels are available, identifying prompt averaging as a strong label-free first stage rather than a replacement for calibration. We frame this as a reliability stress test for zero-shot VLM first-token safety scores and recommend prompt-family evaluation with mean aggregation as a standard label-free reliability baseline.

---


### 27. [AgentFloor: How Far Up the tool use Ladder Can Small Open-Weight Models Go?](https://arxiv.org/abs/2605.00334)

**<font color=#1a73e8>作者：</font>** Ranit Karmakar, Jayita Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production agentic systems make many model calls per user request, and most of those calls are short, structured, and routine. This raises a practical routing question that existing evaluations do not directly answer: which parts of an agent workflow truly require large frontier intelligence, and which can be handled by smaller models? We introduce AgentFloor, a deterministic 30-task benchmark organized as a six-tier capability ladder, spanning instruction following, tool use, multi-step coordination, and long-horizon planning under persistent constraints. We evaluate 16 open-weight models, from 0.27B to 32B parameters, alongside GPT-5 across 16,542 scored runs. Our results reveal a clear boundary of model necessity. Small and mid-sized open-weight models are already sufficient for much of the short-horizon, structured tool use work that dominates real agent pipelines, and in aggregate, the strongest open-weight model matches GPT-5 on our benchmark while being substantially cheaper and faster to run. The gap appears most clearly on long-horizon planning tasks that require sustained coordination and reliable constraint tracking over many steps, where frontier models still hold an advantage, though neither side reaches strong reliability. We also find that this boundary is not explained by scale alone: some failures respond to targeted interventions, but the effects are model-specific rather than universal. These findings suggest a practical design principle for agentic systems: use smaller open-weight models for the broad base of routine actions, and reserve large frontier models for the narrower class of tasks that truly demand deeper planning and control. We release the benchmark, harness, sweep configurations, and full run corpus.

---


### 28. [Budget-Aware Routing for Long Clinical Text](https://arxiv.org/abs/2605.00336)

**<font color=#1a73e8>作者：</font>** Khizar Qureshi, Geoffrey Martin, Yifan Peng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A key challenge for large language models is token cost per query and overall deployment cost. Clinical inputs are long, heterogeneous, and often redundant, while downstream tasks are short and high stakes. We study budgeted context selection, where a subset of document units is chosen under a strict token budget so an off-the-shelf generator can meet fixed cost and latency constraints. We cast this as a knapsack-constrained subset selection problem with two design choices, unitization that defines document segmentation and selection that determines which units are kept.
We propose \textbf{RCD}, a monotone submodular objective that balances relevance, coverage, and diversity. We compare sentence, section, window, and cluster-based unitization, and introduce a routing heuristic that adapts to the budget regime. Experiments on MIMIC discharge notes, Cochrane abstracts, and L-Eval show that optimal strategies depend on the evaluation setting. Positional heuristics perform best at low budgets in extractive tasks, while diversity-aware methods such as MMR improve LLM generation. Selector choice matters more than unitization, with cluster-based grouping reducing performance and other schemes behaving similarly. ROUGE saturates for LLM summaries, while BERTScore better reflects quality differences. We release our code at this https URL.

---


### 29. [Making Every Verified Token Count: Adaptive Verification for MoE Speculative Decoding](https://arxiv.org/abs/2605.00342)

**<font color=#1a73e8>作者：</font>** Lehan Pan, Ziyang Tao, Ruoyu Pang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tree-based speculative decoding accelerates autoregressive generation by verifying multiple draft candidates in parallel, but this advantage weakens for sparse Mixture-of-Experts (MoE) models. As the draft tree grows, different branches activate different experts, expanding the union of activated experts and substantially increasing target-side verification cost. We propose EVICT, a training-free, hyperparameter-free, and lossless adaptive verification method for MoE speculative decoding. EVICT makes every verified token count by truncating the draft tree before target verification and retaining only the cost-effective prefix. It leverages fine-grained drafter signals to estimate candidate benefit, combines them with offline-profiled verification cost, and remains highly compatible with the high-performance graph-based serving framework SGLang. Extensive experiments on diverse MoE backbones and benchmarks show that EVICT achieves up to 2.35x speedup over autoregressive decoding and an average 1.21x speedup over the state-of-the-art baseline EAGLE-3, while significantly reducing unnecessary expert activations during verification.

---


### 30. [Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning](https://arxiv.org/abs/2605.00347)

**<font color=#1a73e8>作者：</font>** Chengshuai Shi, Wenzhe Li, Xinran Liang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given the rapidly growing capabilities of vision-language models (VLMs), extending them to interactive decision-making tasks such as video games has emerged as a promising frontier. However, existing approaches either rely on large-scale supervised fine-tuning (SFT) on human trajectories or apply reinforcement learning (RL) only in relatively short-horizon settings (typically around 20--30 turns). In this work, we study RL-based training of VLMs for long-horizon decision-making in Super Mario Land, a visually grounded environment requiring 100+ turns of interaction with coordinated perception, reasoning, and action. We begin with a systematic investigation of key algorithmic components and propose an adapted variant of PPO with a lightweight turn-level critic, which substantially improves training stability and sample efficiency over critic-free methods such as GRPO and Reinforce++. We further show that pretrained VLMs provide strong action priors, significantly improving sample efficiency during RL training and reducing the need for manual design choices such as action engineering, compared to classical deep RL trained from scratch. Building on these insights, we introduce Odysseus, an open training framework for VLM agents, achieving substantial gains across multiple levels of the game and at least 3 times average game progresses than frontier models. Moreover, the trained models exhibit consistent improvements under both in-game and cross-game generalization settings, while maintaining general-domain capabilities. Overall, our results identify key ingredients for making RL stable and effective in long-horizon, multi-modal settings, and provide practical guidance for developing VLMs as embodied agents.

---


### 31. [Hypergraph and Latent ODE Learning for Multimodal Root Cause Localization in Microservices](https://arxiv.org/abs/2605.00351)

**<font color=#1a73e8>作者：</font>** Xin Liu, Yuhang He, Sichen Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Root cause localization in cloud native microservice systems requires modeling complex service dependencies, irregular temporal dynamics, and heterogeneous observability data. We present HyperODE RCA, a unified framework that combines hypergraph attention learning, latent ordinary differential equations, and multimodal cross attention fusion for fine grained root cause analysis. The method learns higher order service interactions through differentiable hyperedge construction, captures continuous anomaly evolution from irregular observations with an ODE RNN encoder, and adaptively fuses logs, traces, metrics, entities, and events using context aware modality routing. We further improve robustness with a variational information bottleneck, temporal causal regularization, and invariant risk constraints. Experiments on the Tianchi AIOps benchmark show clear gains over strong baselines in ranking and classification performance, while preserving interpretability through learned hypergraph attention.

---


### 32. [From Backward Spreading to Forward Replay: Revisiting Target Construction in LLM Parameter Editing](https://arxiv.org/abs/2605.00358)

**<font color=#1a73e8>作者：</font>** Wei Liu, Hongkai Liu, Zhiying Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM parameter editing methods commonly rely on computing an ideal target hidden-state at a target layer (referred as anchor point) and distributing the target vector to multiple preceding layers (commonly known as backward spreading) for cooperative editing. Although widely used for a long time, its underlying basis have not been systematically investigated. In this paper, we first conduct a systematic study of its foundations, which helps clarify its capability boundaries, practical considerations, and potential failure modes. Then, we propose a simple and elegant alternative that replaces backward spreading with forward-propagation. Instead of optimizing the target at the last editing layer, we optimize the anchor point at the first editing layer, and then propagate it forward to obtain accurate and mutually compatible target hidden-states for all subsequent editing layers. This approach achieves the same computational complexity as existing methods while producing more accurate layer-wise targets. Our method is simple, without interfering with either the computation of the initial target hidden state or any other components of the subsequent editing pipeline, and thus constituting a benefit for a wide range of LLM parameter editing methods.

---


### 33. [Unlearning What Matters: Token-Level Attribution for Precise Language Model Unlearning](https://arxiv.org/abs/2605.00364)

**<font color=#1a73e8>作者：</font>** Jiawei Wu, DouDou Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning has emerged as a critical capability for addressing privacy, safety, and regulatory concerns in large language models (LLMs). Existing methods operate at the sequence level, applying uniform updates across all tokens despite only a subset encoding the knowledge targeted for removal. This introduces gradient noise, degrades utility, and leads to suboptimal forgetting. We propose TokenUnlearn, a token-level attribution framework that identifies and selectively targets critical tokens. Our approach combines knowledge-aware signals via masking, and entropy-aware signals to yield importance scores for precise token selection. We develop two complementary strategies: hard selection, applying unlearning only to high-importance tokens, and soft weighting, modulating gradient contributions based on importance scores. Both extend existing methods to token-level variants. Theoretical analysis shows token-level selection improves gradient signal-to-noise ratio. Experiments on TOFU and WMDP benchmarks across three model architectures demonstrate consistent improvements over sequence-level baselines in both forgetting effectiveness and utility preservation.

---


### 34. [AlphaInventory: Evolving White-Box Inventory Policies via Large Language Models with Deployment Guarantees](https://arxiv.org/abs/2605.00369)

**<font color=#1a73e8>作者：</font>** Chenyu Huang, Jianghao Lin, Zhengyang Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how large language models can be used to evolve inventory policies in online, non-stationary environments. Our work is motivated by recent advances in LLM-based evolutionary search, such as AlphaEvolve, which demonstrates strong performance for static and highly structured problems such as mathematical discovery, but is not directly suited to online dynamic inventory settings. To this end, we propose AlphaInventory, an end-to-end inventory-policy evolution and inference framework grounded in confidence-interval-based certification. The framework trains a large language model using reinforcement learning, incorporates demand data as well as numerical and textual features beyond demand, and generates white-box inventory policy with statistical safety guarantees for deployment in future periods. We further introduce a unified theoretical interface that connects training, inference, and deployment. This allows us to characterize the probability that the AlphaInventory evolves a statistically safe and improved policy, and to quantify the deployment gap relative to the oracle-safe benchmark. Tested on both synthetic data and real-world retail data, AlphaInventory outperforms classical inventory policies and deep learning based methods. In canonical inventory settings, it evolves new policies that improve upon existing benchmarks.

---


### 35. [ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning](https://arxiv.org/abs/2605.00380)

**<font color=#1a73e8>作者：</font>** Zihan Lin, Xiaohan Wang, Jie Cao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) enhances reasoning of Large Language Models (LLMs) but usually exhibits limited generation diversity due to the over-incentivization of positive rewards. Although methods like Negative Sample Reinforcement (NSR) mitigate this issue by upweighting penalty from negative samples, they may suppress the semantic distributions shared between positive and negative responses. To boost reasoning ability without losing diversity, this paper proposes negative sample projection Residual Reinforcement Learning (ResRL) that decouples similar semantic distributions among positive and negative responses. We theoretically link Lazy Likelihood Displacement (LLD) to negative-positive head-gradient interference and derive a single-forward proxy that upper-bounds representation alignment to guide conservative advantage reweighting. ResRL then projects negative-token hidden representations onto an SVD-based low-rank positive subspace and uses projection residuals to modulate negative gradients, improving reasoning while preserving diversity and outperforming strong baselines on average across twelve benchmarks spanning Mathematics, Code, Agent Tasks, and Function Calling. Notably, ResRL surpasses NSR on mathematical reasoning by 9.4\% in Avg@16 and 7.0\% in Pass@128. Code is available at this https URL.

---


### 36. [Agentic AI for Substance Use Education: Integrating Regulatory and Scientific Knowledge Sources](https://arxiv.org/abs/2605.00383)

**<font color=#1a73e8>作者：</font>** Kosar Haghani, Zahra Kolagar, Mohammed Atiquzzaman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The delivery of traditional substance education has remained problematic due to challenges in scalability, personalization, and the currency of information in a rapidly evolving substance use landscape. While artificial intelligence (AI) offers a promising frontier for enhancing educational delivery, its application in providing real-time, authoritative substance use education remains largely underexplored. We built an agentic-based AI web application that combined Drug Enforcement Administration records with peer-reviewed literature in real-time to provide transparent context-sensitive substance use education. The system uses retrieval-augmented generation with a carefully filtered corpus of 102 documents and dynamic PubMed queries. Document storage was semantically chunked and placed in a vector representation in order to be easily retrieved. We conducted an expert evaluation study in which a panel of five subject matter experts generated 30 domain-specific questions, and two independent raters assessed 90 system interactions (30 primary questions plus two contextual follow-ups each) using a five-point Likert scale across four criteria: factual accuracy, citation quality, contextual coherence, and regulatory appropriateness. Mean ratings ranged from 4.18 to 4.35 across the four criteria (overall category range: 4.05-4.52), with substantial inter-rater agreement (Cohen's kappa = 0.78). These findings suggest that agentic AI architectures integrating authoritative regulatory sources with real-time scientific literature represent a promising direction for scalable, accurate, and verifiable health education delivery, warranting further evaluation through longitudinal user studies.

---


### 37. [RTPrune: Reading-Twice Inspired Token Pruning for Efficient DeepSeek-OCR Inference](https://arxiv.org/abs/2605.00392)

**<font color=#1a73e8>作者：</font>** Ben Wan, Yan Feng, Zihan Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> DeepSeek-OCR leverages visual-text compression to reduce long-text processing costs and accelerate inference, yet visual tokens remain prone to redundant textual and structural information. Moreover, current token pruning methods for conventional vision-language models (VLMs) fail to preserve textual fidelity due to improper compression mechanisms. By analyzing the decoding process of DeepSeek-OCR, we find that a distinct two-stage reading trajectory: the model initially prioritizes the majority of high-norm tokens, then subsequently redistributes its attention to the remaining ones. Motivated by this insight, we propose RTPrune, a two-stage token pruning method tailored for DeepSeek-OCR. In the first stage, we prioritize high-norm visual tokens that capture salient textual and structural information. In the second stage, the remaining tokens are paired and merged based on optimal transport theory to achieve efficient feature aggregation. We further introduce a dynamic pruning ratio that adapts to token similarity and textual density for OCR tasks, enabling a better efficiency-accuracy trade-off. Extensive experiments demonstrate state-of-the-art performance, as evidenced by 99.47% accuracy and 1.23$\times$ faster prefill on OmniDocBench, achieved with 84.25% token retention when applied to DeepSeek-OCR-Large.

---


### 38. [Agent Capsules: Quality-Gated Granularity Control for Multi-Agent LLM Pipelines](https://arxiv.org/abs/2605.00410)

**<font color=#1a73e8>作者：</font>** Aninda Ray  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A multi-agent pipeline with N agents typically issues N LLM calls per run. Merging agents into fewer calls (compound execution) promises token savings, but naively merged calls silently degrade quality through tool loss and prompt compression. We present Agent Capsules, an adaptive execution runtime that treats multi-agent pipeline execution as an optimization problem with empirical quality constraints. The runtime instruments coordination overhead per group, scores composition opportunity, selects among three compound execution strategies, and gates every mode switch on rolling-mean output quality. A controlled negative result confirms that injecting more context into a merged call worsens compression rather than relieving it, so the framework's escalation ladder (standard, then two-phase, then sequential) recovers quality by moving toward per-agent dispatch rather than by rewriting merged prompts. On LLM-judged quality, the controller matches a hand-tuned oracle on every measured (model, group, mode) cell: routing compound whenever the oracle would, and reverting to fine whenever quality would fail the floor, without per-model configuration. Against a hand-crafted LangGraph implementation of a 14-agent competitive intelligence pipeline, Agent Capsules uses 51% fewer fine-mode input tokens and 42% fewer compound-mode input tokens, at +0.020 and +0.017 quality respectively. Against a DSPy implementation of a 5-agent due diligence pipeline, the framework uses 19% fewer tokens than uncompiled DSPy at quality parity, and 68% fewer tokens than MIPROv2 at +0.052 quality. Even before compound mode fires, the runtime delivers efficiency through automatic policy resolution, cache-aligned prompts, and topology-aware context injection, matching both hand-tuned and compile-time baselines without training data or per-pipeline engineering.

---


### 39. [Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling](https://arxiv.org/abs/2605.00412)

**<font color=#1a73e8>作者：</font>** Sen Cui, Jingheng Ma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models have recently re-emerged as a central paradigm for embodied intelligence, robotics, autonomous driving, and model-based reinforcement learning. However, current world model research is often dominated by three partially separated routes: 2D video-generative models that emphasize visual future synthesis, 3D scene-centric models that emphasize spatial reconstruction, and JEPA-like latent models that emphasize abstract predictive representations. While each route has made important progress, they still struggle to provide physically reliable, action-controllable, and long-horizon stable predictions for embodied decision making. In this paper, we argue that the bottleneck of world models is no longer only whether they can generate realistic futures, but whether those futures are physically meaningful and useful for action. We propose \emph{Hamiltonian World Models} as a physically grounded perspective on world modeling. The key idea is to encode observations into a structured latent phase space, evolve the latent state through Hamiltonian-inspired dynamics with control, dissipation, and residual terms, decode the predicted trajectory into future observations, and use the resulting rollouts for planning. We discuss how Hamiltonian structure may improve interpretability, data efficiency, and long-horizon stability, while also noting practical challenges in real-world robotic scenes involving friction, contact, non-conservative forces, and deformable objects.

---


### 40. [Rethinking LLM Ensembling from the Perspective of Mixture Models](https://arxiv.org/abs/2605.00419)

**<font color=#1a73e8>作者：</font>** Jiale Fu, Yuchu Jiang, Peijun Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model ensembling is a well-established technique for improving the performance of machine learning models. Conventionally, this involves averaging the output distributions of multiple models and selecting the most probable label. This idea has been naturally extended to large language models (LLMs), yielding improved performance but incurring substantial computational cost. This inefficiency stems from directly applying conventional ensemble implementation to LLMs, which require a separate forward pass for each model to explicitly compute the ensemble distribution. In this paper, we propose the Mixture-model-like Ensemble (ME). By reinterpreting the ensemble as a mixture model, ME stochastically selects a single model at each step to generate the next token, thereby avoiding the need to explicitly compute the full ensemble distribution. ME is mathematically equivalent to sampling from the ensemble distribution, but requires invoking only one model, making it 1.78x-2.68x faster than conventional ensemble. Furthermore, this perspective connects LLM ensembling and token-level routing methods, suggesting that LLM ensembling is a special case of routing methods. Our findings open new avenues for efficient LLM ensembling and motivate further exploration of token-level routing strategies for LLMs. Our code is available at this https URL.

---


### 41. [RadLite: Multi-Task LoRA Fine-Tuning of Small Language Models for CPU-Deployable Radiology AI](https://arxiv.org/abs/2605.00421)

**<font color=#1a73e8>作者：</font>** Pankaj Gupta, Kartik Bose  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show promise in radiology but their deployment is limited by computational requirements that preclude use in resource-constrained clinical environments. We investigate whether small language models (SLMs) of 3-4 billion parameters can achieve strong multi-task radiology performance through LoRA fine-tuning, enabling deployment on consumer-grade CPUs. We train Qwen2.5-3B-Instruct and Qwen3-4B on 162K samples spanning 9 radiology tasks - RADS classification across 10 systems, impression generation, temporal comparison, radiology NLI, NER, abnormality detection, N/M staging, and radiology Q&A - compiled from 12 public datasets. Both models are evaluated on up to 500 held-out test samples per task with standardized metrics. Our key findings are: (1) LoRA fine-tuning dramatically improves performance over zero-shot baselines (RADS accuracy +53%, NLI +60%, N-staging +89%); (2) the two models exhibit complementary strengths - Qwen2.5 excels at structured generation tasks while Qwen3 dominates extractive tasks; (3) a task-outed oracle ensemble combining both models achieves the best performance across all tasks; (4) few-shot prompting with fine-tuned models hurts performance, demonstrating that LoRA adaptation is more effective than in-context learning for specialized domains; and (5) models can be quantized to GGUF format (~1.8-2.4GB) for CPU deployment at 4-8 tokens/second on consumer hardware. Our work demonstrates that small, efficiently fine-tuned models - which we collectively call RadLite - can serve as practical multi-task radiology AI assistants deployable entirely on consumer hardware without GPU requirements.

---


### 42. [BWLA: Breaking the Barrier of W1AX Post-Training Quantization for LLMs](https://arxiv.org/abs/2605.00422)

**<font color=#1a73e8>作者：</font>** Zhixiong Zhao, Zukang Xu, Dawei Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have driven major progress in NLP, yet their substantial memory and compute demands still hinder practical deployment. Binarization can compress weights to 1 bit, fundamentally lowering compute and bandwidth cost. However, existing methods cannot address activation heavy tails and thus must keep activations in high precision, preventing true end-to-end acceleration. To overcome this limitation, we propose BWLA (Binarized Weights and Low-bit Activations), the first post-training quantization framework that preserves high accuracy while achieving 1-bit weight quantization together with low-bit activations (e.g., 6 bits). The Orthogonal-Kronecker Transformation (OKT) learns an orthogonal mapping via EM minimization, converting unimodal weights into symmetric bimodal forms while suppressing activation tails and incoherence. The Proximal SVD Projection (PSP) then performs lightweight low-rank refinement through proximal SVD projection, further enhancing quantizability with minimal overhead. On Qwen3-32B, BWLA reaches a Wikitext2 perplexity of 11.92 under 6-bit activations (vs. 38 from SOTA), improves five zero-shot tasks by more than 70%, and delivers 3.26 times inference speedup, demonstrating strong potential for real-world LLM compression and acceleration.

---


### 43. [AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.00425)

**<font color=#1a73e8>作者：</font>** Haotian Zhao, Yuxin Zhang, Songlin Zhou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has significantly advanced the ability of large language model (LLM) agents to interact with environments and solve multi-turn tasks. Yet effective training remains challenging, as sparse, outcome-only rewards make it difficult to assign credit to individual steps in an agent's action trajectory. A common remedy is to introduce dense intermediate supervision, such as process reward models or auxiliary self-supervised signals, but this increases supervision and tuning complexity and often generalizes poorly across tasks and domains. This paper presents AEM, a supervision-free credit assignment method that adaptively modulates entropy dynamics during RL training to achieve a more effective exploration-exploitation trade-off. Theoretically, we elevate entropy analysis from the token level to the response level to reduce token sampling variance and show that entropy drift under natural gradients is intrinsically governed by the product of the advantage and the relative response surprisal. Specifically, we derive a practical proxy to reshape training dynamics, enabling a natural transition from exploration to exploitation. Extensive experiments across various benchmarks and models ranging from 1.5B to 32B parameters demonstrate the effectiveness of AEM, including a notable 1.4 percent gain when integrated into a state-of-the-art baseline on the highly challenging SWE-bench-Verified benchmark.

---


### 44. [LIMSSR: LLM-Driven Sequence-to-Score Reasoning under Training-Time Incomplete Multimodal Observations](https://arxiv.org/abs/2605.00434)

**<font color=#1a73e8>作者：</font>** Huangbiao Xu, Huanqi Wu, Xiao Ke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world multimodal learning is often hindered by missing modalities. While Incomplete Multimodal Learning (IML) has gained traction, existing methods typically rely on the unrealistic assumption of full-modal availability during training to provide reconstruction supervision or cross-modal priors. This paper tackles the more challenging setting of IML under training-time incomplete observations, which precludes reliance on a ``God's eye view'' of complete data. We propose LIMSSR (LLM-Driven Incomplete Multimodal Sequence-to-Score Reasoning), a framework that reformulates this challenge as a conditional sequence reasoning task. LIMSSR leverages the semantic reasoning capabilities of Large Language Models via Prompt-Guided Context-Aware Modality Imputation and Multidimensional Representation Fusion to infer latent semantics from available contexts without direct reconstruction. To mitigate hallucinations, we introduce a Mask-Aware Dual-Path Aggregation to dynamically calibrate inference uncertainty. Extensive experiments on three Action Quality Assessment datasets demonstrate that LIMSSR significantly outperforms state-of-the-art baselines without relying on complete training data, establishing a new paradigm for data-efficient multimodal learning. Code is available at this https URL.

---


### 45. [Escaping Mode Collapse in LLM Generation via Geometric Regulation](https://arxiv.org/abs/2605.00435)

**<font color=#1a73e8>作者：</font>** Xin Du, Kumiko Tanaka-Ishii  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mode collapse is a persistent challenge in generative modeling and appears in autoregressive text generation as behaviors ranging from explicit looping to gradual loss of diversity and premature trajectory convergence. We take a dynamical-systems view and reinterpret mode collapse as reduced state-space accessibility caused by *geometric collapse*: during generation, the model's internal trajectory becomes confined to a low-dimensional region of its representation space. This implies mode collapse is not purely a token-level phenomenon and cannot be reliably solved by symbolic constraints or probability-only decoding heuristics. Guided by this perspective, we propose *Reinforced Mode Regulation* (RMR), a lightweight, online state-space intervention that regulates dominant self-reinforcing directions in the Transformer value cache (implemented as low-rank damping). Across multiple large language models, RMR substantially reduces mode collapse and enables stable, high-quality generation at extremely low entropy rates (down to 0.8 nats/step), whereas standard decoding typically collapses near 2.0 nats/step.

---


### 46. [Impact of Task Phrasing on Presumptions in Large Language Models](https://arxiv.org/abs/2605.00436)

**<font color=#1a73e8>作者：</font>** Kenneth J.K. Ong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Concerns with the safety and reliability of applying large-language models (LLMs) in unpredictable real-world applications motivate this study, which examines how task phrasing can lead to presumptions in LLMs, making it difficult for them to adapt when the task deviates from these assumptions. We investigated the impact of these presumptions on the performance of LLMs using the iterated prisoner's dilemma as a case study. Our experiments reveal that LLMs are susceptible to presumptions when making decisions even with reasoning steps. However, when the task phrasing was neutral, the models demonstrated logical reasoning without much presumptions. These findings highlight the importance of proper task phrasing to reduce the risk of presumptions in LLMs.

---


### 47. [Thinking in Text and Images: Interleaved Vision--Language Reasoning Traces for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2605.00438)

**<font color=#1a73e8>作者：</font>** Jinkun Liu, Haohan Chi, Lingfeng Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon robotic manipulation requires plans that are both logically coherent and geometrically grounded. Existing Vision-Language-Action policies usually hide planning in latent states or expose only one modality: text-only chain-of-thought encodes causal order but misses spatial constraints, while visual prediction provides geometric cues but often remains local and semantically underconstrained. We introduce Interleaved Vision--Language Reasoning (IVLR), a policy framework built around \trace{}, an explicit intermediate representation that alternates textual subgoals with visual keyframes over the full task horizon. At test time, a single native multimodal transformer self-generates this global semantic-geometric trace from the initial observation and instruction, caches it, and conditions a closed-loop action decoder on the trace, original instruction, and current observation. Because standard robot datasets lack such traces, we construct pseudo-supervision by temporally segmenting demonstrations and captioning each stage with a vision-language model. Across simulated benchmarks for long-horizon manipulation and visual distribution shift, \method{} reaches 95.5\% average success on LIBERO, including 92.4\% on LIBERO-Long, and 59.4\% overall success on SimplerEnv-WidowX. Ablations show that both modalities are necessary: without traces, LIBERO-Long success drops to 37.7\%; text-only and vision-only traces reach 62.0\% and 68.4\%, while the full interleaved trace reaches 92.4\%. Stress tests with execution perturbations and masked trace content show moderate degradation, suggesting that the trace can tolerate local corruption and moderate execution drift, but remains limited under stale or incorrect global plans.

---


### 48. [Scaling Video Understanding via Compact Latent Multi-Agent Collaboration](https://arxiv.org/abs/2605.00444)

**<font color=#1a73e8>作者：</font>** Kerui Chen, Jinglu Wang, Jianrong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal large language models (MLLMs) advance vision language understanding but face inherent limitations in long-video tasks due to bounded perception context budgets. Existing agentic methods mitigate this via rule-based preprocessing, yet often suffer from information loss, high cost, and reliance on textual intermediates. We propose MACF, an end-to-end Multi-Agent Collaboration Framework that decouples per-agent perception budgets from global video complexity, enabling scalable video understanding while preserving visual fidelity. MACF partitions videos into segments for locally budgeted agents and enables holistic reasoning via an agent-native latent communication protocol. Each agent encodes partial observations into compact, task-sufficient tokens in a shared embedding space, allowing efficient and information-preserving collaboration by a central coordinator. We introduce a curriculum training strategy that progressively enforces semantic alignment, evidence summarization, and cross-agent coordination. Extensive experiments on diverse video understanding benchmarks show that MACF consistently outperforms state-of-the-art MLLMs and multi-agent systems under identical budget constraints, demonstrating the effectiveness of our latent collaboration for scalable video understanding.

---


### 49. [The Power of Order: Fooling LLMs with Adversarial Table Permutations](https://arxiv.org/abs/2605.00445)

**<font color=#1a73e8>作者：</font>** Xinshuai Dong, Haifeng Chen, Xuyuan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models have achieved remarkable success and are increasingly deployed in critical applications involving tabular data, such as Table Question Answering. However, their robustness to the structure of this input remains a critical, unaddressed question. This paper demonstrates that modern LLMs exhibit a significant vulnerability to the layout of tabular data. Specifically, we show that semantically-invariant permutations of rows and columns - rearrangements that do not alter the table's underlying information - are sometimes sufficient to cause incorrect or inconsistent model outputs. To systematically probe this vulnerability, we introduce Adversarial Table Permutation, a novel, gradient-based attack that efficiently identifies worst-case permutations designed to maximally disrupt model performance. Our extensive experiments demonstrate that ATP significantly degrades the performance of a wide range of LLMs. This reveals a pervasive vulnerability across different model sizes and architectures, including the most recent and popular models. Our findings expose a fundamental weakness in how current LLMs process structured data, underscoring the urgent need to develop permutation-robust models for reliable, real-world applications.

---


### 50. [ReLay: Personalized LLM-Generated Plain-Language Summaries for Better Understanding, but at What Cost?](https://arxiv.org/abs/2605.00468)

**<font color=#1a73e8>作者：</font>** Joey Chan, Yikun Han, Jingyuan Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Plain Language Summaries (PLS) aim to make research accessible to lay readers, but they are typically written in a one-size-fits-all style that ignores differences in readers' information needs and comprehension. In health contexts, this limitation is particularly important because misunderstanding scientific information can affect real-world decisions. Large language models (LLMs) offer new opportunities for personalizing PLS, but it remains unclear whether personalization helps, which strategies are most effective, and how to balance personalization with safety. We introduce ReLay, a dataset of 300 participant--PLS pairs from 50 lay participants in both static (expert-written) and interactive (LLM-personalized) settings. ReLay includes user characteristics, health information needs, information-seeking behavior, comprehension outcomes, interaction logs, and quality ratings. We use ReLay to evaluate five LLMs across two personalization methods. Personalization improves comprehension and perceived quality, but it also raises the risk of reinforcing user biases and introducing hallucinations, revealing a trade-off between personalization and safety. These findings highlight the need for personalization methods that are both effective and trustworthy for diverse lay audiences.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-79](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
