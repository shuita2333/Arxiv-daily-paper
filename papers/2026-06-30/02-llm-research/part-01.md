# 🧠 大模型相关研究 | 2026年06月30日

> 本类共 **84** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-84](./part-02.md)

---

### 1. [Formalizing Latent Thoughts: Four Axioms of Thought Representation in LLMs](https://arxiv.org/abs/2606.27378)

**<font color=#1a73e8>作者：</font>** Fahd Seddik, Fatemeh Fard  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce an axiomatic evaluation framework for latent thought representations in LLMs, comprising metrics that are independent of downstream benchmark scores and reveal representational failures that benchmark accuracy masks. Existing evaluations conflate representation quality with model capacity. Therefore, failures cannot be attributed to the representation rather than to the model that processes it. We formalize four functional axioms (Causality, Minimality, Separability, and Stability) and define a quantitative measure for each, computed directly on the representation independently of downstream accuracy. We audit open-weight LLMs across 23 reasoning tasks (e.g., Spatial Reasoning, Factual QA). We find that no candidate satisfies all four axioms simultaneously, that the representations distinguish task type reliably but cannot distinguish between two questions within the same task, and that the representations encode little information beyond what is already present in the input embedding. The failure is consistent across dense, reasoning-distilled, and RL-trained model families, indicating that the gap is structural rather than a property of model size or training procedure.

---


### 2. [Position: The Term "Machine Unlearning" Is Overused in LLMs](https://arxiv.org/abs/2606.27379)

**<font color=#1a73e8>作者：</font>** Sangyeon Yoon, Yeachan Jun, Albert No  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly face demands to "forget" training data, knowledge, or behaviors due to regulatory deletion obligations, copyright/licensing disputes, and safety or product-policy requirements. This position paper argues that machine unlearning is overused as a term in LLM research and should be reserved for dataset-defined deletion: removing the training influence of a precisely specified forget set such that the resulting model is approximately indistinguishable from retraining without that data. We contend that many tasks currently labeled "unlearning" (e.g., refusal for harmful requests, entity/knowledge removal, or targeted suppression) pursue different, often policy-dependent objectives and therefore require different terminology and baselines (e.g., alignment, suppression, editing, obfuscation). We further argue that this confusion is not cosmetic: because papers make different implicit guarantees under the same label, metrics and benchmarks are frequently reused outside their intended scope, rewarding surface-level non-disclosure (e.g., low ROUGE/forget accuracy) even when retraining-equivalence is not tested and derived capabilities remain. We conclude by calling for stricter terminology tied to explicit guarantees and reference models, and for evaluations that match the claimed objective.

---


### 3. [Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement](https://arxiv.org/abs/2606.27409)

**<font color=#1a73e8>作者：</font>** Igor Itkin  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) systems often rely on verifier and critic agents to suppress hallucinations, but verification is delayed. During this delay, false claims can propagate through the agent network. We model this process as delayed consensus on a graph with grounded corrector nodes. Spectral decomposition by the grounded Laplacian yields a closed-form stability threshold for the verification dose: correction that is too strong or too delayed can turn consensus into oscillation. The most unstable regime occurs when the communication and verification delays coincide; for delay two, the threshold is the inverse golden ratio. The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. Experiments across five open models confirm the predicted dose-delay oscillations. By contrast, grounded factual answering makes truth an absorbing boundary and eliminates the effect, suggesting that the instability is specific to signed-belief tasks while grounded verification remains stabilizing

---


### 4. [Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents](https://arxiv.org/abs/2606.27416)

**<font color=#1a73e8>作者：</font>** Vassili Philippov, Pavel Katunin, Dmitry Andreev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM coding agents make it tempting to automate empirical research by delegating experiments to them directly, but naive delegation does not scale to large projects: low-rate instruction lapses compound into broken, irreproducible artefacts. To address this problem, we present Glite ARF, an open-source Python framework for running many LLM coding agents in parallel on a research repository without sacrificing reproducibility or auditability. The framework defines a three-role stack: a human researcher chooses which hypotheses to test, coding agents (Claude Code, Codex CLI) implement individual tasks under a fixed structure, and deterministic Python verifier scripts enforce task isolation, immutability of completed work, a corrections overlay, and a materialised project overview. We call this verifier-driven research: the rules of the research process live in code that fails loudly when violated, not in prose that agents are merely asked to follow. Using Glite ARF, we developed our submission to the BEA 2026 vocabulary-difficulty shared task, placing first in the closed track and second in the open track on all three target languages (Spanish, German, Mandarin) and reducing the official baseline RMSE by 29.9% (closed) and 35.9% (open). The campaign comprised 273 tracked tasks (146 experiment runs) across 129 feature sets, run by up to twelve parallel agents orchestrated from a single laptop - with some model training on rented A100s - at approximately \$450 in LLM API spend (\$498 total third-party cost), and structured per-fold provenance let us catch and strip four target-leaking feature sets, correcting an implausible 0.609 RMSE to 0.802. Across three campaigns in three domains, the framework's structural machinery adds only about 1% of wall-clock time. Framework and a public demo project accompany this paper.

---


### 5. [When Does Personality Composition Matter for Multi-Agent LLM Teams?](https://arxiv.org/abs/2606.27443)

**<font color=#1a73e8>作者：</font>** Aryan Keluskar, Amrita Bhattacharjee, Huan Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personality prompting shapes how large language models communicate, yet whether these behavioral shifts affect objective task outcomes remains under-explored. Prior work shows that agents prompted with low agreeableness produce adversarial language, while those prompted with high agreeableness become cooperative, but the relationship between communication style and task performance has not been systematically examined across multiple domains. In this work, we investigate whether personality composition matters for multi-agent team performance by manipulating personality traits across frontier LLMs on three task domains: structured coding, open-ended research collaboration, and competitive bargaining. We find that personality effects depend critically on task structure. In coding tasks, low agreeableness leads to large communication shifts that have little effect on milestone completion. In open-ended collaboration and bargaining, the same manipulation substantially degrades performance. We discuss implications for multi-agent system design and the limits of personality manipulation.

---


### 6. [Causal Connections: Leveraging Multilingual Fine-Tuning for Financial QA@FinCausal 2026](https://arxiv.org/abs/2606.27446)

**<font color=#1a73e8>作者：</font>** Akash Kumar Gautam, Serhii Hamotskyi, Christian Hänig  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes team HSA_CORAL's submission to the FinCausal 2026 shared task on extracting cause-effect relations from financial narratives via extractive question answering in English and Spanish. We compare three modeling families: (i) encoder-only token tagging with multilingual BERT, (ii) encoder-decoder generation with multilingual BART, and (iii) decoder-only LLMs (Llama 3.1 and GPT variants) using prompt refinement, few-shot demonstrations, and supervised fine-tuning. Across settings, prompting and few-shot examples yield competitive performance, while supervised fine-tuning provides the largest gains. Our best system, GPT-4.1 Mini fine-tuned on combined English and Spanish training data, achieves a tied highest score on the English subtask (score 4.8140) and ranks third on Spanish (score 4.7753) under the shared task's LLM-as-a-judge metric. Overall, the results highlight the value of task-specific adaptation and multilingual fine-tuning for cross-lingual transfer in financial causality QA.

---


### 7. [Developmental approach reveals the statistical learning of Neural Language Models: Transformers generalize from the most abstract statistical patterns](https://arxiv.org/abs/2606.27460)

**<font color=#1a73e8>作者：</font>** Wang Bojun, Holly Jenkins, Elizabeth Wonnacott  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this study, we use a developmental approach to investigate the statistical learning and mental representation of neural language models (NLM). A series of Generative Transformer models are trained on a synthetic grammar. The model states are saved at multiple stages in the course of training. Through analyzing how the internal representations of these models change in the developmental path, we found that NLMs acquire the most abstract global statistical knowledge at the beginning of learning and later acquire the relatively local statistical dependencies. This learning path contains many over-generalizations from the very beginning and these over-generalizations are gradually constrained in the later stage of learning. Based on this observation, we propose a new framework to explain the statistical learning and language cognition of NLMs.

