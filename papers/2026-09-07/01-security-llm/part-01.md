# 🔐 大模型安全相关研究 | 2026年09月07日

> 本类共 **4** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [AlcaTRAz - Anchored Tree-Rule Defense Against Jailbreaks](https://arxiv.org/abs/2609.03693)

**<font color=#1a73e8>作者：</font>** Jakub Reš, Petr Kaška, Martin Perešíni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are vulnerable to jailbreak attacks that bypass safety alignment through carefully crafted prompts. Many existing defenses require access to model weights or internals, making them difficult to apply to black-box deployments. We propose AlcaTRAz (Anchored Tree-Rule defense Against jailbreaks), a prompt-level defense based on rule trees that operates exclusively on the input text and requires no modification or retraining of the target model. The method automatically learns a transferable transformation rule that inserts controlled character-level perturbations at selected positions, thereby disrupting structural regularities exploited by jailbreak attacks while largely preserving the model's utility on benign queries. We evaluate the proposed method across 33 open-weight models, 22 jailbreak attack types, and a benchmark of short, single-turn benign questions, comparing against three representative prompt-level baselines (Llama Guard, RA-LLM, Goal Prioritization). Among the compared defenses, AlcaTRAz achieves the best composite security and functionality score in 73.4 % of model-attack combinations and shifts the aggregate score from a modal value of 10 (maximal-severity response to the malicious request) in the undefended setting to a modal value of 2 (near-refusal) after defense, while keeping the mean benign score within 0.27 points of the undefended baseline (8.35 vs. 8.62 on a 0-10 scale). AlcaTRAz substantially reduces but does not eliminate jailbreak success: a high-severity tail remains, and we do not consider adaptive attackers, so we position it as one layer within a defense-in-depth strategy rather than a standalone guarantee.

---


### 2. [IndicSafeEval: Safety Robustness of Large Language Models under Multilingual Persuasive Jailbreak Attacks](https://arxiv.org/abs/2609.03781)

**<font color=#1a73e8>作者：</font>** Saikat Mondal, Mamta, Deeksha Varshney 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in multilingual settings, yet their safety is still evaluated primarily in English. This limits our understanding of how alignment failures manifest in low-resource and culturally diverse languages. We introduce IndicSafeEval, a persuasion-based jailbreak evaluation framework for Indian languages. Our benchmark combines ten safety critical content categories with six human-like persuasive strategies across four different Indian languages, such as Hindi, Bengali, Marathi and Punjabi, resulting in 7,200 adversarial prompts. We conduct a systematic black-box evaluation of several open-source LLMs to examine how their safety behaviour varies across languages, persuasion strategies, and risk categories. Our analysis shows that the model does not behave equally safely across all languages and prompt styles. Instead, safety performance depends strongly on both the languages used and the way a request is phrased using persuasive cues. We further observe that different risk categories exhibit different levels of vulnerability, with some types of harmful content being significantly more susceptible to persuasion-based jailbreaks than others. These findings reveal important limitations of current safety evaluations, which are largely English-centric, and underscore the need for multilingual and persuasion-aware benchmarking frameworks to more accurately assess real-world LLM safety. Our implementation is available at this https URL. Warning: this paper contains example data that may be offensive or harmful.

---


### 3. [Flip, Don't Shuffle: Watermarking LLMs at the Speed of Inference](https://arxiv.org/abs/2609.03844)

**<font color=#1a73e8>作者：</font>** Simone Ceppi, Ignacio Sanchez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce Stateless Bernoulli Watermarking (SBW), a new statistical watermark for Large Language Models that determines green list membership through independent per-token Bernoulli trials. Unlike KGW's vocabulary permutation or SynthID's multi-layer tournament, SBW requires only a single comparison per token against a counter-based random number generator, reducing membership complexity to $O(1)$ and enabling single-kernel execution with zero intermediate allocations. We prove that this formulation preserves the same detection guarantees as fixed-size green lists: the z-score test remains $\mathcal{N}(0,1)$ under the null. The stateless architecture enables capabilities unavailable to existing methods: full-vocabulary self-salt watermarking (over 6000$\times$ faster than KGW's self-salt and 2$\times$ faster than SynthID despite biasing the entire vocabulary with candidate-dependent seeding) and architectural compatibility with distributed inference. In end-to-end generation benchmarks, SBW adds less than 1\% overhead at all batch sizes. We additionally identify hash function design as a previously unexplored axis for watermark quality, showing that a GPU-native Jenkins hash improves null calibration by 1.8$\times$ while producing more diverse text. Experiments across two seeding schemes and eight $(\gamma, \delta)$ configurations confirm statistical equivalence with ROC-AUC differences below 0.01.

---


### 4. [A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors](https://arxiv.org/abs/2609.03884)

**<font color=#1a73e8>作者：</font>** Pengxun Li, Litian Zhang, Jianwei Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern AI agent harnesses expose lifecycle hooks that bind shell commands to runtime events such as session start, tool calls, and file edits. These commands run with host privileges yet ship as lifecycle-hook configuration and may fire at times the LLM never observes. We identify the lifecycle-hook update path, which harnesses trust blindly, as a new attack surface. Under a supply-chain threat model in which an attacker controls only plugin metadata and lifecycle-hook configuration, a benign versioned plugin can be trojanized by an update that silently binds attacker-chosen commands to benign events, yielding malicious host-side behavior such as privilege escalation. We propose HookPry, an open-source and fully automated attack framework that systematically exploits this vulnerability across heterogeneous AI agent harnesses. HookPry realizes ten attack objectives; across 25 combinations of harnesses and backends in 1,000 end-to-end runs, it compromises all seven evaluated harnesses, with per-harness success rates reaching 92.5%. Representative defenses remain insufficient: Microsoft Defender has 0% recall, and the union of three static defenses misses 47.5% of malicious artifacts.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