---


### 8. [Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents](https://arxiv.org/abs/2606.27472)

**<font color=#1a73e8>作者：</font>** Vedant Patel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents operate over long, multi-session interactions in which facts change: a user moves, a price updates, a plan is revised. Acting correctly requires using the current value of a fact and discarding values that have been superseded. We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. On the knowledge-update subset of LongMemEval, replacing an agent's full context with a bounded, self-maintained memory drops accuracy from 92% to 77% even on a frontier model (gpt-5.4), a gap that is statistically significant (paired McNemar p<0.005) and persists across model scale while full-context accuracy saturates near 92%. The bottleneck is therefore memory maintenance, not comprehension, and is not closed by a stronger model. We then ask whether this is merely an undersized memory, and find it is not: as the conversation grows 24x, accuracy falls further (from 68% to 28%), and granting the agent proportionally more memory yields no detectable recovery (28% to 28%, n=25). The failure scales with the length of the conversation, not the compression ratio. We release Supersede, an open reinforcement-learning environment (on the verifiers / prime-rl stack) that turns this measurement into a training signal: agents are rewarded for answering from the current value and penalized for stale ones. Finally, we close the loop and show the gap is trainable: GRPO fine-tuning a small open model (Qwen2.5-3B) on this environment nearly doubles its held-out supersession accuracy on real, unseen conversations (9.0% to 16.7%, a single run), along a monotonic checkpoint curve indicating the learned policy, not the harness, carries the gain. To our knowledge this is the first trainable environment whose reward targets temporal fact-currency, and the first evidence the supersession gap can be trained down, not only measured.

---


### 9. [Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning](https://arxiv.org/abs/2606.27483)

**<font color=#1a73e8>作者：</font>** Xuan Zhang, Zhijian Zhou, Lingfeng Qiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have demonstrated strong capability in sequential decision-making, yet they remains fundamentally reactive in long-horizon tasks. Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. Therefore, we propose to internalize future-aware planning by training a single autoregressive model to verbalize both a prospective state rollout and a plan-conditioned success estimate-a textual analogue of the Q-value. Crucially, we identify a format-capability gap: simply fine-tuning agents on look-ahead traces during post-training leads to superficial mimicry of foresight without genuine predictive grounding. To bridge this gap, we introduce a three-stage training paradigm: (i) World Model Agentic Mid-Training (WM-AMT) to inject latent predictive capabilities into the policy; (ii) Format-Eliciting SFT (FE-SFT) to structure this injected capability; and (iii) Foresight-Conditioned Reinforcement Learning (FC-RL) to refine the calibration and utility of the generated simulations. Evaluated on search and mathematical reasoning tasks, our approach consistently outperforms other training baselines. Our results demonstrate that effective internal world modeling in LLM agents requires a capability-first training pipeline to achieve grounded and calibrated foresight.

---


### 10. [Fine-tuning a multimodal large language model for clinician-grade autism behavioral scoring from short home videos](https://arxiv.org/abs/2606.27484)

**<font color=#1a73e8>作者：</font>** Mohammadmahdi Honarmand, Parnian Azizian, Aaron Kline 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autism spectrum disorder (ASD) affects 1 in 31 US children, yet median age at diagnosis exceeds four years. Artificial intelligence pipelines that provide quantified diagnosis using easy to access observational data (e.g., home videos) could help with earlier diagnosis, and timely delivery of early treatments. We fine-tuned Gemini 2.5 Pro on 400 clinician-rated home videos with low-rank adaptation, training only on 30 behavioral features previously validated to produce reliable predictions when passed to various ML models. On 99 held-out children (49 ASD, 50 neurotypical), inter-rater reliability with clinicians (per-feature weighted Cohen's kappa) improved by 40% (p<0.001), with 27 of 28 evaluable features improving. As an emergent zero-shot capability, direct ASD diagnosis F1 improved by 53% (p<0.001), matching or exceeding clinician outcomes. Classifier-assisted pipelines using fine-tuned LLM-derived behavioral features matched clinician-scored inputs across all tested pathways and achieved 77% accuracy (95% CI: 68-85%) and an AUC of 86% (95% CI: 78-92%). Fine-tuned multimodal LLMs can serve as scalable behavioral feature extractors for use in autism assessment and diagnosis.

---


### 11. [QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems](https://arxiv.org/abs/2606.27492)

**<font color=#1a73e8>作者：</font>** Congjia Tian, Yuhang Yao, Jiaming Cui  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) multi-agent systems increasingly depend not only on how individual agents reason, but also on how agents are connected. This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. A pool of worker agents, the task adapter, and the scoring function are frozen; only an outer LLM planner learns to generate temporal communication DAGs specifying who sends information to whom, in which round, who merges messages, and who emits the final answer. Execution traces are distilled into evidence-backed design rules with three actions: \emph{Preserve}, \emph{Modify}, and \emph{Avoid}. To prevent self-evolution from turning lucky runs or plausible but false explanations into policy, QueenBee uses held-out acceptance gates, variance-aware credit, motif-level attribution, transfer trust, insight falsification, and structural deduplication. We evaluate the method on Count-Frequency aggregation and Silo-Bench-style distributed coordination tasks. With fixed workers, self-evolved graph generation produces communication structures that improve over fixed topologies and cold generation. In the CF fulltest setting, the best generated graph reduces RMSE from 12.53 for the strongest fixed topology to 7.87 while also reducing messages, model calls, and token cost; Silo-style results show the same direction of improvement over cold and fixed-topology baselines. These results suggest that multi-agent systems can learn reusable architectural design knowledge rather than merely memorizing task answers.

---


### 12. [DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection](https://arxiv.org/abs/2606.27499)

**<font color=#1a73e8>作者：</font>** Yujin Tang, Chenming Shang, Ruize Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Research on agent memory has matured rapidly, but almost entirely on the text side: few existing benchmarks ask, in an interactive environment, when an agent genuinely needs to remember what it saw rather than what it could write down. We introduce DMV-Bench (Code: this https URL), the first interactive benchmark for multimodal-agent visual memory. DMV-Bench is built on a controlled home-furnishing e-commerce catalogue of 1,000 product variants in which a text-leakage contract keeps the discriminative signal of each task in the pixels alone. Across a chain of autonomous shopping sessions, every visited product image carries a unique, pre-rendered incidental cue, and the agent is later asked to recall a particular cued product and navigate to its URL. Inspired by dual-coding theory, we propose DualMem, a memory architecture that maintains a visual and a verbal code in parallel. On DMV-Bench, DualMem outperforms a caption baseline and three recent multimodal agent-memory systems at every chain length J in {5, 10, 15, 50} on both Gemini 2.5 Flash and Qwen2.5-VL-7B, with the lead surviving controls for memory-bank size and encoding-position bias, and an asymmetric dual-coding regime in which vision carries the cue end-to-end while the verbal channel plays a smaller query-grounding role.

---


### 13. [Aloe-Vision: Robust Vision-Language Models for Healthcare](https://arxiv.org/abs/2606.27500)

**<font color=#1a73e8>作者：</font>** Jaume Guasch-Martí, Enrique Lopez-Cuena, Martín Suárez-Fernández 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) specialized in healthcare are emerging as a promising research direction due to their potential impact in clinical and biomedical applications. However, progress is constrained by the scarcity of high-quality medical multimodal data, concerns about robustness in safety-critical settings, and the narrow and potentially contaminated evaluation benchmarks that limit reliable assessment. To address these issues, the field requires state-of-the-art solutions to be fully open and reproducible systems in which all components can be inspected, evaluated, and improved. This work introduces Aloe-Vision-Data, a large-scale, quality-filtered mixture which integrates both medical and general domains across multimodal and text-only sources, designed for direct use in model fine-tuning. Building on this dataset, we train the Aloe-Vision family of medical LVLMs, openly released with full weights, training recipes and data, in two scales (7B and 72B). Through comprehensive benchmarking, we demonstrate that high quality training mixtures produce balanced LVLMs which yield significant gains over the baseline models without compromising general capabilities, achieving competitive performance with respect to state-of-the-art alternatives. To support reliable evaluation, we introduce CareQA-Vision, a carefully curated vision benchmark derived from MIR and EIR exams, the residency entrance exams for medical and nursing specialists in Spain, offering novel vision questions with low likelihood of contamination. Finally, we show that current LVLMs remain vulnerable to adversarial and misleading inputs, underscoring reliability challenges in clinical contexts.

---


### 14. [Boundary condition fidelity for bottom-hole pressure and CO2 plume prediction in geological carbon storage](https://arxiv.org/abs/2606.27515)

**<font color=#1a73e8>作者：</font>** Romal Ramadhan, Seyyed A. Hosseini, Larry W. Lake  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of bottom-hole pressure (BHP) and CO2 plume migration is essential for safe geological carbon storage, yet practical simulations often rely on truncated domains where artificial boundaries distort pressure diffusion and CO2 saturation footprints. In this study, we evaluate how boundary-condition fidelity affects BHP and CO2 plume prediction by comparing ten reduced-domain boundary treatments against full-domain reference simulations in homogeneous and heterogeneous reservoirs. We test uniform pore-volume multipliers, transmissibility modifiers, corner-adjusted pore-volume corrections, layered corrections, and gradual modifiers using BHP RMSE, NRMSE, peak pressure deviation, and plume Intersection over Union (IoU) as performance metrics. Our results show that conserving corner pore volume is the most important requirement for truncated-domain modeling. We find that uniform treatments which neglect corner storage generate large pressure errors, with BHP RMSE of 362 to 382 psi in the homogeneous model and 250 to 304 psi in the heterogeneous model, and yield plume IoU values near 0.80 to 0.84, indicating roughly 16 to 20% of the combined plume area is misrepresented. Corner-adjusted scenarios substantially reduce pressure errors and raise plume IoU above 0.94, but we observe that transmissibility correction is not universally beneficial. In homogeneous reservoirs, uniform transmissibility adjustment improves pressure fidelity; in heterogeneous reservoirs, it can over-restrict flow across variable-permeability boundary faces, increasing BHP error and contracting the predicted plume. We find the gradual modifier with transmissibility correction provides the most consistent performance, achieving BHP NRMSE below 3.7% and plume IoU above 0.97 in both reservoir types.

---


### 15. [Large Language Model Teaches Visual Students: Cross-Modality Transfer of Fine-Grained Conceptual Knowledge](https://arxiv.org/abs/2606.27527)

**<font color=#1a73e8>作者：</font>** Thomas Shih-Chao Liang, Zhuoran Yu, Yong Jae Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) possess broad conceptual knowledge acquired through large-scale text pretraining, yet their potential to supervise models in other modalities remains underexplored. In this work, we propose LaViD--Language-to-Visual Knowledge Distillation--a simple and effective framework for transferring high-level semantic knowledge from a language-only teacher to a vision-only student model. Instead of relying on paired multimodal data, LaViD elicits conceptual signals from an LLM by prompting it to generate multiple-choice questions (MCQs) that probe semantic distinctions between visual classes. Each class is mapped to a soft label distribution over these MCQs, forming a rich conceptual signature that guides the student through an auxiliary distillation loss. Notably, despite using a language-only teacher without access to image data, LaViD consistently outperforms recent methods like MaKD that distill from vision-language models across multiple fine-grained benchmarks. It also achieves competitive or superior performance compared to state-of-the-art visual distillation methods such as DKD and MLKD, with further gains when combined with logit standardization. On the Waterbirds dataset, LaViD substantially improves worst-group accuracy, demonstrating enhanced robustness to spurious correlations with distillation. Code is available at this https URL.

---


### 16. [MemoBench: Benchmarking World Modeling in Dynamically Changing Environments](https://arxiv.org/abs/2606.27537)

**<font color=#1a73e8>作者：</font>** Haoyu Chen, Kaichen Zhou, Hang Hua 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models aspire to simulate dynamic environments, and several benchmarks now evaluate memory consistency across frames. However, most assess consistency only while the target remains in view, and the few that force objects out of view evaluate static scenes where nothing changes during occlusion. To bridge this gap, we introduce MemoBench, a diagnostic benchmark built around the disappear-and-reappear paradigm in dynamically changing environments: a target object undergoes a physical process, disappears from view, and must be correctly recovered in its updated state upon reappearance. We curate 360 ground-truth clips spanning synthetic and real-world scenes, and design an evaluation suite combining automated metrics with VQA-based assessment across four diagnostic pillars. Evaluation of eight state-of-the-art models reveals key insights and open challenges regarding memory consistency under the disappear-and-reappear paradigm.

---


### 17. [EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction](https://arxiv.org/abs/2606.27550)

**<font color=#1a73e8>作者：</font>** Carrie Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-token prediction has been shown to increase data density during training, improve downstream text-generation quality, and serves as the defacto approach for self-speculative decoding. Existing foundation and open source models that use MTP heads commit to a static tree-based attention topology throughout the entire generation sequence, meaning the speculation depth, and thus the compute required during verification, stays constant regardless of the context. This is fundamentally misaligned with the entropy patterns of natural language where low-entropy regions often support reliable multi-step drafting, while high-entropy regions require more conservative speculation. To address this, we propose Entropy-guided Multi-Token Prediction (EntMTP), a training-free scheduler that toggles between tree-based attention topologies from a set of task-specific pareto-optimal trees conditioned on a running estimate of local generation entropy. By matching speculation depth to context predictability, EntMTP maximizes expected accepted-token throughput across the full distribution of generated text without sacrificing generation quality. When evaluated across Humaneval, ShareGPT, GSM8k, and Litbench benchmarks, EntMTP consistently achieves a 1.15x speedup against Hydra and peak speedup of 1.36x against Medusa baselines respectively.

---


### 18. [Perceptual 3D Simulation With Physical World Modeling](https://arxiv.org/abs/2606.27575)

**<font color=#1a73e8>作者：</font>** Wanhee Lee, Klemen Kotar, Rahul Mysore Venkatesh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting how a scene will evolve after a desired 3D transformation from images is a central goal in vision, graphics, and robotics. Yet unlike ideal simulators with full access to 3D geometry and dynamics, real world systems must rely on perceptual inputs and local actions that are inherently partial and incomplete. In this work, we present P3Sim, a physical world modeling system that simulates future scene states under both partial observations and incomplete 3D transformation signals. P3Sim is composed of three interacting components: a learned physical world model, a geometric conditioning module, and a persistent scene memory. The world model interprets perception as probabilistic inference over multimodal scene variables, providing predictions of the distributions of any scene variable conditioned on any combination of others. The geometric conditioning module provides a partial 3D transform signal for conditioning the world model at inference time. The persistent scene memory integrates predictions over time, enabling online updates and consistency under uncertainty. By combining learned inference with explicit geometric structure, P3Sim balances data-driven flexibility with built-in inductive bias. This design yields a flexible perceptual simulator that generalizes across diverse 3D transformation tasks, such as novel view synthesis, object manipulation, and dynamic scene prediction, advancing toward general purpose 3D scene understanding and transformation.

---


### 19. [PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration](https://arxiv.org/abs/2606.27578)

**<font color=#1a73e8>作者：</font>** Arnav Raj  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward models for Reinforcement Learning from Human Feedback (RLHF) pool preferences across thousands of annotators and fit one global affine calibrator, collapsing raters with systematically different rating-scale offsets and slopes into a single average-rater fit that does not match any individual annotator. PEBS is a per-rater empirical-Bayes shrinkage estimator: it fits per-rater affine calibrators on a held-out slice of each annotator's ratings and applies Morris-James-Stein empirical-Bayes shrinkage toward the population mean, in closed form and without retraining the reward model. On PRISM, PEBS reduces within-user held-out RMSE by 8.58% over the pooled population-slope baseline. The procedure replicates on PluriHarms harm ratings (Qwen-2.5 base, in-family) with a +9.66% RMSE reduction over the same population-slope baseline. PEBS is a closed-form post-hoc estimator for annotator-specific affine calibration in RLHF reward modeling; it leaves the reward base model unchanged and estimates only the rater-level map used at inference time for new ratings.

---


### 20. [Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF](https://arxiv.org/abs/2606.27580)

**<font color=#1a73e8>作者：</font>** Arnav Raj  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) in production does not always have a synchronous reward signal. Code-execution verifiers, slow judge ensembles, and queued human review can return several gradient steps after the rollout that produced them, breaking the synchronous-reward assumption underlying standard PPO. We address this gap with Retroactive Advantage Correction (RAC): each pending slow completion is queued, aged through a non-negative kernel, and reinjected as a clipped residual into the next optimiser step's advantage. We prove that under an unbiased clipped importance ratio, the cumulative RAC correction is exactly unbiased when the effective delay kernel reinjects all of its mass, and carries a bias linear in the unreinjected fraction otherwise; at the no-delay identity kernel it reduces to V-trace. On a tabular Markov decision process (MDP) proof-of-concept, RAC reduces the closed-form policy bias by up to 47.9x at the two-slow-channel configuration, beating wait-for-slow at lower wall-clock cost. RAC integrates with PPO and GRPO through a two-line reward-manager patch.

---


### 21. [Odyssey: Constructing Verifiable Local Truth-Preserving Foundation Models](https://arxiv.org/abs/2606.27593)

**<font color=#1a73e8>作者：</font>** Sridhar Mahadevan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce a categorical framework called ODYSSEY for constructing verifiable, local truth-preserving foundation models as compositions of foundries: building-block architectural components that specify a cover of local contexts, local representation families, restriction maps, gluing rules, obstruction policies, update obligations, and human-facing views. A foundry is an organized sheaf of knowledge that carries within it an argumentation component. Concrete foundries are built from generic foundries such as evidence/argument, operational decision, institutional/financial, market meaning, scientific challenge, research-program, assistant-build, and evaluation-harness foundries. Universal Foundry Learning (UFL) formalizes foundry construction as a composition of left and right Kan extensions, with left Kan extension rolling local artifacts into candidate foundries and right Kan extension enforcing the restriction, gluing, obstruction, and argumentation conditions required for promotion. Foundry SQL (FSQL) is a small typed query surface for slicing maintained foundry artifacts that uses TICKET (Topos Integration using Causal Kan Extension Transformers) certification for admitting external or pre-built models into durable ODYSSEY state. ODYSSEY is fully implemented and tested across a wide spectrum of concrete foundries, showing that the same categorical machinery supports domain construction, artifact replay, sheaf diagnostics, grounded Toulmin/local-LLM scrutiny, residual-obstruction ledgers, and optimized TICKET-compatible causal-claim extraction across heterogeneous sources. This paper is to be presented as a 2.5 hour tutorial at ICML 2026. The tutorial home page is at this https URL.

---


### 22. [Dismantling Pathological Shortcuts: A Causal Framework for Faithful LVLM Decoding](https://arxiv.org/abs/2606.27596)

**<font color=#1a73e8>作者：</font>** Liu Yu, Can Chen, Ping Kuang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) exhibit sophisticated reasoning but remain susceptible to object hallucination. Deviating from the prevailing attention intensity assumption, we reveal a deeper dynamic structural misalignment: hallucination is triggered at decision-critical steps where specific attention heads, acting as risky mediators, decouple from visual evidence to lock onto language priors. This establishes a pathological shortcut that bypasses visual grounding. To dismantle this, we propose Fox (Faithfulness and Observational-flow via eXpression-rectification), a training-free inference-time framework. Fox diagnoses structural misalignment using a visual attention entropy probe to localize risky mediators unsupervisedly. We then execute a targeted causal intervention via numerical logit saturation to physically sever the shortcut path. Finally, a conflict-gated cooperative decoding strategy reconciles interventional faithfulness with observational fluency. Extensive experiments demonstrate that Fox achieves SOTA performance, outperforming SID by 29.1% while preserving linguistic richness. Code is available at this https URL.

---


### 23. [Qwen-Image-2.0-RL Technical Report](https://arxiv.org/abs/2606.27608)

**<font color=#1a73e8>作者：</font>** Yixian Xu, Kaiyuan Gao, Yuxiang Chen 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. To provide reliable reward signals, we construct task-specific composite reward models by fine-tuning vision-language models with a pointwise scoring paradigm and chain-of-thought reasoning. For text-to-image generation, the reward models cover alignment, aesthetics, and portrait fidelity dimensions. For image editing tasks, the reward system addresses instruction-following accuracy and face identity preservation. Building on this reward system, we develop a scalable GRPO-based RL training framework, incorporating a hybrid classifier-free guidance (CFG) strategy to preserve pre-trained knowledge, prompt curation via intra-group reward range filtering, and per-category reward weight calibration. To merge the task-specialized RL policies for T2I and editing, we propose on-policy distillation as the final training stage, which consolidates multiple teachers into a single student model through trajectory-level velocity matching. Extensive evaluation shows that Qwen-Image-2.0-RL achieves 57.84 overall score on Qwen-Image-Bench (+2.61 over the base model), Elo ratings of 1193 in text-to-image arena (+78) and 1349 in image edit arena (+93), demonstrating consistent gains in aesthetic quality, prompt adherence, and editing accuracy.

---


### 24. [COOPA: A Modular LLM Agent Architecture for Operations Research Problems](https://arxiv.org/abs/2606.27611)

**<font color=#1a73e8>作者：</font>** Chuanhao Li, Xiaoan Xu, Dirk Bergemann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operations Research (OR) provides a rigorous framework for high-stakes decision-making, but effective OR modeling requires substantial domain knowledge, mathematical abstraction, and solver expertise. Recent LLM-based systems automate parts of this pipeline, yet remain limited by low accuracy on complex problems, opaque outputs, and narrow solver support. We propose COOPA (COoperative OPerations Agent), a modular LLM-agent architecture for interpretable and scalable OR decision support. It combines three components: iterative confidence-based modeling, which generates multiple candidate formulations, self-evaluates them across modeling dimensions, and selects one using a max-min confidence criterion; element-level provenance and confidence explanations, which link variables, parameters, constraints, and objectives to quoted source text and provide an audit trail for human verification; and multi-solver routing to specialized optimizer agents for different OR problem classes. Across three OR benchmarks, eight LLM backbones, and four baselines under identical conditions, COOPA achieves the best macro-average accuracy on six of eight backbones and improves over the strongest baseline by up to 6.7 percentage points. A within-system ablation isolates the contribution of iterative confidence-based modeling, while additional analyses and case studies illustrate the value of source traceability and multi-solver dispatch.

---


### 25. [DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners Insights from Online Forums](https://arxiv.org/abs/2606.27619)

**<font color=#1a73e8>作者：</font>** Dana Rezazadegan, Atie Kia, Phongpadid Nandavong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dyslexic learners increasingly use artificial intelligence (AI) tools to support reading, writing, organisation, and study-related tasks. However, their lived experiences with these tools remain largely underexamined. This paper proposes DysLexLens, a low-resource LLM framework, designed to analyse dyslexic learners experience with AI through online forum discussions. DysLexLens is designed as an end-to-end, evidence-traceable architecture which transforms noisy social media posts into a dictionary-driven corpora, provides knowledge-graph (KG)-based question reasoning, generates verifiable query responses, and enables response evaluation through quantitative and human-grounded assessment. DysLexLens has four key features. First, it employs a dictionary-driven filtering method to construct a more focused Reddit corpus on dyslexia and AI, filtering out noisy and weakly related posts to improve the relevance of data collected from low-resource forum contexts. Second, it integrates LLM-assisted semantic analysis with KG-based query reasoning to uncover meaningful patterns. Third, it has quantitative evaluation metrics (RAGAS and Query Robustness) to measure LLM-generated response performance. Fourth, it provides structured qualitative validation guidelines for assessing response quality, with a specific focus on hallucination and evidence alignment. We demonstrate the effectiveness of DysLexLens using dyslexia-related Reddit forum data and 30 questions. The results show its potential generalisability to other low-resource forum data contexts. DysLexLens, sample data, questions and evaluation results are available at Github to support reproducibility.

---


### 26. [HybridCodec: Modeling Discrete and Continuous Representations for Efficient Speech Language Models](https://arxiv.org/abs/2606.27627)

**<font color=#1a73e8>作者：</font>** Artem Ploujnikov, Francesco Verdini, Samir Sadok 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete audio representations have become increasingly popular for building multimodal text-audio systems and integrating audio capabilities into Large Language Models (LLMs). However, numerous studies report performance degradation on various downstream tasks due to information loss during discretization. To address this, we propose a novel approach combining temporally compressed discrete tokens with dimensionality-reduced continuous residuals. Our framework consists of a hybridized discrete-continuous focal modulation codec and a hybrid Transformer. This architecture performs autoregressive inference in the discrete domain, coupled with non-autoregressive prediction and continuous residual upsampling. Experimental results show that our approach significantly improves the retention of speaker characteristics compared to discrete-only methods, while simultaneously reducing the number of required autoregressive steps.

---


### 27. [Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety](https://arxiv.org/abs/2606.27632)

**<font color=#1a73e8>作者：</font>** Ting Ma, Xiufeng Huang, Benlei Cui 等 46 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly deployed in real-world systems, safety failures can still lead to harmful outputs and dangerous misuse. We argue that the essence of safety is adversarial: many failures arise not from natural inputs alone, but from strategic attempts to evade model policies and safeguards. However, existing general-purpose model development largely overlook this adversarial nature, and often remain insufficient for realistic safety scenarios involving planning, tool use, and multi-step reasoning, causing measured safety performance to overestimate real deployment robustness. To address this gap, we present Yuvion LLM, a large language model built for adversarially robust content safety and broader AI safety. Yuvion LLM treats adversarial robustness and agentic capability as first-class objectives. Its pipeline combines adversarially aware data construction, knowledge-enhanced continued pretraining, and policy-grounded multi-task safety post-training, including risk-aware supervised fine-tuning and reinforcement learning-based policy optimization, together with safety-aware agentic reinforcement learning for tool use and multi-step reasoning in complex safety scenarios. We further introduce the Yuvion LLM RiskEval (YLRE), a collection of 93 benchmarks across four evaluation categories, covering diverse open and internal evaluations with a focus on safety, adversarial robustness, and real-world capability requirements. Across these evaluations, Yuvion LLM demonstrates clear advantages on safety-focused benchmarks and particularly strong robustness under adversarial conditions, while maintaining solid overall capability. Notably, Yuvion-8B outperforms most state-of-the-art baselines, including substantially larger models such as GPT-5.4 and Qwen3-MAX, on several safety tasks.

---


### 28. [Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis](https://arxiv.org/abs/2606.27634)

**<font color=#1a73e8>作者：</font>** Thomas S. Paula, Lucas S. Kupssinskü, Rodrigo C. Barros  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small Language Models (SLMs) are increasingly being considered for deployment on edge devices such as laptops, enabling private, low-latency, and locally personalized applications. However, personalization requires models to adapt over time to evolving user- or task-specific data, placing them in a continual learning setting. This creates the risk of catastrophic forgetting, where learning new information degrades performance on previously learned tasks or broader model capabilities. Recent benchmarks such as TRACE have shown that continual fine-tuning can significantly degrade the general abilities of aligned large language models. In this work, we present a study for sequential LoRA personalization of SLMs. We save model checkpoints after each adaptation stage and evaluate them on current tasks, previously seen tasks, and a fixed reference set. This checkpoint-level protocol enables us to monitor task performance, forgetting, and reference set drift over time. We show that lightweight reference set distributional diagnostics can reveal model-specific instability patterns during sequential LoRA personalization of SLMs, including cases where task-level metrics alone hide harmful adaptation. We hope this can highlight new research avenues for monitoring stability of SLMs in a continual learning setting.

---


### 29. [CascadeOcc: Rethinking 3D Occupancy World Models with Cascaded VQ Representations](https://arxiv.org/abs/2606.27644)

**<font color=#1a73e8>作者：</font>** Kyumin Hwang, Wonhyeok Choi, Jaeyeul Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This letter proposes CascadeOcc, a novel occupancy world model that prioritizes intrinsic structural hierarchy over extrinsic auxiliary modalities for autonomous driving. Occupancy world models -- forecasting the future driving environment and planning the driving trajectory -- effectively bridge perception and planning, but current approaches often heavily rely on external modalities or large language models, failing to fully exploit the inherent structural potential of occupancy representations themselves. To enhance representational capacity for complex 3D scenes, we integrate a cascaded Vector Quantized (VQ) mechanism into an autoregressive framework. Following a coarse-to-fine principle, CascadeOcc progressively refines fine-grained details from global structures through a multi-scale architecture. Additionally, we incorporate a TimeMixer to capture multi-scale temporal dependencies, establishing a dual-hierarchy mechanism in both space and time. Experimental results on 4D occupancy forecasting and motion planning benchmarks demonstrate that CascadeOcc achieves superior performance among vision-centric approaches, validating that optimizing inherent representations is a powerful alternative to relying on external foundation models.

---


### 30. [VLM-Aware Meta-Optic Front-End Design for Frozen Vision-Language Models](https://arxiv.org/abs/2606.27646)

**<font color=#1a73e8>作者：</font>** Chanik Kang, Raphaël Pestourie, Haejun Chung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional machine-vision pipelines typically rely on high-quality optics that produce clean, human-interpretable images, and optical design has therefore been driven by image-level criteria such as resolution, aberration correction, and pixel fidelity. However, such optics are often impractical for size-, cost-, or form-factor-constrained applications, where compact meta-optics offer an attractive alternative but operate under strict physical efficiency limits. We propose CODA, a co-design framework that optimizes a continuous-density meta-optic front-end for frozen-model recognition using differentiable image formation and adjoint-gradient updates of Maxwell-based simulations. CODA directly optimizes the cross-entropy loss of a fixed zero-shot CLIP classifier without learned reconstruction, image signal processing, or image-fidelity auxiliary objectives. In a two-dimensional simulated imaging benchmark on ImageNet-100, CODA improves CLIP ViT-L/14 zero-shot accuracy from 53.75 $\pm$ 3.57$\%$ with a focal-concentration baseline to 65.41 $\pm$ 3.99$\%$. The optimized optics further transfer without re-optimization across CLIP, SigLIP, and DINOv2 on ImageNet-100, CIFAR-100, and Food-101. These results demonstrate that, under constrained meta-optic imaging, downstream recognition can be improved by aligning optical design with frozen vision-model objectives rather than conventional image-formation criteria.

---


### 31. [GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies](https://arxiv.org/abs/2606.27650)

**<font color=#1a73e8>作者：</font>** Gen Li, Jieyuan Lan, Pengcheng Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-agent simulation faces a joint grounding and scaling problem: agents should act in environments that reflect real urban constraints, yet direct online LLM calls for city-scale populations are computationally prohibitive. We present GenWorld, an empirically grounded urban simulation infrastructure that combines a building-level synthetic city, a structured agent-environment interface, and offline compilation of LLM-derived decision signals into lookup policies for scalable rollout. In a reference instantiation for Higashihiroshima, Japan, GenWorld grounds 196,608 synthetic residents in census and geospatial data, validates demographic consistency against census tabulations, and uses YJMob100K mobile-phone data as a commuting-distance diagnostic. We demonstrate the infrastructure through three reproducible cases: a full-city weekday rollout, a weekday-weekend behavioral contrast, and a warning-response perturbation with auditable replanning traces. These cases support GenWorld as a reproducible platform for grounded and scalable LLM-agent studies, while calibrated forecasting for traffic, evacuation, or policy outcomes remains future work.

---


### 32. [MER-R1: Multimodal Emotion Reasoning via Slow-Fast Thinking Synergy](https://arxiv.org/abs/2606.27652)

**<font color=#1a73e8>作者：</font>** Zhiyuan Han, Beier Zhu, Wenwen Tong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We find that explicit reasoning does not necessarily translate into better multimodal emotion recognition (MER) accuracy, even though it makes predictions more interpretable. Specifically, for reasoning-based MLLMs, fast thinking by triggering direct answers often outperforms slow thinking after deliberative reasoning. Our empirical analyses show that fast thinking improves recall with broader and more confident predictions, whereas slow thinking favors precision through conservative filtering of incorrect categories. Building on these insights, we propose MER-R1, a reinforcement learning framework that turns slow-fast complementarity into explicit optimization. Dual-objective disentanglement separates recall and precision into two optimization signals, allowing them to be jointly optimized rather than traded off against each other. Slow-fast confidence calibration further aligns the final slow-thinking answer with fast-thinking intuition, strengthening correct emotions while suppressing incorrect ones. In this way, MER-R1 unifies the recall-oriented intuition of fast thinking with the precision-oriented selectivity of slow thinking. We further provide theoretical justification for this synergy, showing that it mitigates variance-induced interference during optimization. Extensive experiments on MER-UniBench and MME-Emotion show that MER-R1 achieves state-of-the-art performance and makes reasoning genuinely benefit emotion recognition.

---


### 33. [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)

**<font color=#1a73e8>作者：</font>** Nan Yang, Zhanwen Liu, Linfeng Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings. Existing token pruning methods employ fixed pruning rate allocation and static importance metrics, ignoring dynamic inter-view importance differences and the evolving information importance during inference. Our analysis reveals that multi-view VLMs inherently encode task-related view priors in deeper layers and exhibit dynamic information requirements. Motivated by these findings, we propose MVPruner, a two-stage adaptive token pruning method that aligns pruning behavior with the model's dynamic information requirements. The first stage allocates pruning budgets based on the information diversity of each view, and retains tokens with consistent contribution across stages, ensuring semantic representational capacity. The second stage allocates budgets and selects tokens guided by instruction text to guarantee task alignment. Experimental results on four benchmarks demonstrate the superior performance of our method. For example, DriveMM equipped with MVPruner achieves 87.3% reduction in FLOPs, 4.97* speedup in prefilling phase while retaining 98.5% accuracy on DriveLM benchmark.

---


### 34. [Are Time-Series Foundation Models Ready for E-Nose Data? An Empirical Assessment of Their Embeddings](https://arxiv.org/abs/2606.27672)

**<font color=#1a73e8>作者：</font>** Taeyeong Choi, Mohammed Kamruzzaman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inspired by advances in natural language processing and computer vision, "time-series foundation models" (TSFMs) have recently been introduced with the promise of strong generalization across diverse time-series tasks, including forecasting, classification, and anomaly detection, as well as across domains such as healthcare, climate science, and manufacturing. However, their utility for gas-sensing data remains largely unexplored. To address this gap, this paper systematically evaluates recent TSFMs on electronic nose (E-Nose) data. In particular, we investigate whether embeddings produced by representative TSFMs, including Chronos-2 and MOMENT, provide effective representations for gas identification and concentration prediction. Specifically, we show that fine-tuning is necessary to achieve satisfactory performance on E-Nose data, and fusing TSFM embeddings with representations learned by specialized predictive models can further improve the performance, suggesting both the potential and limitations of current TSFMs for gas-sensing applications.

---


### 35. [From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models](https://arxiv.org/abs/2606.27679)

**<font color=#1a73e8>作者：</font>** Ponhvoan Srey, Xiaobao Wu, Cong-Duy Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probe-based uncertainty estimation (UE) has emerged as a prominent approach to detect hallucinations in Large Language Models (LLMs) by learning uncertainty from internal model signals. Yet, recent methods vary simultaneously across feature design, training data construction, and evaluation setting, obscuring what actually drives performance. To address this issue, we propose a factorised study of probe-based UE under matched conditions. Our results show that raw hidden states and attention features are difficult to outperform in-domain. However, under distribution shift, structured and compressed features are more robust, suggesting that in-domain performance alone is insufficient to measure progress. Furthermore, prompting and label construction significantly affect probe behaviour. Building on these best-practice findings, we train benchmark-based pretrained probes that transfer reasonably well to open-ended factual generation, providing a stable off-the-shelf baseline. Our work encourages more deployment-oriented evaluation of probe-based uncertainty estimators. The code repository is available at this https URL.

---


### 36. [Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation](https://arxiv.org/abs/2606.27681)

**<font color=#1a73e8>作者：</font>** Xiang Gao, Kaiwen Dong, Yuguang Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models in partially observed environments rely on latent representations that summarize interaction history, but in many modern LLM-based architectures predictive performance fails to reflect representation quality due to history bypass, rendering the latent state unidentifiable. Strict latent state mediation, requiring predictions to depend only on the latent state and action, is a classical principle that resolves this, but enforcing it in text-based settings is an open challenge: textual latent states are discrete and non-differentiable, precluding variational training, and expressive LLM decoders readily ignore the bottleneck. We show how to make strict mediation work in the text domain. We formalize why it is necessary, showing that strict mediation makes representation quality empirically testable while history-leaky architectures break this connection. We then introduce textual latent states, which are discrete, interpretable, and variable-length, and factorized GRPO (fGRPO), a tree-structured reinforcement learning method that enforces strict mediation during training. Experiments on TextWorld and ScienceWorld show preserved one-step prediction accuracy alongside up to 57\% gains in representation quality and 98\% improvements in rollout performance, increasing with task complexity and horizon.

---


### 37. [CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence](https://arxiv.org/abs/2606.27683)

**<font color=#1a73e8>作者：</font>** Zhiqiang Xie, Yijing Lin, Zhipeng Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge devices increasingly invoke large language models (LLMs) through API services for context aware edge intelligence, while edge generated data may be collected to improve LLMs and may introduce sensitive, copyrighted, harmful, or outdated information into model behavior. Machine unlearning offers a practical way to remove the influence of undesired data without retraining LLMs. However, existing methods still face two gaps. The first is API only black box access, where target model parameters and internal logits are unavailable. The second is how to preserve retained utility when unlearning target data and retained data share highly similar prompt structures or semantic patterns. To address these challenges, we propose Controlled Behavioral Divergence (CBD), an API only black box unlearning framework. CBD uses two auxiliary models to create controlled behavioral divergence between retained inputs and unlearning target inputs, converts this divergence into an unlearning relevance score, and routes unlearning related prompts away from the target LLM. To improve discrimination accuracy under high similarity between target and retained data, CBD constructs a gradient statistics based discriminative basis by estimating empirical Fisher matrices and solving a regularized generalized eigenvalue problem, guiding the unlearning signal toward target specific information rather than shared prompt structures. Compared with eleven white box and gray box unlearning baselines, CBD achieves a better unlearning utility trade off and its performance varies little across settings. On ToFU forget10, CBD approaches the retrained reference on the forget set while raising model utility to 74.90, about 15% above the second best baseline. On WMDP, it lowers hazardous knowledge accuracy to 25.68, near random guessing, while preserving MMLU accuracy of 52.67. Code is at this https URL.

---


### 38. [Mitigating LLM-based p-Hacking by Preregistering for the Next LLM](https://arxiv.org/abs/2606.27687)

**<font color=#1a73e8>作者：</font>** Maria Thomas, Kristina Gligoric, Nihar B. Shah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate, classify, and annotate data whose outputs feed downstream hypothesis tests. However, LLM-based research is easy to p-hack: a researcher can tune the prompts, decoding parameters, or output format until a desired result is reached. We propose a protocol to mitigate p-hacking in LLM-based research: preregistering the experiment and eligible models, and then running it on the first eligible LLM that is released after the preregistration. The researcher finalizes the procedure on current models, preregisters the analysis plan together with a set of eligible future models, and runs the confirmatory analysis on the first eligible model released afterward. Because this model does not exist at commitment time, it cannot be hacked against; furthermore, configurations that hack one model frequently do not transfer to the next. We evaluate the protocol on two tasks whose true values are known. Across 20 models from four providers and 11 LLM-analysis configurations, the protocol would have blocked successful transfer of the p-hack in 73.9% and 72.7% of cases in the two tasks. Additional analyses reveal that mitigation remains substantial under several stress tests. Finally, putting money where our mouth is, we followed our own protocol and preregistered our experiment. The preregistered experiment confirmed the protocol's effectiveness: out of the 7 configurations that hacked the prior model, the hacking failed to carry over in 6 configurations on the first eligible model released afterward.

---


### 39. [Mitigating Position Bias in Transformers via Layer-Specific Positional Embedding Scaling](https://arxiv.org/abs/2606.27705)

**<font color=#1a73e8>作者：</font>** Changze Lv, Zhenghua Wang, Yiran Ding 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) still struggle with the ``lost-in-the-middle'' problem, where critical information located in the middle of long-context inputs is often underrepresented or lost. While existing methods attempt to address this by combining multi-scale rotary position embeddings (RoPE), they typically suffer from high latency or rely on suboptimal hand-crafted scaling strategies. To overcome these limitations, we introduce a layer-specific positional embedding scaling~(LPES) method that assigns distinct scaling factors to each layer. LPES achieves a more balanced attention distribution without fine-tuning model parameters or increasing inference delay. A specially designed genetic algorithm is employed to efficiently select the optimal scaling factors for each layer by incorporating Bézier curves to significantly reduce the search space. Extensive experiments demonstrate that LPES effectively mitigates positional attention bias and delivers consistent improvements across multiple long-context benchmarks, yielding up to an $11.2$\% accuracy gain on the key-value retrieval dataset.

---


### 40. [ZooClaw-FashionSigLIP2: Distilled Fine-tuning for Robust Fashion Retrieval](https://arxiv.org/abs/2606.27708)

**<font color=#1a73e8>作者：</font>** Siqiao Xue, Chunxue Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting a foundation vision-language encoder to a specialized retrieval task creates a fundamental tradeoff: gains on the target distribution come at the cost of the foundation model's broad generalization, and fashion retrieval is a stringent instance of this problem. We present ZooClaw-FashionSigLIP2, a fashion-specialized SigLIP2-base model that resolves this tradeoff with a simple recipe -- full fine-tuning with knowledge distillation on curated in-domain data, followed by \wiseft~\citep{wortsman2022wiseft} weight interpolation with the base model -- and outperforms LoRA, larger backbones (up to 1B parameters), and external training data. Under fair evaluation, ZooClaw-FashionSigLIP2 outperforms all baselines on every benchmark in our suite. In addition, we release ZooClaw-Fashion, a new high-quality fashion retrieval benchmark, and a systematic quality analysis of widely-used benchmarks that exposes and mitigates structural biases in their public ground truth. We open-source the model weights and all evaluation artifacts to facilitate future research.

---


### 41. [Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning](https://arxiv.org/abs/2606.27709)

**<font color=#1a73e8>作者：</font>** Austin MY Cheung, Yi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that fine-tuning large language models (LLMs) for social warmth degrades factual reliability and increases sycophancy. We investigate a related but distinct failure mode: warmth fine-tuning also weakens adversarial safety, making models more susceptible to jailbreaks and harmful output generation. We examine whether this reflects an inherent consequence of empathetic adaptation or an artifact of data construction. To address this, we introduce a persona-driven rewriting pipeline that conditions user turns on low agreeableness and pairs this with warm, de-escalating assistant responses. Across three experiments on four models, our approach reduces jailbreak susceptibility and harmful output rates relative to generic warmth fine-tuning baselines, while preserving conversational warmth. Representational probing provides suggestive evidence that this conditioning reduces the geometric alignment between warmth and compliance directions in latent space. These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective.

---


### 42. [Aurora: A Leverage-Aware Spectral Optimizer](https://arxiv.org/abs/2606.27715)

**<font color=#1a73e8>作者：</font>** Alec Dewulf, Dhruv Pai, Li Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that for tall matrix parameters, like projection matrices in the MLP layers, the Muon update can have row norms that are arbitrarily non-uniform. This can lead to a self-reinforcing feedback loop whereby neurons receive persistently small updates and eventually do not contribute meaningfully to network outputs. This problem is effectively mitigated by an additional row normalization step, but current methods do this in a way that moves the Muon update geometry away from the polar factor of the momentum matrix, which we find is undesirable. We propose Aurora, an optimizer that enforces row-uniformity of matrix parameter updates while respecting Muon's polar factor geometry. Aurora outperforms Muon in our pre-training experiments and, when combined with existing methods, achieves state-of-the-art performance among spectral optimizers on the optimizer track of the modded-nanoGPT speedrun. Additionally, we find that Aurora's empirical gains over Muon scale with the MLP expansion factor, suggesting that Aurora may allow for effective training of very wide MLP layers.

---


### 43. [Enhancing Numerical Prediction in LLMs via Smooth MMD Alignment](https://arxiv.org/abs/2606.27731)

**<font color=#1a73e8>作者：</font>** Zhuo Zuo, Li Yue, Wenhao Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite their strong general capabilities, large language models (LLMs) often remain unreliable when outputs must be numerically precise. A key reason is the training objective: standard cross-entropy treats numeric tokens as unstructured categories and ignores the metric structure of their values. We address this mismatch with Smooth Maximum Mean Discrepancy (SMMD), which builds on the classic MMD by incorporating value-distance kernels over numeric tokens and graph-based smoothness. With this kernel defined over a numeric sub-vocabulary, SMMD aligns the predicted numeric distribution to the target via kernel matching and smooths the prediction-target residual over the induced kernel graph to encourage local consistency. We evaluate SMMD on four numeric-target tasks: mathematical reasoning, arithmetic calculation, clock-time recognition, and chart question answering, across multiple open-weight LLM and VLM backbones. SMMD consistently improves accuracy over both cross-entropy and recent numeric-target losses; analyses show complementary effects between MMD and smoothness and underscore the importance of distance-based kernel design. Code is available at this https URL.

---


### 44. [SIFT: Self-Imagination Fine-Tuning for Physically Plausible Motion in Video Diffusion Models](https://arxiv.org/abs/2606.27741)

**<font color=#1a73e8>作者：</font>** Ruoyu Wang, Jialun Liu, Huayang Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video diffusion models have greatly improved visual fidelity, yet their generated motions often violate physical plausibility. We observe a common kinematic failure, "motion entanglement", the unintended coupling of independent motion sources, such as camera movement and object motion. We identify that this issue stems from data bias and the reconstruction-based training design of diffusion models. Training on noisy videos that still retain coarse motion cues inadvertently encourages the model to replicate existing motion without an incentive to learn how to model kinematically-grounded motions. To address this, we propose a Self-Imagination Fine-Tuning (SIFT) paradigm, which enables the model to learn from its own generated videos rather than directly reconstructing real ones, breaking the reconstruction shortcut. We further employ motion-aware discriminative supervision and a progressive hard-case replay strategy to stabilize and accelerate learning. By leveraging freely-generated text prompts, our method can densely cover a broad motion space, including rare or finely-disentangled scenarios that would be costly to collect as video data. Extensive experiments demonstrate that our approach substantially improves the physical realism, motion disentanglement, and controllability of generated videos.

---


### 45. [Panoramic Scene Analysis: A Survey from Distortion-Aware Engineering to Sphere-Native Foundation Modeling](https://arxiv.org/abs/2606.27745)

**<font color=#1a73e8>作者：</font>** Qinfeng Zhu, Lei Fan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic images capture the complete visual sphere in a single frame, providing spatial context unattainable by conventional cameras. Yet this completeness comes at a geometric cost: the 2-sphere cannot be faithfully mapped to the plane, and every planar representation introduces distortions that violate the assumptions underlying standard vision architectures. This survey traces the evolution of panoramic scene analysis along a methodological trajectory, from projection-based adaptation, through distortion-aware engineering, to sphere-native modeling and geometry-aware tokenization for foundation models, and argues that this evolution reflects a progressive deepening of geometric commitment rather than a simple accumulation of techniques. We organize the literature along two orthogonal dimensions: architectural design (how operators interact with spherical geometry) and training paradigm (how knowledge is transferred across domains). Covering dense prediction (semantic segmentation, depth estimation, and room layout estimation), unified multi-task understanding, open-world perception, vision-language reasoning, and dynamic video analysis, we identify a central unresolved tension: among the methods surveyed, none simultaneously delivers strict spherical equivariance and full reuse of perspective-pretrained foundation-model weights, and we argue that this is a structural rather than incidental gap. We further expose five systematic gaps in current evaluation protocols, namely the absence of spherical-area-weighted metrics, seam-consistency testing, polar-robustness stratification, cross-projection generalization, and open-world protocol standardization, and propose a six-point research roadmap toward general-purpose panoramic intelligence. The corresponding repository is publicly available at: this https URL.

---


### 46. [Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework](https://arxiv.org/abs/2606.27757)

**<font color=#1a73e8>作者：</font>** Jiajing Zhang, Jiamei Jiang, Chenyang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have attracted widespread attention from academia and industry, yet their deployment raises critical security concerns regarding robustness and reliability. Planning, a core component of intelligent behavior, remains challenging for LLMs, which often produce infeasible or incorrect solutions in long-horizon decision-making tasks due to inherent complexity. In this paper, we propose a symbolic feedback-driven iterative self-refinement framework to enhance the robustness and reliability of LLMs in long-horizon planning. Specifically, a natural language prompting mechanism is introduced to map logical symbols into natural language descriptions, enabling LLMs to better capture task constraints and semantics. We further design a symbolic verifier that identifies errors and converts them into corrective instructions interpretable by the LLM, thereby guiding self-refinement. In addition, we leverage a plan recognizer to infer goal reachability, facilitating more effective guidance toward desired goals. Empirical results demonstrate that the proposed framework consistently improves both feasibility and correctness in long-horizon planning tasks. This highlights its effectiveness in enhancing the reliability of LLM-based planning and potential to enable more trustworthy AI systems.

---


### 47. [NormGuard: Reward-Preserving Norm Constraints in Flow-Matching Reinforcement Learning](https://arxiv.org/abs/2606.27771)

**<font color=#1a73e8>作者：</font>** Tianlin Pan, Lianyu Pang, Cheng Da 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training improves the reward alignment of flow-based generators, but often degrades perceptual quality in ways that are not captured by the reward proxy. We identify a simple structural signature of this drift: across three post-training methods (NFT, AWM, DPO), RL fine-tuning inflates the per-step velocity norm $\|v_\theta\|$ by $5\%$ to $15\%$ relative to the reference. A form of norm inflation has been studied in classifier-free guidance (CFG), where rescaling the velocity back to a reference norm at inference time can mitigate the resulting artifacts. However, this inference-time correction does not transfer cleanly to RL: rescaling $v_\theta$ to match $\|v_{\text{ref}}\|$ at inference time neither improves reward nor fixes the quality degradation, because the inflation is co-adapted into the model weights. Furthermore, an adjoint sensitivity analysis shows that velocity magnitude rescaling carries no coherent first-order reward signal at the batch level, indicating that suppressing norm inflation is unlikely to remove a consistently reward-carrying component. Since inference-time renormalization fails while norm suppression carries no reward cost, training-time intervention is the appropriate strategy. Together, these findings motivate \methodname, a hinge penalty that activates only when $\|v_\theta\|$ exceeds $\|v_{\text{ref}}\|$ and composes additively with any velocity-local base loss. Across two base models, three post-training methods, and two reward proxies, \methodname consistently improves MLLM-judged image quality and forensic realism while preserving reward, with gains that amplify under few-step inference and are not explained by early stopping.

---


### 48. [Understanding Rollout Error in Graph World Models](https://arxiv.org/abs/2606.27780)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Zekun Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are often used for planning by rolling learned dynamics forward. Many planning environments, however, are not vectors or images; they are graphs of agents, tools, skills, routes, and dependencies. In these settings, a local prediction error may stay local or spread through the graph, and the failure mode changes again when edges are predicted rather than fixed. This paper studies long-horizon rollout error in Graph World Models (GWMs). We formulate a unified fixed-edge and dynamic-edge GWM framework with action nodes for node-, edge-, and graph-level decisions. We develop graph-valued rollout bounds that separate topology-induced amplification from model-induced amplification, and we introduce a joint node-edge operator for dynamic-edge rollouts. Guided by the analysis, we propose Error-Aware GWM, which combines spectral regularization, rollout consistency, and critical-node weighting. Across synthetic topologies and heterogeneous agent-graph testbeds, rollout error and planning regret grow with horizon, dynamic-edge training is needed when structure evolves, and Error-Aware GWM prevents long-horizon divergence while preserving prediction accuracy. Real-world graph benchmarks clarify the scope of GWMs: they are most useful for dynamic graph rollout and agent planning, while specialized graph models remain strong on static or sparse prediction tasks.

---


### 49. [Output-Space Allocation Costs for Calibration-Guided LLM Compression: An Empirical Study](https://arxiv.org/abs/2606.27785)

**<font color=#1a73e8>作者：</font>** Qiong Tang, Xiangkun Hu, Xiangyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training-free compression methods for large language models (LLMs) often use calibration data to guide compression decisions. ROCKET, a recent method combining sparse-dictionary factorization with multi-choice knapsack problem (MCKP) allocation, derives its per-layer factorization from an output reconstruction objective but uses weight-space Frobenius error as the MCKP allocation cost. We investigate whether aligning the allocation cost with the output-space objective improves compressed model fidelity. On Qwen3-8B at 50\% compression, our ROCKET-ActCost achieves +0.8 percentage points higher average accuracy across 8 zero-shot benchmarks (53.1\% vs 52.3\%), but increases WikiText perplexity by 16\% (61.46 vs 52.98). This accuracy-perplexity tradeoff reveals that different allocation objectives favor different downstream metrics. The high correlation ($>$0.99) between weight-space and output-space errors limits allocation divergence, explaining the modest effect size. On Llama-3.2-1B at 20\% compression, the two methods produce near-identical results (53.3\% vs 53.5\% accuracy, 14.45 vs 14.66 PPL), suggesting that the effect of the cost function is minor at lower compression ratios.

---


### 50. [SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict Mitigation in Retrieval-Augmented Generation](https://arxiv.org/abs/2606.27786)

**<font color=#1a73e8>作者：</font>** Ruochang Li, Pengcheng Huang, Zhenghao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) enhances LLMs by incorporating external knowledge to support response generation. However, conflicts between retrieved context and parametric knowledge have emerged as a critical challenge in RAG systems. To mitigate such conflicts, numerous studies have attempted to identify and edit knowledge-related internal neurons, aiming to improve the ability of LLMs to rely on contextual evidence during generation. However, these neuron-level approaches may introduce unintended cascading effects that compromise the general capabilities of LLMs, as the modified neurons are often entangled with broader model behaviors and functionalities. In this paper, we introduce SHIFT, a novel framework that reformulates neuron-level modification as learnable gate modulation, allowing LLMs to adaptively regulate internal activations for knowledge conflict resolution. Technically, our SHIFT equips LLMs with a lightweight gate module and optimizes fewer than 0.01% trainable parameters while keeping the backbone model frozen. During generation, the gate module adjusts the model's internal representations to adaptively leverage contextual and parametric knowledge. Extensive experiments on six datasets validate the effectiveness of our SHIFT in comparison with various competing baselines. All datasets and code are available at this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-84](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
